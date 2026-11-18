# Re:Collection — bounded D2-V1A trust audit → D2-V1B generalization gate

**Date:** 2026-11-18 KST  
**Status:** DESIGN ONLY, NOT APPROVAL FOR NEW KIRO SOURCE CODE, EXTRA CREDITS OR D1E.  
**Baseline:** user-reported D2-V1A local commit `ca941c5748c0c20a11144fd4f1a83da9e85c7a00`. Preserve frozen B0–B5.2, D2-V0, D2-V1A previous tests/data/diffs, do not rerun or rebuild completed stages by default.

Read `48_ALIGNMENT/D2_V1A_REPORTED_PASS_RIGHTS_REBASE_AND_PRODUCT_RESEARCH_20261118.md` and current ADR-0009 in the **actual local workspace** before authoring any new implementation. Author's proposed future plan doesn't establish that a vulnerability exists; the code has not been independently inspected.

## Core product decision

The next iteration must **stop proving only that 2 hardcoded questions can appear**, and begin testing whether Re:Collection handles a *new, not hardcoded* source combination with a trustworthy source→editorial review→visitor choice→invalidate sequence.

A D2-V1B generalized investigation engine cannot be marked PASS solely by adding more fixed template branches, UI cards or mutated status labels. A new synthetic fixture must enter through **existing public contracts** without changing B5.2 security or importing private eval holdout; the system should propose/review and instantiate evidence-linked interaction records. Any claim of AI authorship must actually call the documented model process under fair budget/permissions, not disguise static seeded text as generated. Defer model calls until separately approved.

## Gate A — one bounded targeted code-and-UI audit (non-destructive unless separately authorized)

**Audit problem 1 — “rebind current baseline + reset rights history”**
- Distinguish current verified immutable source/rights snapshot, previously revoked rights event, B5.2 validation report and DEMO_EDITORIAL_REVIEW receipt. Audit exact `src/demo-editorial/*`, `tools/local-viewer/server.ts`, `src/local-viewer/*`, ADR-0009.
- Twelve test ideas must be chosen from this risk rather than another entire generic 30-case suite: (i) currently revoked then demo review; (ii) restored but no fresh review; (iii) forged restore; (iv) old receipt replay; (v) stale right digest; (vi) forged sourceID/snapshot; (vii) same data new untrusted registry; (viii) source change without direct citation; (ix) before-vs-after rights audit retention; (x) two tabs conflicting review; (xi) delayed prior response; (xii) byte-identical no-op.
- For every review, require exact source/rights and editorial bytes from **trusted current snapshot**, never from browser-submitted rights flags or model `approved`. If rights history is reset, ensure it is labelled `DEMO_ONLY` and cannot impersonate real legal rights/approval. Document invariant and observed result, report P0 if an actual fail-open is demonstrated.
- **Do not invent code/test status.** Prefer inspection plus existing runtime tests first. New test files or code modifications need user’s separate approval.

**Audit problem 2 — static label/ARIA/metadata rights leakage**
- D2-V1A browser first run failed due to a static button label containing `NOT_RECORDED` even while rights were revoked. Verify that not only B5.2 blocks and main text but **all HTML attribute and accessibility-tree sinks** remove/withhold this and any other restricted field after rights revoke. Inspect current 15 local screenshots in context, not generated simulations.
- Maintain safe DOM, Host/Origin/CSRF/CSP and out-of-order response protections, demonstrate 320/390 width state transitions and status visibility. No general WCAG certification without real testing.

**Audit problem 3 — equivalent mutant**
- One of 16 mutation changes survived according to Kiro. Prove in actual control flow why the removed check was redundant (or write a distinct adversarial counterexample). Label `EQUIVALENCE_PROVEN` only with evidence; otherwise `OPEN_MUTATION`. Never silently claim 16/16 killed.

**Stop condition:** One targeted pass, clear P0/P1 findings and reproduction paths; do not loop indefinitely if no new vulnerability. A verified FAIL leads to a **small separately approved patch**, not a new architectural research program.

## Gate B — three unfamiliar synthetic investigations (product capability, future approval)

After Gate A's critical boundaries are sound, create **3 separate owner-authored, fictional, rights-clean 2–4-record packs** that are different from the hardcoded ARC-01/02 pair. Choose domains with different evidence relationship structures (e.g. transit service log, an industrial inspection timeline and an environmental monitoring change) but use no real records, copyrighted photos, private 3.2 holdout, or unauthorized museum media.

- Each pack includes a **source registry, rights snapshot, learning goal, one contradictory/insufficient claim, 2 evidence-linked questions, explicit reviewable question/option strings, one source revision and one rights event**. Author the public development fixtures without providing the hidden independent evaluator keys from research 3.2.
- Run the same v0.2→B2→B3→B4→B5.2→D2-V1A reviewed-demo path with **no case-specific source code edits per pack**. Record time to author, adaptation steps, editor review action count, change/review invalidation accuracy, false blocks and blocked unsafe assertions.
- Compare **baseline hardcoded ARC-01/02** vs novel packs for successful structure, answer/feedback abstention, question traceability, source revision. At least one designed negative input must be rejected rather than silently converted to a “valid” question.
- Keep synthetic editorial receipts **non-authoritative**. Do not allow a model-generated question to become trusted merely by a template flag. Actual **AI generation** can only be claimed in a later separately authorized stage when the model run/inputs/outputs and resource cost are directly recorded. Generic static templates are not proof of AI superiority.
- A future D1E against direct Opus 5.5/MAX needs **fair equal output target and independent human oracle**, not current same-model public developer checks.

## Acceptance draft (for future approval only)

- Gate A: no demonstrated privilege/rights-history bypass; static UI, aria and state outputs are safe after revoke including two-tab race; surviving mutant equivalence explained or remedied. Existing 291 Node tests and D2-V1A frozen 24 developer cases remain unchanged.
- Gate B: at least **3 of 3 synthetic packs** complete safe reviewed-demo question/choice/invalidation with unchanged code and distinct registry hashes; reject unsafe false claim inputs; deterministic evidence; two regression runs, actual browser screenshots and audit trail. Do NOT require actual historical answer feedback.
- Product milestone: a repeatable *source-driven demo authoring* workflow, not merely a hardcoded 2-question showpiece. Developer-only tests cannot by themselves establish independent product-market fit or a contest win.
- Reporting: one Korean review with exact local SHA, real diff (if implementation separately approved), 3 pack per-case outcomes, independent visual access status, measured browser coverage, observed vs estimated credits. Local-only, no GitHub product push or public cloud.

**Out of scope:** cloud hosting, paid AWS, real authenticated curator approval, live Met media, claim truth certification, 3.17 collector hardening changes within Kiro source, original hidden 3.2 research holdout, D1E experiment. User approval is required for any new implementation and additional credits.

**Current next decision:** Approve a small **D2-V1A trust-boundary audit** (read-only targeted review first, separate fixes if proven) and then choose whether to fund D2-V1B novel synthetic generalization; do not implicitly spend previous D2-V1A credit allowance on V1B.
