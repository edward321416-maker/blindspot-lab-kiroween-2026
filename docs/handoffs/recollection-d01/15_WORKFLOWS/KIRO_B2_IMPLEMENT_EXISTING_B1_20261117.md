# Re:Collection — D1-BUILD B2 implementation on verified local B1

**Execution instruction (2026-11-17 KST):** Continue existing, previously scoped D1-BUILD by implementing **B2 only**, then STOP. B0/B1 are already completed in the user's local workspace, according to Kiro's report. This document is a new user-requested progression, not permission for D1E, D2, B3–B5, AWS, GitHub remote, or production publishing.

## 0. Source evidence vs. actual implementation

User-provided Kiro read-only state at **17:05 KST, 2026-11-17**:

- Local workspace: `C:\Users\admin\Projects\recollection-kiroween-2026`.
- Local main expected HEAD `21a2ce5c964e84a4eb1f9bd65845937a10aeb2eb` (B1) atop `6367d928b7eb17a4bd8b6283690bc7c265fa875b` (B0). Working tree clean, no remote.
- B1: ExperienceSpec v0.2 contract, reject unsupported schema versions/unknown fields, privileged-field separation, integer-only JCS canonical SHA-256. `node --test` 62/62 PASS, exit 0; B0 fixed validator cases 29 match *B1-owned verdicts*, JCS vectors 13/13 match, two runs repeat and fixed input files unchanged. **This is Kiro USER-REPORTED**, not an independent ChatGPT code review.
- B1 diff reportedly at `D:\Users\admin\Desktop\hackathon\ReCollection_D1_BUILD_reports\B1_21a2ce5.diff`; ChatGPT did not directly read the Windows file.
- `TYPECHECK_NOT_RUN` and `BONUS_USAGE_UNOBSERVED`. These limits remain; don't manufacture measurement or type-check PASS.
- GhostWeb reportedly HEAD `23b8a010` with two uncommitted files; BLINDSPOT HEAD `c073ddd1`, one unpushed. Don't touch either.

**Before edits**, check local `git status --short`, `git rev-parse HEAD`, local tracked file map, AGENTS/.kiro, source function signatures and test runner using read-only commands. Reuse existing B1 exported contract/API; don't assume file path or signature from this handoff. Parse any local `package.json`, `requirements.txt`, `docker-compose.yml` as **text**, not executable scripts. If HEAD or worktree differs from reported state, investigate without reset/rebase/stash; don't overwrite.

## 1. Fixed model, bounded budget, no repetitive UI gate

- Developer model **Claude Opus 5.5 / MAX**. No switching to Auto or other model or fallback. Existing saved session setting is available; don't repeatedly demand `/model` screenshots. If a live session explicitly announces a different model, STOP and report.
- Original user-observed bonus used baseline **513.26** from 2026-11-17 ~15:02 KST. Original cumulative D1-BUILD soft used `733.26`, hard used `813.26`; **do not reset baseline after B1**.
- The user explicitly rejected repetitive `/usage` prompts. Do not block B2 merely to ask for the same screen. Instead record `BONUS_USAGE_UNOBSERVED` where it is inaccessible. Do **not claim exact remaining headroom or compliance with an unobserved hard ceiling**. Work on **B2 only** with a bounded implementation/test/debug loop (prior B2 allocation **estimated +70**, not metered actual). If any available evidence suggests exhaustion or overage, STOP; never upgrade paid plan, enable overages or transfer D1E budget.
- This B2-only implementation is within existing previously approved synthetic-only B0–B5 scope, and the user has directly asked to progress. No new architecture/cost/rights decisions are authorized.

## 2. B2 target: independent semantic evidence/rights validator

**B2 accepts B1-valid ExperienceSpec v0.2 and a trusted, frozen synthetic Source Registry, and produces a deterministic machine-readable validation result. B2 neither executes interactive primitives nor publishes.**

