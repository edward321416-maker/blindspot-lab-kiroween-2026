"""Run the gated, JSON-only Met C capture for two fixed object IDs."""

from __future__ import annotations

import json
import hashlib
import re
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any

import capture_met

OBJECT_IDS = (437127, 436535)
PINNED_CAPTURE_SHA256 = "43a0743a5059f1309edbf8be67c676ce65993d52ee4ff85ca5136342cdfc21a2"
PINNED_TEST_SHA256 = "8edc5b14cf482722b7ed1afd6c1d7cfb7ac93bf746b6b397b4128acac367d46b"
INTEGRITY_SOURCE_NAMES = ("capture_met.py", "test_capture_met.py")


def _source_sha256(path: Path) -> str:
    """Calculate a source file fingerprint from bytes (not a reported log value)."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _passed_exact_49(returncode: int, stderr: str) -> bool:
    """Accept an actual clean unittest process with 49 distinct successful cases."""
    normalized = stderr.replace("\r\n", "\n")
    cases = re.findall(r"^(test_[a-zA-Z0-9_]+) \([^)]+\) \.\.\. ok$", normalized, re.M)
    summary = re.search(r"(?:^|\n)Ran 49 tests in [^\n]+\n\nOK\n?$", normalized)
    return returncode == 0 and len(cases) == 49 and len(set(cases)) == 49 and summary is not None


def run_integrity_gate(private_root: Path, gate_report_path: Path) -> dict[str, Any]:
    """Execute pinned tests freshly and commit a measured JSON gate report.

    The old gate treated an arbitrary existing text log as proof of execution.
    This gate treats the provided path as output-only; tests run in a unique
    evidence subdirectory, leaving test files and run artifacts for inspection.
    """
    report: dict[str, Any] = {
        "passed": False,
        "run_id": uuid.uuid4().hex,
        "started_at_utc": capture_met.utc_now(),
        "expected_test_count": 49,
        "source_commit": "70c1e4527fb34c438d893c9a0a54b35f462314c0",
    }
    root = private_root.resolve()
    output = gate_report_path.resolve()
    if not output.is_relative_to(root):
        report["reason"] = "gate report must be inside the private evidence root"
        return report
    if output.exists():
        report["reason"] = "existing gate report is not trusted or overwritten"
        return report

    code_dir = Path(__file__).resolve().parent
    required = {
        "capture_met.py": PINNED_CAPTURE_SHA256,
        "test_capture_met.py": PINNED_TEST_SHA256,
    }
    try:
        source_before = {name: _source_sha256(code_dir / name) for name in INTEGRITY_SOURCE_NAMES}
        report["source_sha256_before"] = source_before
        if source_before != required:
            report["reason"] = "source files differ from the reviewed GitHub commit"
            return report
        root.mkdir(parents=True, exist_ok=True)
        run_dir = root / "gate_runs" / report["run_id"]
        run_dir.mkdir(parents=True, exist_ok=False)
        for name in INTEGRITY_SOURCE_NAMES:
            shutil.copyfile(code_dir / name, run_dir / name)
        copied_sha = {name: _source_sha256(run_dir / name) for name in INTEGRITY_SOURCE_NAMES}
        if copied_sha != required:
            report["reason"] = "copy-to-run integrity mismatch"
            return report

        completed = subprocess.run(
            [sys.executable, "-B", "-m", "unittest", "-v", "test_capture_met.py"],
            cwd=run_dir,
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        report["exit_code"] = completed.returncode
        report["ended_at_utc"] = capture_met.utc_now()
        report["run_directory"] = str(run_dir.relative_to(root))
        report["test_log_sha256"] = hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest()
        (run_dir / "unittest_stdout.txt").write_text(completed.stdout, encoding="utf-8")
        (run_dir / "unittest_stderr.txt").write_text(completed.stderr, encoding="utf-8")

        after = {name: _source_sha256(code_dir / name) for name in INTEGRITY_SOURCE_NAMES}
        report["source_sha256_after"] = after
        report["passed"] = (
            copied_sha == required
            and after == source_before
            and _passed_exact_49(completed.returncode, completed.stderr)
        )
        report["reason"] = "fresh pinned test pass" if report["passed"] else "test execution/identity/exit mismatch"
        capture_met.write_json_atomic_exclusive(output, report)
        return report
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        report["reason"] = f"gate execution failed: {type(error).__name__}"
        return report


def run(private_root: Path, gate_log: Path) -> tuple[dict[str, Any], int]:
    """Capture the fixed C objects only after the integrity test gate passes."""
    gate = run_integrity_gate(private_root, gate_log)
    if not gate["passed"]:
        return {
            "status": "HOLD",
            "reason": "fresh pinned 49-test integrity gate did not pass",
            "integrity_gate": gate,
            "exit_code": 30,
            "target_object_ids": list(OBJECT_IDS),
            "captures": [],
        }, 30

    results: list[dict[str, Any]] = []
    failure: dict[str, Any] | None = None
    for index, object_id in enumerate(OBJECT_IDS):
        if index:
            time.sleep(capture_met.REQUEST_DELAY_SECONDS)
        try:
            result = capture_met.capture_one(private_root, object_id)
            directory = private_root / str(result["directory"])
            if not capture_met.verify_committed_directory(directory, object_id):
                raise capture_met.CaptureError(
                    "Post-capture committed-directory verification failed",
                    24,
                    stage="post_capture_verification",
                )
            results.append(result)
        except capture_met.CaptureError as error:
            failure = {
                "object_id": object_id,
                "status": "failed",
                "stage": error.stage,
                "exit_code": error.exit_code,
                "error_type": type(error).__name__,
                "error": str(error),
                **error.details,
            }
            break
        except Exception as error:  # Defensive boundary: report, never continue.
            failure = {
                "object_id": object_id,
                "status": "failed",
                "stage": "unexpected",
                "exit_code": 25,
                "error_type": type(error).__name__,
                "error": str(error),
            }
            break

    complete = len(results) == len(OBJECT_IDS) and failure is None
    exit_code = 0 if complete else int(failure["exit_code"] if failure else 25)
    status: dict[str, Any] = {
        "scope": "Met C JSON-only set",
        "target_object_ids": list(OBJECT_IDS),
        "completed_at_utc": capture_met.utc_now(),
        "raw_capture_success_count": len(results),
        "raw_capture_target_count": len(OBJECT_IDS),
        "sha256_verified_count": sum(bool(item["sha256_verified"]) for item in results),
        "object_id_verified_count": sum(bool(item["object_id_verified"]) for item in results),
        "captures": results,
        "failure": failure,
        "exit_code": exit_code,
        "status": "complete" if complete else "HOLD",
        "image_files_downloaded": 0,
        "integrity_gate": gate,
    }
    return status, exit_code


def main() -> int:
    """Execute the gated capture and write status plus response manifest."""
    if len(sys.argv) != 3:
        print("usage: collect_met_c.py PRIVATE_ROOT GATE_LOG", file=sys.stderr)
        return 2
    private_root = Path(sys.argv[1]).resolve()
    gate_log = Path(sys.argv[2]).resolve()
    status_path = private_root / "capture_status.json"
    manifest_path = private_root / "sha256_manifest.json"
    if status_path.exists() or manifest_path.exists():
        print("Refusing to overwrite capture status or manifest", file=sys.stderr)
        return 24

    status, exit_code = run(private_root, gate_log)
    manifest = capture_met.make_manifest(status["captures"])
    capture_met.write_json_atomic_exclusive(manifest_path, manifest)
    capture_met.write_json_atomic_exclusive(status_path, status)
    print(json.dumps(status, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
