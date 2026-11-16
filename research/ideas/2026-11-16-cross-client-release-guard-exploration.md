# BLINDSPOT LAB — 사용자 문제 중심 제품 가설 확장 (2026-11-16 KST)

> **RESEARCH / NOT PRODUCT GO / NO SOFTWARE DEVELOPMENT IN THIS DOCUMENT.** 사용자는 제품 아이디어 연구를 계속하고, Kiro 개발 결과는 별도로 전달하기로 했다. 이 문서는 개발 브랜치를 변경하지 않는 독립 연구 분기의 아이디어 기록이다. 이하 사례는 **실제 공개 근거**와 **구상한 시나리오**를 분리한다. 이 문서의 수치 목표·평가는 실측 성능, 수요 또는 공모전 수상 가능성의 예측이 아니다.

## 1. 문제 정의를 다시 좁힌 이유

기존 Blindspot Regression Gate: 독립 주석→모델 버전 A/B 예측 비교→신규 실패·수정 분류→CI 차단. Phase4의 728개는 합성 사례(신규 회귀 38건)였고, 실제 객체 탐지 모델·인간 정답·경쟁 앱 직접 비교 및 고객 미해결 사례를 입증하지 못했다.

**직접적인 현업 문제 제보**: 2026-01-08 r/computervision 게시글에서 CV 제품 개발자가 한 고객 A의 데이터를 공통 모델에 포함하면 고객 B에 존재하지 않는 객체를 감지하는 식의 회귀가 생기며, 고객이 늘어날수록 전체 회귀 테스트가 오래 걸리고 릴리스 속도가 떨어진다고 1인칭으로 설명. https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/

- **증거 수준:** 공개 1인칭 자기보고; 동일 게시자가 현재 사용한 FiftyOne/Roboflow와 실패를 입증한 것은 아님. 식별 가능한 기업 고객·구매 의사·반복 빈도는 **확인 불가**. G4 미통과.
- 추가 커뮤니티 참고: 2026-09-28 r/computervision에서 입력 드리프트, 카메라 이동, 전처리 버그, 라벨 불일치를 서로 구별하기 어렵다고 토론. https://www.reddit.com/r/computervision/comments/1wsc1c6/what_production_cv_failures_are_hardest_to/ ; 복수 댓글이나 자가보고는 실험 검증이 아님.

**제품 질문 변경:** “모델의 평균 정확도가 향상됐나?”가 아니라 **“한 고객에서 개선한 업데이트가 다른 고객의 운영 조건·검수 기준을 망가뜨리는지, 제한된 검증 시간에 어떻게 확인하고 출시를 판단할 것인가?”**

## 2. 세 제품 가설

### P1. TenantGuard / Cross-client Release Firewall — **1순위 추가 연구 가설, 제품 선정 아님**

사용자: 여러 고객사(또는 여러 생산라인)의 컴퓨터 비전 모델을 공통으로 유지·업데이트하는 CV 엔지니어/릴리스 담당자.

**구체적 사용 장면 (가상의 예시):** 고객 A의 새로운 포장 자재 인식 데이터를 추가한 모델 B가 평균 F1을 개선한다. 하지만 고객 B에는 실제로 없는 포장 종류를 탐지해 출하 분류 오류를 낸다. 담당자는 평균 점수가 아닌 **A/B/C 고객별 신규 실패·수정·검증 불가**를 보고 업데이트를 승인/보류한다. 이 특정 시나리오는 실제 제보의 구조를 설명하기 위해 만든 예시이며 실측 결과가 아니다.

제품 화면: 릴리스 후보 업로드 → 고객/공정별 위험 카드 → “새로 실패한 장면” 원본·두 모델·주석 확인 → 재현된 회귀 테스트 → 조건별 배포 판정 보고서.

