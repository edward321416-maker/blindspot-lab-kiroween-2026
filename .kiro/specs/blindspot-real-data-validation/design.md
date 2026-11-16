# BLINDSPOT LAB: real-data validation design (G1-G3)

> STATUS: DRAFT, REVISION R0 / PLANNING ONLY. Nothing has been run or downloaded.
> History: first draft in commit `03667d6`; R0 revision 2026-11-16 KST by Kiro CLI (`claude-opus-5.5`, max) applying `INDEPENDENT_REVIEW_20261116.md` R1-R7. Cross-family review pending.

## Overview

```text
rights filter (preflight) -> val2017 frame -> pilot (20 images, group B) -> preregistration
  |-- S3 blind sample: two from-scratch label sets, locked -> adjudicated S3 ground truth
  |-- models A, B (pinned safetensors) -> predictions JSON, replayed
        |-- harness arm:   outcomes vs S1 and S3, alerts, controls, PM1-PM6, evidence, exit code
        |-- FiftyOne arm:  evaluate_detections x2, Model Comparison, mistakenness, short CI script
  -> blinded alert adjudication (alerts + controls) -> parity -> PM1-PM6 with intervals -> decision
  S2 (Sama-COCO): correlated-version study only, exploratory
  G4 lane: practitioner evidence, in parallel from day 1
```

## Data

- Frame: COCO val2017 images that pass the per-image rights filter (`research/phase5/protocol/DATA_RIGHTS_PREFLIGHT.md`).
- S1: COCO 2017 annotations (CC BY 4.0).
- S2: Sama-COCO. Its own page says all images were revisited with COCO labels pre-loaded, under a different rubric (crowds split, objects under 10x10 px dropped) ([Sama](https://www.sama.com/sama-coco-dataset)). It is therefore excluded from independence claims and used only to study how a label-version change moves alerts (exploratory).
- S3: blind from-scratch labels per `research/phase5/protocol/ORACLE_INDEPENDENCE_PROTOCOL.md`, the only independent oracle.
- Known limit: COCO-trained models report on val2017, so this tests version behaviour on familiar data, not deployment shift.

## Model pair (pins verified from Hub metadata on 2026-11-16, details in the rights preflight)

- A: `PekingU/rtdetr_r50vd` at revision `df939e6`; B: `PekingU/rtdetr_v2_r50vd` at revision `2824940`. Both list Apache-2.0 and `dataset:coco` and ship `model.safetensors` (about 172 MB each).
- Still to verify before group B: the upstream code license, the exact training split, v2 processor configuration, and a working `transformers` version on the chosen Python.
- Fallbacks unchanged: a D-FINE pair; torchvision Faster R-CNN v1 -> v2 only with `weights_only=True` and user approval. Ultralytics excluded by default (AGPL-3.0, pickle weights).

## Operating point (frozen at preregistration)

Primary `tau` 0.5 for both versions, `theta` 0.5, class-aware COCO-style matching, crowd regions ignored, at most 100 detections per image stored above score 0.05. Sensitivity only: `tau` 0.3 and 0.7, `theta` 0.75, and a matched-precision point for B.

## Pilot gate (group B, never in R0)

20 images outside the evaluation frame, both versions, measured on this machine: wall time per image, peak memory, replay identity and environment versions. Pilot results fix the S3 sample size (from labeling minutes), the alert and control counts (P5) and the CPU budget. A 2,000-image or 8-CPU-hour target is no longer assumed (R5).

Machine inventory (2026-11-16): i7-12700F 12C/20T, 31.8 GB RAM, about 1 TB free on D:, RTX 2060 present. CPU stays the default for determinism. GPU use needs approval and its own replay check.

## Harness (planned under `research/phase5/`, no code yet)

Manifest builder; S3 agreement and adjudication tools; inference runner with replay; outcome engine (recompute, never trust stored verdicts, abstain on unresolved objects); alert and control sampler with recorded seeds; metrics and decision script; parity checker against FiftyOne. `research/reference/phase4/` stays read-only.

## FiftyOne best-practice arm (R4)

- Pinned FiftyOne open-source version in its own environment, same images, S1 and predictions.
- `evaluate_detections` per version (object-level TP/FP/FN and IoU) ([docs](https://docs.voxel51.com/user_guide/evaluation/detections.html)).
- The Model Comparison plugin's Compute Model Differences operator, which labels each ground-truth object `hithit`, `hitmiss`, `misshit`, `missmiss`, `hithit+` or `hithit-` ([plugin](https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html)). Its source code is read and its commit pinned before it runs.
- `compute_mistakenness` from FiftyOne Brain to rank possible label errors. Its current docs page is to be re-read before use; this R0 review could not load it.
- A short CI script written by a competent operator that exits nonzero on confirmed-regression rules.
- Both arms are scored on all seven artifact parts. Differentiation counts only as measured reductions in false blocks or reviewer minutes, never LOC or UI existence alone.

## Statistics

Wilson intervals for PM1, PM3 and PM4; image-level bootstrap (10,000 resamples, recorded seed) for PM2 and PM5; inverse-probability weights where control sampling rates differ. Cohen's kappa and object F1 for S3 agreement.

## Threats to validity

Internal annotators and reviewers (two-person team); partial separation between analyst and annotator; small S3 sample; val2017 familiarity; S2 correlated with S1; builder bias in the FiftyOne timing (mitigated by the non-author operating it and by writing the workflow from docs before timing); shared `tau` across versions (sensitivity analysis).

## Security

No `trust_remote_code`, no pickle, plugin code read first, download hashes checked against the pins, nothing from `research/local-only/` committed.

## Budget and schedule (Phase 5 envelope)

Credits per `docs/PHASE5_RESEARCH_BUDGET_AND_GATES_20261116.md`: soft +500, hard +600 for Phase 5; group A (R0) cap +80; groups B to E only after approval. Reviewer hours are budgeted in the oracle protocol after the pilot.
