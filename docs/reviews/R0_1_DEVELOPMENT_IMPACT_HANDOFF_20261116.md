# Development impact / research change handoff — RCE-20261116-SOL-R0

**Status:** PROPOSED / NOT APPROVED FOR BUILD; requires Research to accept the Sol findings and the corrected Spec. **Do not edit apps/** or **packages/** based on this proposal.

- source research: Public default at `113dc6fb455cfa589567939331e1a8091d4bf2e4`.
- review provenance: user-provided GPT-5.6 Sol output, reported model identity; effort not observable; methodological verdict CONDITIONAL.
- decision: Group B BLOCKED until corrections and separate rights/download approval.
- accepted scientific fact reaffirmed from authors: Sama-COCO's COCO labels were preloaded, making it correlated, not S3 independent.
- affected gate: G1 primarily, G2/G3 design/statistics and G4 practitioner evidence. All remain unverified.
- evidence level: `SOURCE_REVIEWED` and `UNEXECUTED_PROTOCOL_REVIEW`; no `EXECUTED_REAL_DATA` or `INDEPENDENTLY_VERIFIED` upgrade.

## What development can continue to plan
| Task concept | Dependency | Impact | Allowed response |
|---|---|---|---|
| Historical SHA/hashes, deterministic replay, CI manifest | RV-06/07/14, PM6 | L1, KEEP concept | Continue paper schema/test design only |
| S3 oracle loader and geometry match | RV-02–05, G1 | L2, REPLAN | Wait for canonical-box and third-adjudicator/ABSTAIN rule; prepare proposed interfaces, no app code |
| Release-block decision engine | PM1–PM6, P5 | L2, FREEZE | Cannot implement "share of releases" from one A/B pair; define single-pair verdict and test definitions first |
| FiftyOne baseline integration | RV-08/09/10, G3 | L2, REPLAN | Require pinned plugin/version/evaluation config and crossed operator timing protocol |
| Rights-controlled data/model acquisition | RV-01/06, G1/G2 | L2, BLOCKED | Metadata-only request first, exact file/license sizes, no download approval yet |
| User-facing product/deployment | G1–G4 and PRODUCT_GO | L3, BLOCKED | No build until explicitly approved |

## Development chat acceptance challenge
At the next Development ChatGPT session, fetch actual GitHub HEAD and this proposal branch; identify all tasks that depended on invalidated oracle/metric rules; classify KEEP/REPLAN/FREEZE, and send a research question for unresolved S3 fusion rules. **No execution or build should result** from a proposal-only handoff.

## Source and ownership
- Reviewer: Kiro `gpt-5.6-sol` (review-only); effort unknown.
- Next owner: Research ChatGPT + Kiro Opus 5.5 MAX to draft R0.1 changes.
- Second owner: GPT-5.6 Sol to independently re-review R0.1, and Dev ChatGPT to update plan-only task map.
- No merge into default, no automatic state promotion or sync claimed. This packet becomes active only through an accepted integration decision.
