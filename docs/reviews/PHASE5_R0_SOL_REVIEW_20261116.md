# Phase 5 R0 — GPT-5.6 Sol cross-family review record

**Status:** CONDITIONAL / R0.1 CORRECTION REQUIRED / GROUP B BLOCKED.
**Provenance:** Findings supplied by the user as the output of a separate Kiro CLI `gpt-5.6-sol` review session, reported 2026-11-16 KST. This record was prepared by ChatGPT from that user-supplied report and direct readback of the public source files at `113dc6fb455cfa589567939331e1a8091d4bf2e4`. ChatGPT **did not execute the Kiro Sol session**, and no independent runtime benchmark or human labels were produced.

- Review source SHA: `113dc6fb455cfa589567939331e1a8091d4bf2e4`.
- Model identity: `gpt-5.6-sol` reported and verified by live Kiro metadata.
- Effort: **UNKNOWN / NOT OBSERVABLE**. User requested xhigh, but the Sol review reported the running effort was not observable; do NOT claim it used xhigh or high.
- Working tree: clean throughout, review-only. No downloads, installs, inference, tests, file modifications or commits by Sol.
- Kiro /usage: start `142.44 / 4000` at 13:21 KST, end `164.98 / 4000` at 13:24 KST; observed delta `22.54`. Baseline `110.23`, R0 cumulative `54.75 / 80`, headroom `25.25` **at end reading, exclusive of final chat-message cost**.
- This note is a **public review record**, not acceptance of revised requirements and not approval to begin Group B.

## R1–R7 verdicts

| Finding | Sol verdict | Required correction / evidence |
|---|---|---|
| R1 Source independence | **RESOLVED** | Sama-COCO = correlated COCO revision. Source-independent S3 must be labeled from scratch. No G1 pass until actual labels exist. |
| R2 Annotation vs alert adjudication | **PARTLY RESOLVED** | Two contributors cannot each become the adjudicator "who did not cause disagreement"; independent third party or ABSTAIN. Lock S3 before inferencing. Compute regression mechanically; human reviewers assess annotation validity only. Canonical box rules need preregistration. |
| R3 Metrics and decision rules | **PARTLY RESOLVED** | PM1 denominator/alert population, PM2 one-release impossibility, PM3/PM4 denominators, PM5 randomized operator timing, PM6 binary acceptance rubric. Cluster-aware CIs, a primary endpoint and predeclared practical margin. |
| R4 Incumbent fairness | **PARTLY RESOLVED** | Pin FiftyOne and every evaluation option, Model Comparison plugin revision and license. Equal operator proficiency, randomized/counterbalanced workflows, cold/warm timing, modest reasonable CI script. |
| R5 Pilot and clustered observations | **PARTLY RESOLVED** | Preregister seeded 20-image smoke subset (not eval set), cache warm-up/repeats/resource limits, no accuracy peeking, and image-cluster sampling rather than independent-object Wilson P5. |
| R6 Rights and safe loading | **PARTLY RESOLVED** | Existing B.1/B.3 circularity: image license ID requires annotation metadata. Require separately approved **metadata-only** retrieval first, then per-image copyright check before image download. Correct model training split and v2 processor ambiguity. |
| R7 Practitioner evidence | **PARTLY RESOLVED** | G4 consent form and case schema, deadline + explicit pre-C stop gate. Do not claim verified customer demand from general posts or synthetic experiments. |

## Highest-risk methodological issue

The current R0 source `ORACLE_INDEPENDENCE_PROTOCOL.md` uses a two-person team both to create labels and later vote TRUE_REGRESSION. That risks circular evidence. **S3 must be source-independent and locked first; actual HIT→MISS transition is a deterministic function of frozen S3 and frozen predictions, not a human vote about the model change.**

Operationally:
1. Both blind annotators see original image and neutral ontology, not COCO/Sama/model output, and separately sign/hash/lock labels before comparison.
2. Agreements use a preregistered class/IoU/coordinate-fusion rule; nontrivial disagreements go to a genuinely separate third adjudicator with blinding, otherwise ABSTAIN.
3. After S3 is locked, A/B predictions are matched against S3 by frozen class/score/IoU/crowd rules. A HIT and B MISS defines a TRUE S3 REGRESSION mechanically.
4. Reviewers can flag an S3-label-validity dispute or ambiguity; they do not substitute subjective votes for the model transition.
5. Image/object/decision denominators, alert sampling and abstention treatment must be specified before seeing evaluation results.

## Source-checked distinctions

- Sama-COCO creators explicitly say original COCO labels were preloaded: https://www.sama.com/sama-coco-dataset
- COCO annotations are CC BY 4.0 but COCO does not own Flickr images: https://cocodataset.org/dataset/termsofuse.htm
- FiftyOne community Model Comparison covers `hitmiss`/`misshit`, but needs separate code/version audit: https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- FiftyOne `compute_mistakenness` is model-prediction-conditioned label triage, NOT independent ground truth: https://docs.voxel51.com/getting_started/object_detection/03_finding_mistakes.html
- User-supplied Sol report cited Model Comparison community commit `d0579c7fbd3ca82f3d18311330cedda7d7a3cc10` and Apache-2.0; **verify the exact immutable commit and its license before relying on them**.

## Approval status / blocker summary

**Group B is NOT approved.** No image archive, annotation manifest, model safetensors, Python environment or FiftyOne packages have been authorized for retrieval/installation. Requirements and protocols remain DRAFT; original R0 spec is preserved. Next action: repair seven partials in an auditable research-branch commit; perform a non-authoring independent review of the *revised* protocol; then request exact, scoped approval for metadata/rights and feasibility. G1–G4 still unmet. Product remains RESEARCH_HOLD.

No work in `apps/` or `packages/`; Kiro Opus MAX allowed for authorized protocol edit only. Historical Phase 4 728 synthetic cases and intentional 38 NEW_REGRESSION failures are unchanged.
