# Kiro B5 — Re:Collection D1-BUILD final technical QA (NO B0–B4 rerun)

**Stage authority:** The user's previously scoped local-only **D1-BUILD B0–B5**; execute **B5 quality/evidence review only**, then STOP. Do not treat this handoff as authorization to implement D1E comparator, D2 product, user-facing release, cloud/AWS, actual museum assets or a new license. Product selection remains undecided.

**Model:** Claude Opus 5.5 / reasoning effort MAX only, with no Auto/fallback. Use a fresh Opus 5.5/MAX review session if available **without compromising the user's existing work or model setting**. Label reviewer `SAME_MODEL`; independent human oracle, publisher approval and external rights review are **NOT** implied. Do not repeatedly ask user for `/model` or `/usage` screenshots. If existing UI provides actual observation, record it; otherwise `SESSION_CONFIG_ONLY` / `BONUS_USAGE_UNOBSERVED`.

Read from the **exact SHA-pinned GitHub commit supplied in the user's short prompt**:
1. `docs/handoffs/recollection-d01/22_ALIGNMENT/B4_COMPLETE_B5_QUALITY_RESEARCH_GATE_20261117.md` — B4 results and known weaknesses.
2. `docs/handoffs/recollection-d01/20_ALIGNMENT/RESEARCH_3_9_OAP_REFERENCE_RETEST_20261117.md` — research **reference only**, proposed new output-assurance contract, not approved product code.
3. `docs/handoffs/recollection-d01/16_ALIGNMENT/RESEARCH_DEV_ALIGNMENT_REGISTER_20261117.md` — accepted-vs-proposed research map.
4. `docs/handoffs/recollection-d01/08_PLANS/D1_BUILD_BOUNDED_SPEC_APPROVAL_PENDING_20261117.md` — original D1-BUILD B5 boundaries.

## 1. Preflight — inspect actual local B4, preserve existing working tree

- Local workspace: `C:\Users\admin\Projects\recollection-kiroween-2026`; expected current branch `main`, HEAD `09f4b8a524058440a7dbc9917d3112640d73d258`, clean, no remote. Parent B3 `4c4dc7adf49f8c6a3e699da0370bd8c93374e98a`.
- If B5 already exists locally, **do not repeat B5**. Verify results read-only, report exactly which evidence is available. If unexpected dirty worktree, STOP and report conflict without modifying it. No reset/stash/rebase/checkout, no rewriting B0–B4 commits.
- Read applicable AGENTS/operating policy, local .kiro task/requirements, frozen oracles, B1/B2/B3/B4 contracts, report generator and local evidence files. Use `rg`/AST to discover signature/schema, then read only relevant modification targets; parse `package.json`, `requirements.txt`, `docker-compose.yml` as stack metadata without executing declarations.
- Protected GhostWeb dirty HEAD `23b8a010` and BLINDSPOT unpushed `c073ddd1` remain untouched.
- Source code/test/fixtures must remain immutable during the QA phase. QA **may** add bounded documentation/checkpoint/evidence reports and non-destructive new canonical diff copies to existing local report directory only.

## 2. Independently challenge reported B4 evidence in fresh same-model review

**Verify actual bytes and commands**, not just the 199-line Kiro summary:
- `git cat-file -t` and `git show --stat` for B0 through B4 commits, clean status, no remote, expected ancestry.
- B4 full diff size/count/SHA: user report `B4_09f4b8a.diff` 2,375 lines/114,690 B, SHA-256 `2191e06afd971c9acfe09cf5bb8004a5bfb30a9057996ed9672b95fa8f90bafe`. If mismatch, record **actual** and investigate without changing code.
- Frozen B0 oracle manifest 9 files, validator 29/29, runtime R01–R06, JCS 13/13. Confirm no changes since B0 and no B1–B3 regressions changed since B3.
- Run the existing full `node --test --test-reporter=tap "tests/**/*.test.ts"` twice with capture of raw logs, exit 0 and stable test-result semantic digest (normalize only durations/timestamps, keep raw files separately). Expected baseline **164/164**, not a substitute for observed result.
- Independently regenerate B4 evidence using **existing** generator and compare exact SHA `3bcb03e5616cc8ad426389b25cd977881c43e46f3dc54537de8f7ffcd928fba3`. Confirm fixture hashes, B2/B3 bind, `historicallyVerified=false`, `publishable=false`, no approval/HTML/JS/network/external assets. No new npm packages.
- Verify per-scenario counts: **23 total = 3 EXECUTED (F1-01, F2-01, F3-12) + 20 REFUSED (F1-02 plus 19 F3)**, not 23/23 attacks blocked. Check `F3-12 SOURCE_BOUND_NOT_ENTAILED` is an **intentional observed limitation**, and F3-13 `Data:` is P2 overblocking.
- Challenge B4's deliberate B3 invocation when B2 is not valid: runtime must refuse before any primitive step or externally visible side effect. Check any report generation writes as trusted tool-only operation separate from runtime.
- Rerun **read-only source-level inspection** for class of graph path trust and potential caller-supplied `mode/validation` spoof. Separate actual P0 from hypothetical risk. Do not claim historical entailment is proven when B2 only matches a quote.

## 3. Diff provenance repair — new audit copies only

User's report found prior B0–B3 `.diff` files damaged by PowerShell text recoding. Do **not** change original files, rename, delete, overwrite or modify Git history.

