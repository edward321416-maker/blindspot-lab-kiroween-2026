# BLINDSPOT LAB — Phase 4 research gate / Kiro handoff

**Status: RESEARCH HOLD.** Not a Kiro-created or submitted app. This package includes a locally executed, zero-network CI gate prototype and a proposed Kiro Feature Spec for the next phase.

## Verified fixture
Exact 728-case JSON and independent-model oracle audit from the previously completed Phase 3 evidence package. `fixtures/cases.json` SHA-256 is pinned:
`41bb878ea72dec1caf239bff272eba2a93a2ba793eb5188db25a9ee18d829828`.

## Run (Python standard library; pytest only for tests)
```bash
python -m pytest -q tests/test_gate.py
python src/blindspot_gate.py \
  --cases fixtures/cases.json \
  --expected-sha256 41bb878ea72dec1caf239bff272eba2a93a2ba793eb5188db25a9ee18d829828 \
  --out evidence --mode research
```
**Expected exit code: 1** because 38 new regressions are correctly found. `exit 2` means invalid or tampered input; `exit 3` means technical PASS but attempted production approval is blocked. A `0` in research mode does not establish production suitability.

## Evidence outputs
- `evidence/gate_verdict.json` — summary, conditions, two separate release states.
- `evidence/gate_cases.csv` — deterministic per-case decisions and hashes.
- `evidence/gate_junit.xml` — CI-readable 38 failures and 1 skipped case.
- `reports/` — PDF/HTML planning report and viewer.

## Key safeguards and limits
- Only recomputes bbox/prediction consistency from Phase 3 records, does not load stored models or infer on new images. Does not verify pixels against `image_hash` unless raw image bytes are separately available.
- `oracle_audit.json` previously checked rendered synthetic masks but is NOT independent real-human verification.
- A JSON review ledger only checks syntactic quorum; offline tool cannot authenticate reviewer identities. Therefore production approval intentionally stays BLOCKED, even for test rows claiming reviewers.
- Competition credits are available per previously user-shared screenshot, but **this package used no Kiro credits**; no Kiro CLI authenticated in this container.
- No GitHub push, branch, deployment, paid API, AWS resource, or personal images involved.

## Handoff
Open the project in Kiro. Review the draft `.kiro/specs/blindspot-regression-gate/requirements.md`, `design.md`, `tasks.md`, steering rules and proposed hook. Do not implement unchecked product tasks until same-user need and real-model evidence pass.
