# Phase 5 R0 checkpoint (2026-11-16 KST)

> Kiro CLI 3.3.0, model `claude-opus-5.5`, effort `max` (saved global setting). Desk review and spec revision only: nothing downloaded, installed, inferred or deployed. RESEARCH HOLD.

## Findings addressed

| Review item | Change | Where |
|---|---|---|
| R1 Sama-COCO not independent | S2 reclassified as a correlated version; S3 blind from-scratch labels are the only independent oracle | requirements Terms, RV-02, RV-03; oracle protocol sections 1, 4, 5 |
| R2 Alert review is not annotation | Blind annotation, alert adjudication and triage separated; random non-alert controls; internal-review disclosure | RV-04, RV-05; oracle protocol sections 2, 3, 6, 7 |
| R3 Metrics | PM1-PM6 (confirmed precision, false blocks, missed regressions, abstentions, reviewer minutes, artifact completeness); M1-M4 and their cutoffs made exploratory | requirements "Primary measures" |
| R4 FiftyOne baseline | Best-practice arm: evaluation, Model Comparison plugin, mistakenness, short CI script; seven parts scored; differentiation only by measured outcomes | RV-09, RV-10; design "FiftyOne best-practice arm" |
| R5 Throughput and events | 2,000-image and 8-CPU-hour targets removed; 20-image pilot in group B fixes sizes; insufficient events means INCONCLUSIVE/HOLD | RV-11, P5; design "Pilot gate"; tasks B.5, B.6 |
| R6 Rights and pins | Per-image rights before download; revisions and SHA-256 of both checkpoints recorded | `research/phase5/protocol/DATA_RIGHTS_PREFLIGHT.md`; RV-01, RV-06 |
| R7 G4 | Parallel practitioner lane from day 1 | RV-17; tasks G4.1, G4.2 |

## Confirmed from official sources (read 2026-11-16)

- Sama-COCO was produced by revisiting all images with COCO-2017 annotations pre-loaded, under a different rubric: https://www.sama.com/sama-coco-dataset
- COCO annotations are CC BY 4.0; COCO does not own image copyright, and image use follows Flickr terms: https://cocodataset.org/dataset/termsofuse.htm
- `PekingU/rtdetr_r50vd` revision `df939e661d8c52e80608d1ec566561aabd25a4e7` and `PekingU/rtdetr_v2_r50vd` revision `282494075698cab9faa1096ae26856890030c817`, both Apache-2.0 tags with `model.safetensors` (SHA-256 values in the rights preflight): https://huggingface.co/api/models/PekingU/rtdetr_r50vd?blobs=true, https://huggingface.co/api/models/PekingU/rtdetr_v2_r50vd?blobs=true
- The Model Comparison plugin classifies `hithit`, `hitmiss`, `misshit`, `missmiss`, `hithit+` and `hithit-` from two single-model evaluations: https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html

## Uncertain

- The Sama-COCO license version (the FiftyOne zoo says CC-BY-4.0; Sama's page says only "Creative Commons").
- Per-image license distribution in val2017, the upstream RT-DETR code license, the exact training split, and the v2 processor configuration.
- `compute_mistakenness` details: https://docs.voxel51.com/brain.html did not load its content during this review.
- torch, transformers and FiftyOne support on Python 3.14 (the only Python installed).

## Blocked (by design until approvals)

- Group B downloads, environment creation, the 20-image pilot and GPU use: need A.5 cross-family review and A.6 user approval.
- G1: no S3 labels exist. G4: no practitioner evidence yet.

## Local inventory (no installs)

Windows 11 Home 26300; i7-12700F 12C/20T; 31.8 GB RAM; C: 130 GB free, D: 1,010 GB free; RTX 2060; Python 3.14.0 only.

## Checks run during R0

From `research/reference/phase4`: 13/13 SHA-256 match `SOURCE_SHA256.json`; `python -m pytest -q tests/test_gate.py` gave 18 passed; the documented gate command exited 1 with 38 NEW_REGRESSION and `BLOCKED_UNVERIFIED_ORACLE`. These recheck the unchanged Phase 4 reference only, not any new measurement.

## Credits (`/usage`, kiroween bonus pool)

- R0 start, 09:13 KST: 110.23 (Phase 5 baseline).
- Before writing this file, 09:18 KST: 127.64 (+17.41).
- R0 cap: +80, so stop by 190.23. The final reading is recorded in `docs/DECISIONS.md` and the session report.
