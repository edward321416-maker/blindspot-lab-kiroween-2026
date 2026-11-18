# Re:Collection 3.17 — Codex Met A marker verification patch stage

**Date:** 2026-11-18 KST  
**State:** PLAN_READY / SANDBOX_PATCH_REPLAY_PASS / USER_WINDOWS_PATCH_NOT_APPLIED  
**Privacy:** Docs-only. No user-uploaded raw museum responses, HTTP headers, cookies or executable code copied into this public branch. Exact unified diff remains in the user's private evidence ZIP / conversation artifact.

## Verified defect, exact source

Opened user's actual `ReCollection_3_17_Met_A_Independent_Review_Result_20261118.zip` and its nested original Codex capture files. Existing `capture_met.py::verify_committed_directory()` checks `marker_path.read_text(...).startswith("COMMITTED\\n")`, so a marker with wrong objectID / wrong sha256 / only the first line incorrectly passes while the other three files match. Existing actual 36491 and 45434 markers themselves were valid. **This is a verifier bug, not evidence of defective raw captures.**

The separate private [review ZIP](https://drive.google.com/file/d/1ObJPTjdW53mrPnnuPUw7IuRg6G2bO_Nc/view) SHA-256 `3becd3fd9ce610096221d3f2d1ce014e1d8398119c40f680e42af1e7ea7754db` includes strict unified diff `ReCollection_Met_A_Verifier_Marker_Hardening.patch` (SHA-256 `46f215d8af335b5eb8ac47561521a3f1dd0462e63303325d23eb6b431732935e`). Use private file access only; Codex's prior Drive login redirect is not an error to bypass.

## Scope

**Only** two isolated copied files:
- `capture_met.py`: strengthen `verify_committed_directory()` to verify exact 4-line COMMITTED marker; source ID strictly int matches expected ID; SHA256 matches re-read `response.bin`; timestamp is timezone-aware UTC; no trailing content; `capture.json` typed ID and bytes/sha/status check.
- `test_capture_met.py`: replace old one-line marker fixture with a valid 4-line fixture; add the five named regression tests test_33 to test_37 (wrong ID, wrong SHA, prefix only, naive timestamp, unexpected extra line).

**Must not change** `capture_one()`, HTTP fetch, storage semantics, existing 32 prior test intentions, original `response.bin` / `capture.json` / `COMMITTED`, 3.2 holdout, or Kiro B5.2/D2-V0 product code. No optional refactor, new dependencies or network activity.

## Preflight and repeatable acceptance

Original reported baseline 32/32 tests. Separate assistant sandbox verified on the exact user-uploaded source:
- `git apply --check` and `git apply` cleanly succeeded on an isolated copy;
- patched `python -m unittest test_capture_met -q` **37/37 PASS**;
- patched verification returned True for both original Met captures without modifying their `response.bin` files (bytes 2171 and 2385 and original SHA unchanged);
- wrong-objectID marker in a copied 36491 capture returned False.

The previous independent review also verified all 5 negative cases and a clean patch replay. These are **sandbox observations**, not Windows execution results.

### Codex stage instructions

User working folder (preserve unchanged):
`D:\Users\admin\Desktop\hackathon\ReCollection_3_17_Met_A_20261118T052349Z`

Create sibling *new* staging folder `ReCollection_3_17_Met_A_MarkerPatch_STAGING_20261118`. Stop if it already exists. Copy only the two relevant Python files to stage; run existing baseline. If the private patch is reachable, verify SHA before `git apply --check`. Otherwise reconstruct equivalent exact narrow change as a unified diff from local two files; no Drive auth bypass. Run 37 tests, both **real capture read-only** positive verifies, all five synthetic negatives, and compare original two raw file hashes before/after.

Save `patch_report.md`, `patch_tests.txt`, `source_hash_before_after.json`, `code_changes.diff` and SHA256 manifest under stage; no committed/published artifact and no automatic C-pack expansion.

## Gate status

- `PASS_STAGE`: baseline 32/32, patched 37/37, real captures 2/2 True, 5/5 malformed markers False, unchanged two raw SHA256s, unchanged original working folder and Kiro repo.
- `PATCH_CONFLICT_HOLD`: source differs or unified diff fails; never use force apply.
- `INTEGRITY_HOLD`: any positive fails, negative false-accept, or bytes change.
- `EVIDENCE_HOLD`: missing run logs, before/after hashes or patch.
- `RIGHTS_AND_PRODUCT_HOLD`: stays regardless of patch PASS; this consistency patch does not give independent TLS source authentication, curator truth, media license or public release authority.

## Private research plan

[Google Doc for project owner](https://docs.google.com/document/d/1vkRnnn-b0-nIVDoc4zPgs-ElJocOb6LxXOtTeew47Ac/edit) in the existing private [Met A independent review folder](https://drive.google.com/drive/folders/1xV5svRvVs5laP9jhducHZxsE2bQi7B2d).

**Next scope after a confirmed Windows report:** Collect Met C JSON `437127` and `436535` in a separate stage, no images, no assumption that `isPublicDomain` alone clears every right.
