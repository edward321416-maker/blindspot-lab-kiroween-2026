# Kiro CLI — Re:Collection D0.1 read-only evidence alignment

> **This is the only execution packet the user needs to reference from Kiro.**
> Authorized scope: READ-ONLY fact verification and report only. **D1 is NOT authorized**.
> Kiro desired active model `claude-opus-5.5` with effort `max`; do NOT use `Auto` or any other model. If actual active model cannot be verified, mark it `MODEL_UNVERIFIED`, do not invent evidence.

## A. Pin and read the GitHub handoff, WITHOUT any Git changes

Source repository: `edward321416-maker/blindspot-lab-kiroween-2026` (PUBLIC)
Document-only branch: `handoff/recollection-d01-readonly-20261117`
File root: `docs/handoffs/recollection-d01/`

1. Retrieve repo metadata and target branch commit SHA via **read-only public HTTPS**. Verify visibility/branch and current commit. No `git checkout`, `git fetch` inside existing worktrees, `git clone`, new branch, GitHub write or local files.
2. Read in this sequence:
   - `README.md` (source limitations)
   - `01_START_HERE/ReCollection_DevChat_Handoff_Phase0_ReadOnly_20261117.md` (top-priority available text)
   - `02_REFERENCES/ReCollection_Technology_Architecture_ADR_20261117.md` (lower priority)
   - this instruction file
3. Record each GitHub path, observed blob SHA/commit SHA, retrieval time and whether content fetched successfully. **These are indexed Library text copies with origin labels, NOT original ZIP byte copies**.
4. Never claim to have accessed the original `ReCollection_DevChat_Handoff_Packet_20261117.zip`, `ReCollection_Development_Master_Audit_20261117.pdf`, `ReCollection_Comparison_Results_20261117.pdf` or `ReCollection_Reproducible_Comparison_Packet_20261117.zip`: all are **UNAVAILABLE** in this handoff. If the exact originals become accessible via an authorized, known path, inspect them by reading not executing, and prefer the verified Master Audit over ADR.
5. The existing Markdown and ADR contain product proposals, not authoritative permission to implement.

If GitHub is inaccessible, report `GITHUB_READ_UNAVAILABLE` and stop document-dependent work; no guessed links, no fallback to new accounts or paid connectors.

## B. Read the actual local D0 report (outside protected repositories)

From the prior Kiro D0 report, the stated **report directory** is `D:\Users\admin\Desktop\hackathon\ReCollection_D0_Report_20261117\`. This is an **unverified expected location** until your tool confirms it exists.

- Search ONLY this exact directory for the current D0 Markdown (1,138 lines) and 29-page PDF, using filenames / metadata; do not recursively search all drives.
- Read D-1 through D-7 from the **actual D0 Markdown at lines 1116–1122**, word-for-word. They are Kiro-created decision items and must not be attributed to original handoff.
- If exact lines differ or file is not accessible, mark `UNAVAILABLE` instead of re-creating decisions.
- Compare existing D0 assumptions to the two current GitHub indexed sources, recording **what is supported, contradicted or absent**. The final Master Audit is still missing, so a preliminary review cannot resolve its precedence.
- Do not attempt to merge GhostWeb or BLINDSPOT content.

## C. Preserve existing local Git without any writes

As user reported before this handoff, GhostWeb and BLINDSPOT are different protected workspaces. Verify with read-only commands if accessible:
- GhostWeb expected branch `d1.4-p1-closure`, HEAD prefix `23b8a010`, uncommitted changes in `ghostweb/discover.py` and `tests/test_d14_security.py`. No stash.
- BLINDSPOT expected branch `review/phase5-r0-1-opus-20261116`, HEAD prefix `c073ddd1`, one local unpushed commit. No stash.

These are **user-reported past snapshots**. Use actual state and disclose any discrepancy. Do NOT `git fetch`, `git checkout`, `git pull`, `git reset`, `git stash`, commit, install, push or change files in these workspaces.

## D. Model, effort, and credit audit

- Preferred model: `claude-opus-5.5` ONLY, effort `max`.
- If interactive CLI slash commands require human UI interaction, clearly report that the agent cannot execute them. **Do not silently switch models**.
- Ask the user to supply copied actual `/model` (and effort) and `/usage` observations **only if indispensable for billing authorization**. Until then use `MODEL_UNVERIFIED`, `EFFORT_UNKNOWN`, `USAGE_UNAVAILABLE`. Do not treat `Credits: turn/session` as an `/usage` reading.
- Because this is read-only review, finish as far as evidence allows even if `/usage` is unavailable; withhold cost-governed D1 authorization. Use no paid API.

## E. D0.1 evaluation topics

1. **Source completeness and authority** — priority indexed text vs missing original ZIP/final master; no false certainty.
2. **Product/IP separation** — GhostWeb/BLINDSPOT no-code reuse, no relocation, no repo conversion.
3. **ExperienceSpec v0.2** — AI-authored claims/plan/graph separated from independently generated verification, curator approval and publication; hash three-way binding, rights fail-closed.
4. **Museum task consistency** — 2–4 objects user promise vs Case A one-object technical fixture. Keep one-object as unit smoke only; add prereg two-object E2E.
5. **A/B experiment preregistration** — same actual Opus 5.5/MAX, independent workspaces/sessions, arm A cannot see compiler specs, fixed sources/rights/tasks/oracle, construction cost vs incremental per-object cost, no 55/55 evidence inflation.
6. **Holdout authority** — blind separate author, rights-verified corpus, frozen oracle before implementation observations, explicit NOT_YET_AVAILABLE if absent.
7. **Security/rights/AWS** — source/multimedia license distinctions, prompt injection, no arbitrary JS, SSRF, admin-only publish, mock model local first, no AWS calls.
8. **Credit plan** — earlier D1 build estimate 170–315 credits, D1E 60–120, total 230–435; these are PROPOSED, unmeasured. Build soft 260 / hard 340 not a D1E approval. Require real `/usage` at task start/end before future paid/credit-bearing execution.
9. **Decision D-1..D-7** — quote exact source lines and propose HOLD/APPROVAL_REQUIRED with reason, never replace the original question text.

## F. Required output and stop

Produce **Korean** D0.1 report (read-only); possible PDF only if preinstalled safe tooling and outside protected folders, otherwise Markdown and explain limitation.
- source index: path, Git blob/commit, actually read/missing and provenance;
- local D0 report excerpt decision D-1..D-7 if present;
- VERIFIED / USER_REPORTED / PROPOSED / UNVERIFIED / BLOCKED separation;
- actionable D1 plan, isolated file tree and tests **as planning only**;
- exact D1 and D1E budget proposals, not billed usage;
- remaining decisions and **GO_FOR_D1_APPROVAL / HOLD / NO_GO_OR_REDUCE_SCOPE**;
- observed model/effort/credits or explicit UNKNOWN;
- actual code/git/AWS changes = NONE.

**STOP after D0.1.** No repository creation, no branch operation, no code edits, no installs, no download of missing copyrighted sources, no GitHub push, no AWS/Bedrock call and no deployment. Do not solicit new broad permissions. When source completeness remains blocked, return HOLD and list minimal missing evidence.

## G. Future policy

ChatGPT will prepare and verify documents on GitHub; user will paste only a small SHA-pinned Kiro prompt. Kiro will treat GitHub as the read-only handoff source and return evidence. Document upload to GitHub is not an approval for product development or for public redistribution of missing originals.
