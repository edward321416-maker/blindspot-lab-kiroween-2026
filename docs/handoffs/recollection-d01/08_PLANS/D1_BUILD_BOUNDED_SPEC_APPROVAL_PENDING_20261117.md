# Re:Collection D1-BUILD — bounded implementation specification (AWAITING APPROVAL)

**This is a PREPARED FUTURE SPEC. Reading it or pasting a Kiro prompt does NOT authorize implementation.** Re:Collection remains a product candidate, not the selected contest entry.

**Authoring basis:** D0.3 user-reported Kiro summary (not full local report bytes) and pinned public D0 priority Markdown, D0.2 decision review. The original Master Audit PDF bytes have not been independently read on the Kiro PC.

## Decision contract requiring explicit user authorization

Before any build:
- **Workspace:** inspect preferred isolated directory; create it ONLY with user approval, and only if absent. No code copied from GhostWeb or BLINDSPOT.
- **Scope:** approve D1-BUILD core only as below. **D1E and D2 are excluded**.
- **Stack:** existing Node 24 LTS, proposed TypeScript with Node built-in test runner. Need to pin and approve any new package versions (TypeScript checker, Ajv); prefer minimal dependencies. No forced Node26 upgrade. Inspect package.json/requirements.txt/docker-compose.yml as text if present.
- **Model:** Claude Opus 5.5 / MAX with no Auto/fallback; verify actual session selection. If only a saved config is available, log `SESSION_CONFIG_ONLY`.
- **Credits:** incremental soft **+220** and hard **+300** from a fresh user-observed `/usage` reading. These are new recommendations for **reduced** build scope, not user-approved limits and not observed consumption. At soft: stop and provide a tradeoff report; at hard: terminate task before continuing. Do not pool D1E.
- **Data:** only own synthetic objects/mock sources; no live museum media, site crawling, personal data or licensed external assets.
- **Git:** isolated local repository after approval, no GitHub remote and no publication without a separate approval.
- **Cloud:** zero AWS/Bedrock calls, credentials, resource creation or billing.

If any high-impact item is not explicitly approved, **preflight/read-only only**.

## Proposed file tree — NO FILES CREATED BY THIS DOCUMENT

    recollection-kiroween-2026/
      AGENTS.md
      .kiro/
        steering/product-boundaries.md
        specs/recollection-d1-build/{requirements,design,tasks}.md
      docs/
        decisions/
        provenance.md
        plans/
      packages/
        source-contract/
          src/
        experience-spec/
          src/
        evidence-validator/
          src/
        primitive-registry/
          src/
        experience-runtime/
          src/
      tests/
        fixtures/{owned-one-object,owned-two-object,unsupported-rights}/
        contracts/
        semantic/
        security/
        runtime/
      experiments/
        direct-build/           # RESERVED, NO D1E EXECUTION
        compiler-build/         # RESERVED, NO D1E EXECUTION
      apps/
        web/                    # RESERVED, NO USER-FACING APP IN D1-BUILD
      reports/
        evidence/
      package.json              # proposed once approved
      lockfile                   # proposed only if dependencies installed

## Stages and acceptance criteria

### B0. Source lock and worktree safety — estimated maximum 30 credits
1. Verify the approved scope/permissions, current `/usage`, effective model, local path emptiness and allowed dependencies.
2. Initialize standalone repository ONLY if approved. Preserve earlier GhostWeb and BLINDSPOT untouched.
3. Freeze the approved self-contained D1-BUILD spec, explicit exclusion list, synthetic test oracle and original-handoff limitations. Version and hash all inputs.
4. **STOP** if the user has not approved directory creation/local repo or if /usage is unavailable.

### B1. ExperienceSpec v0.2 contract — estimated maximum 70 credits
1. Enforce `schemaVersion`, separate **AI-owned** `claims`, `plan`, `graph` from privileged **system-owned** `verification`, `curatorApproval`, `publication`.
2. Unknown fields rejected by default. `v0.1` migration is **UNKNOWN** until original v0.1 bytes are inspected; reject unsupported versions, do not invent migration.
3. Define `SourceAsset` rights/media and `EvidenceClaim` kinds `HISTORICAL_FACT|EDUCATIONAL_MODEL|INFERENCE|UNKNOWN` with exact claim locators.
4. Use explicit integer-only JCS canonicalization subset and provided test vectors; no truth or rights inference from hash equality.
5. Tests: type validation, trust-boundary tests, hash determinism, schema mismatch, fabricated privileged records.

