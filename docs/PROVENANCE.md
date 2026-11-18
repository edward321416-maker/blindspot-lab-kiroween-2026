# Source provenance and attribution

| Material | Creator/provenance | Present role | May claim Kiro-built? |
|---|---|---|---|
| Earlier Phase2/Phase3 experiments | Pre-Kiro research, developed through ChatGPT assistance (2026-11-15) | Historical evidence, not code baseline for new app | NO |
| Phase4 Python gate, fixture, 18 tests | Pre-Kiro ChatGPT research package (2026-11-15) | Reference-only and independently testable | NO |
| Phase4 `.kiro/specs` and steering | Draft generated outside Kiro on 2026-11-15 | Kiro planning input; Kiro changes tracked in commits | NO, until actual Kiro contributions |
| GitHub/local bootstrap | ChatGPT-authored imported research and handoff documents; Kiro CLI 3.3.0 performed isolated local workspace setup, Git import, checks, and private remote push on 2026-11-16 | `C:\\Users\\admin\\Projects\\blindspot-lab-kiroween-2026`; `chore/kiro-repo-bootstrap`; initial verified push `3fba8e0` | Bootstrap activities performed in Kiro, but NO contest application has been built |
| New `apps/` + `packages/` | Not started | Candidate contest software pending explicit GO | Only after Kiro actually builds/tests it |
| Re:Collection 3.17 Met A marker-validator patch | OpenAI Codex local validation session (2026-11-18); public branch contains sanitized code, tests, diffs and measured logs only | Research-only security evidence; raw Met responses and complete HTTP captures remain local | NO |

The official rules require newly created projects, meaningful Kiro usage, and disclosure of reused existing code. Track each new work item, Kiro session, change, commit and test in `docs/DECISIONS.md` or `docs/KIRO_BUILD_LOG.md` once implementation begins. Do not backdate or misattribute.

## 2026-11-18 Re:Collection Met A validation evidence

- Evidence path: `docs/recollection-evidence/3.17-met-a/` on the isolated branch `evidence/recollection-met-a-20261118`.
- Baseline 32/32 and patched 37/37 standard-library tests passed; the five additional cases cover strict four-line marker validation.
- Two local Met A captures validated `True` without modification. Only response SHA-256 values and a sanitized result record are public.
- No raw responses, complete `capture.json` files, `COMMITTED` files, review ZIP, authentication material or institution images are published.
- This work was performed with OpenAI Codex and is not evidence of Kiro product implementation.

## 2026-11-16 verified handoff checkpoint

- New private repository: `https://github.com/edward321416-maker/blindspot-lab-kiroween-2026`; verified private with default `chore/kiro-repo-bootstrap` at initial commit `3fba8e013cf6389744a9306a8d02626c434f66af` and tree `c1fd28244d5db46ad1f960c0b029d29c4abd1f77`.
- Kiro CLI 3.3.0 imported and checked the pre-existing data without altering historical fixtures. Test evidence: all 13 hashes, 18 pytest cases, intentionally blocking gate with 38 new regressions. Current data and `.kiro` drafts remain pre-Kiro research rather than Kiro-authored app implementation.
- First initial clone and validation reportedly used Auto; later Git synchronization used `claude-opus-5.5` at max effort, differing from policy target high. A separate model/effort change by user is pending.
- No `main` branch, license, deployment, purchased cloud infrastructure or public release. Do not make original research evidence into claimed real-world oracle validity.

## 2026-11-16 publication and model-effort authorization

- The user explicitly approved `claude-opus-5.5` with `max` effort and PUBLIC visibility for **this single contest repository**. Earlier `max`-versus-`high` policy discrepancy is resolved as a policy decision; retain the historical record that bootstrap ran at max.
- The GitHub source was **still PRIVATE** when this log update was made. The authorized visibility change must be completed from the user's authenticated Windows `gh` CLI and verified. Public code is not proof that a Kiro-built application exists.
- This changes visibility only, **not** ownership, source provenance, copyright, licensing, competition eligibility, production deployment, or safety approval. Before public transition, inspect history and artifacts for secrets, personal data and redistribution restrictions.
