# Kiro execution — APPROVED B5.2 typed visitor-output adapter

**Approved:** B5.2 local code implementation only, user consent recorded at `36_DECISIONS/B5_2_USER_APPROVAL_AND_COST_EXTENSION_20261118.md`. Follow `35_PLANS/B5_2_TYPED_OUTPUT_ADAPTER_IMPLEMENTATION_GATE_20261118.md` for all 32 specified tests and default-deny policy, `34_ALIGNMENT` for latest Kiro state, and `31_RESEARCH/RECOLLECTION_3_15_FUTURE_TEST_DATA_CONTRACT_20261118.md` for **research-only reference; do not import private data**. Use the **exact immutable GitHub commit linked by the user's short Kiro prompt**, not an evolving branch head.

**Implement now; do not return to planning or ask for repeated permission.** Stop after B5.2.

## 1. Local starting point

Workspace: `C:\Users\admin\Projects\recollection-kiroween-2026`. Expected **local** `main`, HEAD `52e230dfa96601e310b3210ae4af81e701eb74ad` (ADR-0006 corrective documentation commit), clean, **no remote**.

Read-only preflight for `git rev-parse HEAD`, `git status --short`, `git remote -v`, actual local AGENTS/.kiro operating rules, source/test inventories and relevant API signatures. If the B5.2 implementation has **already been completed** on a later local commit, do NOT redo; read-only verify and report. On conflicting dirty worktree/HEAD, stop with actual evidence: no overwrite, force, reset, stash, checkout, rebase.

Historic reported test evidence: original B0–B4 164 test executions; B5.1 +30 = **194/194 PASS twice and postcommit**, earlier B5.1 SHA `101836551883aae0e5fc179100538de2e5beeacb`. The docs-only erratum commit did NOT rerun tests (`NOT_RUN_DOCS_ONLY`). Treat these as Kiro-reported prior observations, not this stage's test results. All B0 frozen oracle, B1 contract, B2 stable validator, B3 runtime, B4 evidence and B5.1 repaired logic remain unchanged.

**Do not touch** GhostWeb `23b8a010` dirty state or BLINDSPOT `c073ddd1` unpushed commit.

## 2. Model and additional credits already approved

**Main Kiro session only, configured `claude-opus-5.5` / `max`. No Auto, fallback, or subagents.** A prior B5.1 challenge subagent switched to Opus4.8; ADR-0006 erratum truthfully records that violation. Do not create new agents whose effective model cannot be pinned. If actual session explicitly reveals an incompatible model, STOP rather than silently using it. Do not request repetitive `/model` screenshots.

User authorized **extra B5.2 credits**, knowing the planning estimate **+40–70** and that promo pool actual meter is currently unavailable. This is **B5.2-only** authorization, no open-ended spend. Keep a single bounded coding/test/fix loop, give estimated vs measured credits honestly. Starting original promo used=513.26, older soft used=733.26 and hard used=813.26 are **historical tracking references, not a new falsely measurable cap**. Do not reset origin, conflate session footer with bonus pool, claim observed budget compliance, ask repeated `/usage` screenshots, enable billing upgrades, or chain a new stage. If work materially exceeds planned B5.2 scope or estimated +70 exposure, stop and report instead of assuming extension.

## 3. BEFORE coding: freeze developer-safe acceptance cases

