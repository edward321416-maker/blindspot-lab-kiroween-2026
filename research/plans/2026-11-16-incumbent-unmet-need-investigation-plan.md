# ChangeScope / TenantGuard — 기존 FiftyOne·Roboflow·AWS로 해결되지 않는 업무 조사 계획
**작성:** 2026-11-16 KST · **상태:** 조사 프로토콜 확정안 / 미실행 비교는 결과로 취급 금지 / 제품 미선정 / 개발 작업 범위 외

## 0. 조사 원칙

질문을 "왜 기존 제품은 못 하는가"에서 **"동일한 실제 개발팀의 고객 간 모델 회귀·출시 병목이 기존 솔루션과 합리적인 추가 작업으로도 해결되지 않는다는 증거가 있는가?"**로 수정한다. 기존 제품에서 해결된다면 ChangeScope는 독립 제품으로 NO-GO가 가능한 **반증 우선** 조사다.

**현재까지 직접 확인된 출발 사실 (2026-11-16):**
- 2026-01-08 r/computervision 1인칭 제보: 여러 고객이 공유하는 하나의 CV 모델, 고객 A 데이터 업데이트로 고객 B의 오탐·회귀 발생, 전체 고객 재검사로 출시 지연; **그 사용자가 FiftyOne/Roboflow/AWS를 시험했다는 자료는 아직 없음**. https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/
- FiftyOne: detection evaluation; community model-comparison plugin's hitmiss/misshit; grouped datasets/slice filtering. https://docs.voxel51.com/user_guide/evaluation/detections.html ; https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html ; https://docs.voxel51.com/user_guide/groups.html
- Roboflow (2026-11-12 공식 게시): Workflow Evals, 동일 검증 데이터 기반 버전 비교, 사용자 정의 Check, 배포 승인 게이트, Python·CLI·HTTP API·CI. https://roboflow.com/blog/computer-vision-regression-testing
- AWS (2026-10-26 공식 게시): SageMaker SDK v3의 **카메라별 모델** 학습·품질 게이트·버전 관리와 플릿 오케스트레이션. SageMaker Shadow Tests는 운영 지표/모델·서빙 설정 비교에 활용되지만, 별도 정답 없는 객체별 진실 판정은 자동 제공되지 않는다. https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/ ; https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html

위 공식 문서에 항목이 없다는 이유만으로 "불가능/미지원"이라고 판정하지 않는다. **미확인**으로 표기하고 다른 공식 자료·소스·실행·동일 사용자의 1차 근거로 보강한다.

## 1. 정확한 연구 질문과 조사 단위

**단위 = ONE USER/TEAM × ONE BUSINESS WORKFLOW × ONE RELEASE EVENT × ONE INCUMBENT ATTEMPT.**
서로 다른 조직의 고충, 제품 설명, 해결책 미사용 사례를 결합해 하나의 입증된 고객 사건으로 만들지 않는다. 익명 사용자는 본인이 공개한 업무 범위 내에서만 추적하고 신원 탈익명화는 금지.

- Q1 존재: 동일 팀이 정말 *공유 모델*에서 고객 A 개선 후 고객 B 퇴행을 직접 관측했는가? 재현 로그/개별 사건/테스트 기록 있는가?
- Q2 기존 해결: 팀이 FiftyOne, Roboflow Workflow Evals, AWS per-camera SageMaker 방식, 또는 자체 CI 스크립트/tenant-specific fine-tuning 가운데 무엇을 **실제로** 도입·시험했는가?
- Q3 미해결: 구현·설정·권한·비용·시간·정답 불확실성·데이터 격리 중 어느 제약 때문에 그 후에도 출시 판단이 막히는가?
- Q4 대안의 비용: 임베딩/불확실성 기반 선별, 층화 무작위 표본, 고객별 모델 분리를 포함한 현실적 베이스라인에서 무엇이 남는가?
- Q5 ChangeScope 필요성: **고객 A 학습 변경 -> 다른 고객 영향 예측**이 같은 자원으로 실제 회귀를 더 일찍 발견하며, 중요한 실패 누락률을 늘리지 않는가? 이것은 차기 실험 가설이지 이번 기획의 실행 결과가 아니다.

