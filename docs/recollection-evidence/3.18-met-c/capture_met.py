"""Strict, append-only evidence capture for two Metropolitan Museum objects."""

from __future__ import annotations

import hashlib
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any, BinaryIO, NoReturn

OFFICIAL_HOST = "collectionapi.metmuseum.org"
OBJECT_IDS = (36491, 45434)
REQUEST_DELAY_SECONDS = 1.0
MAX_RESPONSE_BYTES = 16 * 1024 * 1024
USER_AGENT = "ReCollection-Evidence-Capture/3.17"


class CaptureError(RuntimeError):
    """A controlled capture failure with reportable details."""

    def __init__(
        self,
        message: str,
        exit_code: int,
        *,
        stage: str,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the error and preserve non-secret diagnostic fields."""
        super().__init__(message)
        self.exit_code = exit_code
        self.stage = stage
        self.details = details or {}


def utc_now() -> str:
    """Return a timezone-aware UTC timestamp."""
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def object_url(object_id: int) -> str:
    """Build the canonical official API URL for one object."""
    return f"https://{OFFICIAL_HOST}/public/collection/v1/objects/{object_id}"


def validate_met_url(url: str, expected_id: int) -> None:
    """Require the canonical HTTPS Met host and object path."""
    parsed = urllib.parse.urlsplit(url)
    expected_path = f"/public/collection/v1/objects/{expected_id}"
    if (
        parsed.scheme != "https"
        or (parsed.hostname or "").lower() != OFFICIAL_HOST
        or parsed.username is not None
        or parsed.password is not None
        or parsed.port not in {None, 443}
        or parsed.path != expected_path
        or parsed.query
        or parsed.fragment
    ):
        raise CaptureError(
            f"URL is outside the approved Met endpoint: {url}",
            23,
            stage="url_validation",
        )


class RestrictedMetRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Reject redirects outside the exact requested Met object endpoint."""

    def __init__(self, expected_id: int) -> None:
        """Store the expected object for redirect checks."""
        super().__init__()
        self.expected_id = expected_id

    def redirect_request(
        self,
        request: urllib.request.Request,
        file_pointer: BinaryIO,
        code: int,
        message: str,
        headers: Any,
        new_url: str,
    ) -> urllib.request.Request | None:
        """Validate a redirect before allowing urllib to follow it."""
        validate_met_url(new_url, self.expected_id)
        return super().redirect_request(request, file_pointer, code, message, headers, new_url)


def reject_constant(value: str) -> NoReturn:
    """Reject NaN and Infinity, which are not standard JSON values."""
    raise ValueError(f"Non-standard JSON constant: {value}")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Build a JSON object while rejecting duplicate keys."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_and_verify_json(raw: bytes, expected_id: int) -> dict[str, Any]:
    """Strictly parse JSON and verify its exact integer objectID."""
    try:
        text = raw.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        raise CaptureError(
            f"Strict JSON validation failed: {error}",
            22,
            stage="json_validation",
        ) from error
    if not isinstance(value, dict):
        raise CaptureError("JSON root is not an object", 22, stage="json_validation")
    object_id = value.get("objectID")
    if type(object_id) is not int or object_id != expected_id:
        raise CaptureError(
            f"objectID mismatch: expected {expected_id}, got {object_id!r}",
            22,
            stage="object_id_validation",
        )
    return value


def sha256_bytes(value: bytes) -> str:
    """Return the SHA-256 hex digest of bytes."""
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> tuple[str, int]:
    """Reopen and hash a saved file, returning digest and byte size."""
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return digest.hexdigest(), size


def write_bytes_atomic_exclusive(path: Path, payload: bytes) -> None:
    """Durably write bytes and rename without replacing an existing target."""
    if path.exists():
        raise CaptureError(f"Refusing to overwrite {path}", 24, stage="filesystem")
    temporary = path.with_name(f".{path.name}.partial")
    if temporary.exists():
        raise CaptureError(f"Partial path already exists: {temporary}", 24, stage="filesystem")
    try:
        with temporary.open("xb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.rename(path)
    except OSError as error:
        raise CaptureError(
            f"Failed to write {path}: {error}", 24, stage="filesystem"
        ) from error


def write_json_atomic_exclusive(path: Path, value: dict[str, Any]) -> None:
    """Serialize JSON and write it with exclusive atomic semantics."""
    payload = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    write_bytes_atomic_exclusive(path, payload)


def read_limited(response: Any) -> bytes:
    """Read a response while enforcing a strict maximum size."""
    chunks: list[bytes] = []
    total = 0
    while chunk := response.read(64 * 1024):
        total += len(chunk)
        if total > MAX_RESPONSE_BYTES:
            raise CaptureError(
                f"Response exceeds {MAX_RESPONSE_BYTES} bytes",
                21,
                stage="http_read",
            )
        chunks.append(chunk)
    return b"".join(chunks)


def fetch_response(object_id: int) -> tuple[bytes, dict[str, Any]]:
    """Fetch one object from the official API and return raw bytes plus HTTP facts."""
    request_url = object_url(object_id)
    validate_met_url(request_url, object_id)
    request_started = utc_now()
    request = urllib.request.Request(
        request_url,
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
        method="GET",
    )
    context = ssl.create_default_context()
    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=context), RestrictedMetRedirectHandler(object_id)
    )
    try:
        with opener.open(request, timeout=45) as response:
            status_code = response.getcode()
            final_url = response.geturl()
            response_headers = [[key, value] for key, value in response.headers.items()]
            validate_met_url(final_url, object_id)
            if status_code != 200:
                raise CaptureError(
                    f"Met API returned HTTP {status_code}",
                    20,
                    stage="http_status",
                    details={
                        "http_status": status_code,
                        "final_url": final_url,
                        "response_headers": response_headers,
                    },
                )
            raw = read_limited(response)
            collected_at = utc_now()
    except urllib.error.HTTPError as error:
        raise CaptureError(
            f"Met API HTTP error: {error.code} {error.reason}",
            20,
            stage="http_status",
            details={
                "http_status": error.code,
                "final_url": error.geturl(),
                "response_headers": [[key, value] for key, value in error.headers.items()],
            },
        ) from error
    except urllib.error.URLError as error:
        raise CaptureError(
            f"Met API network error: {error.reason}",
            21,
            stage="network",
        ) from error
    except (OSError, ssl.SSLError) as error:
        raise CaptureError(
            f"Met API transport error: {error}", 21, stage="network"
        ) from error

    facts: dict[str, Any] = {
        "request_url": request_url,
        "final_url": final_url,
        "request_started_at_utc": request_started,
        "collected_at_utc": collected_at,
        "http_status": status_code,
        "response_headers": response_headers,
    }
    return raw, facts