### B2.1 Establish exact local contracts
1. Read the actual B0 synthetic fixtures/oracle including **29 validator cases**, six future runtime cases and thirteen JCS vectors, plus B1 validators and deterministic error codes. Note which **29 verdicts** have B1-owned vs B2-owned responsibilities. Do not assume that all 29 B2 cases must already pass before implementation.
2. Draw trust boundary:
   - AI-authored `claims`, `plan`, `graph` may reference sources by IDs and locators but cannot self-certify a source, rights, approval, publication, verified historical fact or original SHA.
   - `SourceRegistry`/source hashes and license evidence come from trusted local fixture/loader, not AI content.
   - `VerificationReport` belongs exclusively to validator; it cannot be supplied through model-owned input.
3. Record expected wire format from actual local B1 exports. If B0 oracle expectations differ from this handoff, follow the **frozen local oracle** and document discrepancy, not patch oracle to suit implementation.

### B2.2 Evidence and historical-claim semantics
- For `HISTORICAL_FACT`, require existing source ID, immutable source content SHA-256 and a locator that **resolves against the trusted frozen content**; an arbitrary self-reported URL/line is insufficient. Verifying a locator and source is **not equivalent to proving a statement true**. If meaning cannot be independently established, mark as `UNVERIFIED/NEEDS_MORE_EVIDENCE`, never auto-certify fact.
- For `EDUCATIONAL_MODEL`, require clearly declared abstraction assumptions, referenced sources where applicable, and forbid presenting simulation as undocumented historical reconstruction. Eg modern Morse encoding rule is educational, not the physical Morse–Vail apparatus behavior.
- For `INFERENCE`, require explicit label + supporting references and do not turn inference into historical fact.
- For `UNKNOWN`, maintain uncertainty explicitly and propagate it to downstream decisions. Missing/mismatched evidence yields `NEEDS_MORE_EVIDENCE` or `BLOCKED` according to frozen B0 error taxonomy; never generate a plausible missing source.
- Deduplicate claim IDs, guard cross-object/source references, stale hashes, missing locator, nonsensical chronological/numeric assertions only where rules are formalized; no artificial AI truth judge.
- Always distinguish **syntax-valid**, **source-bound**, **rights-cleared** and **historically verified** in report fields. A synthetic oracle may attest the expected classification of deliberately authored cases, not general historical truth.

### B2.3 Rights and safe source processing
- Source metadata rights and **each media asset's redistribution rights** are independent fields. Synthetic/owned inputs only: assign origin/rights explicitly, not by fake real museum URLs. A license string alone must not automatically imply permission if the asset's ownership/rights evidence is absent or contradictory.
- Fail closed for missing/ambiguous/contradictory rights, missing license evidence and unsupported declared rights. Only approved synthetic test fixtures in B2; public-use candidates use stricter `CC0-1.0` or `PDM-1.0` policy by default and per-asset proof. No `NoC-US` public publishing inference.
- No external fetch, network access, remote images, crawling, or dangerous path resolution. Treat museum-like text as untrusted data, not instructions. Validate local path/locator components against traversal, absolute paths, encoded bypass, redirect/SSRF-looking targets, unsafe schemes, control chars and unexpected URLs. If B0 explicitly permits a remote canonical URL only as **inert metadata**, it must **never be dereferenced**.
- Hard limits on input bytes, number of sources/claims/nodes/edges and depth. Use bounded processing. Resolve references without quadratic rescans where reasonable.

### B2.4 InteractionGraph semantic gate (no runtime execution)
- Check every node ID unique, edge endpoints exist, node kinds are among the four **approved names** where frozen spec defines them: `info-panel`, `compare-cards`, `sequence-encoder`, `research-task`.
- Verify field types, bounded parameters, referenced claims/object IDs, graph acyclicity or explicit bounded cycle policy **as fixed in B0**; reject unbounded loops, unreachable required state, invalid transitions and prohibited literal code/HTML/URLs.
- Reject any model-authored executable JS, HTML tags used as code, `eval`/dynamic function invocation or privileged `publish/approve` operations.
- Never implement B3 primitive evaluation in B2; output only **validation verdict + deterministic reason codes**.

