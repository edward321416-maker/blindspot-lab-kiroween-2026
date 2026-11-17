# Re:Collection — B3 completion / B4 research-and-development alignment

**2026-11-17 KST · documentation only · B3 LOCAL USER REPORT · no external QA of user's Windows code.**

## 1. Reported technical checkpoint (do not repeat)

- Local Re:Collection: `C:\Users\admin\Projects\recollection-kiroween-2026`, branch `main`, clean, **no remote**.
- Parent B2: `54f88b5be8a50afa187640d7d8564f75cb7b51ae`; completed B3: `4c4dc7adf49f8c6a3e699da0370bd8c93374e98a`.
- User-reported diff: `D:\Users\admin\Desktop\hackathon\ReCollection_D1_BUILD_reports\B3_4c4dc7a.diff`, 860 lines, SHA-256 prefix `4f43de5e`. The full diff and local code are **not accessible to this public docs-only branch**.
- `src/runtime/run.ts` public API reportedly `run(spec, snapshot, script, { mode, validation })`. Re-normalizes input exactly once, reruns B1/B2 validation against normalized snapshot, accepts only byte-equivalent validation report for that exact spec/snapshot/mode; otherwise `RUNTIME_REFUSED_UNVALIDATED`.
- Four built-in primitives `info-panel`, `compare-cards`, `sequence-encoder`, `research-task` produce **structured data only**, with no generated HTML/JS, historical truth certification, correctness judgment or visitor feedback.
- Visitor script currently only `user:start`, optional encoder input up to 1,000 chars; 50 step cap, 256 KiB aggregate output cap. Failed steps do not mutate state or echo user strings.
- Frozen runtime oracle R01–R06: **6/6 matching**. Prior full `node --test --test-reporter=tap "tests/**/*.test.ts"`: **134/134 PASS** on two runs and a postcommit rerun, output line hash prefix `b6b6cc05`, evidence SHA prefix `a6be901d`; 15 runtime adversarial tests.
- B0, B1, B2 tracked files and test fixtures reportedly diff 0, research holdout not imported.
- `TYPECHECK_NOT_RUN` and `BONUS_USAGE_UNOBSERVED`. Model only `SESSION_CONFIG_ONLY` = `claude-opus-5.5` / `max`; no per-turn attestation.
- GhostWeb dirty HEAD `23b8a010` (two local edits), BLINDSPOT `c073ddd1` (one unpushed) preserved. No installs, AWS, remote, deploy, B4.

**This is a precise summary of the user's Kiro report, not independent technical verification.**

## 2. B4 bounded role: reproducible technical integration, NOT a museum product demo

Existing D1-BUILD scope assigns B4 `Controlled smoke/evidence output`, projected +40 credits (unmeasured). Complete **one-object synthetic UNIT_SMOKE** and **two-object synthetic nonpublishing E2E** from trusted registry → B1 contract → B2 semantic/rights validator → B3 Runtime, produce deterministic machine-readable evidence, rerun complete suite twice and preserve existing fixed oracle.

B4 must explicitly fail or mark NOT_TESTED rather than imply:
- browser interaction, actual visitor UI, keyboard or accessibility;
- real museum media distribution rights or curator approval;
- generated-experience success from **novel unseen museum records**;
- independent human-held-out evaluation or comparison against direct Opus generated HTML;
- research-version `ARCHIVE DETECTIVE` 3–8 artifact end-to-end journey or evidence-complete feedback;
- AWS/Bedrock orchestration, public publishing, authenticated approval ledger.

**B4 PASS requires proof of technical integration only**, not a product/contest victory claim.

## 3. Research alignment as of this memo

| Issue | Actual status | Impact | Action |
|---|---|---|---|
| Re:Collection 3.0 HERO `ARCHIVE DETECTIVE` (3–8 items, 3–5-min investigative visitor path) | Research product plan; current B0–B3 has a frozen 2–4 contract and B3 2-object `compare-cards` | **L2 contract change candidate**, not accepted in D1 | **KEEP** B4 scoped integration, **REPLAN/DECIDE** future 3–8 release schema and multi-record graph/visitor UI before claiming hero experience |
| Evidence-to-Interaction Graph with source→claim→choice→feedback | Direct source bindings/semantic gate and structured runtime exist, but B3 deliberately does **not** calculate answer correctness or feedback | Missing product feature, not proven safe | **KEEP** B4 no-feedback result; future confidence/feedback needs evidence-closure acceptance before coding |
| R-3.6 selective revalidation | Prior research-chat reported dependency misses; not demonstrated in B3 | Invalidation correctness unresolved | B4 full validation path is **conservative**; do not claim selective revalidation |
| R-3.7 indirect dependency completeness | Research design, not independent B4 pass | Missing indirect supporting evidence for feedback/branch | **OPEN RESEARCH GATE**. No leaked holdout or fabricated completion |
| R-3.8 empirical falsification program | Reported planned comparison, raw final source unavailable in current handoff | Not executed here, not product result | Keep planned evaluation in research channel only; no results manufactured |
| B2 overblocking `Data: ...` | Known Kiro-reported P2 issue retained by B3 | Legitimate curator language can be refused | **P2 backlog**, no bypass inside B4; later change requires threat-model & regression review |
| B2 irrelevant-locator validity | B2 locator matching confirms quote existence, **not relevance/entailment** | Severe potential claim/feedback risk | Do not treat `historicallyVerified=false` as historical fact certification, never generate authoritative feedback |
| Current model & credit accounting | Saved Opus/MAX config only, bonus usage unread | Cost cap cannot be independently certified | No repetitive manual screenshot gates; report unknown and limit B4 to originally estimated small stage |

## 4. Decision: B4 now vs future design

**GO — B4 synthetic integration** with original B0–B3 contracts and test harness. Do not redo earlier stages. Keep local scope isolated, no npm packages.

**HOLD — B5 final quality/go-for-D1E conclusion** until B4 outcomes exist, and distinguish source/test evidence from research hypotheses. Do not silently expand B5 into product UI.

**PENDING USER PRODUCT DECISION (not necessary to run B4):** whether 3–8 objects and indirect evidence-qualified feedback replace or version the current 2–4 ExperienceSpec contract. This is an L2 change that needs explicit product/architecture acceptance before user-facing implementation. Do not ask to decide it as a precondition to the small B4 integration smoke.

**Research confidentiality:** Do not copy hidden test artifacts, held-out cases, full corpus, negative-case answer keys or protected rights metadata from research source bundles into Kiro's local runtime tests or this public GitHub branch.

## 5. Later engineering priorities, not B4 deliverables

1. Product contract versioning with 2–4 synthetic demo backward compatibility and planned 3–8 research experience.
2. Evidence dependency closure for choice/branch/feedback with independent human blind evaluation.
3. Multi-source comparison/investigation flows beyond fixed two-item `compare-cards`.
4. Actual accessible browser/visitor preview, curator review/approval and safe publication (separate architecture + rights + cost decisions).
5. Comparative direct-code vs compiler experiment (D1E) separately approved, no credit reuse.

**Current statement:** B0/B1/B2/B3 PASS **KIRO_LOCAL_REPORTED**; B4 **NOT_RUN**, until actual Kiro report supplied. Product success = **UNPROVEN**.
