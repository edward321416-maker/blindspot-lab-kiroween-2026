<!-- PUBLIC DOCUMENT BRANCH: Re:Collection documentation handoff only. This is a TEXT TRANSCRIPTION from an indexed user-provided Library document, NOT an independently verified byte-identical original ZIP member. Original full ZIP / final Master Audit / comparison-result PDF / reproducibility packet remain UNAVAILABLE. Source title: ReCollection_DevChat_Handoff_Phase0_ReadOnly_20261117.md. Retrieval: 2026-11-17. D0 READ-ONLY; no D1 authorization. -->

# [전달용 지시문] Kiroween 2026 — Re:Collection 기술 인계 및 D0 사전 검토

**현재 실행 허용 범위: READ-ONLY / PLANNING ONLY.** 이 메시지는 신규 제품의 코드 개발을 승인하는 메시지가 아니다. 먼저 기존 환경을 읽기 전용으로 확인하고, 독립된 신규 제품 개발안을 검토·보고한 뒤 멈춰라. 사용자에게 후속 개발 승인 없이 디렉터리 생성, 브랜치 전환, 커밋, 설치, 유료 API, 배포, GitHub 공개를 수행하지 마라.

## 0. 최상위 개발 결정

- 작업명 **Re:Collection**은 임시 제품명이다. 기존 GhostWeb의 목적(사라진 웹사이트·고장 난 상호작용 복원)과 **다른 제품 후보**다. 지금 Re:Collection을 최종 선정했다고 가정하지 마라.
- 제품 의도: 박물관·미술관·과학관의 사용 빈도가 낮은 소장품 사진·메타데이터·연구 자료 등을 학예사가 2~4개 선택하고 학습 목표를 제시하면, **근거와 권리를 확인할 수 있는 실제 작동형 인터랙티브 교육·전시 프로그램**을 설계·검증·승인·발행하는 제작 스튜디오.
- 주요 사용자: **학예사/박물관 교육 담당자/전시 기획자**. 관람객은 발행된 체험의 최종 사용자.
- Kiro 개발/분석/코드 리뷰 모델은 **Claude Opus 5.5 / reasoning effort MAX 고정**. 실측 확인 가능한 모델·effort·실제 Kiro 크레딧 사용량만 보고하고, Auto 사용 또는 확인 불가를 Opus 사용으로 단정하지 마라. 다른 AI 모델로 바꾸거나 별도 모델 검수를 필수화하지 마라.
- **Kiro 개발 모델과 제품 내부 추론 모델(AWS Bedrock)은 별도**다. 유료 Bedrock 호출/모델 사용/리전/요금은 아직 승인되지 않았다.

## 1. 반드시 읽고 대조할 자료

첨부 자료를 우선 열고, 없으면 '접근 불가'로 보고하되 대체 원문을 상상하지 마라.

1. `ReCollection_Development_Master_Audit_20261117.pdf` — 현재 9쪽의 최종 개발 기준안/위험·중단 조건.
2. `ReCollection_Technology_Architecture_ADR_20261117.md` — 기술 후보 및 상세 데이터 계약의 이전 설계안. 최종 기준안과 충돌하면 1번이 우선.
3. `ReCollection_Comparison_Results_20261117.pdf` — 기존 실험 결과 및 한계.
4. `ReCollection_Reproducible_Comparison_Packet_20261117.zip` — 자체 테스트 재현 참조 자료. **55/55는 사전에 만들어 둔 결정론적 체험 2종과 차단 사례 1종의 자체 테스트 통과**일 뿐 신규 소장품 자동 설계/실제 LLM 경쟁 우위의 증거가 아니다. 현재 이 패킷을 실행·설치하거나 사용자의 프로젝트에 복사하지 말고, 우선 정적 메타데이터와 문서만 검토하라.
5. 필요할 때 공식 참고: Kiroween 2026 규정 https://kiroween.devpost.com/rules ; Kiro CLI 모델 설정 https://kiro.dev/docs/reference/slash-commands/ ; IIIF Presentation 3.0 https://iiif.io/api/presentation/3.0/ ; Bedrock Structured Outputs https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html .

