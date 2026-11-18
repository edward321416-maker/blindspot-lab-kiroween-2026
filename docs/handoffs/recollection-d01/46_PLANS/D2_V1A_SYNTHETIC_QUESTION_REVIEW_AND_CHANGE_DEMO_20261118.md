# Re:Collection D2-V1A — reviewed synthetic question journey (product planning, NOT implementation authorization)

**Research/product alignment:** Research 3.11–3.12 first ARCHIVE DETECTIVE vertical slice = two fictional source records, two linked questions and source/rights change. D2-V0 now provides a **Kiro-reported** real local B5.2-to-browser *quote-only* preview (261/261 Node tests + 20/20 Edge QA). This design intentionally addresses the **single most consequential product gap**: two questions remain `NEEDS_REVIEW` and **zero** blocks are visible when questions exist. D1E and public launch remain HOLD until complete judged visitor experience and independent evaluation.

**State:** `DESIGN_PROPOSED / USER_APPROVAL_PENDING` for local Windows implementation and incremental Kiro credits. No local code, product review authority, new npm package, cloud resource or D1E execution is authorized by this document alone.

## 1. Desired experience and exact boundaries

The goal is a **real clickable 3–5 minute educational investigation** for owned fictional data, not an arbitrary prompt→HTML application and not a false claim of curator-reviewed real history.

Actor | Before | At D2-V1A proposal | Scientific/rights authority
---|---|---|---
Museum/editor demo operator | B5.2 blocks two unreviewed Qs | Author two exact fictional questions and inspect a version-scoped **DEMO_EDITORIAL_REVIEW** decision | NOT authenticated human museum curator, NOT external rights grant
Visitor in local demo | 11 quote cards only | Study 2 synthetic records, read two explicitly *demo-approved* questions, select source evidence and answer options | Demo choices only; not factual correctness certification
Evidence source change | New digest blocks old quotes | Change ARC-02 status/rights; previously reviewed question receipts become STALE and visitor view clears | No claim of selective dependency closure or production CDN invalidation
Product evaluator | Cannot see a complete lesson | Can test full source→question→choice→re-review interaction on fictional data, then compare against direct-code prototype | Independent blind oracle / real data still absent

**Two precise questions, system/editor-owned DEMO content** (not free model copy):
- Q1: `계획서에서 'PROPOSED'라는 기록만으로 실제 운영이 이루어졌다고 결론지을 수 있나요?` A neutral multiple choice can distinguish **what document states** vs **what has not been observed**, but cannot automatically issue an independently verified historical judgement.
- Q2: `현재 장부의 상태 항목에 어떤 값이 기록되어 있나요?` Options bound to actual fictional ARC-02 `serviceStatus` field. After the ledger changes from `NOT_RECORDED` to `IN_SERVICE`, **all old question receipts stale** until re-reviewed. Do not hardcode old source value as a current trusted fact.
- Do **not** add auto `CORRECT`/historical certainty, real publication, licensed media or real curator approval. A visitor's selection is an event with a source link; safe feedback may say `선택한 근거를 기록했습니다` (system-owned generic text) rather than judging right/wrong. A future genuinely independent claim oracle would be needed for explicit factual answer validation.

## 2. Contract boundary: do NOT bypass B5.2

Retain `ExperienceSpec v0.2`, B0–B5.2 source/fixtures/oracles and D2-V0 safe renderer as existing versioned contracts.

**Proposed additive version `DemoEditorialReceipt v0.1` and display gate `ReviewedDemoQuestionView v0.1`, not a replacement authority for B5.2:**

- `reviewId, receiptVersion, mode=DEMO_SIMULATION, sourceSnapshotSha256, rightsSnapshotSha256, specSha256, outputPolicyVersion, questionId, exactTextSha256, allowedChoiceSha256, language=ko, dependencyDigest, expiresOnMutation=true, editorAction=DEMO_MARK_REVIEWED`.
- **Never** accept model-owned `approved/publishable/historicallyVerified`, arbitrary HTML/JS, or detached raw copied question/answer text. The literal fictional content originates from a trusted fixture/editor entry, not a model's unreviewed spec field. A receipt does NOT establish human identity: display `DEMO_EDITORIAL_REVIEW • 실제 박물관 승인 아님`.
- The trust boundary should be **inside a new separately versioned review adaptor** that validates currently produced B2/B3/B5.2 hashes and an allowlisted trusted fixture/editor draft; the browser may only receive typed safe review-approved-demo question blocks. **Do NOT have browser directly read B3 raw spec questions** or render them because the URL says `approved`.
- External or user-supplied text that is identical to demo template is not automatically trusted; bind source identity, byte digest, language, version and event context. R3.5 unsafe string rules remain unchanged (known `Data:` overblock).
- The actual local editor UI lacks authenticated museum identity, so **`editorAction` is a synthetic self-asserted demo state**. It must never set the real `APPROVED/PUBLISHED` fields, issue external public tokens, or appear as actual independent verification.

