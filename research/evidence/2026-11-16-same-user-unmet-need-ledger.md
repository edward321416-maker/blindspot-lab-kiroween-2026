# D0–D3 · 사용자 사건 및 사용 제품의 미해결성 증거 원장
**2026-11-16 KST 공개 웹·GitHub 원문 조사.** 기준 SOP: `research/protocols/2026-11-16-incumbent-gap-sop-v1.md`. 총 4개 핵심 원문 기록. **목표 문제를 직접 입증하는 E2 건수 = 0.** 다른 문제의 높은 증거 등급을 합산하지 않는다. Search query scope is bounded, not a claim to have searched the entire Internet.

## INC-01 · 고객 간 모델 변경 회귀 — 목표 업무
- 원문: https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/
- 2026-01-08; 본인이 여러 고객에게 배포한 **단일 공유 CV 모델**에 고객 A 데이터를 추가하면 B에서 존재하지 않는 물체를 검출하는 회귀가 생길 수 있고, 전체 고객 검사가 느려진다고 1인칭 제보.
- 같은 업무·변경: YES (작성자의 설명). **실제 오류 로그/재현 데이터:** UNKNOWN. **조직 식별:** 공개된 가명 이외 UNKNOWN.
- 사용한 FiftyOne: UNKNOWN. Roboflow: UNKNOWN. AWS SageMaker: UNKNOWN. 실제 시도한 고객별 미세조정: **대안으로 고민 중**이라고만 기록; 시행/성과 미확인.
- 해결책 적용 후에도 남은 실패: UNKNOWN. 엔지니어 분·검사 비용·고객 수: UNKNOWN.
- 반대 가능성: 모델을 고객별로 분리하면 A→B 간섭 원인을 구조적으로 피할 수도 있음. AWS 2026 카메라별 구현이 실제 대안.
- **증거 등급: E1, 목표 업무 직접 관련. E2 승격 FAIL.** 주어진 원문에 공급자 사용 후 실패가 없다. 접근 가능한 검색 결과는 게시글 본문 중심이며 모든 댓글의 부재를 보증하지 않는다.
- 독립적 사용자 응답 확인: NOT PERFORMED. 추후 해당 작성자의 공개 후속 글/댓글 중 실제 시도와 결과만 추적. 비공개 신원 추적 금지.

## INC-02 · FiftyOne 그룹 데이터셋에서 대규모 similarity UI 실패 — 주변 업무
- 원문 https://github.com/voxel51/fiftyone/issues/7060 (2026-02-23, OPEN이라고 연결 GitHub issue API에서 조회).
- 동일 사용자가 FiftyOne 1.13.2 + MongoDB/Atlas + image/3D grouped dataset에서 미리 계산한 임베딩으로 유사도 검색 UI를 실행했는데 MongoDB의 BSON 16MB 제한에 따른 `DocumentTooLarge` 오류를 제보. FiftyOne 유지관리자는 재현했고 매우 큰 그룹 slice의 ID 필터 문제가 원인이라 설명.
- 사용자의 공개 후속: 약 100만 샘플; Python `sort_by_similarity()` 우회법은 작동하지만 앱 UI를 대체하기 위해 플러그인 개발. 10,000개 선택 시 `session.view = view` 경로 약 15분, 별도 `select` 경로 약 10초라고 사용자 본인이 기록. 모두 **그 사용자 환경의 자가보고 수치**, 직접 계측이나 일반 벤치마크 아님.
- 유지관리자는 Python SDK 우회, MongoDB 설정 실험, 후속 배치 검색 방식을 제안. **전체 제품에서 영구 해결 불가**가 아니라 *일부 워크플로 및 규모에서 발생한 구현 제한*.
- 등급: **E3 (동일 사용자 실사용·로그/버전·우회 이후 비용)**, 단 **ChangeScope 고객 간 공유 모델 업데이트와 사건·직무가 달라 G4 대상에서 제외**. 이를 INC-01과 결합해 E2 획득으로 주장 불가.
- 기존 솔루션 유효한 대안: Python SDK, 개선 플러그인, MongoDB 대체 인덱스. 실제 고비용 워크플로의 가능성을 보여주지만 새 release product 필요성은 미입증.