def capture_one(root: Path, object_id: int) -> dict[str, Any]:
    """Capture, validate, persist, re-hash, and commit one object."""
    object_directory = root / f"object_{object_id}"
    if object_directory.exists():
        raise CaptureError(
            f"Refusing to reuse {object_directory}", 24, stage="filesystem"
        )
    object_directory.mkdir()

    raw, facts = fetch_response(object_id)
    parsed = parse_and_verify_json(raw, object_id)
    received_sha256 = sha256_bytes(raw)
    response_path = object_directory / "response.bin"
    write_bytes_atomic_exclusive(response_path, raw)
    stored_sha256, stored_size = sha256_file(response_path)
    if stored_sha256 != received_sha256 or stored_size != len(raw):
        raise CaptureError(
            "Stored response differs from the received bytes",
            24,
            stage="stored_file_validation",
        )

    capture = {
        **facts,
        "byte_size": len(raw),
        "received_sha256": received_sha256,
        "stored_sha256": stored_sha256,
        "stored_byte_size": stored_size,
        "json_objectID": parsed["objectID"],
        "expected_objectID": object_id,
        "object_id_verified": True,
        "sha256_verified_after_reopen": True,
        "response_file": "response.bin",
    }
    write_json_atomic_exclusive(object_directory / "capture.json", capture)
    marker_payload = (
        f"COMMITTED\nobjectID={object_id}\nsha256={stored_sha256}\n"
        f"committed_at_utc={utc_now()}\n"
    ).encode("utf-8")
    write_bytes_atomic_exclusive(object_directory / "COMMITTED", marker_payload)
    return {
        "object_id": object_id,
        "status": "committed",
        "directory": object_directory.name,
        "byte_size": stored_size,
        "sha256": stored_sha256,
        "object_id_verified": True,
        "sha256_verified": True,
    }


def parse_utc_timestamp(value: Any) -> datetime | None:
    """Parse a timezone-aware UTC timestamp, returning none when invalid."""
    if type(value) is not str or not value:
        return None
    normalized = f"{value[:-1]}+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        return None
    return parsed


def has_json_content_type(headers: Any) -> bool:
    """Require well-formed response headers with a JSON content type."""
    if not isinstance(headers, list):
        return False
    content_types: list[str] = []
    for header in headers:
        if (
            not isinstance(header, list)
            or len(header) != 2
            or type(header[0]) is not str
            or type(header[1]) is not str
        ):
            return False
        if header[0].lower() == "content-type":
            content_types.append(header[1])
    return bool(content_types) and all(
        value.split(";", 1)[0].strip().lower() == "application/json"
        for value in content_types
    )


