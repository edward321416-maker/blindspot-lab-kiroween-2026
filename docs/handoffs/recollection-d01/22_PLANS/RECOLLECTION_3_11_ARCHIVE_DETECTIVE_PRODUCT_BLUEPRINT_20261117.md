# Re:Collection 3.11 — Archive Detective Product Blueprint (proposal)

**Date:** 2026-11-17 KST  
**State:** PLANNING / NOT A CODE OR CLOUD AUTHORIZATION  
**Prior handoffs:** existing docs branch `20_ALIGNMENT` and `21_WORKFLOWS`; preserve original B0–B3 frozen oracle and local Kiro workspace. The 13-page PDF and detailed private handoff were produced in the planning chat, but are NOT mirrored as product source here.

## Product proposition

Re:Collection is **not merely AI quiz generation**. It proposes a source-grounded investigation authoring and maintenance workflow for museum educators:
**official asset → source-field & claim → bounded interaction spec → visitor observation/comparison/judgment → source-aware feedback → evidence-change impact and re-review**.

Product hypothesis, not proven differentiation. Actionbound and Axiell CultureConnect already offer museum digital experiences; actual paired baseline comparison remains unexecuted.

First Archive Detective vertical slice: **2–4 items** under existing D1 v0.2 contract, one learning objective, one short investigation, one reproducible synthetic update. Do **not** silently migrate to the research-product aspirational 3–8-item contract.

## Concrete user flow

1. **Curator / source intake:** select 2–4 rights-qualified items, original location, snapshot/version/hash, field evidence, learning goal. Rights-missing or locator-missing → explicit review/blocked status.
2. **Curator / builder:** AI proposes a restricted ExperienceSpec; display all ClaimRef links, source locators and epistemic types; AI cannot set verified/approved/published.
3. **Visitor / browser investigation:** inspect record, compare evidence, choose claim, receive constrained evidence-bound feedback. Unsupported historic truth must yield UNKNOWN or NEEDS_MORE_EVIDENCE, not fabricated certainty.
4. **Curator / change monitor:** simulate snapshot field correction (clearly labeled simulated); display affected question, answer, branch, feedback and stale approval. If dependency closure isn't proven, safely re-review/block the whole experience. Media-rights withdrawal needs its own publisher test.

Suggested **illustrative** investigation: “Does a historical city-plan document prove that its proposed works were actually constructed?” Use synthetic owned records for the first engine/product demo; replace only after official record & media rights review. Never infer real construction or geography from an isolated plan.

## Work boundaries

- **Kiro local B3** user-reported full SHA `4c4dc7adf49f8c6a3e699da0370bd8c93374e98a`, 134/134 Node tests; underlying source **not independently read** in this planning chat.
- **B4** existing `21_WORKFLOWS/KIRO_B4_INTEGRATION_SMOKE_EVIDENCE_20261117.md`; latest connected evidence here is *instructions*, not completion. Do not recreate B4 if the local Git HEAD already reflects completion.
- **B5** QA separately after B4. Browser D2, OAP-0.1 product integration, real museum assets, human approval and production publishing are all *future, separate authorization*.
- Existing B3 four typed primitives, 50-step cap, structured output only, no dynamic HTML/JS, external network and unrestricted tool execution. No implicit D2 UI features at B3.
- Research 3.8/3.9 offline Python reference tests ≠ Kiro product proof. No sealed 3.2 holdout identities/answer keys in this public doc or implementation prompt.
- Any code modifications must be unified diffs or exact SEARCH/REPLACE and include new files. No direct GhostWeb or BLINDSPOT modifications.

## Falsifiable acceptance outline

Critical P0: (1) trusted source/rights valid, (2) no privileged field injection, (3) linked factual feedback has a review state and explicit uncertainty, (4) demo source change invalidates affected Q/A/F or conservatively blocks everything, (5) altered/withdrawn media never silently remains public, (6) runtime caps and B0–B3 regression preserved, (7) English accessible judging demonstration matches actual app.

Measured product metrics: human task time, C1 direct-Opus JS vs C2 compiler paired safety/effort, education rating, changed-evidence review load, false blocks, source link coverage. Freeze original research 3.2 12-case + 2-negative/4-holdout/100-point C0/C1/C2 rubric, including compiler initial engineering cost as separate line. Never invent results or independent review.

## Contest packaging (official 2026 rules checked)

Submission cutoff: **2026-12-04 14:00 PST = 2026-12-05 07:00 KST**.
Working and unrestricted judge-testable app; public open-source OSI-licensed repository with root `/.kiro`; under-three-minute public demo video; English description or English translations; Kiro process evidence.
**Three equally weighted principal criteria**: Potential Value, Implementation, Quality and Design (not five).
Recommended candidate category **Frankenstein**, not selected or submitted.

Sources: https://kiroween.devpost.com/rules ; https://en.actionbound.com/museum ; https://www.axiell.com/solutions/product/cultureconnect/ ; https://metmuseum.github.io/

**STOP/approval boundary:** This is research-to-development alignment only. It does not authorize B4/B5/D2/AWS/cloud spend, unreviewed media redistribution, OSI license selection or public deployment.
