# Independent Phase 5 Spec Review — 2026-11-16

**Review status: CHANGES REQUIRED BEFORE DATA/MODEL EXECUTION.**
Target: `.kiro/specs/blindspot-real-data-validation/{requirements,design,tasks}.md` at `bc4a4d796917515668c11c8f6085a145249fba56`.
Review performed by ChatGPT GPT-6, a **different model family from draft author Kiro Claude Opus 5.5 MAX**, using direct inspection of the three source files and publisher/maintainer documentation. This is an external desk-review of protocol logic, **not an executed model experiment, user interview, runtime FiftyOne comparison or independent human annotation**. Preserve the draft; ask Kiro to amend it in a separately reviewable commit.

## What passed
- The draft distinguishes historical synthetic results (728 Phase4 cases) from nonexistent real-data measurements and explicitly keeps the product at RESEARCH HOLD.
- Oracle/model output separation, checkpoint hashes, repeat inference, data rights, CI fail-closed and provenance are correctly anticipated.
- Equal-input FiftyOne comparison, preregistration and explicit abstentions are useful foundations.

## REQUIRED corrections (blocking)

### R1 — Sama-COCO is **not a fully independent blinded annotation source**
The design proposes S1=COCO2017 and S2=Sama-COCO as the preferred independent pair. Sama's **own methods** explicitly state that the original COCO annotations were pre-loaded for the human associates, and some original boxes were intentionally kept/deleted according to a different labeling rubric. The annotation sets are *versions* with systematic protocol differences, not two blind independent ground truths. Source: https://www.sama.com/sama-coco-dataset and https://www.sama.com/blog/sama-releases-new-coco-dataset

**Fix:** Remove Option A from `RV-02/RV-03` as an automatically qualifying second independent ground truth. You MAY compare COCO/Sama as correlated annotation versions to find candidate disputes, but not count them as independent labels or use raw disagreements as errors. Independent verification must rely on **blinded human annotation from scratch** on a preregistered bounded subset (reviewers see the image, ontology and guidelines, but never S1/Sama or A/B outputs until labels are locked), followed by adjudication. If this cannot be done, mark G1 unvalidated and HOLD. Track sampling frame, independent reviewer roles, labels, disagreements, abstentions and actual reviewer time.

### R2 — Review-on-alerts is not independent reannotation and induces selection bias
`RV-03/RV-04` Option B lets reviewers see an alert candidate box. That is **blinded adjudication of an existing candidate**, not an independent annotation source. Sampling only alerts also makes overall disagreement-rate estimates biased.

**Fix:** Separate (i) source-independent blind annotation on a preregistered probability sample of images, (ii) subsequent blinded adjudication on alert and control cases, and (iii) model-conditioned triage. Document which conclusions each supports. Use random controls from non-alerts and report stratified sampling weights where inference beyond the audit sample is claimed. A two-person project review is internal and not third-party ground truth; disclose this.

### R3 — Metrics M1/M2 and GO rules do not measure the actual release decision quality
M1=share of model A->B alerts disputed by Sama, which is not independent. M2=INVALID/AMBIGUOUS proportion conditional on being disputed; ambiguity does not establish that original alert was false. The 15%, 50%, AUROC 0.70 and 150-LOC/120-minute cutoffs are **proposed, not validated customer-value thresholds**.

**Fix:** Add principal measures with independent blinded adjudication: confirmed new-regression precision, false-block rate per release, abstention count/time, missed regressions on control sample, review minutes per correctly adjudicated actionable regression and reproducible CI artifact completeness. Report counts and CIs. Retain M1/M2 as **exploratory diagnostics**, not automatic standalone-app GO. Split `true regression`, `label source disputed`, `cannot decide` explicitly.

