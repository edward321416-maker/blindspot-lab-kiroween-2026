# ChangeScope — Incumbent Unmet-Need Research SOP v1.0
작성일 2026-11-16 KST · 책임 범위: **아이디어 기획 및 공개 근거 조사** · **상태: 계획 작성, 조사 전용, 제품 미선정**
기준 문서: `research/plans/2026-11-16-incumbent-unmet-need-investigation-plan.md` (blob `38325f528c1fa0a98792b6f62604834fe442d145`). 기존 연구 문서의 Q1–Q5, S1–S4, E0–E4, J1–J10, T1–T3, D0–D5를 아래 운영 절차로 구체화한다. **원래 문서의 기준을 대체하거나 완료 결과를 발명하지 않는다.**

## 0. 조사 목적과 귀무가설
- H0 (기본 가정): FiftyOne+합리적인 Python/CI, Roboflow Workflow Evals 또는 AWS 카메라별/고객별 모델 운영 방식으로 해당 팀의 실무 문제를 해결할 수 있다.
- H1 (제품 가설): 같은 사용자의 구체적인 모델 릴리스 작업이 기존 해결책을 실제 적용한 뒤에도 막혀 있고, 신규 ChangeScope 기술이 해결 가능하며, 동등 조건 비교에서 실질적 추가 가치가 있다.
- **중립 원칙:** 당사 제품 가설을 입증할 의무는 연구자에게 있다. 문서에 없는 기능=미지원 아님. 커스텀 스크립트가 필요함=미해결 아님. 일부 사용자 불만=상용 수요 아님.
- **금지:** 동일 팀·동일 업무를 확인하지 않고 서로 다른 사람의 고충과 경쟁 제품의 한계를 합쳐 E2로 승격하는 행위. 개인 신원 역추적, 비공개 자료 수집/공개, 임의 연락, 권한 없는 서비스 접근, 유료 계정/클라우드 실행.
- 초점: **고객 A의 학습 데이터 변경 뒤 고객 B에서 새로 생기는 오류**, 다수 고객 회귀 검사의 릴리스 병목, 고객별 모델 분리의 현실적 대안.

## 1. 연구 구성 및 책임
- **프로토콜 담당:** 질문·판정 기준 및 제외 조건 고정(연구 시작 전에 commit 기록).
- **원문 수집 담당:** URL, 작성일, 검색 경로, 원문/답글, 상반 증거를 각각 카드화. 익명 계정을 탈익명화하지 않음.
- **독립 검토 담당:** 다른 시각 또는 다른 모델로 동일 카드의 사건 동일성·등급·기능 주장 재심사. 원자료를 직접 읽으며 1차 판정 결과를 보지 않고 독립 기록한 후 비교.
- 한 사람이 복수 역할을 맡을 경우 **독립 인적 검증으로 주장하지 않는다**. 모델 간 리뷰는 독립 인간 심사나 실제 엔지니어 사용 검증을 대체하지 못한다.
- 불일치 처리: 다수결로 사실을 생성하지 말고 `CONFLICT/UNVERIFIED` 및 양측 출처를 함께 보존. 판정에 중대한 불일치는 HOLD.

## 2. 연구 질문의 실행 가능한 의미
**분석 단위 = 사용자/팀 한 주체 × 하나의 업무 × 하나의 릴리스 변경 × 실제 적용한 기존 해결책.**
- Q1 누가/어떤 모델 공유 구조에서 무엇을 바꿨는지, 변경과 새 실패의 시계열이 설명되는가?
- Q2 사용한 솔루션의 이름·제품 버전·플랜·설정·스크립트·운영 방식을 실제 사용자 자신의 말이나 공개 로그로 확인하는가?
- Q3 적용 결과가 실패/보류였다면 그 *남은 작업*은 무엇인지: 미검출/오탐, 검증 시간, 원격 데이터 권한, 고객 분리, 비용, 정답 분쟁, 릴리스 승인?
- Q4 제품 기능/추가 코드/설계 변경 등 현실적 대안으로 작업을 완료할 수 있는가? 비용/권한은 근거가 있는가?
- Q5 새 기술이 필수인지, 그 우위를 실험으로 **반증 가능하게** 정의할 수 있는가?

