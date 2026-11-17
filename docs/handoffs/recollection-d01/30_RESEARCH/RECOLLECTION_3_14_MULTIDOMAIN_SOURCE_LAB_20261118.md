# Re:Collection 3.14 — Multi-domain source universe and offline falsification lab

**Observed date:** 2026-11-18 KST  
**Status:** RESEARCH CATALOG / OFFLINE SELF-ORACLE PASS / KIRO PRODUCT AND PUBLICATION HOLD  
**Scope:** No changes to the separate user-local Windows Re:Collection code, frozen B0–B5 tests, sealed 3.2 holdout, paid services or museum images.

## Why this exists

A single Brooklyn–Battery Bridge example cannot establish transferability. We assembled **58 public source/provider/standard links** (19 prior links + 39 additional resources) spread across **14 broad catalog domain labels**. These are **not 58 individually verified artworks** or an exhaustive global corpus: they include object items, index-only references, technical standard documents and API provider policy pages. The full private JSON/CSV, tests and 16-page report are in the user's connected private Drive library; this public GitHub file contains only safe summary/reference URLs.

The corpus supports **12 curator-designed 2–4-object experience scenarios**:
1. S01 planned bridge vs constructed tunnel (TEXT_LINK);
2. S02 1883 Brooklyn Bridge vs later approach improvement (ITEM_PD);
3. S03 two distinct Met Hokusai Great Wave impressions, object IDs 36491 and 45434 (ITEM_PD API);
4. S04 Korean buncheong vs Japanese tea-bowl interpretive influence (META_LINK);
5. S05 sundial mechanism/form comparison (no physical simulation proof);
6. S06 complete ancient vases vs fragments (no fabricated reconstruction);
7. S07 AIC Seurat painting vs secondary making-of exhibition narrative (text license separate);
8. S08 CMA altered/uncertain artist attribution (content-sensitive image; staff suitability review);
9. S09 restricted Met Monet 437127 vs open Met Van Gogh 436535 (MEDIA HOLD);
10. S10 NYC 1950 “Mayor Robert F. Wagner” caption vs official 1954–1965 tenure (HUMAN REVIEW HOLD; do not assert wrong pictured identity);
11. S11 Smithsonian 3D object rights unknown (MEDIA HOLD);
12. S12 AIC 27992 artwork image public domain vs API authored description CC BY (TEXT REUSE HOLD).

**Research preview:** 8/12 supported as link/metadata-only exercises; 4/12 held by rights/conflict/attribution requirements. **Product publication approved: 0/12**, since actual curator review and B5.1/5.2 product gates are missing.

## Directly observed source evidence, important limitations

- [Met object 36491](https://collectionapi.metmuseum.org/public/collection/v1/objects/36491) and [45434](https://collectionapi.metmuseum.org/public/collection/v1/objects/45434): same depicted work, different original physical accession numbers and item IDs. Do not deduplicate by title.
- [Met Monet 437127](https://collectionapi.metmuseum.org/public/collection/v1/objects/437127): cached API `isPublicDomain=false`, empty primary image. [The item page](https://www.metmuseum.org/art/collection/search/437127) says image cannot be downloaded. Do not infer image license from provider-wide open access.
- [CMA 1953.424](https://www.clevelandart.org/art/1953.424) explains earlier Titian attribution dropped; present painter unresolved. No claim that our service independently validated attribution.
- [AIC 27992](https://api.artic.edu/api/v1/artworks/27992) has `is_public_domain=true`, but API description field has separate CC BY terms vs other metadata CC0.
- [The Met Korean bottle](https://www.metmuseum.org/art/collection/search/851660) and [Japanese tea bowl](https://www.metmuseum.org/art/collection/search/62649) enable careful museum-authored influence questions, not unqualified physical origin claims.
- [NYC historical bridge record](https://www.archives.nyc/blog/2019/9/26/the-brooklyn-battery-bridge) and [official mayoral roster](https://www.nyc.gov/site/dcas/about/green-book-mayors-of-the-city-of-new-york.page) surface a caption/office chronology contradiction for curator review.

Field snapshot JSON within the private packet is **a researcher-transcribed selection of observed fields** (12 resources), not original raw API response bytes or a current full snapshot.

## Offline evidence only (do not overstate)

- Python stdlib rule engine: **495 checks per run, 495/495 match researcher-authored expected labels; 2 identical runs, 990 decisions total**, deterministic serialized result digest. It validates catalog format, declared rights, case object count, declared source-to-Q/A/F dependencies, mutation impact, fail-closed labels, digest stability and conservative unknown-field handling. It does **not** detect missing semantic edges automatically or prove historical entailment.
- Chromium Source Lab: **21/21** UI interaction and responsive layout checks, 320px/390px no horizontal overflow, no JS errors. A distinct standalone HTML research console, not the user-local Kiro engine.
- Private ZIP: **27 entries**, 26 internal SHA-256/CRC checked files, includes historical project archive ZIP; fresh extraction reran Python and Chromium tests successfully.
- Research author, oracle and test engine were the **same agent/workflow**; no independent human blinded reviewers, real Kiro B2/B3 code, external live API fetch by the offline test runner, browser publishing or 3.2 heldout C0/C1/C2 model comparison.
- Real institutional media bytes were deliberately **not** copied. Rights are stored as item-level flags or as not verified.

## Technology novelty under prior art

Museum AI + KG is **not novel by itself**. See [2026 controlled-generation ceramics KG](https://www.nature.com/articles/s40494-026-02587-4), [MuseRAG++](https://www.nature.com/articles/s41598-026-55700-9), [CULTUREBOT 2026 preprint](https://arxiv.org/abs/2610.16435), and [2024 Dura-Europos Stories](https://journals.sagepub.com/doi/10.3233/SW-243552).
Competitors [Curio Publisher](https://www.curiopublisher.com/), [Actionbound](https://en.actionbound.com/museum) and [Axiell CultureConnect](https://www.axiell.com/solutions/product/cultureconnect/) already create museum digital experiences.
Proposed but **unproven** differentiator: deterministic, source-field-aware **change invalidation and human re-approval** across generated visitor question/answer/branch/feedback and rights, under equal model and cost conditions.

## Next gates and blockers

1. Item-level rights and exact source API payload capture (image URL verification, terms, hashes and revised-date metadata).
2. Independent licensed-curator validation, age/cultural suitability, uncertainty and entailment decisions; new blinded oracle sealed from developer.
3. Separate authorization/fixes for Kiro B5 snapshot/step-bound issues and visitor output-policy risks; source-linked is not historical truth.
4. Execute original frozen 3.2 C0/C1/C2 paired baseline on genuinely fresh real-source cases with model/cost parity and holdout integrity.
5. Confirm actual judge-ready browser UI integrated with Kiro engine and publisher/rights gates before release.

**Approved in this note:** nothing beyond safe data catalog research. **No AWS, deployment, D2/B5.1 source implementation, leaked research answers or licensed media redistribution.**
