# Kiro CLI — Phase 5 R0 only: fix the real-data validation research spec

**HARD SCOPE:** This task is permitted design/source-review work only. NO bulk dataset downloads, NO model weights, NO inference benchmark, NO arbitrary model pickle code, NO training, NO app in `apps/` or `packages/`, NO license/publication/deployment/account changes. Keep RESEARCH HOLD.

## Environment and model
- Local root: `C:\Users\admin\Projects\blindspot-lab-kiroween-2026`
- GitHub: `edward321416-maker/blindspot-lab-kiroween-2026` (PUBLIC)
- Branch: `chore/kiro-repo-bootstrap`
- First fetch; if local clean, fast-forward to current remote HEAD. Do not reset, force-push, rebase an unpushed local commit or alter history without reconciliation.
- Preferred lead: `claude-opus-5.5`, effort `max` (user already approved). The user reports `gpt-5.6-sol` and `claude-sonnet-5.5` are listed; for **independent revised-Spec review**, use a separate `gpt-5.6-sol` session if selectable with high or xhigh. If a model switch needs human UI action, report that, do not claim completed cross-family review.
- Read `/usage` before and after. Stage 5 incremental soft +500/hard +600, **group A cap +80**. Do not confuse with the completed 100-credit bootstrap budget.

## Inspect before edits (source of truth)
1. `AGENTS.md`, `docs/DECISIONS.md`, `docs/KIRO_CLI_MODEL_EFFORT_POLICY_20261116.md`.
2. All 3 files under `.kiro/specs/blindspot-real-data-validation/`.
3. **Independent desk review:** `.kiro/specs/blindspot-real-data-validation/INDEPENDENT_REVIEW_20261116.md`.
4. **Stage plan:** `docs/PHASE5_RESEARCH_BUDGET_AND_GATES_20261116.md`.
5. `docs/PROVENANCE.md`, existing Phase 4 source summary. Consult official links in the independent review; verify content and date, not only names.

## Must correct in a reviewable Spec update
- **R1:** Sama-COCO was derived from preloaded original COCO annotations, so COCO + Sama is **not two independent blind label sources**. Preserve as a correlated annotation-version study only; design a separately independent human blind-from-scratch annotation sample. Do not characterize mere disagreement as label error.
- **R2:** Distinguish blind original annotation from adjudication prompted with a candidate box/model alarm; preregister non-alert controls and audit sample selection, and record review independence limitations of the two-person project.
- **R3:** Rework decisive metrics around independently verified regression-precision, false-block risk, missed controls, abstentions, actionable reviewer minutes, CI evidence/replay. Treat prior M1/M2/M3/M4 cutoffs as exploratory research hypotheses, not validated decision grounds.
- **R4:** A fair incumbent baseline includes official FiftyOne detection evaluation + community Model Comparison `hitmiss/misshit` + `compute_mistakenness` + modest documented code/CI. Separate 7 output artifacts; no weak GUI strawman.
- **R5:** Do not mandate 2,000 images or 8 CPU-hours before measuring 20 non-evaluation smoke images. Predeclare event sufficiency and classify lack of enough fixes/regressions as INCONCLUSIVE/HOLD rather than product failure. Do NOT run that smoke test during R0.
- **R6:** COCO annotations have CC BY 4.0 but images belong to Flickr authors; collect per-image license/rights plan before downloads. Pin exact RT-DETR/RT-DETRv2 model revisions, safe `safetensors`, library versions, checkpoint licenses, source citations.
- **R7:** Start a *parallel read-only G4 lane* identifying the same practitioner's concrete unsolved job after real incumbent use; do not invent customer quotes.

## What to write
- Amend `requirements.md`, `design.md`, `tasks.md` as a **unified diff** for review. Preserve their origins and draft status, no fabricated completed checkboxes.
- Add `research/phase5/protocol/DATA_RIGHTS_PREFLIGHT.md` (sources/licenses/uncertainties) and `research/phase5/protocol/ORACLE_INDEPENDENCE_PROTOCOL.md` (roles, sampling, blind annotation, bias/abstain), **text only**.
- Add `docs/PHASE5_R0_CHECKPOINT.md` with confirmed/uncertain/blocked information, exact URLs and observed /usage.
- Update `docs/DECISIONS.md` with the observed R0 status; keep full history and Phase4 reference data unchanged.
- Recheck existing Phase4 tests only if required for safety; if run, record actual command and outcome. No promise of a new measured object detection result.
- Commit on current branch only after reporting the intended file list and scope; follow `AGENTS.md`. Do not create `main`, open a PR, or change visibility.

## Exit criteria
- All seven review findings explicitly addressed, independent oracle unconfused with correlated Sama data.
- Data/model licensing unresolved facts clearly marked, not asserted as verified without sources.
- Read-only source review and revised Spec all evidenced by Git commit, with real observed budget delta.
- Send the revision for cross-family review before any dataset/model download or GPU/CPU benchmark.
- **No product GO**; no codebase implementation or contest submission claims.
