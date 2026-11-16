# Kiroween 2026 — DATA ACCESS FIRST: ConstraintForge vs FlowTwin
2026-11-16 KST | **idea planning + local synthetic proof only** | Product: UNSELECTED | Kiro app development: NOT STARTED BY THIS REVIEW

## Decision in one paragraph
기업 내부 DB/API가 없는 두 명의 개발자도 **합성 사례**로 두 후보의 계산 구조를 시험할 수 있다. 하지만 실제 업무 의사결정에는 사용자 보유 입력/현장에서 새로 생성한 이벤트 중 하나가 필수다. **ConstraintForge를 로컬 소유 일정표 기반 소규모 결근 복구라는 조건부 후보로 유지**하고, **FlowTwin의 기업 운영 시뮬레이션/실시간 예측 단독 제품은 현재 보류**한다. 합치면 입력·정답·신뢰도 문제가 두 배가 되므로 당장은 결합하지 않는다. 이것은 사용자 가치/경쟁우위 인증이 아니라 **데이터 진입 가능성과 계산 오라클에 대한 결정**이다.

## 1. First-use data acquisition — no enterprise API
| Candidate | Direct user-provided or in-use captured input | Minimum to claim actual output | When input missing | Initial verdict |
|---|---|---|---|---|
| ConstraintForge | User-owned simple CSV or editable roster of tasks+time+required skills, people+availability, previous assignments, a disruption | A concrete plan sufficient to check time conflict, eligibility and reassignment count | **DATA_MISSING / REQUEST_INPUT**; demo example is synthetic only | CONDITIONAL |
| FlowTwin | Tap-recorded event starts/completions, capacity, service definitions; measured durations as they accrue | Current observed activity (counts, means); for **credible forecast**, separate calibration + validation | **NO_PREDICTION**; do not pretend historical distributions are known | HOLD |
| Combined | Both roster + event log + consistent IDs | Both independently validated inputs | Missing either prevents credible joint result | NO-GO for initial MVP |

A sample dataset bundled with an app is **only a tutorial**; it does not prove the user's actual organization can be optimized. CSV import is not magic auto-discovery: users without a roster still must enter roles/availability. No special permissions, private ERP or paid cloud service assumed.

## 2. Executed local algorithmic sanity check (NOT a user test)
Input: **synthetic** 6 volunteers A–F, 6 tasks T1–T6 across two nonoverlapping time slots (09:00 and 10:00), roles check-in/guide/tech, worker availability and role eligibility frozen, no dual assignment in the same slot. Minimize the **number of task owners that change** from a fixed prior roster. Verify every complete eligible assignment by Python `itertools.product` exhaustive enumeration, not an LLM-generated score.

| Worker | Allowed role(s) | Available hour(s) |
|---|---|---|
| A | check-in, guide | 09, 10 |
| B | tech | 09 |
| C | guide, tech | 09, 10 |
| D | check-in | 10 |
| E | guide | 09 |
| F | tech | 10 |

Current assignments: T1 (09 check-in)→A, T2 (09 guide)→C, T3 (09 tech)→B, T4 (10 check-in)→D, T5 (10 guide)→A, T6 (10 tech)→C.

**Observed synthetic test 1:** With B absent, there are **4 valid complete assignments** under the frozen constraints; the smallest change is **2 task reassignments**: T2 from C to E, and T3 from B to C. The other 4 jobs are unchanged. This is an exhaustive small-input optimum, **not** an observed real employee/staff outcome.
**Observed synthetic test 2:** With B and E both absent, there are **0 valid complete assignments**: at 09:00 three tasks require different people but only A and C are available/eligible for any 09:00 work. Output is `INFEASIBLE`, not an invented employee or unsafe PASS.
**No large-scale benchmark, real user study, Timefold API parity run, or actual wait forecast has been done.**

QA: /mnt/data/_data_access_gate_20261116/synthetic_enumeration_qa.json includes exact counts/assignments, replayable pure logic in the published interactive concept viewer. HTML browser sanity checks passed at 390/768/1024/1440px for default 4 feasible / 2 changes, simultaneous absences 0 feasible, event count changes and no horizontal overflow or JS errors. This research visualization is **not** a Kiro-created competition app.

