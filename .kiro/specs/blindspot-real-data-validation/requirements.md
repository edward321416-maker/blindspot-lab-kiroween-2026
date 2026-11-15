# BLINDSPOT LAB: real-data validation research spec (G1-G3)

> STATUS: DRAFT / RESEARCH HOLD / PLANNING ONLY.
> No dataset has been downloaded, no detector has been run, and no benchmark exists for this stage. Every number in this spec is a proposed threshold or an assumption, not a result.
> Provenance: drafted by Kiro CLI 3.3.0 (model `claude-opus-5.5`, effort `max`) on 2026-11-16 KST at the user's request. Not yet independently reviewed. Planning artifact, not contest software.
> When approved, this spec replaces the G1-G3 items in `.kiro/specs/blindspot-regression-gate/tasks.md`. That file stays unchanged.

## Why this stage exists

Phase 4 showed that the gate logic works on 728 synthetic cases (38 NEW_REGRESSION). It cannot show that the idea matters on real data: the labels were synthetic, the two "models" were not real detector releases, and nothing was compared with FiftyOne. Before any app work, this stage tests:

- G1: real images with independent human annotations and measured annotator disagreement.
- G2: two pinned, reproducible versions of a modern object detector, run on identical inputs.
- G3: the same job done in FiftyOne on the same data, with measured effort and coverage.

G4 (a practitioner confirms the unmet need) is out of scope, so a research GO here is not a product GO.

## Research questions

- RQ1 Oracle sensitivity. When A->B regressions are computed against one human annotation source, what share of the flagged objects does a second independent source dispute, and how many of those are label problems rather than real regressions?
- RQ2 Version behaviour. How many per-object regressions and fixes occur between the two versions on consensus labels, and where do they concentrate (object size, class, crowding, lighting proxy)?
- RQ3 Incumbent coverage. What does a competent user need (minutes, custom code, steps) to produce the same release-decision artifact with FiftyOne, and does FiftyOne's own label-error triage already find the disputed alerts?

## Terms

- Version A / B: the released and the proposed detector checkpoint.
- Source S1 / S2: two independent human annotation sets for the same images. S1 is the standard ground truth a typical user would already have.
- Operating point: score threshold `tau` and IoU threshold `theta`, frozen before inference.
- HIT / MISS: a ground-truth object is a HIT for a version if a same-class prediction with score >= `tau` matches it at IoU >= `theta` under COCO-style greedy one-to-one matching; otherwise it is a MISS. Crowd regions are ignored.
- Regression: HIT under A, MISS under B. Fix: MISS under A, HIT under B.
- Consensus object: matched across S1 and S2 (same class, IoU >= `theta_agree`). Disputed object: has no same-class counterpart in the other source.
- Alert: a regression computed against S1.
- Decision artifact, seven parts: (1) per-object regression and fix list; (2) abstentions with reasons; (3) per-condition summary; (4) blinded two-reviewer adjudication record; (5) offline evidence manifest with hashes of images, labels, weights and config; (6) replay result; (7) CI exit code with JUnit and JSON output.

## Requirements (EARS)

