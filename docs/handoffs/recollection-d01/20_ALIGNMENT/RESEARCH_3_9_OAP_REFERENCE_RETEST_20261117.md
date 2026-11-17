# Re:Collection 3.9 — OAP-0.1 reference retest and B3/B4 alignment

**Date:** 2026-11-17 KST  
**State:** RESEARCH-REFERENCE PASS / KIRO PRODUCT NOT TESTED / PUBLISH HOLD  
**Source:** executed locally by the research assistant, not in the user's Windows Kiro repository.

## Measured research results

Previously fixed, researcher-authored 3.8 G0 and G1-S inputs and 3.9 attack/benign pairs were run through a new standalone Python output-policy reference. **38 unique cases, 2 identical runs each, 76 deterministic judgments**, with 0 discrepancies against their self-authored expected blocking and impact labels. The older oracle/fixture bytes were preserved.

After the first pass, **five new cross-sink attacks were authored**, and all 5 were incorrectly allowed by the first reference model: fabricated feedback literal; extra rendered node label; media URL in an educational constant; arbitrary output kind with factual prose; root metadata used as visible output. A revised strict output contract blocked all 5. An intermediate 5-case benign overblocking issue was resolved by explicitly separating the pre-existing research harness fields from the allowed public-output contract, and all 76 cases were rerun. Eight additional **open-label** metamorphic probes matched expected labels.

These are NOT independent or blind tests. The oracle, attacks, test harness and reference are researcher-authored. No human curation, source truth check, Kiro product code run, model inference, cloud service or browser publisher test was performed.

## Engineering boundary

The prior user-reported Kiro B2 checkpoint is local commit `54f88b5be8a50afa187640d7d8564f75cb7b51ae`, with 112/112 tests, **NOT independently verified here**. The current GitHub `19_WORKFLOWS/KIRO_B3_IMPLEMENT_RESTRICTED_RUNTIME_20261117.md` calls for B3 only. No completed B3 code result is available in this workspace.

**Preserve B0/B1/B2 frozen oracle, unchanged B3 scope, and B3 R01–R06.** OAP-0.1 is only a **proposed later versioned output assurance contract**, not an approved change to current B3 or an instruction to start B4.

Recommended later contract:
- Exact, recursively validated public output kind and field allowlists across question, answer, branch, feedback, multilingual copy and media.
- Fail closed on arbitrary factual strings, unknown AST operators, nested literals and model-supplied `approval`.
- Trusted educational-model value registry, reviewed-text + context digest, immutable media rights snapshot.
- Statically track field consumption and downstream claim-to-feedback use, including unexecuted branches.
- Track system-owned selected OR evidence witness, displayed text hash and approval scope; revoke after any relevant changes.
- Distinguish safe UI instruction templates from unverifiable free text and measure benign overblocking.

After actual B3 completion, require an isolated product-specific adapter and rerun known attack + benign cases and the additional new attacks **against actual Kiro B2/B3**. New 20-case independent blind oracle and curator review remain pending. No sealed 3.2 evaluation data or answers are to enter the development prompt or this public repo.

## Reproducibility provenance

- Original 3.8 G0 fixture SHA256: `adc0b9a5b067af1fef2a28e849e6dc04b1bd77f69b4d838b9b427a1e72047468`
- Original 3.8 oracle SHA256: `214376a7469f72561cf37cd3ea77a06caa0c9968c40d3b2636cae23bafbec8e3`
- 3.9 existing regression matrix SHA256: `b3202c7bffa78511018f3fe4101954bf19f6f5381562b698e6e2c757052ef256`

Research scripts, full fixture results, unified diff and QA PDF are retained in the ChatGPT research deliverable ZIP only, **not** mirrored as product source to GitHub. **PRODUCT PUBLISH HOLD** until separate actual implementation verification and rights/curator gates.