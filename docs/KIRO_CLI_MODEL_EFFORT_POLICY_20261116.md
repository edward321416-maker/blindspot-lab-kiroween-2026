# BLINDSPOT LAB — Kiro quality-first model routing policy (2026-11-16 KST)

**Decision:** Choose the most suitable model for each task based on correctness, tool-use reliability, and independent review quality, not lowest credit cost. The user's Kiro account visibly has 4,000 Kiroween bonus credits, and the user confirms **Claude Opus 5.5 is selectable**. Do not mistake 4,000 Kiro credits for US$4,000. Other premium models, including GPT-5.6 Sol, remain **availability-unverified** until the live CLI model picker confirms them.

**Scope:** Private GitHub handoff → separate local workspace → evidence verification → research/architecture planning. Product remains **RESEARCH HOLD**; this is not approval to implement or deploy a contest app. Keep prior ChatGPT research attributed as reference material.

## Quality-first role matrix

| Task and expected deliverable | Primary | Effort target | Independent checker / fallback | Why this fit |
|---|---|---|---|---|
| 0. Private repo + local workspace, Git authentication boundary, integrity checks and safe Git init | **Claude Opus 5.5** | **high** | Sonnet 5.5 high; if unavailable, Opus high | Reliability and careful scope preservation outweigh small routine cost |
| 1. Research gap, assumptions, measurable product hypothesis, incumbent comparison, original evidence ledger | **Claude Opus 5.5** | **high**, escalate **xhigh** for conflicting evidence | Sonnet 5.5 high | Conservative reasoning and evidence-aware decisions; web claims need verified sources, not fluent text |
| 2. Formal oracle validity, abstention, threat model, failure taxonomy, acceptance criteria | **Claude Opus 5.5** | **xhigh** | **GPT-5.6 Sol high** if selectable, else Sonnet 5.5 high | Highest priority: avoid conflating model predictions with independently validated ground truth |
| 3. Architecture & Kiro Spec requirements/design/tasks for a testable MVP | **Claude Opus 5.5** | **xhigh** | GPT-5.6 Sol high if available; otherwise Sonnet 5.5 high | Multi-system design, safety invariants, Kiro artifacts and clear contracts |
| 4. Multi-file engine implementation and long-horizon terminal orchestration **only after separate GO** | **GPT-5.6 Sol**, if actually selectable | **high** or **xhigh** if picker supports; else model native | **Opus 5.5 high** is mandatory independent review. If Sol unavailable, Opus 5.5 xhigh implements, Sonnet 5.5 high reviews | Kiro recommends Sol for difficult spec-driven terminal work and Opus for sustained architecture & self-verification |
| 5. Deterministic regression/CI integration, GitHub Actions, reproducible packaging **only after GO** | **GPT-5.6 Sol**, if selectable | **high** | Opus 5.5 high | Multiple tools/steps plus exact failure codes. No LLM substitutes for tests |
| 6. UI implementation, accessibility, export flows and 3-minute demonstration **only after GO** | **Claude Sonnet 5.5** | **high** | Opus 5.5 high on design-critical decision/demo | Efficient scoped implementation, iterative UX and documentation; visually inspect actual render |
| 7. Routine docs, isolated fixes, test-fixture wiring | **Claude Sonnet 5.5** | **medium** (high if tricky) | Opus 5.5 high only for disputed failures | Focused implementation; do not use expensive thinking where measurable outcomes do not improve |
| 8. Independent release candidate audit and model-vs-model discrepancy review **only after GO** | **Opus 5.5 xhigh** AND **GPT-5.6 Sol high/xhigh** where accessible | see preceding | If Sol unavailable, independent Sonnet 5.5 high + deterministic regression | Different model families reduce correlated assumptions, but do not prove independence of datasets/ground truth |

**Never call a self-reviewed result “independent” solely because it is the same model with a second prompt.** An independent check must have separate tests, evidence, and a reviewer model not simply accepting the author’s conclusions.

