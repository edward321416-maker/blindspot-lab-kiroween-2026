# Phase 5 oracle independence protocol (R0, text only)

> STATUS: DRAFT PROTOCOL. No annotation, sampling or review has happened. Author: Kiro CLI 3.3.0, `claude-opus-5.5`, effort `max`, 2026-11-16 KST. Addresses review findings R1 and R2.

## 1. What each label source can support

| Source | Independent of models A/B? | Independent of COCO? | May be used for |
|---|---|---|---|
| S1 COCO 2017 | Yes | n/a | Reference labels. A typical user's single ground truth. |
| S2 Sama-COCO | Yes | **No.** COCO labels were pre-loaded and edited under a different rubric | Correlated-version study and candidate-dispute finder only. Never counted as a second independent ground truth. S1/S2 differences are not label errors by themselves. |
| S3 blind from-scratch annotation (this protocol) | Yes | Yes | The only source for independently verified claims (G1). |
| Adjudication of alerts | No: the reviewer sees a candidate box | No | Decides whether a specific alert is a true regression. Conditioned on the alert, so no unconditional error rates. |

## 2. Roles

- Annotators R1 and R2: the two team members. They label independently and never see S1, S2, model outputs or each other's labels until both label sets are locked (hash committed).
- Adjudicator: whichever team member did not create the item's disagreement, or a third person if available. This is internal review, not third-party ground truth, and every report says so.
- Analyst: runs sampling and analysis scripts and doesn't annotate the items they select. In a two-person team this separation is partial, which is disclosed as a limitation.
- Time is logged per item for every role.

## 3. Sampling (preregistered before any model inference on these images)

1. Sampling frame: val2017 images that pass the rights filter in `DATA_RIGHTS_PREFLIGHT.md`, minus the 20 pilot images.
2. S3 blind sample: a seeded simple random sample of images. Size is set after the pilot from measured labeling minutes per image (target: 100 to 200 images within the reviewer-time budget). Seed, frame hash and image IDs are committed before labeling.
3. Alert audit: after A/B inference, all regression alerts on S3 images, plus a seeded random sample of non-alert ground-truth objects as controls (same count as alerts, at least 30). If inference beyond the audit sample is claimed, inverse-probability weights are reported.
4. Optional enrichment, labelled exploratory: alerts on objects where S1 and S2 differ, used to study the correlated-version signal, never pooled with step 2 estimates.

## 4. Blind annotation rules

- Guidelines: the COCO 80-class ontology with written rules for crowd, occlusion, truncation and minimum size (10x10 px, as in Sama, so tiny-object differences are not counted as disagreement). Fixed before labeling.
- The tool shows only the image and an empty canvas. Pre-labels are off. Image order is shuffled per annotator.
- Each annotator stores boxes, class and a confidence flag (CLEAR, UNSURE) per object, with timestamps, in a separate file.

## 5. From two blind label sets to S3 ground truth

- Objects matched across R1 and R2 (same class, IoU >= 0.5) become consensus S3 objects.
- Unmatched or class-conflicting objects go to adjudication. VALID adds the object, INVALID drops it, and AMBIGUOUS or UNRESOLVED becomes ABSTAIN. Abstentions are excluded from pass/fail and counted.
- Agreement is reported as object-level F1 and Cohen's kappa on adjudicated decisions, with counts.

## 6. Alert adjudication (separate step)

- Reviewers see the image crop and the ground-truth box, with source and model names hidden and alerts and controls shuffled together.
- Decision options: TRUE_REGRESSION, LABEL_PROBLEM (the label is wrong or missing), CANNOT_DECIDE.
- An alert counts as confirmed only if both reviewers independently choose TRUE_REGRESSION. Disagreements become CANNOT_DECIDE, not a pass.

## 7. Bias and limits that are always reported

Internal reviewers, partial analyst separation, small samples, val2017 familiarity for COCO-trained models, and the fact that S2 is correlated with S1.
