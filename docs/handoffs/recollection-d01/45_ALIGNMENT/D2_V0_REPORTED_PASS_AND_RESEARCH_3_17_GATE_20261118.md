# Re:Collection — D2-V0 technical completion checkpoint and research alignment

**Date:** 2026-11-18 KST
**Classification:** `D2_V0_TECHNICAL_PASS = KIRO_LOCAL_USER_REPORTED`, not independently executed/inspected by the GitHub docs author.
**Evidence input:** complete user-pasted 163-line D2-V0 completion report (no original local Windows source, full diff, binary screenshots, or local test logs attached).
**Next stage:** none newly authorized. D2-V1, D1E, real data and public release remain `HOLD`.

## 1. Local development facts as reported

- Local Re:Collection branch `main`, HEAD `cadfc12508231881e7755b20850e597b6ca17ede` on B5.2 parent `c02ac7caee1eb163d5ed24b108605c6bb89f5cb0`; clean, no remote, not pushed.
- Unified diff local `ReCollection_D1_BUILD_reports\D2_V0_cadfc12.diff`: 159,072 bytes / 2,891 lines / full SHA-256 `c5d5c89b7b30d0cb1d717c1f9220092c00d080f6afacf8b65083666d9b8e6e22` **reported, not read here**.
- 21 changed files, 18 new, +2,753/-1. New isolated `src/local-viewer/` actual chain `validateText→run→integrate→adaptVisitorOutput`, built-in `node:http` loopback server, native Edge DevTools browser QA, four-screen viewer using `textContent`, 24-case separate test suite, ADR-0008, README/tasks and evidence.
- Original B0–B5.2 source, test, oracle and evidence files reportedly diff 0 and 16 regenerated evidence files byte-identical. GhostWeb dirty and BLINDSPOT unpushed states preserved.

### Test accounting — avoid double counting

