# PUBLIC visibility preflight — 2026-11-16

Scope: `edward321416-maker/blindspot-lab-kiroween-2026` **only**. User explicitly requested PUBLIC. The connected GitHub tools cannot change repository visibility, so the user's already authenticated Windows Kiro CLI / GitHub CLI must do it.

## Read-only inspection already performed in chat
- Repository is PRIVATE, current default branch `chore/kiro-repo-bootstrap`, latest observed source commit `f252e78a9f5d9aa3a839fa0063c01f528c1cfa5d` **prior to this documentation update**.
- All 32 tracked files on that branch were inspected using GitHub file reads (including the large `research/reference/phase4/fixtures/cases.json`).
- Pattern screening detected **no** private key headers, standard GitHub/AWS/OpenAI-looking tokens, obvious credential assignments, or email addresses in current tracked file contents. This is a heuristic screen only; it is **not** a complete secret scan.
- No committed image files, deployment artifacts or model checkpoints appear in the current 32-file tree. The research uses synthetic reference fixtures.
- Repo has **no LICENSE** at this point; user has not selected an open source license. Public visibility does not grant open source redistribution rights. Kiroween submission rules eventually require a visible open-source license and a functional Kiro-built project.
- Commit authors, messages, old revisions, branches, and GitHub Actions history may become public. **Run a full history/secret scan before changing visibility** (the chat screening inspected the current branch files, not every historical commit).

## Local steps for Kiro CLI
1. Use the existing root `C:\Users\admin\Projects\blindspot-lab-kiroween-2026`; verify `gh auth status`, `git status --short`, and remote URL; never reveal credentials.
2. Ensure current branch is clean and fast-forward to remote tip after this documentation commit. No force push, resets, or deletions.
3. Audit all Git history with `git log --all --format=fuller`, `git ls-files`, and a locally available trusted secret scanner or conservative content patterns. Check binary objects, tracked paths, GitHub Actions logs, commit author email, and any history excluded from a simple current-tree scan. Do not run scripts fetched from unknown sources.
4. If blockers are found, STOP and report exact paths/types without displaying secrets. Do not assume a later delete removes data from Git history.
5. If clean, change this **exact repository** with official GitHub CLI:
   `gh repo edit edward321416-maker/blindspot-lab-kiroween-2026 --visibility public --accept-visibility-change-consequences`
6. Verify with `gh repo view edward321416-maker/blindspot-lab-kiroween-2026 --json nameWithOwner,visibility,url,defaultBranchRef` and from an unauthenticated GET (or browser incognito).
7. Record evidence in `docs/DECISIONS.md`, commit/push and verify remote HEAD. Leave existing default branch alone; do not create `main`, LICENSE, releases, or deployment without separate approval.

## Operational safeguards
- On Opus tasks keep user-authorized **MAX** effort and record `/usage` at start/end, preserving credit headroom.
- This repo remains **RESEARCH HOLD**, no product selected, no full application or deployment.
- Do not expose credentials, user-owned camera/face photos, private datasets or third-party copyrighted materials.
- Publication is a visibility change, **not** Kiroween submission completion.

Official references:
- https://cli.github.com/manual/gh_repo_edit
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
- https://kiroween.devpost.com/rules
