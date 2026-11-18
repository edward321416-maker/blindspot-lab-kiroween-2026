# Re:Collection 3.17 — Met A COMMITTED 마커 보안 패치 검증 보고서

## 결과

- 상태: **SUCCESS**
- BASELINE_TESTS: **32 / 32 PASS**
- PATCHED_TESTS: **37 / 37 PASS**
- REAL_CAPTURE_VALIDATION: **2 / 2 TRUE**
- NEGATIVE_MARKER_TESTS: **5 / 5 PASS**
- SOURCE_HASHES_UNCHANGED: **YES — 2 / 2 response.bin 검증 전후 동일**
- ORIGINAL_WORKSPACE_UNCHANGED: **YES — 26 / 26 파일의 경로·크기·수정시각·SHA-256 동일**
- KIRO_PRODUCT_CHANGED: **NO**

## 최소 패치 범위

수정한 파일은 STAGING 복사본의 `capture_met.py`와 `test_capture_met.py`뿐이다.

`verify_committed_directory()`는 이제 다음을 모두 요구한다.

- 마커가 정확히 네 줄일 것
- 첫 줄이 정확히 `COMMITTED`일 것
- `objectID` 줄이 요청한 정수 ID의 10진 문자열과 정확히 일치할 것
- `sha256` 줄이 다시 연 `response.bin`에서 계산한 SHA-256과 정확히 일치할 것
- `committed_at_utc`가 파싱 가능한 timezone-aware UTC 시각일 것
- 기존 `capture.json`의 ID, 바이트 크기, 저장 SHA-256, 두 검증 상태가 모두 일치할 것

`capture_one()`, HTTP 요청, JSON 파서, 원자적 저장 방식은 변경하지 않았다. 변경 내용은 `marker_patch.diff`에 unified diff로 보존했다.

## 테스트

수정 전 원본 코드 복사본에서 Python 3.14.0 표준 라이브러리 `unittest` 32개가 모두 통과했다. 기존 fixture 산출물은 `baseline_unit_test_artifacts`로 이동해 보존했고 삭제하지 않았다.

수정 후 기존 fixture를 실제 네 줄 마커로 바꾸고 다음 음성 시험을 추가했다.

1. 잘못된 `objectID` 거절
2. 잘못된 SHA-256 거절
3. `COMMITTED` 접두부만 남은 마커 거절
4. UTC 시간대가 없는 완료시각 거절
5. 추가 줄이 있는 마커 거절

전체 37개 테스트가 통과했다. 변조 시험은 STAGING의 테스트 fixture에서만 실행했다.

## 실제 Met A 원본 검증

원본 디렉터리를 읽기 전용으로 검사했으며 두 결과 모두 `True`였다.

| objectID | 패치 검증 결과 | 검증 전 SHA-256 | 검증 후 SHA-256 |
|---:|---|---|---|
| 36491 | True | `1591688c92ce0cfe788a47edad4bd9a84e70afbd1b7b7f58b754ccb902699b6c` | `1591688c92ce0cfe788a47edad4bd9a84e70afbd1b7b7f58b754ccb902699b6c` |
| 45434 | True | `eddd9f43c0d80b176c53a895ef2776f8d77010ce5ac945a3bdeb043a2bc8d72e` | `eddd9f43c0d80b176c53a895ef2776f8d77010ce5ac945a3bdeb043a2bc8d72e` |

두 파일 모두 크기와 수정시각도 검증 전후 동일했다. 원본 `capture.json`과 `COMMITTED`도 수정하지 않았다.

## 결과물

- `capture_met.py` — 패치된 STAGING 복사본
- `test_capture_met.py` — fixture 수정 및 5개 회귀 시험 추가본
- `marker_patch.diff` — unified diff
- `baseline_test_results.txt` — 수정 전 32개 테스트 로그
- `patched_test_results.txt` — 수정 후 37개 테스트 로그
- `real_capture_validation.json` — 실제 원본 2건 검증 결과
- `original_workspace_before.json` — 원본 작업 폴더 최초 스냅샷
- `sha256_manifest.json` — 원본 불변성 및 STAGING 산출물 해시

Met C세트, 이미지, Drive 공유 설정, Kiro 제품, Git 브랜치에는 접근하거나 변경하지 않았다.
