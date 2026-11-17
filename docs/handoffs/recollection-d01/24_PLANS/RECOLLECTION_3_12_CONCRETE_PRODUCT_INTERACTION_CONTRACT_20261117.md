# Re:Collection 3.12 — Concrete Archive Detective interaction and trust contract

**As of:** 2026-11-17 KST. **Classification:** PRODUCT DESIGN / OFFLINE SYNTHETIC CLICKABLE PROTOTYPE ONLY. No new Kiro product implementation or external publication is authorized by this document.

## One complete first experience

**Actor:** curator + museum visitor. **Input:** 2 owned synthetic records. **Outcome:** 2 linked questions and change-aware review state.

- `ARC-01` — synthetic 1952 R1 PLAN. `proposalStatus = PROPOSED`, locator `ARC-01#field.proposalStatus`.
- `ARC-02` — synthetic 1956 R1 LEDGER. `serviceStatus = NOT_RECORDED`, locator `ARC-02#field.serviceStatus`. Proposed mutation `NOT_RECORDED → IN_SERVICE`.
- `ARC-02.mediaRights = DEMO_OWNED → REVOKED` used to simulate stopping image/display. This does **not** prove actual publisher/cache enforcement.
- All documents, route, dates and values are **fictional synthetic samples**, never historical claims or verified collection assets.

**Q1:** Does a proposed plan prove the line actually opened? Expected `NO`, distinguish plans from independent execution evidence. `ARC-01.proposalStatus → CL-01 → Q1/F1`.

**Q2:** What does the 1956 status ledger actually say? Expected `NOT_RECORDED`, or `IN_SERVICE` after synthetic change. `ARC-02.serviceStatus → CL-02 → Q2/F2`.

Quote location existing in source ≠ claim relevance/entailment ≠ historical truth. Preserve B4 F3-12 review as a P0 gap.

## Four exact screens + transitions

| Screen | Input / action | Output / validation |
|---|---|---|
| S01 Source Intake | Two sources and rights/locators; press Continue | Source cards with field paths, rights, title, goal; invalid rights/locator must not be passed as verified |
| S02 Curator Builder | Generate fixed synthetic experience; inspect claim links; simulate review | Two ClaimRefs, Q1/Q2, feedback references, approval only of exact current source/text/policy version |
| S03 Visitor Investigation | Read records, answer Q1 then Q2 | Evidence-linked feedback, uncertainty. Unapproved/stale/rights-revoked revision must not be served |
| S04 Evidence Change | `ARC-02.serviceStatus: NOT_RECORDED→IN_SERVICE` | Direct dependency graph marks Q2/F2 for review; Q1/F1 stable in simplified graph; visitor blocks until reapproved |
| S04 Rights | revoke ARC-02 image; restore later | `BLOCKED` and image hidden; restore results in `STALE_REVIEW`, **never** automatically republished |

Product-state proposal: `DRAFT→NEEDS_REVIEW→APPROVED→PUBLISHED`, plus `STALE_REVIEW/BLOCKED` on changes. Actual HTML **only simulates APPROVED as local state**. No server, curator auth, persistent digest, publication URL, rights proof or production CDN. Real model generation NOT invoked.

## Proposed product-only DTO/API (NOT a modification to frozen B1 v0.2)

DTO: trusted source snapshots, `sourceId/fieldRefs/locator/rights`, `learningGoal`, immutable scope and review status. Propose separate adapter endpoints `POST /drafts`, `GET /:id/review`, `POST /:id/approvals`, `POST /:id/change-preview`, `GET /:id/visitor`, `POST /:id/events`. These paths are conceptual, not observed running API signatures; first inspect existing B1/B2/B3 actual exports in local Kiro workspace. Use SHA-256/JCS versioned review digest in production, not the prototype's noncryptographic `SYNTHETIC vN`.

### Version and security boundary

- Keep all B0–B4 frozen oracle, typed v0.2, integer-only JCS, B2 trust and B3 four primitives/50 steps unchanged. No arbitrary output HTML/JS, SSRF fetching or model-owned `approved/published`.
- The existing source/claim matching does not prove independent historical truth. Historical certainty requires appropriate human judgment and separate evidence checks.
- OAP-0.1 was only a 3.9 Python research comparator; don't call it shipped. Add to future independently versioned D2 validation after approval.
- When static dependency closure can't be proven (unexecuted branches, OR witnesses, free text), **block/review the whole experience** and separately measure unnecessary review. Do not claim selective invalidation precision from this HTML.
- Existing 3.2 master/4-case sealed holdout and negative cases cannot enter implementation prompts or public docs.

## Measured preview QA

The planning chat created a standalone HTML/CSS/JS prototype (no external resources). Chromium Playwright `page.set_content` smoke verified **17/17 checks**, including source cards, draft, local approval, Q1/Q2 feedback, mutation → STALE_REVIEW → visitor block → simulated re-review, media rights revoke → BLOCKED → visitor block, rights restore → STALE_REVIEW, and viewport width 390px and 320px without horizontal overflow. Browser JS exceptions zero. Nine visual screenshots were captured and a PDF report was rendered **16/16 pages**, no replacement glyphs/out-of-page text. The ZIP was independently extracted and the 17 browser checks reproduced. Not a Kiro engine test.

The research session produced: A4 landscape 16p PDF detailed spec; interactive standalone HTML; 39-row acceptance matrix with `PROTOTYPE_PASS` vs `NOT_TESTED`; 14KB technical handoff; new-file unified patch; source smoke script and SHA manifest. These files stay in the user's chat artifacts, NOT copied into public product source.

## Actual Kiro development snapshot

Latest observable B4 user-pasted local report main `09f4b8a524058440a7dbc9917d3112640d73d258`, 164/164 Node tests twice; B4 sources **not independently audited**. B5 final QA not confirmed at time of this plan. No automatic B4 rerun. D2 implementation, auth, cloud billing, real collection rights, public license, deployment and actual publishing remain separately gated consequential decisions.

**Next action:** B5 inspect local evidence and known F3-12/F3-13, then scope the separately authorized D2-UI adapter to render *actual B3 structured output* rather than a synthetic fixed HTML experience. This document does not itself authorize starting D2/cloud.

Source links: https://kiroween.devpost.com/rules ; https://en.actionbound.com/museum ; https://www.axiell.com/solutions/product/cultureconnect/ ; https://www.w3.org/TR/prov-o/
