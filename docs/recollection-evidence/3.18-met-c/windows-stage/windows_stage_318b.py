"""Re:Collection 3.18b: reproducible Windows staging validation of a pinned GitHub commit.

This module only acquires six public Python sources and runs local, isolated tests.
It never downloads Met original JSON/media, changes Kiro files, or uploads data.
Requires Python >= 3.11 and the standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = "edward321416-maker/blindspot-lab-kiroween-2026"
PINNED_COMMIT = "d344673599408732ce1400a22cafb798c6e760b4"
SOURCE_PREFIX = "docs/recollection-evidence/3.18-met-c"
SOURCE_EXPECTED = {
    "capture_met.py": (18528, "43a0743a5059f1309edbf8be67c676ce65993d52ee4ff85ca5136342cdfc21a2"),
    "collect_met_c.py": (8364, "2ee25274caef9c8cf02756eae752c993f3651a4e788683f850081bb8bea9d605"),
    "rights_policy.py": (4396, "b3e75856395a2c534bc77b4faed28099ac73e53ff1b38201555a826907c8d049"),
    "test_capture_met.py": (17354, "8edc5b14cf482722b7ed1afd6c1d7cfb7ac93bf746b6b397b4128acac367d46b"),
    "test_rights_policy.py": (4380, "65e97fc4e6346df7ee2eba262ca5ec8b0543240b9c96c1ec20a6cddcff9c07c2"),
    "test_independent_318b.py": (5493, "71085c42deec49ccb39162c8e24fd95840d716b754101fec190390809c8bd937"),
}
MAX_SOURCE_BYTES = 128 * 1024
DEFAULT_STAGE_NAME = "ReCollection_3_18b_Windows_STAGE_20261119"


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def hash_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def hash_file(path: Path) -> str:
    return hash_bytes(path.read_bytes())


def write_exclusive(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as out:
        out.write(content)
        out.flush()
        os.fsync(out.fileno())


def json_exclusive(path: Path, data: Any) -> None:
    write_exclusive(path, (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


class SameHostOnly(urllib.request.HTTPRedirectHandler):
    """Do not follow cross-host redirects for the pinned raw-code download."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        from urllib.parse import urlsplit
        if urlsplit(newurl).scheme != "https" or urlsplit(newurl).hostname != "raw.githubusercontent.com":
            raise RuntimeError("cross-host or insecure redirect blocked")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def load_public_source(name: str, offline_source: Path | None) -> bytes:
    if offline_source is not None:
        return (offline_source / name).read_bytes()
    url = f"https://raw.githubusercontent.com/{REPO}/{PINNED_COMMIT}/{SOURCE_PREFIX}/{name}"
    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ssl.create_default_context()), SameHostOnly()
    )
    request = urllib.request.Request(url, headers={"User-Agent": "ReCollection-318b-WindowsStage/1.0"})
    with opener.open(request, timeout=35) as response:
        if response.status != 200:
            raise RuntimeError(f"Pinned source HTTP status {response.status}")
        data = response.read(MAX_SOURCE_BYTES + 1)
    if len(data) > MAX_SOURCE_BYTES:
        raise RuntimeError("public source size limit exceeded")
    return data


def acquire_sources(stage: Path, offline_source: Path | None) -> dict[str, str]:
    src = stage / "src"
    src.mkdir()
    checked: dict[str, str] = {}
    for name, (size, digest) in SOURCE_EXPECTED.items():
        data = load_public_source(name, offline_source)
        if len(data) != size or hash_bytes(data) != digest:
            raise RuntimeError(f"PINNED_SOURCE_HASH_MISMATCH: {name}")
        write_exclusive(src / name, data)
        checked[name] = digest
    return checked


def copy_verified(stage: Path, destination: Path, names: tuple[str, ...]) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    for name in names:
        original = stage / "src" / name
        if hash_file(original) != SOURCE_EXPECTED[name][1]:
            raise RuntimeError(f"SRC_CHANGED: {name}")
        shutil.copyfile(original, destination / name)
        if hash_file(destination / name) != SOURCE_EXPECTED[name][1]:
            raise RuntimeError(f"COPY_MISMATCH: {name}")


def check_unittest_log(stderr: str, count: int) -> dict[str, Any]:
    normalized = stderr.replace("\r\n", "\n")
    cases = re.findall(r"^(test_[a-zA-Z0-9_]+) \(([^)]+)\) \.\.\. ok$", normalized, re.M)
    summary = re.search(rf"(?:^|\n)Ran {count} tests in [^\n]+\n\nOK\n?$", normalized)
    qualified = {f"{method}::{suite}" for method, suite in cases}
    return {"found_ok_cases": len(cases), "unique_cases": len(qualified), "summary_exact": summary is not None, "passed": len(cases) == count and len(qualified) == count and summary is not None}


