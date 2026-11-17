# Re:Collection — D1-BUILD preflight review and approval template

**Document date:** 2026-11-17 KST  
**Status:** HOLD / PREPARED FOR DECISION ONLY / D1 IMPLEMENTATION NOT AUTHORIZED

## Provenance

This memo assesses the **user-pasted Kiro preflight summary**, not a byte-verified copy of the reported local 65-line file
`D1_BUILD_preflight/ReCollection_D1_BUILD_Approval_Brief_20261117.md` (reported truncated SHA-256 `7f8150f0...`).
The original local report, source ZIP and final Master Audit are NOT present on the GitHub docs branch.
Do not represent this memo as the full original source.

Available GitHub basis: `01_START_HERE`, `07_DECISIONS/D0_3_REVIEW_AND_SCOPED_BUILD_GATE_20261117.md`,
`08_PLANS/D1_BUILD_BOUNDED_SPEC_APPROVAL_PENDING_20261117.md`.
Existing GhostWeb and BLINDSPOT user worktrees are out of scope and remain protected.

## Core review

| Component | Verdict | Verified vs proposal |
|---|---|---|
| Node 24.14.0 + npm 11.21.1 reported locally | FEASIBLE, user-reported | No version upgrade necessary for this bounded prototype |
| Native TypeScript execution on Node 24 | FEASIBLE with restrictions | Type-stripping of erasable TS only; **does NOT typecheck**, does not honor `tsconfig`, and cannot run runtime TS features (`enum`, non-erasable namespace etc.) without transformation |
| Dependencies | START WITH ZERO | `node:test`, `node:crypto`, `node:assert` support core tests, hash and contract checks. Do not equate zero dependencies with passing static typecheck or robust schema/rights proof |
| Type checker `typescript@7.0.2` | DEFERRED DEV TOOL | npm lists 7.0.2; if needed, separately approve and pin version + lockfile, run offline-friendly scoped type check |
| Ajv `8.20.0` | DEFERRED BACKEND SCHEMA VALIDATOR | MIT; if approved later, compile only trusted developer-authored schemas, never dynamically compile AI-authored schemas; no codegen inside restricted Runtime |
| Primitives | PROPOSED FOUR | `info-panel`, `compare-cards`, `sequence-encoder`, `research-task`. Require exact bounded semantics and deterministic negative tests before coding, do not treat names alone as implementation contract |
| Runtime scope | STRUCTURED OUTPUT ONLY | No browser rendering, editor or publisher in D1; browser functionality remains unverified, not a test pass |
| ExperienceSpec version | ACCEPT ONLY `0.2` in D1 | `0.1` source unavailable => BACKWARD_COMPAT_UNKNOWN, fail closed; disallow model-authored `verification`, `approval`, `publication` |
| Object counts | 1-item smoke TEST HARNESS ONLY; 2–4 items for publishable product | D0 policy remains proposed; ensure AI cannot enable one-item bypass by generated JSON |
| Synthetic-only | FEASIBLE | No real museum media, external crawling, AWS or public output for D1 |
| Saved model/effort | `claude-opus-5.5` / `max` SESSION_CONFIG_ONLY | Effective turn/session model still requires live observation; no Auto fallback |
| Credit budget | SOFT +220, HARD +300 D1-BUILD ONLY | Still unapproved and no fresh `/usage` baseline. D1E additional budget NOT covered |

### Practical validity distinction

Native Node TypeScript strip mode does **not** execute `tsconfig` compiler options and performs **zero static type checking**. At package-zero stage record `TYPECHECK_NOT_RUN`; dynamic schema validation and deterministic test assertions must not be misrepresented as static type verification.

If requirements demand compile-time type safety rather than only runtime validation, propose `typescript@7.0.2` as an explicitly approved **development-only** dependency when reaching B1 or B2. `ajv@8.20.0` is not needed in restricted runtime merely because it is on an optional list; a trusted offline schema validator can be built with standard library for a narrow fixed contract, but document its limitations.

### Proposed immutable primitive contract additions

