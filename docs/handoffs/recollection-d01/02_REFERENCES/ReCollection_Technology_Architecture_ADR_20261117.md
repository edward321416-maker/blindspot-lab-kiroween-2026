<!-- PUBLIC DOCUMENT BRANCH: Re:Collection documentation handoff only. This is a TEXT TRANSCRIPTION from an indexed user-provided Library document, NOT an independently verified byte-identical original ZIP member. Original full ZIP / final Master Audit / comparison-result PDF / reproducibility packet remain UNAVAILABLE. Source title: ReCollection_Technology_Architecture_ADR_20261117.md. Retrieval: 2026-11-17. D0 READ-ONLY; no D1 authorization. -->

# Re:Collection — 기술 선정 및 아키텍처 결정안

**Kiroween 2026 · 기술 기획 v0.3 · 2026-11-17 KST · 상태: DESIGN PROPOSAL / NOT DEPLOYED**

> **설계 결론:** AI가 임의의 웹앱 코드를 생성해 실행하는 대신, 박물관 자료를 **근거 레코드**로 수집하고, Bedrock 모델이 **형식이 제한된 ExperienceSpec**을 제안하면, 자체 **검증기와 명세 실행기**가 관람객용 체험을 구성한다. 사람의 승인 전에는 발행되지 않는다.

> **개발 상태:** 기존 로컬 Re:Collection 비교실험은 사람이 정의한 체험 유형 2종과 자료 부족 거절을 시험한 55/55 자체 테스트다. 이 결과는 임의 소장품 자동 제작, GPT 대비 우위, AI/API 실동작, 박물관 실사용을 증명하지 않는다. 본 문서는 기술 선택안이며 새 제품 구현과 AWS 과금·배포를 승인하지 않는다.

## 1. 무엇을 기술로 증명할 것인가

### 1.1 사용자 작업
학예사·교육 담당자가 공개 소장자료 2~4개를 선택하고 학습목표를 입력하면, 시스템이 **근거가 확인된 사실**, **교육용 모델·해석**, **권리/동작이 불분명한 요소**를 분리해 1~3개 체험안을 제안한다. 담당자가 사실과 표현을 승인하면 직접 조작 가능한 페이지를 발행한다.

### 1.2 반드시 남길 독자 기술 가설
1. **Evidence Contract**: 모든 핵심 주장·상호작용 규칙이 원본의 URL/필드/위치 또는 별도 교육 모델의 정의·검증 테스트에 연결된다.
2. **Typed Interaction Grammar**: AI는 실행 코드를 내지 않고 `signal`, `compare`, `sequence`, `hotspot`, `decision` 같은 제한된 조작 프리미티브를 결합한 구조화 명세를 출력한다.
3. **Executable Evidence**: 명세가 동일하면 동일한 프로그램·테스트·승인 기록이 재현된다. 자료가 부족하면 `BLOCKED / NEEDS_REVIEW`를 내고 환각성 시뮬레이션을 생성하지 않는다.

독창성은 현재 **가설**이다. 위 세 가지가 일반 GPT와 교육 콘텐츠 제작기보다 재사용성·검증성·제작 속도에서 실측 우위를 보여야 한다.

## 2. 핵심 기술 최종 권고표

