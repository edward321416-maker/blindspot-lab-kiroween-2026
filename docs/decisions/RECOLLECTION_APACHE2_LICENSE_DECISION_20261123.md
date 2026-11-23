# Re:Collection — Open-source licensing decision

**Decision date:** 2026-11-23 (KST)  
**Decision:** Apache License, Version 2.0 (`SPDX-License-Identifier: Apache-2.0`)  
**Approval:** User approved full public-release scope and then explicitly accepted the Apache-2.0 recommendation.  
**Status:** LICENSE_CHOICE_APPROVED / APPLICATION_PENDING_SOURCE_AND_RIGHTS_AUDIT

## Intended scope

Release original, rights-cleared Re:Collection application source, ExperienceSpec adapters, bounded scene-block engine, AI authoring/validation logic, Studio and visitor-player source, synthetic test fixtures, reproducible tests, Kiro development material, and public documentation under Apache-2.0.

A public, accessible visitor/Studio demonstration and a public video are intended for Kiroween submission. A public demo need not expose a hosted LLM endpoint; deterministic approved-content playback may be publicly accessible, while AI authoring can remain reproducible through the previously approved local Ollama `gemma4:12b` workflow. Public web deployment, if performed, must satisfy the existing cost and security restrictions.

## Material not automatically relicensed

- Pre-existing BLINDSPOT LAB Phase 4 research/reference code and historical documents on the current default `chore/kiro-repo-bootstrap` branch: preserve its provenance and establish authorship/reuse rights before changing its license.
- Third-party libraries, templates, media, fonts, museum records, and datasets: retain their original licenses and attribution; do not assume that inclusion in this repository confers relicensing rights.
- API credentials, tokens, user/personal data, private development artifacts and rights-uncleared images: exclude from distribution entirely.
- Ollama model weights or other model assets: no redistribution authorization is implied by this decision.

## Release implementation checklist

1. Identify the canonical Re:Collection implementation branch/tree, with immutable commit and file inventory. The current repository default branch is still a BLINDSPOT LAB bootstrap and is not proof that the Re:Collection application is present.
2. Audit repository history, each owned/third-party source or asset, copyright provenance, license compatibility, and sensitive data. Preserve prior attribution and license obligations.
3. After that audit, apply the **unmodified complete** Apache-2.0 license as `LICENSE` at the appropriate release root; prepare an accurate `NOTICE` when attribution is required, and apply `SPDX-License-Identifier: Apache-2.0` to owned source files as suitable. Update package metadata and README license statements where applicable.
4. Verify the license text against the Apache Software Foundation's official text; review all changes as a narrowly scoped diff and run relevant existing tests without treating a docs/license check as product functionality validation.
5. Confirm public source and demo content, submission requirements, data and rights isolation, no paid/external model calls, and a tested fail-closed path before release. Do not rewrite history or merge unrelated work as part of licensing.

## What this record does and does not do

This record **confirms the user's licensing choice**. It does **not** attach Apache-2.0 to every pre-existing file in this mixed-history repository, does not assert that every prior contributor granted the license, does not deploy an application, and does not represent a completed license audit. Do not report `LICENSE_APPLIED` until the canonical release tree contains a verified license and passes the gates above.

References:
- https://www.apache.org/licenses/LICENSE-2.0
- https://www.apache.org/legal/apply-license
- https://www.apache.org/foundation/license-faq
