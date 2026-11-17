# Re:Collection — B5 audit and Research 3.12 alignment (2026-11-18 KST)

**STATUS:** B5 technical QA COMPLETE **KIRO_USER_REPORTED**; `GO_FOR_D1E_PREP` **planning only**. Real D1E, user-facing output, publisher, D2 and deployment remain **HOLD**. This public GitHub document is NOT an independent audit of the unpushed Windows repository.

## Exact source basis

- User-attached B5 report: 284-line `Re:Collection D1-BUILD B5 기술 QA 보고서`, pasted 2026-11-18 about 00:04 KST. Original Kiro-generated files/diff remain in user's Windows local filesystem and have not been byte-inspected here.
- Source GitHub (read at this docs branch before authoring): `22_PLANS/RECOLLECTION_3_11_ARCHIVE_DETECTIVE_PRODUCT_BLUEPRINT_20261117.md`; `24_PLANS/RECOLLECTION_3_12_CONCRETE_PRODUCT_INTERACTION_CONTRACT_20261117.md`; `20_ALIGNMENT/RESEARCH_3_9_OAP_REFERENCE_RETEST_20261117.md`; existing B4–B5 docs.
- Research 3.11 and 3.12 are **product PLANNING**, not changes already accepted to frozen `ExperienceSpec v0.2` or a Kiro code-implementation authorization. Research 3.12 standalone HTML 17/17 browser checks are a **prototype-only** result, NOT a tested Kiro renderer, actual real-source rights, or a functioning publisher.
- Protect embargoed 3.2 holdout/evaluation answers, unpublished 3.7–3.9 research oracle, rights-sensitive artifacts; publish none here.

## Local development evidence, user/Kiro-reported only

- History B0 `6367d928...` → B1 `21a2ce5...` → B2 `54f88b5...` → B3 `4c4dc7a...` → B4 `09f4b8a...` → **B5 `b112c6a93c715e027a8ad3155f35a667f5260396`**.
- Local `main`, clean worktree, no remote, linear ancestry, `git fsck` exit 0, reported Kiro same-model QA 67 inference events `claude-opus-5.5`; effort remains `SESSION_CONFIG_ONLY`, **NOT** independently human-reviewed.
- B5 QA reportedly ran `node --test --test-reporter=tap "tests/**/*.test.ts"` twice and post-commit: **164 executions / 164 pass** each, 135 unique test titles and 536 observed assertion calls; normalized digest `0452a87078b475cfcb0ee904702d87aa2b4a43e2b335902775029d83398e45d1`; B4 evidence SHA `3bcb03e5616cc8ad426389b25cd977881c43e46f3dc54537de8f7ffcd928fba3` reproduced.
- B4 case counts: **23 distinct scenarios = 3 executed (F1-01, F2-01, F3-12), 20 refused**. F3-12 was **not blocked**: irrelevant actual quote can be accepted and rendered as “Recorded fact” while `historicallyVerified=false`. This is a real unsafe epistemic/UI implication even if synthetic tests expected it.
- Historical diff byte-provenance: B0–B3 old files `LEGACY_DAMAGED` due to PowerShell encoding; B5 produced distinct `REGENERATED_FROM_GIT` UTF-8/LF/no-BOM copies without modifying old reports or git commits. Current full SHA values and manifest are local-only, not independently checked here.
- B5 no product source/test logic changes, only QA docs/evidence + README/tasks; B5 diff reportedly SHA256 `60e4dad7aa58b3823a9fd887d36b80d7ed5a2d4fa4f86280bda890a817151025`.
- `TYPECHECK_NOT_RUN`, `BONUS_USAGE_UNOBSERVED`; original cumulative soft/hard compliance **NOT VERIFIED**. Previous user rejected repetitive `/model` and `/usage` prompts. Do not demand screenshots as a generic per-stage gate.
- Kiro's checkpoint log is **local `PENDING_SYNC`**, not synced by Kiro to Google Sheets. A separate ChatGPT execution-log entry is distinct from that local backlog.

## Defect disposition and scope decisions

