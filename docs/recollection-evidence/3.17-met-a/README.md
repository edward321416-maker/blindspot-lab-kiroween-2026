# Re:Collection 3.17 — Met A marker validation evidence

This directory contains the reviewable source, tests, patch, and measured logs for a fail-closed `COMMITTED` marker validation fix.

## Verified results

- Existing baseline suite: **32/32 passed** before the patch.
- New marker regression tests: **5/5 passed** after the patch.
- Combined patched suite: **37/37 passed**.
- Local read-only validation of the two Met A captures: **2/2 returned `True`**.
- Original local response hashes remained unchanged before and after validation.

The five new regression tests reject:

1. a wrong marker `objectID`;
2. a wrong marker SHA-256;
3. a marker containing only the `COMMITTED` prefix;
4. a completion timestamp without a UTC timezone; and
5. a marker with an extra line.

## Reproduce the code tests

Python 3.11 or later is sufficient; the tests use only the standard library. From this directory, in a clean or disposable checkout, run:

```text
python -B -m unittest -v test_capture_met.py
```

The expected final lines are:

```text
Ran 37 tests

OK
```

The tests create a local `unit_test_artifacts` directory. Run them in a disposable copy if a pristine checkout must be retained.

## Local-only source evidence

The raw Met API responses, complete HTTP capture metadata, `COMMITTED` files, review ZIP, and institution images are intentionally not published. Consequently, the code tests are fully reproducible from this directory, while the 2/2 real-capture result is represented by the sanitized validation record and immutable response hashes rather than by public raw data.

| Object ID | Local response SHA-256 | Patched validator |
|---:|---|---|
| 36491 | `1591688c92ce0cfe788a47edad4bd9a84e70afbd1b7b7f58b754ccb902699b6c` | `True` |
| 45434 | `eddd9f43c0d80b176c53a895ef2776f8d77010ce5ac945a3bdeb043a2bc8d72e` | `True` |

## Files

- `capture_met.py` — patched validator source.
- `test_capture_met.py` — 32 baseline tests plus 5 marker regression tests.
- `marker_patch.diff` — unified diff against the unpatched local source.
- `baseline_test_results.txt` — measured 32-test baseline log.
- `patched_test_results.txt` — measured 37-test patched log.
- `real_capture_validation.json` — sanitized 2/2 local validation record.
- `sha256_manifest.json` — public artifact hashes and source-evidence hash checks.
- `validation_report.md` — measured validation summary.

## Security and provenance

- No cookies, authentication headers, tokens, passwords, absolute user paths, raw responses, complete `capture.json` files, ZIPs, or images are included.
- Local absolute paths were replaced with relative or scope-only labels in public derivative JSON files.
- This is research validation evidence produced in an OpenAI Codex session. It is not Kiro-built product functionality and does not change the repository's product/research HOLD state.