## 3. 증거 단위, 판정 및 중복 방지
### 3.1 5개 등급 유지
- `E0`: 제품 마케팅·공급자 가이드·연구자 해석만 존재. 기능 참고이며 사용자 미해결 증거가 아니다.
- `E1`: 실제 업무 주체가 문제를 1인칭으로 설명. 기술·조직·도구 사용은 확인된 만큼만.
- `E2`: **같은 팀/사건**에서 사용한 기존 제품/합리적 우회 해결책의 시도와 *잔여 실패*가 연결된 1차 원문. 실재 업체명 공개는 필수 아님; 공개 작성자 일관성/사건 연결 증거는 필수.
- `E3`: E2 + 실행 설정·이슈/PR·동일 사건의 로그·릴리스 지연/비용 등 재현·수량 근거.
- `E4`: E3 또는 동일 작업의 외부 검증 가능한 비교로 기존 강한 솔루션 대비 실측 효용이 확보됨. 연구자가 만든 데모만으로 E4 불가.
- **2026-01-08 Reddit 사건은 E1:** 공유 모델 A→B 문제와 검증 지연은 1인칭이나, 실제 FiftyOne/Roboflow/AWS 사용이 적혀 있지 않음. E2 미확보.
- 출처 중복: 기사 재게시/검색 결과/인용 스레드가 같은 원문 사건이면 `canonical_case_id` 1개. 한 사람의 후속 댓글은 같은 카드의 증거 추가. 다른 작성자는 별도 사건.
- `UNKNOWN`과 `NO` 구분: 현재 증거가 안 보이면 UNKNOWN. NO는 공식 지원 범위에 따른 부재 증거 또는 정당한 실행의 재현 실패가 있을 때만.

### 3.2 사건 카드 필수 항목
자세한 양식은 `research/protocols/templates/CASE_EVIDENCE_CARD.md` 참조.
- identity-proof는 공개 원문에서 **같은 작성자/팀의 업무 동일성**까지만 적는다; 실명 추정 금지.
- `source_type`: FIRSTHAND/MAINTAINER/OFFICIAL_DOC/SECONDARY/INFERENCE
- `incident_key`, `source_url`, 작성·조회 날짜(KST), 문맥, 실제 시도 솔루션, 미해결 결과, 반대증거, 등급 근거, 원문 URL.
- 원문 인용은 개별 출처당 25단어 이내, 나머지는 사실에 충실한 요약+링크.
- 자료에 없는 고객명/계약금/검증시간/고객 수는 `UNVERIFIED`, 추측 수치 입력 금지.

### 3.3 교차검토 최소 체크
사건 카드마다 6개: (a) 1차 원문? (b) 같은 주체? (c) 같은 릴리스? (d) 도구의 실제 사용? (e) 남은 장애 확인? (f) 상반 해법? 항목 하나가 불충분하면 E2 승격 보류.

## 4. 재현 가능한 공개 자료 검색 절차
### 4.1 검색 로그
각 검색은 날짜/검색엔진/정확한 검색식/상위 검토 URL·열람 결과·채택/제외 이유를 적는다. 결과가 0이면 **그 쿼리에서 발견 0**이지 시장에 문제 없음이 아니다.
검색 예시 (초기 고정 세트):
1. `"shared model" "clients" "regressions"`
2. `"model update" "other clients" "false positives"`
3. `site:reddit.com/r/computervision/ "clients" "testing" "regression"`
4. `"fiftyone" "model comparison" "client" "problem"`
5. `"roboflow" "eval" "multiple customers"`
6. `"sagemaker" "per-camera" "retraining" "regression"`
7. `site:github.com/voxel51/ "regression" "model"`
8. `site:discuss.roboflow.com "eval" "regression"`
검색식은 탐색 후 확장 가능하지만 추가된 검색식을 별도 기록하여 선별편향을 노출한다.

