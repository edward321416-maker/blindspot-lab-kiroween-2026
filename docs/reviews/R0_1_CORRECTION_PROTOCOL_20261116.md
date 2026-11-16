# R0.1 correction protocol — execution-ready acceptance specification (PROPOSAL ONLY)

Source: GPT-5.6 Sol user-supplied review at remote SHA `113dc6fb455cfa589567939331e1a8091d4bf2e4`; findings archived in `docs/reviews/PHASE5_R0_SOL_REVIEW_20261116.md`.

**Goal:** Amend the Phase5 requirements, design, tasks, oracle protocol and rights preflight to eliminate circular evidence and make PM1–PM6 reproducible. **This document is NOT a source of user approval for downloads, inference, training, model weights, installing a Python environment, publication of imagery or product development.**

## Work order, required files, pass criteria

### C1 — Remove circular oracle and alert decisions (R2; highest)
Target: `research/phase5/protocol/ORACLE_INDEPENDENCE_PROTOCOL.md`, `requirements.md`, `design.md`.
- Freeze a source-independent S3 sample and two from-scratch blinded annotation sets before any evaluation inference (file hashes + lock timestamp).
- Neutral ontology and object-size policy preregistered independently from Sama rubric; do not silently impose 10×10 pixels to suppress S1/S2 differences. Analyze small objects separately.
- Preregister matching and canonical-box construction: thresholds, class concordance, tie-breaks and deterministic coordinate-resolution method; a simple IoU 0.5 match by itself is NOT an adjudication rule. Use sensitivity analysis for borderline boxes; unresolved class/box disputes => ABSTAIN.
- Two authors are **not a third independent adjudicator**. If their labels conflict, use a genuinely separate third blinded adjudicator where available, otherwise ABSTAIN. Disclose source independence vs independence from the two-person research team separately.
- Regession truth: `S3_HIT(A,obj) AND S3_MISS(B,obj)` using frozen predictions and matching code; fixes use reverse. Human review judges oracle validity/label ambiguity, not a subjective TRUE_REGRESSION vote.
- Alert candidate identity (S1 vs S3), non-alert sample frame, inclusion probabilities and answer masking/sequence predeclared before viewing A/B results.
**Pass:** no paths call a two-person TRUE_REGRESSION vote an independent ground truth; no source labels or models leak into the S3 blind step; contested labels have third-party or ABSTAIN path.

### C2 — Define executable PM1–PM6 and statistical decision rule (R3 + R5)
Targets: `requirements.md` and `design.md`.
- Unit of sampling = image, clustered by image; event unit = matched S3 object. Preregister sampling frame, eligible conditions/classes, controls and image-level bootstrap/cluster design simulation. Do not use an independent-object Wilson sample rule to assert P5.
- PM1: primary alert population `S1-derived A-HIT/B-MISS alerts on preregistered S3 images`. Among decisive/mappable alerts, numerator `S3-confirmed regressions`, denominator `all eligible decisive S1 alerts`. Report unmappable and ABSTAIN alerts separately, and fraction of total alerts resolved.
- PM2: one A→B release comparison yields a **single observed false-block decision**, not a "share of releases." Record source-S1 vs source-S3 binary decision disagreement for this pair, and optionally stratified false-alert counts/rates per image/class/condition; NO population-level release-risk inference without multiple independent release pairs.
- PM3: S3 regression recall = `S3 regression objects retrieved by S1 alert / all decisive S3 regression objects on independently sampled S3 images`. For a subsampled control stratum, use documented inclusion probabilities/weights and uncertainties.
- PM4: separate `oracle-abstention` (indeterminate S3 object / all S3 candidate objects) from `workflow-abstention` (could not resolve alert / all reviewed alert candidates); counts and minutes for both.
- PM5: paired operator timing, trained/preflighted operators and counterbalanced arm order; measure setup, warm processing and label review separately; define denominator `confirmed actionable regression`, and fallback report when count is zero (undefined ratio, not 0 or infinite). Separate human minutes from compute wait time.
- PM6: 7 predeclared binary artifact rubrics require **correctness and successful independent replay**, not simply file presence or count. Include file SHA, schema validation and CI verdict.
- Primary endpoint and business-relevant practical superiority margin specified **before outcome inspection**; one family-wise decision rule and multiplicity handling if more than one metric can trigger GO. Compare arms on matched cases, image-cluster CIs. `25% within` equivalence must use equivalence bounds and interval, not just a point ratio. If underpowered, classify INCONCLUSIVE/HOLD.
**Pass:** every PM has population, outcome definition, numerator/denominator, zero case, uncertainty method and preregistered threshold; P5 no invalid iid-object Wilson.

