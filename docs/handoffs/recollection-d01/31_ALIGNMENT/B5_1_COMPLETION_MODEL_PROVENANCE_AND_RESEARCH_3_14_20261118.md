# Re:Collection — B5.1 postmortem and 3.14 research/development alignment

**2026-11-18 KST · SOURCE TYPE: user-pasted local Kiro B5.1 report · NOT independent code audit or GitHub product code.**  
**Decision:** `B5_1_TECHNICAL_PATCH_PASS (KIRO_REPORTED)` / `MODEL_POLICY_VIOLATION` / `D1E_EXECUTION_HOLD` / `VISITOR_OUTPUT_AND_PUBLISH_HOLD`.

## 1. Actual local Kiro checkpoint (not uploaded to this public docs repository)

- Isolated workspace: `C:\Users\admin\Projects\recollection-kiroween-2026`; `main`, clean, **no remote** per Kiro.
- Parent B5: `b112c6a93c715e027a8ad3155f35a667f5260396`.
- **B5.1 local commit:** `101836551883aae0e5fc179100538de2e5beeacb`.
- Full diff on user Windows: `B5_1_1018365.diff`, 140,571 bytes / 3,397 lines, SHA-256 `dbb7c6fc5225c64f7287fe51ef4703dbce5f11928b3112e2d0167b893e960ad3`; not byte inspected in this ChatGPT environment.
- Reported `node --test` 194/194 PASS twice and after commit, **164 original tests + 30 new tests**, same semantic output hash `be9350bc...2992`. 194 unique stage/file#ordinal identities were added without renaming old 164 test titles. `B5.1` own evidence 27/27 reported deterministic. Prior B1–B4 evidence bytes reportedly unchanged, including B4 `3bcb03e5616cc8ad426389b25cd977881c43e46f3dc54537de8f7ffcd928fba3`.
- B5-05 fixes reported: snapshot actual executed `script` before counting steps; reject over-50; normalization total value cap 262,144; options.validation single read. Regression A01 200→STEP_LIMIT/0 executed, A04 100,000→STEP_LIMIT/0, A08 malicious 1M Proxy→NOT_CANONICAL before reading fake elements.
- B5-06 fixes reported: `validate()`/`validateText()` own detached stable snapshot; reject getter accessor `SCHEMA_INVALID`, catch throwing Proxy trap and return REJECTED; decisions and SHA from same effective snapshot. B1 `validateSpecContract`/`validateSnapshotContract` independently still reread input; never treat detached B1 helpers as an authoritative validator for untrusted in-process objects.
- B5-07 fixes reported: `integrate()` hashes exactly its normalized script passed to B3; supplied report SHA shape restricted to lower-case 64 hex; shape ≠ authenticity.
- The real scope is JSON-like stable input; *JavaScript Proxy trap code can execute during normalization*. No general hostile in-process JS sandbox claim. Native TS typechecking still `TYPECHECK_NOT_RUN`.
- No modifications to ExperienceSpec 0.2 2–4 object contract, R3.5 unsafe-text rules, primitives, earlier frozen oracles, B0–B4 evidence or GhostWeb/BLINDSPOT. No local GitHub remote, npm deps, AWS or public publisher. Kiro usage `BONUS_USAGE_UNOBSERVED`, never claim soft/hard ceiling objectively enforced.

### Nonconforming subagent provenance — correct ADR-0006 without history rewriting

The user-provided Kiro report says:
- `2026-11-18 01:18–01:22 KST`: review subagent had **eight** `claude-opus-5.5` inference events.
- `2026-11-18 01:28–01:44 KST`: review subagent had **fifteen** `claude-opus-4.8` inference events. This **violates Opus 5.5/MAX ONLY, no fallback**.
- Main Kiro session log reportedly contained Opus 5.5 for all its inference events and **re-executed** subagent probes against final B5.1 commit; all results reproduced, and B5 versus B5.1 65-case comparison had zero mismatched expected comparison outcomes.
- Technical `PASS` belongs to **main-session revalidation**, not a claim that the entire review was Opus5.5-only. Main effort is observable as saved configuration (`SESSION_CONFIG_ONLY`) rather than per-turn certainty.
- Committed `ADR-0006` reportedly says `SAME_MODEL` for subagent challenge: **false**. User's local report directory contains `B5_1_ADR_0006_ERRATUM_PROPOSED.md`, a renamed `B5_1_CHALLENGE_MIXED_MODEL` bundle, `MODEL_PROVENANCE.md` and TSV correction lines. These local files are not presently GitHub-synced, and their exact bytes have not been read here.
- **Disposition:** add a new DOCS-ONLY local commit clarifying `MIXED_MODEL_NONCOMPLIANCE` and main-session independent-of-subagent revalidation; preserve original ADR and commit in history, with additive erratum. Do NOT conceal, backdate, amend or delete logged model drift. **No new subagent invocation**, as user/main session cannot pin its effective model. A fresh independent human review, if demanded, remains separate and unperformed.

## 2. D1E preparation vs actual experimental readiness

