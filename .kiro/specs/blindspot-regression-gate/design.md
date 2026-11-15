# BLINDSPOT LAB — Proposed technical design (subject to gate)

## Validation work done in Phase 4
- The reference **728 synthetic** Phase-3 cases are imported from their unchanged, SHA-pinned JSON artifact.
- A zero-network Python stdlib CLI re-evaluates image metadata, GT boxes, A/B predictions and stored verdicts. It emits JSON/CSV/JUnit with deterministic case IDs and fails CI on new regressions.
- All extracted fixture data are explicitly flagged `synthetic_provenance`. The CLI does **not** load arbitrary `.joblib` files, does **not** inspect original image pixels, and cannot authenticate reviewer identities.
- `technical_gate=FAIL` and `production_approval=BLOCKED_UNVERIFIED_ORACLE` are intentionally separate states.

## Proposed demo UI (only after GO)
`Upload evidence / pick provided fixture` → `Oracle audit review` → `A/B change matrix` → `Failure explorer` → `Download CI packet`.

The UI initially renders a **precomputed** evidence bundle in the browser, with clear demo/synthetic labels. No customer image data or model weights are uploaded to a public server. The canonical evaluator is Python; if browser-side calculations are added, parity tests against the Python engine are mandatory.

## Proposed components
1. `Gate Core` — pure Python detector comparison contract and independent score recalculation.
2. `Oracle Registry` — source/provenance, human review workflow, label validity and uncertainty; external reviewer authentication is a *future integration*, never inferred from names in JSON.
3. `Artifact Auditor` — content hashes; model, image and transformations provenance. File content must be available and independently hashed to verify claimed image hashes; standalone metadata cannot prove real images.
4. `Replay Runner` — later support a pinned ONNX/torch detector adapter in a sandboxed, no-untrusted-pickle process. Not implemented here.
5. `Release Gate` — fail-closed policy with JSON report and JUnit/XML CI status; policy must be preregistered and reviewable.
6. `Demo UI` — browser-first report explorer; for Kiroween use React/Vite/TypeScript for UI + Python CLI to produce signed-off evidence packet. No hosted inference initially.

## Data envelope v0
- Case: `case_id`, `scene_id`, `image_sha256`, `gt bbox (xyxy) / negative`, `oracle_status`, `oracle_source`, `transform`, `severity`, `A/B {present,score,bbox}`, `model_hash_A/B`, `min_iou`, `annotation_review_id`.
- Provenance: source content digest; dataset license, review type, source of boxes, model artifact digest; no unverifiable identity claims.
- Outcome: `PASS_BOTH`, `FIXED`, `NEW_REGRESSION`, `FAIL_BOTH`, `ABSTAIN_ORACLE`; **not** a safety certification.
- `technical_gate` and `production_approval` separately derived; no external real-world approval API in Phase 4.

## Security and cost
- No secrets embedded in code or public test fixtures; do not copy personal Kiro credit redemption URL into source.
- Default to local-only data processing; reject executable uploads and untrusted pickles.
- No AWS resources, GPU services, paid APIs, auto overages or deployment without user approval.

## Relevant upstream art
- FiftyOne detection evaluator and community model-comparison plugin already have hit→miss and miss→hit diagnosis; reuse or integrate rather than claim originality.
- Kiro Feature Specs use `requirements.md`, `design.md`, `tasks.md`; steering in `.kiro/steering/`; hooks in `.kiro/hooks/`.

## Technology decisions (provisional)
- Research/CLI: Python 3.11+ standard library; pytest only for tests.
- UI demo after selection: Vite + React + TypeScript (static client; no paid cloud dependencies); no committed stack migration yet.
- Once real model adapter is justified: ONNX Runtime pinned after license, security and benchmark review; not silently installed.
