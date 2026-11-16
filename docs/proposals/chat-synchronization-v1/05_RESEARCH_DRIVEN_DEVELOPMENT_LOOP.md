# BLINDSPOT LAB — Research-driven continuous development loop (Proposal v1.1)

> **PROPOSAL ONLY — not activated, no app built.** This addendum extends `00_ARCHITECTURE.md`, which divides Research/Development ChatGPT rooms. The point of this document is to make **development continuously react to validated research direction**, rather than merely read static status at chat start.
> Verified facts on planning date (2026-11-16): public repo, default `chore/kiro-repo-bootstrap`; R0 corrected Spec is published, no demonstrated real A/B or independent S3 run. The default HEAD was `113dc6fb455cfa589567939331e1a8091d4bf2e4` on recheck. Product RESEARCH HOLD; G1-G4 unverified. The R0 Sol cross-family review was not present in the files inspected. Treat all such values as dated checkpoints, **never live state**.

## 1. Core concept: asymmetric but continuous two-way loop

Research directs **WHY / WHAT / WHAT WOULD DISPROVE IT**.
Development continuously tracks **HOW / HOW MUCH / WHAT IS STILL VALID / WHAT CAN SAFELY BE BUILT**.
Kiro executes approved tasks, measures outcomes, and publishes evidence to GitHub.
The user resolves consequential product, licensing, data, money, privacy and architectural forks.

```text
 Research Chat             GitHub SSOT                         Development Chat       Local Kiro
 Problem + evidence  -->   Research Change Event (RCE)  -->  impact analysis --> approved work
 G1-G4 Spec/decision       accepted Spec revision SHA          dependency map       branch / tests
       ^                         |                                  |                 |
       |                         v                                  v                 |
 research question  <--    DEV_TO_RESEARCH handoff    <--  result + uncertainty  <--  test / evidence
       |
 accepted decision  -->  ops/STATUS.md updated by integrator only (NOT an auto-generated chat memory)
```

GitHub stores **the facts and artifacts**, not instant ChatGPT-to-ChatGPT messages. Each chat must **fetch** GitHub on start, before edits, at research-change decisions and after a test/push. The actual developer cannot update automatically while ChatGPT chat is inactive; a future GitHub check can flag stale work, but no agent executes in the background unless explicitly configured.

## 2. What becomes the source of truth?

- **Accepted scientific direction:** accepted `.kiro/specs/**`, `research/**` and `docs/DECISIONS.md` commits with citations and review. Never let an ops summary override a Spec.
- **Current compact status:** reviewed `ops/STATUS.md` (future M0), with exact examined HEAD, phase and gate states. A snapshot, not a secret independent database.
- **Alignment / impact projection:** proposed `ops/DEVELOPMENT_ALIGNMENT.md` maps each development work item to the particular accepted Spec requirement(s) and hashes. It is derived from the Spec + GitHub Issues; never allowed to promote scientific evidence.
- **Handoffs:** immutable files in `ops/handoffs/` with who, what changed, WHY, base and accepted SHAs, evidence, impact, next owner.
- **Execution truth:** Git commit, Kiro `/usage` snapshot, console test transcript, environment and artifact hashes; a chat claim without these is NOT_RUN/UNVERIFIED.
- **Work queue:** GitHub Issues with labels `research`, `development`, `blocked-research`, `ready-plan`, `ready-build`, `needs-revalidation` and links to the accepted Spec revision. GitHub Issues/PRs are recommended only after the manual pilot; do not claim those labels or workflows exist today.

The single `ops/STATUS.md` remains the current-state index. `DEVELOPMENT_ALIGNMENT.md` is a dependency map, not a second competing status. Changes to either occur in **one reviewed integration change**, never via simultaneous writes from both chat rooms.

## 3. Change protocol: Research Change Event (RCE)

Every accepted research-direction change creates a small **RCE packet**, with:
- `change_id`, timestamp KST, `proposed_from` and `accepted_at` **full commit SHA**, `approval_class` (proposal vs approved).
- Research question, what exact earlier assumption was invalidated, original citation and evidence level.
- `changed_spec_ids` (e.g. RV-02/RV-03/RV-04), `research_gate_effect` (G1 etc.), whether thresholds, data rights or acceptance rules changed.
- `impact_level` and `required_action` for each downstream development task, test, UI state and model adapter.
- Which tasks can CONTINUE, which must FREEZE, which require REPLAN, and what counts as their acceptance after the change.
- User decision required? Exact target/side effect. A research chat cannot imply approval to download models or modify architecture.