**공식 마감:** 2026-12-04 14:00 PST = **2026-12-05 07:00 KST**. 2026년 대회는 **2026-10-30 이후 새로 제작한 프로젝트만** 인정한다. 기존 코드나 템플릿을 재사용하면 출처·라이선스를 명시해야 한다. 나중에 제출할 때 Kiro를 이용한 새 작동 앱, 공개 기능 URL, 공개 GitHub+LICENSE+루트 `.kiro/`, 3분 미만의 공개 YouTube 시연 및 Kiro 사용 설명이 필요하다. 이는 미래 제출 체크리스트이지 지금 공개·배포하라는 명령이 아니다.

## 2. 지금 즉시 수행할 D0: 환경·범위 읽기 전용 검수

아래 사항만 관측하고 보고한다. `git status`, `git log`, `git branch --list`, `git remote -v`, `git ls-files`, `rg --files`, `rg` 검색 등 **읽기 전용 명령** 사용 가능. 소스 전체를 무차별 덤프하지 않고 `package.json`, `requirements.txt`, `docker-compose.yml` 등 발견된 선언 파일은 **내용을 실행하지 않고** 읽어 스택을 확인한다. 실제 조정 대상 함수는 `rg`로 시그니처를 먼저 찾는다.

- Windows 로컬 경로 `C:\Users\admin\Projects\ghostweb-2-spike-20261116`가 접근 가능한지, 존재한다면 현재 브랜치/HEAD/working tree/remote와 D1.2·D1.3 상태를 확인. **이 폴더는 GhostWeb 실험이며 Re:Collection 제품으로 임의 전환 금지.**
- GitHub `edward321416-maker/blindspot-lab-kiroween-2026`는 이전 점검 기준 연구용 브랜치 6개 및 BLINDSPOT 연구 부트스트랩 저장소다. Re:Collection 신규 제품의 공개 GitHub로 오인·푸시하지 마라.
- Re:Collection을 위한 **별도 디렉터리·별도 Git 저장소 또는 완전 격리 worktree**를 권고하되, 실제 생성/전환/푸시는 아직 하지 마라. 폴더명·브랜치명은 충돌 검사를 끝낸 뒤 '제안'으로만 작성하라.
- 기존 GhostWeb의 경계 검사·ZIP 보안·불변 증거 기록·해시 로직 중 **코드 재사용 후보**와 **새로 개발해야 할 영역**을 분리해, 파일 경로/라이선스/저작자/테스트 근거를 제시하라. 재사용·복사는 미승인.
- Kiro CLI 실제 모델·effort·사용량·크레딧 잔액을 확인할 수 있는 범위를 기술하고, 정확한 화면/로그 근거 없이 특정 값으로 단정하지 마라. 설정을 변경하지 마라.

## 3. 개발 승인 후 예정된 핵심 실험(D1) — 현재는 설계만

**핵심 연구 질문:** 동일한 Opus 5.5/MAX를 사용하더라도, '직접 HTML/JS 작성'보다 '근거 기반 ExperienceSpec + 검증된 실행 엔진'이 소장품 체험을 **반복 제작**하는 데 의미 있는 우위를 보이는가?

### 두 실험군

- **대조군 A / Direct Build**: Opus 5.5/MAX가 동일한 소장품 자료·학습 목표를 받아 직접 HTML/JS 체험을 제작. B의 Compiler/ExperienceSpec/실험 결과는 제공하지 않는다.
- **실험군 B / Evidence-bound Compiler**: 같은 모델/effort가 출처가 연결된 `ExperienceSpec`만 생성하며, 독립 검증기와 허용된 interaction primitive registry를 통해서만 브라우저 체험을 구성. 출력 HTML에 임의 AI 생성 JS를 실행하지 않는다.
- 모두 같은 **입력 스냅샷·소장품 라이선스·테스트·시간·시도 횟수·사용량 상한**으로 실행. 독립 세션과 분리된 격리 작업 공간을 사용하고, 사전 공개된 기존 모스 부호 시안을 신규 성능처럼 계산하지 않는다. B의 **초기 Compiler 개발 비용과 새 자료별 추가 제작 비용을 각각 기록**한다.

