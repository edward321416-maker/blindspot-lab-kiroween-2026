# KIRO IDE — 1st run / local + GitHub bootstrap (copy this text into Kiro chat)

You are working inside my local **BLINDSPOT LAB / Kiroween 2026** starter workspace. This is a research HOLD, not a selected product. I want you to organize the workspace, initialize Git locally, and prepare linkage to a NEW private GitHub repository. Do not build the app or deploy yet.

## Authoritative context
1. First read `AGENTS.md`, `README.md`, `docs/REPO_MAP.md`, `docs/PROVENANCE.md`, `docs/DECISIONS.md`, and `docs/SETUP_ACCEPTANCE.md`.
2. Inspect `.kiro/specs/blindspot-regression-gate/{requirements,design,tasks}.md` and `.kiro/steering/guardrails.md`, preserving their existing meaning. These were drafted outside Kiro; do not claim this makes the app Kiro-built.
3. Check `package.json`, `requirements.txt`, `docker-compose.yml` **as text if present**, not by executing them. Before loading Python code fully, search function/class signatures and calls with rg/grep. Never run unknown scripts without understanding scope.
4. Reference experiment: `research/reference/phase4/`. This is PRE-EXISTING RESEARCH, not the contest app. Preserve it read-only; do not move it into `apps/` or `packages/` or claim it was created in Kiro.

## Phase A — local (may proceed inside this designated workspace)
- Record exact workspace root absolute path; confirm it is not nested inside another Git repo. Verify `git` and `python` availability; do not auto-install paid or privileged software.
- Verify SHA256s listed in `research/reference/phase4/SOURCE_SHA256.json`; run read-only tests from `research/reference/phase4`.
- Expected: 18/18 Phase4 tests pass in the previous environment (re-measure actual), research gate reports 38 NEW_REGRESSION, **exit code 1 on purpose**, and production approval BLOCKED. If environment differs, report the discrepancy and don't invent success.
- Check .gitignore and avoid any secrets, external personal camera images, checkpoint weights, or binary dumps. Propose the smallest safe corrections with unified diffs and stop on unexpected changes.
- Initialize a NEW local repo only if no existing .git. Make sure root `.kiro/` stays tracked. Create `chore/kiro-repo-bootstrap` only in this new repo, leaving main unchanged when it exists.
- Compile an inventory of files and provenance (old research vs new prospective software), then make a clear GO/HOLD decision for the workspace only.

## Phase B — remote GitHub (requires my specific approval before creation/push)
- Check whether `edward321416-maker/blindspot-lab-kiroween-2026` exists. Propose creating it with visibility **PRIVATE**, not public. If it already exists, stop and explain; never overwrite or reuse without approval.
- Before creating the repository, connecting GitHub apps with broad scopes, or pushing any files, display the exact owner, repo, visibility, target local directory, requested permission and list of files to upload; ask for my explicit approval.
- Use existing authenticated git/GitHub tooling or GitHub Desktop. Browser-authorized login is OK; no token/password copying into chat and no credential-file extraction.
- After approved creation/push, read back URL, branch, HEAD SHA, and target file tree. Confirm local and remote HEAD match. DO NOT create releases, merge PRs, make repository public, or change other repos.

## Phase C — organize outputs, then stop
- Organize docs, tests, reference code and `.kiro` according to `docs/REPO_MAP.md`; don't refactor the old gate to make CI green.
- Keep proposed app folders empty and document their intended responsibilities. You may improve draft Kiro specs but do not implement unchecked tasks until G1–G4 and my GO decision.
- Note an original Phase4 save hook expects root `tests/test_gate.py`; DO NOT activate it unchanged after moving reference code. Propose a path-correct hook first.
- Report (1) actual local path, (2) actual remote URL or NOT CREATED, (3) branch and commit SHA, (4) test commands + exits, (5) exact Kiro edits, (6) actual Kiro credits if shown, (7) security/competitor/product blockers.
- Use your spec-driven workflow and preserve Kiro session traces for eventual contest submission, but never call a bootstrap a functional Kiro-built app.

No cloud billing, overages, external deployment, public GitHub, license selection, IAM modifications, file deletion, or production approval without my specific authorization.