Kiro created outside-repository local D1E_PREP files `D1E_PREREG_DRAFT.md`, `D1E_FAIRNESS_MATRIX.md`, and `D1E_APPROVAL_GATE.md`. Source reports C1 direct-Opus and C2 compiler planned, two runs/case, independent human oracle author, rights reviewer, blind scorer **UNASSIGNED**, credits/budget **UNKNOWN**. Only 1/10 prerequisites completed, so `D1E_EXECUTION_HOLD`.

**Proposed user-facing comparison choice:** favor **B — defer browser-app quality comparison until a genuinely safe C2 renderer is implemented and evaluated**. A restricted **A — contract-level output benchmark** may be planned separately now if rigorously labeled schema/evidence compliance only; it must NOT be marketed as user-facing product quality, direct-HTML superiority or visitor usability. No actual experiment with live arms is approved by this document.

Both arms must include initial compiler build costs separately from per-case costs; same Opus 5.5/MAX settings and equal inputs; contamination-free blind scoring; holdout sealed from implementer. No invented human reviewers or measured credits.

## 3. Latest product/research alignment: R3.11→3.14

At authoring the same GitHub docs-only branch also contains:
- `22_PLANS/RECOLLECTION_3_11_ARCHIVE_DETECTIVE_PRODUCT_BLUEPRINT_20261117.md`: **first vertical slice stays 2–4 artifacts** to match frozen 0.2; future 3–8 version remains a separate L2 proposal.
- `24_PLANS/RECOLLECTION_3_12_CONCRETE_PRODUCT_INTERACTION_CONTRACT_20261117.md`: independently developed **two owned synthetic record, two-question** standalone browser prototype (research-reported 17/17 UI smoke), change-aware review and media revoke state simulation. **Not connected to Kiro engine**; local APPROVED state is not real curator authority.
- `29_RESEARCH/ARCHIVE_DETECTIVE_SOURCE_INTAKE_AND_RIGHTS_REGISTER_20261118.md`: NYC historical bridge/tunnel sources and proposed item examples; text/source indices are NOT license to redistribute media; identified cross-source mayor-caption chronology conflict requires human review, not model assertion.
- `30_RESEARCH/RECOLLECTION_3_14_MULTIDOMAIN_SOURCE_LAB_20261118.md`: 58 heterogeneous public URLs/provider/standards across 14 coarse labels, **not 58 verified digital objects**. Research designs **12** 2–4-object cases; 8 source/link-only candidates, 4 held for licensing/attribution issues, **0/12 authorized for publication**. Offline **495 self-oracle checks ×2**, 21/21 standalone Chromium prototype UI tests; **none** is product Kiro integration, human blind validation, real media license approval or independent historical truth verification.
- R3.9 output-policy reference (38 self-oracle cases ×2) is an experimental **source** for designing versioned output-sink threats, not accepted or shipped B5.2 code. Do not leak private source-master/holdout IDs, answers or private cross-case test fixture bytes into this public branch.

### Work-item impact decisions

| Item | Development status | Disposition |
|---|---|---|
| B5.1 B5-05/06/07 runtime/input/evidence consistency | **KIRO PASS**, main-session repeated | KEEP; add provenance correction only |
| B5-01 `Recorded fact` on quote that does not entail claimed statement | **P1 VERIFIED** | Visitor/public outputs **BLOCKED** until separate versioned output/claim-review policy |
| B5-02 unrestricted AI-authored visible labels/questions/text | **P1 VERIFIED** | Visitor/public outputs **BLOCKED**, all output sinks reviewed before renderer |
| B5-11 rights laundering into textual strings | P1 synthetic counterexample | No real data/media; design field/sink-level rights derivation |
| B5-24 indirect source→choice→branch→feedback closure | P1 research gap | No unreviewed feedback; conservative whole-experience re-review where needed |
| R3.14 12 cases vs D1 test oracle | Research-only self-oracle | Do **not** import to Kiro, especially sealed 3.2 holdout; no new test PASS claims |
| B5.2 OAP output-binding and safe renderer | Not authorized/implemented | PLAN_ONLY; user architecture approval needed for actual code/UI |
| D1E fairness and independent evaluation | PREP DRAFT; missing reviewers & budget | HOLD actual experiment |
| AWS, public GitHub, curator auth, production publish | NOT AUTHORIZED | HOLD |

## 4. Recommended next steps

1. **Immediately correct ADR-0006 in a new local docs-only commit**, without changing code, original model logs or retroactively altering historical commits. Main session only. This is factual correction and does not require rerunning expensive full B5.1 tests.
2. **Complete B5.2 output-contract design before implementing visitor UI**: typed output/visible text registry; claim/source/evidence relevance flags; safe epistemic labels; rights derivation, review scope and invalidation; no approval/publish API fabricated from prototype local state.
3. **D1E B route recommended for product value**: align both comparison arms on actually runnable visitor app with same source/goal and independent evaluation. A restricted technical contract-only benchmark may be designed sooner but is not a substitute for B.
4. Real user consent gates: new B5.2 architecture/code change and D2/browser integration, cloud/paid budget, rights/IP/OSI license, public repository, independent evaluator roles. Keep first 2–4-item demo synthetic until rights cleared.

**No monitoring outside active chat is implied**. This snapshot is timestamped; later Kiro results must be retrieved again.
