# Re:Collection 3.17 — Met A evidence independently audited (2/2), marker verifier patch required

**Date:** 2026-11-18 KST  
**Status:** MET_A_EVIDENCE_INTEGRITY_PASS / COLLECTOR_MARKER_PATCH_READY / INDEPENDENT_HTTP_ORIGIN_UNCONFIRMED / RIGHTS_AND_PRODUCT_HOLD.  
**Code ownership:** This is a *research-only docs handoff*, not a Kiro product implementation. The user-attached raw evidence and test code remain in private archives, **not in this public repository**.

## Source ZIP actually opened by reviewer

The user attached `ReCollection_3_17_Met_A_Independent_Review.zip` (**31,441 bytes**, SHA256 `e28e7745eb633ca68526e03f4481d4f582aeb9553503f086f8e91b31ee98f1ac`), containing two original `response.bin` JSON files, sanitized capture metadata, original `COMMITTED` markers, record status, test logs and source.

A newly authored offline independent verifier (not the original author's 32-test oracle) passed **34/34** integrity checks: ZIP CRC, all **16/16 payload SHA256**, strict objectID, canonical request/final source URL, HTTP 200, reported Content-Length and MIME, response bytes vs capture/manifest/marker digest, UTC ordering.

| Met object | Accession | Raw bytes | SHA256 | Reported UTC capture |
|---|---|---:|---|---|
| [36491](https://collectionapi.metmuseum.org/public/collection/v1/objects/36491) | `JP10` | 2,171 | `1591688c92ce0cfe788a47edad4bd9a84e70afbd1b7b7f58b754ccb902699b6c` | 2026-11-18T05:29:20.581351Z |
| [45434](https://collectionapi.metmuseum.org/public/collection/v1/objects/45434) | `JP1847` | 2,385 | `eddd9f43c0d80b176c53a895ef2776f8d77010ce5ac945a3bdeb043a2bc8d72e` | 2026-11-18T05:29:21.939083Z |

They have the same Hokusai print title, but different accession numbers, dimensions, image URLs, and direct collection identifiers. The first `36491` JSON includes `metadataDate=2026-08-28T04:59:40.517Z` versus a *stale web-indexed* 2025-11-11 date. Do not claim the historical field diff, because the prior actual raw body is absent.

**Redaction scope:** the shared `capture.json` copies omit two `Set-Cookie` response headers each; source original header metadata bytes cannot be independently rehashed, but `response.bin` was not modified. The user-submitted evidence and manifest are internally consistent. This audit **did not** independently rerun the upstream live HTTP exchange; do not claim proof of origin at the network/TLS level.

## Independent security finding (reproduced)

The user-supplied new Codex collector `capture_met.py` had a fail-open verification in `verify_committed_directory()`: testing only `marker_path.read_text(...).startswith("COMMITTED\\n")` meant that tampering the `COMMITTED` object's identity or hash, or replacing the marker with only the prefix, erroneously returned True.

- Against **isolated copies** of authentic item 36491: wrong marker objectID = false PASS; wrong SHA = false PASS; prefix-only marker = false PASS; altered response.bin = correct reject.
- The actual submitted marker files are valid. Source data acceptance is not reversed by this code bug.
- Created a minimal unified diff for `capture_met.py` plus `test_capture_met.py` requiring exact four lines, bound ID and SHA, strict UTC marker timestamp; **32 old Codex tests + 5 new negative tests = 37/37 PASS**. Reapplied the patch in a fresh standalone copy: 37/37 PASS.
- Independently reran the attached Codex tests **32/32 PASS**, and independently reran the **previous, separate 3.17 collector packet** tests **32/32 PASS**. These are distinct test suites and must not be conflated.

## Verified private persistence

- Private Drive folder: https://drive.google.com/drive/folders/1xV5svRvVs5laP9jhducHZxsE2bQi7B2d
- Full **private** review kit ZIP, including unchanged user-submitted ZIP, newly-authored read-only verifier, 34/34 results JSON, complete 4-page report PDF, strict marker unified patch and test logs: https://drive.google.com/file/d/1ObJPTjdW53mrPnnuPUw7IuRg6G2bO_Nc/view, **167,388 bytes**, SHA256 `3becd3fd9ce610096221d3f2d1ce014e1d8398119c40f680e42af1e7ea7754db`; remote size/parent read back.
- Research decision record: https://docs.google.com/document/d/1K2ht_yBupZ9-3DKwUibXgL0aOnRngPpRCdS0gyt01jU/edit
- PDF-in-ZIP SHA256 `fb8149b53b7d319868b6ceabc45ceb8e03980f261cf25b59ac33a3c0d3ebbdf7`, rendered all four pages, no overflow/replacement glyphs.

## Next gates (strict)

1. Apply only the reviewed, idempotent marker hardening patch to an isolated copy of Codex collector (NOT directly to frozen Kiro code) and rerun 37/37. Source ZIP and its original response bytes stay immutable.
2. Mark A records as **EVIDENCE_INTEGRITY_PASS** with `independent_http_origin_verified=false`; don't call licensed media or expert claim approved.
3. Collect **C pack** official JSON objects `437127` and `436535` only, again with original response hashes, headers and identity, leaving media download / license review separate.
4. Preserve 3.2 sealed holdout, B5.2/D2-V0 product development separation and no public museum image/media copying.

**DO NOT claim real Kiro integrated museum-source test, live HTTP second-source authentication, human curator review, or copyright clearance based on this audit.**
