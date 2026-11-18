# Re:Collection 3.18b — applied hardening on a separate GitHub evidence branch

Baseline: `70c1e4527fb34c438d893c9a0a54b35f462314c0`. New branch: `evidence/recollection-met-c-318b-gate-rights-patch-20261119`. This is an isolated research-only commit, not a Kiro application release.

### Changes
- `collect_met_c.py`: replace log-substring trust with fresh 49-case pinned subprocess execution; require measured exit code 0, 49 distinct named passing cases, source SHA-256 before and after, UTC timestamps, run ID, and output-only private gate JSON; block stale/forged existing gate report.
- `rights_policy.py`: exact bool runtime validation for approval fields. Invalid types produce `RIGHTS_REVIEW_HOLD` in all three slots.
- `test_independent_318b.py`: 13 new positive/negative tests.
- Pinned baseline `capture_met.py`, `test_capture_met.py`, `test_rights_policy.py` remain byte-identical to `70c1e4527fb34c438d893c9a0a54b35f462314c0`.

### Independently executed validation
- Baseline code: 57/57 PASS in isolated Python; exit 0.
- Patched code: 70/70 PASS; exit 0.
- Clean unified diff replay: 70/70 PASS, exactly matching patched file hashes.
- Fresh actual Python integrity subprocess: 49/49 PASS with exit 0; private run ID `5dd5241159fc455a9b2b4a7157cc95d7`.
- Forged existing success log: HOLD, exit 30, 0 captures.
- Four independent invalid runtime rights approvals: all HOLD.
- Checks were executed in the isolated ChatGPT research sandbox. **This does not attest to execution on user's Windows Codex workstation or Kiro product.**

### CLI compatibility
The collector's second command argument has changed from *previously existing SUCCESS LOG* to *new, not-yet-existing JSON gate report path inside private output root*. The existing historical Met A/C capture roots must never be reused. Only new disposable staging roots are permitted for test runs.

### Evidence and provenance limits
The report includes no museum HTTP response bodies or images. Private Met C `response.bin` files were unavailable here and **remain unverified at independent byte level (0/2)**. The 4 authored-text/image rights slots remain HOLD; metadata-only workflow decisions do not confer media/text product release rights. No PR, merge, deploy, AWS use, or product code changes.

Private independent audit archive: https://drive.google.com/file/d/1JWfJciqsQ7Xjp7yCn7Xw7e76VoTbw-xE/view

Exact 3.18b patch SHA-256: `7e10616242b937de411f72c26bba23b03c0671b283d78ec75a8f994485d14c4e`. This document plus the GitHub commit diff describes the changes; patch itself stays in the private audit archive.

Decision: `CODE_PATCH_APPLIED_ISOLATED_GITHUB_BRANCH`; `LOCAL_TESTS_70_PASS`; `GATE_49_PASS`; `C_RAW_HOLD`; `RIGHTS_AND_PRODUCT_HOLD`.
