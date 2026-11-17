# Kiro — EXECUTE APPROVED D2-V0 local safe viewer (not a publisher)

**Authorization:** Read `43_DECISIONS/D2_V0_USER_APPROVAL_LOCAL_VIEWER_CREDITS_20261118.md`: the user explicitly approved D2-V0 loopback-only viewer and additional credits. This supersedes the `approval pending` label in `39_PLANS/D2_V0_LOCAL_SAFE_VIEWER_REVIEW_GATE_20261118.md` **for D2-V0 only**. **Implement now, no repeated permission questions, STOP after this stage**.

Read source documents **from this exact SHA-pinned GitHub commit** supplied by the user, not from a later mutable branch HEAD:
1. `43_DECISIONS/D2_V0_USER_APPROVAL_LOCAL_VIEWER_CREDITS_20261118.md` (authorization and limits).
2. `39_PLANS/D2_V0_LOCAL_SAFE_VIEWER_REVIEW_GATE_20261118.md` (full design/security and 24-case QA).
3. `38_ALIGNMENT/B5_2_PASS_RESEARCH_3_17_PRODUCT_GAP_20261118.md` (actual reported B5.2 limits).
4. `24_PLANS/RECOLLECTION_3_12_CONCRETE_PRODUCT_INTERACTION_CONTRACT_20261117.md` (four-screen product design; **standalone research UI must not be falsely identified as integrated engine**).

## 0. Model, budget and local workspace

**Use main Kiro session `claude-opus-5.5` effort `MAX` only**; no Auto, fallback or **subagents** (past unpinnable subagent switched to 4.8; historical noncompliance was already corrected in ADR-0006). Never demand repeated `/model` or `/usage` screenshots. Label effort `SESSION_CONFIG_ONLY` if per-turn unobserved and credit `BONUS_USAGE_UNOBSERVED` if promo pool unread. User authorized **additional D2-V0-only credits** (not a measured numeric new hard cap). Keep one bounded implementation and verification pass, limited patch/debug loop; stop if new paid services, account, significant scope growth or apparent credit exhaustion is required. Session-footer credits are **not** bonus-pool used; keep historical 513.26/733.26/813.26 baselines without claiming compliance.

Isolated Windows repository `C:\Users\admin\Projects\recollection-kiroween-2026`, expected local `main`, full HEAD `c02ac7caee1eb163d5ed24b108605c6bb89f5cb0`, clean, no remote. Confirm read-only Git HEAD/status/remotes and existing D2-V0 status. **If D2-V0 already exists on top of this HEAD, do not recreate it; verify actual code/tests and report.** On unexpected dirty tree or incompatible HEAD stop without reset, rebase, stash or overwrite. Do not touch GhostWeb dirty HEAD `23b8a010` or BLINDSPOT unpushed `c073ddd1`.

Read local AGENTS/.kiro/project operating policy. Inspect actual B1, B2, B3, B4, B5.1, B5.2 exports using `rg`/AST signatures before reading modification targets. Parse `package.json`, `requirements.txt`, `docker-compose.yml` as **metadata text**, never execute these declarations. No new npm package/CLI unless user separately approves; reuse Node24 built-ins and already available legitimate browser/QA tooling. Frozen B0–B5.2 source, oracle and evidence **stay unchanged**.

## 1. Pre-register D2-V0 independent developer integration cases before implementation

Create a separate `D2_V0_CASES.json` with EXACTLY **24** enumerated cases, freeze the input/expected behavioral result/fixture SHA256+source revision via a new immutable manifest **before writing viewer code**. Use separate names from frozen B5.2 S/E/R/D 32 cases. 24 developer cases **are not a human blinded oracle**.

Freeze 4 groups of 6 cases, with exact expected state per actual local B5.2 output:

**T01–T06: genuine positive and negative transitions**
- T01: BASELINE_QUOTE → DEMO_PREVIEW, **exactly** 11 visible blocks **if actual B5.2 gives 11**.
- T02: WITH_UNREVIEWED_QUESTIONS → NEEDS_REVIEW, **zero** visible blocks, six pending sink paths if actual B5.2 reports six.
- T03: DIRECT_FIELD_CHANGE → BLOCKED, no stale text.
- T04: UNREFERENCED_FIELD_CHANGE → NEEDS_REVIEW, no stale text.
- T05: REVOKE_RIGHTS → BLOCKED, no quote/media left.
- T06: RESTORE_RIGHTS → NEEDS_REVIEW, **no auto approval**.

