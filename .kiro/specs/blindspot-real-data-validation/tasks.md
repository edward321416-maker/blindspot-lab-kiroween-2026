# BLINDSPOT LAB: real-data validation tasks (G1-G3, G4 in parallel)

> STATUS: PLANNED, REVISION R0. Only group A items with evidence in commit history are checked. History: first draft in `03667d6`; R0 revision 2026-11-16 applying `INDEPENDENT_REVIEW_20261116.md`.
> Budget: `docs/PHASE5_RESEARCH_BUDGET_AND_GATES_20261116.md` (soft +500, hard +600; group A +80). Record `/usage` at the start and end of each group.

## A. R0 protocol and source review (no downloads, no models)

- [x] A.1 Read the independent review, the budget doc and the original spec. _Evidence: R0 commit, `docs/PHASE5_R0_CHECKPOINT.md`_
- [x] A.2 Check official sources for Sama-COCO method, COCO terms, model Hub metadata and the Model Comparison plugin; record them in `research/phase5/protocol/DATA_RIGHTS_PREFLIGHT.md`. _Refs: RV-01, RV-06_
- [x] A.3 Write `research/phase5/protocol/ORACLE_INDEPENDENCE_PROTOCOL.md` (roles, sampling, blind annotation, adjudication, limits). _Refs: RV-02 to RV-05_
- [x] A.4 Inventory local hardware and Python without installing anything. _Refs: RV-11_
- [ ] A.5 Cross-family review of this revision in a separate `gpt-5.6-sol` session (high or xhigh), using `docs/PHASE5_R0_REVIEW_PROMPT_GPT56SOL.md`. Record findings and fixes.
- [ ] A.6 User approves the exact downloads (files, sizes, per-image rights filter), the Python environment and whether GPU use is allowed.

## G4. Practitioner lane (parallel, from day 1, no cost)

- [ ] G4.1 Identify one practitioner who compares detector versions for a release, with consent to record their job, current tools and failures.
- [ ] G4.2 Record their actual workflow with FiftyOne or equivalent and where it fails or costs measurable time. No invented or anonymous quotes.

## B. Feasibility (only after A.5 and A.6)

- [ ] B.1 Close the UNVERIFIED rows of the rights preflight (per-image license IDs, upstream license, training split, v2 processor).
- [ ] B.2 Extend `.gitignore` (safetensors, images, FiftyOne database) and confirm with a staged `git status`.
- [ ] B.3 Download only the approved files, verify SHA-256 against the pins and build the manifest.
- [ ] B.4 Create the pinned environment after reading every requirements file as text.
- [ ] B.5 Run the 20-image pilot outside the evaluation frame: wall time, memory, replay identity. _Refs: RV-07, RV-11_
- [ ] B.6 Time S3 labeling on 10 pilot images to size the blind sample and reviewer hours.

## Preregistration (after B)

- [ ] P.1 Freeze the operating point, sample sizes and seeds, P5 event sufficiency, PM thresholds and the decision rule in `research/phase5/protocol/preregistration.md`, and commit before any evaluation inference. _Refs: RV-13_

## C. Harness and S3 (after P.1)

- [ ] C.1 Blind S3 labeling by both annotators; lock and hash the label sets, then adjudicate. _Refs: RV-03_
- [ ] C.2 Run A and B on the frame and replay. _Refs: RV-07_
- [ ] C.3 Outcome engine, sampler and metrics with unit tests, plus a mutation suite that must fail closed. _Refs: RV-08, RV-14_
- [ ] C.4 Blinded alert and control adjudication. _Refs: RV-04_

## D. FiftyOne best-practice arm (after C.2)

- [ ] D.1 Read and pin the Model Comparison plugin code; re-read the current `compute_mistakenness` docs. _Refs: RV-09_
- [ ] D.2 The non-author operator writes the workflow from docs, then runs it timed for all seven artifact parts. _Refs: RV-10_
- [ ] D.3 Parity check against the harness (at least 99.5%). _Refs: RV-08_

## E. Analysis and decision

- [ ] E.1 Compute P1-P5 and PM1-PM6 with intervals and write `research/phase5/REPORT.md`; exploratory M1-M4 in a separate section. _Refs: RV-12, RV-15_
- [ ] E.2 Cross-family check of the report and code.
- [ ] E.3 User decision (INCONCLUSIVE/HOLD, NO-GO standalone, research GO), recorded in `docs/DECISIONS.md`. A product GO also needs G4.
