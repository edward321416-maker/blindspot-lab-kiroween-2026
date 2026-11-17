# Re:Collection — D2-V0 local safe viewer bridging actual B5.2 data (proposal / approval needed)

**Date:** 2026-11-18 KST  
**Status:** `DESIGN_READY / USER_ARCHITECTURE_APPROVAL_PENDING / NO_CODE_EXECUTION`. This proposed stage sits **outside** the previously authorized B5.2 adapter-only scope. User's extra credit approval for B5.2 cannot be assumed to cover D2-V0 or paid hosting.

Read `38_ALIGNMENT/B5_2_PASS_RESEARCH_3_17_PRODUCT_GAP_20261118.md` first. Start only after the user explicitly approves **local offline/loopback viewer architecture, the security boundary, and additional stage credit risk**. No Kiro instructions in this file constitute that approval by themselves.

## 1. Product/engineering rationale: actual integrated preview, not fake two-question success

B5.2 local result is **USER_REPORTED PASS** at `c02ac7caee1eb163d5ed24b108605c6bb89f5cb0`, with 239/239 tests in two runs, 32/32 frozen developer cases, 20/20 reported mutation guards and a real B1/B2/B3 → B5.2 data bridge. This is synthetic-only, no browser. For the owned `ARC-01` plan and `ARC-02` ledger demo, quote-only returns **`DEMO_PREVIEW` with 11 safe data blocks**; adding two unreviewed questions returns `NEEDS_REVIEW` with **zero visitor blocks**. Source changes and rights revocation must block or require review. A browser viewer that ignores these states would invalidate the whole reason for the B5.2 adapter.

The **D2-V0 primary deliverable** is a local judge-facing **preview/review visualization of real B5.2 outputs**, not an authenticated museum publication tool, autonomous question+feedback experience, or contest-ready deployment. It should make the safe/blocked distinction visible and valuable to a curator. The first controlled experience remains **two fictional owned synthetic sources** and **no verified historical truth**.

## 2. Architecture option selected for review (not implemented)

**Preferred:** Node24 **built-in** `node:http` local-only service bound to `127.0.0.1` with randomly assigned free local port; same-origin browser resources; server executes actual pinned local B1/B2/B3/B4/B5.2 integration on **trusted allowlisted synthetic fixture actions only**; browser renders **only the B5.2 typed safe output contract**.

```
Browser [S01–S04, only local simulated data]
   → same-origin POST /api/preview {scenarioId: ENUM}
   → trusted locally embedded owned synthetic scenarios
   → B1 contract → B2 stable source/right validator → B3 bounded run
   → B4 integration evidence → B5.2 output adapter
   → { kind: DEMO_PREVIEW|NEEDS_REVIEW|BLOCKED,
       visible blocks only if DEMO_PREVIEW, issues and digest,
       demoSimulation:true, publishable:false }
   → safe renderer (DOM textContent / allowlisted element types)
```

**No** remote model, untrusted free-form source, open HTTP proxy, dynamic HTML, uploaded image, museum artifact, cloud host, auth, localStorage-based approval, API-key secret, localhost listener open to LAN, or public URL. Browser UI itself is **new client code** and may manipulate DOM through trusted JS, but it never interprets model-authored JS/HTML. Runtime data engine still executes no arbitrary JS.