### R4 — FiftyOne incumbent baseline may already cover the alleged differentiator
FiftyOne's documented `evaluate_detections` exposes object-level TP/FN/IoU; the community Model Comparison plugin explicitly categorizes `hitmiss`/`misshit` and localization changes; `compute_mistakenness` flags possible missing/spurious labels. References:
- https://docs.voxel51.com/user_guide/evaluation/detections.html
- https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- https://docs.voxel51.com/brain.html

**Fix:** Benchmark all 7 artifact components separately, and include a **best-practice FiftyOne-plus-short-script CI baseline**, not just the default GUI or a weak novice. Pin plugin and license, inspect community plugin code before execution. Differentiate only by empirically measured reduction in **user work or incorrect release decisions**, not by LOC arbitrarily or existence of a second UI. If incumbent parity meets the user job, NO-GO for standalone; consider optional companion only with evidenced extra value.

### R5 — Uncertain CPU throughput and underspecified sample/event counts
`tasks.md` assumes at least 2,000 images and approximately 8 CPU-hours while no 20-image throughput benchmark exists. `P5` requires at least 30 *consensus* regressions AND 30 fixes, which may fail simply because the model pair is similar, without falsifying the workflow hypothesis. Expensive CPU experiments before viability checks would consume the competition timebox.

**Fix:** After license/model checks, run 20 separate non-evaluation smoke images, measure wall time, memory and repeatability for both A and B. Record exact hardware, Python/torch versions and checkpoint licenses. Freeze final eligible image IDs and event-powered sample rule based on observed feasibility; if insufficient events, report **INCONCLUSIVE/HOLD**, not product NO-GO by default. Use predeclared small pilot then scale, no silent cherry-picking. Freeze primary threshold and conduct matched-precision sensitivity separately.

### R6 — Data/model rights and checkpoint loading preconditions
COCO terms say COCO owns its annotations (CC BY 4.0) but **does not own image copyrights**, which depend on Flickr terms and individual image licenses: https://cocodataset.org/dataset/termsofuse.htm . Original RT-DETR and v2 HF cards identify Apache-2.0 and `model.safetensors`, but exact immutable revision, dependencies, training sets and safe load need separate verification: https://huggingface.co/PekingU/rtdetr_r50vd and https://huggingface.co/PekingU/rtdetr_v2_r50vd .

**Fix:** No automatic bulk download until license-by-image, disk, CPU throughput, and safe model-load plan are written and reviewed. Keep raw images, annotations, weights and FiftyOne local DB outside Git. Recheck `.gitignore` and run a staged `git status` before any push. Do not publish copied COCO images.

### R7 — G4 customer/job evidence cannot be deferred until after a long G1-G3 cycle
Even a statistically positive oracle/model benchmark does not prove that a practitioner lacks a workable existing tool. The draft excludes G4 until after 2026-11-21.

**Fix:** Run a **parallel no-cost G4 evidence lane from day 1**: one identifiable practitioner/workflow where native FiftyOne plus reasonable scripts fails or costs measurably more; record exact business job, baseline, impact and direct citations, not anonymous cross-user anecdotes. Do not claim G4 passed without direct evidence.

## Review decision
**SPEC REVISION REQUIRED / R0 ONLY APPROVED:** Offline design, official source/terms review, collaborator/reviewer protocol, and on-device environment inventory are appropriate next actions. This review does **not** authorize dataset/model downloading, external permissions, license selection, paid cloud, application build or a model benchmark that has not been preregistered.

## Next Kiro revision (must be an auditable change)
1. Update requirements definitions for source-independent labeling vs correlated annotation-version differences.
2. Update design with source-independent blind sample, fully specified labels/roles, match/crowd taxonomy, measured CPU pilot gate, and a strong FiftyOne baseline.
3. Update tasks so licensing and 20-image no-evaluation feasibility come first; move G4 evidence to parallel track; revise P5 and decision metrics.
4. Keep existing draft history/provenance; mark all changes from this review and leave unchecked tasks unchecked until actual evidence exists.
5. Have another model family independently check the amended protocol before any high-volume inference.

**All numbers below are proposed research targets, not observed Phase 5 performance.**