- RV-01 Data rights. WHEN a dataset is selected THEN the study SHALL record the image license, annotation license, per-image license IDs and terms URLs with retrieval date, and SHALL exclude images whose license does not permit this research. Images, raw annotations and weights SHALL NOT be committed to Git.
- RV-02 Annotation independence. WHEN a label source is used as ground truth THEN it SHALL be human-made without access to version A or B outputs, and its documented process (annotators, tool, guidelines, any model assistance) SHALL be recorded. Model-generated or model-assisted labels, including FiftyOne mistakenness scores, SHALL NOT count as independent ground truth.
- RV-03 Second source. The evaluation subset SHALL have a second independent source: an existing independent re-annotation of the same images (option A), or a blinded two-reviewer review of every alert plus a control sample (option B).
- RV-04 Blinded adjudication. WHEN reviewers adjudicate an object THEN they SHALL see the image and the candidate box but not the source name, the model outputs or the other reviewer's decision. Each decision SHALL be stored separately with reviewer ID and time. Unresolved disagreement SHALL become ABSTAIN.
- RV-05 Model pinning. WHEN a detector version is used THEN the study SHALL record repository, revision commit, SHA-256 of every weight file, license, training data, library versions, preprocessing config and inference parameters. Weights SHALL be loaded from safetensors or with a safe loader; remote code execution (for example `trust_remote_code`) SHALL stay disabled.
- RV-06 Identical inputs. Both versions SHALL process byte-identical images (SHA-256 checked) in the same environment, and every prediction record SHALL carry the image hash and model hash.
- RV-07 Replay. WHEN inference is repeated with the same pins THEN detections at the operating point SHALL be identical (same set, box coordinates within 0.01 px, scores within 1e-5). Any mismatch SHALL be logged as a reproducibility failure, separate from accuracy.
- RV-08 Independent recomputation. The harness SHALL recompute matches and outcomes from raw predictions and labels and SHALL NOT trust stored verdicts, as in Phase 4 R-04.
- RV-09 Definition parity. The harness and FiftyOne SHALL use identical definitions (same `tau` filter, `theta`, class-aware matching, crowd handling and detection cap). Per-object outcomes SHALL agree on at least 99.5% of non-crowd ground-truth objects, and every disagreement SHALL be explained before any comparison is reported.
- RV-10 FiftyOne baseline. The FiftyOne arm SHALL use a pinned open-source FiftyOne version, the same images, labels and prediction files, and documented features and plugins only. The workflow SHALL be written from the documentation before it is timed, and plugin code SHALL be inspected before it runs.
- RV-11 Effort measurement. For each part of the decision artifact the study SHALL record whether FiftyOne covers it natively, by configuration, by custom code (with lines of code) or not at all, plus operator minutes, steps and errors. Builder-operator bias SHALL be disclosed.
- RV-12 Statistics. Rates SHALL be reported with counts and 95% confidence intervals (image-level bootstrap, 10,000 resamples, recorded seed; Wilson intervals for small samples). Source agreement SHALL be reported as object-level F1 and reviewer agreement as Cohen's kappa.
- RV-13 Preregistration. Definitions, operating point, subset IDs, model pins, metrics and the decision rule SHALL be committed, with the commit SHA recorded, before any A/B inference on the evaluation subset. Later changes SHALL be logged as deviations, and results under changed rules SHALL be labelled exploratory.
- RV-14 Fail closed. A missing license, missing provenance, hash mismatch, replay mismatch or parity failure SHALL block GO.
- RV-15 Honest reporting. Reports SHALL separate measured results from hypotheses, SHALL NOT pool Phase 4 synthetic results with real-data results, and SHALL NOT state benchmark outcomes before the runs exist.
- RV-16 Scope and cost. The study SHALL run locally on CPU with no paid cloud, GPU rental or paid API; SHALL NOT use personal CCTV or face images; and SHALL NOT add code to `apps/` or `packages/`.

## Metrics and proposed thresholds

All thresholds are proposals. The user confirms or edits them in task 3.1, before inference.

| ID | Metric | Strong case | Weak case | No case |
|---|---|---|---|---|
| M1 | Disputed-alert share: share of alerts whose object S2 disputes | >= 15% and CI lower bound >= 10% | 5% to 15% | < 5% |
| M2 | Overturn rate: share of adjudicated disputed alerts that reviewers judge INVALID or AMBIGUOUS | >= 50% | 25% to 50% | < 25% |
| M3 | Incumbent gap: custom code and operator time FiftyOne needs, beyond native features, for the full decision artifact | >= 150 LOC or >= 120 min | in between | < 50 LOC and < 30 min |
| M4 | Incumbent triage: AUROC of FiftyOne mistakenness for ranking disputed alerts above consensus alerts | < 0.70 | 0.70 to 0.85 | >= 0.85 (FiftyOne already triages) |

M2 guards against a false win. If most disputed alerts are real objects that S2 simply missed, abstaining on them would hide real regressions.

Secondary, reported but not decisive: base disputed rate among all objects and how strongly alerts are enriched above it; overlap of the regression sets computed against S1 and against S2; condition concentration; tamper detection in each arm; sensitivity at `tau` 0.3 and 0.7, `theta` 0.75 and a matched-precision operating point.

## Preconditions (all required for any GO)

- P1 RV-01 record complete for 100% of evaluated images.
- P2 Second source for 100% of the subset (option A) or 100% of alerts (option B).
- P3 Replay identical for 100% of images, for both versions.
- P4 Parity of at least 99.5%, with every difference explained.
- P5 At least 30 consensus regressions and 30 consensus fixes at the primary operating point.

## Decision rule (proposed)

- A metric whose 95% CI crosses a decision threshold is inconclusive. An inconclusive decisive metric means HOLD, unless more data can be collected inside the timebox.
- NO-GO: a precondition still fails at the end of the timebox; or M1 or M2 is "no case" (the oracle-uncertainty premise is falsified); or M3 and M4 are both "no case".
- GO, standalone tool: M1 strong, M2 at least weak, M3 strong, M4 at least weak.
- GO, FiftyOne companion (plugin or CI add-on): M1 at least weak, M2 at least weak, M3 weak, M4 at least weak.
- HOLD: any other combination. The user decides, and the reason goes into `docs/DECISIONS.md`.

## Out of scope

App implementation, deployment, public data release, model training or fine-tuning, paid compute, G4 customer validation and safety certification.
