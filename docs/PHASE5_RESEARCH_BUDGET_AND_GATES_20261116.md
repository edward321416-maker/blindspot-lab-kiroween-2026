# BLINDSPOT LAB — Phase 5 budget and execution gate (2026-11-16)

## Scope and actual starting state
- Public GitHub repository `edward321416-maker/blindspot-lab-kiroween-2026`; reviewed source HEAD `bc4a4d796917515668c11c8f6085a145249fba56` before these docs. Default `chore/kiro-repo-bootstrap`; still no `main`, no LICENSE, app, public deployment or submission.
- Kiro 3.3.0: user-confirmed `claude-opus-5.5` **MAX**; models `gpt-5.6-sol` and `claude-sonnet-5.5` visible in Kiro model list. Keep MAX for Opus as authorized. Other model effort depends on live selector.
- Last Kiro usage **reported** 106.00 / 4,000 promotional credits at 08:51 KST. This is a checkpoint, not a fresh usage reading.
- Historical **bootstrap** ceiling 100 credits was exceeded by cumulative use. Close that bootstrap phase; do NOT confuse it with the fresh Stage 5 allocation.

## Stage 5 credit envelope (incremental charges from a NEW /usage reading)
**SOFT: +500 credits; HARD: +600 credits for all of Phase 5 combined.** The 500/600 values are planning/execution ceilings, *not* an estimate or permission for paid services. Record `/usage` at start/end of every task group; compute the delta against the new Stage 5 baseline. Stop new agent work at +500 for review/reallocation. At +600 absolutely STOP; no paid overages or plan upgrade. If usage cannot be read, stop and record the gap. Use MAX selectively per the user's decision; still require hard stops.

| Task group | Soft credits | Permitted activity | Stop/acceptance gate |
|---|---:|---|---|
| A: independent protocol and rights/competitor source review | 80 | Read-only legal/licensing, provenance, data source methods, model cards, hardware inventory and spec correction | Source independence decision and rights notes accepted; **NO downloads** |
| B: bounded real-data feasibility and reproducibility | 100 | **Only after A passes and user authorizes exact datasets/checkpoints**, safe approved downloads, local isolated environment, 20-image out-of-evaluation smoke and replay | Safe load, per-image terms, CPU wall-time and hashes verified |
| C: real model A/B harness and statistical tests | 160 | **Only after preregistration and feasibility gate**, limited real-image inference, source-blind annotation checks, hash/IoU/mutation suite | Distinct real vs synthetic findings; no manufactured labels/results |
| D: best-practice FiftyOne parity and user workflow comparison | 110 | **Only after C feasibility**, plugin audit, pinned FiftyOne, true comparison with short-script baseline | Same inputs, parity, measured person-minutes and work outcome |
| E: reporting, independent audit and decision | 50 | CI/replay audit, source-linked findings and GO/HOLD/NO-GO dossier, final publication-safe Markdown/PDF | Every claim links to executed evidence; G4 not falsely implied |
| **Total soft** | **500** |  |  |
| Emergency headroom | **+100** | For an explicitly documented critical retry only, not automatic use | **Hard +600** |

The user has authorized Kiro MAX and public-repo visibility. **Dataset downloads, particular weight licenses, external deployment, cloud charges and open-source LICENSE selection have NOT been authorized merely by this budget.**

## One critical source correction
Sama's dataset author explicitly says COCO source annotations were **pre-loaded** when Sama-COCO was produced. It is a correlated annotation revision. Do not treat COCO + Sama as two independent blind ground truths. Reference: https://www.sama.com/sama-coco-dataset

## R0 execute now (no downloads or models)
- Read `.kiro/specs/blindspot-real-data-validation/INDEPENDENT_REVIEW_20261116.md` and the three existing draft Spec files.
- Update the Kiro Spec in a new auditable commit (do not erase draft history).
- Verify per-image COCO/Flickr rights; document where blind reviewers and review time will come from; record dataset/model citations and licence checks.
- Inventory local OS, CPU cores/RAM/disk/Python version; do NOT assume any GPU. Estimate minimum storage/network and CPU feasibility.
- Decide if the premise survives the independent-source finding and whether a best-practice FiftyOne experiment would be worth conducting.
- In parallel collect firsthand G4 problem evidence without downloading private customer data or contacting people without consent.
- After updated draft, independent cross-family review, and user approval of **exact** rights/model/download scope, only then start group B.

## Business gates
G1 = independently reviewed real labels (not Sama-vs-COCO alone); G2 = two pinned models on exact inputs plus reproducible replay; G3 = measured best-practice FiftyOne workflow; G4 = an actual identifiable practitioner needing the missing value. Completion of G1-G3 is **RESEARCH GO at best**, not product GO. The user's contest product selection remains unmade.

## Source documents
- https://www.sama.com/sama-coco-dataset
- https://cocodataset.org/dataset/termsofuse.htm
- https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- https://docs.voxel51.com/brain.html
- https://huggingface.co/PekingU/rtdetr_r50vd
- https://huggingface.co/PekingU/rtdetr_v2_r50vd
