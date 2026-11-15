# Decision log

| Date (KST) | Item | Status | Evidence / approval |
|---|---|---|---|
| 2026-11-15 | BLINDSPOT LAB research candidate | RESEARCH HOLD | Phase4 38 regressions; same-user unmet incumbent workflow not yet proven |
| 2026-11-15 | Set up new isolated project workspace | PLANNED / LOCAL SEED CREATED | This starter packet; no user device action performed |
| 2026-11-15 | Create new GitHub repository | PENDING USER CONFIRMATION | Proposed `edward321416-maker/blindspot-lab-kiroween-2026` PRIVATE |
| 2026-11-15 | Connect origin, initial push | NOT EXECUTED | Require actual remote readback, SHA, branch and clean status |
| 2026-11-15 | Kiro-built app implementation | BLOCKED / PRODUCT UNSELECTED | G1 real oracle, G2 model A/B, G3 FiftyOne runtime, G4 user unmet task |
| 2026-11-15 | Public release, LICENSE and external deployment | NOT APPROVED | Official rules require public repo upon submission, user to authorize details |
| 2026-11-16 | Sync handoff docs from source commit `06981d4` | DONE | Added `KIRO_CLI_MODEL_EFFORT_POLICY_20261116.md` and `START_HERE_KIRO_CLI_20261116.md`, updated `REMOTE_KIRO_BOOTSTRAP.md`; Git blobs equal source. `research/`, `.kiro/`, `AGENTS.md`, `README.md`, `.gitignore` unchanged between `1a5445e` and `06981d4` |
| 2026-11-16 | Kiro CLI model and effort for this bootstrap | RECORDED | kiro-cli 3.3.0. Clone, copy, first QA and commit `e479e23`: model `auto`, underlying model not identified. Doc sync, re-verification and GitHub steps: model `claude-opus-5.5`, effort `max` (session metadata; saved global `chat.modelDefaults` for this model is also `max`). Policy target `high` was not applied. `--list-models` also lists `claude-sonnet-5.5` and `gpt-5.6-sol` |
| 2026-11-16 | Kiro credit usage | RECORDED | `/usage` at 02:00 KST: bonus `kiroween-20-26` 32.82/4000 used; plan credits 0.00/50 (KIRO FREE). No pre-session reading exists, so the exact bootstrap cost is unknown; at that reading it was at most 32.82, under the 100-credit cap |
| 2026-11-16 | Phase 4 reference re-verification | MATCHES BASELINE | 13/13 SHA-256 match; `cases.json` and `gate_cases.csv` blobs match; 18 passed; research gate exit 1, 38 NEW_REGRESSION, `BLOCKED_UNVERIFIED_ORACLE` |
| 2026-11-16 | Create PRIVATE `edward321416-maker/blindspot-lab-kiroween-2026`, push `chore/kiro-repo-bootstrap` | APPROVED BY USER | To be executed after this commit; remote readback is reported in the session, not in this file |
