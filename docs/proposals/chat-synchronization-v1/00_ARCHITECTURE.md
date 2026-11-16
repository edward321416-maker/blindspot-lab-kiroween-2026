# BLINDSPOT LAB — research/development chat coordination proposal v1

Status: PROPOSAL ONLY. Not installed, not merged, not an automatic synchronization system.
Drafted 2026-11-16 KST from verified GitHub commit f9b2b026b2d619f3c2c764a5149975363e4fb724.

## Current factual baseline
- Public repository: https://github.com/edward321416-maker/blindspot-lab-kiroween-2026
- Default: chore/kiro-repo-bootstrap. No main or LICENSE in checked tree.
- R0 updated Phase5 Spec is present; GPT-5.6 Sol cross-family review still pending in inspected records.
- Product RESEARCH HOLD. G1 real blind labels, G2 model A/B, G3 FiftyOne comparison, G4 practitioner evidence unverified.
- Previous 728 synthetic / 38 new regressions are historical Phase4 evidence, NOT real detector performance.
- Phase5 budget from the existing recorded baseline is incremental +500 soft and +600 hard credits. Live balance requires an actual Kiro /usage reading.

## Design principle: one project, distinct chat responsibilities
GitHub accepted commits + issues + reviewed PRs are the COMMON SYSTEM OF RECORD.
Research ChatGPT chat = hypotheses, citations, G1-G4 scientific validation, Spec proposals.
Development ChatGPT chat = implementable architecture, approved code, tests, Kiro task instructions.
Kiro CLI on Windows = local file operations, tests, commits, PR preparation, actual credit measurement.
User = important irreversible decisions and research/product GO.
Neither ChatGPT conversation auto-reads the other. A local commit is not available to the other chat until pushed or supplied with evidence.

