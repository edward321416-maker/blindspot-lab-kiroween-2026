# Source provenance and attribution

| Material | Creator/provenance | Present role | May claim Kiro-built? |
|---|---|---|---|
| Earlier Phase2/Phase3 experiments | Pre-Kiro research, developed through ChatGPT assistance (2026-11-15) | Historical evidence, not code baseline for new app | NO |
| Phase4 Python gate, fixture, 18 tests | Pre-Kiro ChatGPT research package (2026-11-15) | Reference-only and independently testable | NO |
| Phase4 `.kiro/specs` and steering | Draft generated outside Kiro on 2026-11-15 | Kiro planning input; Kiro changes tracked in commits | NO, until actual Kiro contributions |
| GitHub/local bootstrap | ChatGPT-authored imported research and handoff documents; Kiro CLI 3.3.0 performed isolated local workspace setup, Git import, checks, and private remote push on 2026-11-16 | `C:\\Users\\admin\\Projects\\blindspot-lab-kiroween-2026`; `chore/kiro-repo-bootstrap`; initial verified push `3fba8e0` | Bootstrap activities performed in Kiro, but NO contest application has been built |
| New `apps/` + `packages/` | Not started | Candidate contest software pending explicit GO | Only after Kiro actually builds/tests it |

The official rules require newly created projects, meaningful Kiro usage, and disclosure of reused existing code. Track each new work item, Kiro session, change, commit and test in `docs/DECISIONS.md` or `docs/KIRO_BUILD_LOG.md` once implementation begins. Do not backdate or misattribute.

## 2026-11-16 verified handoff checkpoint

- New private repository: `https://github.com/edward321416-maker/blindspot-lab-kiroween-2026`; verified private with default `chore/kiro-repo-bootstrap` at initial commit `3fba8e013cf6389744a9306a8d02626c434f66af` and tree `c1fd28244d5db46ad1f960c0b029d29c4abd1f77`.
- Kiro CLI 3.3.0 imported and checked the pre-existing data without altering historical fixtures. Test evidence: all 13 hashes, 18 pytest cases, intentionally blocking gate with 38 new regressions. Current data and `.kiro` drafts remain pre-Kiro research rather than Kiro-authored app implementation.
- First initial clone and validation reportedly used Auto; later Git synchronization used `claude-opus-5.5` at max effort, differing from policy target high. A separate model/effort change by user is pending.
- No `main` branch, license, deployment, purchased cloud infrastructure or public release. Do not make original research evidence into claimed real-world oracle validity.

## 2026-11-16 publication and model-effort authorization

- The user explicitly approved `claude-opus-5.5` with `max` effort and PUBLIC visibility for **this single contest repository**. Earlier `max`-versus-`high` policy discrepancy is resolved as a policy decision; retain the historical record that bootstrap ran at max.
- The GitHub source was **still PRIVATE** when this log update was made. The authorized visibility change must be completed from the user's authenticated Windows `gh` CLI and verified. Public code is not proof that a Kiro-built application exists.
- This changes visibility only, **not** ownership, source provenance, copyright, licensing, competition eligibility, production deployment, or safety approval. Before public transition, inspect history and artifacts for secrets, personal data and redistribution restrictions.

## 2026-11-18 Re:Collection Met C evidence branch

- Execution plan: repository commit `ddfa8ad36ff61128a684dc125d5105721ad246e7`; collector/test baseline: repository commit `93c4f7a9765af8c4fcd5a4c74f1ee7c98e9b2bd8`.
- OpenAI Codex performed this evidence run outside Kiro. It added 12 integrity regressions and 8 synthetic rights/output safety tests, collected two official Met JSON responses, and generated the sanitized packet in `docs/recollection-evidence/3.18-met-c/`.
- Private local evidence contains the raw response bytes, capture metadata, commit markers, and response headers. Those artifacts are intentionally excluded from GitHub; the branch publishes only code, tests, measured logs, response hashes/sizes, and source-separated rights decisions.
- This work is research evidence, not a Kiro-built product feature, legal opinion, image-use authorization, deployment, or contest-app implementation. No image file was downloaded.
