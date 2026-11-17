# Re:Collection — Research ↔ Development Alignment Register
**Snapshot:** 2026-11-17 KST  
**State:** CROSS-CHAT ALIGNMENT PROPOSAL / NOT an accepted product-contract rewrite / NOT evidence of Kiro code execution

## 0. Trust and provenance

This public document is a *source-indexed impact summary*, not a repository of private research artifacts. Research sources were read through authorized project/Library content in a separate ChatGPT workspace context; their original bytes are **not hosted here**. The current Kiro Windows local commits and test outcomes are **USER-REPORTED** and must not be described as GitHub-synced code.

- **Source R-3.0:** `ReCollection_3_Product_Strategy_and_Experience_20261117.pdf`, 9 pages; directly reviewed as indexed text. States product/experience planning, not authority to change code or spend credits.
- **Source R-3.2:** `ReCollection_3_2_Adaptive_Experience_Research_Protocol_20261117.pdf`, 10 pages; directly reviewed as indexed text. H1–H5 research questions; model-vs-compiler benchmark still unexecuted.
- **Source R-3.2F:** `ReCollection_3_2_Corpus_and_Evaluation_Freeze_20261117.pdf`, 12 pages; directly reviewed as indexed text. A frozen research corpus and evaluation protocol exist, **NOT** evidence of completed model evaluation. IMPORTANT: research master/holdout/negative-case identities and oracle answers are EMBARGOED from development. Never copy source IDs, full corpus, oracle files or internal answer keys to this public branch or a Kiro implementation workspace.
- **Sources R-3.6/R-3.7:** Cross-chat planning updates are available only through prior conversation context, **NOT byte-verified research originals here**. 3.6 reports comparative dependency revalidation tests; 3.7 proposes claim-to-feedback evidence completeness with 12 falsification scenarios. Treat both as USER/RESEARCH_CHAT_REPORTED, and their conclusions as *research work*, not acceptance that Kiro shipped any such engine.

### Research maturity (do not overstate)
- Product target: **ARCHIVE DETECTIVE**, evidence-based investigation through photos/maps/records rather than a single Morse-device demo. Product design input in R-3.0 = **3–8 objects** with learning goal/rights; draft output 3–5-minute investigative program with traceable evidence and curator-approved publication link.
- Secondary experience: MECHANISM LAB (illustrative, physical-truth risk); NATURE FIELDWORK deferred expansion. These are *product planning priorities*, **not implemented modules**.
- Core differentiation hypothesis: **Evidence-to-Interaction Graph** joins source assets → evidence claims → relations → visitor interactions → feedback. Hypothesis is NOT experimentally verified as better than direct HTML/JS produced by Opus.
- R-3.2 evaluates H1 structure adaptation, H2 educational alignment, H3 evidence trust, H4 engine utility, H5 transfer/generalization. Genuine A/B execution and curator adoption are pending.
- Research 3.6 reported: full-rebuild comparison catches all 14 changes but triggers 15 unnecessary re-reviews, selective dependency graph misses 2 key dependencies. This is **context-reported**, not independently reproduced by this author. Do not silently code a selective invalidation algorithm based on it.
- Research 3.7 reported: 12 planned counterexample tests for evidence dependency completeness. Completion status = **DESIGN ONLY / NOT EXECUTED**, not 12/12 pass. Its principal risk—justified answer/branch/feedback depends on evidence beyond directly cited claims—must be tracked separately from basic B2 source ID/locator validation.

## 1. Known development checkpoint (only Kiro user report, NOT remote code)

- B0: local Re:Collection `main` `6367d928b7eb17a4bd8b6283690bc7c265fa875b`, frozen synthetic tests/oracle.
- B1: local `main` `21a2ce5c964e84a4eb1f9bd65845937a10aeb2eb`, `node --test` 62/62 PASS (Kiro report, not independently re-run here). Contract `ExperienceSpec v0.2`, claims/plan/graph schema, privileged output rejection, integer-only JCS.
- B2: **INSTRUCTIONS PUBLISHED, IMPLEMENTATION STATUS UNVERIFIED**. Frozen B2 execution plan is `15_WORKFLOWS/KIRO_B2_IMPLEMENT_EXISTING_B1_20261117.md` at the same docs branch's historical commit `019957be67e5e799085f636e7b1040115bb8b630`.
- GhostWeb dirty and BLINDSPOT unpushed remain separate/protected. Neither repo may be manipulated to implement Re:Collection.

## 2. Change impact matrix: research questions vs actual build stages