### Model availability / control
- Confirm exact active names with `/model` in the user's **live** Kiro CLI, not from this document. If Sonnet 5.5 or GPT-5.6 Sol is unavailable, follow fallback explicitly and report it; do not upgrade subscriptions, enable overages or claim these models were used.
- `/model` selects models interactively; `/effort high` changes the session (not necessarily a persisted global default). The model picker displays supported effort choices. Never invent model IDs, and never ask agents to auto-change active models if the CLI cannot.
- **Opus 5.5 supports low/medium/high/xhigh/max at the provider level**, but only set what Kiro's active picker exposes. Opus 5.5's provider default effort is **medium**, so explicitly choose high/xhigh for important work where supported.
- Reserve `max` for a demonstrably unresolved correctness/security issue AFTER high/xhigh failed and after setting a bounded task/query budget. Do not automatically use max for every request.
- Don't select **Auto** for benchmark comparisons whose model identity is essential; an unknown routed model weakens reproducibility. Auto is an acceptable operational fallback if the user explicitly permits it, recording it as Auto rather than a guessed model.
- Model-specific routing may require **separate sessions or a user selection**. At each phase boundary, Kiro should stop, state the intended next model and effort, and report the actual selected values after switching.

### Credits: protect quality, avoid unbounded retries
- Promo 4,000 credits are not dollars; Kiro quotes relative model multipliers against Auto. Official current documentation indicates **Opus 5.5 2.0x**, **Sonnet 5.5 1.3x**, and **GPT-5.6 Sol 4.4x up to 272K context tokens and 8.8x above that** (check live Kiro pricing before relying on charges). These do NOT predict exact credits for a task.
- Initial GitHub/local bootstrap may use **at most 100 newly consumed Kiro credits**, checked with `/usage` before and after each major segment. This ceiling is an operating limit, not a cost prediction. Stop if reached. The other credits remain for user-approved research/engineering and competition finalization.
- Prefer Opus on difficult decisions despite higher cost; do not repeatedly rerun expensive reasoning without new evidence or failing test.
- No paid upgrades, overages, cloud provision, new account registration, broad permissions, destructive shell commands, public release, or production approval.

## First session: required execution order
1. In Kiro CLI, run `/usage` and `/model`; verify Opus 5.5 availability and set **Opus 5.5 + high** (where supported).
2. Read `docs/START_HERE_KIRO_CLI_20261116.md`, `docs/REMOTE_KIRO_BOOTSTRAP.md`, `AGENTS.md`, `docs/PROVENANCE.md` from this private GitHub handoff.
3. Clone the existing private source branch into separate temporary staging; verify source SHA and all files, including dotfiles, then create distinct local project folder **without modifying research repo main**.
4. Re-run historical Phase 4 tests: prior baseline 18/18, 38 NEW_REGRESSION and expected intentional blocked production verdict. Measure again; don't reinterpret intended exit code 1 as false failure.
5. Initialize isolated local Git repo. **Ask for exact user approval of owner/name/private visibility and source inventory before creating/pushing a new private remote.**
6. Report observed model, actual effort, test results, hashes, absolute paths, observed credit delta. No app building during bootstrap.

## Task-specific quality gates (future)
- **Oracle**: ground truth is independent from model output; invalid/ambiguous labels => ABSTAIN; no automatic production approval.
- **Model A/B**: reproducible checkpoints, exact dataset/license, deterministic evaluation and per-condition regressions, CI nonzero on blocking cases.
- **Competitive novelty**: compare to actual FiftyOne/Roboflow behavior on same tasks; marketing copy is not benchmark evidence.
- **Demonstration**: actual executed model results, no simulated benchmark presented as production performance.

## Sources and dates
- Kiro model descriptions (updated 2026-11-12): https://kiro.dev/docs/models/available-models/ and https://kiro.dev/docs/models/
- Kiro CLI model/effort persistence: https://kiro.dev/docs/cli/reference/slash-commands/ and https://kiro.dev/docs/cli/chat/settings/
- Provider model effort semantics: https://platform.claude.com/docs/en/build-with-claude/effort
- Source project: `edward321416-maker/urban-intelligence-os-research`, `handoff/blindspot-kiro-20261115` branch
