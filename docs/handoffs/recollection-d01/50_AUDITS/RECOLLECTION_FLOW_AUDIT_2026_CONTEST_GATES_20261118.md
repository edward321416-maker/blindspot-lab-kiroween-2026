# Re:Collection — product/development/research flow audit before D2-V1B

**2026-11-18 KST** · Decision: **CORRECT COURSE / GO ON BOUNDED AUDIT, HOLD THE OLD THREE-INDUSTRY D2-V1B IMPLEMENTATION PLAN**. This is an independent planning audit of the exact prior 3-page PDF, exact GitHub docs 3.11/3.12, D1E plan, D2-V1A checkpoint, D2-V1B proposal, live-indexed 2026 Kiroween official rules, and current competitor descriptions. It is **not** a Kiro Windows source review, a new user approval for code, or a release authorization.

## 1. Why the earlier plan is incomplete

### Technical evidence, genuine but narrow

- D2-V1A local user/Kiro-reported SHA `ca941c5748c0c20a11144fd4f1a83da9e85c7a00`: **291/291 Node** twice plus postcommit; **24/24 developer-defined cases**; **17/17 final Edge browser QA**, preceded by one actual browser QA failure from a static label leaking a rights-revoked field, then fixed; mutation **15/16 killed**, one asserted equivalent but not independently proved. Local code/diff, 15 original screenshots and original 4-page Kiro PDF have **not been independently reviewed in this chat**.
- Two question texts come **only from fixed trusted fictional editorial fixture**. Visitor can select evidence/choices and observe source/rights invalidation; the B5.2 model-authored question case still produces `NEEDS_REVIEW` and zero visitor blocks. This is credible *demo editorial integration*, **not generalized AI source→experience authorship, historical truth, real rights, real curator approval or a full learning-outcome measurement**.
- `D2-V1A` re-issues reviewed-demo receipts after *re-basing* B5.2 inputs on a fresh source snapshot and restarting the rights-history baseline. No actual bypass has yet been proved, but the audit risk is material. Multi-tab state shared, old model claims still blocked, some static UI text rights-leak happened in first browser QA; mutation equivalence remains unproved.
- Main project current model provenance only `SESSION_CONFIG_ONLY` and Kiro bonus credits `BONUS_USAGE_UNOBSERVED`; don't conflate 291 automated tests with 291 independent evaluation cases.

### Product and contest-gap truth

