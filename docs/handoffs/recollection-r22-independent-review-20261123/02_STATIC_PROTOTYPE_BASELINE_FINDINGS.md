# Re:Collection — archived v0.2 HTML static inspection evidence

**Inspection date:** 2026-11-23 KST  
**Scope:** `Archive_Detective_Product_Demo.html` (archived Project/Library original) **ONLY**, not R2.2 Windows app.  
**Method:** Read the actual 68-line, ~37,362-character HTML/JS through the authorized Files reader, then apply 13 **non-executing** pattern checks. No browser execution, no screenshot rerender, no model call or local Windows source access. The 13/13 count means all inspected features/patterns were located; **it is not a 13/13 runtime test pass**.

## Static observations: 13 checks performed

| # | Observed in original source | Result |
|---|---|---|
| 01 | Embedded synthetic source IDs `ARC-P01` / `ARC-L02` | PRESENT |
| 02 | Initial browser state `DEMO_APPROVED`, revision 1, approved revision 1 | PRESENT |
| 03 | `visitor`, `curator`, `evidence`, `report` view routing | PRESENT |
| 04 | Reference to source field `ARC-L02#field.serviceStatus` | PRESENT |
| 05 | Q1/Q2 multiple-choice interaction renderer | PRESENT |
| 06 | Ledger change calls `invalidate(['CL-02','Q2','F2','approval'], ...)` | PRESENT |
| 07 | Rights toggle invokes `invalidate(['media','publication','approval'], ...)` | PRESENT |
| 08 | Visitor path checks for `DEMO_APPROVED` status | PRESENT |
| 09 | No network `fetch`, `XMLHttpRequest`, `WebSocket` or `EventSource` in this original file | NOT FOUND |
| 10 | Explicit caveat that AI generation, real approval signature and server are unimplemented | PRESENT |
| 11 | No evident general `GeneratedDraftV1`, `GeneratorProvider` or allowed scene-block registry | NOT FOUND |
| 12 | JSON export serializes `serviceStatus` and `rights` in an offline audit snapshot | PRESENT |
| 13 | Explicit synthetic/offline demo marking | PRESENT |

Static checks are **source-presence observations**, not proof of correct event ordering, browser security, license enforcement, real cross-source inference, accessible render, or compatibility with B0–B5.2.

## Actual archived content

- Source 1: fictional 1952 R1 route plan; `proposalStatus=PROPOSED`. Q1 asks whether existence of a plan proves opening. Correct logical direction: NO.
- Source 2: fictional 1956 R1 operation ledger; `serviceStatus=NOT_RECORDED`. Q2 asks for the **literal ledger value**, which is correctly not automatically interpreted as 'the route was never operated'.
- Main interaction flow: opening → inspect two fields → answer Q1 and Q2 → result; creator view and change/rights simulation are adjacent navigational views.
- Source impact path `ARC-L02.serviceStatus → CL-02 → Q2/F2` is explicitly represented. Changing the ledger causes whole visitor experience to become stale; the partial-impact view is **a simulated explanation**, not proof of a production field-level invalidation graph.
- Rights revocation suppresses the ledger SVG and gates the visitor. The audit export includes synthetic values and the browser in-memory state remains in client-side JS, so the feature **must not** be presented as real rights/secret-data revocation across cached or server distribution paths.
- `DEMO_APPROVED` is preset when initializing state. This is **not** actual curator approval.

## Experience-level findings

1. **Keep:** source disclosure, evidence IDs, Q1 distinction between planning and actual execution, feedback with explicit provenance, clear stale/rights states, separate curator and visitor views.
2. **Improve after R2.2 review:** Q2 is a direct-value lookup, not yet an engaging cross-document deduction. Add a supported Evidence Compare and final Judgment block without weakening claim limits.
3. **Do not fake:** a full AI authoring pipeline, real archival source validity, server rights enforcement, Kiro implementation credit, real source-field graph completeness or visitor user-study results.
4. **Compatibility note:** archived v0.2 IDs (`ARC-P01/L02`) are not interchangeable with separate `ARC-01/ARC-02` fixture names used in subsequent planning. Require an explicit adapter/mapping if these datasets are connected.

## Current verdict

`ARCHIVED_V02_STATIC_INSPECTED / R22_RUNTIME_UNVERIFIED / R22_USER_CONTENT_REVIEW_PENDING`

**Next gate:** run the separate R2.2 independent review execution packet on the user's Windows machine and present **real** content/screenshots. Do not mark B-option block development approved until that review is accepted.
