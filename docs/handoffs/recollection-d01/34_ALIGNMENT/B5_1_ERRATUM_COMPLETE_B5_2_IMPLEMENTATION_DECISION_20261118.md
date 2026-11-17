# Re:Collection — ADR-0006 correction closed / B5.2 product decision register

**Snapshot:** 2026-11-18 KST  
**Source confidence:** USER-PASTED KIRO LOCAL REPORT, NOT direct Windows Git inspection.  
**Current decision:** ADR-0006 factual correction CLOSED (local reported), B5.2 OUTPUT ADAPTER ARCHITECTURE RECOMMENDED BUT **NOT IMPLEMENTATION-AUTHORIZED**, D1E EXECUTION HOLD, public product/visitor output HOLD.

## A. Already completed, never repeat

Local Re:Collection history:
- B5.1 technical security patch at `101836551883aae0e5fc179100538de2e5beeacb`; prior measured **194/194 PASS** twice and postcommit, 164 B0–B4 tests and 30 new tests. Separate main-session Opus5.5 validation underlay this TECHNICAL PASS.
- ADR-0006 docs-only correction: new full local main HEAD **`52e230dfa96601e310b3210ae4af81e701eb74ad`**, parent `101836551883aae0e5fc179100538de2e5beeacb`, clean/no remote, `git diff --check` pass.
- Corrected current ADR `docs/decisions/ADR-0006-b5-1-integrity-patch.md` + new `docs/decisions/ADR-0006-erratum-1-challenge-model-provenance.md` (47 lines). Local report `B5_1_ERRATUM_52e230d.diff` full SHA256 `19482bb4aed696575ca2f8c761e199c0f7f7484cc59e393a8f1f42714e4e6576`, 7,965 bytes/95 lines. Raw bytes not available in this GitHub docs repository.
- All `src`, `tests`, `tools`, `reports/evidence`, `reports/qa`, `.kiro`, `package.json` and README tree hashes remained unchanged. `NOT_RUN_DOCS_ONLY` is accurate; **do not falsely say 194 tests were rerun after erratum**.
- Model audit: B5.1 QA subagent **8 events Opus5.5 then 15 Opus4.8**, violating Opus5.5/MAX only. Main session had **210/210 recorded Opus5.5 events as of 02:33 KST** and reran challenged cases; effort still `SESSION_CONFIG_ONLY`. Earlier same Kiro session before Re:Collection also contained other-model activity in separate projects, so never claim every Kiro event was Opus5.5. Original logs/commits preserved.
- No new subagent in docs-only correction. **Do not reopen the ADR correction unless actual evidence contradicts the report**.

## B. B5.2 planning proposal from user-pasted report

- Existing local `D:\Users\admin\Desktop\hackathon\ReCollection_D1_BUILD_reports\B5_2_DECISION_BRIEF.md`, reportedly 6,271 bytes and SHA256 prefix `dd8bacfd`; **not independently byte reviewed here**.
- Proposed separate `VisitorOutputContract v0.1-DRAFT` adapter consumes trusted B2 snapshot/validation and B3 structured output, returns typed view OR `BLOCKED` / `NEEDS_REVIEW`.
- Maintain existing `ExperienceSpec v0.2` and four primitive set, integer-only JCS, 50-step bound and source/rights check, Node24 zero initial dependencies, 2–4 objects, no `R3.5 UNSAFE_TEXT` loosening.
- Free-form AI titles, question copy, compare labels and `suggestedEvidence` are **not automatically visible**; require genuine authorized review of exact output bytes/context or explicitly inert system-owned copy. Never interpret an existing unrelated quote as historical entailment.
- Only `SOURCE_QUOTE_PRESENT` labels exact quote/locator/source hash; **never `Recorded fact`**, automatic `CORRECT`/feedback, approval or publication.
- All output sinks, unknown JSON fields, visible internal state IDs, right-to-left/text encodings, media asset IDs, text-specific rights and change invalidation must be inventoried and default-denied.
- Real human signed approval and public publisher are **not** part of B5.2 first patch; the proposed initial demonstration is **`DEMO_SIMULATION`** with two *owned fictional* records and two questions, no network, no curator login, no public link. Demo state must not be represented as real REVIEW_APPROVED.
- Research 3.11 first slice 2–4 aligns with current D1; older 3.0 3–8 is **future L2**, not a reason to modify v0.2 today.

