"""Run the gated, JSON-only Met C capture for two fixed object IDs."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Any

import capture_met

OBJECT_IDS = (437127, 436535)


def gate_passed(log_path: Path) -> bool:
    """Return true only when the measured 49-test gate completed successfully."""
    try:
        text = log_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return False
    normalized = text.replace("\r\n", "\n")
    return "Ran 49 tests" in normalized and "\nOK\n" in normalized


def run(private_root: Path, gate_log: Path) -> tuple[dict[str, Any], int]:
    """Capture the fixed C objects only after the integrity test gate passes."""
    if not gate_passed(gate_log):
        return {
            "status": "HOLD",
            "reason": "49-test integrity gate did not pass",
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
