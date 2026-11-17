# Re:Collection — B4 complete / B5 evidence-and-research QA gate

**Date:** 2026-11-17 KST  
**Scope:** documentation-only acceptance review from user-pasted Kiro B4 report (199 lines). Kiro Windows source/diff/test logs not independently accessible to the GitHub handoff author. **Do not interpret this as an independent B4 execution.**

## 1. B4 checkpoint and evidence

Reported local Re:Collection commit chain:
- B3 parent: `4c4dc7adf49f8c6a3e699da0370bd8c93374e98a`.
- **B4 local main HEAD:** `09f4b8a524058440a7dbc9917d3112640d73d258`; worktree clean, remote NONE.
- Full B4 Git diff supposedly `B4_09f4b8a.diff`, **2,375 lines/114,690 bytes**, full SHA-256 `2191e06afd971c9acfe09cf5bb8004a5bfb30a9057996ed9672b95fa8f90bafe`. Local file not read by this author.
- 10 files changed (+2301/-2), seven new: `src/integration/pipeline.ts`, `tests/helpers/integration-scenarios.ts`, `tests/b4/integration.test.ts`, `tools/b4-evidence.ts`, `reports/evidence/B4_INTEGRATION_EVIDENCE.json`, `reports/evidence/B4_TEST_RUNS.json`, `docs/decisions/ADR-0005-b4-integration.md`. Other files are README, tasks and package.json evidence script.
- `integrate()` invokes actual B1/B2 `validateText()` and B3 `run()`. It deliberately invokes B3 even after B2 refusal to verify B3's second refusal gate. The strict parser rejects duplicate JSON keys.
- B4 ran **164/164 Node tests** (B0 3, B1 59, B2 50, B3 22, B4 30) twice and post-commit, all exit 0, normalized test-result SHA-256 `0452a87078b475cfcb0ee904702d87aa2b4a43e2b335902775029d83398e45d1`. Raw TAP files differ by durations; must not claim byte-identical raw logs.
- B4 evidence artifact SHA-256 `3bcb03e5616cc8ad426389b25cd977881c43e46f3dc54537de8f7ffcd928fba3`; two generations identical; `recordsSha256` reported prefix `8c022525...`.
- B0 frozen 9 files and prior B1–B3 tracked files reportedly unchanged. No Node modules/cloud/network or deployment. `TYPECHECK_NOT_RUN`, `BONUS_USAGE_UNOBSERVED`, model only `SESSION_CONFIG_ONLY` (`claude-opus-5.5` /`max`).
- A Kiro-side checkpoint entry was saved as `PENDING_SYNC` in a local TSV because Kiro lacked Sheets connector. **That local row was not synchronized to Google Sheets by Kiro**.

### Precise B4 scenario counts

**23 integrated scenarios = 3 actually executed + 20 refused before primitive steps**:
- Executed: F1-01 (one-item `UNIT_SMOKE`), F2-01 (two-item synthetic normal E2E), and F3-12 (deliberate known gap).
- 20 refusals: F1-02 (one-item STANDARD rejected) plus **19** F3 cases excluding F3-12.
- F3-12 `SOURCE_BOUND_NOT_ENTAILED`: unrelated but real quote (e.g. "No") can bind a false/unsupported claim; B2 returns `VALID`, B3 **EXECUTES**, `historicallyVerified=false`. This is **not a successful fail-closed security outcome**, despite the test legitimately PASSing against a known-gap oracle. Do not market “20 attack cases all blocked” or “100% semantic accuracy”.
- F3-13 `P2_OVERBLOCKING`: benign `Data: ...` rejected by unsafe-text gate; no unauthorized B2 bypass.
- Original B3 evidence parallels F1-01 R04, F2-01 R01, and F3-20 R03.
- Four of five mutated guards were killed, while M1 strict-parser guard removal survived; report describes it as behaviorally equivalent because parseJsonText already rejects malformed input. A surviving mutant is **not necessarily** a missed test; require direct justification plus coverage/threat trace, not a claim of 100% mutation coverage.

## 2. Provenance issue discovered: B0–B3 historical diffs

Prior B0–B3 `.diff` reports were captured with a PowerShell pipeline and reportedly contain BOM, CRLF and corrupted non-ASCII characters (e.g. `R01–R06` mangled). Their historic full-diff *bytes* cannot be trusted as byte-identical `git diff` output, even when line counts match.

