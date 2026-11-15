import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from blindspot_gate import InputError, classify, evaluate, iou, junit_xml, main

ROOT=Path(__file__).resolve().parents[1]
CASES=json.loads((ROOT/"fixtures/cases.json").read_text())
EXPECTED="41bb878ea72dec1caf239bff272eba2a93a2ba793eb5188db25a9ee18d829828"


def test_reference_counts_and_gate():
    summary, items=evaluate(CASES)
    assert summary["case_count"]==728
    assert summary["valid"]==727
    assert summary["verdict_counts"]=={"ABSTAIN_ORACLE":1,"FAIL_BOTH":2,"FIXED":57,"NEW_REGRESSION":38,"PASS_BOTH":630}
    assert summary["technical_gate"]=="FAIL"
    assert summary["production_approval"]=="BLOCKED_UNVERIFIED_ORACLE"
    assert len(items)==728


def test_model_b_scores_not_trusted_as_oracle():
    rows=copy.deepcopy(CASES)
    rows[0]["correct_B"]=not rows[0]["correct_B"]
    with pytest.raises(InputError,match="stored verdict"):
        evaluate(rows)


def test_recomputed_iou_exposes_mutated_ground_truth():
    rows=copy.deepcopy(CASES)
    rows[0]["gt"]=[400,400,440,440]
    with pytest.raises(InputError,match="stored verdict"):
        evaluate(rows)


def test_duplicate_identifiers_rejected():
    rows=copy.deepcopy(CASES)
    rows[1]["case_id"]=rows[0]["case_id"]
    with pytest.raises(InputError,match="duplicate"):
        evaluate(rows)


def test_bad_hash_rejected(tmp_path):
    f=tmp_path/"cases.json";f.write_text(json.dumps(CASES))
    assert main(["--cases",str(f),"--out",str(tmp_path/"out"),"--expected-sha256",EXPECTED])==2


def test_abstention_does_not_become_pass():
    invalid=next(x for x in CASES if x["oracle_status"]=="ABSTAIN")
    res,items=evaluate([invalid])
    assert res["valid"]==0 and res["abstain"]==1
    assert items[0]["verdict"]=="ABSTAIN_ORACLE"
    assert res["production_approval"].startswith("BLOCKED")


def test_no_regressions_still_does_not_approve_synthetic():
    rows=copy.deepcopy(CASES)
    for x in rows:
        if x["verdict"]=="NEW_REGRESSION":
            x["B"]=copy.deepcopy(x["A"])
            x["correct_B"]=x["correct_A"]
            x["correct_diff"]=0
            x["verdict"]="PASS_BOTH"
    summary,_=evaluate(rows)
    assert summary["technical_gate"]=="PASS"
    assert summary["production_approval"]=="BLOCKED_UNVERIFIED_ORACLE"


def test_attested_reviews_do_not_fake_authentication():
    sample=next(x for x in CASES if x["oracle_status"]=="VALID")
    reviews=[{"case_id":sample["case_id"],"reviewer_id":k,"decision":"ACCEPT","bbox":sample["gt"]} for k in ("R1","R2")]
    s,_=evaluate([sample],source_class="real_attested",reviews=reviews)
    assert s["review_quorum"]["quorum_passed"]==1
    assert not s["review_quorum"]["authenticated"]
    assert s["production_approval"]=="BLOCKED_UNVERIFIED_ORACLE"


def test_conflicting_review_is_not_quorum():
    sample=next(x for x in CASES if x["oracle_status"]=="VALID")
    reviews=[{"case_id":sample["case_id"],"reviewer_id":"R1","decision":"ACCEPT","bbox":sample["gt"]},
             {"case_id":sample["case_id"],"reviewer_id":"R2","decision":"REJECT"}]
    s,_=evaluate([sample],source_class="real_attested",reviews=reviews)
    assert s["review_quorum"]["conflict"]==1 and s["review_quorum"]["quorum_passed"]==0


def test_unknown_source_rejected():
    with pytest.raises(InputError,match="provenance"):
        evaluate([CASES[0]],source_class="verified_by_magic")


def test_junit_exports_failures_and_skips():
    _,items=evaluate(CASES)
    x=junit_xml(items).decode()
    assert x.count("<failure ")==38 and x.count("<skipped ")==1


def test_iou_and_status_contract():
    assert iou([0,0,10,10],[0,0,10,10])==1
    assert iou([0,0,10,10],[11,11,12,12])==0
    assert classify(True,True,False)=="NEW_REGRESSION"
    assert classify(False,True,True)=="ABSTAIN_ORACLE"


def test_end_to_end_cli_expected_failure(tmp_path):
    rc=main(["--cases",str(ROOT/"fixtures/cases.json"),"--out",str(tmp_path),"--expected-sha256",EXPECTED])
    assert rc==1
    j=json.loads((tmp_path/"gate_verdict.json").read_text())
    assert j["verdict_counts"]["NEW_REGRESSION"]==38
    assert (tmp_path/"gate_cases.csv").exists() and (tmp_path/"gate_junit.xml").exists()


def test_model_confidence_nan_rejected():
    rows=copy.deepcopy(CASES)
    rows[0]["B"]["score"]=float('nan')
    with pytest.raises(InputError,match="invalid B score"):
        evaluate(rows)


def test_correctness_delta_tampering_rejected():
    rows=copy.deepcopy(CASES)
    rows[0]["correct_diff"]=42
    with pytest.raises(InputError,match="correctness delta"):
        evaluate(rows)


def test_duplicate_reviewer_identity_rejected():
    sample=next(x for x in CASES if x["oracle_status"]=="VALID")
    reviews=[{"case_id":sample["case_id"],"reviewer_id":"R1","decision":"ACCEPT","bbox":sample["gt"]},
             {"case_id":sample["case_id"],"reviewer_id":"R1","decision":"ACCEPT","bbox":sample["gt"]}]
    with pytest.raises(InputError,match="Duplicate reviewer"):
        evaluate([sample],source_class="real_attested",reviews=reviews)


def test_technical_pass_but_production_exit3(tmp_path):
    import hashlib
    rows=copy.deepcopy(CASES)
    for x in rows:
        if x["verdict"]=="NEW_REGRESSION":
            x["B"]=copy.deepcopy(x["A"])
            x["correct_B"]=x["correct_A"]
            x["correct_diff"]=0
            x["verdict"]="PASS_BOTH"
    case=tmp_path/"changed.json"
    case.write_text(json.dumps(rows))
    digest=hashlib.sha256(case.read_bytes()).hexdigest()
    out=tmp_path/"report"
    assert main(["--cases",str(case),"--out",str(out),"--expected-sha256",digest,"--mode","production"])==3
    verdict=json.loads((out/"gate_verdict.json").read_text())
    assert verdict["technical_gate"]=="PASS"
    assert verdict["production_approval"]=="BLOCKED_UNVERIFIED_ORACLE"


def test_negative_object_case_contract():
    sample=next(x for x in CASES if x["positive"] is False)
    s, items=evaluate([sample])
    assert s["valid"]==1 and items[0]["oracle"]=="VALID"