- `info-panel`: display content and source-bound claims only; no raw HTML, script or external URL resolution.
- `compare-cards`: pairwise compare structured known fields on two source-linked objects; no claim of derived physical or historical differences without evidence.
- `sequence-encoder`: bounded deterministic encoding of explicitly declared educational alphabets/rules; no emulation of an original historical machine's undocumented behavior.
- `research-task`: prompt a user to inspect original evidence or mark UNKNOWN; no automatic historical completion, evaluation authority or publication.
- Every primitive has input/output schema, maximum size/steps, deterministic error code, source reference, rights check and pre-registered expected behavior. No arbitrary JS or HTML code from AI output.

## D1-BUILD scope recommendation

**YES if and only if the user separately approves after measured usage:**

1. Isolated path `C:\Users\admin\Projects\recollection-kiroween-2026` (check nonexistence; don't overwrite), new local repository with **no remote**.
2. Scoped B0–B5 only from pinned `08_PLANS`: ExperienceSpec v0.2, evidence/rights validator, four bounded primitives, synthetic 1-item smoke + synthetic 2-item E2E, own-object tests, no real publishing.
3. Strict preservation of GhostWeb dirty worktree and BLINDSPOT unpushed commit.
4. Node 24 native TS (erasable syntax), zero npm dependencies at initial build; any new `typescript`/Ajv installation **requires separate scope review**.
5. Claude Opus 5.5 / effort MAX only; no fallback; recorded actual session and `/usage` observations before and after phases.
6. Fresh `/usage` starting number **must be provided**, with +220 soft / +300 hard **incremental** budget, not USD. Stop/return a status report at soft and stop implementation at hard. No paid upgrades.
7. D1E A/B, D2 curator UI/publish/auth, AWS, external rights-sensitive objects, GitHub repo remote, public deployment are **NOT approved** by D1-BUILD.
8. Despite inaccessible original Master Audit on Kiro PC, the user may explicitly choose to treat the pinned **self-contained B0–B5 contract as sufficient** for this bounded synthetic-only build, documenting the original-source gap as a risk acceptance. This choice has **not** been made yet.

## Approval message — TEMPLATE ONLY; NOT AN EXISTING USER APPROVAL

Do not invent the starting /usage number, or misrepresent the following as signed.

> Re:Collection D1-BUILD B0–B5 **only**: I approve an isolated new local workspace and local-only Git at the stated empty path, Node24 with zero initial npm dependencies, the four strictly bounded primitives and ExperienceSpec 0.2-only with fail-closed unknown fields and test-harness-only single-item smoke. Synthetic/owned data only; no curator UI, publisher, D1E, AWS, GitHub remote or deployment. I accept use of the pinned D1-BUILD contract despite the original Master Audit binary remaining unavailable in Kiro's Windows workspace. Claude Opus 5.5 / MAX only, no fallback. I approve an incremental Kiro credit envelope soft +220/hard +300, measured from /usage: [actual date/time, bonus pool used and plan credits]. If model/effort or /usage cannot be verified, STOP before substantial implementation. Optional packages remain unapproved; propose them separately if later needed.

If the user does **not** send an approval equivalent in scope to this template, D1 remains HOLD. Merely reading this GitHub file does not authorize action.

## Independent evaluation not required for this build

D1-BUILD uses deliberately synthetic tests; it cannot establish market usefulness or beat Opus direct coding.
The separate human blind holdout author and the independent rights reviewer are mandatory before **D1E** and before asserting credible generalization with real assets, **not required to initialize a bounded synthetic-only core** after specific user approval.

## Next action

User supplies the observed `/model` and `/usage` values and explicitly accepts or edits the above scope. Kiro then receives a *different*, approval-gated implementation prompt. The prompt in `11_WORKFLOWS/` is **preflight only**.

Official public sources:
- https://nodejs.org/api/typescript.html
- https://www.npmjs.com/package/typescript
- https://www.npmjs.com/package/ajv
- https://kiro.dev/docs/cli/reference/slash-commands/