**S01–S06: trust/HTTP/renderer safety**
- S01: injected `approved` or forged B5.2 status from HTTP request → HTTP error and no bypass.
- S02: arbitrary nested output kind / unsafe visible field rejected by renderer and never inserted.
- S03: HTML/JS payload encoded as text cannot execute, no `innerHTML`/inline handlers.
- S04: URLs, images and external media/protocol injection not rendered or dereferenced.
- S05: wrong Host, Origin, external/LAN/DNS-rebinding and CSRF-style request refused; loopback-only socket.
- S06: unknown scenario ID, extra JSON fields, oversized/malformed input and incorrect content type rejected.

**L01–L06: state consistency and process lifecycle**
- L01: slow earlier response cannot repaint after newer BLOCKED/NEEDS_REVIEW (out-of-order test).
- L02: DOM immediately clears previously visible blocks **before** initiating a blocked/review update.
- L03: `Cache-Control: no-store`, no persistence/service worker/localStorage approval.
- L04: tampered digest/version/right-snapshot mismatch fails closed.
- L05: live synthetic scenario performs actual immutable B1→B5.2 validation on source/rights mutation.
- L06: clean local process shutdown and no unexpected open socket, filesystem writes or hidden persistence.

**U01–U06: actual browser and accessibility evidence**
- U01: 320px viewport no horizontal overflow and readable state.
- U02: 390px viewport no horizontal overflow.
- U03: desktop responsive four-screen navigation and correct content.
- U04: keyboard-only controls and visible focus, no inaccessible hidden primary action.
- U05: aria-live status announcement for BLOCKED/NEEDS_REVIEW, inspect semantics; report actual measured checks, not a blanket WCAG certification.
- U06: no JS runtime exceptions, no third-party network resources; inspect actual browser resource requests.

If a browser QA runner is absent and low-risk native browser automation is unavailable **without installing extra packages**, perform HTTP/test and manual browser QA that is actually possible, but report `D2_V0_CONDITIONAL / UI_NOT_TESTED` for any unsupported browser test. **Never fake screenshots, DOM interactions or 24/24 results.**

## 2. Implementation — strict local loopback server, same-origin safe DOM

**Prefer** `node:http` Node24 built-in loopback server with `listen(0,"127.0.0.1")` and log the **actual** randomly assigned local port. Never bind `0.0.0.0` or `::` or expose a public tunnel.

Routes:
- `GET /`: bundled safe static HTML shell, with no dynamic model content;
- `GET /assets/<exact allowlisted asset>`: serve only fixed bundled JS/CSS, correct MIME, no path traversal;
- `GET /healthz`: no secrets, minimal local health status;
- `POST /api/preview`: only JSON `{"scenarioId":"BASELINE_QUOTE" | "WITH_UNREVIEWED_QUESTIONS" | "DIRECT_FIELD_CHANGE" | "UNREFERENCED_FIELD_CHANGE" | "REVOKE_RIGHTS" | "RESTORE_RIGHTS"}`, no other keys. Bound body length and content type, reject any raw spec/snapshot/script/rights/approve/publish input.

Use exact Host value `127.0.0.1:<actualPort>`, Origin equal to self for POST, explicit deny of missing/unexpected Origin unless a tightly constrained trusted local test client is documented, and CSRF token/custom JSON header. Reject DNS rebinding, origin confusion and wildcard CORS. Never send `Access-Control-Allow-Origin: *`.

Response is computed using **actual** local `validateText()/validate()`, `run()`, `integrate()` and `adaptVisitorOutput()` on trusted synthetic scenario fixtures only. No fabricated B5.2 decisions or hard-coded output as substitute. Reconcile exact signatures with local source. Safely handle and report BLOCKED/NEEDS_REVIEW (do not echo unreviewed model strings). Server output may include non-visitor-visible typed status/issue code and content digest, but avoid exposing debug source text except already B5.2-allowlisted safe blocks.

Guard response content digest, output schema/kind/allowlist, source/rights binding and version. Never promote model-owned approval/publication flags; no `APPROVED` button or auth simulation that looks real. `demoSimulation:true`, `publishable:false`, `historicalTruthVerified:false` must remain true/false as specified.