def verify_committed_directory(directory: Path, expected_id: int) -> bool:
    """Return true only for a complete, internally consistent committed capture."""
    response_path = directory / "response.bin"
    capture_path = directory / "capture.json"
    marker_path = directory / "COMMITTED"
    if not response_path.is_file() or not capture_path.is_file() or not marker_path.is_file():
        return False
    try:
        raw = response_path.read_bytes()
        parse_and_verify_json(raw, expected_id)
        capture_value = json.loads(
            capture_path.read_text(encoding="utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
        digest, size = sha256_file(response_path)
        marker_lines = marker_path.read_text(encoding="utf-8").splitlines()
        if len(marker_lines) != 4:
            return False
        if marker_lines[0] != "COMMITTED":
            return False
        if marker_lines[1] != f"objectID={expected_id}":
            return False
        if marker_lines[2] != f"sha256={digest}":
            return False
        timestamp_text = marker_lines[3].removeprefix("committed_at_utc=")
        if timestamp_text == marker_lines[3] or not timestamp_text:
            return False
        committed_at = parse_utc_timestamp(timestamp_text)
        request_started = (
            parse_utc_timestamp(capture_value.get("request_started_at_utc"))
            if isinstance(capture_value, dict)
            else None
        )
        collected_at = (
            parse_utc_timestamp(capture_value.get("collected_at_utc"))
            if isinstance(capture_value, dict)
            else None
        )
        if (
            committed_at is None
            or request_started is None
            or collected_at is None
            or not request_started <= collected_at <= committed_at
        ):
            return False
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, CaptureError):
        return False
    return bool(
        isinstance(capture_value, dict)
        and type(capture_value.get("expected_objectID")) is int
        and capture_value.get("expected_objectID") == expected_id
        and type(capture_value.get("json_objectID")) is int
        and capture_value.get("json_objectID") == expected_id
        and capture_value.get("received_sha256") == digest
        and capture_value.get("stored_sha256") == digest
        and type(capture_value.get("byte_size")) is int
        and capture_value.get("byte_size") == size
        and type(capture_value.get("stored_byte_size")) is int
        and capture_value.get("stored_byte_size") == size
        and type(capture_value.get("http_status")) is int
        and capture_value.get("http_status") == 200
        and capture_value.get("request_url") == object_url(expected_id)
        and capture_value.get("final_url") == object_url(expected_id)
        and has_json_content_type(capture_value.get("response_headers"))
        and capture_value.get("response_file") == "response.bin"
        and capture_value.get("object_id_verified") is True
        and capture_value.get("sha256_verified_after_reopen") is True
    )


def make_manifest(results: list[dict[str, Any]]) -> dict[str, Any]:
    """Build the response-file SHA-256 manifest from committed results."""
    return {
        "algorithm": "SHA-256",
        "generated_at_utc": utc_now(),
        "entries": [
            {
                "object_id": result["object_id"],
                "path": f"{result['directory']}/response.bin",
                "byte_size": result["byte_size"],
                "sha256": result["sha256"],
                "verified_after_reopen": result["sha256_verified"],
            }
            for result in results
            if result.get("status") == "committed"
        ],
    }


def run_capture(root: Path) -> tuple[dict[str, Any], int]:
    """Capture the fixed two-object Met A set and stop on the first failure."""
    results: list[dict[str, Any]] = []
    failure: dict[str, Any] | None = None
    for index, object_id in enumerate(OBJECT_IDS):
        if index:
            time.sleep(REQUEST_DELAY_SECONDS)
        try:
            results.append(capture_one(root, object_id))
        except CaptureError as error:
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
        except Exception as error:  # Defensive boundary: report, never commit.
            failure = {
                "object_id": object_id,
                "status": "failed",
                "stage": "unexpected",
                "exit_code": 25,
                "error_type": type(error).__name__,
                "error": str(error),
            }
            break

    raw_count = len(results)
    exit_code = 0 if raw_count == len(OBJECT_IDS) and failure is None else int(
        failure["exit_code"] if failure else 25
    )
    status: dict[str, Any] = {
        "scope": "Met A set only",
        "target_object_ids": list(OBJECT_IDS),
        "completed_at_utc": utc_now(),
        "raw_capture_success_count": raw_count,
        "raw_capture_target_count": len(OBJECT_IDS),
        "sha256_verified_count": sum(bool(item["sha256_verified"]) for item in results),
        "object_id_verified_count": sum(bool(item["object_id_verified"]) for item in results),
        "captures": results,
        "failure": failure,
        "exit_code": exit_code,
        "status": "complete" if exit_code == 0 else "failed",
    }
    return status, exit_code


def main() -> int:
    """Execute the fixed capture and write root-level status and manifest files."""
    root = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else Path.cwd().resolve()
    status_path = root / "capture_status.json"
    manifest_path = root / "sha256_manifest.json"
    if status_path.exists() or manifest_path.exists():
        print("Refusing to overwrite capture status or manifest", file=sys.stderr)
        return 24

    status, exit_code = run_capture(root)
    manifest = make_manifest(status["captures"])
    write_json_atomic_exclusive(manifest_path, manifest)
    write_json_atomic_exclusive(status_path, status)
    print(json.dumps(status, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
