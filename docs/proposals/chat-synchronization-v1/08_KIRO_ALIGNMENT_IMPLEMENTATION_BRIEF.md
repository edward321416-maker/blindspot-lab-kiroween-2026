# Kiro CLI implementation brief — research-driven dev alignment (future M0-M2, approval needed)

Status: PROPOSED workflow implementation, NOT executed. Do not touch application code or historical research reference during coordination rollout.

## Purpose
Build a small, deterministic coordination layer so a Development ChatGPT room can read current Research direction, detect changed requirements and maintain an engineering plan that cannot silently lag an accepted Spec. This is NOT autonomous ChatGPT chat synchronization and NOT permission to build a product.

## Scope once the user approves a docs-only coordination rollout
Workspace: `C:\Users\admin\Projects\blindspot-lab-kiroween-2026`
Repository: `edward321416-maker/blindspot-lab-kiroween-2026`, PUBLIC.
Proposed design branch: `proposal/research-dev-chat-sync-v1-20261116`. It is deliberately not integrated into default.
Kiro lead: `claude-opus-5.5`, effort `max` as approved. Choose other models only with the live model picker and record usage.
Do not treat current historical default `chore/kiro-repo-bootstrap` and any SHA in this document as fixed; inspect fresh state before running.

## Stage M0 — Documentation only, safe starting point
1. Check current worktree clean, `git branch --show-current`, `git remote -v`, `git fetch` and exact default HEAD. Reconcile any unpushed local commits; never reset/rebase/force push automatically.
2. Read `AGENTS.md`, accepted `.kiro/specs/`, `docs/DECISIONS.md`, all prior proposal files 00..08, and current G1-G4 evidence. Inspect package.json / requirements.txt / docker-compose.yml as text if they exist before running anything.
3. Prepare an ops-only branch. Propose additions of:
   - `ops/STATUS.md`, with acceptance SHA and current state; 1 reviewed writer;
   - `ops/HANDOFF_CONTRACT.md`, standard RCE and handoff fields;
   - `ops/DEVELOPMENT_ALIGNMENT.md`, derived from accepted Spec, task/work-item references, pending impact;
   - `ops/handoffs/YYYY-MM-DD_RCE-20261116-S3-ORACLE.md`, real historical example clearly labelled SOURCE_REVIEWED;
   - a revision to `docs/DECISIONS.md` recording only actual coordination adoption.
4. At this phase, do **not** create product code, local Flask/React/Vite servers, GitHub workflows, run any actual detector, download data/model packages, choose LICENSE, change main/default or expose private material.
5. Provide unified diff for review, file inventory, evidence links and exact source SHA.
6. If scope approved, create a PR against the **actual** default branch, not assumed main. No auto-merge.

## Stage M1 — Manual research→dev event
1. Research ChatGPT reads the same accepted remote HEAD and creates an RCE on a research branch for a **historical** G1 protocol change. Record original R0 Spec IDs RV-02/RV-03/RV-04 and source citation.
2. Development ChatGPT reads that RCE from GitHub (or is given link), checks RCE approval state and applies impact classification:
   KEEP generic SHA manifest/replay concept; REPLAN S3 schema and blind-review contracts; FREEZE any false S1+S2 independence assumption; BLOCK real model downloads and apps.
3. Development writes a proposed `ops/DEVELOPMENT_ALIGNMENT.md` matrix update and DEV_TO_RESEARCH question if needed. It does NOT implement an application.
4. Integrator reviews both handoffs and current Spec, and updates accepted `ops/STATUS.md` in a reviewed PR. Both chats re-fetch and agree on gate status at the same named SHA.
5. Save the actual test transcript and timestamps; a handoff checked-in without being read by the second chat is NOT a passed E2E test.

## Stage M2 — Safe stale-change detector, optional later
Build a standalone **stdlib Python** checker for PRs that:
- parses required RCE fields and immutable SHA formats;
- flags a proposed development item when its `task_spec_sha` is stale relative to changed requirement IDs;
- blocks disallowed `BUILD_APPROVED` or `INDEPENDENTLY_VERIFIED` states without a linked accepted decision/evidence;
- distinguishes intentional Phase4 reference gate exit 1 from genuine test failure;
- produces a read-only Markdown/JSON report without writing Git, editing status or changing user permissions.

Use fixture-based tests for L0/L1 unaffected changes and L2/L3 blocking changes. Connect GitHub PR checks only after code review of workflow permissions and a manual dry run. Do not create broad tokens or actions with write permissions by default.

## Quality and reporting criteria
| Check | Measurable result |
|---|---|
| SYNC-01 | Two separate ChatGPT rooms independently observe same accepted HEAD |
| SYNC-02 | Research RCE causes exactly the dependent work IDs to become stale |
| SYNC-03 | Old assumptions cannot resume under the new accepted Spec |
| SYNC-04 | Unaffected work continues without unnecessary mass restart |
| SYNC-05 | A LOCAL_ONLY Kiro commit is never reported as remotely accepted |
| SYNC-06 | CI and Kiro test transcripts distinguish simulated/synthetic vs real evidence |
| SYNC-07 | No unauthorized data/model/app build, paid changes, rebase, main or releases |
| SYNC-08 | Each completed result has git SHA, actual commands, checks and /usage if observed |

Required Kiro final report:
- current default HEAD and proposal branch HEAD;
- exact tested ops paths, diff and acceptance status;
- what is installed and what remains a proposal;
- observed actual model/effort, CPU environment only if relevant, Kiro /usage before/after;
- any blockers/contradictions and exact next owner;
- no fabricated live-sync or background actions.

No automation or code work is authorized solely by reading this implementation brief; it is a draft for user review.
