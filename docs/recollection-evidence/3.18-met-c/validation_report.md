# Met C validation report

## Scope and provenance

Execution followed fixed plan commit `ddfa8ad36ff61128a684dc125d5105721ad246e7`. The collector baseline was commit `93c4f7a9765af8c4fcd5a4c74f1ee7c98e9b2bd8`. Only Met object IDs `437127` and `436535` were collected from the canonical HTTPS Collection API endpoint.

The local evidence store retained separate `response.bin`, `capture.json`, and `COMMITTED` files for both objects. Each stored response was reopened, hashed, strictly parsed, and matched to its exact integer object ID. Raw evidence and headers are intentionally absent from this public packet.

## Measured gates

| Gate | Result |
|---|---:|
| Baseline tests | 37/37 PASS |
| Integrity suite after I01–I12 | 49/49 PASS |
| Rights/output safety R01–R08 | 8/8 PASS |
| Combined isolated execution | 57/57 PASS |
| Raw captures | 2/2 |
| SHA-256 verified | 2/2 |
| Object ID verified | 2/2 |
| Images downloaded | 0 |

## Raw-response measurements

| Object ID | Bytes | SHA-256 |
|---:|---:|---|
| 437127 | 2386 | `a0db88a8cc7548e63036c030a7ace1e2c65df040148d07da5c0610e7a827185b` |
| 436535 | 2793 | `497e0d1cd9166d27f6ef9b5e551b0cd8bafbcf1a5e134f364ba406b3a1f57d62` |

## Rights review

Rights signals were kept separate from actual-use approval. For `437127`, the captured API reported `isPublicDomain=false` and no primary image; the current item page also did not expose a download action. For `436535`, the API reported `isPublicDomain=true`, a primary image URL was present, and the item page displayed Public Domain and Download Image wording. These source observations do not by themselves approve product display.

The six independent slot decisions are:

- Two `METADATA` slots: `METADATA_ONLY_ALLOWED` after source review.
- Two `AUTHORED_TEXT` slots: `RIGHTS_REVIEW_HOLD` pending explicit approval.
- Two `IMAGE` slots: `RIGHTS_REVIEW_HOLD`; no image was downloaded or approved for display.

The current API and item-page signals were internally consistent for each object at review time. The workflow still fails closed because provenance, policy signal, and actual-use approval are separate gates. This report is not legal advice.

## Remaining holds

- Independent product/legal review is still required before any image or authored description is used.
- The `436535` Open Access indicators do not substitute for application release approval.
- `437127` has no approved image source in this run.
- Private raw evidence must be reviewed locally if byte-level independent verification is required.

Status: **DONE_WITH_CONCERNS** — collection and tests passed, while four rights slots remain on hold.