## 2. 우선 검증할 4개의 고객 업무 시나리오

**S1 공유모델 cross-tenant 회귀 (가장 직접적인 원문):** 사용자 한 명이 모델 A(v1)로 다수 고객을 서비스하다 고객 A 샘플을 추가한 B(v2)에서 고객 B에는 없는 클래스 오탐 발생, 회귀 검사 지연. 확인할 것은 실제 규모/검증 방식/원래 사용한 툴/수정 비용/고객별 데이터 정책. **고객명·수치·손실액은 근거 전까지 비워둔다.**

**S2 카메라별 모델 분리라는 대안:** AWS의 생산라인 사례에서는 공통 모델을 포기하고 카메라별 fine-tuning+검증+버전 관리로 대응한다. 고객별 모델 분리가 총비용/유지보수·데이터 권한에 어떤 제약이 있는지 확인한다. 이 방식이 충분하면 우리의 공유모델 release firewall이 불필요할 수 있다.

**S3 독립적으로 확인된 출고 오류 vs 라벨 오류:** 모델 B가 고객 B 이미지에 없는 물체를 검출한 것인지, 기존 GT에 빠진 물체인지, 데이터/클래스 매핑이 다른 것인지 분류. 실제 독립 GT가 없다면 LABEL_DISPUTE/ABSTAIN. FiftyOne의 mistakenness 등 기존 label-QA 지원까지 포함해 비교한다.

**S4 많은 고객에 대한 제한된 검증 시간:** 실제 엔지니어가 고객 수 증가 때문에 모든 고객 테스트를 반복할 수 없는 사건. 대체 방법 (병렬화, 캐시, 테스트 슬라이스, 축소 샘플, 고객별 모델 분리, 야간 배치/예산 제한) 적용 후에도 남는 지연·사고가 있는지 확인.

## 3. 증거 사다리 — 독립 제품 GO를 위한 최소 입증 수준

| 등급 | 확보된 증거 | 주장 가능한 범위 |
|---|---|---|
| E0 | 공급자 소개/마케팅/연구자의 추론 | 기능이 있거나 있을 수 있다는 가설; 고객 미해결 증거 아님 |
| E1 | 사용자가 한 문제를 1인칭 설명 | 고객 업무 문제 존재의 공개 사례 |
| E2 | 같은 사용자/팀이 구체적 기존 도구/방법 적용과 잔여 실패를 함께 설명 | **기존 해결책 적용 후 미해결 사례** |
| E3 | 같은 사례에 설정·오류 로그·시간/비용·재현 가능한 결과 또는 공개 이슈 대응 | 제품 필요성 판단에 강한 1차 근거 |
| E4 | 해당 사용자의 재검증/동등 업무 벤치마크에서 강력한 기존 해결 대비 정량 개선 | 제품 실효성에 대한 추가 실증 |

**엄격한 연결 규칙:** 동일 출처 인물/팀·동일 업무·동일 시기·동일 도구/대안. 단순히 FiftyOne GitHub 이슈와 다른 사람의 사용자 고통을 붙여 E2로 승격 금지. 익명 개인의 개인정보/회사 이름을 역추적하지 않는다. 불명확한 동일성은 UNKNOWN.

**최소 승격 목표:** E2 이상 **동일 사건 최소 1건** + 강한 기존 대안으로 해결 가능성을 직접 비교할 수 있는 명확한 미충족 작업. E1만 여러 건이면 HOLD. E3/E4는 후속 실험 강화를 위한 목표이나 이번 기획만으로 달성한 것으로 표시 금지.

## 4. FiftyOne·Roboflow·AWS 통합 기능 대비표 조사 설계

