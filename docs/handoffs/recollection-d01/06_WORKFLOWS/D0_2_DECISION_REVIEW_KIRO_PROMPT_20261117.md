# Kiro read-only follow-up — D0.2 decision reconciliation (NOT D1 development)

**Priority:** User restrictions > actual original priority handoff (if accessible) > verified Master Audit > current `05_DECISIONS/D0_2_REPORT_REVIEW_AND_D1_GATE_20261117.md` > older ADR.

**The authorized action is to review and report, not to implement.**

1. Confirm the active session configuration from the interface if possible. **Claude Opus 5.5 / MAX only**, no Auto or fallback. If the settings file is the only evidence, report `SESSION_CONFIG_ONLY` rather than asserting that every turn used Opus MAX.
2. From the same pinned GitHub source commit, read:
   - `README.md`;
   - `04_EVIDENCE/D0_2_SOURCE_RECONCILIATION_20261117.md`;
   - `05_DECISIONS/D0_2_REPORT_REVIEW_AND_D1_GATE_20261117.md` (latest decision review).
3. Read the previously generated **local D0 report and D0.2 addendum** only from their already reported existing output directory; no whole-drive search. Verify the seven exact D-1..D-7 rows against their source; treat this GitHub memo as a **proposal** if it differs.
4. Evaluate the bounded recommendations:
   - D-1 preserve GhostWeb dirty changes;
   - D-2 published experience requires 2–4 objects; 1-object unit smoke remains permissible;
   - D-3 distinguish D1-BUILD from D1E;
   - D-4 D1-BUILD soft +260/hard +340 proposed, not approved, and separate D1E estimate +60–120;
   - D-5 preregister two attempts/case before viewing results; if budget insufficient, report INCONCLUSIVE rather than quietly reduce after outcomes;
   - D-6 only rights-qualified CC0/PDM for public assets, no NoC-US;
   - D-7 official Oct30 submission start, reported Nov16 GhostWeb commit is within period, but any preexisting reused material must be disclosed.
5. Check how D0's original ExperienceSpec v0.1 artifact differs from v0.2 **if the real v0.1 bytes are actually accessible**; otherwise mark `BACKWARD_COMPAT_UNKNOWN`. Do not invent migration proofs.
6. Verify local installed Node 24 compatibility with the proposed TS core; **no Node 26 upgrade is required merely to meet Next 16's published Node 20.9 minimum**. No npm install.
7. State which original handoff ZIP / Master Audit binaries are independently accessible locally versus only referenced by a provenance note. Do not publish original bytes, personal file paths or rights-sensitive inputs to a public repo.
8. Record `/usage` from the interactive UI only if available; if not, leave `USAGE_UNAVAILABLE` and HOLD all cost-capped D1 work. Do not treat Kiro's turn/session counters as pool usage.
9. Write a **brief Korean read-only decision summary**, each item with VERIFIED / USER_REPORTED / PROPOSED / UNKNOWN and a `READY_TO_REQUEST_D1_BUILD_APPROVAL` or `HOLD` verdict. Note whether separate human holdout/oracle and rights clearance are actually assigned. Do not invent reviewers or interviews.

**Non-negotiable:** Leave GhostWeb and BLINDSPOT dirty/unpushed state untouched. No Git branch changes, fetch into existing worktrees, commit, push, install, new repo, source code, AWS/Bedrock, deployment, product or experiment execution. Do not claim a Kiro D1 authorization. Stop after the summary and hand the findings back to the user.