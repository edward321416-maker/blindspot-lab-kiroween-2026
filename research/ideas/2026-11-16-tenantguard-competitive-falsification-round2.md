# BLINDSPOT LAB / TenantGuard - 2026-11-16 경쟁 기술 및 사용자 미해결 문제 심층 검증 (Round 2)

> **Research only. Not selected for product implementation.** Existing Kiroween Kiro development/spec branches, apps/ and packages/ are not touched. All examples and thresholds below are explicitly marked as observed facts, mathematics, or **hypotheses**. No new model inference, external human study or commercial competitor run was executed.

## Executive decision

**Generic "detect CV regressions and block release" => differentiation NO-GO as a standalone contest concept.** Roboflow officially described a tested object-detection Workflow Evals + release gate + CI automation on 2026-11-12, four days before this report, overlapping the previously proposed Blindspot Regression Gate end-to-end. FiftyOne, Kolena, AWS SageMaker fleet pipeline and recent prior-art disclosures cover more of the adjacent space than previously accounted for.

**A narrower P1b idea remains on RESEARCH HOLD:** when a **shared** object detector gets retrained using client A data, automatically forecast which **other tenants/cameras** warrant full verification and prioritize *human-reviewed* regression tests under a known budget, preserving transparent random surveillance coverage and UNTESTED/ABSTAIN. This is not yet proven novel, effective, safe, or demanded.

**Alternate P2:** pipeline-component delta diagnosis (old/new input transforms × model × postprocessing), limited to causal claims about controlled software versions, not field causality. Industrial ML testing literature already describes old/new image-pipeline integration testing; only automated minimal-failure-inducing diff with measured advantage could differentiate it. P3 ProofPack is a **feature** to attach to a demonstrated customer job, not a standalone product thesis.

## 1. Source-backed first-person user needs (not customer validation)

| Event | Original account | Why relevant | Evidence limit |
|---|---|---|---|
| 2026-01-08 / r/computervision | CV engineer deploying **one shared CV model across multiple clients**, adding client A data can introduce false detections for B; full regression run across clients slows releases | Direct same-practitioner A->B business pain and developer workaround of *base model + separate client/subgroup fine-tuning* | Anonymous company; did **not** say they tried FiftyOne/Roboflow then failed; no demand/budget/procurement evidence. https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/ |
| 2025 / r/mlops | Engineer maintaining ~100 client-specific ML models says 5 degrade when migrating containers and block full rollout | Concrete release-blocking *similar* operational problem | Not established as CV or shared model; cannot conflate with Jan2026 practitioner. https://www.reddit.com/r/mlops/comments/1m8so03/ |
| 2021 / r/MachineLearning | DS with client models scattered across cloud/client VPC/on-prem says painful upgrades, late customer detection and poor visibility | Operations and remote context, not merely detector accuracy | Older, cross-domain, not the same customer, no incumbent-failure proof. https://www.reddit.com/r/MachineLearning/comments/ppbjqw |
| 2026-10-26 / AWS official field account | AWS team observed multi-line manufacturing camera angles/glare/light; pooled model underperformed enough cameras to require per-camera fine-tuning | Industrial multi-camera problem independently corroborated by vendor | AWS provides a substantial per-camera, quality-gated alternative; not evidence need for a new product. https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/ |

**G4 remains FAIL/UNKNOWN:** We have no **same identifiable team** documenting a tested incumbent and the unresolved requirement after that workaround. Do not imply real users tried our idea or request a build on this basis.

## 2. Competitor/precedent functional coverage (official primary sources where possible)

