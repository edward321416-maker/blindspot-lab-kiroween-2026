# Re:Collection 3.17 — Actual RAW source capture and validation execution gate

**Date:** 2026-11-18 KST  
**Status:** PLAN_READY / RAW_SOURCE_CAPTURE **0/8** / RIGHTS **0/24 approved** / INDEPENDENT_ORACLE **0** / REAL_PRODUCT_HOLD  
**Nature:** Public, sanitized docs-only research-to-operations handoff. **Do not execute or modify frozen Kiro product source on the strength of this note.**

## Why 3.17 differs from earlier plans

Research 3.16 actually checked the official web-indexed *selected fields* for eight candidate sources (4 packs), wrote 16 researcher-authored mutation examples and ran 51 offline policy checks plus 11 mock-HTTP collector tests. However **none of the actual institutional HTTP original response bytes was collected**. Derived selected-field digests cannot be passed off as original-byte SHA-256 or independent historical truth. New stage 3.17 explicitly prioritizes fixing source provenance and acquiring RAW byte snapshots, starting with the two Met Hokusai objects.

## Frozen 8-target input

Reuse the existing private 3.16 `data/wave1_targets.csv` and collector `tools/capture_raw_http.py` from:
https://drive.google.com/drive/folders/1B1RmHTdX_BLIJNqjVLSFW1x7oNir8_u5

- **A first:** [Met 36491](https://collectionapi.metmuseum.org/public/collection/v1/objects/36491) and [Met 45434](https://collectionapi.metmuseum.org/public/collection/v1/objects/45434). Distinct accession numbers, despite same Hokusai motif.
- **C second:** [Met 437127](https://collectionapi.metmuseum.org/public/collection/v1/objects/437127) (previous web result `isPublicDomain=false`, empty image URL) vs [Met 436535](https://collectionapi.metmuseum.org/public/collection/v1/objects/436535) (previous web result `isPublicDomain=true`); no image extraction or public reuse.
- **B third:** [Cleveland 1953.424](https://www.clevelandart.org/art/1953.424), artist attribution formerly Titian, now uncertain; a *single object* is insufficient under unchanged D1 2–4-object contract. New companion independent object required.
- **D fourth:** [NYC Archives bridge proposal](https://www.archives.nyc/blog/2019/9/26/the-brooklyn-battery-bridge), [NYC municipal library history](https://www.nyc.gov/assets/records/html/march_2018.html), [NY Preservation Archive Project](https://www.nypap.org/preservation-history/brooklyn-battery-bridge/). Source HTML and media rights are separate.

## Mandatory collector P0 preflight — evidence from direct 3.16 source inspection

Existing Python stdlib collector at `tools/capture_raw_http.py` contains an identity-check gap:
`if 'objectID' in data and str(data['objectID']) != row['catalog_id']: raise ...` means **missing objectID can still pass**. Must make the exact ID **required**, reject null, type mismatch, and wrong identity before capture status promotion.

Additional P0 audit:
1. HTML response HTTP 200 + `text/html` **does not prove it is the requested historical record**. Keep HTML identity as `IDENTITY_REVIEW_PENDING` until final/canonical URL, title, source locator and excerpt reviewed.
2. Current `response.bin` followed by `capture.json` can leave incomplete folders if interrupted. Versioned collector requires readback/re-hash and **COMMITTED marker written last**. No original 3.16 archive overwrite.
3. Store redirect **chain**, not just final URL; TLS + exact official host allowlist. No unofficial proxies or bypass for 403/429. No media downloading in this task.
4. Limits from prior script: API JSON 2 MiB, HTML 4 MiB, 15-second timeout, 1.25s spacing, 1 request at a time. Met official docs state up to 80 requests/s; research defaults are far stricter: https://metmuseum.github.io/.
5. All edits to **isolated data lab copy**, not Windows product workspace: unified diff including new regression tests; **run old 11 collector mock tests and new missing-ID/partial-commit/HTML-identity tests first**.

## Operator sequence (separate Windows network-capable lab)

Inspect local operating policy, preserve worktree, do not install if Python unavailable. Extract existing Drive ZIP into a fresh `D:\ReCollection-Data-Lab\wave1` folder with no overwrite. Read original collector signature; patch P0 and test. Then run the original CLI on new isolated copy:

```powershell
py -3 -m unittest discover -s tests -p 'test_*.py' -v
py -3 tools/capture_raw_http.py --root . --pack A
# after A passed raw byte SHA + correct ID + immutable commit marker:
py -3 tools/capture_raw_http.py --root . --pack C
# B and D only after A/C stable; inaccessible sources stay HOLD:
py -3 tools/capture_raw_http.py --root . --pack B
py -3 tools/capture_raw_http.py --root . --pack D
```

No external GET has been performed as part of this **3.17 plan authoring**.

## Verification gates, strictly separated

- **G1 RAW:** HTTPS actual provider response body bytes, UTC time, response headers/status, full redirect history, requested & final URL, `sha256(response.bin)`, exact object identity. Store immutable `private/raw/{source_id}/{capture_id}/` with `COMMITTED` last. Provider `metadataDate` is **not** the timestamp for capture.
- **G2 RIGHTS:** originally 24 slots: 8 records × metadata/authored text/media image; check exact item/asset license, reuse scope, restrictions, revocation; none automatically approved by `isPublicDomain=true`. IIIF `rights` and `provider` fields are useful evidence, not a universal grant: https://iiif.io/api/presentation/3.0/.
- **G3 CLAIMS:** original quoted text is **not** automatically semantic entailment. Two genuinely distinct blinded human reviewers (unassigned) judge SUPPORTED/REFUTED/INSUFFICIENT/AMBIGUOUS with exact source hash/locator and disagreement adjudication.
- **G4 CHANGE:** 4 packs × four scenarios (field mutation, rights withdrawal, unexecuted branch, no-op) = 16 open-label, researcher-authored candidates. Lock *affected and unaffected* node truth with independent reviewer; without historical previous snapshot label `SIMULATED_MUTATION`.
- **G5 PRODUCT:** separate B5.2 user-approved synthetic typed visitor-output adapter exists as authorized work, but **no verified completion result** was seen by this research planner. Do not silently expand it to real archives or public renderer.
- **G6 EVAL:** new open-label C0/C1/C2 comparisons require equal sources/model/budget, paid credit authorization if applicable, both time and human review effort, frozen independent oracle. Preserve original sealed 3.2 holdout completely untouched.
- **G7 PUBLISH:** no third-party media, curator authority, product public URL or actual historical truth claims until license/claim/rendering gates are verified.

## Exact exit decision

- `PLAN_READY`: **YES**, deliverables in this chat: 9-page Korean PDF, 8-target JSON, 16-gate CSV, runbook and clean-extraction QA 8/8. This is plan integrity only.
- `MET_RAW_M1`: PASS only after actual original response bytes **2/2** and identity/hash/commit verification.
- `MET_RAW_M2`: PASS only after actual original response bytes **4/4** (A+C), while media reuse stays separate.
- `FULL_RAW`: PASS only after 8/8 real raw captures; inaccessible links should remain explicit `ACCESS_HOLD` instead of invented success.
- `INDEPENDENT_TEST_READY`: HOLD pending human reviewer/rights/mutation oracles.
- `ACTUAL_KIRO_PRODUCT_PASS`: HOLD pending measured B5.2 and new real data acceptance.
- `JUDGE_READY`: HOLD.

**Transport and security:** read-only official research, isolated Windows data lab, no user-source overwrite, no sealed holdout in public GitHub, no external image redistribution, no paid model/cloud calls in this plan. Original local Windows B5.2 work remains separate.
