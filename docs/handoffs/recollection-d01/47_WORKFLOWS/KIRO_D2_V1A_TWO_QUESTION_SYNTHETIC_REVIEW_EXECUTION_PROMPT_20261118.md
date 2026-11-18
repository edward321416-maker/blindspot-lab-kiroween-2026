# Kiro handoff — D2-V1A reviewed synthetic two-question exploration

**Authorship date:** 2026-11-18 KST  
**State:** `IMPLEMENTATION_SPEC_PREPARED / USER_APPROVAL_REQUIRED / NO_CODE_EXECUTED`. This public document is a planned Kiro workflow, NOT an implementation or permission to spend more credits. **Execution requires that the user explicitly authorizes D2-V1A local code and new stage credits by submitting the short approval prompt.** The earlier D2-V0 approval does NOT carry forward to this new architecture.

**Read together, using the same SHA-pinned public handoff commit:**  
- `docs/handoffs/recollection-d01/45_ALIGNMENT/D2_V0_REPORTED_PASS_AND_RESEARCH_3_17_GATE_20261118.md`
- `docs/handoffs/recollection-d01/46_PLANS/D2_V1A_SYNTHETIC_QUESTION_REVIEW_AND_CHANGE_DEMO_20261118.md`
- `docs/handoffs/recollection-d01/44_WORKFLOWS/KIRO_EXECUTE_APPROVED_D2_V0_LOOPBACK_SAFE_VIEWER_20261118.md` (existing approved D2-V0 security/integration invariants)
- This file. Sealed original 3.2 holdout, research-private oral answers, rights-restricted media and future 3.17 raw acquisition artifacts are **not inputs to Kiro developer prompts**.

## 0. Objective and proof standard

Build **one concrete, coherent 3–5-minute, offline, local-only Archive Detective experience** using **two fictional owned source records, two fixed Korean questions, explicit demo editorial review, structured visitor evidence choices, and source/rights-change invalidation**.

This is an **end-to-end *demo editorial* product slice**, not an autonomous historically truthful AI museum exhibit. Its purpose is to show an original, traceable source→question→visitor choice→review-invalidated chain that a generic GPT-generated static page alone does not prove. Nevertheless, **do NOT claim an empirical advantage over GPT** until future D1E fair comparison.

The key correctness rule is:
> **Keep B5.2's unreviewed question output blocked. Do not just read raw model-authored question text in the browser or render it under a local “approved” switch.** The *new question display path* must be a separately versioned, trusted fixture-based, digest-bound **DEMO_EDITORIAL_REVIEW** output gate with a demonstrably different provenance from B5.2's unreviewed model text. Only actual typed safe outputs reach the DOM; no real curator approval or publishability is created.

Existing D2-V0 result: **KIRO-USER-REPORTED**, local main HEAD `cadfc12508231881e7755b20850e597b6ca17ede`, parent B5.2 `c02ac7caee1eb163d5ed24b108605c6bb89f5cb0`. Existing 261/261 Node tests (original 239 + 22 D2-V0), 24 D2-V0 cases, 20/20 Edge browser checks, 12/12 mutation challenges. **Do not fake a new independent source audit.**

## 1. Start/stop gates and stack

**Expected workspace:** `C:\Users\admin\Projects\recollection-kiroween-2026`  
**Expected branch/HEAD:** `main` / `cadfc12508231881e7755b20850e597b6ca17ede`; clean, **NO remote**.  
If a later local D2-V1A already exists, do not reconstruct. Read-only inspect, run appropriate verification and report. If any mismatch or user edits exist, **STOP** and report; never reset, stash, rebase, force push or delete.

Main Kiro session **`claude-opus-5.5`, effort `MAX` ONLY**. Do **NOT** use Auto/fallback or spawn subagents—the prior B5.1 review subagent switched to Opus4.8 and was properly recorded as a model-policy violation. Model settings are `SESSION_CONFIG_ONLY` unless independently attested per inference; report observed D2-V1A events without retroactively rewriting model logs. Don't repeatedly request `/model` or `/usage` screenshots.

No new accounts, OAuth, new npm packages, paid service, AWS/Bedrock, internet scraping, source pushing or deployment. Use Node24 built-ins and installed Edge 157 via the existing native CDP browser QA path. Read actual `AGENTS.md`, `.kiro` steering, package manifests **as text without executing them**, inspect function signatures/AST or `rg` first, then only modify target source. Touch **no** GhostWeb dirty `23b8a010` or BLINDSPOT unpushed `c073ddd1`.

