# Re:Collection D2-V0 — user approval, local-viewer architectural boundary and credits

**Date:** 2026-11-18 KST  
**Status:** `D2_V0_LOCAL_VIEWER_APPROVED` — **ONE bounded local development stage ONLY**. User consent from current conversation: after being asked “D2-V0 로컬 브라우저 시연 개발과 필요한 추가 크레딧 사용까지 승인하고 진행할까?”, user replied **“승인할게”**. The user's approval includes local-only loopback viewer architecture, safety and same-origin controls, synthetic two-record scope, new-stage Kiro credits. It does **not** include external paid services, public publishing, real-source IP rights, or unbounded further stages.

## Binding technical constraints

- Execute from Kiro user's isolated `C:\Users\admin\Projects\recollection-kiroween-2026`, expected current local main `c02ac7caee1eb163d5ed24b108605c6bb89f5cb0` (B5.2 PASS user-reported, clean/no remote). Do not repeat B0–B5.2, redo frozen 32 cases, or reset/rebase/stash.
- Deliver **D2-V0 local safe browser preview** directly calling actual B1→B2→B3→B4→B5.2 existing APIs for owned synthetic scenarios; **never** copy handcrafted safe-looking JSON as a substitute for output adapter.
- Architecture: Node24 built-in `node:http` bound **only** to `127.0.0.1` ephemeral port, same-origin static assets, strict Host/Origin/CSRF guards and capped allowlisted `POST /api/preview` scenario enum. DOM renderer uses allowlisted elements and `textContent`, no model-owned HTML/JS. Keep service entirely local and shut down cleanly.
- Exactly two fictional owned synthetic records ARC-01/ARC-02, statuses `DEMO_PREVIEW | NEEDS_REVIEW | BLOCKED`, six fixed scenario transitions. Baseline may show 11 safe blocks **only if actual B5.2 returns these**; unreviewed two-question case shows **zero** blocks. Clear stale visible blocks immediately on non-preview state, handle out-of-order responses and rights revocation.
- Four review/preview screens aligned to Research 3.12 (source intake, review queue, visitor preview, evidence change), with **no live human curator, authorization, actual approval, verified historical truth, correctness/feedback or public publisher**. Model-generated titles/questions not visible without real review. Prototype shows `FICTIONAL SYNTHETIC / DEMO_SIMULATION`.
- 24 predeclared **developer** integration/security/browser/UX acceptance cases, separate from B5.2 frozen cases. Freeze exact inputs, expected status and SHA **before code** and count cases independently. Browser QA required for UI PASS. Keep all 239 previous tests green twice and frozen evidence unchanged.
- Node24 native facilities and existing locally available browser tools; **zero new npm dependencies** and no network download/installation without separately justified approval. If the browser harness is unavailable, mark `UI_NOT_TESTED / D2_V0_CONDITIONAL`, never fabricate a screenshot or call it PASS.
- Kiro **main session claude-opus-5.5 / MAX ONLY**; NO subagents (B5.1 subagent used 4.8 in the past), no fallback/Auto. Historical correction remains intact. No repeated `/model` or `/usage` screenshot requests.
- User authorizes **additional stage credits**, without an exact metered cap. Record `BONUS_USAGE_UNOBSERVED` until actual bonus-pool reading exists; don't conflate Kiro session footer with pool, reset baseline 513.26 or claim original 733.26/813.26 caps were observed. Bound to a single D2-V0 implementation + tests, limited troubleshooting, stop if new paid/cloud account, materially expanded costs or stage scope are needed. No subscription upgrades or billable AWS.
- The extra-credit permission is **only D2-V0**. It does not authorize later D2-V1, real reviewer sign-in, output approval token service, museum rights, open internet binding, public URL, cloud, GitHub push, D1E C0/C1/C2 arms or deployment.
- Preserve protected GhostWeb dirty HEAD `23b8a010` and BLINDSPOT unpushed `c073ddd1`; no changes in those repos. Research 3.2 sealed holdout/oracle and research 3.14–3.17 private datasets never enter local developer source/public GitHub.
- Before implementation inspect local project policy and actual exports with `rg`/AST, read manifests as text, preserve current user edits, no destructive commands.

## Evidence and release truth

- B5.2 PASS user-reported local `239/239` twice plus postcommit; **NOT** independent source review here.
- Research 3.12's standalone 17/17 browser prototype is **NOT** the user-local Kiro engine, and research 3.17 has **zero original HTTP raw captures, zero public media-rights approvals, zero independent human claim adjudications**. These limitations remain.
- `D2_V0_TECHNICAL_PASS` may be issued only after actual browser+security checks against local B5.2 output; does not mean independent truth, full question/answer experience, accessibility compliance outside measured checks, or public judge-ready link.
- No actual D2-V0 code/QA is claimed by this GitHub decision. It simply records authorization to execute the next pinned handoff and move from design to implementation.

**Decision supersedes** the `USER_ARCHITECTURE_APPROVAL_PENDING` state in `39_PLANS/D2_V0_LOCAL_SAFE_VIEWER_REVIEW_GATE_20261118.md` for this restricted D2-V0 stage only. Other HOLD requirements remain.