**Impact levels:**
- `L0 DOCUMENTATION`: sources/copy only, scientific contract unchanged -> continue; update traceability.
- `L1 ADDITIVE`: new evidence/optional requirement with no invalidated contract -> continue unaffected tasks; add tests if relevant.
- `L2 CONTRACT_CHANGE`: schema, oracle, metric, operating point or acceptance change -> freeze **affected** downstream tasks, recalculate tests/estimates, require accepted change before implementation.
- `L3 DIRECTION_PIVOT`: product hypothesis or user job invalidated; incumbent parity or NO-GO -> freeze product-specific work, inventory reuse vs archive, require explicit user decision on consequential scope.

**Priority rule:** a verified rights/security issue or evidence that invalidates the active release decision immediately marks affected work `BLOCKED_REVALIDATION`. The team does NOT delete work automatically; it preserves provenance and proposes reversible change.

## 4. Two-loop development while Research HOLD

Research HOLD must **not** mean Development Chat is idle. Work is segmented:

**Always eligible to PLAN / REVIEW (no product approval needed):**
- Source/requirement traceability and interface contracts as drafts;
- Design review, threat model, portability choices and test plans;
- Kiro task breakdown with estimates and model/effort selection;
- Existing synthetic reference validation and file/hash/CI policy review;
- Evidence export schema and mock sketches labelled as proposed, not a functional contest app.

**Potentially eligible to EXECUTE only with scoped authorization:**
- Docs and workflow checks for cross-chat synchronization;
- Deterministic unit tests around reference-only schemas;
- Isolated proof-of-concept for a **research experiment** when the exact data/model/right/compute scope is approved;
- Reusable adapters, subject to clear provenance and no product claim.

**Blocked until product/data approvals:**
- User-facing product application development in `apps/**`/`packages/**` under present project rules;
- Real dataset/model weights downloads, new dependencies and inference absent Phase5 A.5/A.6 approval;
- SaaS deployment, new LICENSE, paid services or visibility changes;
- Assertions of actual customer value or production readiness while G1-G4 remain unverified.

This separates **preparatory engineering** from **application build authorization**. Do not treat an unmerged proposal as a standing authorization for either.

## 5. Continuous Development alignment algorithm (each work invocation)

1. **FETCH** actual default branch, HEAD SHA, latest accepted `ops/STATUS.md` if installed, `docs/DECISIONS.md`, accepted `.kiro/specs/`, proposed RCEs and relevant PRs.
2. **BASELINE** each active task's `task_spec_sha`, `task_base_sha`, `dependency_ids` and `approval_class`.
3. **DIFF** accepted research changes since the task's last review (not only repository HEAD): `git diff <old_spec_ref> <new_spec_ref> -- .kiro/specs research` plus decision log. Note a doc-only commit might not invalidate tasks.
4. **CLASSIFY** each task: `CONTINUE`, `UPDATE_TESTS`, `FREEZE`, `REPLAN`, `ARCHIVE_PROPOSAL`. Record impact level L0-L3 and explanation; do NOT use "always restart everything".
5. **CHECK AUTHORIZATION**: whether development work is docs/research scaffolding vs explicitly approved research experiment vs user-approved full app build. If the task exceeds its class, stop **that affected task** and request a decision.
6. **PLAN+RUN** only approved tasks with bounded commands, SHA-pinned inputs, Kiro model/effort and per-task credits. Prefer fast, reversible changes, not large speculative rewrites.
7. **VERIFY** unit/e2e/evidence tests and old Phase4 baseline where relevant; distinguish expected Phase4 gate exit 1 from application CI health.
8. **PUBLISH** issue/PR and handoff with verified remote SHA, actual credit delta, scope, source evidence, blockers. An unpublished local result stays `LOCAL_ONLY`.
9. **SYNC**: integrator accepts the change, updates compact status/traceability and sends the next action to Research if there are scientific implications.

Never auto-push or auto-approve a change merely because a new Spec appeared. App branch must not be rebased blindly when research rewrites requirements.

## 6. Concrete example: S2 to S3 change in R0

R0's official Sama source shows Sama-COCO is correlated with original COCO labels. Research changes RV-02/RV-03, defines S3 blind independent labels and keeps G1 UNVERIFIED.

A BAD workflow: dev proceeds implementing S1/S2 as two independent oracles because its old task prompt has not refreshed.

Correct RCE:
- `change_id: RCE-20261116-S3-ORACLE`; `level: L2 CONTRACT_CHANGE`; `accepted_spec: f9b2b026...`.
- INVALIDATED: `two independent labels from COCO and Sama`.
- KEEP: versioned model adapter concept, source hash/replay tests, generic results export schemas (if invariant).
- FREEZE: any code that votes S1+S2 as independent ground truth; any release decision calling S1/S2 disagreement a confirmed false block.
- REPLAN: S3 annotation ingest schema, blind review workflow, abstain path, test fixtures simulating disagreement.
- NOT AUTHORIZED: model download or real S3 annotation execution without rights/reviewer approvals.
- DEVELOPMENT RESPONSE: first provide interface/test design and exact risks; do not claim model A/B results.
- INTEGRATOR: updates accepted Spec and dependency map after review; old code is not silently deleted.

