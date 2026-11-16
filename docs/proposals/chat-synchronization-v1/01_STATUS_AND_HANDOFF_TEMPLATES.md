# Coordination file templates — PROPOSAL ONLY

These are examples, not accepted project state. The future ops/STATUS.md is a human-readable review index, not a replacement for Git history or evidence.

## Proposed ops/STATUS.md

    # BLINDSPOT LAB — authoritative snapshot
    status: RESEARCH_HOLD
    snapshot_as_of_kst: YYYY-MM-DD HH:mm
    reviewed_remote_head_sha: <full SHA actually read>
    reviewed_default_branch: chore/kiro-repo-bootstrap
    approved_by: <person/PR ref>
    product_selected: false
    data_download_authorized: false
    app_build_authorized: false

    ## Current gates
    | Gate | State | Supporting repo/URL | Blocker | Next owner |
    | G1 S3 blind real labels | NOT_STARTED | link | none collected | Research |
    | G2 two real checkpoint replay | NOT_STARTED | link | no run | Research |
    | G3 best-practice FiftyOne parity | NOT_STARTED | link | no runtime comparison | Research |
    | G4 same practitioner unmet need | NOT_STARTED | link | no directly grounded case | Research |
    | R0 cross-family review | PENDING | specific SHA | review not in accepted history | Research |

    ## Latest accepted evidence
    | Claim ID | Evidence level | Claim | Source/ref | What it does not prove |
    | BL-1 | SOURCE_REVIEWED | Sama-COCO preloaded COCO labels | exact official source | G1 independent human labels |
    | BL-2 | REPRODUCED_SYNTHETIC | 38 Phase4 synthetic regressions | exact case fixture SHA | real detector performance |

    ## Active work and handoffs
    | Issue/ID | Owner | Original base SHA | Branch/PR | State | Next action |
    | - | - | - | - | - | - |

    ## Usage snapshot — never pretend to be current
    Kiro bonus pool used: UNKNOWN until fresh /usage
    Observed time: UNKNOWN
    Phase5 incremental baseline: 110.23 as recorded by R0
    Plan soft/hard: +500 / +600 unless a later accepted decision amends it

    ## Known constraints
    Default branch: chore/kiro-repo-bootstrap (recheck)
    LICENSE: missing (recheck)
    main: missing (recheck)
    Product: RESEARCH_HOLD
    Next action and owner: independent R0 review / Research
    Last decisions: link to docs/DECISIONS.md entries

Interpret reviewed_remote_head_sha as the head the curator inspected when writing the file, NOT the commit that includes the file itself.

## Proposed ops/HANDOFF_CONTRACT.md

Each handoff is an append-only file; corrections create a superseding handoff and retain history. Required fields:

    handoff_id: BL-YYYYMMDD-NNN
    created_at_kst: ...
    from_role: RESEARCH | DEVELOPMENT | KIRO | INDEPENDENT_REVIEW
    to_role: ...
    originating_ref: branch + full commit SHA
    tested_ref: branch + full commit SHA (may differ)
    approval_class: PROPOSAL_ONLY | RESEARCH_EXECUTION_APPROVED | BUILD_APPROVED
    evidence_level: HYPOTHESIS | SOURCE_REVIEWED | REPRODUCED_SYNTHETIC | EXECUTED_REAL_DATA | INDEPENDENTLY_VERIFIED
    synchronization: LOCAL_ONLY | PUSHED_NOT_REVIEWED | ACCEPTED
    work_item: GitHub Issue number OR explicit local identifier
    source_urls_and_dates: ...
    changed_paths: ...
    artifacts_and_SHA256: ...
    actual_tests_and_exit_codes: ...
    Kiro_model_and_effort_if_observed: ...
    Kiro_usage_before_after_if_observed: ...
    proposed_decision_not_autoapproval: ...
    restrictions_and_known_unknowns: ...
    next_owner_and_first_action: ...
    supersedes_handoff: NONE | BL-ID

Explicit logic:
- A chat cannot label an item ACCEPTED without a reviewed and merged/accepted GitHub decision.
- A local Kiro commit is LOCAL_ONLY until actual origin readback.
- For a science claim, source citation and reproducible program output are different evidence categories.
- Unknown test result is NOT_RUN or UNKNOWN, never PASS.
- Report contradictions between README, STATUS and Spec rather than silently deciding that one model is correct.
- Research handoff cannot authorize product app implementation; development may only implement after separately recorded user PRODUCT_GO.

## Example RESEARCH_TO_DEVELOPMENT (current R0)

    handoff_id: BL-20261116-R0
    from_role: RESEARCH
    to_role: DEVELOPMENT
    originating_ref: default branch at f9b2b026b2d619f3c2c764a5149975363e4fb724
    approval_class: PROPOSAL_ONLY
    evidence_level: SOURCE_REVIEWED
    synchronization: EXAMPLE_ONLY
    summary: Sama-COCO is correlated with COCO; S3 from-scratch blind label protocol drafted, NOT executed
    blockers: G1/G2/G3/G4; cross-family review incomplete
    allowed_next: inspect code architecture on paper; review proposed contracts
    forbidden_next: download model weights; infer; implement production app; claim standalone moat
    next_owner: Research, for GPT-5.6 Sol cross-family review

## Example DEVELOPMENT_TO_RESEARCH

    handoff_id: BL-YYYYMMDD-D001
    from_role: DEVELOPMENT
    to_role: RESEARCH
    approval_class: PROPOSAL_ONLY
    question: The rubric for S3 adjudication may not give independent consensus in a 2-person team.
    exact_spec_ref: .kiro/specs/blindspot-real-data-validation/requirements.md at full SHA
    why_it_matters: Changes regression false-block estimate and planned CI gate.
    test_to_disambiguate: blinded control annotation protocol and reviewer agreement
    requested_decision: Define INCONCLUSIVE case and adjudicator roles.
    next_owner: Research