### 4.2 선별·제외 결정
INCLUDE: 날짜/원문 접근 가능, 실제 업무의 행동/사건 확인 가능, 문제 또는 직접 기능 실증. 채택 여부는 주장별 기록.
EXCLUDE: 스크린샷 없는 홍보/근거 없는 집계, 출처 불명 복제, 작성자를 동일인으로 단정한 제삼자 추론, 단순 "이 기능 있었으면" 추측은 E2에 불가. 마케팅은 E0 기능 후보로 기록 가능.
- 삭제/404 자료: 확인 가능한 원래 문구 없으면 E2 근거로 불인정, URL 접근 실패 기록.
- 댓글 작성일·제품 출시일 역전 주의: 사건 당시 존재하지 않던 기능으로 과거 사용자 미해결을 재단하지 말고, **2026-11 현재 가능한 해결책** 평가와 당시 상황을 분리한다.

## 5. 경쟁 제품 비교 프로토콜 — 강한 대안부터 인정
### 5.1 동일 업무 10단계 (J1–J10)
`J1` tenant data isolation/provenance, `J2` training delta lineage, `J3` old/new per-tenant TP-FP-FN,
`J4` per-tenant critical acceptance threshold, `J5` A-update→B-impact *prior* prediction,
`J6` fixed inference/review budget, `J7` independent GT dispute/ABSTAIN,
`J8` local/private image handling and CI, `J9` replay/evidence-ledger release decision,
`J10` dedicated-per-tenant-model alternative TCO.
참조 매트릭스: `research/protocols/templates/INCUMBENT_CAPABILITY_MATRIX.md`.

### 5.2 기능 상태 값
- `N` 제품 기본/공식 기능으로 직접 또는 매뉴얼에서 확인
- `C` 설정 조합으로 가능 (실제 설정/기능 이름 증거 필요)
- `S` 합리적인 사용자 스크립트/공식 SDK 사용으로 해결 (한도를 100 LOC로 **단정하지 않고** 작성·유지·검수 비용도 측정)
- `I` 유효한 솔루션 아키텍처 통합(예: AWS camera-specific models); 단일 앱 기능이 아니라도 **해결**로 인정
- `U` 확인 불가·플랜 미확인·해당 버전 문서 부재
- `X` 공식 제약/정당한 재현 테스트로 불가능·차단을 확인한 경우만
임의의 "없는 기능"에는 U를 준다. N/C/S/I면 결과를 제공할 수 있는 해결 방법으로 인정하며, 필요 인력/운영 비용을 별도 기록.

### 5.3 업체별 공정한 베이스라인
- **FiftyOne:** `evaluate_detections` (객체 TP/FP/FN, IoU), Model Comparison plugin의 `hitmiss/misshit`, group/view·Brain + 합리적 Python/CI 스크립트. 평가 시 OSS vs Enterprise 구분, 실제 라이선스·버전·설치/운영 비용 명시.
- **Roboflow:** 2026-11-12 Workflow Evals 공식 가이드의 Check/rules/version/publish gate/CI. Workspace plan, 데이터를 외부 서비스에 보낼 권한, 평가 규모/비용은 확인 전 U. 2026-01 사용자가 2026-11 기능을 썼다고 소급하지 않음.
- **AWS:** SageMaker camera-specific pipelines, Model Registry/quality gates, S3/IAM/Step Functions/Shadow Tests. 고객별 모델 분리/adapter가 문제를 제거하는 경우 별도 독립 제품 필요성은 낮아짐; 실제 비용과 조직 제약은 확인 필요.
- **ChangeScope:** 아직 **가설**. '변경 영향 사전 추정 + 위험·무작위 감시 표본 + 미검증 상태 표시'를 설명할 수 있지만 구현/성능 우위로 기재 금지.