HTTP security contract:
- Bind loopback **only**, default not `0.0.0.0`; check strict `Host` and `Origin` on every state-changing/preview request; send no wildcard CORS headers; reject external origin / DNS rebinding / user-supplied URLs.
- Only allowlisted `GET /`, `GET /assets/{exact bundled file}`, `GET /healthz` and `POST /api/preview`. No filesystem path traversal, third-party HTTP fetching, API credentials or directory listing.
- Only `application/json` with request body cap and an exact `scenarioId` enum; reject unknown fields, free-form spec/snapshot/script, excessive/bidi/control strings. Never allow caller to set rights, publisher status, verified flags or version digest.
- Use browser same-origin anti-CSRF constraints and a fresh per-session unguessable token or equally strong explicit same-origin request guard with Host+Origin+custom JSON header; no side effects, no persistent approval store. No secret leakage or new account.
- Set `Cache-Control: no-store` for data; on any `BLOCKED/NEEDS_REVIEW` transition, immediately clear **previous safe blocks** in DOM before new fetch, never show stale quote, even if old async responses arrive late; use sequence IDs/AbortController to prevent out-of-order stale response.
- CSP: default-deny with `script-src 'self'`, `style-src 'self'`, `connect-src 'self'`, `object-src 'none'`, `base-uri 'none'`, `frame-ancestors 'none'`; no third-party scripts, images, fonts, inline event handlers, `innerHTML` or `eval`.
- Strict no public socket, public IP/hostname or product URL; tests verify remote LAN clients cannot access. Keep process lifecycle controlled with an explicit CLI shutdown instruction.

**Alternative:** static offline HTML generated from precomputed B5.2 output JSON (no HTTP server) is safer operationally but **does not demonstrate live B1→B5.2 revalidation on user-changed source states**. Unless the user selects static-only, prefer the restricted loopback service above. This architectural choice is why user approval is needed.

## 3. Grounded four-screen layout with honest state labels

**S01 Source Intake — fixture viewer, not real data ingest:** show two clearly labeled `FICTIONAL SYNTHETIC` cards, rights state and digest from trusted fixture manifest, not raw source uploads. Source quote cards render only when B5.2 `DEMO_PREVIEW` permits; no misleading historical status.

**S02 Curator Builder / Review Queue — simulator, no real curator auth:** show B5.2 issue `code/path`, pending question count and their visibility status. If the adapter returned zero blocks, never directly read raw model-authored spec text to fill the missing UI. No `Approve` button that grants authority. May show an inert `Requires review` banner and `DEMO_SIMULATION` label.

**S03 Visitor Preview — viewer of allowed data only:** on `DEMO_PREVIEW`, render B5.2's 11 typed neutral-copy/quote/compare blocks using `document.createElement` and `textContent`, with `SOURCE_QUOTE_PRESENT` clearly translated “원문 인용 존재 · 주장 참 여부는 미검증”. If `NEEDS_REVIEW` or `BLOCKED`, **zero old visible blocks**, only neutral local-state message and why; no question/answer/correctness/feedback.

**S04 Evidence Change & Rights Revocation — deterministic simulation:** buttons choose only built-in scenarios `BASELINE_QUOTE`, `WITH_UNREVIEWED_QUESTIONS`, `DIRECT_FIELD_CHANGE`, `UNREFERENCED_FIELD_CHANGE`, `REVOKE_RIGHTS`, `RESTORE_RIGHTS`. Responses must match actual B5.2 status with new snapshot hash; rights restore stays NEEDS_REVIEW, no automatic republish. Show before/after snapshot/hash **as technical evidence**, not as approval.

UI feel: museum-educator investigation console, neutral ivory/charcoal, clear source cards, a right-hand evidence/rights timeline on desktop; mobile vertical stack at 390 and 320 px. System controlled language can be Korean with static English glossary; translating original content/claims without review is forbidden. Don't put real institution marks or copyrighted images into prototype. Keyboard nav, WCAG contrast and screen-reader status announce via controlled static copy.

## 4. Proposed initial acceptance plan (not yet frozen or executed)

Before implementation, freeze a distinct `D2_V0_CASES.json` expected matrix and immutable hash **from actual B5.2 outputs**, then create tests. Do not mutate the 32 B5.2 frozen cases, original 239 test suite, or research 3.2 held-out oracle.

