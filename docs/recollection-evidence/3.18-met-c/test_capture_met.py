"""Standard-library unit tests for the strict Met evidence collector."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import capture_met


class ArtifactCase(unittest.TestCase):
    """Base case that leaves all test artifacts intact for auditability."""

    artifact_root = Path(__file__).resolve().parent / "unit_test_artifacts"

    @classmethod
    def setUpClass(cls) -> None:
        """Create a new append-only artifact root once."""
        if not cls.artifact_root.exists():
            cls.artifact_root.mkdir(exist_ok=False)

    def make_directory(self) -> Path:
        """Create a directory named for the current test."""
        path = self.artifact_root / self.id().rsplit(".", 1)[-1]
        path.mkdir(exist_ok=False)
        return path


class TestStrictJson(ArtifactCase):
    """Exercise strict JSON and object identity validation."""

    def test_01_accepts_exact_integer_object_id(self) -> None:
        value = capture_met.parse_and_verify_json(b'{"objectID":36491}', 36491)
        self.assertEqual(value["objectID"], 36491)

    def test_02_rejects_missing_object_id(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"title":"x"}', 36491)

    def test_03_rejects_wrong_object_id(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"objectID":45434}', 36491)

    def test_04_rejects_string_object_id(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"objectID":"36491"}', 36491)

    def test_05_rejects_boolean_object_id(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"objectID":true}', 1)

    def test_06_rejects_duplicate_top_level_key(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(
                b'{"objectID":36491,"objectID":36491}', 36491
            )

    def test_07_rejects_duplicate_nested_key(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(
                b'{"objectID":36491,"nested":{"x":1,"x":2}}', 36491
            )

    def test_08_rejects_nan(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"objectID":36491,"x":NaN}', 36491)

    def test_09_rejects_infinity(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(
                b'{"objectID":36491,"x":Infinity}', 36491
            )

    def test_10_rejects_negative_infinity(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(
                b'{"objectID":36491,"x":-Infinity}', 36491
            )

    def test_11_rejects_invalid_utf8(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"objectID":36491,"x":"\xff"}', 36491)

    def test_12_rejects_trailing_data(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"objectID":36491}x', 36491)

    def test_13_rejects_array_root(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'[{"objectID":36491}]', 36491)

    def test_14_rejects_malformed_json(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'{"objectID":36491', 36491)

    def test_15_rejects_utf8_bom(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(b'\xef\xbb\xbf{"objectID":36491}', 36491)

    def test_16_rejects_escaped_duplicate_key(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.parse_and_verify_json(
                b'{"objectID":36491,"object\\u0049D":36491}', 36491
            )

    def test_17_accepts_nested_unique_values(self) -> None:
        raw = b'{"objectID":45434,"nested":{"x":1,"y":[true,null,2.5]}}'
        value = capture_met.parse_and_verify_json(raw, 45434)
        self.assertEqual(value["nested"]["y"][2], 2.5)


class TestUrlPolicy(ArtifactCase):
    """Exercise the exact-host, HTTPS-only URL policy."""

    def test_18_accepts_canonical_url(self) -> None:
        capture_met.validate_met_url(capture_met.object_url(36491), 36491)

    def test_19_accepts_explicit_https_port(self) -> None:
        capture_met.validate_met_url(
            "https://collectionapi.metmuseum.org:443/public/collection/v1/objects/36491",
            36491,
        )

    def test_20_rejects_http(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(
                "http://collectionapi.metmuseum.org/public/collection/v1/objects/36491",
                36491,
            )

    def test_21_rejects_wrong_host(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(
                "https://example.org/public/collection/v1/objects/36491", 36491
            )

    def test_22_rejects_userinfo(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(
                "https://x@collectionapi.metmuseum.org/public/collection/v1/objects/36491",
                36491,
            )

    def test_23_rejects_nonstandard_port(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(
                "https://collectionapi.metmuseum.org:444/public/collection/v1/objects/36491",
                36491,
            )

    def test_24_rejects_wrong_object_path(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(capture_met.object_url(45434), 36491)

    def test_25_rejects_query(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(f"{capture_met.object_url(36491)}?x=1", 36491)

    def test_26_rejects_fragment(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(f"{capture_met.object_url(36491)}#x", 36491)

    def test_27_rejects_lookalike_host(self) -> None:
        with self.assertRaises(capture_met.CaptureError):
            capture_met.validate_met_url(
                "https://collectionapi.metmuseum.org.example/public/collection/v1/objects/36491",
                36491,
            )


class TestStoragePolicy(ArtifactCase):
    """Exercise hashing, overwrite prevention, and commit completeness."""

    def write_complete_capture(self, directory: Path, object_id: int = 36491) -> None:
        """Create a self-consistent committed fixture."""
        raw = json.dumps({"objectID": object_id}, separators=(",", ":")).encode("utf-8")
        response_path = directory / "response.bin"
        capture_met.write_bytes_atomic_exclusive(response_path, raw)
        digest, size = capture_met.sha256_file(response_path)
        capture_met.write_json_atomic_exclusive(
            directory / "capture.json",
            {
                "request_url": capture_met.object_url(object_id),
                "final_url": capture_met.object_url(object_id),
                "request_started_at_utc": "2026-11-18T05:29:18Z",
                "collected_at_utc": "2026-11-18T05:29:19Z",
                "http_status": 200,
                "response_headers": [["Content-Type", "application/json; charset=utf-8"]],
                "byte_size": size,
                "received_sha256": digest,
                "expected_objectID": object_id,
                "json_objectID": object_id,
                "stored_sha256": digest,
                "stored_byte_size": size,
                "object_id_verified": True,
                "sha256_verified_after_reopen": True,
                "response_file": "response.bin",
            },
        )
        marker = (
            f"COMMITTED\nobjectID={object_id}\nsha256={digest}\n"
            "committed_at_utc=2026-11-18T05:29:20Z\n"
        ).encode("utf-8")
        capture_met.write_bytes_atomic_exclusive(directory / "COMMITTED", marker)

    def replace_capture_value(self, directory: Path, key: str, value: object) -> None:
        """Replace one capture field in a synthetic test fixture."""
        capture_path = directory / "capture.json"
        capture = json.loads(capture_path.read_text(encoding="utf-8"))
        capture[key] = value
        capture_path.write_text(
            json.dumps(capture, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def test_28_atomic_write_and_file_hash(self) -> None:
        directory = self.make_directory()
        path = directory / "value.bin"
        capture_met.write_bytes_atomic_exclusive(path, b"abc")
        digest, size = capture_met.sha256_file(path)
        self.assertEqual(
            digest, "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
        )
        self.assertEqual(size, 3)

    def test_29_overwrite_is_refused(self) -> None:
        directory = self.make_directory()
        path = directory / "value.bin"
        capture_met.write_bytes_atomic_exclusive(path, b"first")
        with self.assertRaises(capture_met.CaptureError):
            capture_met.write_bytes_atomic_exclusive(path, b"second")
        self.assertEqual(path.read_bytes(), b"first")

    def test_30_incomplete_capture_is_not_committed(self) -> None:
        directory = self.make_directory()
        capture_met.write_bytes_atomic_exclusive(
            directory / "response.bin", b'{"objectID":36491}'
        )
        self.assertFalse(capture_met.verify_committed_directory(directory, 36491))

    def test_31_corrupted_response_is_not_committed(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory)
        with (directory / "response.bin").open("ab") as handle:
            handle.write(b" ")
        self.assertFalse(capture_met.verify_committed_directory(directory, 36491))

    def test_32_complete_capture_is_committed(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory)
        self.assertTrue(capture_met.verify_committed_directory(directory, 36491))

    def test_33_wrong_marker_object_id_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory)
        marker_path = directory / "COMMITTED"
        marker_path.write_text(
            marker_path.read_text(encoding="utf-8").replace(
                "objectID=36491", "objectID=45434"
            ),
            encoding="utf-8",
        )
        self.assertFalse(capture_met.verify_committed_directory(directory, 36491))

    def test_34_wrong_marker_sha256_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory)
        marker_path = directory / "COMMITTED"
        lines = marker_path.read_text(encoding="utf-8").splitlines()
        lines[2] = f"sha256={'0' * 64}"
        marker_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertFalse(capture_met.verify_committed_directory(directory, 36491))

    def test_35_committed_prefix_only_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory)
        (directory / "COMMITTED").write_text("COMMITTED\n", encoding="utf-8")
        self.assertFalse(capture_met.verify_committed_directory(directory, 36491))

    def test_36_naive_marker_timestamp_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory)
        marker_path = directory / "COMMITTED"
        marker_path.write_text(
            marker_path.read_text(encoding="utf-8").replace(
                "2026-11-18T05:29:20Z", "2026-11-18T05:29:20"
            ),
            encoding="utf-8",
        )
        self.assertFalse(capture_met.verify_committed_directory(directory, 36491))

    def test_37_extra_marker_line_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory)
        with (directory / "COMMITTED").open("a", encoding="utf-8") as handle:
            handle.write("unexpected=true\n")
        self.assertFalse(capture_met.verify_committed_directory(directory, 36491))

    def test_38_i01_valid_c_capture_is_accepted(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.assertTrue(capture_met.verify_committed_directory(directory, 437127))

    def test_39_i02_typed_capture_object_id_is_required(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "expected_objectID", "437127")
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_40_i03_received_sha256_mismatch_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "received_sha256", "0" * 64)
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_41_i04_stored_sha256_mismatch_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "stored_sha256", "0" * 64)
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_42_i05_received_byte_size_mismatch_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "byte_size", 1)
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_43_i06_stored_byte_size_mismatch_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "stored_byte_size", 1)
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_44_i07_non_200_http_status_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "http_status", 206)
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_45_i08_non_json_content_type_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "response_headers", [["Content-Type", "text/html"]])
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_46_i09_noncanonical_request_url_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(
            directory, "request_url", f"{capture_met.object_url(437127)}?source=test"
        )
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_47_i10_noncanonical_final_url_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(directory, "final_url", capture_met.object_url(436535))
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_48_i11_invalid_utc_order_is_rejected(self) -> None:
        directory = self.make_directory()
        self.write_complete_capture(directory, 437127)
        self.replace_capture_value(
            directory, "request_started_at_utc", "2026-11-18T05:29:21Z"
        )
        self.assertFalse(capture_met.verify_committed_directory(directory, 437127))

    def test_49_i12_malformed_or_duplicate_capture_json_is_rejected(self) -> None:
        root = self.make_directory()
        malformed = root / "malformed"
        malformed.mkdir()
        self.write_complete_capture(malformed, 437127)
        (malformed / "capture.json").write_text("{", encoding="utf-8")
        self.assertFalse(capture_met.verify_committed_directory(malformed, 437127))

        duplicate = root / "duplicate"
        duplicate.mkdir()
        self.write_complete_capture(duplicate, 437127)
        capture_path = duplicate / "capture.json"
        text = capture_path.read_text(encoding="utf-8")
        capture_path.write_text(
            text.replace('  "http_status": 200,', '  "http_status": 200,\n  "http_status": 200,', 1),
            encoding="utf-8",
        )
        self.assertFalse(capture_met.verify_committed_directory(duplicate, 437127))


if __name__ == "__main__":
    unittest.main(verbosity=2)
