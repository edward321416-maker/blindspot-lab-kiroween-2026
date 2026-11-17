# Re:Collection — Execute B1 on completed B0 (user-directed continuation)

**Date:** 2026-11-17 KST  
**Status:** USER REQUESTED PROGRESSION TO B1 — bounded implementation only.  
**Supersedes:** The repeated pre-B1 `/model` and `/usage` screenshot requests in `13_WORKFLOWS/D1_BUILD_B0_COMPLETE_B1_USAGE_GATE_20261117.md` and the earlier B0 resume document. **All other scope, safety and no-cloud restrictions remain active.**

## 0. Why this packet exists

The user explicitly said: **"아니 왜 자꾸 MODEL 이랑 USAGE를 원하는 거야 그냥 진행해"** ("Why keep asking for model and usage? Just proceed"). The operator's desired model and accounting baseline were already provided. Repeated manual checks have blocked delivery; do not ask for the same screenshots again at each stage. Treat this as authorization to execute **B1 only within the previously authorized D1-BUILD scope**, not permission to spend unlimited credits or initiate D1E/D2.

This is a new, affirmative user direction to continue from completed B0. Do not interpret a prior local report's B0 stop condition as authority to overwrite existing work.

## 1. Worktree and model starting point

Local workspace (already populated):
`C:\Users\admin\Projects\recollection-kiroween-2026`

Expected local:
- branch `main`
- full B0 commit `6367d928b7eb17a4bd8b6283690bc7c265fa875b`
- clean, no remote
- prior B0 frozen oracle: 29 validator cases, 6 runtime cases, 13 integer-only JCS vectors
- 3 guard tests two passing runs, per Kiro report.

Confirm only **read-only Git status/commit and source inventory** at start. If different, do not reset, stash, rebase or overwrite; explain the actual conflict. **Do not recreate B0, refreeze its oracle, initialize another repository or modify existing B0 commits.**

Use existing Kiro configuration `claude-opus-5.5` / `max`, **no Auto and no model fallback**. Do not switch models. Do **not** ask the user again for /model screenshots. The session config is evidence of settings, not a guarantee of per-turn execution; report `SESSION_CONFIG_ONLY` if that is the only observability. If the running environment explicitly indicates a different model, STOP rather than silently using it.

Protected projects are untouched: GhostWeb reportedly dirty `23b8a010`; BLINDSPOT reportedly unpushed `c073ddd1`. No fetch/checkout/stash/reset/commit/push in either.

## 2. Cost discipline without repeated user-gated measurements

Existing **user-observed** Kiroween bonus-pool accounting baseline = **513.26 / 4000 used** (2026-11-17 around 15:02 KST). D1-BUILD global agreed incremental allowances: +220 soft => 733.26 bonus used, +300 hard => 813.26 bonus used. These are **fixed cumulative ceilings** across B0–B5; they must not be silently reset. Note that current cumulative usage after B0 is not observed.

User has explicitly directed to proceed **without repeated interactive /usage requests**. Therefore:
- Do not claim any precise current pool usage or that the original hard cap was actively verified if it was not.
- Do not pretend `Credits: turn/session` equals `/usage`.
- If usable /usage observations are already available without prompting the user, record and apply them. Otherwise mark `BONUS_USAGE_UNOBSERVED` and report **cost-cap enforcement is uncertain**.
- Execute **B1 only**, one controlled implementation/test pass with a small bounded debugging loop; do not autonomously chain B2–B5. The prior B1 planning envelope was +70 credits (an estimate, **not** an instrumented hard budget). Prefer shorter, reproducible unit tasks to expensive retries. If session counters or available actual readings indicate unusual consumption or near-cap risk, stop and report.
- At B1 end, disclose that the original global credit cap may be unverified without updated /usage. Do not initiate subscriptions, overages, cloud, paid APIs or model fallbacks.

## 3. B1 required deliverable: ExperienceSpec v0.2 contract (NO B2 features)

**Read B0 frozen sources and actual oracle first**. Build from exact existing cases, not reconstructed memory:
- read `AGENTS.md`, applicable `.kiro` steering/specs and local D1 contract;
- inspect tracked `package.json`, `requirements.txt`, `docker-compose.yml` if present **as text**, not executed;
- inspect `oracle` fixtures (29 validation cases, 6 runtime scenarios, 13 JCS vectors), SHA manifest and B0 test runner before altering source;
- inspect `rg` / `grep` signatures/field paths before reading full direct-modification functions.

