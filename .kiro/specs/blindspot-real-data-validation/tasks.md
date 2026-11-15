# BLINDSPOT LAB: real-data validation tasks (G1-G3)

> STATUS: PLANNED. Nothing below has started. Check a box only with evidence (commit, file or transcript).
> Model routing follows `docs/KIRO_CLI_MODEL_EFFORT_POLICY_20261116.md`. Record model, effort and `/usage` at the start and end of each task group.

## 0. Approval and review (no data, no models)

- [ ] 0.1 User approves or edits this spec: the thresholds in requirements.md, the timebox and credit ceiling in design.md, and downloading the public data and weights (a few GB, see design.md) to local disk. _Refs: RV-13, RV-16_
- [ ] 0.2 Independent review of the three spec files in a separate session with a different model per the policy (for example `claude-sonnet-5.5` high, or `gpt-5.6-sol` high after confirming it is available). Log findings and resulting changes.

## 1. Data due diligence (G1)

- [ ] 1.1 Record license texts and terms for COCO 2017 images and annotations and for Sama-COCO (URLs, retrieval date) in `research/phase5/protocol/data_rights.md`. _Refs: RV-01_
- [ ] 1.2 Establish from direct statements (Sama documentation, its published paper) whether Sama-COCO was annotated without COCO labels or model pre-labels. If this cannot be established, switch to option B. _Refs: RV-02, RV-03_
- [ ] 1.3 Extend `.gitignore` for data, weights and the FiftyOne database. Download val2017 images and both annotation sets into `research/local-only/`, record archive and per-image SHA-256, and build `manifest.json`. _Refs: RV-01, RV-06_
- [ ] 1.4 Run the cross-source agreement analysis (no models): consensus and disputed sets, disagreement types and the base disputed rate. Visually check 30 random disagreements to confirm the matcher. _Refs: RV-12_
- [ ] 1.5 Choose option A, B or C by the selection rule in design.md and record it in `docs/DECISIONS.md`.

## 2. Model pinning (G2)

- [ ] 2.1 Verify the candidate checkpoints (model-card license, revision SHA, safetensors files, training data, published COCO metrics) and record them in `research/phase5/protocol/models.md`. _Refs: RV-05_
- [ ] 2.2 Create the harness environment with pinned, hashed requirements (CPU torch, transformers, pillow, numpy). Read every requirements file as text before installing. _Refs: RV-05_
- [ ] 2.3 Write the inference runner with deterministic CPU settings and schema tests. _Refs: RV-05, RV-06_
- [ ] 2.4 Smoke test on 20 images that are then excluded from evaluation. Measure seconds per image and run replay twice. _Refs: RV-07_
- [ ] 2.5 Fix the subset: all eligible val2017 images if A, B and replay fit in about 8 CPU hours, otherwise a seeded random subset of at least 2,000 images.

## 3. Preregistration

- [ ] 3.1 Freeze definitions, operating point, thresholds, subset IDs, model pins, metrics and the decision rule in `research/phase5/protocol/preregistration.md`. Commit and record the SHA before task 4.1. _Refs: RV-13_

## 4. Harness arm

- [ ] 4.1 Run A and B on the subset and store predictions with image and model hashes. _Refs: RV-06_
- [ ] 4.2 Replay both versions and compare. Any mismatch blocks GO. _Refs: RV-07, RV-14_
- [ ] 4.3 Implement the outcome engine and metrics with unit tests for matching, crowd handling, abstention and the bootstrap. _Refs: RV-08, RV-12_
- [ ] 4.4 Run a mutation suite (label, prediction, model hash, config and image-byte tampering). The harness must fail closed on all of them. _Refs: RV-14_

## 5. FiftyOne arm (G3)

- [ ] 5.1 Capability inventory for the seven decision-artifact parts and Phase 4 R-01 to R-12, with links to the pinned version's docs and executed snippets. _Refs: RV-11_
- [ ] 5.2 Write the FiftyOne workflow from the docs before timing it. The operator is the team member who did not write the harness. Read plugin code before running it. _Refs: RV-10_
- [ ] 5.3 Timed run: minutes, custom lines of code, steps and errors for each artifact part. _Refs: RV-11, M3_
- [ ] 5.4 Parity check of per-object outcomes against the harness: at least 99.5%, every difference explained. _Refs: RV-09_
- [ ] 5.5 Mistakenness triage: AUROC for ranking disputed alerts above consensus alerts, computed from A's and from B's predictions; report the higher. _Refs: M4_

## 6. Blinded adjudication (G1 review trace)

- [ ] 6.1 Draw a seeded sample of 60 to 100 disputed alerts plus 30 consensus alerts as controls, and build blinded review sheets. _Refs: RV-04_
- [ ] 6.2 Two reviewers decide independently into separate files. Compute kappa. Unresolved items become ABSTAIN. _Refs: RV-04, RV-12, M2_

## 7. Analysis and decision

- [ ] 7.1 Compute P1 to P5 and M1 to M4 with CIs, apply the decision rule and write `research/phase5/REPORT.md`, labelling measured results, hypotheses and deviations. _Refs: RV-15_
- [ ] 7.2 Independent check of the report and code by a different model family or a person. Self-review does not count.
- [ ] 7.3 User decision: GO standalone, GO as FiftyOne companion, NO-GO or HOLD, recorded in `docs/DECISIONS.md`. A GO here still needs G4 before a product GO.

## Proposed schedule (two people)

| Day (KST) | Task groups |
|---|---|
| 2026-11-17 | 0, 1 |
| 2026-11-18 | 2, 3 |
| 2026-11-19 | 4, 5.1 to 5.2 |
| 2026-11-20 | 5.3 to 5.5, 6 |
| 2026-11-21 | 7 |