## INC-03 · Roboflow Workflow 결과가 단독 모델 테스트와 상이 — 주변 업무
- 원문: https://discuss.roboflow.com/t/workflow-results-inconsistent-with-model-test-results/11968
- 2026-03-22 user hoibun: 바위 해변 플라스틱 이미지 instance segmentation 모델 `ppm-thumb-corner/1`은 단독 테스트에서 타당해 보이나 동일 이미지 Workflow 후속 Polygon Visualization/Property Definition 결과가 엉뚱하게 나타난다고 설명. 구성과 출력 사진·PDF 제출, Roboflow 지원 접근 동의.
- 2026-04-02 지원 담당자가 **bounding boxes를 polygons처럼 연결한 잘못된 필드 참조**가 원인인 것으로 진단하고 mask output을 지정하도록 안내. 모델 자체의 성능 저하 또는 신규 학습 회귀라는 증거는 아님. 질문자가 수정 후 재검증한 결과는 공개 페이지에서 확인되지 않음.
- 동일 사용자 도구 사용: YES; 여전히 미해결: **UNKNOWN** (설정 수정 해법 제시, 후속 재확인 없음). 고객 간 모델 업데이트 사례: NO.
- 등급: **E1 + 실사용 설정 오류/해법 제시**, ChangeScope의 E2 대상 아님. P2 Pipeline Twin의 실무 문제 **힌트**는 되지만 지원 답변이 이미 진단했으므로 제품 미해결 E2는 아님.
- 검증 반증: 현재 Roboflow Workflow Evals는 Model+Pre/Postprocessing 전체를 검증하는 회귀 체크·배포 게이트를 제공(2026-11-12 문서).

## INC-04 · AWS 카메라 플릿 운영 문제와 공식 대안 — 공급자 설명
- 공식 AWS 2026-10-26 https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
- 생산라인마다 카메라 각도·반사광·조명이 다른 공장, pooled model이 개별 카메라에서 약해져 카메라별 미세조정·quality-gate·versioned Model Registry·Step Functions 플릿 파이프라인을 제시. 특정 외부 구매자의 미해결 보고가 아니라 **공급자가 문제와 해결 구현을 함께 설명한 기술 기사**.
- 등급: **E0 기업 공식 구조/필드 경험**, 다른 조직의 ChangeScope 미해결 E2로 전용할 수 없음. 강한 반대 근거: 고객별/카메라별 모델 분리가 공유모델 간섭 제거의 실질적 대안.
- 비용 주장: AWS가 게시한 합성 샘플 실행 **$0.07**은 특정 구동 환경의 예시, 실제 고객 총비용/정확도 측정치로 환산 금지.

## 결과 요약 (중복 없음)
| Case | 동일 실제 사용자 | 실제 경쟁 도구 사용 | 적용 후 잔여 문제 | 목표 A→B 업무 동일성 | 입증 등급 | G4 목표 충족 |
|---|---|---|---|---|---|---|
| INC-01 Reddit | 예 | 없음/미확인 | 미확인 | **예** | E1 | **NO** |
| INC-02 FiftyOne #7060 | 예 | **예** | 일부 성능/기능 제약 | **아니오** | E3 adjacent | **NO** |
| INC-03 Roboflow forum | 예 | **예** | 수정 후 미확인 | **아니오** | E1 adjacent | **NO** |
| INC-04 AWS blog | 공급자 | 구현 소개 | 문제 대응 구조 제시 | 유사 | E0 | **NO** |

**절대 주장하지 않을 것:** "FiftyOne·Roboflow·AWS 고객이 shared-model A→B 회귀를 기존 솔루션으로 해결하지 못했다" (현재 근거 없음).

## 검색 경로 기록 (공개 자료 실탐색)
- 공개 웹 검색: `"shared model" "clients" "regressions"`, `"model update" "other clients" "false positives"`, `site:discuss.voxel51.com fiftyone multi-tenant slice regression`, `site:discuss.roboflow.com "regression" "eval" "release"`, `"clients" "model" "regressions" "fiftyone"`, `"customer" "regressions" "Roboflow"`, `"tenant" "model update" "regression" computer vision`, `site:repost.aws SageMaker multi tenant models quality gates issues` 등 키워드군. 모두 2026-11-16 KST.
- GitHub 연결: `voxel51/fiftyone/issues/7060` 이슈와 모든 공개 댓글 재조회, 본문/상태/유지관리자 반응을 분리. Repo 내 multi-tenant / evaluation performance / grouped regression / plugin 탐색도 수행. 전체 GitHub 모든 문제를 exhaustive 검색했다고 주장하지 않음.
- Roboflow 공식 기술 문서·커뮤니티 원문, AWS 2026 공식 샘플, FiftyOne OSS 공식 문서·플러그인 확인. 웹 검색에서 안 나온 사례가 없다는 뜻 아님.
- 선정 편향 통제: E2가 없는 사실을 숨기지 않음. 공급자 소개와 실제 사용자 문제를 묶지 않음. 반증 및 정상 우회 제시를 포함.