## C. Current research snapshot

- GitHub `24_PLANS/RECOLLECTION_3_12_CONCRETE_PRODUCT_INTERACTION_CONTRACT_20261117.md`: synthetic 2-record Q1/Q2 interaction and change/revocation concept; standalone browser research prototype 17/17 UI tests is **not** integrated Kiro B3 output.
- GitHub `29_RESEARCH/ARCHIVE_DETECTIVE_SOURCE_INTAKE_AND_RIGHTS_REGISTER_20261118.md`: genuine catalog references, text/index links **not** third-party media redistribution permission; mayor caption conflict requires human review.
- GitHub `30_RESEARCH/RECOLLECTION_3_14_MULTIDOMAIN_SOURCE_LAB_20261118.md`: **58 heterogeneous research URLs** (not 58 individually verified artworks), 12 research case proposals, 8 link-only candidates and 4 rights/conflict HOLD, **0/12 publicly approved**. 495 researcher-authored oracle checks/run (two runs) and 21 standalone Chromium UI checks are not Kiro code security, independent human accuracy or rights licenses.
- The 3.2 sealed evaluation corpus/hidden answers and detailed private research fixtures must not enter B5.2 prompt or public docs.

## D. User-impactful decision and recommendation

| Decision | Proposed default | Rationale / tradeoff |
|---|---|---|
| Product architecture | **A separate versioned visitor-output adapter** between unchanged B3 and future viewer | Add typed provenance/rights/review without risky frozen schema rewrite |
| Prototype auth | **`DEMO_SIMULATION`**, two fictional records and two questions | Build visible proof cheaply; no false assertion of authenticated human approval |
| Security/benign test owner | Public developer-safe test matrix authored and **SHA frozen before code**, separate research team cross-check; independent human blind oracle **UNASSIGNED** | Public tests are regression, NOT independent evaluation |
| Credit budget | **UNKNOWN actual consumption and headroom**; explicit spending allowance required for new code; no AWS/paid services | Original cumulative soft used 733.26/hard 813.26 cannot be proven from session footer; do not reset baseline |
| D1E choice | **B: defer product-level direct-code vs compiler comparison until safe real viewer exists** | Contract-only A can be planned separately, cannot claim product quality |
| Visitor/PUBLISH | **HOLD** even after adapter code PASS | Real reviewer, live rights and review digest/publisher missing |

### Scope distinction

- **The current user message supplies a completion report, NOT explicit permission for a new B5.2 local source-code implementation, architecture acceptance or additional credit allocation.**
- Prepared GitHub plans are not implementation authorization.
- Next assistant/user action may explicitly approve **limited B5.2 adapter only** on existing local isolated repository, no renderer/visitor UI or cloud, within separately stated credit authorization, while preserving holdout and existing oracles.
- Until then, read-only inspection and nonexecuting design/test-plan documents are permitted, not a covert code change.

## E. Issues remaining BLOCKED

**B5-01:** actual quote at locator (even one byte) can be unrelated to generated historical claim and erroneously rendered `Recorded fact`. **B5-02:** AI-authored visible strings without review. **B5-11:** rights-laundered text not derivation-checked. **B5-24:** indirect claim→choice→branch→feedback dependency closure unproved. UI-specific B5-04/09/10/15 likewise not proven safe. `TYPECHECK_NOT_RUN`, `BONUS_USAGE_UNOBSERVED`, independent human reviewer `UNASSIGNED`.

**Milestone status:** B5.1 PATCH PASS reported; ADR correction CLOSED reported; **B5.2 NOT_IMPLEMENTED**; `D1E_EXECUTION_HOLD`; `PRODUCT_PUBLICATION_HOLD`.