1. First inventory each historic diff name/full SHA/byte count and original B0–B3 commits/parents; record a `LEGACY_DAMAGED` manifest.
2. **Non-destructively generate separate canonical diff files with new filenames** in the existing local report destination. Use Git command options that write raw diff bytes or a safe subprocess binary capture (UTF-8 LF no BOM); do not pipe Git output through PowerShell's text encoding transformation. Verify Git version, `--no-ext-diff`, `--no-textconv`, output encoding, parent selection and filenames. Ensure ASCII/Unicode is not corrupted.
3. Include B0 initial-root diff via `git show --format= --root` (first commit can have no parent); B1/B2/B3 via each exact local commit vs parent. Do not assume `git diff HEAD~ HEAD` applies for B0 root. Compute SHA256 via byte reads, output exact byte count, line count, UTF-8 decode validation, status if binary diff exists. Avoid rewriting or attempting to magically reconstruct damaged report bytes.
4. B4 original diff stays untouched. Mark each new canonical path and hash `REGENERATED_FROM_GIT`, not `ORIGINAL_REPORT_RECOVERED`. If no original Git commit bytes, mark `UNRECOVERABLE`, do not fabricate.
5. New audit copies are reversible local report artifacts, not changes to implementation and not new permission to manipulate other projects. If operating policy requires further confirmation for writes to this report directory, keep this repair as a read-only suggested action, do not silently extend permissions.

## 4. Research alignment / P0-P1-P2 risk review

- **F3-12 P1 candidate:** Quote-at-locator exists but does not entail the claimed historical proposition. Current B4 run may EXECUTE as source-bound; this is unacceptable as proof of history for future **visitor-facing answer/feedback**, even though current `historicallyVerified=false` and no publish. Explicitly state current exact risk and conditional acceptable scope.
- **Indirect dependency P1:** Research 3.6/3.7/3.8: current engine has no visitor correctness/feedback oracle and no closure proof across claims→choices→branches→feedback. Do not add a fake feedback primitive or leak research holdouts to dev.
- **3.9 OAP output-sink assurance:** Research reference had five newly introduced cross-sink attacks initially allowed, blocked by revised **research reference** contract. It subsequently passed 38 cases twice (76 self-authored judgments) and 8 open-label metamorphic probes, **not product-verified**. Inspect present B3/B4 output shape and list exact future adapter seams (question, answer, feedback, branch, multilingual strings/media) without modifying code or importing hidden cases. The OAP proposal is not accepted D1 schema, is not B5 acceptance criterion, and is NOT independent validation.
- **3–8 research vs 2–4 D1:** `ARCHIVE DETECTIVE` product direction is different from the frozen compiler scope. Keep B0/B1/B2/B3/B4 unchanged, flag L2 versioned schema/UX decision for later, not a hidden B5 migration.
- **P2:** B2 `Data:...` false-positive, `TYPECHECK_NOT_RUN`, non-independent oracle, byte-damaged old diff copies, current Kiro bonus usage UNKNOWN. Explicitly assign severity and proposed separate fix, but no unapproved regex loosening or dependencies.

## 5. B5 acceptance & deliverables

**B5 is a QA/reporting phase, not a new product feature.** Produce exact Korean report with:
1. Local Git ancestry/HEAD/worktree/remote and verification date; **same-model** review label;
2. Original synthetic oracle SHA, B4 evidence SHA and test command/exit per run; number of distinct tests vs assertions, raw logs vs normalized digest;
3. 23 B4 scenarios: 3 executed incl F3-12 known flaw, 20 refused; any newly observed P0 must be stated, not buried;
4. P0/P1/P2 register with observed evidence, affected user state, recommended *separate* fix and tests, research/source distinction;
5. Original damaged historical diffs and regenerated side-by-side canonical diff SHA/paths (or `PENDING` with reason), no re-written history;
6. Security/audit boundary: what exactly is demonstrated, what remains `NOT_TESTED`: human independent oracle, current external rights, browser/keyboard/accessibility, history truth, 3–8 multi-object product, AI generation, direct HTML comparator, cloud;
7. `SESSION_CONFIG_ONLY` if only session config, `BONUS_USAGE_UNOBSERVED` if no actual user-facing pool read, estimate +20 vs measured UNKNOWN; preserve original D1 cumulative soft/hard limit. Do not repeatedly demand screenshots.
8. Clear *one* outcome: `GO_FOR_D1E_PREP` (planning only), `HOLD`, or `REWORK`. If P0 or reproducible failing invariants, do not produce GO; if technical integration is green but F3-12 cannot be safely controlled in future visitor output, GO FOR **PREPARATION ONLY** with mandatory restrictions, product publish **HOLD**.

Evidence audit may use existing Node24/Python available locally, but **do not install any dependencies**. If extra tools absent, use native PowerShell/Python/Bash with same approved permissions and disclose unknowns. No AI model fallback and no paid/cloud calls.

At end, keep source/test files unchanged; add a scoped local QA report/checkpoint only, and if appropriate create **one local B5 QA-only commit** after verifying no user modifications or forbidden files. Report exact full SHA and unified diff if any. No GitHub remote/push, no app implementation, no B2 patch, B4 rerun with altered oracle, D1E actual execution, D2/production publisher, AWS/Bedrock, real museum downloads or sealed research datasets.

**STOP after B5.** User receives a concise Korean result including evidence, disagreements and **next research-and-development decision**. No endless preflight re-review loops.