| 층 | 1차 채택 | 선택 이유 | 처음에는 하지 않을 것 |
|---|---|---|---|
| 개발 기반 | **Kiro CLI/IDE + Node.js 26 LTS + TypeScript + Next.js 16 / React 19** | Kiro 사용 증거와 단일 언어 웹 제품; SSR·브라우저 체험을 함께 구성 | 신형 Node 27 alpha, 다중 서비스 프레임워크 |
| 소장품 연결 | **IIIF Presentation 3.0 + Met API 1.1 + Smithsonian 정규화 어댑터** | 공개 소장품·이미지·메타데이터와 권리를 추적 | 범용 크롤러, 전 박물관 DB 연동 |
| 원본 저장 | **S3 객체 + SHA-256 + URL/rights 스냅샷** | 원본 불변과 출처 재검토 | 처음부터 고해상도 3D 일괄 수집 |
| AI 제작 제안 | **Amazon Bedrock `bedrock-runtime` + Claude Haiku 5.5 (후보 기본값)** | 2026-10 출시, 이미지 입력, 구조화 출력 지원 | 무제한 에이전트, 모델의 임의 코드 실행 |
| 고난도 비교 | **Claude Sonnet 5.5 / Nova 2 Lite 후보를 동일 문제로 평가** | 질과 비용의 이원 선택 | 사전 평가 없이 최신 모델 고정 |
| 체험 명세 | **ExperienceSpec v0.2 (정적 JSON / JSON Schema)** | 화면/데이터/주장/권리/승인/테스트를 구분 | 자유형 HTML·JS를 AI 출력으로 사용 |
| 검증 | **Ajv 또는 호환 JSON Schema 검사 + 의미 검증 + Playwright** | 구조·허용 규칙·실제 브라우저 작동을 각각 확인 | JSON이 유효하다는 이유만으로 사실 승인 |
| 실행기 | **React 컴포넌트 기반 2종 실행 모듈** | 동일한 명세로 반복 렌더, 안전한 경계 | 범용 physics engine, 임의 iframe script |
| AWS 배포 | **Amplify Hosting + Lambda/서버 API + S3 + DynamoDB** | Kiro 공모전용 작은 서버리스 경로 | Kubernetes, OpenSearch/벡터 DB, Step Functions |
| 3D 확장 | **Three.js GLTFLoader 선택적** | CC0 GLB가 있을 때만 3D 관람/핫스팟 | LLM의 기계적 구조 자동 3D 재현 |

모델 및 라이브러리 정확한 패치 버전, 리전, 과금 단가, 접근 권한은 개발 환경에서 `lockfile`과 공식 모델 카드를 재검증한 뒤 고정한다. 표는 설계 선택이지 설치·배포 완료 목록이 아니다.

### 2.1 선택의 핵심 근거 및 탈락 대안
- **범용 코드 생성 대신 명세 컴파일:** 기존 GPT 직접 코딩으로도 체험 1개는 만들어진다. 경쟁력은 새 체험마다 코드를 다시 쓰지 않게 하는 반복성에 둔다.
- **소규모 데이터에 벡터 DB 제외:** 2~4개 자료에서 전수 검증 가능한 원문 레코드와 필드 기반 검색이 먼저다. 자료 수가 증가하고 실제 검색 품질 문제가 확인되면 멀티모달 임베딩을 평가한다.
- **독립적인 체험 실행기:** AI 모델을 변경해도 승인된 ExperienceSpec과 시각화 결과는 변하지 않도록 한다. 모델은 제안만 하고 실행기는 사용자 입력과 상태만 처리한다.
- **외부 콘텐츠 자동 수집 지양:** 기관의 공개 API·IIIF를 지원하되, 무제한 URL 크롤링은 권리·보안·서비스 약관 위험 때문에 제외한다.
- **3D는 선택적 시각화:** 원본 3D 모델을 보여주는 기능과 전신기의 실제 기계 작동을 재현하는 것은 다른 문제다. 역사적 물리 동작을 추정해 만들지 않는다.
- **AWS는 제출용 최소 시스템으로:** 개발 초반에는 로컬 스냅샷과 가짜 모델 어댑터로 보안·동작을 시험하고, 서비스 사용 비용을 승인받으면 배포한다.

## 3. 전체 데이터·실행 흐름

```text
학예사: 소장자료 선택 + 학습 목표
              |
              v
[Source Adapters] IIIF / Met / Smithsonian / 직접 파일(권리 확인)
              |
              v
[Asset + Evidence Registry] immutable source URL, snapshot hash,
  title/date/author, rights, claim evidence locator, trust level
              |
              v
[AI Proposal / Amazon Bedrock] 후보 체험 1~3개 + 필요한 근거 표시
              |
              v
[Structured ExperienceSpec v0.2]  (AI 출력은 아직 미신뢰)
              |
              v
[2차 검증] schema -> rights -> source locator -> interaction bounds
              |                                 |
          VALID/REVIEW                         BLOCKED
              |                                 |
[Deterministic Renderer / Playwright tests]     보완 요청
              |
              v
[학예사 승인 및 서명된 스냅샷] -> [Public Exhibit (read-only)]
```