**Safe receipt policy choices to freeze before implementation:**
1. Conservative: a change to any relevant source/rights/policy or an unproven dependency field **invalidates the entire 2-question review** (no claim that Q1 is unaffected if Q2 source changes). Distinguish dependency status `UNKNOWN` from intentionally unchanged.
2. Explicit rights revocation → immediately withhold all affected quote, question, option and last-visited state; restoration requires fresh demo review, not auto approval.
3. A new question or option wording, different language, changed teaching goal or differing content SHA → stale review. A no-op exact byte-identical update can remain valid only if full trusted source/rights digest is unchanged.
4. Two questions displayed in local demo only while BOTH evidence/text receipts are current, and B5.2's raw unreviewed generated question output must remain blocked. If the B5.2 contract cannot be extended additively without breaking existing safety, mark D2-V1A `HOLD`, don't spoof new status.
5. No silent persistent session auth; receipts synthetic and ephemeral in trusted local memory/test fixture, no public publication or third-party access. Loopback attack protections remain active.

## 3. Product flow and meaningful demonstration

**Four scenes (retain D2-V0 layout):**
- S01 `자료 확인`: fictional plan vs ledger, exact source quote presence, date/field labels from synthetic fixture; two records visible with rights.
- S02 `질문 검토`: two proposed questions in a **reviewer-only demo draft panel**, explicit copy/field digest and `DEMO_EDITORIAL_REVIEW` action; before demo mark both pending, visitor view stays blocked.
- S03 `방문자 탐험`: after exact *demo review*, read source cards and Q1/Q2, choose an evidence card/option; current choices become structured data without automatic historical judgement. A system-owned completion badge may say `두 질문을 탐험했습니다`, not `역사적 사실 검증 완료`.
- S04 `자료 변경 실험`: click `ARC-02.status = IN_SERVICE`, or rights `REVOKED`, or no-op. UI clears previous questions/choices synchronously; show source→question dependency **review required**, not false incremental closure. Restored media remains reviewed-again needed.
- Make the novel value visually obvious: a **source-to-question trace ribbon**, exact cited field and hashed review state, before/after invalidation and no silent reuse of stale answers. Render only genuinely allowed typed objects.

**Success demo sequence:** BASELINE quote preview → Q1/Q2 drafts `NEEDS_REVIEW` → explicit demo-only editorial review → two questions visible + evidence-linked visitor selections → change source/rights → pending/blocked and zero stale questions → explicit new demo review on new fixture → safe current copy. No real museum personnel, paid cloud, public sharing or answer correctness claim.

## 4. Pre-registration / engineering acceptance (draft until approval)

**Proposed 24 separate new D2-V1A developer cases** (public, not blind), to be frozen by SHA before code:
- **Q01–Q06 text+receipt:** two pending Qs cannot display; demo reviewed exact copy can display; wrong text hash blocked; wrong language blocked; model-approved flag blocked; unknown question/option kind blocked.
- **E01–E06 evidence binding:** Q1 source “PROPOSED” cannot entail operating line; Q2 source field linked; visitor choice points to selected source; missing claim/evidence results NEEDS_REVIEW; no auto correctness; receipt changes under source mutation.
- **R01–R06 rights+review lifecycle:** rights revoke blocks; restoring rights requires new review; snapshot change blocks; no-op trusted identical revision controlled; previously rendered questions cleared during transition; old delayed response cannot restore stale view.
- **U01–U06 UI/safety:** actual installed Edge browser Q1/Q2 navigation, 320/390 no overflow, focus/aria-live, HTML/script injection no execution, Host/Origin/CSRF boundaries maintained, no third-party network or media request.

**Acceptance:** previous **261/261** Node tests remain passing twice (baseline reported, not independently re-executed); frozen B5.2 S/E/R/D 32 and D2-V0 T/S/L/U 24 remain untouched; 24 new developer cases and real-browser checks pass; not just mock data; trace/evidence hash ties to actual run; no unreviewed strings or stale blocked text, no model-created approval, no claim of actual rights or external historical accuracy, no new dependency. Prefer one scoped local commit with full diff and screenshots/QA packet. Browser unavailable = `CONDITIONAL`, never fake QA.

**Non-goals:** authentic curator accounts, signing identity, production rights registry, public app, actual historical claim entailment, full claim→feedback OR witness closure, real museum snapshots/media or D1E quality comparison. None becomes true because a demo-only review receipt exists.

## 5. Research gates and budget

- Research 3.17 hardened independent collector passed 32/32 offline/mocked checks, then MET-36491 actual HTTPS request failed DNS; **RAW 0/8**, real public rights **0/24**, independent claim reviewers **0**. No mixing research collector with Windows product.
- The 13 D2-V0 screenshots were **generated locally but not delivered to this assistant**. Before claiming visual refinements, inspect those actual screenshots or obtain a reproducible screenshot packet; no invented browser screenshots.
- Additional D2-V1A credit requirement is **not approved**: historical B5.2 and D2-V0 bonuses remain `BONUS_USAGE_UNOBSERVED`. A new single-stage credit authorization is needed; no indefinite spending/paid third-party services.
- Model `claude-opus-5.5` MAX in main Kiro session only, no subagents/Auto/fallback, no repeated /model/usage screenshot requests. Report actual observed events, never erase B5.1 mixed-model history.

**Decision to request from user after plan review:** Approve bounded **D2-V1A synthetic editorial receipt / two-question demo** plus its incremental Kiro credit exposure, keeping true curator identity and public publication HOLD. If the user instead prioritizes real data, separately authorize 3.17 isolated Windows research collector network attempt—without modifying D2-V0 or importing sealed holdout.
