# Kiro CLI implementation brief — only after workflow-plan approval

Status: FUTURE IMPLEMENTATION, NOT AUTHORIZED BY THIS PROPOSAL ALONE.
Repository: edward321416-maker/blindspot-lab-kiroween-2026
Source proposal branch: proposal/research-dev-chat-sync-v1-20261116
Current verified research source baseline: f9b2b026b2d619f3c2c764a5149975363e4fb724.
Model: Claude Opus 5.5 MAX as already authorized; record /usage rather than assuming balance.

## Mission
Implement a simple, local and GitHub-readable coordination protocol for separate ChatGPT Research and Development rooms. Do not build the contest app or add paid services.

## Required steps after approval
1. Check git status, actual default branch and remote SHA. Read AGENTS.md, current .kiro and docs/DECISIONS.md, and all four proposal documents.
2. Create ops/STATUS.md with true, actually verified facts only, including G1-G4, pending R0 cross-family review, existing historical Phase4 evidence and known blockers. The file is a curated snapshot, not self-updating.
3. Create ops/HANDOFF_CONTRACT.md using the proposed template with required metadata and provenance levels. Propose a real initial research-to-development handoff marked PROPOSAL_ONLY and NOT_APPROVED_FOR_BUILD.
4. Add docs/DECISIONS.md entry only when implementation of the coordination protocol is actually approved. Avoid changing research facts without independent evidence.
5. Propose GitHub PR targeting the actual default branch. No main creation or default-branch changes. Do not edit the baseline Phase5 R0 spec or Phase4 fixture as part of this operations task.
6. Run the manual acceptance tests: two independent fresh chat reads report same remote SHA/status; development chat refuses unapproved build; stale SHA and LOCAL_ONLY labels are handled honestly; source status and evidence claims agree. Record exact results, no fabricated pass.
7. Only after a successful pilot consider issue/PR templates; optional stdlib-only validation and GH Actions PR checks in a separate small change. Status checks are not configured simply because this proposal mentions them.
8. Finish with remote commit SHA, branch, affected paths, tests performed/not performed, privacy scan, Kiro credits actually observed, and whether ops/STATUS.md has been integrated.

## Safety
- User has authorized Public GitHub source and Opus MAX, not unbounded data publication, paid cloud, new OAuth apps, app deployment, choosing LICENSE, nor model/image downloading.
- Do not commit local Windows usernames, email addresses, screenshots with tokens, private CCTV or weights.
- No global trust-all permissions. No force push, no destructive commands and no silent rebases.
- On a conflict or differing SHA, stop and explain the exact divergence; do not manufacture synchrony.
- Maintain RESEARCH_HOLD and leave product decisions with the user.