### B2. Evidence-bound semantic gate — estimated maximum 70 credits
1. Verify fact locator/source ID, immutable source hash, missing/unknown handling, bounded numbers, finite graph, allowed transition edges.
2. Fail closed on missing rights or unknown media license; D1 uses only owned synthetic mock rights.
3. Missing factual evidence must yield `NEEDS_MORE_EVIDENCE`, no invented source claim.
4. Prohibit prompt-injected content from influencing validator config, tools, publishing or filesystem.
5. Tests for stale citation, wrong claim kind, forged approval, missing rights and path/URL abuse.

### B3. Restricted primitive runtime — estimated maximum 70 credits
1. Implement **only** the frozen allowlisted primitives that have exact semantics in approved spec (do not invent unspecified ten types from summary).
2. No `eval`, `Function`, arbitrary dynamic JS, HTML or remote code from model output.
3. Put an upper bound on graph depth/nodes/steps/output and refuse invalid type edges.
4. Tests: deterministic execution, finite steps, blocked prohibited primitive, invalid node connection, no network/unsafe file reads.

### B4. Controlled smoke/evidence output — estimated maximum 40 credits
1. Single-object synthetic smoke is enabled **only by test harness**, not an AI field; cannot be published.
2. Two-object synthetic E2E verifies source/claim graph and restricted interaction; it is **not a real museum or human evaluation**.
3. Produce clear machine-readable schema/test/rights/evidence results. Keep verification/approval/publication record schemas but **do NOT implement real curator log/UI or publisher**.
4. Run reproducible `node:test` twice and compare exact canonical evidence outputs.

### B5. Internal independent QA and handoff — estimated maximum 20 credits
1. Separate fresh Opus 5.5/MAX session with source-level challenge tests; **same-model review, not cross-family or independent human oracle**.
2. Classify P0/P1/P2, report measured versus estimated costs, record full local commit SHA, test commands/results and model settings/credit readings.
3. Deliver D1-BUILD outcome GO_FOR_D1E_PREP / HOLD / REWORK. **No D1E or D2 implementation**.

Sum of per-stage hard envelopes = 300 credits. A stage's unused allowance is not automatic permission to exceed the global hard cap.

## Explicit separation from D1E A/B benchmark

D1E has not been approved. Future experimental requirements:
- both arms use **the same Claude Opus 5.5/MAX** in separate sessions/workspaces and receive the same frozen sources, rights, learning goals, budget/time/attempt limits;
- Direct Build arm cannot inspect B Compiler implementation or evaluation outputs;
- independent **human** writes/locks holdout/oracle before testing and rights reviewer clears each actual asset;
- Case A one-object smoke cannot be counted as evidence of 2–4 item user workflow;
- **2 runs per case** preregistered before outcomes, distinguish repeated trials from independent samples;
- report initial B construction cost versus marginal repeat-case cost, total time, critical evidence/rights errors and tested browser behavior;
- the previously reported `55/55` deterministic synthetic pass is not an AI superiority result.
- D1E early estimated 60–120 credits for one pass; two runs might approximate 120–240 (unverified and not budget authorization).

## Stop conditions
- Unauthorized workspace write, npm install or Git operations.
- User-visible /usage unavailable before a measured credit-capped run.
- Effective model not verifiable or Auto fallback is active.
- Missing/uncertain rights for any non-synthetic asset proposed for publication.
- Comparator contamination, unauthorized third-party data, unsupported v0.1 migration, violation of privileged-field separation.
- Any P0 security failure, unsupported primitive that cannot fail closed or model-authored approval record.

## Go/Hold policy
- Current: **HOLD** (proposal and budget NOT approved).
- After specific authorization, B0–B5 may be executed within hard caps, recording actual results.
- D1E remains **separate HOLD** until human/oracle/rights, prereg and credits approved.
- Product selection and public release remain **UNDECIDED**.
