# Re:Collection — Future Test Data Contract 0.1
**Date:** 2026-11-18 KST
**Status:** DATA_PLAN_READY / RAW_SOURCE_PENDING / PRODUCT_EVALUATION_HOLD

The 3.14 exploratory inventory contains **58 URLs** across institutional item pages, API policy, standard and provider documentation, **not 58 verified unique objects**; it also has 12 curator-designed pilot scenarios and 12 researcher-transcribed selected field snapshots (not byte-identical raw API responses).

## Data that the first real benchmark must collect

| Tier | Data class | Reproducible minimum |
|---|---|---|
| A | Provider/source | Institution, exact accession/item ID, canonical URL, source kind and original object language |
| A | Immutable raw snapshot | Actual entire HTTP response, UTC retrieval time, status/headers, body SHA256, parser version and parent version |
| B | Asset and rights | Per **media, metadata, description, translation, PDF, 3D**, license evidence URL, allowed actions, actual media SHA, owner review and revocation |
| C | Evidence and factual claim | Exact JSON pointer/page/time/IIIF locator and quote digest, typed claim, SUPPORTED/REFUTED/INSUFFICIENT with independently documented semantic entailment |
| D | Learning/experience | Learning goal, visitor age/accessibility, 2–4 source references, versioned interaction nodes Q/A/F/branch and *static unexecuted* dependency edges/OR witnesses |
| E | Change impact | Real before/after immutable source and rights snapshots, independent affected **and unaffected** node lists, expected reapproval/publication gate |
| F | Independent human | Two separately blinded domain-expert reviewers, source/claim labels and score, conflicts and adjudication, approval hash bound to source+text+rights+policy |
| G | Fair C0/C1/C2 | Same source bundle, model/config, full prompt/output SHA, wall-clock, tokens/cost, separate initial-engineering and marginal curator time, frozen 100-point score |
| H | Product security | Real Kiro B5.1/5.2 fixes/actual code/commit, getter/proxy snapshot tests, actual <=50 actions, no invalid output and unsafe media publication |
| I | Dataset split/contest | Original 3.2 sealed four-case holdout intact, no oracle leakage, signed evidence/manifests, approved app URL/source license/demo |

## Delivered private research kit

- Research entity groups: **22**; field-level entries: **187**
- Acquisition tasks: **181** including 58 original snapshot captures, 58 rights validations, 12 independent claim-oracle, 12 mutation oracle, 12 human-review and 12 comparison items (plus locator/project-wide tasks)
- Planned future product tests: **83**, of which **35** are source/rights/output/dependency/runtime/evaluation adversarial cases
- Empty forms: **24** claim-oracle slots, **24** independent reviewer assignments, **36** C0/C1/C2 planned model run rows
- Integrity checks executed in offline research sandbox: **33/33 PASS** including intentional duplicate-ID, missing-link, overflow and absent-license attack rejection; ZIP manifest/CRC and Excel/PDF QA confirmed
- **0** actual independent human labels, **0** product runs with the collected museum sources, **0** approved third-party media for app publication; old data-transcription hashes are *not* raw HTTP response hashes.

The complete workbook (15 sheets), original 58 source URLs and 12 case records, JSON Schema Draft 2020-12 research import schemas, sample synthetic input, explicit readiness gates, test runner and PDF handbook live in the user's **private connected Google Drive Re:Collection data-folder**. This public documentation-only handoff intentionally **does not copy original 3.2 sealed case identities/answers, personal reviewer data, private licensed-media binaries or Windows-local Kiro source**.

## Key warnings

1. **3.14 S01–S12 are a public/research pilot, NOT the original frozen 3.2 holdout.** Keep original evaluator and benchmark weights unchanged.
2. **Researcher-created dependency and mutation expectations are not independent ground truth.** Two separate reviewers must label and lock cases before product tests.
3. **Item public domain flag is not universal permission** to reuse API descriptions, media, 3D or translated content. Verify each with original evidence and usage scope.
4. **B5 QA defects** previously reported include quote presence not entailing historical claims, generated free-text sinks, mutable in-process getters exceeding the bounded step contract, validator reread and input/script digest issues. The new workbook does not fix real code.
5. Future source acquisition and any B5.1/B5.2 patch, models, AWS, deployment and publication still require separately authorized work and actual evidence.

Source standards: https://www.w3.org/TR/prov-o/ · https://iiif.io/api/presentation/3.0/ · https://metmuseum.github.io/ · https://airc.nist.gov/airmf-resources/playbook/measure/

**Decision:** DATA PLAN READY; REAL PRODUCT / BLIND BENCHMARK / PUBLICATION HOLD.
