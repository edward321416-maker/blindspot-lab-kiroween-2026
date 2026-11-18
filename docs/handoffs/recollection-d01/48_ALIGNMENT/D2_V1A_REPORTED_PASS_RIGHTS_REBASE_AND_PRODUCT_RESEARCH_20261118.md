# Re:Collection — D2-V1A completion checkpoint, output sink and rights-rebase audit

**2026-11-18 KST · public docs-only branch · evidence class: USER/KIRO LOCAL REPORTED.** The attached 2026-11-18 D2-V1A run report is pasted user text, not direct access to the unpushed Windows Git repository, byte diff, actual screenshots or PDF. **No independent local-code review was performed in authoring this file.**

## Technical checkpoint; do not reconstruct D2-V1A

- Local Windows repo `C:\Users\admin\Projects\recollection-kiroween-2026`, `main`, reported clean, remote NONE.
- D2-V0 parent: `cadfc12508231881e7755b20850e597b6ca17ede`.
- **D2-V1A SHA:** `ca941c5748c0c20a11144fd4f1a83da9e85c7a00`.
- Reported local diff `ReCollection_D1_BUILD_reports\D2_V1A_ca941c5.diff`, 184,196 bytes, 2,873 LF lines, SHA-256 `26de29f47d368bd9b8e94e321800e33790e40ad90fe1c2920c367852cf309839`; NOT independently opened. 22 files (18 new), +2662/-9; B0–B5.2 and D2-V0 source/tests/fixtures/evidence reportedly unchanged except an explicit `tools/local-viewer/server.ts` route extension +44/-7.
- New `src/demo-editorial/` `DemoEditorialReceipt v0.1` + `ReviewedDemoQuestionView v0.1`; **B5.2's original unreviewed model-authored 2-question input still yields NEEDS_REVIEW/0 visible blocks**, and is reportedly not sent to browser.
- Newly visible Q1 and Q2 come from trusted **fictional static editorial copy** in `viewer/demo-editorial.json`, with receipt binding visible question/option bytes, source/evidence quote hashes, snapshot/right/spec/B5.2 digest, language/policy/learning-goal. `demoOnly:true`, `humanReviewed:false`, `publishable:false`, `historicalTruthVerified:false`.
- User choices produce source/option/receipt ID-and-digest events with **neutral selection acknowledgement only**, no factual correctness score, answer key authority or original-model prose.
- Rights/source changes reportedly invalidate **both** review receipts and recorded choices, rights restoration requires new DEMO review, byte-identical reapplication retains digest. Loopback Host/Origin/CSRF/no-store/CSP guards inherited and extended to `GET /demo` and `POST /api/demo`.

### Test accounting

| Evidence | Kiro-reported observation | Truth boundary |
|---|---|---|
| Preimplementation RED | 280 total Node tests, 263 pass, 17 new fail | Honest missing feature baseline |
| Frozen D2-V1A developer cases | Q01–Q06 E01–E06 R01–R06 U01–U06 = **24/24 PASS** | Developer-authored, NOT blinded/independent human |
| Frozen manifest | `D2_V1A_CASES_FROZEN_MANIFEST.json` SHA256 `6bde7d2af825870e99df03e7d1434d8a1e1b35384b729ab006ee313b9d75cdea` | Full bytes not independently verified here |
| Node | **291/291 PASS twice + postcommit**, exit 0, normalized digest prefix `44762f4f` | Prior **261/261** regression prefix `c72cd132`, **239/239** prefix `6acf4fa7`, reproduced as claimed |
| Browser | First QA **16/17** (rights leak), second QA **17/17** after fixing static button label | Edge 157 headless real browser reported; not equal to independent visual approval |
| Responsiveness/accessibility | 32 combinations at 320/390 without horizontal overflow, keyboard-only complete, role=status aria-live=polite, CURRENT/STALE/BLOCKED status | Measured subset only; NOT comprehensive WCAG or human screen reader |
| Mutation | **15/16 killed** after additive tests; survivor reported `equivalent` redundant revocation check | Equivalence needs control-flow/source proof, not counted as all killed |
| Evidence regeneration | 18 historical files byte-equivalent in temporary copy | Local report only, original raw bytes not accessible here |
| Captures | 15 screenshots and four-page screenshot-derived PDF (SHA256 `4045cd8128997bf660c3caa1215aae3b95bfa4b58efc012305ae7e6281b6a37b`) | Local Windows only; screenshots/PDF NOT independently opened here |

**No new unreported source execution** performed by this docs author. `TYPECHECK_NOT_RUN`; `BONUS_USAGE_UNOBSERVED`; main-session 33 reported Opus5.5 events, effort `SESSION_CONFIG_ONLY` and no subagents. The original B5.1 mixed-model subagent violation remains separately documented; protected GhostWeb/BLINDSPOT unchanged.

## High-priority design-audit questions exposed by implementation

### A. Re-basing B5.2's source/rights history when a demo is reviewed

User's implementation report explicitly states that after source mutation a DEMO review **re-prepares B5.2 inputs**, re-binds cited claim, sets baseline to the *new* source snapshot, and **starts rights history fresh**; ADR-0009 describes this. This seems necessary to enable a new demo after real changes, but is also an **epistemic/audit trust-boundary question**.

