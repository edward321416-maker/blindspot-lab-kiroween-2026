# BLINDSPOT LAB: real-data validation research spec (G1-G3)

> STATUS: DRAFT, REVISION R0 / RESEARCH HOLD / PLANNING ONLY. No dataset downloaded, no detector run, no benchmark exists. Every number is a proposal, not a result.
> History: first drafted by Kiro CLI (`claude-opus-5.5`, max) in commit `03667d6`. R0 revision on 2026-11-16 KST by the same model, applying `INDEPENDENT_REVIEW_20261116.md` findings R1-R7. Diff: `git diff 03667d6 -- .kiro/specs/blindspot-real-data-validation/`.
> Cross-family review of this revision is pending (see `docs/PHASE5_R0_CHECKPOINT.md`).

## Why this stage exists

Phase 4 showed that the gate logic works on 728 synthetic cases. It cannot show that the idea matters on real data. This stage tests, before any app work:

- G1: real images with independently made human labels.
- G2: two pinned, reproducible detector versions on identical inputs.
- G3: the same job done with a best-practice FiftyOne workflow.
- G4, run in parallel (R7): one identifiable practitioner whose job the incumbent fails. Collecting G4 evidence never blocks G1-G3, but a product GO needs it.

Passing G1-G3 is at best a research GO.

## Research questions

- RQ1 Decision quality: on independently labeled images, what share of A->B regression alerts are confirmed true regressions, and how many would wrongly block a release?
- RQ2 Version behaviour: how many confirmed regressions and fixes occur, and where (size, class, crowding)?
- RQ3 Incumbent: does best-practice FiftyOne (evaluation, Model Comparison `hitmiss`/`misshit`, `compute_mistakenness`, a short CI script) already produce the same correct release decision, and at what reviewer effort?

## Terms

- Version A / B: the released and the proposed checkpoint.
- S1: COCO 2017 annotations, the single ground truth a typical user already has.
- S2: Sama-COCO. Made by editing pre-loaded COCO labels under a different rubric, so it is a correlated annotation version, not an independent source (R1).
- S3: blind from-scratch labels made under `research/phase5/protocol/ORACLE_INDEPENDENCE_PROTOCOL.md`. The only independent oracle.
- HIT / MISS: COCO-style greedy one-to-one matching, same class, score >= `tau`, IoU >= `theta`. Crowd regions are ignored.
- Alert: an object that is a HIT under A and a MISS under B against a given label source. Confirmed regression: an alert both reviewers mark TRUE_REGRESSION in blinded adjudication.
- Decision artifact, seven parts, each measured separately (R4): (1) per-object regression and fix list; (2) abstentions with reasons; (3) per-condition summary; (4) review record; (5) offline evidence manifest with hashes; (6) replay result; (7) CI exit code with JUnit and JSON output.

## Requirements (EARS)

