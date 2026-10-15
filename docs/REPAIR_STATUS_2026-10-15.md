# Repair status — 15 October 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This ledger distinguishes a tested code correction from a completed live rerun. Historical failures and unfavorable results remain intact.

The machine fingerprint remains Omni v6, digest `df6147466ef1804687a9f10b5a27caebff85e39899cca96d74c9897b0cd30a04`. The controller law was not changed to obtain a passing score.

| Case | Evidence | Status |
|---|---|---|
| Azure quota | Full-control repetition 1 completed; later repetitions were refused quota. | Aggregate family/regional checks, confirmed deletion and shared queue implemented. New run 38756403953 uses Standard_D2_v4 at verified public price $0.096/worker-hour; awaiting completion. |
| Robustness restart | Artifact 11971975388 from run 38729569415 contains `CAP_ARGS: unbound variable`. | Fixed exported restart environment. A subprocess regression reproduced the original failure and passes after the correction. The decision-coverage threshold remains unchanged. |
| Release verification | Checks 38749379506 and 38751024376 reported a stale document digest. | Hash now comes from the actual repository version of `docs/OMNI_V6.md`; no functional test was disabled. |
| Repair dispatcher | Run 38758243197 rejected the undeclared robustness input `arms`. | Removed the extra input; both arms are already fixed in the workflow. All requested free checks now validate against actual workflow inputs before any dispatch. API errors retain their cause. |
| Every artifact | Earlier workflows supplied a separate legal artifact. | Each of 79 result uploads now embeds README.md, LICENSE, NOTICE, DISCLOSURES.md, PATENTS.md, TRADEMARKS.md and hashes without moving measured files. |
| Capacity | Run 38722001872 contains quota-refused CPU resizes and a later runner shutdown. | OPEN. Requires quota-aware actuator work with a new fingerprint and a valid rerun. Raising the test quota or relabelling this case is not a correction. |
| Redis burst | Run 38725712960 ended while the workload step still showed in progress, without final logs. | Cause unconfirmed. Rerun resource-objective burst with retained run.log; keep the failed case visible. |

Machine-readable record: `results/repair_20261015/STATUS.json`. Output packaging is implemented by `tools/artifact_legal.py` and `tools/wire_artifact_legal.py`. The frozen engine, workloads, validity checks and excluded Google/Amazon/GPU launches are preserved.

The bounded repair request reruns only the free robustness-kill and Redis-burst cases. It does not launch another paid Azure or GPU test. Every generated artifact receives the legal bundle, including partial artifacts where a job fails. A runner destroyed before cleanup can still leave no artifact; that infrastructure failure cannot be honestly converted into a success.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
