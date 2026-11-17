# Re:Collection — D0.2 evidence review, D-1–D-7 proposed resolution, and D1 decision gate

**DOCUMENTATION ONLY / USER DECISION PENDING / NOT D1 AUTHORIZATION**

- Date: 2026-11-17 KST
- Provenance: user-provided Kiro D0.2 *summary*, not the original 178-line local addendum. We cannot inspect the local addendum or independently verify its SHA-256 from this GitHub authoring environment. **User-reported, not independently re-executed**.
- Public branch: \`handoff/recollection-d01-readonly-20261117\`; distinct from BLINDSPOT default branch and GhostWeb worktree.
- Source hierarchy: user instructions > actual original \`01_START_HERE\` > verified final Master Audit > ADR > Kiro-proposed D0 choices. GitHub text transcriptions of the first two known text sources are **not original byte-identical ZIP members**.
- Cross-environment evidence: \`04_EVIDENCE/D0_2_SOURCE_RECONCILIATION_20261117.md\` records a prior isolated ChatGPT environment's CRC/SHA verification of 6 originals; original ZIP and PDFs are **not uploaded here**, and Kiro on Windows did not independently read their bytes. Treat that record as \`CHATGPT_ARTIFACT_VERIFIED\`, not \`KIRO_LOCAL_VERIFIED\`.

## 1. D0.2 findings: evidence classes, not unsupported promotion

| Item | Evidence level | Current implication |
|---|---|---|
| Session config says \`claude-opus-5.5\`, \`max\` | **KIRO_LOCAL_CONFIG_VERIFIED (user report)** | Saved configuration only; does not prove every response's effective runtime model or effort |
| \`/usage\` | **USAGE_UNAVAILABLE** | No actual credit baseline; terminal turn/session counters are not equivalent to the \`/usage\` pool |
| GitHub public documents | **KIRO_GIT_READBACK (user report)** | Branch HEAD reported \`6a6dd1c9...\`, Kiro checked 4 blob SHA values |
| Original 6 binary sources | **CHATGPT_ARTIFACT_VERIFIED in existing evidence note; KIRO_LOCAL_UNAVAILABLE** | Byte-level audit cannot be represented as a Kiro-local verification |
| D-1–D-7 | **KIRO_LOCAL_REPORT_EXTRACT (user report)** | Kiro-generated decision list, not a list invented by the original handoff |
| GhostWeb | **KIRO_LOCAL_GIT (user report)** | Uncommitted changes; must not be discarded, reset, staged or touched in this project |
| BLINDSPOT | **KIRO_LOCAL_GIT (user report)** | One unpushed local commit; must not be touched, pushed or rebased here |
| Re:Collection D1 | **NOT AUTHORIZED** | No code, dependency install, repository initialization, Git operations, AWS or deployment |

The exact D0.2 addendum is reported at local D0 report folder under \`D0_2/\`; this text is a separate review, **not a copy of those 178 lines**. Do not assert the reported \`8ae34442...\` is a complete verified hash.

## 2. Decisions D-1 to D-7: original options and bounded recommendation

The *options* below are quoted from the user-supplied D0.2 table. The recommendations are this technical review's PROPOSALS, not user approvals.

| Decision | Given choices | Proposed resolution | Approval/status |
|---|---|---|---|
| D-1 GhostWeb D1.4 dirty changes | (a) separate approval and finalize; (b) leave branch on hold; (c) discard | **(b) HOLD**. Preserve source files, HEAD, and uncommitted work; Re:Collection does not depend on cleaning it. | Reversible default; NO destructive action |
| D-2 \`ExperiencePlan.objects\` count | 2–4 reflecting product; or 1–4 reflecting Case A | **Product/publish gate = 2–4**. One-object Case A allowed only as a separately named UNIT_SMOKE fixture. Avoid allowing \`objects=1\` into a public 2-object experience without a distinct experimental schema/validation mode. | Proposed product contract; requires acceptance before implementation |
| D-3 D1 phasing | one joint build+experiment approval; or split | **SPLIT.** D1-BUILD builds compiler/validators and tests; D1E evaluates direct A vs compiler B later under separate authorization. | Proposed; do NOT equate this proposal with approval |
| D-4 D1 build credits | Original soft 260/hard 380 vs suggested soft 260/hard 340 | **Soft +260 / hard +340** *for D1-BUILD only*, contingent on real \`/usage\` baseline and user approval. D1E has a separate proposed +60–120 estimate, not covered. | **HOLD** without measured baseline |
| D-5 runs/case | 1 vs 2 | **Two preregistered runs per evaluable case when budget allows**. If funds insufficient, mark incomplete/inconclusive; do not drop a run after viewing results. Trial repeats must not inflate independent sample size. | Proposed; budget-dependent, freeze before seeing outputs |
| D-6 publishing license allowlist | CC0-1.0 + PDM-1.0 only vs include NoC-US | **CC0-1.0 / PDM-1.0 only for D1 candidate public-media allowlist** with asset-by-asset proof and attribution; NoC-US **excluded**. Licensing string alone is not enough if particular assets/rights fields conflict. | Proposed conservative security/rights policy |
| D-7 GhostWeb timing | prior to Kiroween window vs during Kiroween | **Neither automatic label**. Official submissions open 2026-10-30; Kiro reports first GhostWeb commit 2026-11-16, which is WITHIN submission window. But any reused pre-existing material must be disclosed; commit date alone does not prove all source work is new. Treat GhostWeb as separate candidate, not used by Re:Collection; preserve provenance. | Official date verified; full eligibility of a hypothetical GhostWeb submission unverified |

User's original D0.2 table proposed D-2 \`1–4\` and D-5 2 runs if budget; this review deliberately recommends **2–4 for publication + 1-object unit-smoke exception**. This is an explicit design proposal, not a silent rewrite of source consensus.

## 3. Verified official facts that resolve the contested assumptions

1. **Kiroween official rules:** Registration 2026-10-13; Submission Period 2026-10-30 09:00 PT to 2026-12-04 14:00 PT (2026-12-05 07:00 KST). Newly created project using Kiro required, and all incorporated preexisting work must be disclosed. Root \`/.kiro\` required. https://kiroween.devpost.com/rules
2. **Node.js schedule:** Both Node 24.x and 26.x are supported LTS as of 2026-11-17. Node 24.x is Maintenance LTS and Node 26.x Active LTS; Node26 upgrade is **not required just to start a compatible prototype**. https://nodejs.org/en/about/previous-releases
3. **Next.js 16:** documented minimum Node 20.9, so existing reported Node 24.14 meets the runtime minimum. This does **not** attest dependency compatibility, installed Next.js or that Next is necessary. https://nextjs.org/docs/app/getting-started/installation
4. **Kiro CLI:** \`/model\` picker configures model and effort; \`/effort max\` is session-specific unless persisted; \`/usage\` in the interactive terminal reports actual limits/usage. \`/model fallback clear\` may restore vendor default, so if model must be frozen select **None** in the fallback picker when supported; verify actual display. https://kiro.dev/docs/cli/reference/slash-commands/
5. **No proof of outcome superiority:** previously reported \`55/55\` deterministic tests of preselected interaction modules are not blind novel-item generation nor proof that a compiler beats direct coding.

## 4. Stage names / stack / backward compatibility — recommended stable contract

To avoid mixing ADR and D0 names:

- \`D0\`: source/evidence/architecture/preregistration review.
- \`D0.2\`: evidence reconciliation and decisions (this is historical user report).
- \`D0.3\`: **final readiness reconciliation only**, no code.
- \`D1-BUILD\`: if separately authorized, isolated local compiler, validator and primitives; construction cost measured.
- \`D1E\`: if separately authorized, same Opus 5.5/MAX direct-build A vs compiler B; marginal case-by-case costs and quality measured.
- \`D2\`: future curator experience and publishing workflow work **after** benchmark judgment; no D2 authority here.

**Stack proposal:** TypeScript on existing Node 24 LTS for deterministic contracts, validators and \`node:test\`. No compulsory Node 26 install. Evaluate Next.js 16/React 19 only for an approved UI slice; do not require them for initial compiler/experiment contract. Keep npm/Playwright/Ajv/axe-core installation blocked until D1 authorization. Limit React/Next-specific APIs outside the core compiler.

**ExperienceSpec v0.1→v0.2:** v0.1 original schema bytes/interfaces not currently accessible, so **compatibility = UNKNOWN**. Future design should specify a versioned migration table, refusal for unknown fields/privileged records, immutable SHA of inputs, and explicit \`schemaVersion\`; do not claim backward compatibility without fixture tests. AI may author \`claims/plan/graph\`, never \`verification/approval/publication\`.

**Independent evidence:** user should pick a genuinely separate **human** holdout author/oracle and freeze that person's cases before any authoring model sees them. Using Opus 5.5 in both implementation and audits does not itself make an oracle independent. No other AI model is mandatory here.

## 5. Distinguish real blockers from things that can proceed

**Blocking cost-bearing D1 approval:**
- A real, user-visible \`/usage\` before launch and after each capped stage; saved session model/effort config is not per-turn attestation. If screenshots are not accessible to the agent, user can paste the values.
- User's explicit authorization of **a specific D1-BUILD scope** and credit cap; isolated workspace, npm packages/versions, local headless Edge and source rights should be named precisely.
- Frozen rights-qualified source corpus + **independent human** holdout plan and objective A/B scoring contract. Do not claim readiness where these are missing.
- Final-original Master Audit / ZIP are not available to the local Kiro; a cross-environment SHA attestation can support planning but cannot substitute for their exact byte audit. If this remains unavailable, label uncertainty; decide whether a self-contained accepted master-spec excerpt is sufficient for a strictly limited D1-BUILD only after separate human approval.

**Non-blocking for planning:**
- GhostWeb's dirty branch and BLINDSPOT's unpushed commit (do not touch).
- Lack of node 26; Node24 meets Next16's published minimum.
- Different-model audits (not required by user; use separate humans/sessions and independent tests).
- Cloud Bedrock credentials; local mock mode is the correct planned baseline, no AWS calls.

## 6. D0.3 exit artifacts — read-only only

A short D0.3 technical memo must state:
- exact GitHub pinned source commit and which original bytes remain locally UNAVAILABLE;
- D-1..D-7 accepted/proposed/blocked distinctions, respecting Kiro's original text;
- single product object count and 1-object smoke exception, A/B protocol and stage names;
- Node 24 LTS compatibility and chosen minimal TS core proposal;
- current Kiro model/effort/usage as **observed**, or UNKNOWN;
- actual rights and oracle owner, not invented names or consent;
- decision: \`READY_TO_REQUEST_D1_BUILD_APPROVAL\` or \`HOLD\` or \`NO_GO\`.

**Absolutely no D1 code, Git changes, install, AWS or deployment.** A result of READY_TO_REQUEST is **not approval**.