**보안 경계:** 외부 API와 업로드한 소장품 설명은 *신뢰되지 않는 데이터*이며 시스템 명령이나 모델 지시가 아니다. AI는 `ExperienceSpec` 초안을 제안할 수 있지만 승인·파일 접근·공개 URL 발행 권한이 없다.

## 4. AI 모델·추론 전략: 2026년 현재

### 4.1 기본 모델은 후보로만 결정
- **Claude Haiku 5.5 on Bedrock**: 공식 카드 기준 2026-10-07 출시, 이미지/텍스트 입력, Converse 및 구조화 출력 지원. 작은 자료 추출·체험 유형 제안의 **비용/속도 후보**로 선택.
- **Claude Sonnet 5.5 on Bedrock**: 다중 원본의 복잡한 관련성/체험 설계에 대한 **정확도 대조군**. 실제 토큰 요금·리전 접근성을 확인한 뒤 제한적 실험.
- **Amazon Nova 2 Lite**: AWS 네이티브 멀티모달 **대조 후보**. 요구되는 정형 출력 API 호환성과 한국어 자료 성능을 각 모델별로 스모크 테스트한 뒤 채택 여부 결정.

Bedrock Structured Outputs는 응답의 **JSON 구조**만 보장한다. 역사적 사실·출처 유효성은 보장하지 않는다. 일부 JSON Schema 제약(`minimum`, `maximum`, `minLength`, `maxLength`, recursive refs 등)은 네이티브 지원되지 않으므로 **모델 출력용 제한 스키마**와 **서버의 전체 규칙 검증**을 분리한다. Anthropic 모델의 구조화 출력과 네이티브 citation 기능은 병용 제한이 있으므로, 자체 증거 ID/locator 검증을 사용한다.

### 4.2 권장 추론 단계
1. 정규화된 레코드에서 **자료별 확인 가능한 사실 후보**를 추출한다. 무근거 확신을 금지하고 `UNKNOWN`을 허용한다.
2. 자료/학습 목표에 맞는 체험 구조를 **최대 3개** 선택하게 한다. 각 체험에 요구되는 추가 근거·권한을 함께 보고한다.
3. 선택안 하나를 제한된 `ExperienceSpec` JSON으로 변환한다. **실행 코드, 임의 URL fetch, 임의 컴포넌트 이름 생성 금지**.
4. 독립 검증기에서 소스 ID와 인용 위치, 사용권, 조작 수치 상한, 공개 가능성, 퀴즈 정답을 확인한다.
5. 필요한 경우 사람에게 **대체 시안/근거 자료 요청**을 반환하고, 승인되면 생성물이 고정된다.

**비용 한도:** 모델 호출은 사전 승인된 AWS 계정·리전·결제 한도 내에서만 실행한다. 우선 로컬 가짜 모델 어댑터로 기능 개발; 실 Bedrock 테스트 전 모델당 입력·출력 토큰, 요청 수, 재시도 수 및 Marketplace 청구 경로를 계측하고 호출 상한을 설정한다. 이 기획에서는 유료 호출을 실시하지 않았다.

## 5. ExperienceSpec v0.2 설계

이전 v0.1 스키마에는 `sourceAssets`, `claims`, `experience`, `approvals`, `tests`가 있다. 전면 폐기하지 않고 **호환 확장**한다.

| 분리할 엔터티 | 필수 필드·의미 | 검증 책임 |
|---|---|---|
| `SourceAsset` | source_id, institution, canonical_url, media_type, rights_status, rights_evidence, snapshot_hash | 공개 가능한 원본/미디어 여부 |
| `Claim` | claim_id, text, kind=`HISTORICAL`/`EDUCATIONAL_MODEL`, evidence_asset_id, locator, reviewer_status | 검증되지 않은 역사적 주장 차단 |
| `ExperiencePlan` | audience, objective, proposed_primitives[], alternatives, refusal_reason | AI가 **만들 수 있는 것**만 선택 |
| `InteractionNode` | node_id, primitive_type, input/outputs, state_transition, bounds, linked_claim_ids | 안전한 조작 규칙과 재현성 |
| `Verification` | schema_errors, evidence_coverage, rule_tests, browser_tests, rights_gate | 기계적 점검과 사람 심사의 분리 |
| `Publication` | curator_approval_id, source_snapshot_hash, spec_hash, build_hash, public_url | 승인된 스냅샷 외 발행 금지 |