Browser client uses **only** `document.createElement`, `textContent`, strictly controlled `setAttribute` for static safe values and fixed component type map. Do NOT use `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `eval`, `Function`, dynamic import of model fields, unsanitized CSS, media URL renderers or raw B3 model spec/trace. Use a default-deny CSP with same-origin JS/CSS, no inline handlers, no external fonts/images. Test the actual served CSP header and no unexpected browser requests.

On scenario selection (including pending blocked case), **clear all previous quote/preview blocks synchronously**, show neutral loading UI, ignore older responses via AbortController/sequence monotonic counter. If result is BLOCKED/NEEDS_REVIEW, render only trusted local static state description + safe non-text issue codes; **zero** B5.2 blocks. Rights revoked means nothing prior is left on screen. Do not misrepresent `SOURCE_QUOTE_PRESENT` as historical validation.

## 3. UI design — actual integrated output, four screens

- S01 **Source Intake:** only two fictional owned records ARC-01 PLAN (PROPOSED) and ARC-02 LEDGER (NOT_RECORDED), source hashes/rights *from trusted fixture*, no third-party museum asset uploads.
- S02 **Curator Review Queue:** show blocked/needs-review counts and allowlisted issue codes; no actual curator identity, no review approval grant. Clearly mark `DEMO_SIMULATION`.
- S03 **Visitor Preview:** shows actual 11 system+source quote blocks only if `DEMO_PREVIEW` returned; quote label in Korean “원문 인용 존재 · 주장 참 여부는 미검증”, and truthful `publishable:false`. Two proposed Qs remain **not displayed** because unreviewed. No correctness/feedback.
- S04 **Evidence Change:** six enumerated controlled scenarios; visible before/after digest and trust-state timeline, not real source captures. On restored rights, review remains required.
- Styling: ivory/charcoal neutral gallery-console, clear evidence chain and state labels, mobile widths 320/390, desktop contrast/focus/aria-live tested. Use only system-owned Korean UI copy; no automatic translation of source claims. Preserve actual previous known P2 `Data:...` overblocking rather than bypassing validator.

## 4. Acceptance, evidence, and scope exit

**Existing tests:** previously user-reported full suite **239/239** (not independently verified here); run actual complete `node --test --test-reporter=tap "tests/**/*.test.ts"` twice **after implementation**, record command/exit/digest and count; preserve all old 239 cases, B0 frozen oracle and B5.2 frozen 32-case manifest untouched. New 24 cases and browser checks counted distinctly, no double-counting 32 earlier cases as new.

**D2-V0 PASS** requires:
- server from actual pinned local code returns six correct observed B5.2 results, and browser genuinely receives/renders them correctly;
- all 24 preregistered checks matching expected results, including **real browser** checks for U01–U06, and strict Host/Origin, stale DOM clearing, CSRF/security, no third-party fetches;
- both full Node test runs pass, deterministic semantic digest and frozen evidence unchanged;
- no unsafe modeled HTML/JS, unreviewed question, actual historical truth claim, media, reviewer approval, publisher, AWS/network access or public binding;
- clear process shutdown, one scoped **local D2-V0** commit if PASS, full SHA/unified diff including new files, clean main/no remote.

If browser automation absent, record `UI_NOT_TESTED` and `D2_V0_CONDITIONAL`, not PASS. If no existing tool for promised PDF/screenshot, provide exact accessible local HTML and evidence/test records with explicit `NOT_GENERATED` reason; do not install a new account/paid package or fake output.

Deliver a concise Korean report: local parent/new commit, changed files, frozen 24-case SHA, T/S/L/U per-case status, six scenario browser screenshots only if actually generated, screen reader/keyboard and 320/390 QA, two full test suite runs counts/exits and digest, no network/rights leakage, model/credit observability, P0/P1/P2 residual risks, browser start/stop command and localhost address (valid only while running). Local report PDF if easy with already available authorized tooling; no source or screenshot fabricated.

User-approved **extra credits cover D2-V0 only**, not a new D2-V1 feature, research 3.17 collector, actual museum ingestion, human rights/claim verification, D1E experiment, public repository, hosting, cloud, login or publishing. No independent human oracle, sealed holdout or real licensed media imported. Protected GhostWeb/BLINDSPOT remain untouched. Kiro local TSV may be `PENDING_SYNC` until separately verified Sheets connector write.

**STOP after D2-V0.** Report actual result, no automatic D2-V1/D1E/deploy. Focus on a faithful visible integration of already validated B5.2, not another long series of architecture proposals.