### 세 사례와 한계 고정

- **A: Smithsonian Morse–Vail Telegraph Key**. 실제 소장품 페이지와 사용권을 재확인. 현대 국제 모스 부호의 부호화/해독은 **교육용 모델**이며 1844년 장비의 실제 속도·상세 동작을 임의 재현하지 않는다.
- **B: 권리 확인된 19세기 지도/기록 2개**. 관람객이 기록 연도·제목·설명/출처를 비교. 공간 좌표 정합이나 실제 거리·지도 변화량은 검증되지 않으면 주장하지 않는다.
- **C: 증거 부족 유물**. 사진·명칭만으로 기계의 실제 작동 원리를 생성하지 않음. 불확실성을 표시하고 관찰·자료 읽기 같은 대안을 제안.
- 추가로 **사전에 개발자가 보지 않은 1개 이상의 외부 holdout 자료**를 요청하여 고정할 것. 그 입력의 사용권 확인 및 채점 oracle을 미리 저장할 것. 같은 작성자가 수정한 테스트를 '독립 블라인드'라고 부르지 마라.

### ExperienceSpec v0.2 필수 설계 계약

- `SourceAsset`: `id`, `provider`, `canonical_url`, `rights_uri`/`license`, `media_type`, `sha256`, `retrieved_at`, attribution 의무.
- `EvidenceClaim`: `id`, `statement`, `claim_kind=HISTORICAL_FACT|EDUCATIONAL_MODEL|INFERENCE|UNKNOWN`, `source_id`, `locator`, `status`.
- `ExperiencePlan`: `audience`, `learning_goal`, 허용 primitive 종류, 거절/보완 근거.
- `InteractionGraph`: allowlisted node type, 입력/출력/상태 전이, assertion, claim 참조, 유한한 범위 제약.
- `Verification`: schema/semantic/rights/browser/keyboard 테스트 상태와 생성·검수 버전.
- `Publication`: 승인자, `source_hash`, `spec_hash`, `build_hash`, 상태와 발행 일시.
- 상태 전이: `DRAFT -> VALIDATED -> CURATOR_REVIEW -> APPROVED -> PUBLISHED`; `BLOCKED`(권리 불명) 및 `NEEDS_MORE_EVIDENCE`(사실 근거 부족) 별도 처리. 원본·승인·발행은 불변 스냅샷으로 보존.
- **JSON Schema 형식 적합성 ≠ 역사적 사실의 참 여부·출처 접근 가능성·사용권·브라우저 동작 검증**. 별도 의미 검증기를 작성할 것.

### 첫 판정 기준 — 제안, 아직 달성 성과 아님

1. 지원 대상 **체험 2종 실제 브라우저 동작**, 새 holdout에서 검증 반복, P0 결함 0.
2. 공개 자료/미디어의 권리 상태와 발행되는 **핵심 역사적 주장 100%**에 검증 가능한 원본·locator 연결.
3. C 사례에서 근거 없는 작동 시뮬레이션 **0건**.
4. 새 자료를 받아도 목적별 사용자 JS를 매번 수정하지 않는 **공통 Compiler/Runtime 재사용**.
5. 두 실험군의 완료 시간·실제 Kiro 크레딧·실패·수동 개입·테스트 성과를 같은 기준으로 측정. B가 적어도 한 중요 지표에서 **반복 가능한 이점**을 입증해야 개발 확대 권고.