**최소 작동 규칙 예:** `signal.encode`는 국제 모스 부호로 교육용 문자열을 변환한다. 자료의 1844년 전신기 사진만으로 역사 당시 전송 프로토콜의 정확한 재현이라고 주장할 수 없으므로 `EDUCATIONAL_MODEL`로 분류하고 설명을 표시한다.

**정당한 거절 예:** 정체가 불명확한 기계 사진만 있으면 `mechanism.simulate`를 내지 않고 `NEEDS_MORE_EVIDENCE`와 `hotspot.observe` 대체안을 제안한다.

## 6. 체험 실행 엔진: '템플릿'이 아닌 조합 가능한 문법

### 첫 2개 완성형 모듈
1. **Signal Lab**: 사용자 입력 -> 점/선 신호 -> 해독 결과 -> 속도·문제풀이; 자료와 별개의 교육용 규칙임을 분명히 표시.
2. **Catalog/Timeline Compare**: 기관 기록에서 확인된 연도·제목·설명을 비교하고 데이터 누락·불확실성을 함께 시각화; 이미지 좌표 보정 정보 없이 도시가 실제로 어떻게 바뀌었는지 단정하지 않음.

### 공통 프리미티브
`select_source`, `inspect_asset`, `compare_evidence`, `sequence_steps`, `encode_decode`, `annotate_region`, `answer_with_feedback`. AI는 허용된 프리미티브들을 **유효한 순서와 연결 규칙**으로 결합할 뿐, React 코드를 반환할 수 없다.

### 3D의 적용 기준
Smithsonian의 CC0 GLB 사용권·원본 크기·렌더 성능이 확인되면 Three.js `GLTFLoader`를 `inspect_asset` 시각화에 연결한다. 3D 외관 표시와 실제 기계 기능 시뮬레이션을 혼동하지 않도록 모델링 수준을 구분한다.

**제품 데모 시나리오:** ① 전신기 + 학습목표 → Signal Lab, ② 다른 기관의 기록/지도 → Catalog Compare, ③ 정보 부족 유물 → 근거 요청과 안전한 대안. 심사위원이 각 결과의 '이 주장에 사용된 자료'를 직접 열어볼 수 있어야 한다.

## 7. AWS 배포: 두 단계로 단순화

### Stage L — 무료·로컬 우선 실험
- Next.js 프런트/백과 TypeScript 규칙 엔진을 로컬에서 작동시킨다. 기록은 **버전 고정된 JSON fixtures**. Bedrock은 인터페이스 모킹.
- 실험마다 입력 SHA, 프롬프트 버전, 모델 ID(실행했을 때만), 출력 Spec SHA, 테스트 결과를 기록한다.
- 외부 자료는 공식 URL/권리 정보가 확실한 최소 레코드만 선별한다. API 키를 코드에 포함하지 않는다.

### Stage C — 제출용 AWS 최소 배포 (비용 승인 후)
- **Amplify Hosting**: 접근 가능한 웹앱과 관람객 공개 페이지를 제공.
- **서버 측 Lambda/API**: 기관 API 프록시, Bedrock 요청, 검증 및 발행. API 키와 AWS 권한은 서버에만 존재.
- **S3**: 원본 자산의 해시·승인된 결과물 저장; 공개 자산과 비공개 초안 영역 분리.
- **DynamoDB**: 소장품 정규화 결과, 명세 버전, 승인 상태, 출처/권리 메타데이터.
- **Cognito**: 편집·승인 관리자 접근. 초기 공개 체험은 읽기 전용. 관리자 인증 미완성 시 익명 편집 API는 **출시 금지**.
- **CloudWatch**: 요청·오류·비용 경보/로깅. 원본 민감 파일과 비밀값은 로그에서 제외.

멀티테넌트 기관 연동, 벡터 DB/OpenSearch, Step Functions, 대형 3D 파이프라인, 자동 영상·음성 생성 등은 1차 **제외**. AWS 사용은 Kiroween의 필수 조건이라기보다 제품 구현·시연에 유용한 선택 사항이며 필수 조건은 Kiro 사용이다.

