# Kiro CLI — Remote bootstrap from GitHub (2026-11-15 KST)

## Scope and status
This is a **handoff of pre-existing BLINDSPOT LAB research**, not an already built Kiro application. Its product decision remains RESEARCH HOLD. The 29-file starter was verified against the original local ZIP using Git blob SHA, including original CRLF in gate_cases.csv. No Kiro credits were used by this handoff.

Source: private repository `edward321416-maker/urban-intelligence-os-research`
Branch: `handoff/blindspot-kiro-20261115`
Project subfolder: `handoffs/blindspot-lab-kiroween-2026/`
Verified source tree commit: `a185fce62ce540e34d360890f7441727401dd72d` (the source files remain identical after this instruction file was added).
Original research repository `main` MUST remain untouched.

## Goal
Using Kiro CLI on the user's Windows computer, create a **separate local project** named `blindspot-lab-kiroween-2026`, transfer exactly the starter source files from this branch's subfolder, verify integrity, run the existing reference tests, then plan a **NEW private** GitHub repository of the same project name. Do not start app implementation, create a public repository, spend on cloud resources, or deploy.

## Procedure
1. Verify `git`, `python`, and current private-GitHub read authentication using Git Credential Manager, existing `gh` login, or the user's own interactive browser login. Never ask for or inspect passwords, personal access tokens, cookies, or credentials. If authentication is unavailable, report the exact login action and STOP remote steps.
2. Inspect proposed safe locations under the user's home Projects directory. Never delete or overwrite an existing workspace. If a folder is occupied, choose a distinct empty folder and report it.
3. Read from GitHub: clone this source repository **only into a separate temporary staging folder**, checking out branch `handoff/blindspot-kiro-20261115` (a shallow single-branch clone is preferred). Verify the branch and commit. Confirm `handoffs/blindspot-lab-kiroween-2026/README.md`, `AGENTS.md`, `.kiro/specs/`, `research/reference/phase4/` exist. Count the 29 original files (plus this remote instruction, 30 total). Do not copy the source repository's `.git` or any files outside the project subfolder.
4. Copy the contents of `handoffs/blindspot-lab-kiroween-2026/` into a new separate local workspace root. Preserve dotfiles including `.kiro` and `.gitignore`. Keep `research/reference/phase4/` explicitly labelled historical reference research. Do not attribute it to Kiro.
5. Read local `AGENTS.md`, `README.md`, `docs/REPO_MAP.md`, `docs/PROVENANCE.md`, `docs/SETUP_ACCEPTANCE.md`, `docs/KIRO_EXECUTION_PROMPT.md`, and `.kiro/specs/blindspot-regression-gate/` before proposing changes. Inspect any `package.json`, `requirements.txt`, or `docker-compose.yml` as text if present. Use `rg`/grep for function/class signatures before modifying code.
6. Check SHA-256 against `research/reference/phase4/SOURCE_SHA256.json`. For Git blob verification, the original `fixtures/cases.json` blob is `cea74fec1f9e2eebce900f507bf3ad5e6ab5e50d` and `evidence/gate_cases.csv` is `9a5b4fd6720e15f1804afd0117845eda945561ff`. Be aware that Git checkout line-ending filters may affect worktree bytes on Windows; compare original Git blobs and avoid silent normalization.
7. Run reference tests from `research/reference/phase4` using `python -m pytest -q tests/test_gate.py` in a safe isolated environment. Previous evidence was 18/18 passed; measure again, do not assume. Run the gate only according to the documented CLI usage; expected reference result is **38 NEW_REGRESSION and an intentional exit code 1**, with production approval BLOCKED. Never relabel this exit as success or approve deployment.
8. Initialize a NEW local Git repository inside the new workspace, not inside the staging clone. Keep `.kiro/` tracked. Do not merge/rewrite any existing repository. Record changed files and provenance clearly.
9. Only after local QA, check whether `edward321416-maker/blindspot-lab-kiroween-2026` exists. If not, prepare to create it as **PRIVATE** with existing authenticated GitHub tools; before the actual creation/push, display owner/name, visibility, file inventory, and target branch for user approval. No public repo, access changes, broad OAuth scope, releases, merges, paid services, or IAM changes.
10. After any approved private repo creation/push, read back remote HEAD, branch, file tree, and root `.kiro`. Record actual local path, GitHub URL, commit SHA, test transcript, and blockers. Remain in RESEARCH HOLD; build the new contest app only after a separate product GO decision.

## Stop conditions
- The private repository cannot be read with the user's authorized login.
- SHA mismatch or missing `.kiro` files.
- Workspace path occupied, unsafe scripts, exposed credentials, or unexpected files.
- Tests or model verdict differ materially from recorded evidence.

No destructive commands, forced pushes, changes to `main`, automatic public publication, credential extraction, or false claims of Kiro-built code.