1. Read actual `src/contract`, B2 `validate()` / `validateText()`, B3 `run(...)`, B4 `integrate(...)` exports, B5.1 detachment and exact report hash/issue code types. Use `rg`/AST for signatures/schema before loading full function bodies. Parse `package.json`, `requirements.txt`, `docker-compose.yml` as nonexecutable text if present. Do not invent API paths or edit old source to fit a guessed DTO.
2. Define a new independent **output-adapter API** and typed data contract `visitor-output-0.1`, with explicit safe status `DEMO_PREVIEW | NEEDS_REVIEW | BLOCKED`. No public publisher and no extra visitor-primitive or browser.
3. Materialize **exactly 32** explicit, independently counted public developer-safe fixtures/expected decisions matching cases S01–S08, E01–E08, R01–R08, D01–D08 in `35_PLANS`. Resolve any `BLOCKED or NEEDS_REVIEW` disjunction into ONE deterministic status **before code** and document reason and policy. The source fixture + expected JSON + names + SHA256 constitute a preimplementation oracle. Preserve these records unmodified during fixes; if an expectation contradicts frozen existing spec, mark incompatibility and stop rather than hiding/rewriting evidence.
4. These cases are **developer regression fixtures, not sealed independent scientific or human evaluation**. Do not import private research 3.2 holdout, research 3.14 source ZIP or research 3.15 workbook/oracle into the repo. Research 3.15 has 83 **proposed** future tests, 0 independent human labels; it is not 83 product tests PASS.

## 4. Core adapter implementation

Build as a new scoped module (e.g. `src/output-policy/`), plus tests, simple synthetic fixture, evidence generator and ADR; avoid changes to frozen B0–B5.1 sources, or request a new approval if an unexpected compatibility rewrite is unavoidable.

### Trust and output safety

- Input = **trusted** synthetic owned source/snapshot/rights digest + exact v0.2 spec + **freshly bound** B2 validation status + **actual B3 structured run result**. Do not treat caller-provided `validated`, `publishable`, simulated `approved` or detached `reportSha256` as authority. Prefer revalidation of same detached snapshot, consistent content hash, mode and policy version. Reuse hardened B5.1 detachment; reject exotic live objects or inconsistent snapshots.
- Build **recursively closed allowlists** for visitor-visible fields, primitive kinds and permitted nested result structures. Anything unknown/extra silently renderable (metadata, labels, feedback strings, nested literals) -> `BLOCKED` or `NEEDS_REVIEW`; do NOT silently drop an unsafe visible field then mark the rest safe.
- Any AI-authored factual headline, question, comparison label, explanation, `suggestedEvidence`, answer or feedback requires actually trusted reviewed exact visible text+context receipt, otherwise **no visible model text**. This first stage has **no real approved human reviewer or authentication**; never fabricate review receipts. Allowed preview may contain only **system-owned neutral instructions** and exact rights-qualified owned-source quotations with locator+hash marked `SOURCE_QUOTE_PRESENT`, NOT verified historical truth.
- In particular, B4 F3-12 unrelated one-character citation must **never** cause a displayed `Recorded fact` or confident content; source-quote presence is not semantic entailment. A model-generated contradictory proposition cannot be transformed into a fact label by hashing. Keep `historicalTruthVerified=false`, `publishable=false`.
- Preserve **per-field text/media/translation rights**, distinguish rights-protected prose from publicly allowed asset metadata; do not allow NoC-US or missing licensed excerpts to be re-encoded into free text or `UNKNOWN` to bypass visibility gate. Not a general plagiarism detector: default deny unreviewed external copy, no real media.
- Keep internal IDs, state names `published`/`curator_approved`, raw trace and debugging metadata **out of all visible sinks**. Unknown kind, arbitrary AST, model-made HTML/JS or media URL cannot become a safe view.
- Hash/version the **actual display bytes**, source/quote/locator, source/content SHA, rights snapshot and policy, language/audience, review context, dependency status. Do not include variable timestamps/paths in deterministic digest.
- If rights revoke/contradict, snapshot or field changes, or complete static claim→question→feedback dependencies are unknown: **fail-closed whole preview**, `BLOCKED` or `NEEDS_REVIEW`. Rights restoration does NOT automatically reapprove. Do not claim precise selective revalidation without independent proof.
- Don't implement a synthetic authenticated curator or issue `APPROVED/PUBLISHED` states. Demo marker `DEMO_SIMULATION` is explicitly **NOT** real approval.
- Enforce bounded input/number-of-blocks/output size using current code conventions. No Node eval/Function/external network, HTML/JS output, file I/O in runtime adapter or new npm packages. Test and evidence tooling may write only approved local reports.