### 5.4 기능 정보 검증 규칙
각 Jx×Vendor 셀마다 `version`, `edition/plan`, `direct_url`, `verified_at`, `claim_scope`, `status`, `evidence_quote_or_loc`, `usage_steps`, `extra_code`, `constraints`, `confidence`.
실행하지 않은 기능은 `DOC_VERIFIED`이지 `EXEC_VERIFIED`가 아니다. 공급자 판매 문구는 실행·고객 실패를 증명하지 않는다.

## 6. 추후 비교 실험의 사전등록 계약 (이번 단계에서는 실행 금지)
**실험 시작 조건:** E2+ 현업 업무 1건과 검증 가능한 빈틈이 확인되고, 자료 사용권/플랜/비용 및 비교 시나리오가 별도 승인됨.
- 입력: 동일 고객 그룹·같은 올드/뉴 모델 및 frozen predictions/이미지 해시/GT·오류 비용/실행환경/예산.
- 비교군: FiftyOne+short script, Roboflow의 native Check, AWS per-camera alternative, random·stratified·uncertainty·model disagreement, ChangeScope. 모든 솔루션이 꼭 동일 API 구조일 필요는 없지만 **같은 업무 성공과 비용**을 측정.
- 출력 7종: 회귀/수정, 미검증 커버리지, 정답 분쟁, 재현 manifest, 고객별 출시 판단, CI exit, 운영자 시간/비용.
- 원본 정답 독립성과 검증 샘플/홀드아웃을 강제. Sama-COCO처럼 상관된 재주석을 독립 GT로 계산하면 무효. 모델 출력에 의존해 자동 확인한 사례는 인간 독립 정답 아님.
- 시간은 시작/중단 기준을 모든 업체에 동일 적용. 로그인/프로덕션 권한·학습 선행 시간·반복 운영 유지 보수 비용은 별도 집계. 파라미터·모델 버전 차이 고정, 학습 누수 방지, 스크립트 크기 기준만으로 승패 결정 금지.
- **안전 판정:** 일부만 테스트한 고객은 `UNTESTED`, 주석 불명확 `ABSTAIN`, 실제 확인된 회귀만 `CONFIRMED`; 안전을 보증하는 PASS는 금지. 미검증 구간을 0개 결함으로 환산하지 않음.

## 7. D0–D5 운영 스프린트 및 납품 게이트
| Phase | 세부 행동 | 증거 산출물 | 수행 기준 |
|---|---|---|---|
| D0 | 2026-01 원문 1건, 3개 업체의 기준 기능 원문 잠금 | `source_manifest`, 사건 E1 카드 | 1차 URL/작성일/접근일 확인 |
| D1 | 사건/댓글/공개 이슈 중심 동일 사용자 증거 탐색 | E1~E3 카드, 검색 로그 | E2 연결 여부 따로 표시 |
| D2 | J1~J10 셀의 N/C/S/I/U/X와 반대 근거 기록 | 기능 매트릭스 | U를 X로 승격하지 않음 |
| D3 | 사용자의 해결 시도와 잔여 문제를 **같은 사건**에서 연결 | E2 후보 독립 검토 | 불일치 HOLD |
| D4 | 동일 업무 기준 baseline/실험 계약·비용 사전등록 설계 | `benchmark_preregistration` | 실제 데이터/모델/유료 도구 실행 X |
| D5 | 반증·기회비용을 명시한 연구 의사결정 | `decision_record` | GO-to-VALIDATE/HOLD/NO-GO/PIVOT |
권장 일정은 기존 계획 2026-11-17~19 KST 유지하되 **조사 목표 시간**이지 비동기 완료 약속이 아니다.

### 중간 QC 게이트 (각 단계의 종료 때 실시)
- Source Gate: URL/원문·날짜·카드 출처 확인. 미확인 사실과 조사자의 해석 분리.
- Identity Gate: 동일 작성자/팀/업무/변경·실제 솔루션 연결을 검증. 불명확하면 E1 유지.
- Baseline Gate: 경쟁 솔루션 세 업체에 강한 실제 대안 부여. 현재 문서/당시 기능을 섞지 않음.
- Reviewer Gate: 독립 재검토 결과 기록. 상반 근거 폐기 불가.
- Decision Gate: 반증에 따른 NO-GO 및 시간 제한에 따른 HOLD를 강제로 표기.

