# D4–D5 · ChangeScope 반증 조사 Round 1 판정
**2026-11-16 KST / 연구 진행 완료 범위: 공개 자료 사용자 사건·공식 공급자 능력·GitHub issue/support thread desk research.** 실제 설치/대시보드 실험/유료 서비스 실행/사용자 연락 = **하지 않음**.

## 명시적 판정
**ChangeScope: EVIDENCE HOLD.** 사용자의 목표 업무(고객 A 학습 추가→B 신규 오류, 고객 증가에 따른 회귀검사 병목)의 1인칭 공개 사례 **1건** 확보. 동일 사용자가 FiftyOne·Roboflow·AWS/분리형 대안을 실제 시험하고도 실패한 **E2 목표 사건 0건**. 현행 경쟁 제품 기능과 고객별 모델 분리의 강한 해결책 존재. 불확실한 기능은 U로 둠.

## 근거 FOR (실제 확인된 것)
1. 2026-01-08 실제 CV 개발자가 A→B 간섭 및 검증 지연 제보 https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/
2. AWS 2026-10-26 현장 카메라별 도메인 차이와 공통 모델 성능 약화를 공식 기술 사례로 제시 https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
3. FiftyOne 약 100만 그룹 이미지에서 UI similarity failure/스케일 우회 비용 확인 (단 **다른 작업**, 직접 제품수요 G4에는 미포함) https://github.com/voxel51/fiftyone/issues/7060

## 근거 AGAINST (강력한 반증)
1. Roboflow Workflow Evals가 2026-11-12 이미 고정 GT 기반 A/B workflow version, per-case checks, immutable result, deploy gate, CLI/CI를 제공. generic regression gate 신규성 NO-GO. https://roboflow.com/blog/computer-vision-regression-testing
2. FiftyOne core+community plugin에서 per sample/class TP/FP/FN, `hitmiss/misshit`, groups 지원. 직관적인 release dashboard만으로 차별화 불가. https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
3. AWS는 공유 모델을 포기하고 카메라별 fine-tuned model을 학습·평가·버전관리·승인하는 참고 파이프라인을 공개. 문제를 다른 아키텍처로 회피 가능. https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/

## 빈틈·불확실성 (투자 블로커)
- 모델의 **training-delta→other-tenant regression preflight prediction**을 기존 제품이 기본 제공하는지는 직접 실행/공식 명시적 제한 근거가 없음. `U`로 판정하고 '경쟁 제품에 없다'고 말하지 말 것.
- 2026-01 실제 개발자는 기존 제품을 사용했다고 밝히지 않았고, 그 후에도 문제를 해결 못했다는 근거가 없음. 이 사건의 E2 승격 불가.
- Roboflow 지원 포럼 별개 사례는 잘못된 Workflow output wiring을 지원팀이 수정하도록 설명. 사용자가 이후 해결 여부를 확인하지 않음; 실패한 incumbent로 재사용 불가.
- 실제 사용자/기업의 시간·비용·보안·데이터 권한, 고객 수, 구매 의사 모두 미확인. 가상 데모/문서 출처는 E4 아님.
- 제품 경쟁/특허 신규성 판단을 위한 대규모 독립 실험 미실행.

## 기획상 GO/HOLD/NO-GO
| 후보 | 실제 판단 | 이유 |
|---|---|---|
| Generic Blindspot Regression Gate | **NO-GO standalone** | Roboflow/Evals, FiftyOne, AWS 직접 경쟁 |
| ChangeScope prediction + budgeted audit | **EVIDENCE HOLD** | E1만 보유; J5/J6 경쟁 앱 구체 구현/사용자 미해결 미증명 |
| Pipeline Twin input/pre-/postprocess cause isolation | **ALTERNATIVE HOLD** | Roboflow 별개 사례 있으나 지원 설정 원인 제시. 직접 unmet validation X |
| ChangeScope as feature/extension | **POSSIBLE REUSE, NOT SELECTED** | strong competitor integration may make own product unnecessary |

## 조기 중단·조건부 재개
- **이 단계에서 확정된 제품 GO 없음. Kiro 개발 브랜치 및 사용자의 Phase5 독립 GT 연구 범위 미변경.**
- 재개하기 위한 단일 우선 증거: **같은 CV 개발팀에서의 실제 고객 A→B 간섭 사건 + 시험한 기존 tool/workaround + 남은 업무 + 영향(시간/비용/오탐)을 연결한 공개 E2**.
- 같은 자료가 없다면 **새 경쟁 분석 표를 무제한 확장하지 말고**, Pipeline Twin 혹은 제조/건설 등 더 구체적인 산업 작업으로 피벗 비교.
- 제안하고 미실행한 후속 벤치마크: Three-tenant, old/new model fixed, train delta from tenant A only, B/C holdout, human-independent GT, FiftyOne+script, Roboflow native Evals, AWS per-tenant model alternative; matched query/review budgets and coverage. **실제 데이터/모델·클라우드 호출은 별도 승인 후.**
- **현재 조사에서 G4 승격 FAIL / E2 목표 사례 0.** 실패를 숨기지 않는 것이 공모전 시간 예산에 중요.

## 업무 및 시간 기록
- 공개 원문 읽기: Reddit 2026-01, GitHub FiftyOne issue + comments, Roboflow community + 2026-11 Evals, AWS 2026-10 sample, AWS 2026-07-30 Ground Truth restriction, FiftyOne core/plugin/groups, Roboflow pricing/inference.
- 추가 검색은 주로 같은 사용자·제품 연결을 목표로 수행했으며, 접근 가능한 원문으로 목표 E2를 확인하지 못했다. 전체 웹에 그런 사례가 없다는 뜻은 아님.
- 데이터/문서 상태: **직접 확인한 공개 소스와 연구 추론**만 포함. 위 빈칸은 외삽 없이 UNKNOWN.
