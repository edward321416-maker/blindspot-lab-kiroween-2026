# Re:Collection — D1E A/B preregistration package (PLAN-ONLY)

**DATE 2026-11-18 KST · D1E PREP ALLOWED BY B5 RECOMMENDATION, D1E EXPERIMENT NOT AUTHORIZED.** The B5 same-model QA said `GO_FOR_D1E_PREP` only; this document is a **design**, not A/B results, human/blind validation, AWS permission or credit approval. **No original research 3.2 sealed holdout / independent answers may be disclosed here or to the Kiro implementation agent.**

## 1. Research question & claim boundary

RQ: For the *same source-qualified synthetic or rights-cleared museum inputs and a frozen learning goal*, does the source-bound `ExperienceSpec v0.2` compiler approach reduce unsupported factual/rights/publication errors and curator verification effort compared with asking Claude Opus 5.5/MAX to directly code a visitor experience?

**Arms:**
- **C1 Direct Build**: Opus 5.5/MAX writes bounded standalone app/code using the supplied common educational task, public source/rights bundle, security requirements and time/credit constraints, no access to C2 implementation, hidden oracle, scoring examples or C2 results.
- **C2 Compiler Build**: Same Opus 5.5/MAX proposes a schema-safe `ExperienceSpec` from the same common public input, passes immutable B1/B2 validators and B3 restricted runtime and (if independently approved later) a secure versioned renderer. Compiler construction and the proposed future renderer are **one-time engineering costs** tracked separately from marginal per-case work.
- **C0 optional conventional baseline**: existing museum authoring tool or manually designed static lesson with comparable user study, only if a rights-checked comparable evaluation is approved. Don't invent product parity.
- **Equal constraints**: same model, MAX effort, same available text/source/rights, same educational goal, separate sessions, preregistered attempt limits, identical clock/credit accounting assumptions. Tool-access differences must be documented and normalized, not handwaved.
- **No model fallback or silently switching LLMs**. Same-model different-session QA is not independent human holdout.

## 2. Precommitted evaluation design, pending human assignment

Before revealing any holdout or generating candidates:
1. Identify independent human **holdout/oracle author** distinct from the model implementer and a separate **rights/curator reviewer**. If unavailable, prereg status `INCOMPLETE`; do not claim blind evaluation.
2. Freeze experimental hypotheses `H1` complete runnable outcome, `H2` unsupported claims/error severity, `H3` source/rights traceability, `H4` curator review actions & time, `H5` adaptation across item types and revisions, `H6` useful visitor questions and feedback. The exact 3.2 research 100-point contract must be consulted only by the authorized evaluation owner, not copied into developer training.
3. Define units at **case×arm×repeat**, not test assertion count. Two runs/case pre-registered for both arms (not picked after outcomes), blind rubric scoring, separate severe-violation frequency `P0/P1/P2`, evaluation of invalid inputs/abstention. The earlier rough two-run estimate `120–240` credits is **unmeasured** and not authorization.
4. Primary outcomes: percentage of cases with runnable interaction and no security/rights policy violations; verified source relation to factual claims; critical unsupported or self-approved statements. Secondary: visitor task completion/readability, review time, false blocks, total compute/credits and authoring time. Provide confidence intervals where possible; avoid superiority claims with small N.
5. Mark whether **human** verified historical entailment and media rights. `historicallyVerified=false` cannot be promoted to accuracy; full SHA or quote existence alone is not entailing truth.
6. Record B5-01/02/11 output-sink risks and B5-05/06/07 integrity patch prerequisite for any executable D1E. Any protected source provenance failure or unsupported output must be scored as failure/abstention, not invisible omission.
7. Freeze what the evaluator sees: generated app and outputs, source/rights fixture, hidden independent expected field, any important source changes and revocations; never reveal evaluator answer keys to either arm.
8. Replay tests and code/browser validation against **actual implemented release outputs**; standalone research HTML and Kiro Node synthetic suite are separate evidence. If compiler currently has no real UI/publisher, do not score “complete visitor app” as passed.
9. Include original initial compiler build cost B0–B5 and patch, plus per-case C2 cost; publish both comparison views with and without initial cost. Direct-vs-compiler cannot be compared fairly by ignoring that investment.
10. Enforce STOP criteria: insufficient rights, holdout contamination, nonidentical model/constraints, out-of-budget, uncontrolled output sink, generated public historical fact with unreviewed supporting evidence, privilege/cap bypass, rubric changed after seeing outcomes.

## 3. Development-research alignment

- Research 3.11 explicitly recommends a 2–4-item **first vertical slice** for ARCHIVE DETECTIVE. Research 3.12 details 2 fully fictional owned records, 2 claim-linked Qs and status mutation/review/rights revoke; this is a planning/UI **prototype** (17/17 browser checks), **not** a D1E tested output or an approved product adapter.
- Longer-term 3–8-item research 3.0 aspiration is not silently grafted onto frozen v0.2.
- Research 3.6–3.8 dependency closure/selective revalidation are unproven actual product capabilities. For any feedback inference score, demand all required source dependencies/witnesses (or abstain); do not use the evaluation hidden oracle as a developer prompt.
- Research 3.9 OAP output sink rules are **research reference** only and require a separately approved versioned adapter before product UI. Initial 5 bypass attacks were found then blocked in research, not proven against actual Kiro renderer. The D1E plan should include untrusted title, comparison labels, question and suggestedEvidence in output-policy threat coverage, not leak unpublished test case content.
- Offline engine B0–B5 plus a 17/17 standalone HTML research prototype does not yet constitute an integrated output to compare as browser app. **Mark comparator-readiness `NOT_READY`** pending explicit product/UI architecture and a safe renderer. The alternative is a scoped contract-only technical comparison with matching output types, if preregistered and approved instead of claiming product quality.

## 4. Required PREP-ONLY output

Without running an arm or modifying the local source:
- `D1E_PREREG_DRAFT.md` with scientific question, arms, blinded owners (UNASSIGNED until real), repeat schedule, n-case units, start/stop/failure rules, success metrics, provenance and budget **unknown**.
- `D1E_FAIRNESS_MATRIX.md` listing exact equivalent resources, model/effort, allowed code libraries, local/browser availability, time/attempts, reused Kiro engine costs and contamination detection.
- `D1E_APPROVAL_GATE.md`: `HOLD` until B5.1 patch verified, visitor-output adapter scope decided, independent human oracle and rights reviewer named, prospective credits allocated, safe benchmark data access agreed.
- Each file separately labelled `PLANNED / NO_EXECUTION`; not merged into product source or public repo without separate approval. No hidden evaluation truth or rights-restricted URLs.

**Status at authoring:** B5 done (KIRO_USER_REPORTED), `B5_1_PATCH_NOT_APPROVED`, `D1E_PREP_DRAFT_READY`, `D1E_EXECUTION_HOLD`, `PRODUCT_PUBLICATION_HOLD`. Future product scope / licensing / paid compute needs user decision.