### B1.1 Schema and trust boundary
- Define explicit `schemaVersion: "0.2"`, reject `0.1`, other versions and unknown properties.
- AI-authored input is limited to `claims`, `plan`, `graph` (plus explicitly defined safe version/meta fields); it **cannot** include `verification`, `curatorApproval`, `approval`, `publication`, `publishStatus` or system-owned hashes. Any such field must cause a deterministic `PRIVILEGED_FIELD_FORBIDDEN`, even if nested in an unexpected location where the schema disallows it.
- System-generated evidence, verification and future approval/publication schema definitions remain separate; **do not implement the actual approval engine or publication**.
- Define exact source asset references and evidence claim kinds `HISTORICAL_FACT`, `EDUCATIONAL_MODEL`, `INFERENCE`, `UNKNOWN`. No hallucinated truth checking in B1; semantic source/rights verification belongs to B2.
- Bound string lengths, array counts, graph shapes and nesting; fail closed on unsupported structures, prototype pollution field names or disallowed types.
- 2–4 object release policy remains a **schema proposal**; trusted test-harness-only `UNIT_SMOKE` permits one synthetic object but AI output may not set this flag. No public artifact is created.

### B1.2 Canonical hash
- Implement **only the agreed integer-only JCS / RFC 8785 subset**; reject floats, negative zero (where represented), non-finite numbers, unsafe integer representation or unsupported Unicode if the frozen contract demands it. Document how JSON parser behavior affects duplicate keys and precision. No pretending native `JSON.stringify` is automatically full JCS.
- Check key ordering/canonicalization and UTF-8 bytes against the **13 frozen B0 JCS vectors** before accepting a PASS. Verify matching SHA-256. Preserve input bytes and oracle hashes.
- Provide deterministic error IDs and traceable differences for invalid inputs.

### B1.3 Tests and provenance
- Implement from the existing B0 oracle; 29 validation cases and 13 JCS vectors are not to be silently reduced/redefined. The 6 runtime cases may be used as contract fixtures but B3 runtime isn't authorized here.
- Add negative tests for fabricated privileged fields, unknown keys/versions, malformed graph, unsupported JCS data, input mutation and artificial single-object publish bypass.
- Run actual B0 guard tests and all B1 tests **twice**, log exact commands, exit codes and stable results. Distinguish `PASS` from `NOT_RUN`.
- No mandatory npm installs: Node 24 built-in TS type-stripping is runtime support, **not static type checking**; record `TYPECHECK_NOT_RUN` unless separately approved TypeScript checker actually exists. Do not add Ajv or TypeScript package without explicit approval.
- Changes must be reported as **unified diffs or exact SEARCH/REPLACE**, including new files. Create one local B1 commit on current local `main` once tests pass, leave worktree clean, do not push or add a remote.

## 4. Hard prohibitions

- No redoing B0, changing frozen oracle or source provenance;
- No touching GhostWeb/BLINDSPOT;
- No GitHub remote, public publishing, cloud/AWS/Bedrock, external museum imagery;
- No optional npm install or paid service;
- No D1E A/B competition, D2 curator/editor/publisher, or B2–B5 execution in this task;
- No claiming independent human validation or release readiness from synthetic fixtures.

## 5. Required final Korean B1 checkpoint

Report concisely:
1. Actual local branch, original B0 SHA, new B1 commit SHA and clean/dirty state;
2. Implemented file inventory with design boundaries and unified diff path;
3. Frozen oracle SHA unchanged, 29/13 cases with per-case outcomes, B0 guard tests twice;
4. Actual test commands, exit codes, deterministic report hashes, known failures;
5. Model/effort **as observable** (session config vs effective per-turn), no repeated screenshot request;
6. Existing credit baseline 513.26, available observed new readings if any, otherwise `BONUS_USAGE_UNOBSERVED`, planning-vs-measured limits;
7. B1 `PASS / CONDITIONAL / FAIL`, explicit security/schema gaps and next **B2 proposal**, not execution.

**Then STOP.** The user wants measurable coding progress, not another D0 or B0 approval loop.
