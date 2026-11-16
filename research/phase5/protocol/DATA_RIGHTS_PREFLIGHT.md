# Phase 5 data and model rights preflight (R0, text only)

> STATUS: R0 DESK REVIEW. Nothing has been downloaded. Facts marked VERIFIED were read from the cited page on 2026-11-16 KST. UNVERIFIED items must be closed before task group B.
> Author: Kiro CLI 3.3.0, `claude-opus-5.5`, effort `max`. Not legal advice.

## Sources

| Item | Finding | Status | Source |
|---|---|---|---|
| COCO 2017 annotations | Owned by the COCO Consortium, licensed CC BY 4.0. Attribution required. | VERIFIED | https://cocodataset.org/dataset/termsofuse.htm |
| COCO 2017 images | COCO does not own image copyright. Use must follow the Flickr Terms of Use, and users take full responsibility for copies they make. | VERIFIED | same page |
| Per-image licenses | COCO annotation files carry a per-image license ID. Values and coverage not yet inspected. | UNVERIFIED (needs annotation file, group B) | annotation JSON `licenses` and `images[].license` |
| Sama-COCO license | FiftyOne zoo lists CC-BY-4.0. The Sama page says only "Creative Commons" without a version. | PARTLY VERIFIED | https://docs.voxel51.com/dataset_zoo/datasets/sama_coco.html, https://www.sama.com/sama-coco-dataset |
| Sama-COCO method | All images were revisited with COCO-2017 annotations pre-loaded. Associates followed a different rubric: crowds split into instances, objects under 10x10 px ignored or deleted. | VERIFIED | https://www.sama.com/sama-coco-dataset |
| RT-DETR R50vd (version A) | `PekingU/rtdetr_r50vd`, revision `df939e661d8c52e80608d1ec566561aabd25a4e7`, `model.safetensors` SHA-256 `5263d5521eff3e356f6cd8a371fd5dfb891725beda5f713674f79669115cdc64`, 172,175,856 bytes. Card tags: `license:apache-2.0`, `dataset:coco`. Last modified 2025-02-06. | VERIFIED (Hub API metadata) | https://huggingface.co/api/models/PekingU/rtdetr_r50vd?blobs=true |
| RT-DETRv2 R50vd (version B) | `PekingU/rtdetr_v2_r50vd`, revision `282494075698cab9faa1096ae26856890030c817`, `model.safetensors` SHA-256 `3331d977dbc0c7a6cdae9ec0b0b6ad156eb6720d65b7cf0fa710dcc541d88d71`, 172,176,856 bytes. Card tags: `license:apache-2.0`, `dataset:coco`. Last modified 2025-02-06. | VERIFIED (Hub API metadata) | https://huggingface.co/api/models/PekingU/rtdetr_v2_r50vd?blobs=true |
| Upstream code and weight license | The Hub card says Apache-2.0. The upstream RT-DETR repository license was not checked. | UNVERIFIED | upstream repo named on the model card |
| Training data of both checkpoints | Card tag says `coco`. Exact split (train2017 assumed) not confirmed. | UNVERIFIED | model cards, papers arXiv 2304.08069 and 2407.17140 |
| Preprocessing | v1 `preprocessor_config.json` is 841 bytes and v2's is 444 bytes. v2 Hub metadata names `AutoTokenizer` as processor, which needs checking. | UNVERIFIED | Hub API metadata above |

## Rules for this project

1. Keep raw images, annotation archives, weights and the FiftyOne database out of Git (`research/local-only/` or caches outside the repo). Before group B, add `*.safetensors`, image extensions and FiftyOne database paths to `.gitignore`, then check a staged `git status` before every push.
2. Public commits may contain image IDs, SHA-256 hashes, boxes, labels we created, and metrics. COCO-derived boxes need CC BY 4.0 attribution to the COCO Consortium.
3. Show an image in the public demo or video only if its per-image license allows redistribution with attribution (CC BY, CC BY-SA, public domain or US government work), with the Flickr author credited. Exclude non-commercial and no-derivatives images from public display by default. Whether a contest demo counts as non-commercial is an open legal question, not assumed.
4. Weights load from safetensors only, with `trust_remote_code` off and no pickle files.
5. Use no personal CCTV or face datasets.

## Local feasibility inventory (observed 2026-11-16, no downloads)

- Windows 11 Home build 26300; Intel Core i7-12700F, 12 cores / 20 threads; 31.8 GB RAM; C: 130 GB free; D: 1,010 GB free.
- GPU: NVIDIA GeForce RTX 2060 present (`nvidia-smi` found). The earlier CPU-only plan stays the default for determinism. GPU use needs user approval and replay checks.
- Python: only 3.14.0 is installed. torch and FiftyOne wheel support for 3.14 is unverified, so a separate 3.12 environment may be needed (installation needs user approval).
- Download size: two checkpoints total 344 MB (verified). COCO val2017 images and annotations are roughly 1.2 GB (estimate, unverified). Disk space is not a constraint.

## Approvals needed before group B

- The exact files to download (URLs and sizes) and the per-image license filter rule.
- Python environment creation and the package list.
- Whether GPU inference is allowed.
