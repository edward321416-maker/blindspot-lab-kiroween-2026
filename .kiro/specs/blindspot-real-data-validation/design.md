# BLINDSPOT LAB: real-data validation design (G1-G3)

> STATUS: DRAFT / PLANNING ONLY. Nothing here has been run. Items marked "verify" are unconfirmed until the named task checks them.
> Provenance: drafted by Kiro CLI 3.3.0 (`claude-opus-5.5`, effort `max`), 2026-11-16 KST. Not yet independently reviewed.

## Overview

One image set, two independent annotation sources, two detector versions and two analysis arms: the BLINDSPOT research harness and FiftyOne. Both arms read the same pinned files, so any difference comes from the workflow, not the inputs.

```text
images + S1 + S2 (hash-pinned manifest)
  |-- cross-source agreement (no models) --> consensus / disputed objects
  |-- detector A, detector B (pinned, CPU, replayed) --> predictions JSON
        |-- harness arm:   matching, outcomes, alerts, M1, adjudication sample, evidence, exit code
        |-- FiftyOne arm:  evaluate_detections x2, evaluation panel, scenarios, plugin, mistakenness
  --> parity check --> metrics with CIs --> preregistered decision rule
```

## Candidate data (verify in task group 1)

Option A, preferred: COCO val2017 images with two annotation sets.

- S1: the original COCO 2017 instance annotations.
- S2: Sama-COCO, a relabeling of COCO-2017 with the same splits (5,000 validation images). FiftyOne's zoo lists it as CC-BY-4.0 and can load it, and notes tighter masks, many crowd regions split into individual instances, and some images without annotations ([FiftyOne zoo: Sama-COCO](https://docs.voxel51.com/dataset_zoo/datasets/sama_coco.html), [Sama](https://www.sama.com/sama-coco-dataset)).
- Verify: whether Sama annotators worked without seeing COCO labels or model pre-labels (RV-02); exact license texts for COCO images (per-image Flickr license IDs) and both annotation sets; class ontology alignment (80 classes).
- Known limitation: val2017 is the standard reporting set for COCO-trained detectors. Results show version-to-version behaviour on familiar data, not deployment shift.
- S1/S2 differences can be protocol differences rather than errors. The agreement analysis ignores crowd regions, matches across sources at IoU 0.5, reports disagreement by type (presence, class, localisation), and reports S2 objects that fall inside S1 crowd regions as their own stratum.
- Images missing from either source are excluded. Images that both sources list as empty stay in. The count of exclusions is reported.

Option B, fallback if S2 independence is not established: S1 plus a blinded two-reviewer review of every alert and of a same-size random control sample of non-alert objects.

Option C, stretch for RQ2 only: a real adverse-condition dataset with human labels (screen ExDark, RTTS, ACDC, BDD100K). Their licenses are unverified. Use one only if its license permits this research and the later demo.

Selection rule: A if tasks 1.1 to 1.4 pass, otherwise B. C only after the core metrics exist.

## Candidate model pair (verify in task group 2)