The user can approve bounded incremental **D2-V1A stage** Kiro credits by submitting the short prompt; actual promo-pool usage remains `BONUS_USAGE_UNOBSERVED`. Older `Credits: turn/session` are **not** proof of bonus spending. No numeric hard-cap observability is established. Stay within one implementation, two regression runs, one browser QA/fix cycle plus necessary bounded correction. If scope or spending materially expands, stop rather than assuming further approval. D2-V1A approval does not cover D2-V1B, D1E, AWS or public deployment.

## 2. Current APIs and immutable boundary

Before coding, discover actual current local signatures and types for:
- B1 `ExperienceSpec v0.2`, canonical JCS/source snapshots;
- B2 stable `validateText`/`validate` and rights/locator/claim handling;
- B3 `run`, 50-step cap and four primitives;
- B4 `integrate`;
- B5.2 `adaptVisitorOutput`, `VisitorOutputContract v0.1` output shape/status/digests;
- D2-V0 `src/local-viewer`, `tools/local-viewer/server.ts`, HTML/JS/CSS, typed safe renderer, `browser-qa.ts`, native Edge CDP and tests.

**Immutable:** B0–B5.2 original source/test/evidence SHA and frozen oracles, D2-V0 24 preregistered tests and evidence, existing JSON/spec formats, R3.5 `Data:` overblocking behavior, existing output adapter denial. Add new scoped `src/demo-editorial/*`, new tests/manifest/evidence and minimal D2-V0 route/view extension. Do not modify frozen primitives or silently alter B5.2 to make its own unreviewed question case pass. If genuine compatibility requires changes to a frozen source implementation, stop/flag `CONTRACT_CHANGE_REQUIRED` rather than sneaking a patch.

## 3. Freeze tests BEFORE code

First perform **read-only** replay of six existing D2-V0 scenarios and exact B5.2 quote/blocked outputs. Read the 13 actual existing D2-V0 screenshots if present; if they are missing/unreadable, record `VISUAL_BASELINE_NOT_INSPECTED` and take fresh current screenshots before visual modifications, not fabricated visual comparisons.

Then write a separate, immutable **24-case D2-V1A acceptance file** with fixed source fixture SHA, exact expected response status, text/choice/source hashes, visible block counts, and deterministic browser behavior. Store `D2_V1A_CASES_FROZEN_MANIFEST.json` with full SHA-256 **before writing implementation**. Prior manifests must remain byte-identical. Do not secretly rewrite cases after seeing failure; new adversarial tests may be appended in separately named non-frozen files.

Freeze exactly six in each group, with **deterministic** expected results:
- **Q01–Q06, review trust:** Q1/Q2 pending → withheld; two receipts generated from exact trusted synthetic editorial copy → visible, explicitly DEMO; different literal/hash → stale; language mismatch → withheld; model-owned `approved=true` → rejected; unknown question/option → rejected.
- **E01–E06, evidence and choices:** Q1 `PROPOSED` never proves actual service; Q2 linked only to current ARC-02 field; visitor choice event contains enum question/option/source/field digest only; absent source witness → withheld; no `CORRECT/INCORRECT` or historical judgement; a source-status change invalidates old question receipts and selected choices.
- **R01–R06, revocation and lifecycle:** rights revoke → BLOCKED; rights restore → NEEDS_REVIEW until fresh demo review; changed source invalidates both receipts conservatively; true byte-identical no-op leaves digest stable; previous visible questions cleared synchronously before pending operation; delayed stale response cannot repaint the review-blocked screen.
- **U01–U06, real browser/security:** desktop 2Q keyboard flow; 320px and 390px no horizontal overflow; keyboard focus/accessible status semantics for review→blocked; HTML/script and Unicode string injections never execute/render unsafely; Host/Origin/CSRF/dns-rebind/loopback request checks and new endpoints; no external requests/media/cookies/storage/worker.

Do NOT count developer-authored cases as independent blinded human evaluation. A single assertion is not a separate end-to-end case.

## 4. Proposed versioned demo contracts (must reconcile against actual local code)

