# Re:Collection 3.18 — Met C evidence

This directory is the public, sanitized reproduction packet for the Met C JSON-only run on object IDs `437127` and `436535`.

## Results

- Baseline collector tests: 37/37 PASS.
- Baseline plus new integrity tests: 49/49 PASS (12 new tests, I01–I12).
- Rights/output safety tests: 8/8 PASS (R01–R08).
- Combined isolated run: 57/57 PASS.
- Raw JSON captures: 2/2 verified locally; public hashes and sizes are in `public_capture_summary.json`.
- Rights slots: 2 metadata-only decisions and 4 `RIGHTS_REVIEW_HOLD` decisions.
- Image files downloaded: 0.

`METADATA_ONLY_ALLOWED` is a workflow decision for the reviewed basic metadata in this packet. It is not a legal conclusion. No image or authored-text slot is approved for product use by this run.

## Reproduce the tests

Requires Python 3.10 or newer and only the Python standard library.

```powershell
python -m unittest -v test_capture_met.py test_rights_policy.py
```

Expected result: `Ran 57 tests` followed by `OK`.

To run the groups separately:

```powershell
python -m unittest -v test_capture_met.py
python -m unittest -v test_rights_policy.py
```

The collector is intentionally fixed to two IDs. A live run requires an empty private output directory and a successful 49-test gate log:

```powershell
python collect_met_c.py PRIVATE_OUTPUT_DIRECTORY integrity_49_test_results.txt
```

Do not point it at this public directory. The collector writes raw evidence that must remain private.

## Evidence boundaries

The public packet includes code, tests, logs, a unified diff, content hashes, and a sanitized rights summary. It excludes `response.bin`, `capture.json`, `COMMITTED`, response headers, cookies, image files, absolute workstation paths, and credentials.

Primary policy references:

- [Met Open Access](https://www.metmuseum.org/hubs/open-access)
- [Met Terms and Conditions](https://www.metmuseum.org/policies/terms-and-conditions)
- [Met object 437127](https://www.metmuseum.org/art/collection/search/437127)
- [Met object 436535](https://www.metmuseum.org/art/collection/search/436535)

## File map

- `capture_met.py`, `test_capture_met.py`: collector verifier and 49-test suite.
- `rights_policy.py`, `test_rights_policy.py`: fail-closed slot policy and 8 synthetic tests.
- `collect_met_c.py`: gated two-object JSON collector; no image download code.
- `met_c_integrity_patch.diff`: unified diff from collector baseline commit `93c4f7a9765af8c4fcd5a4c74f1ee7c98e9b2bd8`.
- `*_test_results.txt`: measured test logs.
- `public_capture_summary.json`: sanitized capture measurements.
- `rights_review.json`, `rights_slots.csv`: source-separated rights observations and decisions.
- `sha256_manifest.json`: hashes for all other public payload files.
- `validation_report.md`: scope, gate results, and unresolved holds.

No pull request, merge, deployment, or product-code change is part of this evidence branch.

The diff uses zero context to keep its own Git blob free of trailing-whitespace false positives. Validate or apply it from a directory containing the two baseline files with:

```powershell
git apply --check --unidiff-zero met_c_integrity_patch.diff
```
