# Repository map and import policy

```text
blindspot-lab-kiroween-2026/
├─ .kiro/
│  ├─ steering/guardrails.md         # imported draft, improve in Kiro
│  └─ specs/blindspot-regression-gate/{requirements,design,tasks}.md
├─ AGENTS.md                         # project policy
├─ apps/web/                         # reserved: Kiro-built new UI (not yet present)
├─ packages/engine/                  # reserved: Kiro-built new engine (not yet present)
├─ research/reference/phase4/        # read-only snapshot of pre-Kiro experiment
│  ├─ src/blindspot_gate.py
│  ├─ tests/test_gate.py
│  ├─ fixtures/{cases,summary,oracle_audit,...}.json
│  ├─ README.md
│  └─ SOURCE_SHA256.json
├─ docs/{PROVENANCE,DECISIONS,REPO_MAP,KIRO_EXECUTION_PROMPT}.md
├─ docs/RESEARCH_AND_SOURCE_LOG.md
├─ .gitignore
└─ README.md
```

**Separation of concerns:** Don't treat prior Phase4 code as freshly authored Kiro app. Use its tests/fixtures as a golden reference. After research gates G1–G4 pass and the user approves GO, implement working application under `apps/` and `packages/` using Kiro specs, adding independent parity tests.

**Hooks:** Original Phase4 `python-verify.json` assumed `tests/test_gate.py` at repository root. It is intentionally NOT active in this seed because test paths moved under `research/reference/phase4/`. Kiro should propose a path-correct hook, test it, and enable it only after review. Never install a silently failing save hook.

**Committed content:** sanitized reference sources, hashes, draft specs, program policy; no sensitive camera images, copyrighted benchmarks without clear redistribution permissions, binary checkpoints, tokens or user email.

**App deployment and license:** not approved; do not create license until the user selects compatible terms and third-party licenses have been inspected. Official competition submission ultimately requires public repo + root `.kiro` + open-source license.
