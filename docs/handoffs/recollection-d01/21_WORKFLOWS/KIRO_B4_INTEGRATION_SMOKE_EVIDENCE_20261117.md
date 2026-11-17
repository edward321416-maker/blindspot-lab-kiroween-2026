# Re:Collection D1-BUILD B4 — synthetic end-to-end integration and evidence packet

**Execution scope:** Existing approved D1-BUILD **B4 ONLY**, starting from completed B3; **STOP after B4**. This is not D1E A/B, B5 final audit, D2 curator UI/publishing or product selection.

Read from the same immutable GitHub commit:
- `docs/handoffs/recollection-d01/20_ALIGNMENT/B3_COMPLETE_B4_PRODUCT_RESEARCH_GATE_20261117.md`;
- `docs/handoffs/recollection-d01/08_PLANS/D1_BUILD_BOUNDED_SPEC_APPROVAL_PENDING_20261117.md`;
- this execution file. These public docs do NOT contain user's unpushed local project code. Treat the actual local frozen B0 contracts/oracle as authoritative for case expectations.

## 1. Starting state — verify, do not reconstruct

Expected isolated Windows repository: `C:\Users\admin\Projects\recollection-kiroween-2026`; local `main`, no remotes, clean; expected B3 HEAD `4c4dc7adf49f8c6a3e699da0370bd8c93374e98a`, parent B2 `54f88b5be8a50afa187640d7d8564f75cb7b51ae`.

**If B4 already exists in the actual local Git history, do not run it again.** Read-only compare commit, tests, report and publish a completion checkpoint in chat only.

Inspect actual `AGENTS.md`, `.kiro` requirements, frozen B0 oracle/manifest, B1/B2 `validate()`/`validateText()`, B3 `run(spec,snapshot,script,{mode,validation})`, B3 evidence generation and local scripts before changing anything. Use `rg`/grep/AST for exports and signatures first; do not dump entire source indiscriminately. Read `package.json`/`requirements.txt`/`docker-compose.yml` as metadata text if present, do not execute declaration files. STOP safely on unexpected branch/HEAD/dirty conflicts: no reset, checkout, stash, rebase, overwrite or destructive cleanup.

Reported current baseline: B0 3, B1 59, B2 50, B3 22 = **134/134** two runs and postcommit pass. R01–R06 6/6. This is `USER_REPORTED`, **not independent GitHub evidence**, and must be checked against real local files.

## 2. B4 integration purpose

Establish that **B1 schema → B2 trusted-source semantic/rights validation → B3 structured deterministic runtime → machine-readable evidence** works without manual artifact editing.

**Fixtures:**
- **F1 ONE-OBJECT UNIT_SMOKE**: owned synthetic source/object ONLY, trusted *test harness* sets `UNIT_SMOKE` mode; AI-authored ExperienceSpec cannot set this mode and the output is always `publishable=false`.
- **F2 TWO-OBJECT SYNTHETIC E2E**: two owned distinct synthetic source assets with fixed content/hash and explicit rights evidence, normal nonpublishing mode; invoke real contract validator and B2 validator on frozen local snapshot and then invoke actual B3 `run`. The full path should reach contract-defined completion state using a fixed declarative visitor event script; do not invent additional `user:` events or primitive behaviors not in B0–B3.
- **F3 NEGATIVE GATES**: synthetic invalid/missing rights, wrong/irrelevant locator, mismatched quote hash, input change after validation, forged/detached validation report, `NEEDS_MORE_EVIDENCE`, non-allowlisted primitive, `publish` event, one-object mode spoofing. Each refusal must terminate before any model-authored/executable code or curator publication artifact appears.

Fixtures are **only owned/synthetic**, not actual museum material, not any research 3.2 developer holdout, and no internet fetch.

### Boundary proofs
1. **Snapshot binding:** Check source content hashes/registry version and B1 canonical spec SHA, with B2 evidence report bound to the exact same normalized bytes/mode as B3 `run`. Passing a stale, forged or mismatched `reportSha256` never enables execution.
2. **Rights:** Distinguish source metadata from each asset's usage proof; missing/contradictory rights must fail closed; `historicallyVerified=false` and `publishable=false` throughout.
3. **Trust:** Only trusted harness sets `UNIT_SMOKE`; model fields `validation`, `approved`, `publishable`, `publication`, system-generated status/verification are not execution authority.
4. **Runtime:** Four existing allowlisted primitives ONLY, max 50 steps, max 256 KiB outputs, deterministic finite trace. Do not expand to 3–8 objects, AI-generated feedback, browser rendering or full Archive Detective visitor journey in B4.
5. **Evidence:** Emit a compact immutable record with fixture ID, hash of input spec/source snapshot, B1/B2 verdict and issue codes, B3 trace/exit reason and final state, evidence/tool version and deterministic result hash. Keep wall clock, local path and mutable run metadata OUTSIDE the deterministic digest. Use actual local schemas, do not invent fields incompatible with B1/B2/B3.
6. **Non-authority:** Passing B4 should never fabricate historical truth, rights for external media, human curator approval, independent evaluator score, accessibility certification, web deployment or AI quality superiority.

