# Re:Collection D0.3 review — development decision register (2026-11-17)

**STATE: HOLD / REVIEWED PLAN ONLY / NO D1 EXECUTION APPROVED**

## Source and confidence

This is an independent assessment of the user's pasted **Kiro D0.3 summary** (83-line local report reported, but full local file not directly read here), with comparison to previously verified public GitHub handoff documents. It **does not** establish a verified local Kiro `/usage` baseline, an independently sampled holdout, a rights reviewer or byte-level availability of the original Master Audit in the user's Windows Kiro environment.

Previous GitHub documents available in this branch:
- `01_START_HERE/ReCollection_DevChat_Handoff_Phase0_ReadOnly_20261117.md`: labelled text transcription, not original byte-identical ZIP member.
- `04_EVIDENCE/D0_2_SOURCE_RECONCILIATION_20261117.md`: records prior independent ChatGPT workspace SHA checks for six originals, not original files hosted on GitHub.
- `05_DECISIONS/D0_2_REPORT_REVIEW_AND_D1_GATE_20261117.md`: earlier decision recommendations.
D0.3 Kiro report source: user-pasted summary on 2026-11-17, not a remote verified original. D0.3 original local file is `D0_3/ReCollection_D0_3_Decision_Review_20261117.md` inside the reported D0 report directory.

## Current factual ledger

| Item | Source/quality | Consequence |
|---|---|---|
| Kiro config model=`claude-opus-5.5` effort=`max` | Kiro local `session.json`, user-reported `SESSION_CONFIG_ONLY` | Supports intent; does not prove actual model for every turn |
| `/usage` | `USAGE_UNAVAILABLE` | Cannot authorize a quantified credit cap from an unknown starting balance |
| Existing Node 24.14.0 supports `node:test`, SHA-256, fetch | Kiro local verification, user reported; official Node24 LTS | No compulsory Node26 upgrade; no `npm install` has been authorized |
| Existing GhostWeb tree | Reportedly two uncommitted files on `d1.4-p1-closure`, no stash | Preserve completely, do not make D1 dependent on cleanup |
| Existing BLINDSPOT tree | Reportedly local commit `c073ddd1...` ahead of remote | Preserve completely, do not push or rebase |
| Original Master Audit / ZIP on Kiro PC | `UNAVAILABLE`; prior ChatGPT provenance note only | Treat an exact original-source audit as blocked; any accepted excerpt is a substitute **only with explicit human acceptance** |
| Human holdout designer and rights reviewer | `UNASSIGNED` | D1E live comparison blocked; not necessarily D1-BUILD core development blocker if **synthetic/owned inputs only** |

## D-1–D-7: separate decisions from implementation approval

The choices are quoted/reasoned from the **user-pasted D0.2 and D0.3 reports**. No user approval is asserted.

| ID | Technical recommendation | Current authorization |
|---|---|---|
| D-1 | Preserve GhostWeb dirty files without commit/reset/stash; separate product cannot depend on its code | RECOMMENDED, no action |
| D-2 | Release configuration has **2–4** objects. A **one-object synthetic unit-smoke** fixture is enabled ONLY by test harness configuration, never by model-generated spec | USER APPROVAL REQUIRED (public product contract) |
| D-3 | Split **D1-BUILD** (compiler/validator/primitive runtime) from **D1E** (A/B experimental comparison), separate credit caps and GO decisions | USER APPROVAL REQUIRED (architecture/cost) |
| D-4 | D1-BUILD cost estimate reduced to **145–270 credits** after deferring curator UI/build publish implementation. Proposed soft **220**, hard **300** incremental credits for *scoped core only*; previously suggested 260/340 remains an alternative, not approved. Fresh `/usage` is compulsory before charged work | HOLD until user + usage |
| D-5 | D1E should preregister **2 runs/case** when feasible, not change after outcomes. Earlier 60–120 estimate assumed one pass; *rough* two-pass envelope **120–240 additional credits**, to be re-estimated with pilot and actual readings, not approved | HOLD for D1E |
| D-6 | Candidate public exhibit media allowlist `CC0-1.0` / `PDM-1.0`, plus proof of rights for **each** image/object and attribution. Exclude `NoC-US` until separately assessed; metadata and each media's rights differ | USER APPROVAL REQUIRED (rights policy) |
| D-7 | Re:Collection is independent of GhostWeb. Official contest submission period began Oct 30 2026; reported GhostWeb first commit Nov 16 is within that window, but provenance of any pre-existing reused work remains separately relevant | NO IMPACT on Re:Collection D1 |

