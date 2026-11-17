# Re:Collection B5.1 — Snapshot & evidence-integrity corrective patch

**STATE: SPECIFICATION PREPARED / NOT AUTHORIZED BY B5 REPORT.**  
**Approval required:** separate explicit user authorization to modify the post-B5 source, tests and local evidence reports. No product release or real-data work.  
**Parent baseline:** local (user-reported) B5 commit `b112c6a93c715e027a8ad3155f35a667f5260396`; existing local `main` with **no remote**. Preserve every B0–B4 frozen oracle and all preceding commits/diffs.

## Why this patch comes before D1E actual runs

Actual B5 fresh same-model QA reported three reproducible defects:
- **B5-05:** an in-process Proxy/getter can cause 121–200 actual steps despite a 50-step check on a different caller-owned object.
- **B5-06:** B2 validator rereads mutable object values, producing a report marked VALID with a digest for a semantically different object. B3 rechecks today, but detached consumers would be exposed.
- **B5-07:** B4 `scriptSha256` can hash a later re-read of an input rather than the exact executed script; `suppliedReportSha256` is insufficiently constrained.
- **B5-17:** repeated test names: 164 tests, 135 distinct test names. This is a reporting/attribution defect, not a security gate.

These are `KIRO_USER_REPORTED` from the directly read 284-line B5 attachment. Their exact functions/paths must be identified from local `rg`/AST, not invented by this document.

## Allowed changes — only after user approval

**B5.1-A / Execution snapshot step bound (mandatory):**
1. Derive a **single normalized, bounded execution copy** of `spec`, `snapshot`, `script`, `mode`, `validation` before execution. All validation, script-length limit, event iteration, output digest and trace construction operate on that **same immutable copy**. Avoid a second read from raw caller-owned object.
2. Calculate `steps <= 50` on the script actions that are actually executed, not an external reference. A 51st action fails closed before any primitive effect. Preserve 50-step PASS, 51-step refusal and output 256 KiB cap.
3. If callers supply in-process exotic objects/accessors/Proxy, document explicit input type boundary. Prefer rejecting accessors/unsupported prototypes, bounded one-shot normalization or accepting strict JSON bytes/text only. It is impossible to promise arbitrary malicious JavaScript Proxy has no side effects when inspecting it; guarantee only that downstream execution uses a stable copy and fails closed if normalization fails. Prevent getter read-twice variance.
4. Tamper/adversarial tests must reproduce original B5-05 counterexamples, including 121/200 step mutation and nested getter/proxy shape, and show correct refusal **without changing original B0–B4 oracle**.

**B5.1-B / B2 report/input binding (mandatory):**
1. In `validate()` and `validateText()`, canonicalize or strictly parse into one trusted bounded JSON-like snapshot once; compute source/spec hashes and semantic verdict **from identical bytes/copy**. No subsequent raw caller reads for reported data, locators, claims or trust flags.
2. Reject unsupported object kinds and noncanonical/duplicate-key textual input under existing B1/B2 contract. If the B1/B2 exported API needs a compatible wrapper or a versioned overload, preserve existing callers and test expectations, don't weaken old fail-closed behavior.
3. A B2 `VALID` report is a *verdict for exactly one snapshot*, not a transferable authorization for caller-provided reportSha256. Require B3/B4 revalidation, hash/mode comparison and system-only provenance as before.
4. Add tests reproducing original B5-06 mutable-getter `VALID`/false-hash evidence; ensure a mismatched snapshot/hash cannot acquire a VALID report for a different snapshot. Document residual limits with executable in-process Proxies.

**B5.1-C / executed script hash and evidence (mandatory):**
1. Generate `scriptSha256` from **exact normalized script used by B3 runtime**, not from a caller input reread after completion.
2. Require any supplied SHA256 field to match canonical lowercase/uppercase normalization policy and **64 hex characters**, reject invalid shape; then validate by recomputing from trusted data. Hash shape correctness is not hash authenticity.
3. Add version identifier to new B5.1 evidence format. **Do not overwrite old B4 historical evidence or retroactively alter its recorded SHA.** Store the new artifact as `B5_1_...` with its own content hash, source commit, comparison to B4 baseline and an explanation of any new digest differences.
4. Adversarial tests: flip-on-read object, altered reportSha256, script mutated after first access, non-hex/short hash, legitimate identical data, canonical vector replay.

