# Re:Collection 3.18b — Windows Codex isolated stage execution

**Date:** 2026-11-19 KST. **State:** `WINDOWS_EXECUTION_PENDING`; independent Linux stage runner `70/70 + fresh 49/49 + adversarial PASS`.

This is an executable **handoff to the user's Windows Codex terminal**, not a claim that ChatGPT can issue terminal commands on the user's physical Windows workstation. The current ChatGPT environment has no authenticated Windows terminal, remote Codex session-control connection, or local-drive mount. Do not represent sandbox/CI tests as user Windows tests.

## Exact pinned GitHub source

Repository: [`edward321416-maker/blindspot-lab-kiroween-2026`](https://github.com/edward321416-maker/blindspot-lab-kiroween-2026)

Patch commit (immutable): `d344673599408732ce1400a22cafb798c6e760b4`.

Source directory in commit: `docs/recollection-evidence/3.18-met-c/`.

Verified six Python files (length in bytes; sha256):

| File | Bytes | SHA-256 |
|---|---:|---|
| `capture_met.py` | 18528 | `43a0743a5059f1309edbf8be67c676ce65993d52ee4ff85ca5136342cdfc21a2` |
| `collect_met_c.py` | 8364 | `2ee25274caef9c8cf02756eae752c993f3651a4e788683f850081bb8bea9d605` |
| `rights_policy.py` | 4396 | `b3e75856395a2c534bc77b4faed28099ac73e53ff1b38201555a826907c8d049` |
| `test_capture_met.py` | 17354 | `8edc5b14cf482722b7ed1afd6c1d7cfb7ac93bf746b6b397b4128acac367d46b` |
| `test_rights_policy.py` | 4380 | `65e97fc4e6346df7ee2eba262ca5ec8b0543240b9c96c1ec20a6cddcff9c07c2` |
| `test_independent_318b.py` | 5493 | `71085c42deec49ccb39162c8e24fd95840d716b754101fec190390809c8bd937` |

## Recommended Codex execution

Use the existing authenticated Codex terminal, **no model fallback/subagents**, no new package installation, no paid service. Python **3.11+** and standard library only. The owner-specific existing hackathon folder is supplied in the private Codex message, **not posted here**.

1. Make a **new sibling/child stage** named `ReCollection_3_18b_Windows_STAGE_20261119`; if it already exists, fail without overwrite, deletion, or reuse.
2. Download exactly the six Python files above using immutable commit URLs at `raw.githubusercontent.com`. Check **both** byte size and SHA-256 before test execution; abort `SOURCE_HASH_HOLD` on any mismatch or redirect outside the approved HTTPS host. Or clone the public repository **into a separate new directory only**, check out exact commit detached, and select the six source files.
3. Run original 57+new13 cases (70 total) in a **fresh isolated copy**; save *actual process* exit code, stdout/stderr, case counts and executable Python version. Unit tests create `unit_test_artifacts/`; do not re-run in a used directory.
4. In another fresh source copy, invoke `collect_met_c.run_integrity_gate(private_root, new_json_output_path)`. Do **not** invoke the full Met `collect_met_c.main()` or `capture_one()`: this stage must **not** request fresh museum data. Check actual new **49/49 cases**, process exit 0, a new run ID, code/test fingerprints and output JSON.
5. As explicit negative checks, a forged existing `Ran 49 tests\nOK` text file must not enable `run()` (HOLD, exit 30, zero captures); `metadata_reviewed="false"`, `authored_text_approved="false"`, `image_display_approved="false"` and `image_display_approved=1` must all cause HOLD on their respective/all slots.
6. Verify all six original source SHA-256 values again. Package only **sanitized test logs/JSON** into `STAGE_VALIDATION_BUNDLE.zip`. Do not include local user credentials, raw museum responses or headers.
7. Return **absolute Windows staging location only in private chat**, script/runner SHA-256, run ID, 70/70 and fresh49/49 exit statuses, six SHA-256 checks, and ZIP SHA-256. Do not mark `WINDOWS_STAGE_PASS` if not actually executed in Windows.

An executable, audited **standard-library-only Python runner**, `windows_stage_318b.py` (13,857 bytes, SHA256 `89fddeb6084cb26d9fe44ccd5bfc1f9cf864d524c0b631d24ada74d10ab18fe7`), and a single-file **new-file unified diff** are supplied in the user's corresponding ChatGPT conversation artifact. The runner has been executed offline in **Linux**, with the pinned six sources from a previous independently audited ZIP. Reuse of a stage name was rejected (exit 32).

## Acceptance gates

| Gate | Required |
|---|---|
| G0 source freeze | immutable commit and all six exact SHA256s |
| G1 Windows stage | new folder, no overwrite or Kiro products touched |
| G2 Python 70 | `Ran 70 tests` + 70 unique named passes + **real process exit 0** |
| G3 fresh integrity 49 | verified subprocess 49, exit 0, run ID, source SHA before=after |
| G4 attack tests | forged log HOLD exit30/0 captures, 4 invalid approval types HOLD |
| G5 evidence | append-only stage status + private sanitized ZIP SHA256 |
| G6 independent audit | reviewer rechecks Codex Windows results and unchanged existing branches |

**Remaining independent HOLD:** private original Met C `response.bin` for 437127 and 436535 (byte-level independent verification 0/2) and four authored-description/image display rights slots. No PR, merge, AWS, product deployment, Windows remote execution or Kiro modification is authorized by this handoff.
