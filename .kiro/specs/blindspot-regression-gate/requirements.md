# BLINDSPOT LAB — Research-to-Product Gate (Draft, NOT approved product)

Status: **SPEC CANDIDATE / RESEARCH HOLD**. No deployment, no cloud billing, no medical/safety certification. This is a scoped **Kiroween 2026** concept to be reviewed before full implementation.

## Users and jobs-to-be-done
- Primary hypothesis: a vision ML engineer has a real camera failure frame and wants it tracked across model upgrades, not merely counted in aggregate mAP.
- Trigger: a new model checkpoint is proposed for release. A named failing scene, its trusted label, and the old/new predictions are available.
- Desired artifact: deterministic regression evidence bundle with human-oracle uncertainty, a condition-specific release decision, and a CI-readable result.
- Customer demand remains **unverified**: no identified user has confirmed that FiftyOne + current workflow cannot solve this task adequately.

## EARS requirements
R-01 WHEN user imports a supported detector-prediction bundle THEN the system SHALL verify declared SHA-256, schema, unique case IDs, positive/negative ground truth and bbox coordinate conventions before scoring. Invalid input SHALL fail closed.

R-02 WHEN a source is synthetic-only, model-generated, or merely proxy-verified THEN the system SHALL label that provenance and SHALL NOT claim independent human correctness or production release permission.

R-03 WHEN an independently reviewed image is supplied THEN the system SHALL record source license, image hash, class ontology, two reviewer identities, their *separate* decisions, bounding boxes, reviewer disagreement and adjudication. It SHALL preserve review uncertainty. Merely typing two review names SHALL NOT be considered authenticated verification.

R-04 WHEN old and new detection predictions are supplied THEN the system SHALL recompute box IoU and per-case accuracy from ground truth, not trust vendor-provided `is_correct` or `verdict` fields.

R-05 WHEN a new regression is found THEN the system SHALL emit a stable case identifier, input hash, transform/severity metadata, model artifact hashes, old/new predictions, and a reasoned decision.

R-06 WHEN a ground-truth label is invalid or ambiguous THEN the system SHALL ABSTAIN and SHALL NOT count the case as a pass or fail.

R-07 WHEN a proposed release violates its *predeclared* regression threshold THEN the CI command SHALL return a nonzero exit status and produce JUnit/JSON/CSV reports. Never derive safety claims from the status alone.

R-08 WHEN the system has only synthetic or unverified ground truth THEN it SHALL keep **production approval blocked** even when the numerical gate passes.

R-09 WHEN a case is replayed with the same saved model and preprocessing THEN the system SHALL compare stored input/model hashes and results, and record reproducibility failures separately from accuracy failures.

R-10 WHEN the user opens a report THEN the system SHALL show summary success rate, newly broken cases, fixed cases, abstentions, failure clusters by condition, and clickable per-case evidence. Every numerical claim SHALL expose dataset/model provenance.

R-11 WHEN the user exports results THEN a portable evidence packet SHALL be produced containing case records, gate status, ground-truth provenance, model version IDs, the scoring policy, and test artifacts.

R-12 WHEN a competitor comparison is presented THEN it SHALL distinguish baseline FiftyOne evaluation/model comparison capabilities from a *measured* incremental advantage. Do not describe existing hit→miss classification as novel.

## Out of scope for this validation phase
- Live cloud inference, downloading unknown model checkpoints, arbitrary Python execution, user account systems, paid resources, physical camera installation guidance, automatic production approval.
- Calling synthetic data "real-world safety evidence", collecting private CCTV or biometric images by default.

## Release gates
- G1 external real-image oracle: legally usable dataset, independent labels, visible disagreement handling and review trace.
- G2 real model versions: stable actual checkpoints, same preprocessing and test dataset; two-version detector comparison.
- G3 incumbent head-to-head: same source data and task compared to FiftyOne + plugin; measure operator minutes, missing/false regression alerts, setup complexity.
- G4 customer validation: at least one *same* practitioner confirms incumbent limitations and unsolved workflow with evidence.
- G5 final product approval only after user reviews G1–G4; competition submission requires Kiro-created working app, public source/license/root `.kiro/`, <3-minute public video and reachable demo.