### 2.1 Roboflow Workflow Evals - strongest disconfirmation (2026-11-12)
Official original https://roboflow.com/blog/computer-vision-regression-testing (Mostafa Ibrahim, published Nov 12 2026):
- Same fixed labeled 17 image cases, five pill-type count checks (85 checks).
- Different model/Workflow versions (RF-DETR Small) are run on identical cases, detailed per-case and per-class failure maps, version comparison and recorded immutable historical Run settings.
- Explicit **Publish -> Publishing Requirements -> Require an Eval to pass**; per-check minimum pass rate; auto-publish may run checks automatically.
- Evals can be invoked through Python SDK/CLI/HTTP API/MCP and as a CI job that fails with nonzero exit. User-configurable rules and latency checks.
- Public tutorial shows deliberately crippled version (baseline 85/85 vs candidate 35/85 checks); this is **vendor tutorial demonstration, not unbiased head-to-head** against our code.
- **We cannot claim** newness for "model swap regression", "workflow check", "CI gate", "fix known failure image", "model input preprocessing regression" or "one-click release review". Cross-tenant contracts and independent model-blind oracle confidence have not been demonstrated absent in Roboflow; require direct hands-on comparison.

### 2.2 FiftyOne core and plugin
- Open-source \`evaluate_detections()\`: TP/FP/FN, matching IDs/IoUs per detection and samples. https://docs.voxel51.com/user_guide/evaluation/detections.html
- Evaluations: multi-version, metadata/saved-view slice/scenario analysis, sample/class performance. https://docs.voxel51.com/user_guide/app.html and https://docs.voxel51.com/user_guide/evaluation.html
- Community Model Comparison: \`hithit\`, \`hitmiss\`, \`misshit\`, \`missmiss\`, localized better/worse; currently documented TODO unmatched FP tallies (a limited plugin omission not evidence no workaround). https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
- Data curation / high-quality golden QA set/selection workflows already documented. https://docs.voxel51.com/getting_started/annotation/02_setup_splits.html
- **Strong competitor arm must be FiftyOne + reasonable Python script** (not crippled GUI-only).

### 2.3 AWS fleet & deployment baseline (2026-10-26)
- AWS published an **actually runnable example architecture**, per-camera model trained/evaluated/compiled/registered using SageMaker v3 + Model Registry + Neo, Step Functions, SQS, Lambda. Gates exported ONNX on balanced accuracy/defect recall and retains previously approved per-camera model. https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
- AWS tutorial's reported ~$0.07 run applies to its **synthetic sample** and on-demand specific region instance, NOT to our experiment or future product cost.
- Alternative architectural solution: do not share one global checkpoint among all tenants. Fine-tune and version client/camera-specific models. This is the Jan2026 poster's own proposed workaround. A new shared-model release platform must justify why that workaround is too expensive or undesirable. Microsoft's official multitenant AI architecture also discusses shared base with tenant-specific tuned versions: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/ai-machine-learning
- SageMaker Shadow Tests compare deployed/candidate model-container-infrastructure versions, primarily operational latency/errors; not equivalent to human-verified object level regression: https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html

### 2.4 Other established tools and published concepts
- Kolena's **2022** computer vision test-case/test-suite/regression test methodology + pre/post-release scenario comparisons: https://medium.com/kolena-ml/best-practices-for-ml-model-testing-224366d3f23c . Do not assert its current SKU covers all older capabilities.
- Landing AI has model comparison per-image/metrics UI: https://landinglens.docs.landing.ai/compare-models .
- A publicly accessible PatentScope mirror https://eureka.patsnap.com/patent/CN122289904B describes **high-risk scene slice regression gates, conditional traffic routing and rollback**. Treat this as concept-overlap/potential prior-art lead **only**, not independently verified patent legal status, freedom-to-operate or an infringement finding.
- 2025 ACM TOSEM study of 11 DNN test-selection methods found ways selection can underperform; up to **86.85% relative coverage drop** in settings studied; no reason to infer our algorithm is immune: https://doi.org/10.1145/3715693
- 2026 risk/cost-aware CI regression-test prioritization exists in non-CV software: https://www.mdpi.com/2079-9292/15/17/3854 (retrospective ABB logs, not prospective CV validation). Novel "priority ranking" alone is not established.
- Industrial pipeline pre/post camera firmware/preprocessing swaps for fault identification were described in 2023: https://pmc.ncbi.nlm.nih.gov/articles/PMC10280203/ . P2 must measure extra diagnostic value beyond this standard protocol.

## 3. New product hypothesis: **ChangeScope** (TenantGuard specialized, not selected)

### User and job-to-be-done
- **User:** CV release engineer responsible for one **shared** model used by many sites/clients.
- **Trigger:** training set/model updated to address new client A defect class or camera condition.
- **Decision:** which of N other clients need full re-evaluation first under 30-60 minutes while protecting verified critical cases, and which must remain UNTESTED rather than automatically approved.
- **Who pays?** A CV software vendor/operator losing deployment velocity from repeated cross-client review. This is **hypothetical until interview / direct use evidence**.

### Proposed analysis units and input requirements
- Exact old/new model or *frozen predictions* (A/B), versioned preprocessing and label ontology.
- Per-tenant images with provenance tags; independent GT and non-alert control samples; per-image and per-model content hashes.
- **Training delta:** timestamped changed/added training image IDs/labels and which tenant contributed, NOT tenant raw private images shared to other tenants.
- Tenant constraints: critical class, camera condition, per-tenant policy and never-overridden minimum surveillance sample.
- Output statuses: \`CONFIRMED_REGRESSION\`, \`CONFIRMED_FIX\`, \`LABEL_DISPUTE\`, \`ABSTAIN\`, \`UNTESTED\`, \`NO_OBSERVED_REGRESSION\` (last never means guaranteed safe).

### Distinct potential engine (needs measurable falsification)
1. **Cross-tenant change exposure estimator:** identify changed data's class/context representation and its neighborhood overlap with tenant evaluation distributions. This is *associational risk ranking*, not causal proof or model-safety certificate. Report calibration.
2. **Budgeted release audit:** reserve tenant-level stratified/random sentinel samples FIRST, then allocate remaining inference/human-label budget to high-risk cases; expose uncovered tenant/slices and inference cost. Compare to uniform random, balanced stratified, uncertainty/margin, embedding distance and FiftyOne+custom script with **identical** labeling/inference budgets.
3. **Version-pair discrimination:** rank cases by the old vs new prediction-difference features; hold out new clients/sessions to assess prospective transfer, not only cherry-picked failures.
4. **Oracle and release contract:** independent human adjudication plus immutable offline evidence manifest, no automatic PASS when important data remain untested; CI must distinguish FAIL, REVIEW and UNTESTED.
5. **Optional responsible causal isolation:** only on *controllable software components*, replay \`preprocess_old/new × model_old/new × postprocess_old/new\`; isolate which change toggles failure and interaction terms. Do not claim environmental causality or complete root cause identification.

### Why it might be meaningfully distinctive
Not “automatically perform evaluation”: it would predict a **cross-client blast radius from training modifications** *before* expensive blanket verification, then provide measurable less wasted work while showing the untested coverage explicitly. Neither we nor independent sources have yet demonstrated that vendor platforms lack all such functionality, so this is a **falsifiable hypothesis** not a novelty claim.

### Most direct rejection cases
- Baseline "FiftyOne slice evaluations + a <100-LOC script" or Roboflow custom checks achieves the same primary outcome with negligible added effort.
- Site-specific models/adapters solve the original user issue with lower total operating costs.
- Change-exposure risk ranking fails to beat stratified random or model disagreement under matched budgets.
- It routinely misses clinically/operationally high-consequence rare regressions; or privacy/annotation license blocks pilot data.
- No identifiable user demonstrates a repeatable unmet job.

## 4. Statistical sanity: test budget cannot guarantee all-tenant safety

No observed failures on *n independent, uniformly sampled* items from one representative tenant implies a one-sided 95% binomial upper bound \`p_upper = 1 - 0.05**(1/n)\` (zero failures). For target \`p_upper <= 1%\`, \`n >= ceil(log(0.05)/log(0.99)) = 299\`.
For *K = 10* tenants simultaneously, Bonferroni 95% familywise confidence uses \`alpha_per_tenant = 0.05/10\`: \`n_per_tenant >= ceil(log(.005)/log(.99)) = 528\`; 5280 items total. At 0.1% bound the requirement grows dramatically. This assumes iid, representative independent draws, fixed pass/fail oracle. Correlated adjacent video frames, adversarially selected clips and uncertain labels invalidate easy reading of these bounds. Predicted-risk selection may find failures faster but **cannot replace the unbiased sentinel samples used for statistical inference**.

| Desired upper failure rate | One tenant (95%, 0 observed) | 10 tenants jointly (Bonferroni 95%) |
|---|---:|---:|
| 5% | 59 | 1040 total (104 / tenant) |
| 1% | 299 | 5280 total (528 / tenant) |
| 0.1% | 2995 | 52960 total (5296 / tenant) |

These are **mathematical planning examples, not observed customer incident rates**. A conditional approach should report “insufficient evidence” when sample requirements cannot be met.

## 5. What model/data experimental work would REALLY test this new claim?

Kiro Phase5's proposal of **RT-DETR R50vd vs RT-DETRv2 R50vd on COCO/Sama** may test generic version regressions but **does NOT by itself simulate client-A fine-tuning causing client-B regressions**; the two checkpoints differ by broad release/training, not a controlled tenant-A addition. Their correlation/annotation independence issue was separately flagged and remains. Therefore model-version study ≠ multi-tenant causal-interference test.

A relevant additional **future** benchmark design requires:
1. Same detector family/architecture and **fixed group-structured** evaluation data with separate site/client/camera IDs or an explicitly labelled proxy grouping (real site IDs preferable).
2. Model A frozen, Model B trained only with a preregistered incremental sample from group A. Hold out group B/C testing and identify train/test leakage at session/site level.
3. Ground truth independently reviewed on a representative subset, including object-absence/false-positive negatives, time-varying camera conditions, and unknown labels -> ABSTAIN.
4. Offline full-test oracle is the *evaluation reference* (not deployable at scale); algorithm arms are random, stratified, margin/uncertainty, embedding, model-disagreement, and proposed ChangeScope. Evaluate same test query count and human annotation minutes.
5. Metrics: **area under cumulative confirmed regressions found vs budget**, per-tenant missed severe regressions, fraction of regression risk left UNTESTED, human minutes to first actionable signal, false release blocks. Cluster bootstrap by capture session/camera, predefined seed and preregistration.
6. Candidate target for RESEARCH GO **only**: nontrivial improvement over strongest baseline (e.g. >=20% fewer reviewed cases to first independently confirmed high-severity regression) **without worse than baseline worst-client miss risk**. This numeric bar is a *proposed* threshold, not justified by users/power simulation, and must be refined pre-reg.
7. Counterbenchmark: per-camera fine-tune / adapters vs one shared model + extra regression gates, including maintenance cost.

**Do not greenlight implementation from proxy grouping only.** Dataset licenses and media rights require independent checks. No images or model binaries should be uploaded publicly. Hardware feasibility and cost should precede any data transfer.

## 6. Concept comparison / narrow decision

| Candidate | Novelty risk vs existing systems | Customer evidence | 19-day contest feasibility | Research verdict |
|---|---|---|---|---|
| Original Blindspot Gate | **Very high overlap** with Roboflow Nov12 Workflow Evals + FiftyOne + AWS quality gates | None documenting incumbent failure | Can implement, but duplicative | **NO-GO standalone as described** |
| P1 TenantGuard generic slice risk release firewall | High overlap with FiftyOne scenarios + public high-risk-slice gating disclosure | Jan8 firsthand problem (not incumbent failure) | Medium | **RESEARCH HOLD** |
| **P1b ChangeScope** predictive cross-client impact and bounded audit | Strong adjacent literature, **full product parity untested**; measurable new hypothesis | Indirect G4 only | Medium-high; requires group-specific data | **Priority falsification only** |
| P2 Pipeline Twin controlled delta diagnosis | Old/new preprocessing integration tests and Roboflow workflow checks already known | Lacks directly verified same customer | Can make strong interactive demo | Alternative RESEARCH HOLD |
| P3 ProofPack oracle+evidence artifact | FiftyOne label QA + CI and existing review tooling already substantial | Unverified | Good as component | **Not standalone** |

No 1–5 arbitrary scores imply user adoption, patent novelty or winning odds. The next move is **test one specific hard-to-imitate hypothesis**, not publish a richer dashboard than incumbent products.

## 7. Practical zero-code next research and stop condition

1. **G4 same-user search:** resolve if the Jan8 Reddit author/another documented team actually tried FiftyOne/Roboflow/W&B/SageMaker/tenant-specific fine-tuning and *still failed*, without invented identities or unauthorized outreach. Identify scope: lack of annotated heldout images? model-change interference? too many customer retests? unclear rights? Go from quotes to identifiable workflow.
2. **Incumbent parity table:** evaluate official/working product features (Roboflow Evals, FiftyOne+script, AWS per-camera pipeline, Kolena release testing); note native, configuration, custom script, absent/unverified. No “competitor cannot” without running/tested limit.
3. **Design a toy *test plan*, not performance claim:** 3 tenants, old/new model pair, verified positive and negative test cases, hidden regressions, change delta. Build counterfactual scene storyboards for future demo if concept survives.
4. **Research pivot deadline:** by 2026-11-19 KST, if no same-user incumbent failure **and** no defensible measurable P1b advantage, move this idea to EVIDENCE HOLD/NO-GO and compare other specialist workflow ideas. Deadline is an internal research timebox, not a promised background task.

**Research ownership separation:** This file is written by ChatGPT GPT-6 in independent \`research/ideation-multiclient-20261116\`; do not touch Kiro development branch or any code. User will send Kiro implementation completion reports separately.

## Sources, visited 2026-11-16
1. Roboflow, Nov12 2026, original CV regression/deploy gate article: https://roboflow.com/blog/computer-vision-regression-testing
2. AWS, Oct26 2026, fleet-wide camera lifecycle with export quality gates: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
3. Jan8 2026 practitioner: https://www.reddit.com/r/computervision/comments/1q78rcn/avoiding_regressions_when_incorporating_data_from/
4. 2025 multi-model migration question: https://www.reddit.com/r/mlops/comments/1m8so03/
5. FiftyOne: https://docs.voxel51.com/user_guide/evaluation/detections.html
6. FiftyOne scenario panel: https://docs.voxel51.com/user_guide/app.html
7. FiftyOne community model compare: https://docs.voxel51.com/plugins/plugins_ecosystem/model_comparison.html
8. Kolena original methodology: https://medium.com/kolena-ml/best-practices-for-ml-model-testing-224366d3f23c
9. Google Cloud champion/challenger and slice validation: https://docs.cloud.google.com/architecture/guidelines-for-developing-high-quality-ml-solutions
10. Microsoft multitenant model tuning: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/ai-machine-learning
11. Patent-overlap lead (NOT legal opinion): https://eureka.patsnap.com/patent/CN122289904B
12. 2025 ACM TOSEM test-selection robustness: https://doi.org/10.1145/3715693
13. 2026 industrial CI risk/traceable test selection: https://www.mdpi.com/2079-9292/15/17/3854
14. 2023 industrial CV system-level pipeline verification: https://pmc.ncbi.nlm.nih.gov/articles/PMC10280203/
15. 2025 industrial release testing paper: https://www.sciencedirect.com/science/article/pii/S0950705125003399
16. AWS SageMaker shadow testing: https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html
17. FiftyOne annotation QA selection: https://docs.voxel51.com/getting_started/annotation/02_setup_splits.html

**No new real experiment conducted in this round.**
