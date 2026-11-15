# One-shot verification checklist (Kiro must report exact evidence)

## Local
- [ ] Print canonical absolute local workspace path; confirm no existing folder overwritten.
- [ ] `git status --short` scoped to the new repo; show current branch and untracked files.
- [ ] Check Python installed. Read existing requirements/config text before executing commands.
- [ ] Run Phase4 reference tests from `research/reference/phase4` using `python -m pytest -q tests/test_gate.py` and record actual N/N result.
- [ ] Run pinned fixture command and verify **exit 1 + 38 regressions + BLOCKED production**; do not mask the exit code as failure of a contract test.
- [ ] Verify each fixture's SHA-256 against manifest; if mismatch, stop.
- [ ] Verify `.kiro/specs` and steering are *tracked* by Git and not ignored (`git ls-files .kiro`).
- [ ] Audit paths for sensitive files and unapproved binary weights/data.

## GitHub (after explicit user authorization)
- [ ] Check remote repo does not already exist and owner is approved.
- [ ] Create new PRIVATE repo. Do not alter, fork, or push any previous competition repository.
- [ ] Connect exactly one `origin` to approved repository. Use browser-authorized Git Credential Manager, GitHub Desktop, or existing `gh` auth; never ask for token in chat.
- [ ] Branch `chore/kiro-repo-bootstrap`; initial commit/push only after user authorizes publication to PRIVATE origin.
- [ ] Read back branch SHA and tree from GitHub, compare local `git rev-parse HEAD`, record actual URL.
- [ ] Use PR to merge into `main` only after user review and passed contract tests.

## Report
- [ ] Actual repo URL, visibility, local absolute path, origin, branch SHA, files changed and test transcript.
- [ ] Separate DONE / PENDING / BLOCKED and give Kiro credits before/after *only if displayed by product*.
- [ ] No claim of app completeness, Kiro-based authorship, GitHub publication, or winning potential without evidence.
