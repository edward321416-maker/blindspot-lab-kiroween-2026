# Re:Collection — B5.2 typed output adapter: implementation-ready gated contract

**Date:** 2026-11-18 KST  
**Status:** `IMPLEMENTATION_READY_DESIGN / USER_APPROVAL_PENDING`. No local Windows source code was changed in producing this GitHub document. **DO NOT EXECUTE unless the user explicitly authorizes B5.2 local code changes and understands unobserved credits.** Read `34_ALIGNMENT/B5_1_ERRATUM_COMPLETE_B5_2_IMPLEMENTATION_DECISION_20261118.md`, `32_PLANS/B5_2_VISITOR_OUTPUT_POLICY_AND_RENDERER_CONTRACT_PROPOSAL_20261118.md`, and frozen local Kiro API exports before implementation.

## 1. Bounded decision sought from user

Proposed choice:
- Architecture: **standalone, versioned `VisitorOutputContract v0.1` adapter**, separate from existing B1 `ExperienceSpec v0.2`, B2 semantic validator, B3 runtime and B5.1 snapshot security patch.
- First demonstrator: **offline `DEMO_SIMULATION`** with **two owned synthetic source records** and two educational questions, no authentic curator identity, no `approved`/published authority.
- Initial implementation stage: **data-only adapter** that returns typed safe preview or `NEEDS_REVIEW/BLOCKED`, not actual browser UI. A separate subsequent safe renderer/browser stage needs another explicit authorization.
- System: existing Node24/test runner, **zero new npm packages**, no AWS/cloud, no network fetch, no external third-party assets, no GitHub remote/push, no human holdout leakage.
- Model: **main Kiro session Opus 5.5/MAX only, NO SUBAGENTS**, no Auto/fallback. Never claim past 4.8 subagent noncompliance is erased. No repeated `/model` or `/usage` screenshot requests.
- Budget: `BONUS_USAGE_UNOBSERVED`, original startup counter 513.26, prior cumulative soft 733.26 and hard 813.26 **cannot currently be independently enforced**. Initial B5.2 adapter work roughly **+40–70 credits planning estimate**, not a guaranteed maximum or metered allowance. A separately accepted spending risk or measurable cap is required before starting code; **do not treat this document as new credit authorization**.
- Release: `productPublicationAllowed=false` always; `historicallyVerified=false` always absent actual independent human review. `DEMO_SIMULATION` never equals `HUMAN_APPROVED`.

## 2. Required existing API and fixed invariants

The Kiro executor must discover exact function signatures from actual local source using `rg`/AST rather than assuming the proposed DTO is already implemented:
- Local main current expected `52e230dfa96601e310b3210ae4af81e701eb74ad` (ADR docs-only correction). Worktree clean, no remote.
- B5.1 had `validate()`/`validateText()` stable detached snapshot, B3 `run(...)`, B4 `integrate(...)` report. Read the actual normalized values, error codes, hash fields, limits, safe-string kinds and snapshots to adapt *without modifying their semantics*.
- Frozen B0–B4 oracle, 164 original tests and B5.1 30 added tests stay intact. Last measured reported suite **194/194** on B5.1; the subsequent ADR correction made docs-only changes and tests were `NOT_RUN_DOCS_ONLY`. Do not fabricate a newer run.
- Preserve source/human rights distinction, `R3.5 UNSAFE_TEXT` as is, source registry and all existing contract semantics. Do not auto-migrate to 3–8 objects.
- Stage requires **pre-registered contract test matrix frozen in source control or checksum-listed before implementation**. Public/shared cases are development regression, not a blind independent oracle.

## 3. Proposed boundary and typed result

```text
Trusted owned synthetic source snapshot + exact registry/rights digest
  + existing v0.2 candidate spec
  + existing B2 validation result revalidated/bound to exact normalized input
  + existing B3 run trace/structured payload
        ↓
[ B5.2 trust-boundary adapter ]
  - exact recursively-allowed visible field kinds and shapes
  - safe source quote + locator + source hash (presence NOT entailment)
  - human-reviewed text receipt ONLY if actual authenticated review exists later
  - simulated review receipt / source-owned text with demo marker
  - rights for each emitted source field, excerpt, asset, medium
  - digest over actual visible text bytes, language, kind, source, quote,
    source/rights snapshot hashes, policy version, audience and content context
  - changes/revocations fail-closed; no incomplete dependency claim
        ↓
{ kind: "DEMO_PREVIEW" | "NEEDS_REVIEW" | "BLOCKED",
  policyVersion: "visitor-output-0.1",
  demoSimulation: true,
  publishable: false,
  historicalTruthVerified: false,
  blocks: TypedSafeViewBlock[],
  issues: {code,path,severity,sourceId?,claimId?}[],
  sourceDigest: String,
  outputDigest: String }
```