### C3 — Honest FiftyOne best-practice arm (R4)
Target: `design.md`, `tasks.md` and rights notes.
- Pin exact FiftyOne version + install/runtime support, evaluation arguments (IoU, score, max detections, class map, crowd/ignore behavior), Model Comparison plugin commit/license/code review, mistakenness version.
- Match frozen inputs and baseline scripts. Allow a reasonable short CI script to reproduce the seven artifact parts; compare against proficient operators.
- Randomize/counterbalance task order and log cache/warm-up; report cold setup, warm execute, human review and mistakes separately.
- Do not infer model superiority from code LOC/GUI presence. Note `compute_mistakenness` is model-conditioned triage, not G1.
**Pass:** a knowledgeable incumbent user could reproduce all results under the same evaluation contract.

### C4 — Rights metadata first, environment and pilot (R5 + R6)
Targets: `DATA_RIGHTS_PREFLIGHT.md`, `tasks.md`, `design.md`.
- A.6 authorization must identify **metadata-only** annotation manifest first, with exact URL, bytes, hash, license and destination. No images, models or dependency installs in this separate step unless later approved.
- Map per-image `images[].license` IDs to `licenses[]` and authoritative author/attribution URLs. Distinguish research frame rights from public demo subset rights; avoid filtering the statistical sample solely for demo redistribution eligibility.
- Source-specific policy for identifiable people/privacy, newly created S3 annotations' authorship/consent, and public redistribution.
- Model pair: immutable revision, verified sha, original code LICENSE at pinned commit, `train2017` claim from immutable model cards vs additional upstream pretraining **still to verify**. Resolve v2 processor discrepancy by inspecting exact processor_config at pin.
- Python 3.14 constraints: plan isolated supported Python 3.12 environment only with explicit install approval, pin dependencies and safe `safetensors` loader; use no remote code or pickle.
- 20-image smoke sample chosen with seed from an **out-of-evaluation pool**, warm-up and repeats specified, wall-clock/memory bounds, no accuracy peeking and fixed expansion criteria. CPU default; GPU only by explicit user permission and fresh reproducibility check.
**Pass:** no circular B.1-before-B.3 dependency; a complete approved metadata-first and then image/weight-specific rights gate.

### C5 — G4 practitioner lane with pre-C stop gate (R7)
Target: `tasks.md` and an evidence template.
- Consent form (what can be attributed publicly, what must remain private), practitioner/workflow identity under appropriate permissions, incumbent steps, cost of failed release decision, exact tool/version, direct first-person evidence and timestamps.
- Public evidence can be anonymized; do not claim it meets "identifiable practitioner" gate without reproducible private provenance and consent.
- G4 evidence gathering starts now **without outreach** or private user data unless user approves. Timebox before Group C: if no credible case, STOP/REASSESS whether high-volume inference is still worthwhile; do not falsely claim G4 verified.
**Pass:** explicit consent/evidence requirements and no empty G4 lane that permits unrestricted C.

## Scope/order/budget

**R0.1 is research protocol editing, not app build.** First revise text-only documents with Kiro Opus 5.5 MAX (user-approved) in a research branch. Then independent GPT-5.6 Sol review of the amended source, ideally read-only again.

At the last **observed** `/usage`: `164.98 / 4000`, R0 cumulative `54.75 / 80`; nominal unused R0 budget `25.25`, but the final report turn may consume more. Check a new `/usage` **before** work; stop if cumulative reaches 80. Never infer the precise current balance or silently move Group B credits into Group A. Phase5 +500 soft/+600 hard applies across groups but does not override the R0 +80 sublimit.

No model / dataset downloads or annotations yet, no CI benchmark or real evaluation; all actual execution tasks remain unchecked.

## Exit checklist
- [ ] five source files edited on a research branch; full unified diff attached for review.
- [ ] each R1–R7 residual has an exact closure location and measurable pass condition.
- [ ] annotations S3 are free of source/model leakage, third-or-abstain is explicit, regression mechanical.
- [ ] PM1–PM6 and P5 numerators/denominators/clustering defined; 1 release cannot estimate release population risk.
- [ ] fiftyone evaluation / plugin / timing preregistered fairly.
- [ ] licensing metadata-only step separately bounded and approved before download.
- [ ] G4 consent/provenance and pre-C stop gate.
- [ ] fresh /usage recorded, work stays within remaining R0 budget.
- [ ] a different model family reviews the corrected **content** and reports findings; no paper PASS without evidence.
- [ ] research/development handoff published if proposal accepted; product remains RESEARCH_HOLD.

## Primary sources / review trail
- `docs/reviews/PHASE5_R0_SOL_REVIEW_20261116.md`
- https://www.sama.com/sama-coco-dataset
- https://cocodataset.org/dataset/termsofuse.htm
- https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- https://docs.voxel51.com/getting_started/object_detection/03_finding_mistakes.html