**검증 가능한 독자 엔진 가설 (구현 전):**
1. **Change Impact Graph**: 학습 데이터 변화/고객별 평가 샘플/운영 조건 사이의 관련성 그래프를 추정해 어떤 고객·조건의 재검증이 우선인지 제안. 인과관계를 안다고 주장하지 않는다.
2. **Constrained Test Allocation**: 제한된 추론·사람 검수 예산 안에서 고객별 최소 무작위 감시 샘플 + 회귀 위험 기반 우선 검사 샘플을 함께 할당. 확인하지 못한 범위는 무조건 **UNTESTED**, 애매한 주석은 **ABSTAIN**. “선별 검사만으로 모든 회귀를 찾았다”는 보장은 금지.
3. **Tenant-aware Release Contract**: 고객별 피해 비용/중요 클래스/조건별 차이를 명시하고 개별 배포 판정 + 근거 SHA/체크포인트/설정/JUnit/재실행 결과를 묶은 리포트 생성. 검수 완료 전 자동 GO 금지.
4. (선택형) 원본 프레임·최종 입력 텐서·전처리 버전의 해시를 구분해 “모델이 변했는가 vs 입력 파이프라인이 변했는가”를 재현 검사.

**반증:** FiftyOne의 그룹/슬라이스 평가 + 짧은 CI 스크립트만으로 같은 결과를 같은 시간에 내면 독립 제품으로 NO-GO. 고객별 데이터 접근권/프라이버시가 막히거나 선택식 검사에서 중요한 회귀를 놓치면 가설 축소.

### P2. Pipeline Twin / Failure Attribution Lab — **대안**

사용자: 모델·카메라·전처리 변경이 동시에 발생하는 현장 CV 엔지니어.

장면: 기존 모델/새 모델 각각 정상으로 보이는데 신규 영상에서만 표지 검출이 사라짐. 원시 프레임과 모델 입력 텐서를 보존하고, 가능한 구성요소를 **구버전/신버전으로 통제 교환**하여 디코딩·크롭·색상 채널·정규화·모델·후처리 중 변화를 재현한다.