각 셀은 \`N(native) / C(configuration) / S(short script) / I(integration/architecture) / U(unverified) / X(reproduced unavailable/blocked)\`로 표기하고, **정확한 버전/플랜/링크/날짜/검사 방법**을 같이 기록한다. 엔터프라이즈 기능과 오픈소스 기능은 분리한다.

| 유효한 사용자의 Job Step | FiftyOne + plugin + ≤100 LOC 스크립트 | Roboflow Workflow Evals + CI | AWS SageMaker + camera/tenant-specific alternative |
|---|---|---|---|
| J1 고객/카메라별 데이터 격리와 provenance | group/view 기능 확인 후 실제 isolation 별도 검사 | workspace/project/permissions 검사 | IAM/S3/camera metadata 정책 검사 |
| J2 학습 delta의 클래스·컨텍스트 lineage | 사용자 스크립트로 가능한지 | 데이터셋 버전/가시성 검토 | training/channel/Model Registry 검토 |
| J3 동일 모델 A/B의 고객별 TP/FP/FN 비교 | core/model comparison 확인 | Eval runs per customer 가능 확인 | offline model evaluation per-camera 가능 확인 |
| J4 고객별 심각도/선택적 승인 조건 | view+code 기준 | Checks+deploy gate 확인 | registry quality gate 확인 |
| J5 고객 A 추가 전 *고객 B 영향* 예측 | custom embedding/slice ranking 베이스라인 | 실제 auto-prioritization 기능 확인 | shared-to-per-tenant architecture 대안 확인 |
| J6 제한된 infer/annotation budget에서 순서/coverage | script/Smart Sample Selection 비교 | Eval suite selection/coverage 확인 | Step Functions pacing/selection 비교 |
| J7 독립 GT 분쟁/ABSTAIN 추적 | Brain+human review 조합 | expected answer review workflow | labeling/ground-truth lineage |
| J8 local/private site 데이터 + CI 증거 | on-prem/open-source 가능 범위 | local deployment + Cloud Eval의 권한/가격 확인 | account/VPC/cross-tenant policies |
| J9 재현 가능한 release decision ledger | SDK/scripts + CI | immutable Eval Runs + CI | Model Registry/artifact hashes |
| J10 고객별 모델 분리 자체의 운영 비용 | 별도 orchestration? | per-project/per-model? | AWS 샘플처럼 분리 배포 대안 |

평가에서 **N/C/S/I 모두 실제 해결 방식**으로 인정한다. "커스텀 스크립트가 필요"는 곧바로 시장의 공백이 아니다. X는 문서 부재가 아니라 정당한 설치/실행/권한 테스트 또는 공식 제한 확인이 있어야만 부여.

## 5. 증거 수집 3개 트랙과 검색·검증 방법

**T1: 동일 사용자/팀 1차 문제** (최우선)
- 공개 Reddit r/computervision, r/MachineLearning, r/mlops, MLOps Community, GitHub issues/discussions, Hugging Face forums, Voxel51 community, Roboflow community, AWS re:Post 등 **원문** 우선.
- 검색식: \`"shared model" "clients" "regressions"\`, \`"fiftyone" "multi tenant" "regression"\`, \`"roboflow" "eval" "multiple customers" "slow"\`, \`"sagemaker" "per-camera" "retraining" "regression"\`, \`"one model" "all clients" "testing"\`, \`"model update" "other clients" false positives\`. 검색 결과의 원문/댓글/해결 표시/일자를 열어 확인.
- 2026-01-08 Reddit 글을 원점으로 논의 답글을 읽되, 작성자가 기존 도구를 안 썼다면 그 사건은 **E1** 이상으로 상향 금지. 사적인 DM, 이메일 발송, 동의 없는 인터뷰는 하지 않는다.

**T2: 공급자 native/enterprise/스크립트/대안 기능 검증**
- FiftyOne core eval, grouped datasets, community model compare/Brain, Smart Sample Selection 및 role/permissions 문서. 관련 GitHub open/closed issues에서 **실제로 해결·대응된 기능**까지 확인.
- Roboflow Workflow Evals의 최신 문서/SDK/API, 프로젝트·워크스페이스/데이터 제약, eval charging, CI 도입 방식. Nov12 글을 특히 반증 원문으로 사용.
- AWS SageMaker 모델 평가/Registry, Shadow Tests, per-camera fleet 샘플, Step Functions, S3/IAM과 고객별 모델 대안. 제품 출시 및 사용 권한 제한을 별도 기록.
- 가격과 회사별 계약·유료 플랜 제한은 공개 문서 기반 범위에서만 정리. 조회 불가한 가격을 발명하지 않는다.

**T3: 실행 가능한 강한 baseline 설계** (계획만, 이번 단계 설치/결제/추론 없음)
- 동일 예시 입력 계약: 3개의 **가상** 고객군, 공유 모델 v1/v2 예측 파일, 고객 A 학습 delta, 고객 B의 부재 클래스/오탐, 독립 label disputes, strict release rules. 미리 작성한 시나리오를 실제 사용자 증거로 표시하지 않는다.
- F1: FiftyOne + 짧은 Python 스크립트; R1: Roboflow Workflow Evals 가능한 native/config/CI; A1: AWS per-camera variant + gate; C1: ChangeScope 가설.
- 같은 7개 출력물: 고객별 회귀/수정 목록, 미검증 coverage, label uncertainty, 재현 manifest, 고객별 배포판정, CI exit status, 실행 비용/운영자 시간.
- 실측은 **다음 승인된 검증 단계**에서만 수행하고, 가격/클라우드/로그인/라이선스/외부 데이터 업로드 결정은 별도 승인. 계산 근거/의사결정 시간 기록.
- 유사 기능이 이미 강한 기존 baseline에서 구현된다면 standalone ChangeScope에 대한 NO-GO.

## 6. 자료 카드와 상태 원장 (한 사건당 1카드)

각 카드는 아래 필드를 채우고 빈 값은 \`UNVERIFIED\`:
\`case_id, published_at, accessed_at, original_url, author_scope (public pseudonym), team_same_entity_proof, actual_job, customer_or_camera_count_if_disclosed, shared_model_proof, triggering_change, new_regression_observed, impact_metric, tried_incumbent_vendor_version, actual_configuration_and_script, documented_result, residual_gap, evidence_grade, contradiction, competing_solution, citation_snippet_under_25_words, next_action, reviewer\`.
- 출처 보존: 공식 문서와 1인칭 사례 분리. 같은 사이트의 복제 기사/검색 스니펫은 독립 사례로 중복 카운트하지 않음.
- 개인 신원 추정, 민감 원본 사진, 비공개 로그를 저장소에 넣지 않음.

## 7. 실제 진행 순서·조기 중단 규칙

| 단계 | 시간 예산(조사 계획값, 작업 완료 아님) | 완료물 | 계속/중단 조건 |
|---|---|---|---|
| D0 원문 기준선 잠금 | 1–2h | 3 incumbent 카드, 2026-01-08 원문 1카드 | 텍스트·기능 출처 정확성 |
| D1 1차 사용자 사건 심층 탐색 | 3–4h | 공개 사례 ledger, 연결 등급 | 같은 팀의 incumbent 사용 증거 확보 또는 정직한 E1 |
| D2 세 공급자 기능의 강한 해결책 조사 | 4–5h | J1–J10 공급자별 N/C/S/I/U/X 매트릭스 | native/script/alt 모두 포함 |
| D3 사건×실제 도구 연결검증 | 2–3h | 동일인·동일 업무/도구·불만 근거 및 반증 | E2/E3 1건 이상? 아니라면 EVIDENCE HOLD |
| D4 비교 실험 프리레지 설계 | 2h | fixture contract, equal-time budget plan, no-unsafe-pass rule | 실제 강한 기준선 없으면 제품 주장 NO-GO |
| D5 최종 연구 판정 | 1h | GO-to-VALIDATE / HOLD / NO-GO 및 대안 제품 피벗 | 아래 판정표 |

**기간 목표:** 2026-11-17~19 KST 2–3일 내부 연구 스프린트. 사용자의 Kiro 앱 개발·Phase5 데이터/모델 실행과 분리.

조기 중단 조건:
- 공식 문서/재현 실험에서 고객별 데이터·평가 + 합리적인 스크립트/CI로 같은 일이 가능한 것으로 확인되면 generic release-gate 후보는 즉시 NO-GO.
- 동일 사용자/조직이 기존 도구를 실제 써보고도 실패했다는 E2가 안 잡히면 **제품 GO 금지**; 더 많은 임의적 사례를 합쳐 E2처럼 표현하지 않음.
- 고객별 모델 분리/adapter 대안이 비용/정확도 기준을 충족하면 "공유 모델"을 전제로 한 솔루션은 필요성 재검토.
- 권한/개인정보/고객 원본 데이터가 없으면 불법 수집/재배포로 진행하지 않고 "검증 불가"로 판정.

## 8. 판정 기준 (검증 자료 확보 전에는 전부 UNPROVEN)

**GO-to-VALIDATE (제품 선정 아님):**
A) E2+ 한 개 이상(같은 실제 조직·같은 업무·사용한 incumbent와 남은 장애가 연결됨), B) J1–J10 비교에서 해소되지 않은 실무 제약이 구체적, C) FiftyOne+short script/Roboflow Evals/AWS per-camera 모델 분리보다 **검증 가능한** 독자 실험 가설이 있음, D) 라이선스/개인정보/3분 데모와 연구 시간 안에 현실적.

**HOLD:** E1만 존재, 제품 기능은 U가 많음, 또는 강한 대안과 비교 전. 미확인 사실은 빈칸으로 두고 착수 확대 금지.

**NO-GO:** 기존 제품/스크립트/아키텍처 대안으로 사용자의 Job이 같은 수준에서 해결되고 추가 기술 가치 불충분, 동일 고객 미해결 증거 장기간 부재, 또는 우세를 실험으로 검증할 수 없고 출품 일정을 크게 잠식.

**PIVOT:** P2 Pipeline Twin의 실제 1인칭 불가해한 파이프라인 문제로 전환하거나, 후보를 제품 단위가 아닌 기능/검증 모듈로 축소.

## 9. 최종 전달물

1. \`research/evidence/incumbent-capability-matrix-20261119.md\`: J1–J10 × 공급자 × native/extension/limitation/unknown + 직접 출처.
2. \`research/evidence/same-user-unmet-need-ledger-20261119.md\`: E0–E4 카드, 동일 사용자/팀 연결성과 반증.
3. \`research/evidence/release-job-to-be-done-20261119.md\`: 1개의 사용자 업무, 작동 방식, 시간·경제적 비용, 확인된/가정된 가치.
4. \`research/evidence/falsification-decision-20261119.md\`: 결론과 반대 증거, 다음 실험이 필요할 경우만 prereg.
5. 한국어 PDF/HTML 보고서와 공개된 출처 URL, GitHub research 전용 브랜치 커밋.

**이 문서 자체는 조사 계획이다.** 아직 공급자 제품을 실행해 비교하거나 E2 고객 사건을 확보한 것으로 주장하지 않는다. 개발 브랜치를 수정하지 않는다. Kiro 크레딧/사용자 AWS 계정/유료 테스트 없음.

## 핵심 공개 출처 (계획 수립에 실제로 다시 확인, 2026-11-16)
- 1인칭 CV 문제 https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/
- FiftyOne Detection https://docs.voxel51.com/user_guide/evaluation/detections.html
- FiftyOne Model Comparison https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- FiftyOne Groups https://docs.voxel51.com/user_guide/groups.html
- Roboflow Evals https://roboflow.com/blog/computer-vision-regression-testing
- AWS fleet pipeline https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
- SageMaker Shadow https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html
