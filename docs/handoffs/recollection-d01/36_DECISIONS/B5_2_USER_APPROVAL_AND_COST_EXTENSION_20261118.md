# Re:Collection B5.2 — User approval and bounded credit extension

**Date:** 2026-11-18 KST  
**Decision:** `B5_2_ADAPTER_IMPLEMENTATION_APPROVED` — **ONE** local-only stage, synthetic/demo data, existing Opus5.5 MAX main Kiro session only.  
**Approval source:** In the directly preceding ChatGPT conversation, the assistant asked for specific consent to implement “별도 출력 어댑터 + 합성 자료 2점 DEMO_SIMULATION + 32개 사전 정의 테스트 + 기존 코드·오라클 보존 + Opus 5.5/MAX 메인 세션만 사용”, and warned of **estimated 40–70 extra credits**, potentially unobservable and beyond previous caps. The user replied **“추가 크레딧 가능 ㄱㄱ”**, authorizing **that described B5.2 scope and additional credit risk**. This grants **no unbounded later stages** and **no paid platform upgrade**.

This decision overrides `35_PLANS/B5_2_TYPED_OUTPUT_ADAPTER_IMPLEMENTATION_GATE_20261118.md`'s *approval-pending* state **for B5.2 only**. All other safety, rights, unchanged-B0-B5.1, no-external-media, no-publish and holdout restrictions remain binding.

## Exact technical scope approved

- Add standalone, versioned **`VisitorOutputContract v0.1` typed data-only adapter** AFTER actual B1/B2 validation and B3 runtime; no rewrite of ExperienceSpec v0.2 or the four primitive semantics.
- Synthetic owned **two-record `DEMO_SIMULATION`**, two proposed educational questions, no real curator authentication/review or real publisher. Explicit demo-only state and nonpublishing output.
- **32 preregistered security+benign public development tests** S01–S08, E01–E08, R01–R08, D01–D08 in `35_PLANS`; freeze exact expected results and fixture/hash manifest BEFORE implementing. These exposed tests are **NOT** independent blind human evaluation.
- Deny default unreviewed model text, misleading `Recorded fact`, unsupported factual feedback, leaked internal IDs/states, unsafe media/text-rights recycling, unknown output kinds, changed-source or rights-revoked output. Quote presence != historical semantic entailment; label `SOURCE_QUOTE_PRESENT` and require human review for claims.
- Conservative whole-experience `NEEDS_REVIEW/BLOCKED` on changed source/rights or unproven dependency closure; no selectively revalidated-feedback claim.
- Node24 built-ins and existing zero-new-dependency architecture. Preserve all B0–B5.1 source/test historical provenance and fixed-oracle cases.
- Main Kiro session configured **Claude Opus 5.5 / MAX**, **no subagents** (unpin-able review subagent previously switched to Opus4.8), no model Auto/fallback. If live model actually changes, STOP rather than silently proceeding.

## Costs and capacity

- User explicitly allows incremental **B5.2 credit exposure** at the estimate **+40 to +70 bonus credits** discussed immediately before approval. This is an **estimate**, neither guaranteed nor measured in `/usage`.
- Historical original start used `513.26/4000`, B0–B5 aggregate original soft used `733.26`, hard used `813.26`; do **not** reset historical ledger or claim those limits were actually monitored. New approved B5.2 extension is explicitly scoped **only to B5.2**, after the historical program. Record actual direct readings when already available, else `BONUS_USAGE_UNOBSERVED`.
- With no direct current pool meter, **do not claim a hard credit cap can be enforced**. Limit work by a single adapter implementation/test pass and bounded fault-fix loop; if estimates become implausible, work expands materially, a paid upgrade/new account is needed or credit exhaustion is observed, STOP and report. User explicitly rejected repeated `/model` and `/usage` screenshot gates.
- No assumption that the `Credits: turn/session` footer is bonus-pool usage. No AWS/Bedrock, subscription, paid API, background automation, deployments or extra model arms are included.

## Local Git and stage boundary

- Isolated Windows local repo expected `C:\Users\admin\Projects\recollection-kiroween-2026`, `main`, clean, remote NONE.
- Expected local HEAD after prior docs-only ADR erratum: `52e230dfa96601e310b3210ae4af81e701eb74ad`.
- Preserve GhostWeb dirty `23b8a010` and BLINDSPOT unpushed `c073ddd1` untouched. Do not reset/rebase/stash, do not rewrite prior Git commits or historical oracle.
- Create **one new local B5.2 commit** only if tested green. Produce full SHA, clean status, exact unified diff including new files, evidence files generated deterministically, two identical normalized tests and per-case expected vs actual verdicts. No pushing and no new remotes.

## Outside the approval / still HOLD

- **No browser/visitor renderer UI**, actual curator role/authenticated approval, public hosting, publication, external rights-sensitive museum assets, real data, AWS, 3–8 contract migration, R3.5 unsafe-text policy relaxations, and no actual D1E A/B experiments.
- **No import** of 3.2 sealed holdout, research 3.14's private corpus, or research 3.15's private workbook/test matrices into Kiro developer workspace. Latest research 3.15 is a **future raw source data contract only**: 181 proposed acquisition tasks / 83 future tests with no independent human labels or executed real-source product runs; no new B5.2 code acceptance criterion or user-media permission.
- Even if B5.2 tests pass, product visitor use, real-source rights, independent historical claim review, D1E and D2 all **HOLD pending separate acceptance**.

**Next:** Execute ONLY the pinned B5.2 implementation workflow at this docs branch's immutable GitHub commit. Do not redo B0–B5.1 or the ADR correction. No additional user question required for this same already-approved bounded task.
