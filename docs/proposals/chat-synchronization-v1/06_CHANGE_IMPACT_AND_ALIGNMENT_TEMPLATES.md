# Research-to-development alignment templates — PROPOSAL ONLY

Use these in a future reviewed `ops/` rollout. They are not active statuses or evidence of any execution.

## 1. Accepted research change event (RCE) — immutable handoff

```yaml
change_id: RCE-YYYYMMDD-0001
created_at_kst: YYYY-MM-DD HH:mm
change_type: DOCUMENTATION | ADDITIVE | CONTRACT_CHANGE | DIRECTION_PIVOT
impact_level: L0 | L1 | L2 | L3
approval: PROPOSED | RESEARCH_ACCEPTED | PRODUCT_APPROVED
evidence_level: SOURCE_REVIEWED | REPRODUCED_SYNTHETIC | EXECUTED_REAL_DATA | INDEPENDENTLY_VERIFIED
originating_branch: research/<issue>
originating_commit_sha: <40 hex>
accepted_spec_revision_sha: <40 hex or NONE>
source_spec_path: .kiro/specs/...
changed_requirements: [RV-02, RV-03]
affected_gates: [G1]
previous_assumption: "..."
new_conclusion: "..."
primary_source_url_and_date: "..."
limitations_and_counterevidence: "..."
downstream_work_item_ids: [DEV-001, DEV-005]
approval_needed_before_execution: "..."
next_role: DEVELOPMENT
handoff_status: PUSHED_NOT_REVIEWED | ACCEPTED
```

The RCE must not invent acceptance. A research PR on a proposal branch is `PROPOSED` until the approval is recorded. The accepted spec SHA is the precise version the developer should use after review.

## 2. Development alignment matrix (derived from accepted Spec, not a second truth)

Proposed future path: `ops/DEVELOPMENT_ALIGNMENT.md`

| Work ID | Job / output | Depends on research IDs | Accepted Spec SHA | Stage authorization | Code / tests / interface | Current decision | Evidence / owner |
|---|---|---|---|---|---|---|---|
| DEV-PROTO-001 | blind S3 oracle input contract | RV-02, RV-03, RV-04, G1 | `f9b2b026...` (historical) | PLAN_ONLY | planned `oracle.schema` + synthetic tests | REPLAN_FOR_S3 | Development |
| DEV-PROTO-002 | model A/B prediction adapter | RV-06, RV-07, G2 | `f9b2b026...` | PLAN_ONLY | model/version/hash adapters as design only | KEEP_CONCEPT | Development |
| DEV-PROTO-003 | exporter and CI evidence manifest | RV-07, RV-14, PM6 | `f9b2b026...` | PLAN_ONLY | immutable artifact integrity plan | KEEP_CONCEPT | Development |
| DEV-PROTO-004 | FiftyOne parity baseline | RV-08, RV-09, G3 | `f9b2b026...` | PLAN_ONLY | comparison setup and protocol review | NEEDS_REVIEW | Research + Development |
| DEV-PROTO-005 | customer-facing release gate | G1-G4 and PRODUCT_GO | NONE | BLOCKED_PRODUCT_GO | no production code | FREEZE | Human decision |

This table is **illustrative**: no actual files `oracle.schema` or application adapters have been created; all entries are proposed tasks, not completed implementation. Re-read real Spec revisions before importing examples into `ops/`.

## 3. Development impact report after any accepted RCE

