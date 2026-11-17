# Re:Collection — B0 completed, B1 entry gate (2026-11-17)

**Status: B0 USER-REPORTED COMPLETE / B1 HOLD PENDING NEW /usage AND /model.** This is a *project-state correction* to `12_WORKFLOWS/KIRO_D1_BUILD_B0_RESUME_CONDITIONAL_20261117.md`. The earlier B0-resumption condition must NOT cause the B0 project to be recreated or the oracle frozen again.

## 1. Local state reported by Kiro at 2026-11-17 16:21 KST

- Workspace: `C:\Users\admin\Projects\recollection-kiroween-2026` **already exists and is populated**.
- Git: local-only `main`, full HEAD `6367d928b7eb17a4bd8b6283690bc7c265fa875b`; **no remote**, clean worktree.
- B0 commit: frozen design and synthetic evidence, Python-authored independent oracle (29 validation cases, 6 runtime cases, 13 integer-only JCS vectors), 3 guard tests reportedly passed on two runs.
- Historical diff report on user's local drive: `D:\Users\admin\Desktop\hackathon\ReCollection_D1_BUILD_reports\B0_6367d92.diff`. This diff and local code are **not uploaded or byte-verified by ChatGPT**; do not assert a third-party code review or independently verified test run.
- Protected existing projects: GhostWeb reportedly HEAD `23b8a010`, dirty two files; BLINDSPOT reportedly HEAD `c073ddd1`, one unpushed commit. **Do not touch either.**
- This GitHub handoff is on a PUBLIC docs-only branch unrelated to the local Re:Collection repo; NO local repo remote exists. Do not add one.

The above facts are **KIRO_USER_REPORTED**, not directly read from the user's Windows local files by this GitHub document author. Kiro must re-verify HEAD and clean state before B1.

## 2. Credit baseline and checkpoints

The user previously provided a real interactive Kiro `/usage` readback **approximately 2026-11-17 15:02 KST**:

- Bonus pool `kiroween-20-26` **used = 513.26 / 4000**, plan-included 0/50, session metric 226.45 (NOT the bonus pool).
- The **original, immutable D1-BUILD credit accounting baseline remains 513.26**, covering B0 and future B1–B5. **Never reset to a new /usage value to evade the cap.**
- Incremental B0–B5 soft stop = bonus **used 733.26** (start +220).
- Incremental hard stop = bonus **used 813.26** (start +300).
- **CURRENT bonus used is UNAVAILABLE**. Kiro last report's `Credits: turn 10.12 / session 285.64` does NOT constitute `/usage` and cannot quantify B0 usage.
- Require a freshly user-observed `/usage` bonus-pool used number and KST observation time **now**, before B1 implementation.
- Once obtained, `B0+preflight consumption since original baseline = newBonusUsed - 513.26`, `remainingToSoft = 733.26 - newBonusUsed`, `remainingToHard = 813.26 - newBonusUsed`. Negative/uncertain values => STOP; if current used is close to soft limit, checkpoint and choose whether to reduce B1 scope before coding. Keep direct observations distinct from estimates.
- Record `/model` showing actual active `claude-opus-5.5`, `effort max`, `fallback None` where exposed. Saved session JSON is only SESSION_CONFIG_ONLY; do not silently switch to Auto/another model. If interactive observation unavailable, mark MODEL_UNVERIFIED/EFFORT_UNKNOWN and STOP before substantial B1 work.

## 3. B1-only entry and expected output

**Authorize no fresh scope by reading this file.** Existing user approval is only the previously scoped synthetic-only B0–B5, Node24 + zero initial npm deps, four proposed primitives, isolated local Git/no remote, no D1E/D2/AWS/GitHub push/deployment. The original Master Audit binary remains unverified on Kiro PC; the narrower accepted source contract applies if approved in that Kiro session.

**Only after observed /usage + /model and existing approval are verified:**
1. In the **existing** Re:Collection local workspace, read the B0 frozen oracle and requirements at `6367d928b7eb17a4bd8b6283690bc7c265fa875b`. If worktree dirty or HEAD differs, STOP and reconcile without reset/rebase/stash.
2. Verify the **B0 artifacts as actual local files** and guard test evidence; do not rewrite/freeze B0 a second time. Do not regenerate frozen oracle based on B1 code/results.
3. Implement **B1 only**: ExperienceSpec v0.2 contract, `schemaVersion == "0.2"`, reject unknown fields/versions, separate AI-owned `claims/plan/graph` from privileged system-only `verification/curatorApproval/publication`, integer-only RFC8785/JCS subset canonical SHA with 13 original frozen vectors, deterministic validation errors.
4. Node24 built-in tools first; no npm install and no fake static type-check PASS from Node's type-stripping.
5. Run actual B1 tests twice with exact process exit codes; report case names and frozen B0 artifact SHA, full local Git commit SHA, unified diff, report where code/test evidence is stored; do not push.
6. Check actual `/usage` again; compute cumulative consumption and remaining headroom from **513.26**, not from the latest snapshot.
7. **STOP after B1** and submit Korean checkpoint report. B2–B5 require new stage checkpoints under the same approved overall budget; do not start D1E or D2.

## 4. If observed measurements are unavailable

Do not loop on D0 reviews, duplicate B0 setup, or ask the agent to invent counters. Send the user a **single concise instruction**:

- In Kiro's interactive CLI run `/model` and read model, effort and fallback; run `/usage` and copy bonus `kiroween-20-26` used/4000 and current KST timestamp.
- Keep all B0 files, branches and source projects unchanged.
- Once user pastes both observations, continue from the existing B0 HEAD to B1.

**Result right now: B0 COMPLETE (user report); B1 HOLD; not product GO.**