The above fields are **a proposed design sketch**, not existing runtime signatures or a new authoritative JSON schema; finalize with actual B1/B2/B3 inputs and immutable tests. Do not allow model-authored fields `approval`, `publishable`, `verified`, `renderOverride`, arbitrary HTML/JS, unknown output kinds, dynamic execution or URL media. Fail closed, not silent-drop unknown properties.

The first adapter **does not issue human review tokens or public URLs**, and must never present a demo flag as a real authenticator. If no trusted review available and a model-authored string would otherwise be visitor-visible, return `NEEDS_REVIEW` or `BLOCKED` rather than rendering its text. Allow inert system-authored neutral instructional labels and separately known trusted source quotes labeled `SOURCE_QUOTE_PRESENT` only; no `Recorded fact`, no auto `CORRECT`/feedback. Source quote is only evidence of string presence and may be irrelevant to a claim.

## 4. First synthetic 2-source user story

Research 3.12 reference design **only**, authored fictional synthetic owned data:
- PLAN `ARC-01` with `proposalStatus=PROPOSED`.
- LEDGER `ARC-02` with `serviceStatus=NOT_RECORDED`.
- The model must not create a new historical truth claim that the line actually opened based only on `PROPOSED`.
- Two proposed investigative questions remain `NEEDS_REVIEW` until their *exact visible text* and evidence mapping are trusted/reviewed for demo. No automatic feedback/correctness key.
- Changing the ledger status `NOT_RECORDED→IN_SERVICE` must invalidate the source/related digest. Because indirect dependency closure isn't proven, **default conservative whole-experience `NEEDS_REVIEW/BLOCKED`**, not a claim that only Q2/F2 requires review. Research 3.12's selective Q2 preview was a standalone simulated simplification, not source-engine proof.
- Rights `DEMO_OWNED→REVOKED` must immediately block any related source text/media; restoring rights returns `NEEDS_REVIEW`, never automatically `DEMO_APPROVED` or `PUBLISHED`.
- Reuse no real artworks, 3.14 museum media or sealed 3.2 evaluation cases. Demo labels prominently state `FICTIONAL SYNTHETIC / NOT HISTORICAL FACT`.

## 5. Preregistered public developer-safe test plan — 32 cases, not blinded

Before code, freeze exact input/expected status, source fixture/provenance and SHA for every case. The following are **proposed** case IDs/expected policies and must be reconciled against actual existing error codes (do not silently change B0 oracle):

### S: output sink and authority (S01–S08)
- S01 Unreviewed AI-generated title → NEEDS_REVIEW / no visible title.
- S02 Inert system-owned navigation copy → DEMO_PREVIEW allowed, no fact assertion.
- S03 Added unreviewed `compare-cards` label → BLOCKED.
- S04 Unreviewed proposed `questions[].text` → NEEDS_REVIEW.
- S05 Fabricated answer/feedback embedded in title → BLOCKED.
- S06 Unknown nested output kind or root metadata used for visible text → BLOCKED.
- S07 `curator_approved` or `published` internal state ID displayed as status → BLOCKED.
- S08 User-generated escaped markup and control chars in would-be visible string → BLOCKED.

### E: source, quote, entailment and epistemic label (E01–E08)
- E01 F3-12 irrelevant 1-character quote → no factual `Recorded fact`, NEEDS_REVIEW.
- E02 Quote whitespace only / unrelated locator → BLOCKED or NEEDS_REVIEW, no auto truth.
- E03 Explicitly contradictory sentence paired with valid source locator → NEEDS_REVIEW; no automatic truth or certainty.
- E04 Exact owned source quote displayed as quote only, precise source label `SOURCE_QUOTE_PRESENT` → DEMO_PREVIEW.
- E05 Educational model missing assumptions/review → NEEDS_REVIEW.
- E06 Old source/claim or hash mismatch → BLOCKED.
- E07 Unsupported cross-source inference/UNKNOWN promoted to asserted fact → BLOCKED.
- E08 Model confidence/hash equality trying to set `historicalTruthVerified=true` → BLOCKED.

