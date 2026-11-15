# Phase 4 decision checkpoint — 2026-11-15 (KST)

- Candidate: BLINDSPOT LAB / Blindspot Regression Gate (research priority, **not** selected product).
- Current actual experiment: Phase 4 reevaluation of **existing** Phase 3 synthetic A/B outputs. No new model training or live camera inference.
- Fixed input: 728 cases / 727 oracle-valid / 1 abstain; A→B fixed 57 / new regression 38 / both fail 2 / both pass 630.
- Executed gate: 18/18 automated tests passed. CLI research gate exit code **1** (intentionally failing due to 38 regressions). Separate simulated scenario of zero regressions and unverified oracle returns exit code **3** in production mode.
- No human-signed external oracle; no physical user/customer evidence; no direct FiftyOne runtime head-to-head yet. `production_approval=BLOCKED_UNVERIFIED_ORACLE`.
- UX proof: offline HTML viewer filters 728 case decisions, including 38 new regressions and 37 glare regressions, exports JSON. Checked at 390/768/1024/1440 widths with no page JS error or overflow.
- Source competitor fact: FiftyOne's plugin already supports hithit, hitmiss, misshit, missmiss and localization deterioration categories; comparing two models is **not new**.
- Draft Kiro specs created; actual Kiro software not invoked, **no competition Kiro credits consumed by this work**. Credit registration was verified previously by the user's screenshot; current balance not independently refreshed.
- Formal Kiro app, cloud deploy, GitHub publish, external customer interview, paid API and submission **not performed**.

## Next branch
1. G1 ethically licensed real annotated frames + two independently recorded reviewers (external proof of identities and adjudication) — needed before real-world validity claims.
2. G2 real detector model A/B + pinned preprocessing + replay.
3. G3 same-task FiftyOne baseline benchmark with measured time, correctness and configuration overhead.
4. G4 same user/organization with failure of incumbent workflow.
5. If G1-G4 pass: use Kiro spec and credits in timeboxed app implementation. Else pivot/no-go before consuming most credits.

## Honest evaluation
- A locally executable **research gate** now exists and can be handed to Kiro as spec + reference tests.
- Competitive differentiator and contest-winning quality are **unproven**; synthetic A/B comparison does not demonstrate customer adoption.
