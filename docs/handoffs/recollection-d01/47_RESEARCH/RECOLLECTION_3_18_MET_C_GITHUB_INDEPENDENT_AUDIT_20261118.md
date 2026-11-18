# Re:Collection 3.18 — Independent GitHub evidence review, Met C

**2026-11-18 KST — verifier:** ChatGPT (separate review of Codex publication).  
**Scope:** GitHub public branch `evidence/recollection-met-c-20261118`, immutable commit `70c1e4527fb34c438d893c9a0a54b35f462314c0`. **No mutation** to this evidence branch, original A captures, local Windows Kiro products, or sealed 3.2 holdout.

## Directly verified facts

- GitHub remote HEAD **matches** `70c1e4527fb34c438d893c9a0a54b35f462314c0`.
- GitHub commit tree matches reported `5016f1e9289322f69d2a28657ea345ec6b24feaa`. Parent is `ddfa8ad36ff61128a684dc125d5105721ad246e7` (planning baseline).
- One C commit modified/added **18 paths**: 16 new `docs/recollection-evidence/3.18-met-c/` files + `docs/DECISIONS.md`, `docs/PROVENANCE.md`. No product application file touched in this commit.
- The repository default `chore/kiro-repo-bootstrap` head remains `113dc6fb455cfa589567939331e1a8091d4bf2e4`. Independent A evidence branch `evidence/recollection-met-a-20261118` remains `93c4f7a9765af8c4fcd5a4c74f1ee7c98e9b2bd8`.
- **Independently computed** UTF-8 SHA-256 and byte size of all **15 of 15** published payloads listed in `sha256_manifest.json`: **all exact**. Verified local SHA-256 implementation with standard `sha256("abc")` self-test.
- Directly inspected `capture_met.py::verify_committed_directory()` (lines ~347–415) and the specific 12 newly added I01–I12 tests; checks include typed object IDs, receipt/stored hashes and sizes, HTTP 200, canonical URLs, JSON MIME, UTC time order, exact COMMITTED binding.
- Directly inspected `rights_policy.py`, `test_rights_policy.py`: **8 synthetic cases** R01–R08; item/asset policy separates metadata, authored institutional text and image. Each requires distinct reviewed/approved flags. Image rights remain HOLD in published records.
- GitHub logs record 37/37 baseline, 49/49 integrity, 8/8 rights, and **57/57** combined. **These are Codex-measured logs read back on GitHub, not a newly run Python test suite in this environment**. GitHub combined commit statuses found **0** checks. Network DNS for raw.githubusercontent.com blocked separate runtime download.

## Captured C data as reported; not privately obtained in this audit

| Object | Privately reported original response | Public API signal at capture | Rights |
|---|---|---|---|
| `437127` Monet | 2,386 bytes SHA256 `a0db88a8cc7548e63036c030a7ace1e2c65df040148d07da5c0610e7a827185b` | `isPublicDomain=false`, empty `primaryImage` | metadata-only; authored text / image HOLD |
| `436535` Van Gogh | 2,793 bytes SHA256 `497e0d1cd9166d27f6ef9b5e551b0cd8bafbcf1a5e134f364ba406b3a1f57d62` | `isPublicDomain=true`, primary image URL present | metadata-only; authored text / image HOLD |

Original `response.bin`/`capture.json`/`COMMITTED` bytes were **not** in this GitHub branch; unlike the previous Met A audit, no private C raw ZIP was submitted to the independent reviewer. Therefore `RAW_C_EXTERNAL_BYTE_REHASH_PENDING`. Web's Met pages were **3-month indexed material**, not a fresh TLS fetch or original byte snapshot. Web item page 437127 displayed download unavailable, and 436535 displayed Public Domain / Download Image: source-context checks only, not proof of current legal clearance.

## New actionable finding: security gate accepts forged test logs

`docs/recollection-evidence/3.18-met-c/collect_met_c.py` lines 16–23:

```python
normalized = text.replace("\r\n", "\n")
return "Ran 49 tests" in normalized and "\nOK\n" in normalized
```

The **same exact predicate** was reproduced in an isolated Python temp folder with a log containing `No unit tests were run here.\nRan 49 tests\nOK\n`: **True** despite no tests being executed. Treat as **P1 gate integrity gap** for a future reusable collector; **does not show the published real test logs are fabricated**. Next narrowly scoped patch should bind `subprocess.run` exit status, exact 49-case suite execution, source code + test file SHA, UTC clock, and evidence run ID; include forged/stale/truncated/partial log adversarial tests. Do not infer actual code execution solely from a TXT file.

## Release and follow-up decision

- `PUBLIC_EVIDENCE_SHA_PASS`: yes, **15/15**.
- `CODE_STATIC_REVIEW_PASS_WITH_CONCERN`: yes; P1 test-gate gap.
- `GITHUB_REPORTED_TESTS`: 57/57 (Codex reported logs, not CI).
- `RAW_C_INDEPENDENT_BYTE_PASS`: **NOT YET**; private response bytes have not been provided.
- `RIGHTS_METADATA_ONLY`: 2/6; no legal/public release permission implied.
- `RIGHTS_DISPLAY_HOLD`: authored text 2 + image 2 = **4/6**.
- `PRODUCT_PUBLICATION_APPROVED`: **NO**.

**Recommended sequence:** preserve C branch and private captures; harden 49-test gate on a *new* branch; review private raw evidence SHA/ID with immutable bundle; only then consider B/D raw collection. Real Kiro source integration, expert oracle, rights and product publication remain independent gates.

**PDF:** `ReCollection_3_18_Met_C_GitHub_Independent_Verification_20261118.pdf` (4 pages; local chat artifact, not copied into public GitHub).