## 8. 보안·저작권·AI 거버넌스

| 위험 | 직접적인 차단 방식 |
|---|---|
| 비공개 또는 제한된 문화유산 미디어 | RightsRegistry 필수, `CC0` 또는 명시 허가만 공개 미디어 빌드에 포함. 공개 메타데이터와 미디어의 권리 구분 |
| 원본 자료 내 프롬프트 인젝션 | 외부 텍스트는 데이터로만 처리, tool/시스템 지시로 사용 금지, 모델에는 제한된 역할·출력 스키마만 허용 |
| SSRF/ZIP 경로·파일 폭탄 | 기관 API 도메인 allowlist, 서버 fetch 상한, 확장자/MIME 확인, 압축 파일 기본 비활성화, 바이트·시간·개수 제한 |
| 악성 AI 생성 실행 코드 | JS/HTML 생성·eval·동적 import 금지, 정적 렌더러 registry·CSP, 샌드박스 미리보기 |
| 역사·물리 환각 | 출처 locator 검증, 수학/규칙 테스트, 사람 승인, 근거 부족 시 '체험 불가/대체안' |
| 모델 지역·비용·계정 | 호출 상한 및 AWS Budgets, 리전 고정/데이터 이동 검토, 무료 로컬 모드, 사용량 계측 |
| 무단 공개 또는 원본 변경 | 원본 불변, 변경 이력, 권한 기반 `APPROVED` 상태만 발행, 공개 URL read-only |

Bedrock Guardrails의 contextual grounding은 **추가 신호**일 뿐 사실의 자동 인증서가 아니다. 특히 생성된 상호작용 규칙/시뮬레이션의 타당성은 별도 결정론적 테스트가 필요하다.

## 9. 테스트·판정 기준 (개발 전에 사전 등록)

### 기술 게이트
- **T0 Source**: 공개 미디어 사용권·원본 URL·해시 모두 확인; 미확인이면 해당 자산의 공개 차단.
- **T1 Spec**: 생성된 JSON 100% 스키마 통과; 두 번째 의미 검증에서 허용 interaction enum, 근거 ID, 매개변수 범위 확인.
- **T2 Evidence**: 공개되는 핵심 역사적 사실 100%에 source+locator; P0 근거 없는 핵심 사실 0건.
- **T3 Function**: 2종의 실제 브라우저 체험에서 최소 3개 조작 경로·키보드 경로·결정론적 정답 비교를 통과.
- **T4 Generality**: 개발 fixture와 다른 기관/자료에서 동일 compiler + renderer로 2종 생성; 새 사례마다 전용 JS를 새로 코딩하면 **일반화 실패**.
- **T5 Refusal**: 증거 부족 유물에서는 구현되지 않은 작동 원리를 단정하는 시뮬레이션 0건.
- **T6 Comparison**: 동일 입력·학습 목표로 독립 GPT 직접 제작과 기획·수정 시간, 역사 사실 오류, 브라우저 테스트, 개발자 개입량, 호출 비용을 공정 비교. 이 결과가 없으면 **경쟁우위 HOLD**.

### 투자 판단
- **GO (MVP)**: T0–T5 통과, T6 비교에서 개선 1개 이상 계측, 일관된 관람객 체험을 시연.
- **HOLD**: 핵심 기능은 동작하지만 모델 독립 평가/권리/시간 비교가 불완전.
- **NO-GO/피벗**: 블라인드 자료에서 근거 없는 작동 기능을 반복 생성, 규칙 검증 없이 임의 코드를 허용, 직접 GPT 대비 추가 제작 가치가 없다.

현재 기준선 55/55는 **기존 수동 분류 엔진 및 자체 검증 시험만** 나타낸다. 위 T1–T6를 달성했다는 뜻이 아니다.

## 10. 개발 순서와 기획/개발 결합