### Demonstrator

Two **owned fictional** records `ARC-01` PLAN(`proposalStatus=PROPOSED`) and `ARC-02` LEDGER(`serviceStatus=NOT_RECORDED`) for an explicitly nonhistorical demonstration. Two proposed learning questions remain hidden/NEEDS_REVIEW until legitimately reviewed; the demo may show safe source quote cards and neutral steps. This is a **data-only** preview, no browser interactions or actual Q/A correctness.

Synthetic mutation `NOT_RECORDED → IN_SERVICE` causes digest change and `NEEDS_REVIEW/BLOCKED`. Rights revoke `DEMO_OWNED → REVOKED` causes BLOCKED; restore requires re-review. Nothing auto-publishes. No imported real NYC/BPL/Met images or 3.14 museum material.

## 5. Test and acceptance

1. Run full existing suite (reported 194/194 before B5.2) and validate fixed hashes. The old B0–B5.1 history and oracle must not change. Test at least two complete runs **after** implementation, log exact command and exit. Mark `TYPECHECK_NOT_RUN` if still true; Node24 type-stripping is not type checking.
2. **All 32 frozen cases** must match exact status, no false historical authority, no untrusted text leak, no rights-laundered output, no model-created approval. Include positive benign cases and count false blocking separately.
3. Security adversarials must cover mutating input/getter/Proxy after initial binding, old B2 report reuse, F3-12 irrelevant quote, extra nested compare labels, root metadata-as-text, unsupported primitive, unknown output kind, malicious state ID, feedback hidden in harmless title, rights revoke→restore, `Data:...` benign false block (do not bypass frozen R3.5), SHA swapping and language mismatch.
4. Synthetic E2E flow from real B1/B2/B3 to B5.2 output **must actually call the existing APIs**, not copy mock decisions into a synthetic adapter. When a legitimately safe quote cannot be produced under existing v0.2 without unseen edits, return explicit `NEEDS_REVIEW` and report limitation rather than bypass contract.
5. Node24 built-ins, 0 new external deps, no AWS, no GitHub remote/push. Repeat results deterministic; compare semantic normalized report hashes, not raw TAP durations.
6. **B5.2 PASS** = positive owned quote and neutral system copy feasible under genuine existing validators, 32 original pre-registered negative/benign cases green, full historical 194 baseline green twice, actual integrated evidence SHA consistent, no privilege, truth or rights overclaims. Otherwise `B5_2_HOLD`, do not loosen tests to force pass.
7. Create one local B5.2 commit only on PASS, `main` clean and no remote, full SHA and full **unified diff** incl new files, files test/evidence manifest and step budget. Never rewrite older oracles or history.

## 6. Final Korean checkpoint; STOP

Report actual parent HEAD/full new B5.2 SHA, paths, exact added/deleted code counts, registered 32 case IDs and frozen manifest SHA, per-category 8-case pass/fail breakdown, two full suite runs/exit/output digests, input/visible-output binding proof, genuine B1/B2/B3 call route, 2-source demo status, provenance/credit uncertainty, residual P1 and rights/human-review limitations.

**Research alignment paragraph**: 3.11/3.12 first vertical slice=2–4 owned synthetic items, 3.14 12 research-only cases with 0 public rights approval, 3.15 data plan ready but real raw snapshots and independent oracle not collected. This B5.2 is infrastructure; no visitor/browser product or D1E comparator yet.

Keep `VISITOR_BROWSER_HOLD`, `D1E_EXECUTION_HOLD`, `D2_HOLD`, `PUBLISH_HOLD`, `REAL_MEDIA_HOLD`. Do not start B5.3, D2, AWS or another stage. No additional approval question is necessary for this already-approved B5.2 implementation alone.
