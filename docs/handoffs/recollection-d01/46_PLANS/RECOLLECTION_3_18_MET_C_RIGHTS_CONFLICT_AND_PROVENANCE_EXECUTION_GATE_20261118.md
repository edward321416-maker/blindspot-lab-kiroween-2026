# Re:Collection 3.18 — Met C real-source and rights-conflict validation plan

**Date:** 2026-11-18 KST  
**Status:** PLAN_READY — actual C source capture `0/2`, new test execution `0/20`, new rights clearance `0/6`, Kiro product test `NOT_RUN`.  
**Scope:** Public safe summary only. No Met image files, cookies, full HTTP response captures, user paths, sealed 3.2 holdouts or product code.

## The critical correction to the earlier C scenario

The API record for Met [437127](https://collectionapi.metmuseum.org/public/collection/v1/objects/437127) returned, in a **three-month-old indexed web snapshot**, `isPublicDomain=false` with `primaryImage=""`. Yet the [official Met artwork page](https://www.metmuseum.org/art/collection/search/437127) simultaneously displayed “Public Domain” and Open Access copy, and some image components reported that downloads were unavailable. This is an **unresolved mismatch between metadata, rights signal, and media availability**, not proof the work is legally prohibited, nor proof the image is currently directly downloadable.

The indexed [436535](https://collectionapi.metmuseum.org/public/collection/v1/objects/436535) API returned `isPublicDomain=true` and nonempty `primaryImage`, also **subject to fresh raw acquisition and asset-level review**. Met [Open Access program](https://www.metmuseum.org/hubs/open-access) and [terms](https://www.metmuseum.org/policies/terms-and-conditions) distinguish OA materials from other content. Do **not** hard-code old source signals as current oracle labels.

Keep **four independent fields** for each object:
1. Raw API `isPublicDomain` value and `metadataDate`, with real UTC capture time and entire original body SHA256.
2. The official item-page OA / public-domain wording + evidence locator/retrieval time.
3. Image URL present/absent + image availability. **An empty URL does not itself mean legal infringement.**
4. Intended image/text reuse decision, with item-level evidence, reviewer, scope and version. Neither a URL nor a public-domain value grants blind app publication.

If official source signals conflict, `RIGHTS_REVIEW_HOLD`; metadata-only research preview may be separately allowed following source/citation review. No image download/fallback for this stage.

## Exact immutable starting point

- Original 3.17 public code and 37 test functions: commit [`93c4f7a9765af8c4fcd5a4c74f1ee7c98e9b2bd8`](https://github.com/edward321416-maker/blindspot-lab-kiroween-2026/commit/93c4f7a9765af8c4fcd5a4c74f1ee7c98e9b2bd8), `docs/recollection-evidence/3.17-met-a/capture_met.py` and `test_capture_met.py`. Existing A data/commit **must not be modified**.
- Private actual A response SHA256: object 36491 `1591688c92ce0cfe788a47edad4bd9a84e70afbd1b7b7f58b754ccb902699b6c`; object 45434 `eddd9f43c0d80b176c53a895ef2776f8d77010ce5ac945a3bdeb043a2bc8d72e`. Both reviewed at 2/2 internal file-integrity only; no independently repeated TLS fetch.
- Only new captures: `437127`, `436535`; exact official HTTPS API URLs, one immutable `response.bin`, `capture.json`, `COMMITTED` per object; no media binary.

## P0 captured-provenance safety gap

The verified public 3.17 `verify_committed_directory()` binds the marker to the response's objectID/hash, and checks a subset of `capture.json`. It does **not** separately require all original capture metadata invariants: `received_sha256`, `byte_size`, `http_status=200`, official `request_url/final_url`, expected JSON content-type and UTC order. Strengthen only copied research tool verifier + tests; do not broaden to Kiro product or original A evidence.

**Test plan, preregistered but NOT EXECUTED:**
- Keep all 37 existing tests.
- New **12 integrity cases** I01–I12: typed object identity, `received_sha256`, stored digest, two byte-size fields, status/MIME, canonical URLs, UTC ordering, malformed/duplicate JSON, and valid C capture.
- New **8 rights/visitor-output cases** R01–R08: OA vs API conflict hold, absent image, non-PD with image URL, PD with URL but unapproved display, third-party fallback ban, simulated rights revocation/reapproval, authored-description independent rights hold, reviewed metadata-only safe fallback.
- **Six item/asset rights slots:** C1+C2 × METADATA, AUTHORED_TEXT, IMAGE. Start `HOLD`; nothing approved by this planning action.

## Bounded Codex execution gate

1. Isolated new Windows data-lab folder; inspect project policy; freeze prior hashes & exact GitHub commit. No edits in Windows Kiro repo or default branch.
2. Run baseline 37/37; fail/stop if nonreproducible.
3. Make *unified diff* against isolated copy for P0 capture metadata verification and 12 new tests; preserve original `capture_one()` behavior unless essential for new immutable C IDs.
4. Pass 37+12 tests first; do not count test plan as PASS.
5. Official HTTPS GET for C1+C2 **JSON only**, strict ID, response bytes, UTC, status/headers/redirect, SHA256 + COMMITTED and readback; no unofficial proxy, credentials, paid service or image downloads. HTTP/DNS failure stays HOLD.
6. Collect current official item-page and OA policy rights evidence separately and run 8 synthetic rights-state tests; `SIMULATED_RIGHTS_CHANGE` never becomes real historical change evidence.
7. Upload *sanitized code/tests/results/diff* to new public evidence branch `evidence/recollection-met-c-20261118` if it does not exist; stop if already exists, no force/no PR/no merge. Report SHA/remote readback. Originals with headers/raw remain private Drive or local `SYNC_PENDING` if authenticated file upload unavailable.
8. Return independent verification packet with source hashes and actual results. Keep all Kiro B5.2/D2-V0/3.2 holdout, independent human curator and release gates separate.

## Exit gates

- G0 source freeze;
- G1 P0 37 baseline + 12 planned new integrity checks;
- G2 real C raw capture 2/2;
- G3 six rights-status/evidence slots;
- G4 eight safe failure-state simulations;
- G5 private/public evidence split;
- G6 ChatGPT independent audit of exact remote source and private raw bytes.

`RAW_PASS` does **not** equal `RIGHTS_APPROVED` or `PRODUCT_PASS`. Explicit `RIGHTS_REVIEW_HOLD` for unverified sources; fail-closed on media output. Do not claim 57/57 tests passed from a plan.

**Local deliverables in ChatGPT:** Eight-page Korean PDF; exact targets JSON; 20-test preregistration CSV; six rights blank rows; seven gates CSV; source-preserving Codex runbook; ZIP with CRC/SHA256. **They are created in this conversation container, not yet executed or committed to the product Git repository.**

**References:** [Official Met API](https://metmuseum.github.io/) · [Met OA](https://www.metmuseum.org/hubs/open-access) · [Met terms](https://www.metmuseum.org/policies/terms-and-conditions) · [437127 artwork page](https://www.metmuseum.org/art/collection/search/437127).