**Safe B5 provenance repair, without rewriting history:**
- NEVER overwrite or delete original B0–B3 diff files; preserve their hashes and paths as `LEGACY_DAMAGED`.
- Reconstruct fresh **distinctly named** diff artifacts from the **existing local commit ancestry**, e.g. `B0_<sha>_CANONICAL_UTF8.diff` ... `B3_<sha>_CANONICAL_UTF8.diff`, using Git raw byte output or a verified encoding-safe file writer (not PowerShell `|` text recoding); UTF-8, LF, no BOM if raw Git outputs that format.
- Compare each regenerated file to the exact `git show --format= --no-ext-diff <commit>`/equivalent verified bytes, and record SHA-256/full byte counts. Validate exact commit parent, diff truncation, binary patches if any, and absence of character replacement. No cherry-pick/reset/stash/rebase; commit graph unchanged.
- Recovered Git byte output is evidence of the commit diff, **not reconstruction of the original damaged report bytes**. If original Git commit unavailable, label `UNRECOVERABLE`, never guess.
- This action only creates **new audit copies** in the existing approved local report output directory; it is reversible and has no product source/repo change. No edits to original file locations.

## 3. Research alignment changes

| Research issue | Evidence | Current meaning | B5 review |
|---|---|---|---|
| 3.0 ARCHIVE DETECTIVE 3–8 artifacts versus frozen D1 2–4 | 3.0 indexed product planning + current D1 source contract | L2 future product schema proposal, NOT automatically approved | Document versioned migration/architecture decision needed **after D1-BUILD**, not rewrite oracles in B5 |
| Source→claim→choice→feedback closure (3.6–3.8) | cross-conversation reported research, not actual developer test | B4 has no correctness or feedback path; **absence of feedback is not correctness proof** | Gating before real visitor feedback/approve/publish, no private holdout leakage |
| **3.9 OAP-0.1 reference retest** | GitHub `20_ALIGNMENT/RESEARCH_3_9_OAP_REFERENCE_RETEST_20261117.md`, current research source record | 38 researcher-authored unique cases ×2 = 76 self-oracle judgments; five initially bypassed cross-output sinks and were blocked after revising research reference. **NOT Kiro product verification or approved schema** | Evaluate output sink and allowed strings as threat model only; provide an **L2 proposed future output-policy adapter**, not B5 code or deploy. Independent human blind oracle pending |
| B2/F3-12 unrelated citation passes | current B4 local reported case | **P1 candidate** for eventual educational truth feedback and publish; report `historicallyVerified=false` mitigates overclaim but does not prevent a misleading source-bound rendered statement in future UI | Verify no B4/B3 public or correctness output; BLOCK product-publication claims |
| B2/F3-13 benign overblocking | current B4 local reported case | P2 usability defect, could be severe for natural text | Preserve fail-closed rule; propose exact narrowly tested patch with regression, NOT an uncontrolled bypass |
| Rights/curation and D1E | synthetic fixtures only; independent rights reviewer/holdout not assigned | NOT_TESTED | Do not promote test PASS to `GO_PRODUCT` or D1E superiority evidence |

**Strongest conclusion:** B4 is a **synthetic compiler integration PASS**. It does not show a museum-ready visitor journey, historical statement entailment or comparative advantage. A B5 quality review can still recommend `GO_FOR_D1E_PREP` with P1/P2 blockers transparently listed, because preparation ≠ permission for real A/B execution or publishing.

## 4. B5 decision criteria

- **P0:** bypass of B2 fail-closed validator, untrusted code/file/network execution, unauthorized approval/publish, mutable source/spec hash mismatch accepted, irreversible corruption → `HOLD/REWORK`.
- **P1:** irrelevant-locator semantic entailment failure for factual visitor-facing output, missing indirect evidence for choice/feedback, insufficient rights/provenance to reuse real museum materials, independent validation absent → **B5 technical QA may PASS with strict product-use restrictions**, but product/real-data publishing stays HOLD.
- **P2:** `Data:` benign text overblocking, absent static type-check, report metadata quirks, canonical diff provenance defects → backlog/repaired evidence; cannot silently weaken safety gates.
- No independent curator review, browser/accessibility, output-policy OAP adapter, D1E A/B results or live rights verification: all remain **NOT_TESTED**.
- B5 options: `GO_FOR_D1E_PREP` (planning only; no actual D1E run), `HOLD` (unresolved technical or provenance risk), or `REWORK` (repeatable P0/failed invariants). Never declare product GO based on 164/164 alone.