| Test group | Kiro reported result | Meaning |
|---|---|---|
| Existing original Node tests | **239/239** preserved | B0–B5.2 regression |
| New D2-V0 Node tests | **22/22** | Total Node tests **261/261** |
| All Node suite | **261/261** ×2 plus postcommit, exit 0 | Normalized semantic hash prefix `c72cd132`; raw TAP timing differs |
| D2-V0 predeclared cases | **24/24** (T01–T06, S01–S06, L01–L06, U01–U06) | Some cases have Node+browser evidence; browser-only UX cases are NOT extra Node test counts |
| Edge 157 browser QA | **20/20** after CSS adjustment | Browser CDP in installed headless Edge; no new npm package |
| Mutation probes | Initially 11/12, then **12/12** after L01 delayed-response regression | Independent human review NOT IMPLIED |
| Screenshots | 13 images reported in local `D2_V0_SCREENSHOTS\` | **Images not delivered here**, visual inspection by GitHub author NOT PERFORMED |
| PDF | `NOT_GENERATED` by Kiro | Scope choice; not evidence of UI defect |

**Browser QA detail (reported):** 320px and 390px no overflow; desktop 4-screen navigation; keyboard Tab 11 presses reached 10 controls, Enter triggered a BLOCKED scenario; focus ring 3px, `role=status`/`aria-live=polite` inspected via accessibility tree; no JS exception/CSP violation/external request; state transitions 11 safe quote blocks ↔ zero blocks. Accessibility-tree evidence is NOT equivalent to actual screen-reader speech testing or comprehensive WCAG conformance.

## 2. Security and trust evidence

- `127.0.0.1` loopback on ephemeral port, no LAN binding. Same-origin 5 paths only as observed; wrong Host → HTTP 421; Origin/CSRF → HTTP 403; preflight → 405; malformed input → 400/413/415/404.
- Only actual B5.2 allowlisted blocks displayed, with `SOURCE_QUOTE_PRESENT` explicitly **not** historical truth. Unreviewed two-question experience → `NEEDS_REVIEW`, 0 visible blocks; server did not transmit those question strings.
- `REVOKE_RIGHTS` removed prior ARC-02 quote/text/media; rights restoration remained `NEEDS_REVIEW`. Late earlier responses did not repaint after a later blocked state; synchronous clearing before fetch.
- CSP/self-origin, no injected HTML execution, no cookie/localStorage/worker approval or publisher state **as tested**.
- **Remaining local-only threat:** other programs/processes on the same Windows machine could access loopback and inspect a reachable token. Synthetic read-only data and lack of external side effects minimize impact but do NOT establish user authentication.
- Browser's internal network traffic suppressed by launch flags but **not exhaustively measured**, as Kiro reports. No claim every network packet in Edge was independently audited.
- `TYPECHECK_NOT_RUN`. Model B5.1 subagent drift historically documented; D2-V0-specific Kiro log 40 observed Opus5.5 events, no subagents, effort `SESSION_CONFIG_ONLY`. `BONUS_USAGE_UNOBSERVED`, current bonus pool/cap compliance unknown.

### Trace provenance issue — actually verified for four docs

Kiro said it fetched its four handoff documents from branch SHA `afd9b979aaf0760c2710deedc518f57d41ad7857` rather than the original pinned handoff SHA `45358556d7b1c75cf8f59deae0739f6533531dfc`. In **GitHub MCP independent comparison**, the Git blob SHAs for all four relevant `43_DECISIONS`, `39_PLANS`, `38_ALIGNMENT` and `24_PLANS` were **exactly equal at both commits**. Thus content drift is **not demonstrated**; still use immutable pinning in subsequent Kiro instructions. Do not infer that Windows local source/test was independently audited by this GitHub check.

## 3. Newest research 3.17 and product dependency

Research-only GitHub file `43_RESEARCH/RECOLLECTION_3_17_COLLECTOR_PATCH_EXECUTED_DNS_HOLD_20261118.md` documents actual data-lab code hardening, **32/32 mock/offline unit tests** and a first attempt to fetch `MET-36491` that failed with DNS (`URLError -3`). All **8/8 original provider raw HTTP captures absent**; other seven target requests not attempted after first gate; 0 independently adjudicated historical claims and **0/24 rights slots** approved. The corrected collector in an isolated container is NOT part of the Windows D2-V0 local viewer, and its tests are NOT product acceptance.

Research 3.12 standalone browser HTML prototype previously had 17/17 QA; it included simulated human approval and two answered Qs, but that was **not** a valid integration of Kiro compiler review authority. D2-V0 uses true B5.2 restricted outputs, so refusal of unreviewed questions is **correct**, not a failed implementation or a product readiness claim.

## 4. What D2-V0 technically proved vs did NOT prove

**Proved within Kiro-reported tests:** real B1/B2/B3/B4/B5.2-to-browser path for owned synthetic quote-only preview; deny-by-default for unsupported output, safe DOM, rights/source change blocking, stale response safety, bounded local HTTP, responsive 320/390 UI smoke.

**Unproven:** a complete *two-question interactive visitor journey*, answer scoring/feedback, semantically entailing factual claims, paraphrase rights provenance, source→question→choice→feedback dependency closure, real verified curator review, real provider raw snapshots/media rights, independent blinded human oracle, production browser security, generalized real-world adaptability, direct-code vs compiler superiority, public contest judges' access.

**Product reading:** D2-V0 is a secure *technical demonstration of review-and-invalidation visibility*, NOT an end-user museum learning app. The user's earlier key criterion that a GPT-generated generic app is not sufficient therefore still requires an evidence-carrying interactive investigation and a measurable advantage.

## 5. Proposed next gate, NOT authorized by this report

**D2-V1A — synthetic editorial review receipt / two-question exploration** (separate scoped product-architecture decision):
- Reuse existing viewer + B5.2 as immutable source. Introduce a separate typed **demo-only** editorial record binding explicit human/editor-supplied *fictional* question copy, source field/claim IDs, exact visible bytes, content SHA, policy version and language. No automatic historical entailment or authenticity claim.
- Simulated local review is explicitly `DEMO_EDITORIAL_REVIEW`, **not real curator authentication or PUBLISHED**. The existing adapter cannot simply be bypassed by writing question text directly in DOM; any approved future additive content path must be cryptographically/context-bound with its own security tests.
- Show two coherent questions only after their demo-stage reviewed exact copy is allowed; visitor-selected answers can be collected as demo events, **do not produce purported historical correctness feedback** until an independently reviewed evidence-completeness contract exists.
- Source mutation/rights revoke invalidates question receipts and clears screen; conservative whole-experience review remains if indirect dependencies not closed.
- Independent UI visual QA needs the 13 actual screenshots (not currently available to ChatGPT), or a verified separate screenshot packet/pinned review artifact. Prevent endless refinement without a recognizable complete lesson.
- Estimate D2-V1A credit and any new auth/hosting choices separately. **The prior D2-V0 credit approval does not carry over.** A future D2-V1A implementation must be explicitly approved by user.

**Parallel research:** The 3.17 collector is patched but blocked by DNS; raw acquisition can proceed only in a separately approved network-capable isolated data lab, with actual institutional terms/licensing and later independent reviewers. Never import private research master/holdout/media into the product repo.

## 6. Status and next checkpoint

- `D2_V0_TECHNICAL_PASS = USER_REPORTED`.
- `D2_V1A = PLAN_ONLY / NOT_AUTHORIZED`.
- `RESEARCH_RAW_HTTP = 0/8, DNS_HOLD`.
- `VISITOR_2Q_COMPLETE = NO`.
- `D1E_EXECUTION = HOLD`; `REAL_MEDIA/PUBLISH/CLOUD = HOLD`.
- No new Kiro code/commit is created in this GitHub docs operation. One next decision is whether to approve bounded D2-V1A demo editorial contract + stage credits, without fake authenticated curator or public release.
