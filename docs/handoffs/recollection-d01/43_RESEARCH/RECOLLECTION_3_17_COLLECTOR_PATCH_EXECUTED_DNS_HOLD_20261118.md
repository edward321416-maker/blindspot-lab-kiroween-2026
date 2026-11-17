# Re:Collection 3.17 — collector patch executed, external raw source acquisition blocked

**Date:** 2026-11-18 KST (UTC execution observed 2026-11-17 19:07).  
**Actual status:** **PATCHED_COLLECTOR_TEST_PASS / OFFICIAL_RAW_CAPTURE 0 OF 8 / DNS_HOLD**.

This is an *actual isolated execution report*, not another proposal. It changes **no** local Windows Kiro product code or baseline B0–B5.2 contracts. It is a research utility in an independent container.

## Executed evidence

- Opened the original 3.16 ZIP and inspected actual `tools/capture_raw_http.py` & 11 unit tests; original 11/11 PASS.
- Fixed a real bug: `if 'objectID' in data ...` accidentally accepted a Met JSON payload with missing `objectID`. The new parser requires an exact integer object ID; also rejects null, boolean, string, nested duplicate JSON keys and nonstandard NaN.
- Added HTTPS redirect chain tracking and final object URL check, source ID path safety, source UTC normalization, HTML `RAW_HTML_IDENTITY_PENDING` status, exclusive-write immutable snapshot and a final readback-verified `COMMITTED` marker, with read-only `verify_captures.py`.
- New tests **21/21**, complete tests **32/32 twice**, a unified patch applied to a fresh copy without conflicts and reproduced exact bytes of four patched/new code files, fresh patch replay tests **32/32**.
- Actual command `python tools/capture_raw_http.py --root . --pack A` attempted the **first** item `MET-36491`: **exit 2**, `URLError [Errno -3] Temporary failure in name resolution`. Stdout empty, no `private/raw` files. `curl` and a separate container download also failed. The seven other targets remained `NOT_ATTEMPTED_GATE`.
- Research audit returns **8 registered, 0 committed original capture**. Original full HTTP response, headers and response SHA256 still absent for all eight. The Web-rendered official JSON records are historical index results (3–7 month crawl dates), **not** raw source bytes and **not** evidence of actual server reachability now.

## Verification artifacts

- Complete private execution kit (code, unified diff, clean replay, logs, status JSON, 4-page PDF): [Drive ZIP](https://drive.google.com/file/d/1UuTsnD3PTVBleMQ5MrXDAzKTZiFZtsQY/view); original ZIP SHA256 `6e0d515dff7fbb4cc2d82919e09ec58674562143c4911925e05043182dd51a38`, 158798 bytes, 19 internal files + manifest. Uploaded byte size verified.
- [Korean 4-page execution report PDF](https://drive.google.com/file/d/1TxG6PQShtW7bAqxkguv1ap6GOplW8mlQ/view). Local canonical PDF SHA `7264c93ab08ca9794929af78427aa7c481b037600863aafc1223ef288e7e0f00`. **Drive preview PDF bytes differ** (remote 150265 vs local 125292), though fetched full text verified 4 pages and 32/32 and 0/8/DNS. **Canonical SHA applies to local file inside ZIP**, not that rendered Drive copy.
- `ReCollection_3_17_Collector_Hardening.patch` SHA256 `1d2e4c9265f9b8eeff3db2c0b3119a7e2419f805345d78a59987f36bae28769d`. Patch covers modifications + all new runnable code files, verified via `git apply --check` and `git apply` on isolated clean 3.16 source copy.
- Separate archival folder: https://drive.google.com/drive/folders/15Ptd_yc9Lbg4sJJX6bFTeaZ1h7X7otb1

## How to finish actual raw acquisition on a network-permitted Windows computer

Extract the ZIP into a NEW folder **outside** `C:\Users\admin\Projects\recollection-kiroween-2026`. From that folder:

```powershell
py -3 -m unittest discover -s tests -p 'test_*.py' -v
py -3 tools/capture_raw_http.py --root . --pack A
py -3 tools/verify_captures.py --root .
```

Stop on DNS/403/429/identity failures; no proxy bypass, credential leakage, unauthorized media or paid access. A gate passes only when both `MET-36491` and `MET-45434` have actual committed response.bin+capture.json+COMMITTED with matching original-byte SHA256 and exact object identity. Thereafter stage C; B/D require extra HTML identity and third-party media license review. **Separate, newly observed Kiro report (AI_Execution_Log row 1110):** B5.2 typed visitor-output adapter user/Kiro-reported LOCAL_PASS at `c02ac7caee1eb163d5ed24b108605c6bb89f5cb0`, Node 239/239 twice, original code not independently audited here. Row 1111 reports D2-V0 local viewer development separately authorized, but not yet evidenced as implemented. **Neither changes this research lab's RAW 0/8, rights/human oracle HOLD nor authorizes release.**

**Do not call this RAW source collection successful. Do not merge these utility patches into the frozen Kiro engine.**
