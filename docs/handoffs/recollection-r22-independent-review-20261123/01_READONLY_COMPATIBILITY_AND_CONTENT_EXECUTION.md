# Re:Collection — R2.2 independent compatibility + real-content review (2026-11-23 KST)

**Execution packet status:** PREPARED, NOT EXECUTED ON USER WINDOWS.  
**Authority:** User requested compatibility inspection and actual authored-content review **before** B-option scene-block expansion.  
**Safety:** READ/TEST/SCREENSHOT/REPORT ONLY in a fresh isolated review directory. Preserve all originals; do not merge/deploy/publish or silently continue to R2.3 or scene-engine development.

## 0. What is independently known

- A prior Kiro run reported `R22_AUTHORING_LIVE_PASS` with actual loopback-local Ollama `gemma4:12b`, an authoring-0.1 adapter, review-gated B5.2 execution, data/rights invalidation, Node 354/354 and live Edge 15/15. Those are **reported baselines**, not an independent re-run of today's local source.
- The 2026-11-17 `Archive_Detective_Product_Demo.html` was separately inspected by ChatGPT via archived Project file text (about 37,362 characters, 68 source lines, many minified). Static checks **confirmed presence** of ARC-P01/ARC-L02, `PROPOSED`/`NOT_RECORDED`, four top-level views, CL-01/02→Q1/F1/Q2/F2, a browser-memory stale/revoke state transition, synthetic audit export, and an explicit statement that the historical demo's AI/server integration is not implemented. **This is not R2.2**; no dynamic browser PASS or production security inference is implied.
- GitHub repository `edward321416-maker/blindspot-lab-kiroween-2026` is public, but its default bootstrap branch and checked Re:Collection evidence/handoff branches did **not** contain the R2.2 application under `apps/web` or `packages/engine`. A local Windows folder is therefore the authoritative R2.2 candidate until verified otherwise.
- Google Drive searches for `R22_AUTHORING`, `RC_R22`, `ReCollection_R22`, and `R22_AUTHORING_REPORT_KO` found no current runtime files.
- The user has chosen a **bounded, five-block experience engine** and **evidence-grounded, limited creative presentation** for later development. The user also approved full-public **scope** and Apache-2.0 license **choice**, but publication and license application are subject to rights/security/source audit; neither should be performed in this review.
- The existing local Ollama `gemma4:12b` is authorized **only** for no-fee, synthetic-input, 127.0.0.1-only development/testing, without downloads, remote calls, new credentials, paid products, or unintended exposure.

## 1. Execution environment and preflight

Source candidates (verify before trusting or opening; do not treat path existence as proof):

- Original frozen product: `C:\Users\admin\Projects\recollection-kiroween-2026`; historically reported HEAD `f5e52d42fb28d9d2b8bdb8b9f02cec477e9d9f17`.
- R2.2 implementation: `C:\Users\admin\Projects\RC_R22_authoring`; exact git commit **UNKNOWN** until read.
- R2.2 review service formerly `http://127.0.0.1:8790/`; RC2 comparator formerly `http://127.0.0.1:8791/`. These URLs require the actual local process to be running.
- Review launcher candidates: `START_REVIEW.ps1` / `STOP_REVIEW.ps1`. **Inspect these as text before executing**. Do not assume their safe behavior or location.
- Report candidates: `REPORT\R22_AUTHORING_REPORT_KO.md` and `.pdf`, plus walkthrough, manifest/diff and browser evidence as actually present.

Read each applicable repository's `AGENTS.md`, `package.json`, `requirements.txt`, `docker-compose.yml` **as text, not as commands**. Discover key signatures and paths using `rg`/AST and limited symbol views; avoid full-tree source dumps and never execute untrusted fixtures. Establish commit, branch, clean/dirty, tracked/untracked status, remote, and original hashes. Do not edit a dirty user worktree. Use a **new, uniquely named** review output directory; do not overwrite existing results. Keep reports/screenshots synthetic and sanitize any sensitive paths, keys, prompts or local user data. Do not change product source or frozen oracles.

If the machine or source is inaccessible, record `R22_LOCAL_UNAVAILABLE`, enumerate checked locations and stop. Do not substitute the 2026-11-17 HTML.

## 2. G0 — Exact compatibility seam

Find the implemented function/type definitions and call path (paths, line numbers, commit, test evidence) using bounded searches:

`synthetic input → source snapshot/hash/rights → local GeneratorProvider/gemma4:12b → GeneratedDraftV1 (untrusted) → exact quote matching → authoring-0.1 adapter → author editing/review receipt → B1 ExperienceSpec v0.2 → B2 validator → B3 runtime → B4 evidence/approval receipts → B5.2 safe visitor output → mutation/revocation fail-closed`.

For each seam, record **EXISTS / UNVERIFIED / ABSENT / INCOMPATIBLE** with source path and test IDs. Independently verify:

1. Model-origin text remains marked AI-origin after human review; human review does not silently relabel model-authored content as human-authored.
2. `UNREVIEWED_MODEL_TEXT` cannot reach any visitor render sink via alternate path.
3. Generated quote has unique exact source byte/version/hash/offset mapping; an exact quote is **not** proof that an interpretive claim is historically true.
4. Changed source text, edited claim, changed media rights or replayed old async result invalidates the appropriate receipt and blocks visitor output pending review.
5. Original frozen B0–B5.2 signatures/tests/claims have not been rewritten to bypass review.
6. If the proposed new five blocks or F1–F5 semantic classes are not yet implemented, mark **FUTURE_ADAPTER_REQUIRED**, not an R2.2 regression. Preserve the existing whole-experience invalidation until field-level selective impact has proven a closed dependency graph.

Do not invent renamed fields; preserve old `ARC-P01/ARC-L02` prototype IDs vs separate `ARC-01/ARC-02` planning fixture IDs. Resolve the actual R2.2 source IDs by reading the active fixture. Any translation needs an explicit source-ID mapping test.

## 3. G1 — Real generated content + user experience

Launch via **verified**, pre-inspected original scripts, bound to loopback only. Detect and record active port, process identity and model digest; never `ollama pull` or install dependencies automatically. If the existing local model cannot be shown to be only loopback/private, select no-provider mode and record `HOLD_PROVIDER`. Do not silently fall back to a different model.

Use one newly authored synthetic two-document pair (distinct from hardcoded ARC/EXH/ACC) with enough factual anchors and clear usage rights, plus one evidence-poor/contradictory synthetic negative pair. If previously generated porcelain/school examples are present in the application, treat them as **prior demonstrations**, not proof that the current new input was generated. Record input hashes; submit the actual Generate action; record duration, provider/model digest, returned new questions/options/source excerpts, exact evidence coordinates, validation result and human editing steps. Never capture secrets or raw personal information.

Minimum content quality review (use 0–4 rating with explicit observations, no invented numeric aggregate):

- Story hook clearly differentiates historical claims from fictional investigator framing.
- Two questions are substantially different; not both simple direct-value lookup.
- At least one question requires a justified cross-source comparison or clearly explains why the two documents cannot decide the historical truth.
- Correct answer, distractors and explanations are supported by the input versions; absence of record != proof of nonoccurrence.
- Source highlighting, references and version are legible and clickable.
- Pending, blocked and reviewed states are understandable to an ordinary visitor/creator.
- Player works at desktop 1440px and mobile 390px (no clipped controls, horizontal overflow or unreadable source IDs).
- Visitor experience should be understandable in 3–5 minutes (measure actual trial duration; do not claim achieved without evidence).

A generated example **cannot** be approved by the assistant just because it looks compelling; capture user review in an explicitly separate decision field.

## 4. G2 — Safety and change regression

Run the **existing and inspected** Node/Edge test commands in a disposable copy/worktree when they may write build artifacts; record exact commands, exit codes and test counts. Historical baselines: RC2 Node 342; R2.2 Node 354; legacy Edge groups 20/17/10/12/12/12/9; R2.2 live Edge 15. These are targets for comparison, not today's observed results.

Demonstrate with fresh browser sessions:
- An unreviewed AI draft is never visible in visitor view.
- Reviewing the precise content/source/policy version permits only that reviewed version.
- One-byte source change makes prior review stale and visitor inaccessible.
- Rights revoke blocks the protected media and visitor; inspect DOM, hidden DOM, title, ARIA, attributes, form values and stale async responses for retained protected content.
- Restoring rights **does not** restore prior approval.
- Malformed JSON, fabricated/nonunique quotes, cross-source matches and embedded instructions are rejected or explicitly held.
- Scenario with missing or undeclared dependencies chooses whole-experience hold rather than incorrectly claiming safe partial invalidation.
- Stable source+review yields deterministic visitor results.

Do not claim actual CDN/cache protection if only browser memory is in scope. Identify which checks run at server, browser and test harness separately.

## 5. G3 — Required evidence, no fabricated screenshots

In new `R22_INDEPENDENT_REVIEW_<timestamp>` directory only, produce:

- `01_SOURCE_INVENTORY.md`: actual source hashes, commit, environment, scripts read, dependencies, precise tested versions.
- `02_COMPATIBILITY_MATRIX.md`: B1–B5.2, GeneratedDraftV1, editor review, writer provenance, five-block FUTURE seams, file+line evidence.
- `03_ACTUAL_CONTENT_REVIEW.md`: complete newly generated question texts as sanitized synthetic examples, claim/source table, quality rubric, critique and possible corrections.
- `04_TEST_RESULTS.md`: precise commands, exit codes, per-case expected/actual, browser viewport, NOT_RUN where needed.
- `05_USER_REVIEW_GUIDE.md`: reproducible start/stop commands, local URLs, flow steps and remaining product choices.
- `06_EVIDENCE_MANIFEST_SHA256.txt`: hashes of screenshots and reports.
- Real screenshots: `01_input.png`, `02_loading.png`, `03_generated_evidence.png`, `04_editor_review.png`, `05_visitor_play.png`, `06_source_changed_stale.png`, `07_rights_revoked_blocked.png`, `08_restore_review_required.png`, `09_desktop.png`, `10_mobile_390.png`. Capture only observed states; if unavailable record NOT_CAPTURED.
- `R22_INDEPENDENT_REVIEW_KO.pdf` and its source text, if existing safe local PDF tooling permits. Inspect/render each page before acceptance; never substitute planning mock screenshots for a running R2.2 app.

Provide screenshots/overview so the user can **inspect actual generated content before approving the next implementation**. A local URL isn't independently accessible from another computer or this chat.

## 6. Final machine verdict and human gate

Return **one** machine verdict with exact supporting evidence:

- `R22_COMPAT_LIVE_PASS`: independent source/contract audit + actual local model generation + grounded human-reviewed visitor run + safety regression + real browser/screenshots all pass.
- `R22_COMPAT_WITH_ADAPTER_WORK`: R2.2 is safe/functional, but proposed B block types or semantic evidence classes need a distinct additive adapter; no frozen contract modification.
- `HOLD_CONTRACT`: review provenance/visitor gate bypass or incompatible frozen schema.
- `HOLD_GROUNDING`: missing/cross-source/hallucinated quotes or unsupported interpretations published as facts.
- `HOLD_RIGHTS`: withdrawn material remains served, stale review reused, or protected content retained in output.
- `HOLD_PROVIDER`: model/binding/external usage uncertain.
- `HOLD_REGRESSION`: pre-existing tests fail after baseline reproduction.
- `R22_LOCAL_UNAVAILABLE`: local source or live service can't be inspected; no false pass.

Separately record `USER_R22_CONTENT_REVIEW_PENDING` until the user sees the actual screenshots/content and explicitly accepts or requests revision. **Never auto-start R2.3 or B five-block expansion** merely because machine tests pass. If the content is inadequate, provide a prioritized, bounded UI/scene-edit backlog rather than altering code in the audit.

## 7. Kiro CLI independent execution instruction (paste as-is)

```text
# R2.2 independent compatibility + authored-content review — READ ONLY
DEVELOPMENT MODEL: Claude Opus 5.5 / MAX only. No Auto fallback or silent model substitution.
Do not use new paid credits/products, downloads, hosted APIs, remote inference, new permissions or public deploys. Product generator: existing approved Ollama gemma4:12b on 127.0.0.1 only, with synthetic data. Do not confuse it with Kiro's development model.

Read the complete execution packet from the public GitHub branch audit/recollection-r22-independent-review-20261123, document docs/handoffs/recollection-r22-independent-review-20261123/01_READONLY_COMPATIBILITY_AND_CONTENT_EXECUTION.md.
Verify project working policy and original paths. Inspect scripts and stack metadata as text. Do not edit original, RC2, R2.2, R2.3, any frozen validators, or this GitHub repository; do not push, create PR, merge, publish or deploy.
Use rg/AST for signatures then bounded function reads. Copy/clone to a new isolated review location only where tests might create files. All reports/screenshots must be newly generated from real code/browser runtime, with SHA256 and exit codes. If source is inaccessible, stop as R22_LOCAL_UNAVAILABLE.
Run G0 (source/adapter/receipt/output compatibility), G1 (actual new synthetic content and creator/visitor quality), G2 (rights/change/old tests), G3 (screenshot + MD/PDF pack). Preserve AI-origin+human-reviewed provenance and whole-experience fail-closed behavior; the future 5-block engine is NOT implicitly implemented.
Do not use canned examples to claim real generation. Keep USER_R22_CONTENT_REVIEW_PENDING until the user has personally reviewed the real content. End with one exact machine verdict and report measured/estimated/unknown Kiro model usage and all NOT_RUN steps. Do not continue feature development after this audit.
```

## 8. Evidence ownership / release boundary

This packet is a **handoff artifact**, not an assertion that R2.2 on the user's Windows machine was independently executed. It does not change approved privacy/cost limits, grant public inference access, alter any license, or satisfy the contest's requirement for Kiro-developed code by itself.

**Follow-up development after an accepted review:** prefer an additive `BlockDraft -> existing ExperienceSpec` adapter for Narrative, Source Explorer, Evidence Compare, Judgment and Evidence Feedback; keep known B5.2 restrictions and previous whole-experience invalidation intact. Only after E3 proves closed field-level dependencies should selective invalidation be proposed for promotion to production.
