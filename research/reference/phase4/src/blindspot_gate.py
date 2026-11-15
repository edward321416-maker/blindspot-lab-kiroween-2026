"""Research-grade, fail-closed detector A/B regression gate.

Does not run models or assert that supplied ground truth is independently human verified.
Never load untrusted pickle/joblib artifacts. Inputs are JSON data only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

VALID_VERDICTS = {"PASS_BOTH", "FIXED", "NEW_REGRESSION", "FAIL_BOTH", "ABSTAIN_ORACLE"}
HEX = frozenset("0123456789abcdef")


class InputError(ValueError):
    pass


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_hash(v: object) -> bool:
    return isinstance(v, str) and len(v) == 64 and all(c in HEX for c in v)


def bbox_valid(v: object) -> bool:
    return (isinstance(v, list) and len(v) == 4 and
            all(type(a) in (int, float) and math.isfinite(a) for a in v) and
            v[2] > v[0] and v[3] > v[1])


def iou(a: list[float], b: list[float]) -> float:
    x0, y0 = max(a[0], b[0]), max(a[1], b[1])
    x1, y1 = min(a[2], b[2]), min(a[3], b[3])
    intersection = max(0.0, x1 - x0) * max(0.0, y1 - y0)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return intersection / (area_a + area_b - intersection)


def correct(row: dict, name: str, min_iou: float) -> bool:
    pred = row[name]
    if not isinstance(pred, dict) or type(pred.get("present")) is not bool:
        raise InputError(f"{row.get('case_id')}: invalid {name} prediction")
    score = pred.get("score")
    if type(score) not in (int, float) or not math.isfinite(score):
        raise InputError(f"{row.get('case_id')}: invalid {name} score")
    bb = pred.get("bbox")
    if bb is not None and not bbox_valid(bb):
        raise InputError(f"{row.get('case_id')}: invalid {name} box")
    if not row["positive"]:
        return not pred["present"]
    return bool(pred["present"] and bb is not None and iou(row["gt"], bb) >= min_iou)


def classify(valid: bool, a: bool, b: bool) -> str:
    if not valid:
        return "ABSTAIN_ORACLE"
    return ("PASS_BOTH" if a and b else "FIXED" if not a and b else
            "NEW_REGRESSION" if a and not b else "FAIL_BOTH")


def verify_reviews(rows: list[dict], reviews: list[dict] | None) -> dict:
    """Syntactic quorum validation, never authenticates real reviewer identity."""
    if reviews is None:
        return {"reviewed": 0, "quorum_passed": 0, "conflict": 0, "missing": sum(r.get("oracle_status") == "VALID" for r in rows), "authenticated": False}
    ids = {r["case_id"] for r in rows if r["oracle_status"] == "VALID"}
    ledger = defaultdict(list)
    for note in reviews:
        if not isinstance(note, dict) or note.get("case_id") not in ids:
            raise InputError("Review for unknown, invalid or abstained case")
        rid = note.get("reviewer_id")
        if not isinstance(rid, str) or not rid.strip() or note.get("decision") not in {"ACCEPT", "REJECT"}:
            raise InputError("Incomplete review record")
        if note.get("decision") == "ACCEPT" and not bbox_valid(note.get("bbox")) and note.get("bbox") is not None:
            raise InputError("Invalid reviewer bounding box")
        ledger[note["case_id"]].append(note)
    quorum, conflict = 0, 0
    for row in rows:
        if row["case_id"] not in ids:
            continue
        notes = ledger[row["case_id"]]
        if len({n["reviewer_id"] for n in notes}) != len(notes):
            raise InputError("Duplicate reviewer for same case")
        if len(notes) >= 2:
            # All independent review entries must agree on decision and bounding box.
            decisions = {(n["decision"], tuple(n.get("bbox") or [])) for n in notes}
            if len(decisions) == 1 and next(iter(decisions))[0] == "ACCEPT":
                if tuple(notes[0].get("bbox") or []) == tuple(row.get("gt") or []):
                    quorum += 1
                else:
                    conflict += 1
            else:
                conflict += 1
    return {"reviewed": len(ledger), "quorum_passed": quorum, "conflict": conflict,
            "missing": len(ids)-quorum-conflict, "authenticated": False}


def evaluate(rows: object, *, min_iou: float = .45,
             source_class: str = "synthetic_provenance", reviews: list[dict] | None = None) -> tuple[dict, list[dict]]:
    if not isinstance(rows, list) or not rows or not 0 < min_iou <= 1:
        raise InputError("Empty/invalid cases or IoU policy")
    if source_class not in {"synthetic_provenance", "real_attested"}:
        raise InputError("Unrecognized provenance type")
    out, seen = [], set()
    for row in rows:
        if not isinstance(row, dict):
            raise InputError("Non-object case")
        cid = row.get("case_id")
        if not isinstance(cid, str) or not cid or cid in seen:
            raise InputError(f"Invalid or duplicate case id: {cid}")
        seen.add(cid)
        if type(row.get("positive")) is not bool or row.get("oracle_status") not in {"VALID", "ABSTAIN"}:
            raise InputError(f"{cid}: invalid ground truth status")
        if row["positive"] != (row.get("gt") is not None):
            raise InputError(f"{cid}: positive/ground-truth mismatch")
        if row["positive"] and not bbox_valid(row["gt"]):
            raise InputError(f"{cid}: invalid ground-truth bbox")
        for key in ("image_hash", "mask_hash"):
            if not is_hash(row.get(key)):
                raise InputError(f"{cid}: missing/invalid {key}")
        sev = row.get("severity")
        if type(sev) not in (int, float) or not math.isfinite(sev) or not 0 <= sev <= 1:
            raise InputError(f"{cid}: invalid severity")
        a = correct(row, "A", min_iou)
        b = correct(row, "B", min_iou)
        v = classify(row["oracle_status"] == "VALID", a, b)
        if v not in VALID_VERDICTS or v != row.get("verdict"):
            raise InputError(f"{cid}: stored verdict/correctness does not match independently recomputed result")
        if row["oracle_status"] == "ABSTAIN":
            if row.get("correct_A") is not None or row.get("correct_B") is not None:
                raise InputError(f"{cid}: abstained case cannot claim labeled accuracy")
        elif (type(row.get("correct_A")) is not bool or type(row.get("correct_B")) is not bool or
              row["correct_A"] != a or row["correct_B"] != b):
            raise InputError(f"{cid}: stored verdict/correctness does not match independently recomputed result")
        stored_diff = row.get("correct_diff")
        if row["oracle_status"] == "ABSTAIN":
            if stored_diff is not None:
                raise InputError(f"{cid}: abstained case cannot claim accuracy delta")
        elif (type(stored_diff) not in (int, float) or stored_diff != int(b) - int(a)):
            raise InputError(f"{cid}: inconsistent stored correctness delta")
        out.append({"case_id":cid,"scene_id":row.get("scene_id"),"transform":row.get("transform"),"severity":sev,
                    "verdict":v,"a_correct":a,"b_correct":b,"oracle":row["oracle_status"],"image_sha256":row["image_hash"]})
    counts = Counter(x["verdict"] for x in out)
    valid = len(rows)-counts["ABSTAIN_ORACLE"]
    a_hits = sum(x["a_correct"] for x in out if x["oracle"] == "VALID")
    b_hits = sum(x["b_correct"] for x in out if x["oracle"] == "VALID")
    cond = defaultdict(Counter)
    for x in out:
        cond[x["transform"]][x["verdict"]] += 1
    reviews_info = verify_reviews(rows, reviews)
    technical = "FAIL" if counts["NEW_REGRESSION"] else "PASS"
    # Human review claims are not authenticated by this offline research prototype.
    production = "BLOCKED_UNVERIFIED_ORACLE" if source_class != "real_attested" or reviews_info["quorum_passed"] != valid or not reviews_info["authenticated"] else technical
    result = {"case_count":len(rows),"valid":valid,"abstain":counts["ABSTAIN_ORACLE"],
              "verdict_counts":{v:counts[v] for v in sorted(VALID_VERDICTS)},
              "accuracy_A":round(a_hits/valid,8) if valid else None,
              "accuracy_B":round(b_hits/valid,8) if valid else None,
              "by_transform":{k:dict(sorted(v.items())) for k,v in sorted(cond.items())},
              "min_iou":min_iou,"source_class":source_class,"review_quorum":reviews_info,
              "technical_gate":technical,"production_approval":production,
              "limitation":"Only structured predictions recomputed; independent image-mask validation and authentic reviewer identity are not proven by this gate."}
    return result,out


def junit_xml(evaluated: list[dict]) -> bytes:
    root = ET.Element("testsuites")
    suite = ET.SubElement(root,"testsuite",name="blindspot_phase4_gate",tests=str(len(evaluated)),
                          failures=str(sum(x["verdict"]=="NEW_REGRESSION" for x in evaluated)),
                          skipped=str(sum(x["verdict"]=="ABSTAIN_ORACLE" for x in evaluated)))
    for case in evaluated:
        test = ET.SubElement(suite,"testcase",classname="detector_version_gate",name=case["case_id"])
        if case["verdict"]=="NEW_REGRESSION":
            ET.SubElement(test,"failure",message="new detector regression").text = case["image_sha256"]
        if case["verdict"]=="ABSTAIN_ORACLE":
            ET.SubElement(test,"skipped",message="oracle validity unverified")
    return ET.tostring(root,encoding="utf-8",xml_declaration=True)


def main(argv: list[str] | None = None) -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cases",required=True,type=Path)
    p.add_argument("--out",required=True,type=Path)
    p.add_argument("--expected-sha256",required=True,help="Trusted out-of-band SHA-256 of cases.json")
    p.add_argument("--min-iou",type=float,default=.45)
    p.add_argument("--source-class",choices=["synthetic_provenance","real_attested"],default="synthetic_provenance")
    p.add_argument("--reviews",type=Path,help="Optional independent-review record JSON (self-reported; no identity authentication)")
    p.add_argument("--mode",choices=["research","production"],default="research")
    args=p.parse_args(argv)
    if not is_hash(args.expected_sha256):
        print("INPUT_ERROR: bad trusted SHA-256",file=sys.stderr);return 2
    actual=sha256(args.cases)
    if actual != args.expected_sha256:
        print("INPUT_ERROR: case-file hash mismatch",file=sys.stderr);return 2
    try:
        rows=json.loads(args.cases.read_text(encoding="utf-8"))
        reviews=json.loads(args.reviews.read_text(encoding="utf-8")) if args.reviews else None
        result, evaluated=evaluate(rows,min_iou=args.min_iou,source_class=args.source_class,reviews=reviews)
    except (InputError, json.JSONDecodeError, UnicodeDecodeError, OSError) as ex:
        print(f"INPUT_ERROR: {ex}",file=sys.stderr);return 2
    result["cases_sha256"]=actual
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/"gate_verdict.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (args.out/"gate_junit.xml").write_bytes(junit_xml(evaluated))
    with (args.out/"gate_cases.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(evaluated[0]));w.writeheader();w.writerows(evaluated)
    print(json.dumps({"technical_gate":result["technical_gate"],"production_approval":result["production_approval"],
                      "cases":result["case_count"],"new_regressions":result["verdict_counts"]["NEW_REGRESSION"],
                      "out":str(args.out)},ensure_ascii=False))
    # Exit status can fail CI without treating a research benchmark as production assurance.
    if result["technical_gate"] == "FAIL": return 1
    if args.mode == "production" and result["production_approval"] != "PASS": return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