def execute_70(stage: Path) -> dict[str, Any]:
    folder = stage / "runs" / "independent_70"
    copy_verified(stage, folder, tuple(SOURCE_EXPECTED))
    start = now_utc()
    command = [sys.executable, "-B", "-m", "unittest", "-v", "test_capture_met.py", "test_rights_policy.py", "test_independent_318b.py"]
    completed = subprocess.run(command, cwd=folder, capture_output=True, text=True, timeout=200, check=False)
    stop = now_utc()
    write_exclusive(stage / "results" / "unittest_70_stdout.txt", completed.stdout.encode("utf-8"))
    write_exclusive(stage / "results" / "unittest_70_stderr.txt", completed.stderr.encode("utf-8"))
    cases = check_unittest_log(completed.stderr, 70)
    hashes_after = {name: hash_file(folder / name) for name in SOURCE_EXPECTED}
    ok = completed.returncode == 0 and cases["passed"] and all(hashes_after[n] == v[1] for n,v in SOURCE_EXPECTED.items())
    return {"started_at_utc": start, "ended_at_utc": stop, "python_exit_code": completed.returncode, "tests": cases, "source_sha256_after": hashes_after, "passed": ok}


def execute_fresh_49(stage: Path) -> dict[str, Any]:
    folder = stage / "runs" / "fresh_49_code"
    copy_verified(stage, folder, ("capture_met.py", "test_capture_met.py", "collect_met_c.py"))
    private_root = stage / "runs" / "fresh_49_private"
    private_root.mkdir(parents=True, exist_ok=False)
    # The patched collector must run 49 cases on its own new, untrusted-free gate.
    # This command does NOT execute collect_met_c.main() or capture any museum data.
    snippet = (
        "import json; from pathlib import Path; from collect_met_c import run_integrity_gate; "
        "root=Path('..')/'fresh_49_private'; "
        "r=run_integrity_gate(root,root/'gate_report.json'); "
        "print(json.dumps(r)); raise SystemExit(0 if r.get('passed') else 30)"
    )
    start = now_utc()
    completed = subprocess.run([sys.executable, "-B", "-c", snippet], cwd=folder, capture_output=True, text=True, timeout=200, check=False)
    stop = now_utc()
    write_exclusive(stage / "results" / "gate_49_stdout.txt", completed.stdout.encode("utf-8"))
    write_exclusive(stage / "results" / "gate_49_stderr.txt", completed.stderr.encode("utf-8"))
    path = private_root / "gate_report.json"
    if not path.is_file():
        return {"started_at_utc": start, "ended_at_utc": stop, "python_exit_code": completed.returncode, "passed": False, "reason": "no new gate report"}
    report = json.loads(path.read_text(encoding="utf-8"))
    copied = {n: hash_file(folder / n) for n in ("capture_met.py", "test_capture_met.py", "collect_met_c.py")}
    ok = completed.returncode == 0 and report.get("passed") is True and report.get("exit_code") == 0 and all(copied[n] == SOURCE_EXPECTED[n][1] for n in copied)
    return {"started_at_utc": start, "ended_at_utc": stop, "python_exit_code": completed.returncode, "run_id": report.get("run_id"), "test_log_sha256": report.get("test_log_sha256"), "source_sha256_after": copied, "passed": ok}


def verify_security_behavior(stage: Path) -> dict[str, Any]:
    folder = stage / "runs" / "security_probes"
    copy_verified(stage, folder, ("capture_met.py", "collect_met_c.py", "rights_policy.py", "test_capture_met.py"))
    probe = r'''import json, tempfile
from pathlib import Path
from collect_met_c import run
from rights_policy import RightsSignals,evaluate_rights
with tempfile.TemporaryDirectory(prefix="recollection-fake-log-") as d:
    root=Path(d); fake=root/"fake_success.txt"
    fake.write_text("No tests were run here.\nRan 49 tests\nOK\n",encoding="utf-8")
    status, code=run(root,fake)
    assert code==30 and status["status"]=="HOLD" and len(status["captures"])==0
base=dict(api_public_domain=True,page_public_domain=True,primary_image_present=True,image_download_available=True,metadata_reviewed=True,authored_text_approved=True,image_display_approved=True)
for key,value in [("metadata_reviewed","false"),("authored_text_approved","false"),("image_display_approved","false"),("image_display_approved",1)]:
    item=dict(base); item[key]=value
    result=evaluate_rights(RightsSignals(**item))
    assert all(v["decision"]=="RIGHTS_REVIEW_HOLD" for v in result.values())
print(json.dumps({"forged_log_blocked":True,"invalid_rights_flags_blocked":4,"captures_created":0}))
'''
    completed = subprocess.run([sys.executable, "-B", "-c", probe], cwd=folder, capture_output=True, text=True, timeout=30, check=False)
    write_exclusive(stage / "results" / "adversarial_stdout.txt", completed.stdout.encode("utf-8"))
    write_exclusive(stage / "results" / "adversarial_stderr.txt", completed.stderr.encode("utf-8"))
    details = json.loads(completed.stdout) if completed.returncode == 0 else {}
    return {"python_exit_code": completed.returncode, "passed": completed.returncode == 0 and details.get("forged_log_blocked") is True and details.get("invalid_rights_flags_blocked") == 4, "details": details}