셋 중 일부가 미확인이라면 `HOLD`; 허위 원본 시뮬레이션 또는 안전성 P0가 반복되면 `NO-GO/축소`를 권고한다. 작은 합성 사례 2~3개만으로 일반적인 박물관 업무에 대한 성공률을 주장하지 마라.

## 4. 보안·권리·클라우드 경계

- 공개 메타데이터와 미디어 재배포 권한은 다르다. **CC0/명시적 사용허가 자료**만 초기 공개 후보로 사용하고, 정보가 불명확하면 차단하라.
- 외부 소장품 텍스트는 프롬프트 인젝션 위험이 있는 **비신뢰 자료**. 도구/비밀키/발행 권한을 부여하지 말고, URL allowlist·redirect·내부망 접근 제한 등은 배포 전에 별도 검증하라.
- 모델이 생성한 `eval`/임의 JS/원격 코드 실행 금지. 검증된 primitive와 제한된 매개변수만 허용.
- 관리자 승인 없이 발행 금지. 로그인·권한·감사기록이 없는 경우 **미리보기/로컬 발행 시안**에만 머물러라.
- **AWS/Bedrock/호스팅/유료 호출/모델 접근 신청/결제 방식·권한 변경/새 외부 계정**은 모두 승인 전 보류. 제품 내부 Bedrock 추론 모델과 리전·국외 처리·비용은 별도 의사결정.
- 신규 npm/CLI/SDK 설치가 필요하면 패키지·버전·라이선스·필요 이유를 보고하고, 현재 READ-ONLY 단계에서는 설치하지 마라. 과금·외부 시스템·새 아키텍처 의사결정은 사용자 승인 전 실행하지 마라.

## 5. Kiro의 D0 산출물 형식 — 여기까지 완료하고 반드시 중단

최종 보고는 **한국어**로, 입증 수준을 `직접 확인 / 사용자 전달 보고 / 계획 / 미확인 / 차단`으로 구분하라.

- `01_Observed_Environment`: 확인된 실제 폴더/브랜치/HEAD/clean·dirty/remote, package 및 소스 현황. 접근 못한 자료는 미확인.
- `02_Product_and_IP_Separation`: 기존 GhostWeb/BLINDSPOT과 새로운 Re:Collection의 개발/저작권/재사용 경계.
- `03_ExperienceSpec_v0.2_Design`: 필수 JSON 구조, claim·source 참조, 상태 전이, 실패 시나리오.
- `04_Experiment_Preregistration`: A/B 동일 조건, 3+holdout 자료, 평가 oracle, 크레딧·시간 예산 **제안**, 승패/중단 기준.
- `05_Security_and_Cost`: 권리/프롬프트 인젝션/임의 JS/승인 없는 발행/AWS의 P0/P1 위험.
- `06_Implementation_Proposal`: **개발 승인 후** 생성할 예상 파일 트리, 순서, dependency 후보, 예상 작업량/비용, 적합한 격리 저장소 계획.
- `07_Next_Decision`: `D1 핵심 실험 승인 / 범위 축소 / 보류` 중 추천과 판단 근거.
- 기획 결과물은 **PDF로도 제출**하고 페이지·한글·표·파일 링크를 전수 검수해라. PDF를 만들 도구가 없는 경우 근거 있는 제한을 설명하고 Markdown을 우선 제출하라.
- 각 파일·근거·실험 결과에는 **원본인지/추정인지/직접 실행한 결과인지**를 명시한다. 체크포인트에는 측정 또는 UNKNOWN 토큰·크레딧을 기록한다. AI_Execution_Log가 실제로 연결·승인되어 있을 때만 append 및 readback; 접근 불가 시 로컬 기록 대기라고 표시하고 동기화했다고 주장하지 않는다.

**D0 결과를 보고한 뒤 멈춰라. 현재 메시지로 새 프로젝트 코드 구현, 테스트 실행에 필요한 설치, 브랜치 생성, GitHub push, AWS 리소스 생성, 배포, 비용 발생까지 진행할 권한을 부여하지 않는다.**