기술 가설: \`old/new preprocess × old/new model × old/new postprocess\`에 대한 작은 요인 실험을 실행해 어느 교환 조건에서 출력이 달라지는지 기록하는 **counterfactual replay matrix**. “원인 규명” 표현은 통제된 재실행에서 확인된 구성요소 영향에 한정하며, 실제 카메라 또는 현장 도메인 변화의 인과관계 전체를 증명하는 것으로 확대하지 않는다.

기존 Arize의 임베딩 드리프트·슬라이스별 성능 추적과 Roboflow 모니터링이 관련 문제를 이미 다룬다. “디버깅 화면”만으로는 차별화 부족; 실제 입력 텐서의 비트 단위 재현 및 구성요소 스왑의 오류 국소화 정확도 측정 필요.

### P3. Blindspot ProofPack / Verified Oracle Release Evidence — **보조 모듈 후보**

사용자: 데이터 주석을 신뢰하기 어려운 CV 품질 담당자.

장면: 모델 B가 정답과 다르다는 이유로 릴리스를 막았지만, 원래 정답 박스가 잘못 작성됐을 수 있음. 비교 실험과 독립적인 인간 검수로 \`CONFIRMED_REGRESSION / LABEL_DISPUTE / ABSTAIN / NOT_TESTED\`를 구분해 재현 가능한 증거 패키지 생성.

기술: 모델 출력에 의존하지 않는 blind-from-scratch 라벨링, 주석 지침/검수자 독립성 체크, 원본 해시, 오류 유형별 원인, 원격 CI 포맷.

FiftyOne의 \`compute_mistakenness\`는 라벨 실수를 이미 **점수화/정렬**한다. 단순 라벨 오류 발견은 신규 기술이라고 주장 불가. 실제 차별화는 “독립 검증·승인 책임·재현 증거 체인”이 사용자에게 주는 측정 가능한 비용 절감에 있음.

## 3. 현재 제품 포지셔닝 비교

| 업체/접근 | 공식적으로 확인된 이미 있는 기능 | 우리에게 남는 검증 가설 |
|---|---|---|
| FiftyOne core + community Model Comparison | 객체 단위 평가·TP/FN/IoU, \`hitmiss\`, \`misshit\`, 위치 개선/악화 | 고객별 우선순위/실패 감별/CI 증거를 사용자 최소 노력으로 통합하는 것이 더 나은가? |
| FiftyOne Brain + groups | 주석 오류 의심 점수, 누락·허위 객체 후보, 그룹/슬라이스 필터 | 검증 출처·blinded oracle·리스크별 테스트 예산·출시 결정을 별도 확인할 가치가 있는가? |
| Roboflow | 모델 비교(정확도/지연시간)와 운영 모니터링/알림 | 고객별 cross-client 신규 실패의 검수·차단 워크플로를 동등 조건에서 비교 |
| Arize | ML/컴퓨터비전 임베딩 드리프트·성능 슬라이스·원인 분석 | 전체 운영 모니터링을 복제하지 않고 변경 전 품질 증명을 확실히 개선하는가? |

FiftyOne community plugin's published TODO notes unmatched **false-positive comparison tallies** are not fully in its current operator, but this is one narrow plugin limitation, not a market-sized independent product gap. A user can write scripts. Baseline must include a competent short-script extension, not artificially weak GUI-only comparisons.

URLs:
- https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- https://docs.voxel51.com/user_guide/evaluation/detections.html
- https://docs.voxel51.com/brain.html
- https://docs.voxel51.com/user_guide/groups.html
- https://roboflow.com/blog/compare-trained-models
- https://roboflow.com/blog/model-monitoring
- https://arize.com/products/ml-cv-observability/

## 4. 엔진 차별성의 실험 설계 (모두 제안, 미실행)

A. **고객별 회귀 발견**: 동일 이미지/라벨/모델 버전, 고객별 데이터 구간에서 신규 실패와 수정 개수. Full evaluation = reference; FiftyOne+short-script = strong incumbent; random, stratified, prioritized budgeted tests = equal-budget comparators.

B. **선별 평가 신뢰성**: 누락된 고위험 실패 비율·고객별 최소 커버리지·진짜 신규 회귀를 발견하기까지 필요한 추론 횟수, 예산 초과 시 \`UNTESTED\`. **검증 누락이 있으면 안전하다고 보증하지 않는다.** 2025 연구는 기존 신경망 테스트 선택법이 자신 있게 틀린 사례 등에 취약하여 탐지 상대 커버리지가 최대 86.85% 떨어질 수 있음을 보였다. https://doi.org/10.1145/3715693

C. **원인 국소화**: 원시 프레임/최종 텐서/전처리/후처리의 조합을 통제한 실험에서, 실제 바꾼 구성요소를 진단하는 성공률과 재실행 정확도를 측정. 도메인 shift와 코드 regressions는 구분해 라벨링.

D. **업무 가치**: 같은 7단계 결과물을 만들 때 오탐(잘못된 차단), 놓친 위험(거짓 안전), 엔지니어 분 단위 투입, 스크립트 양·지속 관리 부담을 FiftyOne+short-script 및 Roboflow와 비교. 단독 GUI 대비 시간 절감만으로는 기술 독창성 입증 불가.

E. **민감 고객 데이터**: 고객 원본 영상의 중앙 업로드를 강제하지 않는 local-first 경로 또는 해시로 요약된 메타데이터 반출. 여러 고객이 데이터를 서로 보지 못하도록 권한 격리를 설계·검증해야 함. 이 부분은 연구 가설이며 구현·보안 인증 완료가 아니다.

제안하는 제품 GO 기준(실측 아님): 식별 가능한 동일 사용자/조직이 기존 도구를 실제 사용하고도 해결하지 못한 업무를 입증(G4) + 강한 비교군 대비 유의미한 운영상 장점 + 중요한 회귀의 누락과 잘못된 차단 모두 공개 평가 + 사람 라벨 독립성의 근거 + 공모전 내 동작 데모 가능성.

## 5. 19일 남은 공모전 기준의 제품 의사결정

공식 Kiroween 2026은 2026-12-04 14:00 Pacific (2026-12-05 07:00 KST) 마감. 5개 심사축은 잠재 영향·Kiro 구현·디자인·혁신·발표 각 20%다. (출처 https://kiroween.devpost.com/rules).

- **2026-11-16~18 아이디어 연구:** 이 연구 문서와 별개로 실제 한 조직이 겪는 “A 고객 업데이트→B 고객 회귀→기존 도구 사용에도 불충분”의 연결 증거를 추가 수집. 현 단계에서는 원래 게시글 하나만 확인.
- **2026-11-19 전 후보 압축:** P1의 고객·출시 회귀 증거가 없다면 P2 현장 파이프라인 실패/입력 텐서 사례와 비교. 기술·사업적 독창성 가정에 미실행 표시.
- **2026-11-20 전 조건부 투자 판단:** G4와 경쟁 제품 차별화 증거에 따라 P1/P2/P3 중 방향 제안 또는 새 문제로 피벗. 기존 Phase5 G1-G3는 유용한 기초 연구이지만 고객 문제 정의를 대신하지 못한다.
- **데모 3분:** 변경 전 평균성능이 정상 → 고객 B 회귀가 발생 → 원인/불확실성/검수 증거 표시 → 릴리스 차단/보류. **실험 실제 결과와 연출 시나리오를 표시해 혼동하지 않는다.**

카테고리 후보는 **Frankenstein** (컴퓨터 비전 + CI/릴리스 엔지니어링 + 인간 주석 증거 + constrained test selection). 적합성은 카테고리 정의를 토대로 한 해석이지 공식 승인이나 우승 확률이 아니다.

## 6. 결론 / 제안

**현재 최우선 탐구 제품은 “고객별 CV 모델 업데이트 회귀 위험을 검증하는 TenantGuard / Cross-client Release Firewall”. 최종 제품은 여전히 미선정.**

왜 이쪽이 기존 Blindspot Gate보다 낫다고 가설을 세우는가: 실제 1인칭 문제의 업무·고객·실패·릴리스 지연 구조와 대응하며, UI/CI/검수 증거를 한 흐름으로 보여줄 수 있다. **반증 위험도 큼**: FiftyOne grouped evaluation + 간단한 스크립트로 해결될 수 있으며, 테스트 선택법은 실제 실패를 놓칠 수 있고, 기업의 고객별 데이터는 얻기 어렵다.

다음 대화의 우선 연구: **동일 사용자의 문제+기존 해결책 적용+남은 미해결성**을 증명하거나, 증명이 안 되면 P2/P3 혹은 다른 실업무 후보로 전환. Kiro 개발 결과 검수는 사용자가 완료 보고를 전달한 경우에만 별도로 수행한다.

## 검토한 선행연구
- 2023 CHI 현장 연구: https://agathe-balayn.github.io/assets/pdf/chi23_Balayn.pdf — 비전 모델 배포 전 실패 처리의 비표준성·다중 이해관계자.
- 2025 KBS 논문: https://www.sciencedirect.com/science/article/pii/S0950705125003399 — 심층모델 업데이트 회귀 이슈, 단순 평균 성능과 구분.
- 2025 ACM TOSEM: https://doi.org/10.1145/3715693 — 기존 DNN 테스트 선택법의 취약성.
- 2026 산업 영상검사 종설: https://www.mdpi.com/2079-9292/15/12/2727 — 조명·카메라·라인별 운영변화와 배포 재검증.
- 2026 AI 시스템 테스트 체계적 매핑: https://www.mdpi.com/2076-3417/16/19/9787 — oracle·연속 수정·사회기술적 문제의 지속적 한계.

**PROVENANCE:** Research authorship ChatGPT GPT-6 + verified linked public sources and existing project materials. No code modified, no model evaluated, no Kiro session/credit spent here.