Suggested 24 controlled cases across:
- **6 positive/transition**: baseline 11 blocks, unreviewed questions 0 blocks, direct source edit block, unrelated edit needs review, rights withdrawal block, restore needs review.
- **6 trust/security**: forged B5.2 status/approved, unsafe visible sink or unknown kind, HTML/XSS payload text escaped/nonrendered, URL/media injection, external Host/Origin/CSRF, malformed scenario ID/free-form JSON rejected.
- **6 stale/lifecycle**: out-of-order response, previous DOM block removal on transition, cache-control no-store, tampered digest refused, script/rights mutation under live server, memory/process shutdown and no hidden persistence.
- **6 UI/accessibility**: 320/390/mobile no horizontal overflow, browser JS errors 0, accessible button labels/keyboard, status announces, contrast and high-zoom layout, no restricted media/network resources.
Record exact fixture/snapshot and B5.2 SHA before UI code. Do not claim independent/blind evaluation: same model authoring and developer cases. Mark browser tests `NOT_TESTED` if Chromium/Playwright/browser automation not available; do not install a new package without explicit user approval.

**D2-V0 technical PASS** only if actual B5.2 code, not mimicked JSON, supplies every displayed block and status, all 239 previous tests still pass twice, state transitions/stale DOM clear, 24 newly preregistered cases pass with real browser checks for browser claims, CSS/keyboard/layout checks, exact security rejection, no public listener/rights leak. If no browser test environment, **D2-V0 CONDITIONAL / UI NOT TESTED**, never manufacture screenshots or claim accessible judge-ready UI.

## 5. Deliverables after separately approved implementation

- New, isolated `src/local-viewer` / `tools/local-viewer` server and `viewer` client, exact actual local code exports observed first; keep B0–B5.2 source and frozen tests unchanged, adapt only narrowly if proven necessary with new approval.
- Safe synthetic fixture-only scenario controller; `node tools/local-viewer...` CLI startup and safe shutdown; no new npm packages.
- B5.2 output digest shown, approval/publish false and fictional label visible; six scenario screenshots (if browser tool available) including 320px and 390px; PDF review sheet **if already authorized tools available** without new external account or paid service.
- Two complete `node --test` runs, exact counts/exits/deterministic evidence, separate browser tests recorded; source audit for network calls/unsafe DOM, no actual museum source assets, no hidden 3.2 holdout.
- One local `D2-V0` commit only if stage pass, full SHA, diff and before/after tree hash; clean main/no remote; preserve GhostWeb/BLINDSPOT; correct TSV PENDING_SYNC if Sheets connector not available locally.
- Korean completion report with actual browser preview link limited to localhost, explicit `NOT_PUBLISHED`; do not claim public link judge can open. If user later wants public contest demo, that requires different security/IP/hosting approval and separate source/rights acceptance.

## 6. Out of scope / still HOLD

- Real authenticated curator approval; human reviewed factual answers, verified historical entailment, rights-cleared museum media, external live APIs and raw source collector 3.17; no automatic publication, cloud/AWS, public GitHub source or OSI license selection.
- No new `HISTORICAL_FACT` facts from 1-character citation, no answer correctness, no generated feedback or adaptive branch, no crossing sealed research holdout into implementation.
- No actual D1E direct-Opus vs compiler evaluation yet; C2 safe renderer is necessary but not sufficient for the product-quality comparison until meaningful two-question experience and independent review exist.
- New model/credit budget must be authorized for this stage. Prior B5.2 approval to use +40–70 estimated extra credits was **B5.2-only**; actual usage after original 513.26 baseline remains `BONUS_USAGE_UNOBSERVED`. Rough D2-V0 design/implementation may need additional credits; no guarantee or silent credit charge.

**Decision to request:** Approve or reject **local loopback-only D2-V0 browser viewer** with described CSRF/Host/Origin and safe DOM constraints, strictly synthetic two-source stage and separate incremental Kiro-credit risk. If rejected, continue independent data quality research and D1E planning only. No question about details that are already chosen above.