- RV-01 Rights. WHEN data or weights are selected THEN the study SHALL follow `research/phase5/protocol/DATA_RIGHTS_PREFLIGHT.md`: record per-image licenses before download, keep images, annotations and weights out of Git, and publicly display only images whose license permits it.
- RV-02 Independence. A label source SHALL count as independent only if humans made it without seeing S1, S2 or model outputs. S2 SHALL be used only as a correlated version, and S1/S2 differences SHALL NOT be called label errors.
- RV-03 Blind sample. G1 SHALL rest on S3: a preregistered seeded random sample of images, labeled from scratch by two annotators whose label sets are locked (hash committed) before they see any other source. If S3 cannot be produced, G1 SHALL be reported unvalidated and the decision SHALL be HOLD.
- RV-04 Adjudication. Alert review SHALL be a separate step from blind annotation. Reviewers see the crop and the ground-truth box but not the source, model names or the other reviewer's decision; alerts are shuffled with preregistered random non-alert controls. Unresolved cases SHALL be CANNOT_DECIDE.
- RV-05 Internal review disclosure. Every report SHALL state that annotators and reviewers are the two project members, not third parties.
- RV-06 Model pinning. Versions SHALL be pinned by Hub revision and weight SHA-256 (values in the rights preflight), loaded from safetensors with remote code disabled, with library versions and preprocessing recorded.
- RV-07 Identical inputs and replay. Both versions SHALL see byte-identical images. Repeated runs SHALL give identical detections at the operating point (box tolerance 0.01 px, score tolerance 1e-5). Mismatches SHALL be logged as reproducibility failures.
- RV-08 Recomputation and parity. The harness SHALL recompute outcomes from raw predictions and labels, and per-object outcomes SHALL agree with FiftyOne `evaluate_detections` on at least 99.5% of non-crowd objects under identical definitions, with every difference explained.
- RV-09 Best-practice baseline. The FiftyOne arm SHALL include detection evaluation, the Model Comparison plugin (code read and pinned before use), `compute_mistakenness`, and a short documented CI script, run by a competent operator. A GUI-only or novice baseline SHALL NOT be used.
- RV-10 Effort. For each of the seven artifact parts and both arms, the study SHALL record coverage (native, configuration, custom code with LOC, not possible), operator minutes, steps and errors.
- RV-11 Pilot first. Sample sizes and CPU budget SHALL be fixed only after a 20-image pilot outside the evaluation set measures runtime, memory and replay. That pilot is a group B task, not R0.
- RV-12 Statistics. Rates SHALL be reported with counts and 95% intervals (Wilson for proportions, image-level bootstrap with a recorded seed otherwise). If inference extends beyond an audit sample, sampling weights SHALL be reported.
- RV-13 Preregistration. Definitions, operating point, sample rules, metrics and the decision rule SHALL be committed before A/B inference on evaluation images. Later changes SHALL be labelled deviations and their results exploratory.
- RV-14 Fail closed. Missing rights, provenance, hashes, replay or parity SHALL block GO.
- RV-15 Honest reporting. Measured results SHALL be kept apart from hypotheses, and Phase 4 synthetic results SHALL NOT be pooled with real data.
- RV-16 Scope. Local only, no paid services, no personal CCTV or face images, no code in `apps/` or `packages/`.
- RV-17 G4 lane. The study SHALL collect first-hand evidence of one practitioner's concrete job, current tool and failure, with consent, and SHALL NOT invent or paraphrase quotes into evidence.

## Primary measures (decision-relevant, on S3 and adjudication)

- PM1 Confirmed-regression precision: confirmed regressions divided by alerts.
- PM2 False-block risk: the share of releases (per class and overall) that a gate using S1 alone would block although no confirmed regression exists.
- PM3 Missed regressions: confirmed regressions found among the non-alert controls.
- PM4 Abstentions: count, share and reviewer minutes spent on CANNOT_DECIDE items.
- PM5 Reviewer minutes per confirmed actionable regression, for each arm.
- PM6 Artifact completeness: how many of the seven parts each arm produces, and whether the replay and CI evidence verifies offline.

Exploratory only, not decision grounds (R3): the earlier M1 (S1/S2 disputed-alert share), M2 (overturn rate), M3 (LOC and minutes cutoffs) and M4 (mistakenness AUROC). Their former cutoffs (15%, 50%, 150 LOC / 120 min, AUROC 0.70 / 0.85) are unvalidated hypotheses.

## Preconditions

- P1 Rights recorded for 100% of evaluated images.
- P2 S3 locked for the full blind sample, with agreement reported.
- P3 Replay identical for 100% of images and both versions.
- P4 Parity of at least 99.5%, with differences explained.
- P5 Event sufficiency is predeclared after the pilot: the minimum count of alerts and controls that gives a Wilson half-width of 0.15 or less for PM1. Falling short means INCONCLUSIVE/HOLD, not product failure.

## Decision rule (proposed, frozen at preregistration)

- INCONCLUSIVE/HOLD: P5 not met, or an interval crosses a threshold.
- NO-GO standalone: the best-practice FiftyOne arm reaches the same release decisions as the harness (same confirmed regressions, no extra false blocks) with PM5 within 25% of the harness. A companion tool is then considered only with separately evidenced extra value.
- Research GO: P1-P4 met, and the harness lowers false blocks (PM2) or reviewer minutes (PM5) against the best-practice baseline by a margin fixed at preregistration, with intervals excluding zero.
- A product GO additionally requires G4 evidence and user approval.

## Out of scope

App code, deployment, public data release, training, paid compute, licensing decisions, and any download or inference during R0.