## File layout to INSTALL only after proposal review
ops/STATUS.md                        one curated current-state snapshot
ops/HANDOFF_CONTRACT.md              exact required source/approval fields
ops/handoffs/YYYY-MM-DD_ID_RESEARCH_TO_DEV.md
ops/handoffs/YYYY-MM-DD_ID_DEV_TO_RESEARCH.md
ops/decisions/ADR-0001-title.md      important product/architecture rationale only
docs/DECISIONS.md                    existing append-only decision history
docs/PROVENANCE.md                   existing provenance notes
research/phase5/**                   existing evidence, experimental design and sources
.kiro/specs/**                       Spec draft and accepted requirements
apps/** and packages/**              Kiro-built work only after product GO
.github/PULL_REQUEST_TEMPLATE.md     later, optional
.github/ISSUE_TEMPLATE/*.yml         later, optional
scripts/check_coordination.py        optional after manual workflow is proven

IMPORTANT: ops/STATUS.md is the ONLY curated quick snapshot. Avoid a second editable status.json and avoid copying facts into several conflicting lists. A status entry references the commit it examined; that does not need to equal its own commit (which would be self-referential). Existing docs/DECISIONS.md remains an append-only historical log, not a second live status board.

## Responsibilities and ownership
Research chat OWNS source review, test protocols, source-independent oracle, preregistration, competitor comparisons, G1-G4 and scientific acceptance. It may PROPOSE changes in research/** and .kiro/specs/** on a research branch, but cannot silently alter apps/** or declare product GO.
Development chat OWNS work planning for apps/**, packages/**, tests/**, CI, UI, UX, security and Kiro execution instructions. Before product GO, it may PLAN and REVIEW only. It cannot silently change oracle/label definitions or assert that G1-G4 passed.
Kiro CLI EXECUTES verified local commands, records actual file tree, SHA, test results, models/effort and credits, commits and pushes after approved scope.
Integrator (Kiro or user after reviewed PR) updates ops/STATUS.md on acceptance. Both chats read it but neither silently updates the accepted snapshot from memory.

## Change and handoff lifecycle
1. START EACH CHAT: fetch repository metadata and exact current default/head commit; read ops/STATUS.md if installed, recent docs/DECISIONS.md, accepted relevant Spec and last role handoff. Distinguish accepted GitHub state, proposal branch, local-only work and memory.
2. RESEARCH: create an issue/branch, collect original evidence with source URLs and observed dates, record uncertainties, freeze proposed metrics, submit research-to-dev handoff. A draft is not implementation authorization.
3. DEVELOPMENT: require approved Spec and exact source SHA. Implement only on feat/<scope> or fix/<scope> with tests after product GO. If a requirement is scientifically unsound, hand it back to Research rather than reinterpreting labels in code.
4. FINISH EACH TASK: report source commit, changed files, branch, actual test commands+exit statuses, data/model versions, license/provenance, Kiro usage snapshot if observed, blockers and next owner. Label results LOCAL_ONLY, PUSHED_NOT_REVIEWED or ACCEPTED accurately.
5. REVIEWED TRANSITION: Integrator uses a PR to apply accepted decisions, updates ops/STATUS.md and docs/DECISIONS.md, records the merge SHA. Other chat re-fetches before further work.
6. HEAD DIVERGENCE: stop, compare graphs/diffs and reconcile without force push/reset/undocumented rebase.

## States, approvals, evidence levels
Project states: RESEARCH_HOLD (NOW), SPEC_REVIEW, VALIDATION_AUTHORIZED (exact bounded data/model scope), RESEARCH_GO, PRODUCT_GO (explicit user approval + G4), BUILDING, BUILD_VERIFIED, SUBMISSION_READY.
Scientific gates G1-G4 separately: NOT_STARTED / IN_PROGRESS / VERIFIED / BLOCKED / INCONCLUSIVE.
Evidence: HYPOTHESIS / SOURCE_REVIEWED / REPRODUCED_SYNTHETIC / EXECUTED_REAL_DATA / INDEPENDENTLY_VERIFIED.
Approval: PROPOSAL_ONLY / RESEARCH_EXECUTION_APPROVED / BUILD_APPROVED. A positive research result never silently becomes product GO.

## Branches and GitHub mechanics
Current default is chore/kiro-repo-bootstrap, not main. Until main exists, target actual default with PRs; do not pretend a PR into main is possible.
Use research/<task> for scientific work, feat/<task> for authorized code, review/<task> for cross-family review, ops/<task> for status and contracts.
Do not edit accepted shared files in two branches without a PR. In particular, only integrator updates ops/STATUS.md after evidence review.
After a manual pilot, optionally introduce protected main + required reviews/checks. No branch/admin policy changes are authorized by this planning document.
Issues are actionable task records, PRs are reviewable changes, immutable handoffs are cross-chat exchanges, decisions are accepted rationale. These are distinct roles; a new automation is not needed initially.

## Freshness and budget rules
Read GitHub at every chat start, before edits, after a material result, before push and at gate transitions. If there is no connector, disclose the limitation; public repo URL can be read with normal web tools but is not writable without permissions.
Never claim local Kiro work is synchronized until remote SHA/tree has been read back.
Measured Kiro credit usage belongs to a dated record with /usage; no guessed current balance.
Keep the approved Opus 5.5 MAX policy for Opus work; actual GPT-5.6 Sol access and effort should be recorded when used.
Public repo: don't push passwords, tokens, private images, raw datasets, third-party models or licensed photos without permission.

## Rollout plan (all unimplemented)
M0 - Manual setup: add ops/STATUS.md + ops/HANDOFF_CONTRACT.md from templates via docs-only PR; do not install CI yet.
M1 - Pilot: launch fresh Research ChatGPT and Development ChatGPT with the role starter prompts, make each report the same remote SHA and G1-G4 state; dev correctly refuses unapproved app development.
M2 - Real exchange: one R0 cross-family reviewer finding becomes RESEARCH_TO_DEV handoff; dev replies with questions or allowed plan-only task; integrator reviews and updates STATUS.
M3 - GitHub collaboration: add Issues and PR templates; verify stale-SHA blocker and branch conflict handling using dry runs.
M4 - Optional validator: build a Python standard-library coordination check and GitHub Actions status check for handoff fields and dangerous state promotion. No auto-write to STATUS and no remote code execution from untrusted PRs.

## Acceptance criteria
T1 both new chats report same HEAD and RESEARCH_HOLD.
T2 a local-only SHA is not called pushed.
T3 source findings never silently become independently verified experiments.
T4 dev refuses code build if PRODUCT_GO absent.
T5 each handoff lists exact SHA, evidence link, tests, next owner and required approval.
T6 no force push/main creation, no history/data loss.
T7 Phase4 18 tests and intentional gate exit 1 remain valid.
T8 public repo secrets/licensing checks occur before publishing.
T9 status changes are tied to reviewed commits, not ChatGPT memory.

User decision requested later: approve implementing M0/M1 ONLY (docs/coordination). This proposal alone does not approve dataset download, licenses, model inference, app build, cloud costs, publication of sensitive assets, or main branch changes.

Official GitHub guidance: https://docs.github.com/en/pull-requests/reference/status-checks
Branch protections: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
Issue forms: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
