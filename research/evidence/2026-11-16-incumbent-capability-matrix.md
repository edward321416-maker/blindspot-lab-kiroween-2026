# D2 · FiftyOne / Roboflow / AWS 강한 대안 능력 대조
**2026-11-16 공개 공식 문서 기반. 실행된 A/B 벤치마크 아님.** 표의 "문서 확인"은 실제 설치·권한·성능 검증이 아님. 각 셀의 N/C/S/I/U는 **해당 좁은 하위 기능의 확보 여부**이며, J 전체가 완결됐다는 뜻이 아니다. X는 공식 제한이 명시된 경우 외에는 부여하지 않는다.
상태 정의: N native, C configured, S reasonable script (예상·미실행이면 * 표시), I architecture integration, U unclear. 판매 플랜/버전 및 배포권한 별도.

## J1–J10 매트릭스
| 업무 | FiftyOne + plugin/SDK | Roboflow Evals/Inference | AWS SageMaker + 서비스 |
|---|---|---|---|
| J1 고객별 데이터 그룹/격리 | **N** group/view 메타데이터 [F3], **U** 고객 권한 격리·멀티테넌트 ACL | **N** private project/workspace [R4]; **U** 독립 고객간 완전 격리 SLA | **I** per-camera ID Model Registry + S3/IAM 설계 [A1]; IAM 실제 설정 미실행 |
| J2 학습 변경 내역 lineage | **S*** field/tag + 스크립트(추론) [F1,F3]; 자동 training-delta 추적 **U** | **N** dataset/model version [R1,R4]; diff→다른 고객 위험 자동 예측 **U** | **I** per-camera model registry metadata/weights history [A1]; 공통모델 A data lineage 특정 방식 **U** |
| J3 모델 A/B 고객별 탐지 회귀 | **N** `evaluate_detections` + plugin `hitmiss/misshit` [F1,F2] | **N** Workflow Evals same cases, checks and multi-run comparison [R1] | **I** per-camera offline held-out scoring+quality gate [A1]; 객체별 FP/FN 특화는 별도 구현 필요 |
| J4 고객/결함별 릴리스 차단 | **S*** SDK/CI로 임계값 설정 가능, **직접 게이트 기본 제공은 U** [F1] | **N** per-check publish requirement + CI [R1] | **I** ConditionStep + FailStep per-camera metrics [A1] |
| J5 A 학습변경→B의 사전 영향 예측 | **U**, 임베딩·슬라이스로 자체 근사 가능성은 미실행 가설 | **U**, Test Check 존재가 *영향 사전 예측* 증명은 아님 | **U**, per-camera 모델 분리는 변화 경로 자체를 제거하는 **대안** [A1] |
| J6 고정 inference/검수 예산에서 선택·coverage | **S*** 샘플 필터/스크립트 가능 [F1,F3], 최적위험 할당 엔진 **U** | **C** 선택 Cases/Checks, cloud Eval 비용 [R1]; 최적 테스트 allocation **U** | **I** Step Functions concurrency pacing [A1]; 위험 기반 평가 대상 선택 우위 **U** |
| J7 GT 오류·독립 인간 adjudication | **N** annotation mistake 후보/시각화 [F4]; 독립 blinded human GT chain **U** | **C** ground truth를 사람이 검토해 Eval Case 생성 [R1]; 독립·blind GT 보증 **U** | **I** 기존 Ground Truth 기존 고객 라벨 verification 가능 [A2]; **신규 고객 접근 X** (2026-07-30부터 닫힘) |
| J8 로컬/고객 현장 데이터 처리 | **N** OSS local Python/DB workflow [F1] | **N** self-hosted Inference local no per-inference credits [R2,R4]; Workflow Evals의 full offline/local 독립 운영은 **U** | **I** account/VPC/S3 + device ONNX/Neo [A1]; 구현·IAM 비용 확인 필요 |
| J9 추적 가능한 출시 결정/CI 산출물 | **N** stored eval metadata [F1,F2]; **S*** 외부 CI script와 승인 증빙 | **N** immutable historical Eval Runs, deploy gate/SDK CLI [R1] | **I** Model Registry approved packages + quality gates [A1] |
| J10 고객별 모델 분리·운영 대안 | **U** FiftyOne 자체 플랫폼은 주로 평가/데이터 툴 | **C** 다중 프로젝트/모델 관리 가능 [R4], 고객 수에 따른 운영 TCO **U** | **I** 본격 per-camera fine-tune, metadata, Step Functions pacing, on-edge ONNX [A1] |

**결론:** J3·J4·J9의 핵심은 여러 대안에서 해결 가능. J5 고객 간 영향 **선행 예측**과 J6 위험에 따른 예산 최적화는 이 조사에서 제품 간 직접적 동등성 확인에 실패했지만, 곧 시장 공백의 입증은 아니다. **U != X.** 현재 핵심 가설의 실측 비교/독립 사용자 NEED는 없다.

## 최초 데이터셋·정답 관련 주의
AWS Ground Truth **신규 고객 접근은 2026-07-30부터 닫힘**, 기존 고객만 사용 가능 [A2]. 이것은 AWS pipeline, SageMaker Registry, AWS 전체 ML이 신규 고객에게 닫혔다는 의미가 아니다. 또한 검수자가 기존 레이블을 보는 verification은 독립 블라인드 신규 주석과 다르다. FiftyOne mistake score도 독립 ground-truth가 아니다.

## 주요 출처
- [F1] https://docs.voxel51.com/user_guide/evaluation/index.html (evaluation; saved results; sample FP/FN)
- [F2] https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html (community plugin; hithit/hitmiss/misshit; plugin TODO FP tally)
- [F3] https://docs.voxel51.com/user_guide/groups.html (group views; careful with slice filters)
- [F4] https://docs.voxel51.com/brain.html (data quality/mistakenness)
- [R1] https://roboflow.com/blog/computer-vision-regression-testing (2026-11-12 17 Cases × 5 checks, immutable Runs and publish gate)
- [R2] https://github.com/roboflow/inference (self-hosted Inference; third party models and commercial licenses differ)
- [R4] https://roboflow.com/pricing (private project/free plan and self-hosted)
- [A1] https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/ (2026-10-26 factory fleet sample)
- [A2] https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html (explicit access closure effective 2026-07-30)
- [A3] https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html (shadow tests; not GT object score)
- [A4] https://docs.aws.amazon.com/ko_kr/sagemaker/latest/dg/build-and-manage-steps-types.html (QualityCheck models drift baselines)
