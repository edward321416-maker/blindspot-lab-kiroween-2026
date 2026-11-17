# Re:Collection B5.2 — Safe visitor-output contract and Archive Detective adapter

**Status:** DESIGN ONLY / NO SOURCE CODE OR UI BUILD AUTHORIZED.  
**Research alignment:** Research 3.11–3.14 proposes a two-source first vertical slice, two linked questions and revocation-aware review; the 3.12 browser prototype's synthetic local approval is not security authorization. Freeze B0–B5.1 contractual oracles and history.

## 1. Problem definition

B5 main QA exposed:
- B5-01: `HISTORICAL_FACT` can match a 1-character/irrelevant locator (F3-12), then visitor-visible text may be labeled `Recorded fact`. The underlying B2 `historicallyVerified=false` does not prevent mistaken visual authority.
- B5-02: AI-proposed question/title/compare labels/`suggestedEvidence` can appear in future output without claim-level human review.
- B5-11: excerpts from rights-restricted media/text can be laundered through free-form claim text; item rights and *text* license may differ.
- B5-24: indirect evidence dependencies across question→choice→branch→feedback are not closed and cannot be presumed.
- B5-04/09: safe structured output can still become unsafe HTML or unauthorized state semantics in a later renderer.

**Do not attempt an automatic historical truth oracle.** Quote existence, hashes and model confidence never equal semantic entailment. Establish auditable human review of exact visible output, historical claims, citations and rights, with strict abstention while unreviewed.

## 2. Proposed architecture (NOT approved for implementation)

Propose an additive **versioned adapter**, e.g. `VisitorOutputContract v0.1-DRAFT`, between immutable B3 structured output and a future safe visitor renderer. This is **NOT `ExperienceSpec v0.3`**, not a freeform model-generated HTML/JS application and not a new approved publisher.

```
Owned synthetic source registry / rights proof
     → Existing ExperienceSpec v0.2
     → B2 validation on stable input snapshot
     → B3 restricted data-only runtime
     → B5.2 Output Adapter: typed visible sink allowlist / evidence+rights binding / review digest
     → [future separately authorized] Safe Renderer (DOM textContent / escaped text)
     → [future separately authorized] authenticated curator approval / immutable publication
```

No actual UI, auth, approver role, publisher, URLs, cloud, media download or authorization is created by this design.

## 3. Exact proposed sink inventory and default policy

Every **visitor-visible string** must be traced to (i) trusted local system-controlled copy, (ii) exact licensed source quote and locator + source hash with non-assertive label, or (iii) **human-reviewed** AI-authored display text bound to the exact output/text hash and context. Unknown sink or unreviewed model string → **BLOCK / NEEDS_REVIEW**, never render.

| Sink / path (conceptual, inspect real runtime exports first) | Risk | Proposed initial response |
|---|---|---|
| Experience title, subtitle and learning goal | Unreviewed factual authority | human-reviewed text or system-owned neutral instructional title only |
| Source-card title/date/creator/location, visible excerpt | Misleading metadata, item/license differences | exact trusted source-field locator, preserve uncertainty and attribution |
| `info-panel` body, compare row label/value | B5-01/02 arbitrary text | typed source-backed observation or **UNVERIFIED/NEEDS_REVIEW**; do not say Recorded fact from B2 alone |
| `questions[].text`, `suggestedEvidence` | Unreviewed leading question | human-reviewed version-scoped output text, exact linked source references |
| Answer options, answer key, feedback | Apparent correctness on missing entailment | **NOT PRESENT** until separately reviewed choice→answer→feedback and all OR-witness dependencies |
| Branch/node/state names and debug trace | `published` / `curator_approved` spoof | internal IDs only, never display these strings as status or authority |
| Language translations and right-to-left text | semantic drift / false blocks | separately reviewed per language + context, no implicit translation reuse |
| Images/audio/video, source URL, alt text | rights laundering, unsafe URL | source asset IDs only, no external media or dereference; per-asset/media/text license and snapshot proof required |
| Generic JSON metadata, arbitrary nested props or unsupported kinds | OAP cross-sink bypass | reject recursively unknown output fields and unknown AST operations rather than silently rendering |

**Label semantics proposal:** `SOURCE_QUOTE_PRESENT` = quote exists in immutable snapshot, **NOT claim truth**. `HUMAN_REVIEWED_CLAIM` requires real named reviewer with verified authority and exact claim/context digest. `EDUCATIONAL_MODEL` needs explicit pedagogical label and reviewed assumptions. `INFERENCE` visibly tentative. `UNKNOWN` / `NEEDS_MORE_EVIDENCE` abstains. Never use `RECORDED/Recorded fact` unqualified.