def package_public_results(stage: Path) -> tuple[str, str]:
    result_zip = stage / "STAGE_VALIDATION_BUNDLE.zip"
    files = sorted((stage / "results").glob("*"))
    with zipfile.ZipFile(result_zip, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for src in files:
            archive.write(src, arcname=f"results/{src.name}")
    with zipfile.ZipFile(result_zip) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("result ZIP CRC failed")
    return result_zip.name, hash_file(result_zip)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", required=True, help="Existing Windows hackathon directory; no existing source is modified")
    parser.add_argument("--stage-name", default=DEFAULT_STAGE_NAME)
    parser.add_argument("--source-dir", default=None, help="Optional existing verified public six-file source directory, for offline test only")
    args = parser.parse_args()
    if sys.version_info < (3, 11):
        print("Python 3.11+ required; no installation attempted", file=sys.stderr)
        return 31
    if not re.fullmatch(r"[A-Za-z0-9_-]{8,100}", args.stage_name):
        print("Invalid stage name", file=sys.stderr)
        return 31
    root = Path(args.workspace_root).expanduser().resolve()
    if not root.is_dir():
        print("Workspace root does not exist", file=sys.stderr)
        return 31
    stage = root / args.stage_name
    if stage.exists():
        print("STAGE_ALREADY_EXISTS: refusal to overwrite anything", file=sys.stderr)
        return 32
    stage.mkdir()  # exclusive, no overwrite
    (stage / "results").mkdir()
    report: dict[str, Any] = {"schema": "ReCollection.3.18b.WindowsStage.v1", "pinned_commit": PINNED_COMMIT,
        "started_at_utc": now_utc(), "transport": "LOCAL_VERIFIED_SOURCE" if args.source_dir else "HTTPS_PINNED_GITHUB_RAW",
        "status": "HOLD", "kiro_product_modified": False, "met_c_raw_files_touched": False,
        "source_root_modified": False, "rights_display_hold_slots": 4}
    try:
        offline = Path(args.source_dir).resolve() if args.source_dir else None
        report["source_hashes"] = acquire_sources(stage, offline)
        report["independent_70"] = execute_70(stage)
        if not report["independent_70"]["passed"]:
            raise RuntimeError("70_TESTS_FAILED")
        report["fresh_49_gate"] = execute_fresh_49(stage)
        if not report["fresh_49_gate"]["passed"]:
            raise RuntimeError("FRESH_49_GATE_FAILED")
        report["adversarial"] = verify_security_behavior(stage)
        if not report["adversarial"]["passed"]:
            raise RuntimeError("ADVERSARIAL_PROBES_FAILED")
        # Every source file remains unchanged after local test execution.
        for name,(_,expected) in SOURCE_EXPECTED.items():
            if hash_file(stage / "src" / name) != expected:
                raise RuntimeError("SOURCE_CHANGED_DURING_TESTS")
        report["status"] = "WINDOWS_STAGE_PASS" if os.name == "nt" else "NON_WINDOWS_STAGE_PASS"
    except Exception as exc:
        report["status"] = "HOLD"
        report["error_type"] = type(exc).__name__
        report["error"] = str(exc)[:400]
    report["finished_at_utc"] = now_utc()
    json_exclusive(stage / "results" / "stage_validation_report.json", report)
    archive_name,digest = package_public_results(stage)
    print(json.dumps({"stage": str(stage), "status": report["status"], "bundle": str(stage/archive_name), "bundle_sha256": digest,
        "tests70": report.get("independent_70", {}).get("passed"), "gate49": report.get("fresh_49_gate", {}).get("passed"),
        "adversarial": report.get("adversarial", {}).get("passed")}, ensure_ascii=False, indent=2))
    return 0 if report["status"].endswith("_STAGE_PASS") else 30


if __name__ == "__main__":
    raise SystemExit(main())