| 우선 | 작업 | 산출물 | Gate |
|---|---|---|---|
| D0 (즉시) | 기술 스택 호환성·라이선스·모델 접근권한 **읽기 전용 검사** | ADR 확정, AWS 과금/접근 리스크 | 승인 판단 |
| D1 | 기존 ExperienceSpec v0.1 → v0.2 스키마+구조/권리 검증기 | fixture+negative cases | T0–T2 |
| D2 | Signal/Timeline renderer와 browser tests 정비 | 2종 재현 가능 앱 | T3 |
| D3 | Bedrock 5.5/2 Lite 어댑터와 모델 동일조건 비교 (비용 승인 후) | model output JSON·실패 이력 | T1/T5 |
| D4 | 블라인드 소장품 → 승인 → 발행, GPT 대조 실험 | 비교표·관람객 URL | T4/T6 |
| D5 | 감사로그·권리·접근성·보안·영상·오픈소스 제출 점검 | Kiro 스펙·후크·공개 저장소·영상 | submit |

**예정 작업 폴더 (생성/수정 승인 전)**: `apps/web`, `packages/source-adapters`, `packages/evidence-contract`, `packages/experience-spec`, `packages/experience-runtime`, `tests/fixtures`, `.kiro/specs`, `.kiro/steering`.

**이전 GhostWeb 개발 활용**: Python ZIP 경로 분석/보안/해시 자산은 취약점 D1.2 정리 후 *선택적 source-adapter*로만 검토. 웹사이트 복구 기능 자체를 새 제품의 핵심으로 가져오지 않는다. 기존 repo·메인 브랜치·감시 자동화는 변경하지 않는다. 공모전 제출 프로젝트가 새 원본 저작물이어야 한다는 규정과 이전 코드 재사용 공개 조건을 확인한다.

**제출 기준**: 2026-12-05 오전 07:00 KST 마감. 공개 작업 앱 URL, 공개 GitHub + OSI 라이선스 + root `.kiro/`, 3분 미만 공개 YouTube, Kiro 활용 설명, 영문 설명 또는 번역이 필요하다. 현재 부문은 **Frankenstein 우선 검토**이나 최종 선정하지 않았다.

## 11. 개발 전 의사결정 및 실행 경계

**현재 기획자가 정해도 되는 범위**: 원본 불변·근거 계약·명세 기반 실행·2개 유형 한정·로컬-first·자체 테스트·모델 벤치마크 방법.

**실제 사용자 승인 후 진행할 항목**: AWS 계정 및 과금 한도, 실 Bedrock 모델 호출/해당 리전 데이터 이동, 관리자 로그인/외부 계정 연결, 기존 Kiro 저장소의 제품 전환 및 브랜치 운영, 공개 배포·라이선스·외부 유물 미디어 포함.

**이번 문서는 위 조건을 확정하기 위한 제안이며 어떤 유료 API, GitHub 변경, 배포도 수행하지 않았다.**

## 12. 확인 가능한 주요 공식 자료

1. [Kiroween 2026 공식 규정](https://kiroween.devpost.com/rules)
2. [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/)
3. [The Met Collection API (2026 v1.1)](https://metmuseum.github.io/)
4. [Smithsonian Open Access 개발자 자료](https://www.si.edu/openaccess/devtools)
5. [Smithsonian Open Access 권리·파일 형식 FAQ](https://www.si.edu/openaccess/faq)
6. [Amazon Bedrock Structured Outputs](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html)
7. [Claude Haiku 5.5 on Bedrock (2026-10-07 출시)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-haiku-5-5.html)
8. [Claude Sonnet 5.5 on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5-5.html)
9. [Amazon Nova 2 Lite](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-lite.html)
10. [Bedrock Guardrails Contextual Grounding](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html)
11. [AWS Amplify Next.js Deployment](https://docs.amplify.aws/nextjs/deploy-and-host/)
12. [AWS Amplify Storage/S3](https://docs.amplify.aws/nextjs/build-a-backend/storage/set-up-storage/)
13. [Three.js GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html)
14. [Playwright official documentation](https://playwright.dev/docs/intro)
15. [Node.js LTS release schedule](https://github.com/nodejs/Release)
16. [React versions](https://react.dev/versions)

**근거 주의:** 공식 문서는 기술의 존재/지원 범위만 확인한다. Re:Collection이 이를 구현하거나 경쟁 기술보다 우수하다는 주장을 입증하지 않는다. 버전·가격·모델 접근 가능 리전은 실제 계정/실행 환경에서 재검증한다.