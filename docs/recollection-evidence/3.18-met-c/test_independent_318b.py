"""Independently authored 3.18b negative/positive gate and rights tests.

These tests are *additional* to the original 57 and do not attest to any
private museum response, legal clearance, or historical rights event.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import collect_met_c
from rights_policy import RightsSignals, evaluate_rights


def valid_signals(**kwargs: object) -> RightsSignals:
    source: dict[str, object] = {
        "api_public_domain": True,
        "page_public_domain": True,
        "primary_image_present": True,
        "image_download_available": True,
        "metadata_reviewed": True,
        "authored_text_approved": True,
        "image_display_approved": True,
    }
    source.update(kwargs)
    return RightsSignals(**source)


class IndependentGateHardeningTests(unittest.TestCase):
    def test_g01_fresh_real_49_cases_are_executed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="met-c-audit-gate-") as name:
            root = Path(name)
            gate = collect_met_c.run_integrity_gate(root, root / "fresh_gate.json")
            self.assertTrue(gate["passed"], gate)
            self.assertEqual(gate["exit_code"], 0)
            self.assertEqual(gate["source_sha256_before"], gate["source_sha256_after"])
            stored = json.loads((root / "fresh_gate.json").read_text(encoding="utf-8"))
            self.assertEqual(stored["run_id"], gate["run_id"])
            stderr = root / stored["run_directory"] / "unittest_stderr.txt"
            self.assertTrue(stderr.is_file())
            self.assertIn("Ran 49 tests", stderr.read_text(encoding="utf-8"))

    def test_g02_existing_forged_log_cannot_be_reused(self) -> None:
        with tempfile.TemporaryDirectory(prefix="met-c-audit-stale-") as name:
            root = Path(name)
            evidence = root / "fake_success.txt"
            evidence.write_text("No tests run.\nRan 49 tests\nOK\n", encoding="utf-8")
            gate = collect_met_c.run_integrity_gate(root, evidence)
            self.assertFalse(gate["passed"])
            self.assertEqual(evidence.read_text(), "No tests run.\nRan 49 tests\nOK\n")

    def test_g03_nonzero_subprocess_exit_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="met-c-audit-exit-") as name:
            root = Path(name)
            result = collect_met_c.subprocess.CompletedProcess([], 1, "", "Ran 49 tests in 0.1s\n\nOK\n")
            with patch.object(collect_met_c.subprocess, "run", return_value=result):
                gate = collect_met_c.run_integrity_gate(root, root / "gate.json")
            self.assertFalse(gate["passed"])

    def test_g04_summary_only_without_individual_cases_fails(self) -> None:
        self.assertFalse(collect_met_c._passed_exact_49(0, "Ran 49 tests in 0.1s\n\nOK\n"))

    def test_g05_truncated_test_log_fails(self) -> None:
        self.assertFalse(collect_met_c._passed_exact_49(0, "Ran 49 tests\n"))

    def test_g06_unreviewed_test_source_hash_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="met-c-audit-hash-") as name:
            root = Path(name)
            with patch.object(collect_met_c, "PINNED_TEST_SHA256", "0" * 64):
                gate = collect_met_c.run_integrity_gate(root, root / "gate.json")
            self.assertFalse(gate["passed"])
            self.assertIn("differ", gate["reason"])

    def test_g07_gate_output_outside_private_root_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="met-c-audit-scope-") as name:
            root = Path(name) / "restricted"
            gate = collect_met_c.run_integrity_gate(root, Path(name) / "outside.json")
            self.assertFalse(gate["passed"])


class IndependentRightsHardeningTests(unittest.TestCase):
    def test_r09_string_false_metadata_flag_is_hold(self) -> None:
        result = evaluate_rights(valid_signals(metadata_reviewed="false"))
        self.assertEqual(result["METADATA"]["decision"], "RIGHTS_REVIEW_HOLD")
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")

    def test_r10_string_false_authored_text_flag_is_hold(self) -> None:
        result = evaluate_rights(valid_signals(authored_text_approved="false"))
        self.assertEqual(result["AUTHORED_TEXT"]["decision"], "RIGHTS_REVIEW_HOLD")

    def test_r11_string_false_image_flag_is_hold(self) -> None:
        result = evaluate_rights(valid_signals(image_display_approved="false"))
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")

    def test_r12_integer_one_image_flag_is_hold(self) -> None:
        result = evaluate_rights(valid_signals(image_display_approved=1))
        self.assertEqual(result["IMAGE"]["decision"], "RIGHTS_REVIEW_HOLD")

    def test_r13_nonboolean_optional_signal_is_hold(self) -> None:
        result = evaluate_rights(valid_signals(page_public_domain="true"))
        self.assertTrue(all(row["decision"] == "RIGHTS_REVIEW_HOLD" for row in result.values()))

    def test_r14_valid_typed_signals_preserve_original_behavior(self) -> None:
        result = evaluate_rights(valid_signals())
        self.assertEqual(result["METADATA"]["decision"], "METADATA_ONLY_ALLOWED")
        self.assertEqual(result["AUTHORED_TEXT"]["decision"], "AUTHORED_TEXT_ALLOWED")
        self.assertEqual(result["IMAGE"]["decision"], "IMAGE_REUSE_APPROVED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