## 7. What changes as a result of an independent review?

If GPT-5.6 Sol R0 review returns PARTLY or NOT RESOLVED for an RV or gate:
- Affected work cards become `NEEDS_REVALIDATION` with the reviewer source SHA and precise file/line.
- Unaffected docs/tests may continue; affected implementation and dependent demos are frozen.
- Research must submit a corrected Spec with clear delta; Development issues a lightweight Impact Report **before Kiro implementation**.
- When accepted, Kiro uses the new exact Spec revision and adds a regression guard preventing the old assumption from reappearing.
- Escalate to user only if product promise, costs, security, privacy, license or architecture materially change.

## 8. Development's required outputs after EACH research change

**Impact report** (not merely a narrative):
- research change ID, accepted SHA, previous Spec SHA, newly required decisions;
- affected work IDs and touched paths, reuse/throwaway risk, estimated effort (observed or estimated explicitly);
- acceptance tests to add/change, test evidence to invalidate, budget/compute/risk implications;
- tasks categorized KEEP/REPLAN/FREEZE and next Kiro action;
- status `WAITING_FOR_RESEARCH` or `READY_TO_PLAN` / `READY_TO_BUILD` only where permission exists.

**Updated, constrained execution packet:**
- fixed cwd, branch and source commit, allowed paths, exact goal, exclusions;
- model/effort, credit ceiling (as user-approved), commands and tests, expected exit results;
- stop on stale SHA, unsupported rights, changed contract or missing approval;
- output commit, real tests, metadata and next owner.

## 9. Trigger points, automation levels and honest limits

**Manual reliable v1:** Research creates a GitHub RCE / PR and tells development chat its link. Development chat also reads the repository at the start of **every** session and pre-task execution. Kiro fetches immediately before changes and push. This is event-driven with explicit human handoff, not background execution.

**Optional GitHub Actions v2:** A read-only PR check compares current accepted Spec file SHA to a declared `task_spec_sha` in each feature PR; if stale, fail check and require impact review. A second check validates RCE fields and rejects unauthorized state promotion. This check can only run on GitHub events, cannot force a ChatGPT conversation to wake or edit itself. Never use automatic code rewriting, merging, or unrestricted tokens.

**Optional scheduled monitoring v3:** only if the user opts in to a separate scheduled agent, summarize pending RCEs/issues and stale tasks at a defined cadence. This is not active and the current plan doesn't require new accounts/automation permissions.

## 10. Success metrics for the coordination process

- **Coverage:** 100% of active development tasks link an accepted Spec revision and RCEs affecting them.
- **Detection:** every accepted L2/L3 change triggers a stale-task flag before the next execution or PR; zero known stale jobs continue as if unchanged.
- **Safety:** 0 unauthorized app builds, downloads, paid deployments or irreversible Git changes.
- **Change efficiency:** measure time from research acceptance to dev impact report, and number of discarded coding hours; set target only after one pilot.
- **Accuracy:** both separate chats report the same accepted gate statuses at a single named Git SHA; reject claims of real model inference from synthetic Phase4 records.
- **Quality:** affected tests/acceptance criteria revised with evidence, and user can replay source links and verified execution.
- **Cost:** use recorded Kiro /usage, not guessed credits. Phase5 +500/+600 and Group A +80 remain as last accepted budgets until changed.

## 11. Activation sequence (not yet approved)

1. Review this addendum with the existing proposal; resolve approval authority and who maintains STATUS/DEVELOPMENT_ALIGNMENT.
2. In a docs-only reviewed ops PR, add `ops/STATUS.md`, `ops/HANDOFF_CONTRACT.md`, `ops/DEVELOPMENT_ALIGNMENT.md` and one real RCE for the R0 S3 transition.
3. Start independent Research and Development chats with the updated role prompts. Have both fetch GitHub at same commit and fill identical state summary; Development produces an impact report for the historical S2->S3 change, not product code.
4. Pilot an actual RCE: research changes a proposed metric; dev marks only dependent work stale, runs no unauthorized code, reports tests needed. Curator reviews outputs and updates accepted STATUS.
5. After two successful manual cycles add simple validator/PR check. Don't start automatic synchronization that silently modifies Spec.

**Decision at this stage:** this is a scoped plan prepared in a proposal branch, not authorization to build the contest app or move default branches.