**`DemoEditorialReceipt v0.1`** (in-memory demo integrity record, not signature/identity):
- `receiptVersion`, `mode: DEMO_SIMULATION`, `questionId`, `exactTextSha256`, `choiceSetSha256`, `sourceSnapshotSha256`, `rightsSnapshotSha256`, `specSha256`, `outputPolicyVersion`, `editorialPolicyVersion`, `language: ko`, `learningGoalDigest`, `dependencyDigest`, `createdForScenario`, `reviewId`, `reviewAction: DEMO_MARK_REVIEWED`.
- SHA/JCS digests bind **actual** bytes of visible Q/choices+rights+source+policy/goal/context. Hash is **integrity**, not human authentication; never call it a digital signature or genuine curator approval.
- The issuer is trusted fixed local fixture-based server functionality only; no client-submitted receipt/secret, `model-approved` field, raw arbitrary question HTML or user-provided `text` enabling free publication. All editor actions and selectable choices come from fixed allowlisted enums.
- Explicit metadata `demoOnly:true`, `humanReviewed:false`, `publishable:false`, `historicalTruthVerified:false`.

**`ReviewedDemoQuestionView v0.1`** (typed additive presentation, not raw model payload):
- Fields: `kind: DEMO_REVIEWED_QUESTION`, `questionId`, `trustedEditorialText`, `options` (enumerated trusted editorial strings, scoped), `sourceRefs`, `receiptDigest`, `demoOnly`, `policyVersion`. Whitelist exact recursive structure; reject unknown property or type. No arbitrary media/image/source URLs.
- Deliver a question only with valid receipt, current source/rights/adapter digest and no unreviewed/free-model strings. The browser must NEVER fall back to `spec.questions`, `run.trace` or raw `suggestedEvidence` when review is missing.
- All original B5.2 `DEMO_PREVIEW | NEEDS_REVIEW | BLOCKED` statuses continue to work unchanged. The new question view is a **separate, explicitly named demo-only overlay** with its own trust gate. Its source quote cards must still come from B5.2 safe outputs; it cannot “approve” the original blocked model-question spec.
- If these guarantees cannot be enforced with additive code, return `D2_V1A_HOLD` with exact incompatible signature; do not weaken B5.2.

## 5. Concrete two-source content and visitor flow

Fictional owned fixture only: `ARC-01` = plan, `proposalStatus: PROPOSED`; `ARC-02` = ledger, `serviceStatus: NOT_RECORDED` initially; rights `DEMO_OWNED`. No actual institution/people/photographs/brands or claims about real history.

**Fixed editorial Q1:** `계획서에서 'PROPOSED'라는 기록만으로 실제 운영이 이루어졌다고 결론지을 수 있나요?`  
**Fixed editorial Q2:** `현재 장부의 상태 항목에 어떤 값이 기록되어 있나요?`

Potential options must be safe fixed strings/data-bound and distinguish `원문에 기록된 값` from `추론` without certifying external truth. The editor's receipt binds **Q1 + Q2 exact text and all options** to this precise fictional source version. Q2 options update only after source mutation and a *new demo editorial review*; do not automatically mark old answer correct/incorrect. For visitor interaction, accept only `questionId`, `choiceId`, `sourceRefId` from allowlists and current receipts; store **transient local session events**, with no persistence/auth/public posting. Visitor may see system-owned acknowledgement `선택한 근거를 기록했습니다`, **never `정답입니다`, `오답입니다`, `역사적으로 사실입니다`, or model-generated narrative feedback**.

**Actual four-screen demo:**
1. **S01 자료 확인** — synthetic-plan and ledger cards, source quote labels, rights and source digest from true B5.2 safe result.
2. **S02 데모 편집 검토** — Q1/Q2 only inside isolated editorial draft screen, fixed data source, exact text+options+evidence/digest, explicit `DEMO_EDITORIAL_REVIEW · 실제 큐레이터 승인 아님`. Until a trusted demo action, **visitor sees zero Q blocks**.
3. **S03 방문자 탐험** — only new typed reviewed-demo question blocks after valid current receipts; each question asks for evidence selection and choice, records structured event and shows source→question trace. No unreviewed model text and no historical correctness verdict.
4. **S04 자료 변경** — alter ARC-02 `NOT_RECORDED→IN_SERVICE` or rights `DEMO_OWNED→REVOKED`; immediately clear old Q/choices and safe quotes as required; invalidate both receipts conservatively, show NEEDS_REVIEW/BLOCKED, require explicit new demo review after restoring rights. Also handle byte-identical no-op without falsely indicating a content change.

**Demo acceptance path:** enter quote-only baseline, open Q drafts, review both in demo mode, visit two Qs and select evidence, mutate status, observe stale/Q0, attempt stale request/replayed receipt (refused), restore rights (still review), review again, see newly bound Q2 content. The demo remains offline localhost and not published.

