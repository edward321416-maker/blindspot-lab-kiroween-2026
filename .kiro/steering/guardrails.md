# Project operating principles — BLINDSPOT LAB

- Evidence first: separate synthetic benchmarks, source documents, user self-reports and measured real-world experiments. Never fabricate observations, models, independent reviewers, customer approval or Kiro credit usage.
- Preserve provenance in exports. Predictions and GT annotations must be produced by separate logical paths. Never silently change labels to make model B look better.
- Research is not release approval. A model with better average accuracy and any important newly failed case can still fail the release gate.
- Abstain on ambiguous oracle. Treat unknown provenance as BLOCKED, not PASS.
- Before suggesting novel model-comparison functionality, inspect FiftyOne's existing support. Require same-dataset measured head-to-head proof.
- No new paid cloud, OAuth, public data sharing, or unsafe arbitrary model code execution without explicit user authorization.
- Run unit tests before reporting completion. Any speculative future feature should be in tasks.md as unchecked.
- All Kiroween claims must be tied to real Kiro-created code; locally authored planning docs do not constitute using Kiro.