**Do not silently reinterpret D0's `1–4` prototype concept as accepted `2–4` release schema.** Distinguish test-harness smoke mode and product published mode in the actual design.

## Scope decision: narrow D1-BUILD to avoid endless D0 reviews

D0.3 identifies a key scope discrepancy: initial proposal included approval journal, publication builder and curator UI, while the later memo deferred these to D2. Proposed resolution:

**Included in separately approved D1-BUILD**:
- isolated **new Re:Collection** workspace (not GhostWeb/BLINDSPOT reuse);
- TypeScript/Node24 LTS core (actual package/versions must be recorded), minimal libraries only if separately approved;
- ExperienceSpec v0.2 `claims/plan/graph` model output schema; privileged `verification/approval/publication` are **server/validator-owned**, not LLM-owned;
- `schemaVersion` and explicit unknown-field rejection, migration decision table from v0.1 **only if original v0.1 bytes are available**;
- deterministic canonical hash with documented **integer-only JCS (RFC8785 subset)** and cross-runtime test vectors; no unproven byte equality claims;
- evidence/claim/source semantic checks, per-asset rights fail-closed, bound inputs/graph parameters, allowlisted primitive registry;
- type/schema placeholders for verification/approval/publication and **immutable approval triple-hash binding** design (source/spec/build); do not implement real publishing authority;
- synthetic/owned one-item smoke and two-item nonpublishing end-to-end fixtures, deterministic `node:test`, negative tests for fabricated historical claims, publisher authority, injection and missing rights;
- build/runtime tests and a true SOURCE/UNKNOWN/inference distinction; local-only outputs.

**Not included in D1-BUILD**:
- curator authentication, UI/editor, approval ledger production implementation, publication builder/live site deployment (defer to D2);
- AWS Bedrock, cloud credentials/costs, remote source crawling, third-party museum image download;
- Arm A direct coding competition or empirical superiority claims (D1E only);
- final contest release/licensing selection, GitHub public repo creation or merge;
- independent holdout execution (D1E only). Role design and frozen scoring plan may be prepared.

This is a **proposal**, not authorization to create files/install dependencies.

## Model, review, and cost policy

- Kiro **Claude Opus 5.5 / MAX only**. No mandatory other-family model reviews; independence is protected by *human* holdout owner, separate sessions/workspaces and an oracle frozen before model output.
- Session configuration is not per-turn model attestation; record actual `/model` and `/usage` only when visible. `Credits: turn/session` counters are not `/usage`.
- D1-BUILD **soft +220/hard +300** proposed from a fresh observed baseline; D1E separate **provisional +120–240** for two-run design; no automatic transfer between pools, no paid upgrade.
- Cost/complexity and outcome small-sample generalization uncertainty are explicit.

## Evidence remaining, and the decision to request

**Hard blockers to D1-BUILD (cost-bearing implementation):**
1. Explicit user approval of *isolated workspace creation*, chosen minimal TS/Node24 stack, any named npm dependencies and local test execution, and specific per-task Kiro credit cap.
2. Fresh user-visible `/usage` reading (timestamp + bonus pool before), and model/effort observation; if not measurable, stop before the substantial credit-bearing run.
3. An approved self-contained D1-BUILD scope/requirements excerpt, with original Master Audit gap disclosed. Original 9p PDF and ZIP still unavailable to local Kiro; they must not be claimed verified there.
4. Product status remains candidate, not final; no rights-sensitive external assets used in BUILD.

**Can be deferred to D1E**: independent human holdout/oracle owner and rights review *of actual external sample*, exact two-run benchmark and 120–240 credit scope. No blind independent validity can be claimed before those are secured.

## D0.3 technical outcome

- **TECHNICAL CORE DESIGN:** FEASIBLE on existing Node24 with proposed TypeScript and local tests.
- **D1-BUILD APPROVAL:** HOLD — needs user authorization, a cost baseline and approved exact scope.
- **D1E COMPARISON:** HOLD — needs independent humans/rights, preregistration and separate credits.
- **PRODUCT GO:** NOT SELECTED / UNPROVEN.
- **NO local user code, Kiro CLI, installation, AWS, GhostWeb/BLINDSPOT, or default branch changed by this memo.**

Official references:
- Kiroween 2026 rules: https://kiroween.devpost.com/rules
- Node status: https://nodejs.org/en/about/previous-releases
- Next.js 16 requirement: https://nextjs.org/docs/app/getting-started/installation
- Canonical JSON JCS: https://www.rfc-editor.org/rfc/rfc8785
