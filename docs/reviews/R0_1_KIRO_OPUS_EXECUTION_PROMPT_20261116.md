# Kiro CLI execution instruction: Phase 5 R0.1 — text-only remediation

**Model:** `claude-opus-5.5`, effort `max` (user approved). Use separate GPT-5.6 Sol session later for independent re-review. Do not claim Sol effort high/xhigh unless the running session actually exposes it.

**Local project:** `C:\Users\admin\Projects\blindspot-lab-kiroween-2026`
**Public repo:** `edward321416-maker/blindspot-lab-kiroween-2026`
**Remediation proposal branch:** `review/phase5-r0-sol-remediation-20261116` (read-only planning docs prepared by ChatGPT, not the approved default).
**Review target base:** `113dc6fb455cfa589567939331e1a8091d4bf2e4`

## Before edit
1. Record `/usage`; Phase5 R0 base `110.23`, A/R0 hard increment `80`. Last report cumulative `54.75` at end reading; rest is NOT guaranteed. Limit this correction pass to the **remaining actual headroom**. Stop at R0 cumulative >=80 and do not claim completion if unfinished.
2. Check Git status, the latest default remote HEAD and any local unpushed commits. Do not silently reset/rebase/force push. Current default and proposal branches may have advanced; reconcile before edits.
3. Read `AGENTS.md`, `docs/DECISIONS.md`, existing 3 R0 Spec files, `research/phase5/protocol/{ORACLE_INDEPENDENCE_PROTOCOL,DATA_RIGHTS_PREFLIGHT}.md`, `docs/reviews/PHASE5_R0_SOL_REVIEW_20261116.md` and `docs/reviews/R0_1_CORRECTION_PROTOCOL_20261116.md` from the proposal branch.
4. Check original sources using approved read-only documentation access. FiftyOne `compute_mistakenness` docs: https://docs.voxel51.com/getting_started/object_detection/03_finding_mistakes.html. Do not download/install anything.

## Authorized scope: PLAN ONLY
Produce **unified diffs** for the requirements, design, tasks, oracle protocol and rights preflight implementing C1–C5. Write proposed G4 consent/evidence template if helpful; do not insert sensitive interview notes in public repo. Respect experimental independence: source-independent S3 from locked blinded annotators, third neutral adjudicator or ABSTAIN, deterministic regression based on locked S3; no arbitrary human TRUE_REGRESSION votes.

Define numeric metrics denominators (PM1–PM6) and cluster-aware P5, paired best-practice FiftyOne workflow, metadata-first rights, 20-image no-accuracy pilot, no inference before preregistration, G4 stop gate before C. No fabricated observed thresholds, data, model results, interviews or evidence.

**Never execute:** dataset/model/image/annotation download; env/dependency installation; model inference or training; app code in apps or packages; LICENSE; cloud billing; deployment; main/default branch edit; unsafe scripts.

## Quality gate
- Show every changed path and a SEARCH/REPLACE or unified diff.
- For each Sol PARTLY finding R2–R7, name exact modified requirement IDs, testable acceptance criteria, residual uncertainty and no-evidence cases.
- If budget hit, stop with incomplete blockers clearly labelled.
- When done, make a scoped commit only on a new/review branch after comparing latest default; no merge into default and no force push.
- Report actual model+effort, start/end usage, test commands/results or NOT_RUN, commit SHA and new review dependencies.

After this authoring pass, stop for independent GPT-5.6 Sol read-only R0.1 re-review. **Group B remains blocked; product remains RESEARCH HOLD.**