### Regression and attack requirements

- Preserve **all B0 fixed oracle data** (29 validator, six runtime, 13 JCS vectors) byte-for-byte and B1/B2/B3 tracked source/tests except minimal *explicitly justified* B4 integration adapter modifications; prefer new integration tests/evidence tooling over altering prior stage logic.
- Run `node --test --test-reporter=tap "tests/**/*.test.ts"` **at least twice** after implementation, capture exact exit codes, total test count and stable deterministic digest. Do not merely compare raw TAP text if test duration or ordering changes across runs; normalize only the explicitly non-semantic fields and retain raw logs.
- Explicitly demonstrate two-object end-state and one-object test harness state, plus negative cases. R01–R06 remain 6/6 matching.
- Add an integration attack for quote locator that exists but does **not** semantically entail a historical claim; the expected result must **NOT assert historical truth** even if B2 syntactically passes. Do not silently rewrite B2 semantic rules in B4.
- Exercise normal benign `Data: ...` text through B2 as a documented expected **P2_OVERBLOCKING** result only; do not loosen security rules or bypass B2 to obtain a green run.
- Confirm no network calls, filesystem writes outside approved local evidence/report directories, mutation of caller's input, HTML/JS output, approval/publisher side effects.
- No new dependencies; Node 24 built-ins only. TypeScript native strip execution is **not** typecheck; report `TYPECHECK_NOT_RUN` unless a previously approved checker exists.

## 3. Deliverables and PASS/FAIL

1. New or minimally modified B4 integration tests/harness + deterministic evidence generator. Keep testing/approval responsibilities separate from model input.
2. Final evidence packet should identify **EXACT tests executed**, frozen fixture hashes, both run output hashes, baseline/total test counts, negative-case results, and known risks. A stage can be PASS for deterministic *synthetic integration* with historical `NOT_VERIFIED`.
3. **B4 PASS only if** F1 one-object smoke is trusted-harness only and nonpublishing, F2 two-object E2E reaches expected terminal state, F3 all refusal cases fail closed, B0–B3 regressions pass twice, output deterministic and original oracle immutable, no privileged output/side effects.
4. On any blocker, report `B4 HOLD/FAIL` with direct evidence rather than changing oracle, weakening validation, skipping tests or claiming a product demo.
5. Create **one local B4 commit** only when tests pass; exact full SHA, clean tree and no remote. Save full unified diff including newly created files; never force, push or change protected projects.
6. Submit concise **Korean** B4 report and research alignment:
   - Actual parent B3 SHA/new B4 SHA, diff path and full hash;
   - F1/F2/F3 per-case final states/reason codes, count, run outputs;
   - two full `node --test` results/exit codes, B0–B3 invariant SHA and mutation/tamper checks;
   - historical/rights/generalization limitations, `TYPECHECK_NOT_RUN`, `BONUS_USAGE_UNOBSERVED` if unavailable;
   - research gap: ARCHIVE DETECTIVE 3–8 vs frozen 2–4; missing choice/feedback; research 3.7 dependency closure not achieved;
   - B5 is a **separate** QA/go-for-D1E-prep recommendation, not execution.

## 4. Credits, model, and strict no-go

- Keep Claude **Opus 5.5 / effort MAX**, no Auto or fallback; do not ask the user repeatedly for `/model` screenshots. If settings-only is observable, `SESSION_CONFIG_ONLY` is correct; do not manufacture per-turn attestation.
- Original user-observed Kiroween bonus used baseline = `513.26`, cumulative D1-BUILD soft `733.26`, hard `813.26`. New current usage not observable => `BONUS_USAGE_UNOBSERVED`; no claim that the hard cap was measured/enforced. **B4 planned approximately +40 credits only** (estimate, not meter). Scope execution to B4, avoid unbounded retries or automatic B5 continuation. If real readings reveal cap reached/exceeded, STOP.
- No unapproved npm package, AWS/Bedrock, GitHub remote/push, external museum assets, rights-sensitive study corpus, D1E A/B comparison, D2 UI/auth/publisher, B5 QA execution, browser/keyboard testing or deployment.
- GhostWeb/BLINDSPOT worktrees remain wholly untouched; do not run Git mutations in them.
- Append one-line phase checkpoint and local report as configured; if no Google Sheets connector exists in Kiro, queue `PENDING_SYNC` and do not claim remote logging.

**Stop after B4**. This is one bounded integration stage under an already-accepted development program, not a new product contract or evidence of contest readiness.