## 4. Proposed review digest / invalidation

For each reviewable object (visible line/claim, answer justification, branch decision, image right):
- Versioned digest should bind the **actual visible text bytes**, selected source/quote/locator/source snapshot SHA, license evidence and provider policy revision (if observed), claim kind, language, audience, question state, answer/feedback template, and the output policy version.
- Only a genuinely authenticated curator/reviewer may sign/approve; synthetic UI demo `approved=true` cannot establish it. No model-authored or caller-supplied `approved` bypass.
- If a source field, rights statement, quoted text, learning objective, feedback rule or policy changes: revoke affected approvals and block visitor output. If full dependency graph can't prove closure, **conservatively block/re-review the whole synthetic experience**, not pretend selective invalidation accuracy.
- In research 3.12 the `ARC-02` status update and `mediaRights: ... → REVOKED` are two separate simulated events; no real asset URL should remain public after a rights revoke. Browser/cache/CDN revocation is **NOT_TESTED**.

## 5. Preregistered threat and benign tests to design first

**Threat classes**: irrelevant 1-byte/whitespace quote (F3-12), contradictory quote, Unicode/injection and escaped HTML, fabricated answer/feedback in free-text title, extra compare label or node, root metadata consumption, unknown AST kind, unsafe state ID, multilingual substitution, wrong source or outdated review digest, rights-restricted excerpt as innocent text, media URL in educational constant, direct URL and encoded scheme, version rollback/TOCTOU, source-change indirect dependency absent.

**Benign classes**: curator title with colon `Data:...` known B5-03 overblocking, ordinary annotations, long but bounded museum captions, classroom-safe quotation, reviewed translated text, time/date/negative statements, correctly rights-cleared synthetic captions.

**Acceptance is not defined as 100% historical truth**. Proposed gates: every unreviewed or rights-unclear visitor-facing sink blocked; no visitor state shows a privileged status from model fields; rendered output uses code-safe string sinks; zero changed-source stale approvals accepted; no false claim of human-reviewed provenance. Show benign false block rate separately. Tests and independent scoring must be separately selected BEFORE implementation; research 3.9 self-authored 38 cases and 3.14 495 offline self-oracle checks are not implementation acceptance.

## 6. First permitted product demo candidate after future approval

**Only synthetic, offline 2-item vertical slice:**
- Curator intake of two owned fictional records, 2 linked reviewed questions; current v0.2 2–4 object count retained.
- Preview source→claim→question without asserting factual entailment; human-like reviewed statuses are **mocked UI state**, explicitly labelled `DEMO_SIMULATION`, never product authority.
- Visitor can observe and compare, but **no automatic unreviewed correctness feedback**. For comparative quality experiment, actual common output and evaluation target must be fixed on both arms.
- Simulated source-field change or media rights revoke: visitor view BLOCKED/STALE_REVIEW until explicit simulated re-review; conservative whole-experience blocking when dependency closure missing.
- Implementation and browser accessibility are **NOT TESTED** in the current user-local Kiro engine. Future D2 safe renderer needs explicit architecture/product security authorization and actual code/app tests. Distinguish from research 3.12 17/17 standalone HTML test.

## 7. Decision gates and sequence

1. **Now:** Correct ADR-0006 mixed-model provenance by additive docs-only local commit; D1E prereg remains planning only.
2. **Design review:** user must select **B5.2 output policy architecture scope** (separate adapter, no ExperienceSpec v0.2 modification) and whether first prototype uses synthetic REVIEW_SIMULATION or requires real authenticated curator roles. This alters architecture and claims, so needs explicit approval.
3. **On approval:** produce a separate implementation task for B5.2 with actual local API signatures, new frozen negative+benign tests, threat model and bounded Node24 zero-dependency budget. No dynamic HTML/JS output from model.
4. **After adapter passes:** approve separately a safe viewer renderer and assess actual visitor UI. Do not translate the prototype's hard-coded approval into real publishing rights.
5. **D1E product comparison B-arm:** only execute when both arms produce comparable judge-testable outputs and independent human blind oracle, real rights if used, and explicit time/credit budget. An A-arm contract-only comparison may be performed only if labeled technical and separately authorized.

**Pending:** user approval of new output adapter architecture, any actual code changes, UI/auth/release, model usage budget, independent evaluators, and IP/right decisions. Never claim approval from the existence of this document.
