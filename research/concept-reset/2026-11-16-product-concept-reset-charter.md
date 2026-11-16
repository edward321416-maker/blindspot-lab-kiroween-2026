# Kiroween 2026 — Product Concept Reset Charter v1
**2026-11-16 KST · IDEA PLANNING ONLY · product UNSELECTED · Kiro dev branch untouched**

## 0. Why the old search stalled

BLINDSPOT LAB began with an interesting "AI failures as interactive experiments" idea. After three iterations, the primary question became "can the same anonymous user demonstrate an incumbent failed after adoption?" That is a useful enterprise validation requirement but not a sufficient **idea-generation engine**. Generic model A/B failure inspection, reviewed-label regression suites, and CI release gating already substantially overlap FiftyOne and Roboflow Workflow Evals. The original Phase4 benchmark found 38 new regressions in **synthetic data**, not unique field value. Preserve all provenance; do not rebrand research fixtures as contest app results.

**Reset decision:** Pause expansion of ChangeScope, TenantGuard and Pipeline Twin. Do not delete results, overwrite or alter existing Kiro specs, or assume the current repository name fixes the submitted product. Only after a user decision can a new app begin.

## 1. Contest contract (official primary source)

- Submission deadline: **2026-12-04 14:00 Pacific / 2026-12-05 07:00 KST**.
- **Five equal judge criteria, each 20%:** Potential Impact, Technological Implementation (effective Kiro use), Design, Innovation/Idea, Presentation. It is NOT enough to demonstrate clever research without a coherent product.
- **New working software built using Kiro** during 2026-10-30 to 2026-12-04; clearly disclose pre-existing ChatGPT research code.
- Public functional demo URL, GitHub public source + root \`.kiro/\` + visible open-source LICENSE, public YouTube demonstration **under three minutes**, written Kiro workflow explanation.
- Categories: Resurrection, Frankenstein, Skeleton Crew (requires two separate functioning example apps), Costume Contest. **Frankenstein is only a provisional interpretation**, not an approved category.
- Official: https://kiroween.devpost.com/rules

## 2. The non-negotiable idea center

**Create → Investigate → Apply to reality**: An interaction that yields a falsifiable, inspectable artifact, not a chat answer, screenshot-only interface, or fake generative physics animation.

Every candidate must answer exactly:
1. **WHO** does what concrete job? Not "everyone is curious".
2. **WHAT INPUT** does the user provide in the first 15 seconds?
3. **WHICH INTERVENTION** can they change themselves?
4. **WHICH COMPUTATION** recomputes a verifiable physical/geometric/optimization state instead of hallucinating an output?
5. **WHICH ARTIFACT** can be replayed/shared and used outside this conversation?
6. **WHAT IS ALREADY SOLVED** by the strongest real incumbent?
7. **WHAT DOES A TWO-PERSON TEAM ACTUALLY SHIP** before Dec 4 with one supported scenario?

The unique engine is **a proposed technical mechanism**, not patented novelty, market proof, or a claim that a rival cannot implement it.

## 3. Concept A — RealityLab: "질문이 실험으로, 실험이 현실 검증으로"

### Person / moment
A first-year engineering or science learner asks: "같은 재질의 선반인데 왜 길이를 늘리면 훨씬 더 휘지?" A GPT answer or static animation does not let them test a prediction against an independently specified physical model.

### A single bounded user journey (illustrative; NOT user-validated)
1. Choose a shelf/cantilever scenario from validated templates; enter span length, cross-section, material assumptions, and load, with units and confidence.
2. AI converts the question to a **typed experiment contract** (\`model_family=linear_elastic_cantilever\`, variables, bounds, assumptions, what changes/holds fixed).
3. User moves the length slider or load position. A deterministic beam model computes deflection; two runs are compared. A test oracle checks units, monotonicity and analytic reference.
4. Optionally upload a user-measured deflection from an actual simple experiment; compare prediction vs observed with measurement uncertainty.
5. Export a **replayable experiment receipt**: inputs, formula/model version, predicted result, observed reading (if any), residual error, assumptions/limits and unsupported cases.

**Proof kernel proposed:** question→restricted experiment schema→unit/assumption validation→analytic solver→intervention search→observation comparator. For a cantilever tip load, \`delta=F L^3 /(3 E I)\` under small-deflection linear elasticity; doubling L at fixed other properties yields 8x predicted tip deflection. This is **not professional structural certification** and cannot infer material properties reliably from one photo.

**20-second wow:** A length slider changes a physically computed shape and the displayed ratio 2× length → 8× deflection. A real calibrated measurement (if available) gives a residual, not just AI narration.

**Minimum viable scope:** **ONE** cantilever/shelf family, validated numerical input, slider, 2D deformation plot, numeric comparison, assumptions, saved experiment. Explicitly not a universal prompt-to-world model nor unconstrained code generation.

**Direct rivals / falsification:** Google's 2026-09-17 generated teacher interactives already support AI-generated guided physics simulations; PhET has existing variable-control simulations; 2026 Phys. Rev. Physics Education Research published experiments with AI-generated simulations. Therefore "AI makes interactive simulation from text" is not unique. The proposed incremental value is **correctness/units + calibrated real measurement + source/proof receipt**. If it cannot be shown using at least one measurement and standard solver comparison, product claim weakens.
- Google: https://research.google/blog/the-future-of-practice-enabling-teachers-to-create-learning-interactives-with-generative-ui/
- PhET: https://phet.colorado.edu/
- 2026 peer reviewed https://doi.org/10.1103/s8dy-kqy5

**Primary unknowns:** Learner would actually perform or enter a real measurement; reliable input calibration; Google GenUI can also support safeguards. Must not suggest one demo is a general physical reasoning breakthrough.

## 4. Concept B — ConstraintForge: "설계 변경이 터뜨린 제약, 최소 수정 경로와 검증 근거"

### Person / moment
A junior engineer working on a precast double-wall detail moves a sleeve opening or embedded fitting and asks: "이 변경으로 어떤 배근/피복/간격 규칙 후보가 깨지고, 가장 적은 수정으로 어떻게 해결하나?"

### Bounded user journey (synthetic construction detail only, never borrowed confidential files)
1. Load a **synthetic 2D PC double-wall segment** containing a shell outline, vertical reinforcement bars, sleeve openings and configurable **demonstration-only** clearances.
2. Drag a sleeve; geometry engine recomputes collisions and clearances from actual coordinates.
3. Generate an **unsatisfied-constraint witness** listing object IDs, minimum separation and parameters.
4. Search a bounded set of allowable moves/sizes; list up to three feasible lowest-change alternatives, showing unchanged requirements and the precise changed objects.
5. Export before/after schematic, constraints, chosen repair, verification log and exact input JSON so a reviewer can replay.

**Proof kernel proposed:** geometric contact/separation computation + explicit constraint graph + bounded optimization/minimal-repair search + verifiable before/after proof. AI translates the verbal job and explains trade-offs; **AI must not invent geometry results**.

**20-second wow:** Move the sleeve into an existing bar → red violation marker → a feasible 24 mm illustrative change suggestion appears → after choosing it all *modelled* rules pass and export shows why. 24 mm here is a **toy geometry example**, not a real engineering rule.

**Minimum viable scope:** one 2D parametric synthetic segment, three object types, three user-supplied design constraints, a single-object move, enumerate and verify repairs. No Revit plugin, IFC import, full 3D meshing, all PC bar detailing, real building standard certification or automatic approval.

**Direct rivals / falsification:** Autodesk Model Coordination already automatically detects object clashes, issue tracking, and supports many formats; Solibri checks rule-based constraints and records issue severity. A basic "AI finds clashes" app is a clone. Only a **bounded minimum-change remedy with explicit proof and verified constraints** might create differentiated value. A direct parity review must check if existing authoring tools and available rule-checkers already generate the same repair.
- https://help.autodesk.com/cloudhelp/ENG/Coord-About/files/About_Model_Coord.html
- https://www.solibri.com/articles/solibri-release-notes-june-2026

**Risks:** proprietary engineering/IFC files, technical detail domain specificity, inability to certify code compliance. Each clearance threshold must be user-configured unless independently tied to a verifiable standard. Cannot market as verified code-compliant structural design.

## 5. Concept C — MaterialQuest: "탄소를 줄여도 기능 조건을 위반하지 않는 교체안"

### Person / moment
An early-stage building designer wants to change a specified material to cut embodied carbon **without invalidating functional-equivalence requirements** or comparing incompatible EPD units.

### Bounded user journey
1. Start with a synthetic one-assembly bill of quantities, units and user-configured functional class/strength criterion.
2. Candidate material EPDs can be compared **only if declared units/boundaries and functionality are compatible**.
3. User changes one constraint (allowable class, embodied-carbon target, procurement constraint); a discrete constrained search recalculates feasible alternatives.
4. Show a Pareto comparison with missing data, EPD uncertainty and no-solution states; prohibit “lowest carbon” claims for incomparable products.
5. Export a provenance-aware selection report with source IDs, units, conversions, assumptions and invalid options.

**Proof kernel proposed:** functional-equivalence validator + EPD unit normalization + bounded multiobjective Pareto search + provenance and confidence accounting.

**20-second wow:** A very low-carbon candidate is rejected because its performance category/declared unit differs; a feasible alternative appears with an explicit estimated difference and source trace. For the concept viewer, all numbers are **synthetic illustrative numbers**, not EPD measurements.

**Minimum viable scope:** one assembly/category, 6–12 synthetic or licensed EPD-like rows, a verified unit converter, constrained discrete comparison and source/uncertainty banner. No real procurement recommendation, structural certification, Scope3 all-emissions accounting, unlicensed bulk EPD downloads.

**Direct rivals / falsification:** Building Transparency EC3 already provides free open EPD comparisons, material quantities, alternate products, uncertainty and project emission targets; EC3 2.0 beta released 2026-10-20. "Carbon calculator" and basic EPD ranking are **not** novel. Require evidence that EC3 cannot express the intended cross-product functional constraints or that our solver reduces a measurable specific job; otherwise NO-GO.
- https://www.buildingtransparency.org/tools/ec3/
- https://docs.buildingtransparency.org/ec3/main-features/find-and-compare-materials
- https://www.buildingtransparency.org/ec3-2-0-modernizing-open-infrastructure-for-embodied-carbon/

**Risks:** true function equivalence needs subject matter verification; production EPD dataset license/API terms; many EPDs cannot be compared directly.

## 6. Fair decision table (QUALITATIVE FORECAST, not measurements or score)

| Criterion | A RealityLab | B ConstraintForge | C MaterialQuest |
|---|---|---|---|
| First 15 seconds demo clarity | High | **High** | Medium |
| User-specific specialized pain evidence | Medium/uncertain | Medium/uncertain (field expertise useful; external evidence needed) | Medium/uncertain |
| Technically testable own core in 2 weeks | **High** with one analytic model | **High** with simplified 2D solver | Medium (EPD rights, functional units) |
| Strong existing product overlap | **High** Google/PhET | **High** Autodesk/Solibri | **Very high** EC3 |
| Replayable falsifiable output | High | **High** | High |
| External permissions/data needed for honest MVP | Low | Low synthetic | Medium |
| Potential architecture interest/visual demo | High | **High** | Medium |
| Risk of claiming unsafe professional authority | Medium (physics approximation) | High (engineering rules) | High (false EPD/procurement equivalence) |

**Research exploration recommendation (NOT a product decision):**
- Primary 24-hour technical proof: **B ConstraintForge** because a visibly different *computational repair/proof* can be shown using licensed-free synthetic geometry and a tight 2D solver. Hard competitor constraint: must be more than clash detection.
- Parallel short competitor/measurement check: **A RealityLab**. If a minimal actual real-world observation and trustworthy model receipt are achievable, A may become stronger in general audience appeal.
- **C MaterialQuest** held as backup, not concurrently built. EC3's direct feature overlap makes differentiation expensive.
- Existing BLINDSPOT LAB / Phase4 evidence remains an **archived reference**, not a stealth fourth entrant or assumed Kiro-built app.

## 7. Stop searching, start testing: 72-hour concept decision contract

**2026-11-16 (today):** lock three concept pages and 3-minute demo storyboards; confirm existing competing official functionality. NO app development or Kiro credits used in this *planning* response.

**2026-11-17:** produce or separately authorize **one paper/spec technical proof each for A and B**, not broad architecture; before coding, write:
- A: reference deflection equation, explicit units/assumptions, test \`delta(2L)/delta(L)=8\` within numeric tolerance, invalid input rejection, evidence from one measured example **if legitimately available**.
- B: 2D synthetic geometry + one intersection, exhaustive candidate offsets with a deterministic minimal valid move, reproducibility hash, deliberately infeasible constraint case.
- Compare each with strongest specific incumbent job and what user can do **after** the interaction.

**2026-11-18:** gate review with (i) non-LLM reference result, (ii) first 20 sec understood without a prompt, (iii) unit/constraint checks, (iv) clear difference from the incumbent native function, (v) output useful outside chat, (vi) two-person implementation scope.

**By 2026-11-19 KST:** select a finalist only with user approval after seeing both scenes. A fail can shift to B, B fail can shift to A; if both fail, choose *one* focused alternative rather than re-running an endless micro-niche literature scan. A pure research result or E2 scarcity cannot indefinitely postpone selection.

**Engineering calendar if a candidate receives approval** (planning, not a scheduled background task):
- Nov 20–26: Kiro creates a NEW actual application core + spec/contracts/property tests (source/provenance tracked); freeze one scenario.
- Nov 27–30: polish complete UX, error cases, replay receipt, 3-minute demo.
- Dec 1–3: independent black-box review, full setup from clean clone, credits and license/publishing rights, demo and submission.
- Dec 4 by 18:00 KST: final production/readback and submission with buffer; official absolute deadline **Dec 5 07:00 KST**.

Do not ask Kiro to implement a product until the user selects the concept. Kiro account credits are Kiro credits, not USD.

## 8. Acceptance/failure gates — no infinite research loop

**Pass/continue** only if:
1. A first-run, no-login demo can show **one user input → one action → recomputed outcome → export** in 90 seconds.
2. A non-LLM computation has an independent analytical/geometric/optimization test with known expected result and at least one invalid/uncertain-state guard.
3. The feature central to the pitch is **not** already available as an equivalent core function of the strongest incumbent, or a measurable better job outcome is specified.
4. The entire MVP is achievable with one domain, one solver, one export and no third-party private data.
5. At least one concrete user job and an expected practical output are described. Actual market demand is **UNVERIFIED** until supported.

**No-Go / narrow**:
- Any candidate relies on fake physics, general-purpose image-to-world accuracy, invented building-code compliance, unlicensed product EPDs, or requires an unfinished external model.
- A central function merely generates an HTML mini-game that ChatGPT/Google already creates, identifies an overlap that Autodesk already detects, or ranks EPDs already compared in EC3 without credible extra functionality.
- New requested feature expands 1 use-case MVP into all of physics, all BIM, or all Scope3.

## 9. Demo storyboard contract

Each must provide 5 beats inside 180 seconds:
1. **Problem:** identify person and frustrating decision in ≤20s.
2. **Input:** one real/synthetic explicitly labelled source in ≤20s.
3. **Core engine:** show visible state change / solver output in ≤45s.
4. **Uncertainty / failure:** display unsupported or invalid state with no fake PASS in ≤30s.
5. **Proof / application:** export a reproducible receipt plus test/implementation explanation in remaining time.

No copyrighted music, third party images without license, fabricated real deployments, or simulated customer metrics posing as actual field results.

## 10. Final product-selection decision record (still blank)
- Product chosen: **NONE**.
- Which user scenario won (A/B/C): **UNDECIDED**.
- User-approved repository rename, architecture, license, deployment budget: **NOT AUTHORIZED**.
- Kiro dev branch changed: **NO**.
- Are the concept HTML sliders/tables actual production benchmarks? **NO — concept-level toy illustrations only.**
- Exact comparative runtime performance: **NOT MEASURED**.
- Competitive novelty and end-user demand: **HYPOTHESES**.

**Preserve this charter and judge all subsequent research by whether it changes A/B/C selection or MVP design; otherwise STOP.**