| Issue | B5 evidence/status | Immediate disposition | Beyond this patch |
|---|---|---|---|
| **B5-01** fact assertion can match one byte/space, contradict source, nevertheless show `Recorded fact` | **P1 VERIFIED IN KIRO REPORT** | **BLOCK visitor output/publication**. No “source-bound = fact true”; until reviewed, use `SOURCE_LINKED_UNVERIFIED` not `RECORDED`. Minimum quote length alone does **not** prove entailment | New output policy, reviewed quote/text bound to immutable source and curator/human evidence |
| **B5-02** AI-authored title/questions/compare labels/suggested evidence reach visitor | **P1 actual design gap** | Block user-facing unreviewed strings. Output sink inventory for proposed versioned adapter | Proposed OAP-0.1 research rules subject to authorization, negative+benign tests and security review |
| **B5-05** getter/proxy mutable caller object violates 50-step cap, 121/200 observed | **P2 classified by Kiro under JSON-only threat model; violated invariant for untrusted in-process caller** | Proposed targeted **snapshot-bound runtime length check**, fail before execution | Scope malicious in-process object protection explicitly and test, don't assume 50-step universal until patched |
| **B5-06** repeated getter reads within B2 `validate()` can produce spoofed VALID report; B3 currently revalidates | **P2 current boundary, P0 if future consumer blindly trusts report** | Proposed **single-snapshot / strict plain-JSON or byte-parsed boundary** to bind verdict and hash | No future publisher can use detached validation report as authority |
| **B5-07** B4 evidence script digest produced from later re-read; supplied hash arbitrary string | **P2 provenance** | Proposed digest of actual **executed** script snapshot, strict 64-hex input format, regen evidence | Must not falsify old report hashes; new report version and explicit migration |
| **B5-08** executed vs completed and metadata status semantics | P2 | Record ambiguous semantics, propose v2 evidence field after critical fixes | Approval/publication separate |
| **B5-17** 164 executions/135 unique test names | P2 QA attribution | Prefer new machine-readable unique test IDs and preserve old TAP / baseline digest; avoid renaming 164 existing frozen tests without versioned evidence | QA ergonomics |
| **B5-03** benign overblocking (22/48) | P2 usability | **DEFER**; R3.5 security policy change requires separate approval and attack-vs-benign regression | No unsafe-text bypass without approval |
| **B5-11** NoC-US source excerpt laundering into an `UNKNOWN` string | P1 synthetic rights hypothesis | **BLOCK real media, visitor output**; investigate per-sink rights provenance after output contract approved | Rights evidence + text derivation lineage, manual review |
| **B5-24** missing claim→choice→branch→feedback closure | P1 research gate | Keep research-only; no feedback primitive sneak-in | Versioned dependency contract and independent oracle |
| **B5-25** research product object count gap | Pending L2 decision | **No immediate B1 migration**. Research 3.11 explicitly sets **2–4 items as FIRST vertical slice**, avoiding the older 3.0 3–8 aspiration conflict for prototype | Long-term 3–8 product contract separate |
| **B5-04/B5-09** dangerous rendered text/state labels absent current browser | INFO that can become P0/P1 in D2 | UI/publishing remains BLOCKED until typed output contract, safe renderer and state gating | D2 design approval |

**Key correction:** `GO_FOR_D1E_PREP` does not mean `D1E_EXECUTION_APPROVED`. Human independent holdout author/oracle, rights reviewer, preregistered arms/budget and credit permission are still unassigned. The same-model B5 QA is more credible than self-review but not blinded human evaluation.

## Research product convergence (3.11–3.12)

- **Hero slice:** 2 synthetic source records, one learning objective, *two* evidence-linked questions, change-aware review state. This matches the **existing 2–4-object prototype count**; the broader 3–8 product target is a *later* versioned contract, not a B5 blocker.
- Research 3.12 illustrative files `ARC-01`, `ARC-02`, source-status mutation and media-rights revoke/restore, review state `DRAFT → NEEDS_REVIEW → APPROVED → PUBLISHED`, `STALE_REVIEW/BLOCKED` **are fictional prototype concepts**, not authorized implementation, actual GitHub/Kiro code, production approval or media-rights enforcement.
- Research 3.12 claimed 17/17 browser prototype checks and output DTO/API proposal; it uses synthetic-only hardcoded data and separate local simulated approval. Don't port a prototype `APPROVED` UI flag as security authorization. Bridge must use current B3 structured output and a **new separately accepted output-policy adapter** after the B5 defects are addressed.
- Research 3.9 OAP is a researcher-built Python reference (38 self-oracle cases × 2, five initially bypassed sinks, then revised reference blocked). **Not an independent standard nor approved Kiro source**, but important for threat-test design.

## Recommended sequential action

1. **D1E_PREP planning now**: freeze scientific hypotheses, selected direct-Opus and compiler arms, human-independent holdout/rights role requirements, budget estimates and NO-EXECUTE checklist. No Kiro source mutation or sealed eval data sharing.
2. **B5.1 PATCH ONLY AFTER USER AUTHORIZATION**: narrowly repair B5-05/B5-06/B5-07; optional B5-17 unique test-ID add-on. Write explicit security regression oracle before code; no R3.5 text-rule changes, no schema/object-count widening, no OAP or D2 adapter. Keep originals and test evidence immutable; generate versioned new artifacts.
3. **B5.2 product-output policy architecture**: different user decision, P1 B5-01/02/11 and 3.9 OAP/3.12 proposed output sink contract; visitor/browser/approval remains HOLD before authorization and independent review.
4. **D1E execution** separately approved only after fixed security gates, independent human holdout/oracle, real rights if assets used, preregistration, and fresh credit budget authorization. No automatic switch from D1E_PREP to execution.

**Next user high-impact question:** approve a **B5.1 scoped security patch** (existing local main branch only; package-zero Node24, regression tests and reversible evidence only), or keep development in D1E_PREP read-only. Merely sending this source report was NOT approval for new code changes.
