# Re:Collection 3.18b — independent exact-source execution and tested gate / rights hardening

**Date:** 2026-11-18 KST  
**Executor:** ChatGPT, independent of the Codex 3.18 source publication.  
**Immutable audit source:** public GitHub `evidence/recollection-met-c-20261118` at commit `70c1e4527fb34c438d893c9a0a54b35f462314c0` (reported tree `5016f1e9289322f69d2a28657ea345ec6b24feaa`).  
**No edits** to that pinned evidence branch, default branch, user's Windows/Kiro product, underlying A/C raw response files, or sealed 3.2 holdout.

## Newly executed evidence (not a rephrasing of Codex logs)

We retrieved **the actual five Python source files** from this exact GitHub commit via connected GitHub:
`capture_met.py`, `test_capture_met.py`, `collect_met_c.py`, `rights_policy.py`, `test_rights_policy.py`. The entire public source-only transfer was held in a separate private Drive audit bridge, never including museum raw responses.

Exporting that pinned source bundle to the independent sandbox introduced a leading UTF-8 BOM on the JSON carrier; it was removed **only from the carrier**, then all extracted Python source byte hashes/sizes were separately compared with the 3.18 manifest: **5/5 exact SHA256 and byte-size match**. Source commit and provenance were verified.

Independently ran, without network, the exact unmodified published code:

```sh
python -B -m unittest -v test_capture_met.py test_rights_policy.py
```

**Observed result: 57/57 PASS, exit code 0 in Python 3.13.** This differs from the earlier audit that checked only published Codex logs.

## Reproduced two previously untested classes of failure

**P1-A: unbound test-success log.** Exact pinned `collect_met_c.py::gate_passed()` checks only the presence of `Ran 49 tests` and `OK` strings in an arbitrary input file. An independent probe supplied `No unit tests were run here.\nRan 49 tests\nOK\n` to the **actual imported function**: returned `True`. Reused old success text also returned `True`; truncated text returned `False`. This is a test authorization flaw, **not evidence the reported 57 cases or original C captures were forged**.

**P1-B: truthy untyped rights approvals.** Actual pinned `rights_policy.py::evaluate_rights()` approves `metadata_reviewed="false"` for METADATA, `authored_text_approved="false"` for AUTHORED_TEXT and `image_display_approved="false"` or integer `1` for IMAGE. Python dataclass type annotations do not coerce/validate runtime JSON values. These are **synthetic adversarial inputs**, not an observed museum rights-state change.

## Implemented and executed isolated *candidate* patch

We prepared a unified diff against the exact five-file source set. Only `collect_met_c.py` and `rights_policy.py` change, plus one new independent test file `test_independent_318b.py`.

- Collector: **no existing success log as input**; instead run the pinned 49-test source in a *new, separate evidence subfolder*, observe process exit 0, exact 49 unique successful individual cases and exact unittest summary, capture pinned source byte SHA256 before/after, UTC timestamps, unique run ID, and append-only output JSON. Forged or reused existing gate report blocks capture with HOLD.
- Rights: enforce runtime **exact boolean** approval and API signals; invalid type means `RIGHTS_REVIEW_HOLD` for METADATA, AUTHORED_TEXT and IMAGE; preserve original behavior for correctly typed values.
- **Original published 57 tests pass unchanged** against patch.
- **13 new independent adversarial/positive tests pass**; isolated patched run **70/70 PASS**.
- A **fresh clean replay** of `git apply --check` and `git apply` produced exact modified file bytes and **70/70 PASS**, then ZIP freshly extracted and **70/70 PASS** again.
- A separately invoked **real fresh Python subprocess gate** ran 49/49 tests, recorded exit 0 and `run_id`. Existing forged success log was rejected by the patched collector `run()` with exit code 30 and zero captures.

**Patch SHA-256:** `7e10616242b937de411f72c26bba23b03c0671b283d78ec75a8f994485d14c4e` (13,048 bytes). This patch is a **separate isolated reviewed candidate**, **NOT** applied in Codex Windows or any GitHub product/evidence branch. Applying it changes the old CLI second argument from an existing success log to a **new, not-yet-existing JSON gate report output inside the private evidence root**; downstream launcher updates and a Windows staging test are mandatory before adoption. Pinned file hashes will also need explicit review if changing those two original code/test files again.

## Actual raw and publication boundary

3.18 public evidence reports:
- `437127`: 2,386 original bytes, SHA256 `a0db88a8cc7548e63036c030a7ace1e2c65df040148d07da5c0610e7a827185b`.
- `436535`: 2,793 original bytes, SHA256 `497e0d1cd9166d27f6ef9b5e551b0cd8bafbcf1a5e134f364ba406b3a1f57d62`.

The independent auditor still does **not** have those two original `response.bin` files or complete private HTTP captures; **RAW_C_INDEPENDENT_BYTE_VERIFY = 0/2 (HOLD)**, regardless of the reported Codex 2/2. No independent external TLS fetch/byte attribution. Rights: **2 metadata-only workflow slots allowed, 4 authored-text/image slots HOLD**; none of the tested rights inputs grants legal or product release approval. Kiro product build, historical oracle and release remain separate.

## Reproducible sealed audit packet (private)

- **Private Drive audit folder:** https://drive.google.com/drive/folders/14_0zWAzCf0sLEgCcEKKPynM7GKW-Z_0-
- **Verified ZIP:** https://drive.google.com/file/d/1JWfJciqsQ7Xjp7yCn7Xw7e76VoTbw-xE/view, **176,255 bytes**, SHA256 `6bfd272e5d6e5b95b7df411867833dc9901b0792d474e2b500c162de132a918d`; 26 entries, all per-item CRC/SHA pass; includes exact source, patched source, standalone unified diff, Python logs and 6-page PDF. Remote ZIP byte size and parent verified.
- **PDF viewing copy:** https://drive.google.com/file/d/1hKsPQvn_-IDisxsfX6HJC-Nj1Nvx2blJ/view, 6 pages. ZIP-internal PDF independently re-opened: **142,933 bytes**, SHA256 `3246b3b9fe92e218179e598d9af38f27cc04e282da956c6ab34aa2cb1fcbe41d`. Drive PDF metadata also reports **142,933 bytes** and fetched text verifies core content. Remote PDF **byte-level SHA was not independently retrieved**, so exact remote content equivalence is not asserted solely from size.
- **Exact public-code-only bridge Doc** in private folder `14_0zWAzCf0sLEgCcEKKPynM7GKW-Z_0-`, no private raw Met response.

## Strict next step

1. Have Codex apply only this exact patch to a **new Windows staging copy** of the pinned 3.18 evidence, run 70/70, and generate a genuine fresh 49-run gate report. Never blindly reuse a prior log.
2. Have Codex **privately** package the 2 original C response.bin bytes, *sanitized* capture.json, COMMITTED and manifest for independent byte/ID/marker audit. Never publicly upload raw responses/headers/imagery to this repo.
3. Review rights slots by **specific asset and use scope**; keep 4 HOLD until separate approval.
4. Only after these passes discuss an isolated B/D next source gate or product integration. Do not merge or deploy this audit patch automatically.

**Verdict:** `EXACT_REMOTE_CODE_57OF57_PASS`; `TWO_P1_BYPASSES_REPRODUCED`; `ISOLATED_PATCH_70OF70_AND_FRESH_GATE_49OF49_PASS`; `C_RAW_BYTES_UNAVAILABLE`; `RIGHTS_AND_PRODUCT_HOLD`.