## 6. Safe HTTP/DOM extension

Preserve D2-V0 Node `node:http` on `127.0.0.1` ephemeral port and strict original routes. Add only minimal exact allowlisted local demo endpoints/actions needed for `DEMO_MARK_REVIEWED` and `VISITOR_SELECT_EVIDENCE`, with fixed JSON enums and capped request bodies. Keep strict Host/Origin/CSRF, no wildcard CORS, restrictive CSP, `Cache-Control:no-store`, local ephemeral in-memory receipts with no cookies/localStorage/worker. Explicitly test replay after mutation, cross-request stale state and session reset. Local process users can access loopback: **not real authentication**.

Browser uses only allowlisted typed block constructors and `textContent`, never `innerHTML`, `eval`, raw B3 trace rendering, user-controlled CSS/URL or network media. Strict deny of arbitrary model-generated question labels. Clear stale DOM synchronously before fetch and ignore late responses with sequence version; test with actual Edge CDP network interception.

Design quality: visual source→question→selected evidence→review-version ribbon, exhibit-like readability, obvious `FICTIONAL SYNTHETIC / DEMO_SIMULATION` badges, clear `review needed` states; do not use color badges as decoration in the app. Inspect previous D2-V0 screenshots and produce current before/after screenshot set with viewport 320, 390 and desktop. Use actual on-PC Edge if available, without new npm packages.

## 7. Tests, threat review, exact evidence and completion report

- **Read-only preflight:** current Node tests and actual D2-V0 UI/screenshots if present. Record original 261 baseline and 24 D2-V0 cases/32 B5.2 cases by manifest SHA. Do not claim 261 was newly run if not.
- **Before code** freeze 24 new cases SHA; deliberately run prereg checks against pre-change source to confirm expected missing feature (record failure as RED), then implement scoped code.
- **After code**, run complete `node --test --test-reporter=tap "tests/**/*.test.ts"` at least twice with observed test counts and exit codes; preserve all historic 261 cases and immutable evidence bytes (compare full SHA). Record normalized result hash separately from raw TAP durations. No falsified `261+24` arithmetic: some cases are browser-only and not additional Node test functions.
- **Actual Edge browser QA:** all six UI-focused cases plus source/rights/refusal scenarios. Measure keyboard, aria/status semantics, responsiveness at 320/390, CSP/no external requests, no stale DOM after source-change and delayed network response. Capture **real** screenshots (no generated replacements) and inspect visually; require zero visible forbidden model text or fake curator approval.
- **Independent adversarial challenge within same permitted main model only:** mutate receipt hash, option text, language, rights, source field, policy version, hidden dependency, delayed response, replay old review, model-provided `approved=true`, forged new HTTP action. Report mutation kill counts honestly; if a test survives, improve guard/test without changing frozen expected cases.
- Node24 built-ins, no new external packages or model subagents. No rights-sensitive media, external URLs, AWS/Bedrock, cloud hosting, actual public release, D1E arms or original 3.2 sealed holdout.
- Provide one **local D2-V1A Git commit only if PASS**, exact full parent and commit SHAs, clean main/no remote, **full unified diff** (UTF-8 LF raw Git bytes, checksum) including new files, exact test command/logs/sha, frozen 24 case manifest, browser screenshot packet, explicit run/shutdown commands and Korean technical/product QA report. Prefer a 3–6-page Korean **PDF visual review report with actual captured screenshots**, if already available local PDF tooling; otherwise report `PDF_NOT_GENERATED` without package install.
- Stage outcome `D2_V1A_PASS` iff actual two Qs and source-linked choice interactions run under truthful demo-only review receipts, all previous security denials preserved, Q/text/rights changes invalidate and clear, all frozen checks green and browser actually verified. If any crucial missing dependency / contract bypass / untested UI → `HOLD/CONDITIONAL` and no false PASS.
- Keep separate residuals: historical claim entailment, real text/asset rights incl paraphrases, independent human reviewer/claim oracle, real curator authentication, full source→feedback closure, real 3.17 raw capture (DNS HOLD), publishing and public contest access, D1E direct-vs-compiler experiment.

**STOP after D2-V1A.** Do not start D2-V1B, 3.17 data collector, D1E experiment, paid AWS or public hosting. Report `BONUS_USAGE_UNOBSERVED` when actual credits cannot be measured. This document is an implementation prompt **prepared only**; explicit user execution approval is a prerequisite.