## 3. Strong established alternatives (DO NOT erase)
- **Timefold** already supports real-time employee shift replanning after sick leave, minimizing disruption with weighted rules, score analysis that explains why a specific assignment was not made, and required vs preferred constraints. The **existence of minimal schedule repair/constraint explanation is NOT our novelty**.
- **Google OR-Tools** CP-SAT supports optimal/feasible/infeasible status and an assumption-based infeasibility analysis. Its minimized assumption core is not necessarily globally minimum by itself, per official troubleshooting. Again, merely showing no solution/violations is not unique.
- **Waitwhile** already logs live queue activity and offers custom service-duration defaults, historical estimates, and an auto model trained on many locations. It does **not require a particular customer's 50 previous visits** to configure every wait-time estimator; 50 is documentation guidance for its historical-mode estimates. Zero-configuration capture and prediction are not novel as claimed.
- **SimPy** supports process-based discrete-event simulation; making an event loop is a base library capability.

Primary docs consulted 2026-11-16:
1. https://docs.timefold.ai/employee-shift-scheduling/latest/real-time-planning
2. https://docs.timefold.ai/employee-shift-scheduling/latest/user-guide/score-analysis
3. https://docs.timefold.ai/employee-shift-scheduling/latest/faq
4. https://developers.google.com/optimization/cp/cp_solver/
5. https://github.com/google/or-tools/blob/stable/ortools/sat/docs/troubleshooting.md
6. https://help.waitwhile.com/en/articles/6762645-how-wait-time-is-estimated
7. https://help.waitwhile.com/en/articles/10047167-how-to-configure-wait-time-estimation
8. https://simpy.readthedocs.io/en/stable/topical_guides/simpy_basics.html

## 4. Distinctive-value hypothesis — pending falsification
The only **candidate user job** worth measuring next is:
> “I already own a small volunteer roster. One person is suddenly unavailable. Without a consultant or company account, tell me what **must** change, what **cannot** be satisfied, and give me a plan I can actually approve.”

The differentiator cannot be “AI plans shifts” or “minimal disruption”; Timefold does both. A credible additional product outcome would require a measured improvement in:
- time from **user-owned unstructured/CSV roster** to trustworthy usable schedule,
- comprehension of the **trade-off / why no plan exists**,
- review/acceptance of constraint relaxations **without violating explicit hard constraints**,
- privacy and reproducibility (local-first hash of input, constraints and results).

These are **candidate comparative metrics**, not proven advantage over Timefold. OR-Tools remains a strong scripting baseline. If competent use of those tools reaches parity, **NO-GO as standalone product**.

## 5. Single next test, no infinite idea drift
1. Provide the **two simple CSV input contracts** (tasks and workers) from an existing, owned, consented roster. No personal data committed publicly. A mock CSV can prove only schema acceptance, not user need.
2. Ask whether a first-time intended user can make a usable file from their actual roster with little setup. Time and record corrections; do not fake a 15-second activation without test.
3. Use the same exact imported roster and shock in a basic Timefold/OR-Tools setup; compare number of user actions, initial setup time, explanations, results and acceptance; **do not pay for a plan or use private materials without authorization**.
4. If high friction or no significant difference, mark `ConstraintForge (staffing) NO-GO`; no expanding to delivery/manufacturing simply to save the concept.
5. FlowTwin can be revived only if it has a **distinctive decision before historical data**, not a queue dashboard already in Waitwhile. Needs an actual user and evidence. Do not combine with B yet.

## Product/Kiro status
- Product selected? **NO**.
- Data independently obtained from an enterprise? **NO**.
- Model inference or deployed Kiro app changed? **NO**.
- Changed GitHub branch: this independent research branch only. **DO NOT** merge into Kiro development without explicit product decision.
- Winner potential or hard-to-replicate engine established? **NO**.

## Files created for review
- `research/data-access/2026-11-16-data-gate-viewer.html`: offline conceptual interactive 6-shift exhaustive enumerator + opt-in synthetic event counter.
- `research/data-access/2026-11-16-data-gate-research-proof.json`: exact synthetic test inputs/results and caveats.
- Korean A4 PDF: `KIROWEEN_DATA_ACCESS_FIRST_DECISION_20261116.pdf`, distributed as conversation artifact, not part of GitHub because current connector's file-write is text-only.

No background work, reminders, Kiro credits or externally charged services used.
