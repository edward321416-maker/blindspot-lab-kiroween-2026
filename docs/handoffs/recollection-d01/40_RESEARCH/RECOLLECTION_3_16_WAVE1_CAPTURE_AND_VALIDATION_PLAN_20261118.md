# Re:Collection 3.16 — Wave-1 real-source acquisition and independent validation plan

**Date:** 2026-11-18 KST  
**State:** PLANNING COMPLETED / RAW_CAPTURES_NOT_RUN / PRODUCT_AND_PUBLISHING_HOLD  
**Evidence distinction:** The private user Drive folder has an 11-page PDF and fully reproducible empty-data ZIP; this public doc summarizes only collection URL targets and acceptance logic. **Do not copy original sealed 3.2 holdout or copyrighted media into this branch.**

## Reuse prior 3.15 research registry

3.15 has **22 data entities, 187 field definitions, 181 acquisition tasks and 83 planned future tests**. The 3.14 catalog has **58 heterogeneous links (NOT 58 distinct collection objects)** and 12 exploratory scenarios. This plan adds no alternate official corpus and does not mutate the original frozen 3.2 benchmark/scoring/holdout.

## Wave-1 selected input set

| Pack | Exact item sources | Key test | Ingestion state |
|---|---|---|---|
| A — same title, different accession | Met [36491](https://collectionapi.metmuseum.org/public/collection/v1/objects/36491) and [45434](https://collectionapi.metmuseum.org/public/collection/v1/objects/45434) | Retain independent item IDs, dimensions, image and claim provenance; title dedup is invalid | raw bytes not yet fetched |
| B — withdrawn attribution | Cleveland [1953.424](https://www.clevelandart.org/art/1953.424) (API documented at [CMA Open Access](https://www.clevelandart.org/open-access-api)) | Historical vs current attribution, source quote ≠ historical certainty | Only one collection object: **HOLD** until 2nd independent record for D1's 2–4 item prototype |
| C — rights contrast | Met [437127](https://collectionapi.metmuseum.org/public/collection/v1/objects/437127) and [436535](https://collectionapi.metmuseum.org/public/collection/v1/objects/436535) | Current non-PD/empty image vs PD image; no off-policy image fallback or unreviewed media | no public-media grants collected |
| D — proposed vs built | [NYC Archives](https://www.archives.nyc/blog/2019/9/26/the-brooklyn-battery-bridge), [NYC Library](https://www.nyc.gov/assets/records/html/march_2018.html), [NYPAP](https://www.nypap.org/preservation-history/brooklyn-battery-bridge/) | Bridge plan does not entail construction; tunnel evidence is distinct | NYC archive media publication needs permission and rights evidence |

**Exactly 8 candidate source records, not eight verified original snapshots.** Actual collection retrieval must be separately performed and versioned. CMA API endpoint `https://openaccess-api.clevelandart.org/api/artworks/1953.424` was not accessible through the browsing test; treat as **API_PENDING**, not as a valid downloaded response. Cleveland site item-page evidence is primary for the open-label pilot, but a single item alone is not a D1 two-item product scenario.

## Collection gates

1. **G1 raw capture:** provider-specific HTTPS GET within terms, record URL and redirect chain, response UTC time, status/content type/ETag/Last-Modified, *actual raw body bytes*, SHA256 and normalized extracted fields separately. Use a unique `capture_id`; no overwriting of snapshots. Metadata `metadataDate` is not HTTP fetch time. Search snippets and researcher transcriptions never substitute for raw bytes.
2. **G2 rights:** review METADATA / AUTHORED_TEXT / MEDIA_IMAGE separately (8×3 = 24 empty decision rows). New 3D/translation/audio assets require additional rows. `isPublicDomain` and a valid JPEG URL are not blanket publication grants. NYC Municipal Archives requests reproduction permission separately: https://portal.311.nyc.gov/article/?kanumber=KA-02632 . Restricted media never downloaded or embedded just to make demos.
3. **G3 independent semantic oracle:** 8 proposed claim slots, two truly independent evaluators blinded from each other's answer and model output, exact locator and source snapshot digest, SUPPORTED/REFUTED/INSUFFICIENT/AMBIGUOUS, disagreement adjudication. Claim quote presence alone does not prove entailment.
4. **G4 mutation and controls:** 4 packs×(field change, rights revoke, unexecuted-branch change, no-op) = 16 preregistered *planned* cases. Require immutable before/after hashes, affected **and unaffected** node oracle locked by independent expert. If previous historical snapshot is missing, label SIMULATED_MUTATION, never claim real source history.
5. **G5 verified engine:** user-reported B5.1 local 194/194 tests is not a direct audit in this research chat; B5.2 output-policy and visitor-safe renderer are design only. No real visitor content, publication or product test without separately approved and verified output gate.
6. **G6 fair pilot:** 4 packs × C0 template / C1 direct AI / C2 typed compiler × 2 = 24 **NOT_RUN** planning slots. Record model ID/effort/prompts/source hashes, actual walltime/tokens/rates/reviewer time and errors, including initial engineering overhead. This is a **new open-label pilot**, not the original frozen 3.2 holdout benchmark.
7. **G7 release:** curator approval bound to precise source/rights/policy/text version, rights-cleared media and authorized publication; HOLD currently.

## Produced private research artifacts (Google Drive, verified)

Folder: https://drive.google.com/drive/folders/1_BFOQzg6l44UOgHccLZtE_ShzRoiXPYF

- [11-page PDF plan](https://drive.google.com/file/d/1Zw0Gr3lDUxlZrh4rnu2rSwNUdl8wH5UH/view)
- [CSV/Runbook/Offline validator ZIP](https://drive.google.com/file/d/1flVUoUThC0AhWmtbZBxC3wMQM5Go9BVr/view)
- ZIP original SHA256: `226830006d77ecd5bb066f75cadcc82ca2f0486ef71d74af01b804247c598330`; 17 entries with validated per-file SHA256 + CRC and fresh extraction rerun
- PDF original SHA256: `14566455ed3ec07f849147c1950aea29850159f1d481f0bce701171bc533152c`; 11 pages rendered and checked
- Offline planning tests: **15/15 PASS**, including negative tests for fake capture, rights approval without proof, duplicate identity, same reviewer on both labels, unknown source, HTTP URL. This proves **only plan files' consistency**, not actual museum data/product behavior.
- Empty statuses are deliberately preserved: `NOT_CAPTURED` / `UNREVIEWED` / `HOLD` / `NOT_RUN`.

**Do not start live scraping, real media downloading, D1E, product code, AWS spending, publishing or new licensing by treating this docs-only plan as approval.**