| Research delta | Source/evidence | Impact | Development action | Rationale / stop boundary |
|---|---|---|---|---|
| New HERO: ARCHIVE DETECTIVE instead of single-device lab | R-3.0 directly read, design decision | L1 design priority / potential L2 product demo contract | **KEEP** B1/B2 core; **REPLAN** future B3/B4 sample path toward multirecord investigation | Reusable evidence validator is shared infrastructure. Do NOT claim 3–5-min browser experience exists. |
| **Object count** product 3–8 vs existing D1 contract 2–4 | R-3.0 directly read vs prior D0/D1 decisions in GitHub | **L2 CONTRACT CHANGE CANDIDATE — USER DECISION REQUIRED** | **KEEP** frozen B0/B1 and B2 existing v0.2 validation; **FREEZE** any 3–8 public release claim; plan versioned contract/test migration before production or user-facing UI | Count alteration affects validation, performance, test corpus, user promise and UX. 2–4 D1 prototype cannot satisfy 3–8 product goal without separate test/proof. |
| Evidence-to-Interaction dependency closure, claims→feedback | R-3.0 principle + R-3.7 conversation-reported design | L1+ study; could become L2 once scored oracle accepted | **KEEP** B2 direct source/locator/rights gate; **PROPOSE TESTS** for indirect dependency closure, do not automatically rewrite B0 oracle | A source link to a single node does not prove all answer/branch/feedback dependencies were traced. |
| Source-change selective revalidation vs full rebuild | R-3.6 context-reported comparison | L1 research, L2 if accepted invalidation contract | **KEEP** B2; **REPLAN** only a later B4/D2 invalidation engine once independently tested | Selective graph reportedly missed 2 critical dependencies; do not deploy it as reliable without counterexample testing. |
| Research corpus/holdout frozen | R-3.2F directly read (research only) | L2 evaluation-integrity boundary | **FREEZE exposure** of heldout assets/oracle; use only developer-safe evaluation contract and public subset when formally released | Do not contaminate D1E by leaking research-master source identities/answers into the implementation prompt or public GitHub. |
| Better model/technique change | No accepted new evidence | L0 / NO CHANGE | **KEEP** Opus 5.5/MAX Kiro and synthetic-only D1-BUILD | No Auto fallback, no new paid model/cloud. |

**Decision status:** The *research direction* is updated, but **no user-approved modification to the already-frozen B0/B1 schema, acceptance oracle, D1 synthetic-only data perimeter, or per-stage budget** is shown. Do not mark L2 candidate as accepted; keep a visible pending decision.

## 3. Research Change Event (RCE) contract for ongoing alignment

Every materially new research decision should be recorded as a small event **before the next Kiro stage**:

```yaml
change_id: RCE-YYYYMMDD-NNN
source_title: ...
source_location: ...             # citation or verified GitHub SHA; do NOT include heldout secrets
source_observation_status: DIRECT_REVIEWED | RESEARCH_CHAT_REPORTED | MISSING
research_status: PROPOSED | ACCEPTED_FOR_PLANNING | ACCEPTED_FOR_DEVELOPMENT
impacted_requirement_ids: [...]
impact_level: L0 | L1 | L2 | L3
development_targets: [B1, B2, B3, B4, D1E, D2]
disposition: KEEP | UPDATE_TESTS | FREEZE | REPLAN
existing_contract_sha: ...
proposed_new_contract_sha: ...  # NONE until approved
user_approval_required: true
security_and_rights_risk: ...
oracle_leakage_risk: ...
next_owner: RESEARCH | DEVELOPMENT | USER
```

- **L0** informational: update documentation only, no code impact.
- **L1** additive: suggest a separate test/feature, keep current validated path.
- **L2** schema/oracle/threshold/rights change: freeze only affected work and ask for explicit accepted revision; preserve all earlier evidence.
- **L3** product direction pivot: freeze product-specific work, preserve generic modules, ask user before architectural rewrite.
- Never change frozen oracle to get a pass. Never treat a research draft, reported number or ChatGPT summary as executed product evidence.

## 4. Per-stage control: never let engineering drift from product research

Before next Kiro task:
1. Read the immutable stage plan *and* latest visible alignment/RCE snapshot in this public docs branch (read-only). Note exact reviewed Git SHA and which evidence is remote vs local-only.
2. Compare dependencies at field+requirement granularity. A documentation-only HEAD advance is not itself reason to halt coding.
3. For current **B2**, the decision is **CONTINUE** exact preapproved synthetic semantic validation only. Treat indirect dependency closure as an **OPEN RESEARCH GAP**, not a secretly added B2 PASS criterion. B2 must report the limitation.
4. After Kiro test, record actual local commit/full SHA and test exits. If local code is not pushed, report `LOCAL_ONLY` rather than `GITHUB_SYNCED`.
5. Feed implementation gaps back to Research as a concise question/negative test candidate; never share held-out cases/answers.
6. Reassess product count/hero changes at **B3/B4 design gate**, with user decision only for actual architecture/product/rights/cost impacts. No automatic D1E or cloud release.
7. Do not require repetitive `/model` or `/usage` screenshots merely to restate unchanged configuration. Preserve existing Opus5.5/MAX and fixed original bonus usage accounting baseline.

## 5. Reporting format for development-chat follow-ups

```text
Research snapshot: version/date/source, accepted vs proposed
Dev checkpoint: local HEAD / test result / remote availability
Alignment: task ID, L0–L3, KEEP/UPDATE_TESTS/FREEZE/REPLAN
Research gap: 1–2 concrete falsifiable questions
Safe next Kiro action: precise B-stage only and exclusions
Costs/model: actual/SESSION_CONFIG_ONLY/BONUS_USAGE_UNOBSERVED, never invented
```

No monitoring occurs automatically when this chat is idle unless a separate scheduled automation is successfully configured. No user local source code, AWS services, or GitHub product branch has been modified by this alignment document.