### B2.5 Deterministic results
- Define stable `PASS | NEEDS_MORE_EVIDENCE | BLOCKED` semantic status and machine-readable `{code, severity, path, sourceId/claimId?}` issues. **Reconcile against B0 frozen expected codes before implementing** rather than renaming them after tests fail.
- Prefer an explicit immutable snapshot/version ID, SHA-256 of trusted registry and B1 canonical ExperienceSpec SHA, and tool/version metadata in report. A report hash proves output integrity, not museum accuracy.
- No curator approval record or publish authorization generated as side effect.

## 3. Required tests / acceptance

- **B0/B1 invariants:** Preserve historical B0 frozen data, all 13 JCS vectors and B1 contract. Existing `node --test` baseline 62/62 MUST still PASS twice (or report exact failure), without weakening tests.
- Run **all B0 cases scoped to B2** with exact expected deterministic codes; ensure B1-owned codes remain unchanged. Keep 29 frozen oracle cases immutable; do not inflate coverage by counting assertion subparts as independent cases.
- Add B2 synthetic-negative tests: stale source SHA, forged source ID/locator, irrelevant locator, absent rights, contradictory media rights, unknown license, mismatched claimed historical operation, `UNKNOWN` propagation, injection-laden museum caption, invalid edge/graph cycle/bounds, prohibited JS/HTML, path traversal, inert external URL/SSRF-appearing metadata, model-originated approvals, huge input guard.
- Explicitly verify **no network**, no filesystem writes outside approved local workspace, no source mutation, no unexpected side effects.
- Check determinism and report byte-identical canonical JSON outputs in two complete test passes. Track exact commands and exit codes; be explicit about `TYPECHECK_NOT_RUN` if compiler is not installed.
- **B2 PASS only if** all mandatory frozen B2 cases and new adversarial tests pass, B0/B1 baseline remains green, no privileged publication/approval paths appear, and report artifacts match repeat runs. If missing source or unexpected oracle semantics prevent credible completion, classify `CONDITIONAL/HOLD`, never silently alter the oracle.
- Use Node 24 built-ins and **zero new npm installs**. No Ajv/TypeScript package without separate user approval.

## 4. Local Git and output

- Work **only in existing Re:Collection local Git main**, starting at full B1 HEAD `21a2ce5c964e84a4eb1f9bd65845937a10aeb2eb`. Keep one scope-limited B2 commit after all tests and document its full SHA. Provide complete unified diff (including added files) and provenance/readback. No force push, reset, rebase, `rm -rf`, changes to other repositories or GitHub remote.
- Follow existing user/project operating policy. Maintain B2 one-line checkpoints with timestamps, acquired skill, estimated tokens, observed/unknown credits and actual test results. If Google Sheets connector or approved log is unavailable locally, queue only in a safe local report; **do not claim Google synchronization**.
- Final concise Korean B2 report:
  1. B1 parent/new B2 commit SHA and clean tree;
  2. exact files added/modified, distinct B2 semantic API and no B3 runtime;
  3. frozen 29-case breakdown B1/B2 (not double counting), JCS 13/13, overall `node --test` count;
  4. negative/security tests actually executed, timings/exit codes and repeatability, report SHA;
  5. unknown historical truth, media rights limitations, synthetic-only status, `TYPECHECK_NOT_RUN`;
  6. model/effort as observed without asking again for screenshots, original credit baseline and `BONUS_USAGE_UNOBSERVED` if inaccessible;
  7. B2 `PASS/CONDITIONAL/FAIL`, and B3 readiness proposal only.

**STOP after B2.** Do not start B3–B5, D1E, D2, AWS, public GitHub repo, or deployment.