- Primary: RT-DETR R50vd (A) -> RT-DETRv2 R50vd (B) through Hugging Face `transformers`. RT-DETRv2 was released in 2024 and added to `transformers` in February 2025 ([docs](https://huggingface.co/docs/transformers/model_doc/rt_detr_v2)). Expected checkpoint IDs: `PekingU/rtdetr_r50vd` and `PekingU/rtdetr_v2_r50vd`. Verify the model-card license, revision SHAs, safetensors files and training data.
- Why this pair: same family and API, and a newer version that is claimed to be better on average. Per-object regressions matter most in exactly that situation.
- Fallbacks: a D-FINE pair in `transformers` (verify availability and license); torchvision Faster R-CNN R50-FPN v1 -> v2 (BSD-3-Clause, but pickle-format weights, so only with `weights_only=True` and user approval per AGENTS.md).
- Excluded by default: Ultralytics YOLO, because of AGPL-3.0 implications for the later public repo and pickle `.pt` weights. Needs explicit user approval.

## Operating point (proposed, frozen in task 3.1)

- The runner stores up to 100 highest-scoring detections per image with score >= 0.05, identically for both versions. Analysis then filters at `tau`.
- Primary: `tau` = 0.5 for both versions; `theta` = 0.5, class-aware; COCO-style greedy matching by descending score; crowd regions ignored. `theta_agree` = 0.5 for cross-source matching.
- Sensitivity only: `tau` 0.3 and 0.7; `theta` 0.75; and a matched-precision point (`tau_B` set so B's precision on consensus objects equals A's at `tau` 0.5). A shared fixed `tau` can turn calibration drift between versions into apparent regressions.

## Harness components (planned under `research/phase5/`, nothing created yet)

1. Manifest builder: image IDs, SHA-256, license IDs and presence in S1/S2; archive hashes.
2. Agreement analyzer: cross-source matching, disagreement types, consensus and disputed sets. Reads no model output.
3. Inference runner: loads pinned safetensors weights on CPU with deterministic settings and writes predictions with image and model hashes. Replay mode compares two runs.
4. Outcome engine: COCO-style matching, HIT/MISS per object per version, and regressions and fixes against S1, S2 and consensus. Abstains on disputed objects. It carries Phase 4's rule (recompute, never trust stored verdicts) over to multi-object images.
5. Adjudication kit: blinded review sheets (crop with candidate box, shuffled, no source or model names, consensus controls mixed in), one decision file per reviewer, kappa and an adjudication log.
6. Metrics and decision: bootstrap CIs, M1 to M4, P1 to P5, the decision rule, a JSON and Markdown report and an exit code.
7. Parity checker: compares the outcome engine with FiftyOne's per-object evaluation results.

`research/reference/phase4/` stays read-only. The harness may reuse its ideas with attribution, but it is new Kiro-authored code with its own tests.

## FiftyOne arm

- Separate virtual environment with the `fiftyone` version recorded. FiftyOne runs a local database, and all data stays local.
- Load the same local images, S1 and S2 as label fields, and the A and B predictions from the same JSON files. FiftyOne does not run the models.
- Apply the same `tau` filter, detection cap and crowd handling as the harness before evaluating.
- Use the documented features: `evaluate_detections` once per version; the Model Evaluation panel to compare runs; scenario analysis for subsets; mistakenness for label-error triage ([model evaluation workflow](https://docs.voxel51.com/workflows/evaluation.html)); and the Model Comparison plugin for two detection models ([plugin](https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html)), after reading its code.
- Fairness: the operator follows official docs and tutorials, and the workflow is written down before timing. FiftyOne gets its best configuration; for M4 the higher AUROC of mistakenness computed from A's or B's predictions is used.
- The seven decision-artifact parts are scored the same way in both arms (RV-11).

## Data contracts (draft v1)

- `manifest.json`: `{image_id, file_name, sha256, license_id, in_s1, in_s2}`
- `predictions_<version>.json`: `{model_id, revision, weights_sha256, config_sha256, records: [{image_id, image_sha256, detections: [{label, score, bbox_xyxy}]}]}`
- `outcomes.csv`: `{image_id, gt_source, gt_object_id, class, area, iscrowd, status (consensus | disputed | crowd), a_hit, b_hit, verdict}`
- `adjudication_<reviewer>.json`: `{item_id, decision (VALID | INVALID | AMBIGUOUS), corrected_bbox, reviewer_id, timestamp}`
- Committed results hold IDs, hashes, boxes and metrics only. No images.

## Environment and storage

- One virtual environment per arm with pinned, hashed requirements and CPU-only torch. The system Python is 3.14; verify wheel availability and use a 3.12 environment if needed.
- Data, weights and the FiftyOne database live under `research/local-only/` (already ignored by Git) or in caches outside the repo. Before the first download, add `*.safetensors`, image extensions and database paths to `.gitignore` (task 1.3).
- Rough download size (verify): about 1 GB of val2017 images, a few hundred MB of annotations and a few hundred MB for two R50 checkpoints.

## Statistics

Image-level bootstrap (10,000 resamples, recorded seed) for M1, enrichment and outcome rates. Wilson intervals for small samples such as M2. Bootstrap CI for M4's AUROC. Cohen's kappa for the two reviewers. Adjudication sample: 60 to 100 disputed alerts plus 30 consensus alerts as controls, seeded. Note that 30 regressions (P5) is only a floor; M1 needs a few hundred alerts for a CI narrow enough to decide.

## Threats to validity

- Benchmark familiarity: val2017 is the models' reporting set.
- S1/S2 differences may reflect protocol rather than error. Typed disagreement and blinded adjudication (M2) address this.
- S2 independence is unverified (task 1.2). The fallback is option B.
- Reviewers are the two-person team, not independent third parties. This is disclosed.
- Builder-operator bias in the FiftyOne timing. A FiftyOne novice also overstates the incumbent's effort. Report both, and use an external FiftyOne user if one is available, which also feeds G4.
- A shared `tau` across versions: covered by the sensitivity analyses.
- Forking paths: covered by preregistration (RV-13).

## Security

No `trust_remote_code`, no pickle loading without approval, plugin code read before use, download hashes verified, no personal images and no credentials in files.

## Timebox and budget (proposed; the user confirms in task 0.1)

- The research ends with a decision on 2026-11-21 KST, leaving about two weeks before the 2026-12-05 07:00 KST deadline. If a precondition cannot be met by 2026-11-20, stop and decide with what exists.
- Kiro credits: soft ceiling 500 for this stage, hard stop at 600, with a `/usage` reading at the start and end of each task group. These are limits, not estimates.
- Compute: local CPU only. Throughput is measured in task 2.4 before the subset size is fixed.

## Sources

- FiftyOne zoo, Sama-COCO: https://docs.voxel51.com/dataset_zoo/datasets/sama_coco.html
- Sama-COCO dataset page: https://www.sama.com/sama-coco-dataset
- FiftyOne model evaluation workflow: https://docs.voxel51.com/workflows/evaluation.html
- FiftyOne Model Comparison plugin: https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- RT-DETRv2 in Hugging Face transformers: https://huggingface.co/docs/transformers/model_doc/rt_detr_v2

Source content was rephrased for compliance with licensing restrictions. All were read on 2026-11-16 and must be re-checked in tasks 1.1, 2.1 and 5.1.