```markdown
# Development impact analysis — RCE-...
reviewed_at_kst: ...
reviewer_model/effort: ...
current_origin_SHA: ...
last_development_base_SHA: ...
accepted_research_spec_SHA: ...
scope_and_approval: PLAN_ONLY / RESEARCH_EXECUTION_APPROVED / PRODUCT_GO

## What changed in research
| Requirement | Previous | New | Source/evidence | Gate effect |

## Dependency classification
| Task ID | Before | Impact L0-L3 | CONTINUE / UPDATE_TESTS / FREEZE / REPLAN / ARCHIVE | Why | Review/ETA |
| ... |

## Technical consequences
- Interface / schema / test delta:
- Invariants remaining valid:
- Old code now misleading or unsafe:
- What can be reused:
- What must NOT be run:
- Reversible work to do now:
- Observed vs estimated effort:
- Credits budget and expected /usage readings:
- Architectural/product/security decision for human approval:

## Acceptance tests / evidence
- Commands to run, expected exits and current actual status:
- Source revision and artifact hashes:
- Cases proving OLD assumption is rejected:
- Critical reviewer limitations:
- Current authorization:
- Next owner and first concrete action:
```

## 4. Specific example: Sama-COCO correlated labels

Change ID: `RCE-20261116-S3-ORACLE`. Source Spec `f9b2b026b2d619f3c2c764a5149975363e4fb724` (historically verified).
- Previous hypothesis: S1=COCO and S2=Sama-COCO are independent truth sources.
- Invalidated by source: Sama produced Sama-COCO with original COCO labels pre-loaded (different annotation guidelines). It is correlated; raw differences are NOT proven mistakes.
- Accepted research change: independent from-scratch S3 labels needed; R0 Spec revised.
- Classification: L2 CONTRACT_CHANGE for any work that uses independent-oracle assumptions.
- KEEP: simple evidence SHA manifest, data-source metadata, generic A/B replay contract (subject to tests).
- FREEZE: any logic claiming S1/S2 disagreement equals confirmed model regression.
- REPLAN: input source provenance, S3 blind annotation UI/contract, unsure/ABSTAIN, non-alert controls, audit logs.
- NO EXECUTION: no actual S3 labels, no real inference; app code gated by product GO and data rights.
- Required development artifact now: proposed schema mapping and synthetic unit tests PLAN, not application code; follow-up from Research when source rights and annotator protocol are approved.

## 5. Stale task guard — deterministic no-code baseline

Before any Kiro operation:
1. `git fetch` remote; identify actual HEAD of accepted default and task branch.
2. Identify `task_spec_sha` from the work item and files changed in accepted `.kiro/specs/` since that SHA.
3. If any dependency IDs or their contract fields changed, mark the task `NEEDS_IMPACT_REVIEW`, do NOT execute it. Otherwise continue scoped work only if separately authorized.
4. A Git HEAD difference caused only by unrelated documentation does NOT automatically invalidate every task. Use file/path/requirement-level diff.
5. Kiro logs observed version, branch, diff summary and decision. Manual human approval required for high-risk direction, data, spending, licensing or architecture decisions.
6. After execution read back actual remote commit/tree; no automation or chat can claim unseen local files are GitHub-synced.

## 6. Manual acceptance test cards

| Test | Stimulus | Expected outcome |
|---|---|---|
| SYNC-01 | Research adds nonbreaking paper | Dev recognizes L0/L1; does not cancel unrelated work |
| SYNC-02 | Research changes RV-02/RV-03 oracle source | Dependent tasks freeze/replan; unrelated manifest/checksum design remains |
| SYNC-03 | Research reverses product hypothesis (L3) | Product-specific work stops pending human decision, reusable assets inventoried |
| SYNC-04 | Dev starts from old task_spec_sha | Detects stale accepted Spec before running Kiro |
| SYNC-05 | New RCE exists only on unmerged PR | Shows proposed, NOT accepted; no unauthorized implementation |
| SYNC-06 | Kiro has unpushed local commit | State LOCAL_ONLY, no remote success claim |
| SYNC-07 | Phase4 baseline intentionally exits 1 | Retains blocked regression signal and separately reports unit-test PASS |
| SYNC-08 | Data rights/G4 unknown | Evidence remains BLOCKED, no unapproved dataset download or PRODUCT_GO |
| SYNC-09 | Both chats start with same accepted SHA | Same gate status and next decision; no automatic "memory" claims |

Manual pilot passes only with actual screenshots/logs or source artifacts and specific Git SHAs. Checking boxes in a template is not test execution.
