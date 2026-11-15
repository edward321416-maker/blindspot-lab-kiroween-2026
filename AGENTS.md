# BLINDSPOT LAB working policy (Kiro + human)

- **Research HOLD, product unselected.** Workspace bootstrap is authorized for planning, not deployment, billing, publication or unrestricted implementation.
- Ask explicit approval for **repository creation, first remote push, visibility changes, granting collaborators/access, license choice, external deployment, new paid service**, or adding user-owned sensitive images.
- Never alter existing repositories or overwrite local folders. No destructive commands, no secrets pasted into chat, no broad GitHub app permissions.
- Inspect `package.json`, `requirements.txt`, `docker-compose.yml` as text before running build/configuration scripts; inspect test and CLI source first. For code edits, present unified diffs or exact SEARCH/REPLACE blocks.
- Do not execute unknown `.joblib`, pickle, external checkpoint code, or arbitrary uploaded Python modules. Synthetic data is never independent human validation.
- Maintain `docs/PROVENANCE.md`, `docs/DECISIONS.md`, source hashes and measured test outputs. Preserve all prior fail-closed behaviors.
- Confirm CLI expected behavior: 18 Phase4 contract tests PASS; deliberate research gate returns exit 1 with 38 NEW_REGRESSION; this is an expected detection, not a broken test suite. Production approval BLOCKED even with zero regression when oracle is unverified.
- Distinguish source evidence, research proxy, real-model experiment and user research. No invented Kiro credit usage, customer quotes, models, datasets or GitHub pushes.
- The existing `.kiro` materials were drafted outside Kiro. Kiro must actually create and test substantial new functionality to establish qualifying tool use.
- Commit only sanitized files. No public release, changes to existing repos, or main branch merges absent explicit review.
