# Re:Collection 3.18b — Windows Codex stage (RUN NOT YET VERIFIED ON USER PC)

The runner was tested in an isolated non-Windows sandbox: **70/70** suite, **49/49** fresh subprocess gate, forged-log rejection, four malformed-rights-approval rejections, and refusing an existing stage (exit 32). This does NOT mean the user's Windows Codex session has executed it.

## Pinned scope

- Original patched source commit: `d344673599408732ce1400a22cafb798c6e760b4`.
- Six public code files are fetched from exact immutable commit `d344673599408732ce1400a22cafb798c6e760b4` with byte-size + SHA-256 verification, no new dependencies.
- Runner: `windows_stage_318b.py`, **13,857 bytes**, SHA-256 `89fddeb6084cb26d9fe44ccd5bfc1f9cf864d524c0b631d24ada74d10ab18fe7`.
- No mutation of Kiro product, existing Met A/C evidence, default branch, or historical source folders.
- No Met API requests or museum images, no PR/merge/push by the runner.

## Windows Codex command

In the user's authorized existing Windows terminal, first obtain `windows_stage_318b.py` from the **immutable commit URL published for this stage branch**; calculate SHA-256 and ensure it equals the value above. Use existing Python 3.11+; **do not install software or seek credentials**.

```powershell
py -3 .\windows_stage_318b.py --workspace-root "<existing local hackathon folder>" --stage-name "ReCollection_3_18b_Windows_STAGE_20261119"
```

The command creates a NEW child folder and refuses to overwrite an existing one. If DNS or HTTP access fails, report HOLD; do not silently substitute stale or different source files.

## Windows acceptance

Read `results/stage_validation_report.json`: require `WINDOWS_STAGE_PASS`, actual Python exit 0, 70 unique passing cases, fresh 49-test process exit 0 + run ID, adversarial tests pass, and all 6 source hashes preserved. Report `STAGE_VALIDATION_BUNDLE.zip` and its SHA-256 to ChatGPT for independent review. The report bundle contains only test logs/metadata; do not add private raw museum files.

All AUTHORED_TEXT/IMAGE rights 4 slots and original Met C 2 raw-byte independent checks stay HOLD. Windows status remains **NOT_EXECUTED** until Codex supplies real machine evidence.
