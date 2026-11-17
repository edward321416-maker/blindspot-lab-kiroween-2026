# Kiro — correct ADR-0006 audit provenance, then B5.2 planning ONLY

**Date 2026-11-18 KST. Authorized target when user pastes this pinned instruction:** a **reversible local docs-only correction** and **read-only/design-only output policy evaluation**. No security source edits, no new QA subagents, no rerunning B5.1 implementation, no D1E actual arm or D2 app.

## 0. Exact GitHub sources (use pinned commit from the user's short prompt)

- `docs/handoffs/recollection-d01/31_ALIGNMENT/B5_1_COMPLETION_MODEL_PROVENANCE_AND_RESEARCH_3_14_20261118.md`
- `docs/handoffs/recollection-d01/32_PLANS/B5_2_VISITOR_OUTPUT_POLICY_AND_RENDERER_CONTRACT_PROPOSAL_20261118.md`
- `docs/handoffs/recollection-d01/27_PLANS/D1E_EXPERIMENT_PREREGISTRATION_PREP_NO_EXECUTION_20261118.md`
- `docs/handoffs/recollection-d01/24_PLANS/RECOLLECTION_3_12_CONCRETE_PRODUCT_INTERACTION_CONTRACT_20261117.md`
- `docs/handoffs/recollection-d01/30_RESEARCH/RECOLLECTION_3_14_MULTIDOMAIN_SOURCE_LAB_20261118.md`

No confidential research holds/answers or private 3.14 ZIP contents in public docs or Kiro dev repo. The latest 3.14 research is **not** a product regression test.

## 1. Main model ONLY and local repository safety

Expected local repo `C:\Users\admin\Projects\recollection-kiroween-2026`, branch main, clean with no remote, HEAD `101836551883aae0e5fc179100538de2e5beeacb`. Check this in read-only Git before any write. If already corrected in later commit, don't repeat. If mismatched or dirty, stop without reset/rebase/stash.

Use the existing **main Kiro session** configured `claude-opus-5.5` / `max`, no Auto/fallback. **DO NOT spawn any subagent or delegate**: its model cannot reliably be pinned, and an earlier subagent used 4.8. The historical drift must be reported; don't claim all prior runs were 5.5. Do not ask user again for /model or /usage screenshots. Saved effort only `SESSION_CONFIG_ONLY`, pool credit `BONUS_USAGE_UNOBSERVED` if not independently available. Do not invoke paid/cloud or unapproved model.

Protected GhostWeb dirty worktree / BLINDSPOT local unpushed state untouched. No repo remote, no push/public code.

## 2. Factual correction of committed ADR-0006 — documentation ONLY

Read local `docs/decisions/ADR-0006*` actual file, exact report-directory `B5_1_ADR_0006_ERRATUM_PROPOSED.md` and `MODEL_PROVENANCE.md`, and actual Kiro model logs **by read-only local access if available**. If files differ, preserve and report specifics, do not improvise evidence. Do not repeat the entire B5.1 QA just to correct a source citation.

Correct in a **new additive docs-only commit**, preserving original Git history, using unified diff/SEARCH-REPLACE:
- Original `ADR-0006` called B5.1 subagent challenge `SAME_MODEL`; amend the current **document contents or add a linked erratum** saying the *subagent run was MIXED_MODEL / MODEL_POLICY_VIOLATION*.
- It ran **eight Opus 5.5 events** around 01:18–01:22 KST, then **fifteen Opus 4.8 events** around 01:28–01:44 KST, 2026-11-18, as reported from session logs. This violated the instructions; the model was not pinned within that subagent.
- Primary main session reportedly ran Opus 5.5 events and reran the probes against final B5.1 commit, including 65-case B5→B5.1 differential. `B5_1_PATCH_PASS` is an outcome from **main-session tests and replay**; this is not retroactive compliance for the subagent. Effort not per-turn attested, no independent human QA.
- Keep an audit pointer to local `B5_1_CHALLENGE_MIXED_MODEL` bundle, existing erratum and preserved original logs. Distinguish `MAIN_SESSION_REVALIDATED` from `SUBAGENT_MIXED_MODEL` in new record. Do not rename old commits or delete historical evidence.
- Only local Markdown/decision or report index changes allowed. Any other source `src/**`, `tests/**`, `tools/**`, `reports/evidence/B1-B5.1*`, `package.json`, frozen oracle, history and external projects must remain byte-unchanged. If correction already done, report status `ERRATUM_ALREADY_PRESENT` and don't create duplicate commit.

Check `git diff --check`, exact changed paths, source tree SHA of frozen code, Git clean state, and commit once only if documentation correction is genuinely required. Run no unnecessary full 194-case suite for docs-only changes, but explicitly mark tests `NOT_RUN_DOCS_ONLY` and reference latest B5.1 measured results without claiming they were newly executed. Give full new local SHA and unified diff. Don't write a model log summary contrary to actual logs.

## 3. Planning-only B5.2 / D1E choice

- Review B5-01/02/11/24 visitor-output hazards and the newly published `32_PLANS` output policy **as a PROPOSAL**. Do not alter code, fixed ExperienceSpec 0.2 schema, 2–4 item count or R3.5 unsafe-text block rule.
- First product vertical slice uses two **owned synthetic** records and two questions (Research 3.11–3.12); 3.14's 12 multi-domain scenarios are research leads, not imported actual customer data or hidden oracle.
- Recommend **D1E B-approach** for eventual product-quality comparison: compare two arms after C2 actually has a safe viewer. Until then keep `C2_COMPARATOR_NOT_READY` and `D1E_EXECUTION_HOLD`. Optional A approach as contract-only technical experiment **with separate prereg/approval**, not a product-quality substitute.
- Draft a one-page `B5_2_DECISION_BRIEF.md` in the approved local report directory (or cite 32_PLANS GitHub if docs already sufficient): source/output sink allowlist, review/rights digest, conservative dependency invalidation, security/benign test design, likely new adapter seam and precise user approval requirement. This is *planning*, not accepted schema.
- Human roles (independent oracle author, rights reviewer, blind scorer) remain **UNASSIGNED**; user need not name anyone for this planning stage. Budget `UNKNOWN`; no arbitrary credits allocated. Do not run C1/C2, add actual renderer, download museum media or publish.
- If writing report directory sidecar files, preserve original evidence, compare SHA before and after and mark local `PENDING_SYNC` if Sheets connector absent. **Never claim Google Sheets synchronized from Kiro**.

## 4. Final response to user

Korean status:
- exact local HEAD before / after, changed docs-only paths and unified diff, model log provenance `SUBAGENT_MIXED_MODEL` vs `MAIN_SESSION_REVALIDATED`;
- tests `NOT_RUN_DOCS_ONLY` versus prior reported 194/194, and actual code/fixtures unchanged;
- report URL/path and research sync status 3.14 research-only;
- B5.2 proposal: proposed typed output/review adapter, P1 visitor/publishing HOLD, recommended D1E B, roles/budget pending;
- **STOP**. No B5.2 implementation/D2/D1E execution, new subagents, AWS/Bedrock, GitHub remote/push, arbitrary output text, new npm package or paid credits.

**This instruction is for correction + planning. Later implementation of the B5.2 adapter, safe renderer or publication requires explicit user approval for changed product architecture/security/cost.**
