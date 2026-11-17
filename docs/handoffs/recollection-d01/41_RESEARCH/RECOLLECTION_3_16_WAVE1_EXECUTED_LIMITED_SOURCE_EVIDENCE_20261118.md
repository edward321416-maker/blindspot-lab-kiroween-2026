# Re:Collection 3.16 — Wave-1 web-indexed official evidence, **limited execution**

**Date:** 2026-11-18 KST  
**Status:** WEB_INDEXED_FIELDS_OBSERVED / RAW_HTTP_CAPTURE **0/8** / SELF_ORACLE_PASS / PRODUCT_PUBLICATION_HOLD  
**Basis:** Official institutional pages and indexed JSON returned through web retrieval. Network from the file-building sandbox failed DNS for `collectionapi.metmuseum.org` and an independent download attempt also failed. We did NOT retrieve the provider's original response bytes. Do not substitute field hashes for raw SHA-256.

## What was observed in the four preregistered packs

| Pack | Sources | Provider-grounded, publicly visible evidence | Remaining acquisition |
|---|---|---|---|
| A | [Met 36491](https://collectionapi.metmuseum.org/public/collection/v1/objects/36491), [Met 45434](https://collectionapi.metmuseum.org/public/collection/v1/objects/45434) | Both Great Wave impressions with same title, but `objectID`, accession numbers `JP10` vs `JP1847`, measurements 24.4×35.7 vs 25.7×37.9 cm, image URLs differ. Indexed provider `metadataDate` was 2025-11-11 on both. | Actual bytes, UTC capture, raw SHA256, current item policy/media verification |
| B | [CMA 1953.424](https://www.clevelandart.org/art/1953.424) | Cleveland says purchased as Titian in 1953, attribution withdrawn; no definite artist. **Single** object cannot satisfy frozen 2–4 object D1 prototype; current official page, no authentic historic version of 1953 catalog obtained. CMA API direct item URL unavailable to web retrieval. | Another independent source, original raw page/API, independent artist attribution oracle |
| C | [Met 437127](https://collectionapi.metmuseum.org/public/collection/v1/objects/437127), [Met 436535](https://collectionapi.metmuseum.org/public/collection/v1/objects/436535) | Restricted Monet `isPublicDomain=false`, empty original image; open Van Gogh `isPublicDomain=true`, nonempty image URL. Met artwork page says Monet image cannot be downloaded. | Raw JSON, current item terms, media usage proof, no unauthorized restricted media |
| D | [NYC archives bridge plan](https://www.archives.nyc/blog/2019/9/26/the-brooklyn-battery-bridge), [NYC Library tunnel record](https://www.nyc.gov/assets/records/html/march_2018.html), [NYPAP unbuilt bridge](https://www.nypap.org/preservation-history/brooklyn-battery-bridge/) | Distinguishes proposed bridge (1939) from constructed tunnel (construction 1940, opening 1950); NYPAP explicitly says bridge was never built. | Exact archived primary record locator, rights for original photos, independent causal claim review |

Current web indexed results were crawled about **3–7 months earlier**. Their `metadataDate` is a record value and is **not the time of our HTTP retrieval**. All observed records include the explicit `WEB_INDEXED_SELECTED_FIELDS_ONLY` status. Selected-field digests are calculated over a researcher-authored JSON projection and are **not proof of unchanged original bytes**.

## Executed offline research checks — not product claims

- **8/8** targeted official/secondary provider pages had their selected field/case statements retrieved for research.
- **24/24** metadata / institution-authored text / image rights review slots registered; **0/24** approved for public display.
- **16** synthetic open-label mutation cases: field change, rights revoke, unexecuted-branch reference and no-op control for each pack. Dependency graph and expectations defined by the **same author**.
- **51/51** researcher-authored record/rights/dependency checks passed twice, semantically identical SHA `d4572864fc01850c8cb59cb1d4b3a8160f346ebf7ad0cdcdcb03b8c649cbff83`.
- **11/11** unit tests of a newly written strict-HTTPS allowlisted HTTP collector, using fabricated in-memory server responses. Tests included exact original byte hash, ID mismatch, MIME mismatch, oversized/missing body, credentials/localhost/non-HTTPS rejection and no overwrite.
- **0/8 original raw body captures**, **0 independent human verdicts**, **0 real Kiro B5.2 runtime tests**, **0 actual C0/C1/C2 same-budget comparisons**.
- No third-party source image bytes were downloaded or publicly mirrored. No actual user Windows project source changed, no cloud spend, no model inference.

## Executable capture transport in private packet

The user's [private Drive Wave-1 folder](https://drive.google.com/drive/folders/1B1RmHTdX_BLIJNqjVLSFW1x7oNir8_u5) stores an executable research capture tool, offline tests, rights status, Web excerpts, open-label mutation cases, Excel six-sheet register and Korean 9-page report. The tool saves immutable `private/raw/{source_id}/{capture_id}/response.bin` and `capture.json` only after an actual allowlisted 200 HTTPS JSON/HTML response; no raw data placeholders. Its original source is supplied in the ZIP as unified new-file patches.

- [ZIP reproducibility packet](https://drive.google.com/file/d/1XPe2PvuYQno2JDIPxHEZhw-WUgzieOCa/view), local SHA256 `ef849c2dc9251f365f6dcde665dbe8a688ade0548686500904b44275ea1d76da`, 20 files, per-file hash/ZIP CRC verified; isolated extraction reran 51+11 checks successfully.
- [Excel 6-sheet register](https://drive.google.com/file/d/1BTnqlRDpCmnnEAtmvHFxDv4nDStdbCZh/view), local SHA256 `a4b4c7496d9a2459f975e50d343ee76d9e22e46b608ac853f9620751c85cd4ff`.
- [PDF human report](https://drive.google.com/file/d/1wtbaYzSysA0aC06FVyUlNAeyCufx__XR/view): 9 pages, source links and tests, user Drive file size may differ from PDF copy included in ZIP due to separate upload artifact handling. PDF-in-ZIP original SHA256 `a80e61704798cda44b952b67e631ae817a4f3ed5161280fe2e24f24d1c11e04e`; uploaded PDF size 115,768 B vs ZIP internal 78,637 B.

## Next gates — no silent authorization

1. Re-run the actual raw collector on a network-capable and terms-compliant environment, verifying exact SHA/HTTP metadata and object IDs; write an **append-only** capture status, compare to observed field projections. No media scraping.
2. Independently verify source-to-claim entailment, rights and selected & unselected dependencies; two blinded qualified reviewers and adjudication.
3. Preserve frozen 3.2 holdout and original `ExperienceSpec v0.2`; open-label S01-S12 and this Wave-1 are *not* the old holdout.
4. Separate actual B5.2 visitor-output policy implementation and safe renderer acceptance before any real museum product/publication claim. Latest available log indicates B5.2 user authorized with more credits but not completed.
5. Run actual Kiro C2 and equal-budget direct AI C1 on locked source bundles, including first-draft vs change-repair human time and false blocking.

**DO NOT PRESENT WEB FIELD EXTRACTS AS ORIGINAL RAW CAPTURED FILES. DO NOT UNLOCK PUBLICATION OR USE UNREVIEWED COPYRIGHTED MEDIA.**