## 8. 의사결정 규칙
- **GO-to-VALIDATE(제품 선정 아님):** 같은 사례의 E2+ 1건 이상; 구체적 고객의 미해결 업무·권한/비용/시간 제약 확인; 주요 Jx에서 실질적인 잔여 제약; 강한 베이스라인에 반증 가능한 새 기술 가설; 합법적 데이터/최소 실증·3분 데모 가능.
- **HOLD:** E1만 확인됐거나, U 비중이 커서 기존 제품이 해결할 가능성을 배제 못 하거나, E2 동일성이 충돌하거나, 비교 실행이 없음.
- **NO-GO:** 사용자 업무가 N/C/S/I 기존 수단으로 충분하거나, 새로운 기술이 강한 비교군을 넘을 합리적 근거 없이 타 기능 복제만 하거나, 필요한 업무 자료/권한/시간이 없어 검증 자체가 출품 일정을 잠식.
- **PIVOT:** P2 Pipeline Twin 같은 다른 원인 분리 문제로 사용자 원문을 교체하고 별도 사건·새 프로토콜 생성. 기존 ChangeScope의 E2 충족처럼 표현 금지.
- 판정 기록에는 **찬성 근거 3건까지, 반대 근거 3건까지, 미확인 요소, 대안, 차기 비용/허가 사항**을 반드시 쓴다.
- E2 하나는 **기초 투자 적합성 신호**일 뿐, 제품 수요나 신규성의 확정·우승 가능성 예측이 아니다.

## 9. 사전 리스크 통제
- 잠재 독립 검수 편향: 둘이 모두 우리 제품 구상자라면 외부 인적 독립성 없음.
- 익명 데이터: 실명/회사·사적 주소 추적 금지. 사용자가 공개하지 않은 기업 신원 추정 불가.
- 공급자 플랜/클라우드: 미확인 가격·기능 U; 승인 전 결제/계정 연결/외부 데이터 업로드 금지.
- 공개 GitHub: 사용자 고객 정보·raw CCTV/얼굴 사진·개인 토큰·스크린샷·비공개 데이터 업로드 금지.
- 신기능 변화: 2026년 11월 12일 Roboflow 기능을 1월 사건에서 이미 쓴 것처럼 작성 금지. 이벤트 시각과 현재 경쟁 능력을 별도 열로 기록.
- 선별 데이터 편향: E2가 없는 결과를 더 많은 E1 숫자로 덮지 않는다.

## 10. 납품 구성 및 회귀 체크
- 마스터: 이 SOP, 기존 계획 문서, 카드/매트릭스/판정 템플릿.
- 이후 실제 조사 산출물: 검색 원장/원문 카드/근거 셀/완성 비교 시트/판정/출처 링크/한국어 PDF.
- 제출 체크: (1) 실제 사용자가 식별 가능한 동일 주체인지 (2) 제품 실제 시도와 결과인지 (3) 문서 vs 실행 분리 (4) 부재 주장 강한 근거인지 (5) 타사 강한 대안 포함 (6) 반대 근거 보존 (7) 결과로 오해할 가상 수치 제거 (8) 최종 GO는 아니라고 명시.
- Kiro 개발 브랜치 `chore/kiro-repo-bootstrap`, `.kiro/`, `apps/`, `packages/` **변경 금지**. 개발 결과는 사용자 보고가 들어온 뒤 별도 검토.

## 11. 원문과 추가 연구 링크
기준 원문: https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/
FiftyOne eval: https://docs.voxel51.com/user_guide/evaluation/detections.html
FiftyOne comparison: https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
FiftyOne grouped datasets: https://docs.voxel51.com/user_guide/groups.html
Roboflow regression Eval (2026-11-12): https://roboflow.com/blog/computer-vision-regression-testing
AWS fleet sample (2026-10-26): https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
AWS Shadow: https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html