- **Confirmed by report:** the original B5.2 implementation itself was unchanged; new review revalidation is performed; after revoke, old receipts invalidate; after restore, a fresh demo review is required.
- **NOT yet independently established:** whether an untrusted caller, stale tab or manipulated rights history can use the “fresh baseline” path to erase evidence of a prior revoke or silently redefine previously reviewed material as new approved material.
- **Required next audit:** read actual `src/demo-editorial/*`, ADR-0009, `src/local-viewer/api.ts` and server route. Prove current rights status, immutable historical rights event chain and review scope are distinct; a receipt can only be issued against a *new verified snapshot*, not caller-provided `approved`, self-asserted restored rights, or old post-revoke quote. If history reset is demo-only, explicitly label limitations and preserve a *monotonic audit digest* for changed/revoked states; prevent any production copy of such reset semantics.
- Test controlled transitions: VALID→REVOKED→RESTORED→new review; REVOKED→attempt review without restoration; edit claimed source ID/snapshot then mint; non-reference field mutation; two concurrent tabs; old receipt replay and delayed HTTP response; fake rights restoration; historical revocation before browser reload. Expected deny/no stale output until trusted new review; **no claim that a local static fixture proves real-rights restoration**.

### B. UI static-string rights/claim leakage

A genuine browser QA failure reported `R01`: a *static button label* contained `NOT_RECORDED` **while rights were revoked**, even though B5.2 and typed question body denied it. The label was fixed and browser suite reached 17/17.

**Root lesson:** strict `textContent` avoids HTML injection but does NOT prove right-to-display. Every presentation sink (button text/value, aria-label, title, option, hidden accessible text, status, metadata, URL param, tooltip, toast, cached DOM, error state, screenshot and announcement) requires provenance and a current rights/claim gate; no model-origin or revoked source field should be duplicated as unconstrained static copy. Review code + browser accessibility tree and dynamic response after revoke in all four screens, across multiple tabs; don't over-generalize a 17-case test to all sinks.

### C. Shared state across tabs and equivalent mutant

The D2-V1A report flags **in-memory demo state shared among all browser tabs** (P2). This is acceptable only as a labeled single-operator local demonstration; not a real role/session boundary. One tab's review may impact another tab's viewer and vice versa. Next test must explicitly cover two tabs and races or keep a product-visible single-session restriction. Do not treat a loopback CSRF token as a real user identity.

The surviving mutation (removing a reportedly redundant revocation check) is a **proof obligation**, not a proof of quality. Document why another invariant always rejects the input; if not, add an attack that kills it without editing frozen test expectations.

### D. Product completeness and empirical differentiation

- **New**: for fictional records, source→reviewed-demo-question→visitor choice→receipt invalidation operates in a real browser. This is a substantive improvement over D2-V0 quote-only preview.
- **Still NOT**: automatic source-to-question generation that generalizes to new materials, independent factual entailment, independently authenticated curator approval, claims→choice→answer/feedback dependency closure, verified media rights or any empirical win over “just ask GPT”.
- The only two questions were **fixed editorial templates in `viewer/demo-editorial.json`**. A hardcoded two-question demo alone does not demonstrate a reusable AI-powered Authoring system or 3–5 minute product value in unfamiliar domains.
- Suggested independent next product gate: use multiple **fresh synthetic source combinations** from a separate case author without copying research 3.2 sealed holdout, freeze evaluator examples/criteria, prove adapting to changed source fields while preserving strict review/deny semantics. Avoid “more screenshots, more P0 checks” as the sole next deliverable.

## Research updated through 2026-11-18

**Important newer evidence than the 3.17 DNS HOLD plan:** GitHub `44_RESEARCH/MET_A_INDEPENDENT_2OF2_RAW_HASH_AND_COLLECTOR_MARKER_PATCH_20261118.md` has a reviewed user-submitted private Met A raw evidence ZIP; exact `response.bin` for Met object IDs 36491 and 45434 (2/2 pack A) passed an *independent offline payload-integrity* verifier (34/34), each payload SHA and object ID checked. However the reviewer **did not independently witness the live HTTPS origin**; submitted sanitized `capture.json` omits `Set-Cookie` headers; actual media/text/publication rights remain HOLD. This is a **research improvement**, not a product source ingestion or independent factual oracle.

Separate `45_PLANS/MET_A_COMMITTED_MARKER_HARDENING_CODEX_STAGE_GATE_20261118.md` records an actual collector `COMMITTED` verifier fail-open: a marker prefix alone, wrong ID or wrong hash could be accepted. A minimal isolated replay patch was independently tested **37/37**, but **the user's Windows isolated collector patch was NOT applied at that snapshot**; not Kiro engine code.

Accordingly, old statements “RAW 0/8 globally” are **outdated for the two A-pack files**. Correct progress at this checkpoint is **Met A submitted raw files 2/2 payload integrity PASS; independent network provenance unconfirmed; broader eight-target project only 2/8 submitted, other six not confirmed captured; public licensing and human truth review 0 accepted**. Do not copy private archive raw media, internal headers or sealed research holdout into public code or the Kiro development repo.

## Current milestone / next decision

- `D2_V1A_TECHNICAL_PASS = KIRO_LOCAL_REPORTED`.
- `D2_V1A_SOURCE_REVIEW / VISUAL_INDEPENDENT = NOT_DONE`.
- `DEMO_ONLY / NOT_HUMAN_REVIEWED / NOT_PUBLISHED`.
- `RIGHTS_BASELINE_RESET_AUDIT = OPEN`; `ALL_UI_SINKS_AUDIT = OPEN`; `MULTITAB_ISOLATION = DEMO_LIMIT`.
- `D2_V1B_GENERALIZATION = PLANNING_ONLY` after boundary review; `D1E_EXECUTION / PROD / REAL_MEDIA = HOLD`.
- No fresh Kiro stage or extra credits authorized solely by the pasted completion report. Prior D2-V1A allowance does not extend automatically to V1B.