- Research 3.11 museum educator promise: **official source→claim→ExperienceSpec→visitor question/choice/feedback→source change→re-review** (first 2–4 items). Current model question/provenance generation, factual relevance verification, feedback, human authentic approval and real rights are not proven. No fair comparison to plain GPT or museum authoring tools has run.
- Existing market tools **already make museum experiences, quizzes and educational collections**. See [Actionbound museum](https://en.actionbound.com/museum), [Axiell CultureConnect](https://www.axiell.com/solutions/product/cultureconnect/), and [Smithsonian Learning Lab](https://learninglab.si.edu/). Do **not** claim these tools lack a given change-aware feature without actual feature-level tests. The plausible differentiator is *source/rights version-bound editorial review and automatic stale-experience refusal*, **not quiz generation**.
- Previous D2-V1B proposed *three novel industrial-domain packs* (transit/inspection/environment). Those test generic architecture but divert attention from the museum-specific hero and contest deliverables. Avoid making three unrelated demos a prerequisite for one polished 3-minute product pitch.

## 2. IMPORTANT: current 2026 contest rules, not cached 2025 rules

Official current 2026 indexed page **updated Nov 16, 2026**: https://kiroween.devpost.com/rules . Older cached URL opens can surface the **2025** edition with 3 equal criteria; **Research 3.11's “Three equally weighted principal criteria” is outdated for 2026**, despite its matching deadline. The 2026 source defines **FIVE equally weighted criteria, each 20%**:
1. **Potential Impact**: genuine audience/problem/usefulness/accessibility.
2. **Technological Implementation**: effective and strategic use of Kiro IDE/CLI/Web/Crew/specs/hooks/steering/MCP/PBT.
3. **Design**: a complete, coherent polished experience, **not just a technical proof of concept**.
4. **Innovation / Idea**: novel combination, distinctness from current offerings.
5. **Presentation**: end-to-end demo video and compelling understandable pitch.

**Hard requirements per 2026 rules:**
- Submit by **2026-12-04 14:00 PST = 2026-12-05 07:00 KST** (approximately 16 days from this report); no late extension.
- Working functional application **URL** available for free judge evaluation through judging period ending **2027-01-29 13:00 PST**; current `127.0.0.1` is not externally accessible to judges.
- **Public GitHub (not another Git host) repository**, complete runnable source/assets/install instructions, approved **OSI open-source license** and visible root `.kiro`. The existing **multi-project public docs branch is NOT a public Re:Collection app repo**; private local Kiro main has no remote. Don't mix GhostWeb/BLINDSPOT source or research-private datasets.
- Public YouTube demo **under three minutes**, real device/app functionality; English submission text/video or English translations and setup/testing directions. Attribution/third-party images/media must be rights clear.
- Project must be **new since Oct 30, 2026**; verify Git commit ancestry/date and dependencies, don't infer eligibility from project name.
- Category options: `Frankenstein` plausibly best as one integrated source+policy+compiler+browser learning workflow; **provisional, not user-selected**. `Skeleton Crew` specifically requires two separate application folders and two applications, so three input cases inside one app are NOT automatically enough. `Costume Contest` requires outstanding UI as primary angle, not a workaround for missing product functions.
- Optional **Best Student Project** bonus may be relevant only if user meets documented current enrollment and requested proof, not inferred as won.
- Current 2026 rules can change; verify again in a logged-in browser before final submission. Do not use cached **2025** rules for current judging factors.

Official rule source: https://kiroween.devpost.com/rules ; event main: https://kiroween.devpost.com/ .

## 3. Corrected strategic goal and one repeatable user story

**Product identity, proposed:** “Evidence-aware interactive exhibit builder: educators can assemble a two-source investigation with traceable question text, show it to visitors, and detect when a changed or revoked record requires review before display.” This is an **assisted and controlled** workflow, not magical historical truth verification.

**One 2–3-minute judge demonstration sequence:**
1. Curator/editor chooses **two owned fictional museum records** (ARC-01/ARC-02) and a learning goal.
2. **Evidence→experience**: clearly identify whether the questions were fixed editorial text, model-proposed, or authored in UI. Existing two questions remain fixed templates unless a genuine separately approved Kiro/model authoring step is implemented; no covert “AI-generated” label.
3. Visitor explores two sources, sees two **demo-editorial-reviewed** questions, selects evidence and gets neutral feedback (“choice recorded”, not truth judged).
4. Editor changes source field or revokes rights, causing an on-screen **provenance path** to turn stale and visitor question/quote output to vanish; restoring rights requires new demo review.
5. Show concise evidence digest and the actual B5.2/R3.5 fail-closed decision. Do not show actual public “APPROVED” state or non-existent user review.
6. At least one unfamiliar **museum-related synthetic pair** replaces ARC-01/02 without case-specific code changes; it may require new owned safe fixture JSON and editorial review, but must not need source-code branches. Capture reproducible runtime evidence, curation steps and false blocks.
7. Kiro specs/steering/hook/test evidence explains how the complex safe path was built.

**Differentiator hypothesis test:** On the same **one source correction or rights revoke**, compare direct Opus-generated standalone experience against Compiler with the same inputs/time/attempt limits: (i) stale/unsupported content revealed, (ii) required editor actions and elapsed time, (iii) valid source-field connections, (iv) UI functionality. A paired **small technical demo** is not a fair human evaluation by itself. Future D1E product-scored comparison still needs independent human evaluator, masked holdout, precommitted metrics and budget.

## 4. Prioritized gates (replaces old sequential D2-V1B industrial-pack direction)

| Gate | Goal & work | Stop / pass standard | Implementation permission |
|---|---|---|---|
| **G0 submission viability** | Inventory local source license/IP/third-party assets, `.kiro` specs/hook/steering, executable startup, repo packaging, judge access URL, YouTube+English plan and category; verify post-Oct30 history | One complete checklist with **owners**, unresolved public/license/hosting decisions explicitly flagged; do not publish or expose code yet | **Planning only now** |
| **G1 trust boundary** | Read-only focused review of ADR-0009 rights-history rebase and browser labels/aria/hidden sinks; 2-tab stale review/receipt replay and equivalent mutant explanation | If real fail-open, **HOLD** for separately approved minimal patch; if not found, document evidence and demos' limits | Read-only audit scope first; source edits need approval |
| **G2 product-value slice** | One **unfamiliar museum-style two-source fixture**, no hardcoded ARC-01/02 assumptions, same versioned UI compiler/review path; measure authoring/re-review, retain two-question story. Distinguish manual editorial text from model proposal. | New pair runs through exactly same code with synthetic-only materials, correct invalidation; no “model-generated” claims without actual calls; published source still HOLD | **New local implementation/credits approval needed** |
| **G3 comparison/readiness** | Small, preregistered direct-Opus versus Compiler *same-task* test and one external viewer/educator walkthrough, if reviewer/time available | Evidence of at least one measured differentiator, not manufactured win; absent human evaluation labelled `NOT_TESTED` | Experimental model calls, budget and independent reviewer need separate consent |
| **G4 submission release** | English product copy, working and judge-accessible app/test build, public standalone GitHub/OSI license/`.kiro`, <3-minute YouTube video, final smoke test | Exact public links, license, judge-testability and end-to-end video verified; submissions before KST deadline | PUBLIC SOURCE/LICENSING/HOSTING/NETWORK require explicit user approval |

**Priority:** Do not build three industrial packs before G0/G1 and the one museum-style novel pair. Timebox future technical broadening. If the new case works but there is no external app and no public repo/video by Dec4, the project may fail submission despite 291 automated tests.

## 5. Specific design corrections before D2-V1B

1. **Baseline/rights semantics:** immutable source and rights *event history* must not be erased when a demo re-baselines to a new verified snapshot. New editorial receipt ≠ legal rights renewal. If history is demo-only, label and keep it separate; no automatic source approval.
2. **All output sinks:** button labels, `aria-label`, hidden text, tooltips, alt and titles can leak rights-revoked content. `textContent` prevents script execution, **not inappropriate data disclosure**. Browser regression must test full DOM/accessibility tree and late/revoked transitions.
3. **No fake “independent QA”**: old 291 tests and 24 public cases are developer-generated; 15 screenshots and local D2-V1A PDF were not transferred for independent visual reading. New screenshots should be actually inspected if submitted.
4. **No claim generation sleight-of-hand**: static trusted questions are legitimate for a synthetic demo but do not demonstrate the proposed AI authoring engine. To prove repeatable authoring, create new fixture and trace its exact question origin, time/cost, review actions and source connections. Avoid auto-trusting Kiro/model output.
5. **No automatic historical correctness feedback**. Future genuinely reviewed claim-entailment and indirect dependency closure are separate risks.
6. **No broad real-source collection as precondition**: Met A two submitted raw JSON payloads passed offline integrity, but independent live TLS origin and publication rights remain unresolved; the collector `COMMITTED` marker verifier patch was replay-tested 37/37 in an isolated copy but not yet applied in the user's Windows collector at that snapshot. This research is independent from the product demo and should not delay synthetic submission.
7. **No silent public repo**: the user must decide OSI license and exposure of current local engine code. Publish only to a clean, separate repo after metadata/secrets/rights/license audit; public hosting of a demo is likewise a distinct approved architecture/security step.

## 6. Explicit decisions needed later

- **Product/IP and OSS**: Is releasing the isolated Re:Collection implementation as OSI-licensed public GitHub acceptable? If yes, which license after ownership and dependency review?
- **Demo access**: locally served only cannot satisfy 2026 judge access. Decide a safe public judge-testable deployment/test-build approach with no privileged claims or third-party media, alongside resource/cost/attack surface.
- **Next stage model spend**: later G2 and G3 model usage budget separately authorized; no inference that previous D2-V1A credit approval persists.
- **Contest category**: tentatively Frankenstein; no Skeleton Crew claim unless two distinct applications actually submitted in separate repo folders.
- **Human/review trust**: synthetic demo-only review vs real authenticated curator must be explicit; user has NOT authorized live auth.

## Final audit verdict

**D2-V1A technical workflow is coherent and has real reported security integration; the roadmap from that point is not contest-optimal.** GO for **G0 submission requirements and G1 bounded trust inspection**; MODIFY D2-V1B to focus a fresh museum archival case and evidence of authoring value; HOLD three industrial cases as optional cross-domain research; PREP G4 immediately, but no public code/URL/license until user approval; keep D1E scientific comparison separate. Claims remain conservatively labelled `USER_REPORTED` wherever local Windows bytes are unavailable.

**No local Kiro code changes, additional paid model calls, public source push, actual hosting or submission were made in authoring this audit.**