### R: field-level rights and revocation (R01–R08)
- R01 Rights-restricted source text copied into `UNKNOWN`/question title → BLOCKED (default-deny unreviewed text, not unsupported plagiarism oracle).
- R02 Media/source rights absent or contradictory → BLOCKED.
- R03 Synthetic source-owned, rights-evidenced quote displayed with no image URL → DEMO_PREVIEW.
- R04 Source item image public domain but text description license separate/unknown → BLOCKED for text until specific proof.
- R05 Asset rights `DEMO_OWNED→REVOKED` → BLOCKED.
- R06 Rights restored after withdrawal → NEEDS_REVIEW, no auto restore.
- R07 Model-supplied external URL, encoded protocol, media reference bypass → BLOCKED.
- R08 Stale review or policy/context/source digest → BLOCKED.

### D: dependency, benign and demo (D01–D08)
- D01 Ledger field mutation with unknown complete dependency graph → whole-experience NEEDS_REVIEW/BLOCKED.
- D02 Unexecuted branch with unresolved source dependencies → NEEDS_REVIEW.
- D03 Unknown alternate OR evidence witness / missing indirect claim→feedback edge → NEEDS_REVIEW.
- D04 Simulated approval field/user-supplied `approval=true` → BLOCKED as authority.
- D05 `Data: ...` normal text entering old B2 `UNSAFE_TEXT` → existing rejection **documented P2 overblocking**, never bypass current R3.5.
- D06 Reviewed-elsewhere language translation used without matching per-language digest → NEEDS_REVIEW.
- D07 Plain trusted bounded punctuation/neutral source quote → DEMO_PREVIEW where existing validator permits.
- D08 Two owned fictional records and two sample questions → only `DEMO_SIMULATION`, `publishable=false`; never imply real curator approval.

**Acceptance:** all 32 frozen planned cases match actual expected status, B0–B5.1 baseline 194 tests remains green, new negative+benign tests demonstrate both false allow and false block rate, two deterministic runs, exact output digest version, no side effects or unknown output sink, no public media. Independent human blind evaluation is **NOT** achieved by these public test cases. If security gaps remain, return `HOLD/FAIL` rather than weakening expected outcomes or hiding cases.

## 6. Execution and reporting after explicit approval only

1. Main Kiro Opus 5.5/MAX only; do not spawn unpinnable subagents. Read local `AGENTS.md`, applicable `.kiro` and package manifests as text. Use `rg`/AST for function signatures. Preserve user worktree before modifying.
2. Freeze inputs/expected cases **before** implementation. Keep test holdout separate from these exposed cases; no independent human oracle is currently assigned.
3. Implement only bounded `src/output-policy/*` or another locally fitting adapter module, its own tests, versioned evidence/report, architecture ADR. No change to B0–B5.1 source unless a scoped compatibility fault is demonstrated and separately approved.
4. No new third-party packages, renderer/browser/UI/auth/publisher/AWS/Bedrock/media downloads; tests against synthetic-owned sources only. Never reuse a mocked `APPROVED` state as actual approval.
5. Run full Node24 test suite twice with deterministic normalized logs, guard old 194 tests and frozen evidence SHA, new output-policy cases exact, capture test counts and exits. One local bounded B5.2 commit if accepted; full SHA/unified diff.
6. Mark `B5_2_ADAPTER_PASS / HOLD / FAIL` with residual risks; product/real-data/real publisher and D1E execution continue HOLD. Main-only model provenance, `TYPECHECK_NOT_RUN` and `BONUS_USAGE_UNOBSERVED` as appropriate.
7. STOP. Any browser-view stage, real approval, output truth, 3–8 count, public media or paid service requires a **new explicit approval**.

**This file is not the approval; a short user message stating approved B5.2 adapter scope and spending risk is required before Kiro source modifications.**