**B5.1-D / test naming (OPTIONAL, reporting only):**
- Preserve test files/names of the B0–B4 historical baseline and their normalized TAP digests. **Do not rename 164 existing tests** merely for cosmetic uniqueness. Instead add a machine-readable `stageId / testFile / testId / testTitle` identity in a *new versioned report* or scoped harness test. Fix only if lightweight and doesn't obstruct security A–C.
- Explicitly state tests count 164, distinct names 135 from B5 baseline; after B5.1 report new counts accurately. Do not call 536 assertion calls independent test cases.

## Forbidden changes (require different user decision)

- **Do not patch B5-01/B5-02 historical-entailment/output-sink problem in this task.** Keep visitor-visible output/publication **HOLD**. Source-linked yet unentailed text remains a P1 issue requiring separate reviewed output-policy/curator contract.
- **Do not change R3.5 `UNSAFE_TEXT`** on the basis of observed overblocking. A safe rule update can change security semantics and 3 frozen test outcomes; needs separate ADR/security approval and before/after attack+benign matrix.
- No `ExperienceSpec 0.2` silent schema expansion, 3–8 object migration, output OAP adapter, visitor feedback generator, UI/auth/publisher, D1E model arm execution, third-party museum data, AWS/Bedrock, public GitHub/push, paid service.
- No new npm dependency; TypeScript checker/Ajv only if separately approved. Node 24 built-ins and existing test tools first.
- No modifying protected GhostWeb/BLINDSPOT, reset/stash/rebase, rewriting any prior historical commits, or deleting old diff/evidence files.
- No copying held-out research cases/answers into local Kiro repo or public GitHub.

## Frozen pre/post acceptance + deliverables

**Preflight**, first validate expected full local B5 HEAD, clean tree, no remote, original oracle and B4 evidence hashes; confirm user explicitly authorized this patch. If the user has not approved, run **READ-ONLY review only**. Inspect file signatures first, then targeted bodies.

**Before implementing** register 10+ adversarial tests (including all B5-05/06/07 counterexamples and nonregression):
- B5-05 Proxy/getter step-length flip, 50/51 boundaries, 100,000 steps, output max, no partial traces on refusal.
- B5-06 mutated claims/rights/locator/source during validation, report hashes bound to effective snapshot; string duplicate key fail.
- B5-07 supplied script/report SHA tamper and canonical normalized executed script only.
- B0–B4 same existing oracle, R01–R06 6/6 and B4 F1/F2/F3 count. Leave historic files frozen.
- No extra code execution, network, files, approval/publish paths; fail closed on unknown.
- Repeat full `node --test --test-reporter=tap "tests/**/*.test.ts"` **twice**; expected original 164 pass plus **actual** new tests, no arbitrary PASS claims. Byte-compare deterministic **semantic** digests, preserve raw TAP separately.
- Run same-model fresh challenge pass if feasible, mark SAME_MODEL not HUMAN-INDEPENDENT.
- Status `PATCH_PASS` only if previously demonstrated B5-05/06/07 are now refused/bound on actual copies and previous B0–B4 regressions green; otherwise `PATCH_HOLD/REWORK`. Don't force a pass by changing frozen oracle or disabling security tests.
- Commit **one bounded local B5.1 patch** if tests pass; provide full commit SHA, complete unified diff including new files, exact commands/exits, changed hashes and diff path, original B5 report/diff SHA, P0/P1/P2 residual risk.
- Report `TYPECHECK_NOT_RUN` unless checked, `BONUS_USAGE_UNOBSERVED` if unmeasured, `SESSION_CONFIG_ONLY` for effort if needed. No repetitive screenshots. Keep previous budget limits as guardrails; do not claim confirmed compliance without data.
- **STOP** after B5.1. Do not auto-run D1E or develop D2.

**Output for product planning:** `B5_1_PATCH_PASS` does not resolve P1 misleading recorded fact or real rights. Separate `OAP` and D2 product release gating remain blocked.
