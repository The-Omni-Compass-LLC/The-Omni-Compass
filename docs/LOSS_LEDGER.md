# The LOSS ledger: every row that reads LOSS in all three runs, in every benchmark's newest table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Every row of every three-run table stands where its table stands, LOSS included; this page gathers the LOSS rows so none of them is found only by reading every table. A LOSS row is a gauge that moved away from its declared aim in all three of the benchmark's runs, A, B and C, every run's 95% interval clear of zero (`tools/readings.py`). Each benchmark is read from its newest whole table; an older engine's table stands only until the engine that stands has run that benchmark three times, and the engine each row ran on is printed beside it.

Rows that read LOSS in all three runs: **110**. Against my own native, the readings do no harm is judged by: **7**. In place of a controller: **14**. Without me, or two changes at once: **89**. By engine: omni-v12: 110.

## Against my own native

Omni-Compass on top of a native controller, against that native alone: the readings do no harm is judged by (`DISCLOSURES.md`, section 3). Each row's cause stands beside it where it is written; a row with none says so.

| Engine | Benchmark | Gauge | Each run's size | Cause | Fixed in | What decides it |
|---|---|---|---|---|---|---|
| omni-v12 | `results/live/V12_ARMADA_4W_BARE.json` | queue: job turnaround, submitted to done, mean (s) | 5.1%, 8.9%, 9.1% | suspected: the conveyance fault fixed in omni-v13 (its shape fits: a batch gauge a few percent slower on a shared host); not yet shown on this rig (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`) | omni-v13, if the suspicion holds | the benchmark's three runs on the engine that stands |
| omni-v12 | `results/live/V12_BINPACK.json` | queue: job turnaround, submitted to done, mean (s) | 1.4%, 1.0%, 1.2% | suspected: the conveyance fault fixed in omni-v13; the omni-v13 toy gate's batch toy, set from the KubeRay runs' own files, read the job turnaround back at native's (`docs/OMNI_V13.md`) | omni-v13, if the suspicion holds | the benchmark's three runs on the engine that stands |
| omni-v12 | `results/live/V12_CRANE_4W_TOP.json` | pod start wait, total (s) | 80.9%, 104.5%, 54.4% | not yet written | — | the benchmark's three runs on the engine that stands |
| omni-v12 | `results/live/V12_KUBERAY_4W_BARE.json` | response time (ms), 99th percentile | 9.8%, 4.4%, 13.0% | on a shared host at its top, beside another workload's room, a CPU limit I raised was kept through a saturated batch queue, so the batch pods ran slower while the web served no faster (`docs/OMNI_V13.md`) | omni-v13 | the benchmark's three runs on the engine that stands |
| omni-v12 | `results/live/V12_KUBERAY_4W_BARE.json` | batch: queue finished (s) | 0.8%, 0.7%, 0.6% | on a shared host at its top, beside another workload's room, a CPU limit I raised was kept through a saturated batch queue, so the batch pods ran slower while the web served no faster (`docs/OMNI_V13.md`) | omni-v13 | the benchmark's three runs on the engine that stands |
| omni-v12 | `results/live/V12_OCM_4W_TOP.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7%, 6.1%, 45.5% | under investigation: the third run's size is far from the first two (`docs/LOSS_ROWS_UNDER_INVESTIGATION.md`) | — | the benchmark's three runs on the engine that stands, read repetition by repetition |
| omni-v12 | `results/live/V12_VANILLA.json` | queue: job turnaround, submitted to done, mean (s) | 0.9%, 0.9%, 1.2% | suspected: the conveyance fault fixed in omni-v13; the omni-v13 toy gate's batch toy read the job turnaround back at native's (`docs/OMNI_V13.md`) | omni-v13, if the suspicion holds | the benchmark's three runs on the engine that stands |

## In place of a controller

Omni-Compass on the organism alone against an orchestrator as shipped (the four ways' VS): Omni-Compass doing an orchestrator's work without it. Shown; a different question from do no harm, which is judged against the native a governor sits on.

| Engine | Benchmark | Gauge | Each run's size |
|---|---|---|---|
| omni-v12 | `results/live/V12_ARMADA_4W_VS.json` | response time (ms), mean | 365.9%, 387.2%, 271.6% |
| omni-v12 | `results/live/V12_ARMADA_4W_VS.json` | response time (ms), 95th percentile | 171.6 to 2510, 186.5 to 2871, 986.8% |
| omni-v12 | `results/live/V12_ARMADA_4W_VS.json` | response time (ms), 99th percentile | 197.3 to 3535, 207.1 to 4014, 162.2 to 2162 |
| omni-v12 | `results/live/V12_ARMADA_4W_VS.json` | time over the response line (% of samples) | 0.004241 to 24.76, 0 to 27.76, 0 to 13.96 |
| omni-v12 | `results/live/V12_ARMADA_4W_VS.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 to 12.33, 0 to 14, 0 to 8.2 |
| omni-v12 | `results/live/V12_BINPACK_4W_VS.json` | time over the response line (% of samples) | 21.1%, 37.2%, 29.8% |
| omni-v12 | `results/live/V12_CRANE_4W_VS.json` | pod start wait, total (s) | 60.3%, 56.1%, 51.9% |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_VS.json` | response time (ms), 95th percentile | 191.2%, 485.5%, 285.6% |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_VS.json` | response time (ms), 99th percentile | 181.3%, 481.6%, 285.0% |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_VS.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 to 4.9, 0.1 to 9, 0.1 to 9.6 |
| omni-v12 | `results/live/V12_OCM_4W_VS.json` | pod start wait, total (s) | 466.7%, 0 to 2.4, 0 to 1.3 |
| omni-v12 | `results/live/V12_OCM_4W_VS.json` | pod start wait, mean (s) | 266.7%, 0 to 1.25, 0 to 0.8 |
| omni-v12 | `results/live/V12_VOLCANO_4W_VS.json` | response time (ms), 95th percentile | 92.6%, 31.9%, 50.9% |
| omni-v12 | `results/live/V12_VOLCANO_4W_VS.json` | time over the response line (% of samples) | 124.1%, 50.2%, 54.8% |

## Without me, or two changes at once

The orchestrator as shipped against the organism alone (ORCH: neither arm carries Omni-Compass), and Omni-Compass on top of the orchestrator against the organism alone (BOTH: the orchestrator and Omni-Compass together, two changes at once). Shown because every row is shown.

| Engine | Benchmark | Gauge | Each run's size |
|---|---|---|---|
| omni-v12 | `results/live/V12_ARMADA_4W_BOTH.json` | batch: queue finished (s) | 72.4%, 68.6%, 86.7% |
| omni-v12 | `results/live/V12_ARMADA_4W_BOTH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.09722 to 1158, 0.07083 to 1158, 0.0875 to 1159 |
| omni-v12 | `results/live/V12_ARMADA_4W_BOTH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 to 1474, 0.6 to 1474, 0.6 to 1475 |
| omni-v12 | `results/live/V12_ARMADA_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 528.0%, 469.9%, 904.9% |
| omni-v12 | `results/live/V12_ARMADA_4W_BOTH.json` | queue: jobs unfinished at the window's end | 0 to 24, 0 to 24, 0 to 24 |
| omni-v12 | `results/live/V12_ARMADA_4W_ORCH.json` | batch: queue finished (s) | 72.6%, 68.4%, 86.7% |
| omni-v12 | `results/live/V12_ARMADA_4W_ORCH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.09722 to 1160, 0.07083 to 1157, 0.0875 to 1158 |
| omni-v12 | `results/live/V12_ARMADA_4W_ORCH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6667 to 1476, 0.6 to 1473, 0.6 to 1475 |
| omni-v12 | `results/live/V12_ARMADA_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 529.1%, 469.3%, 904.5% |
| omni-v12 | `results/live/V12_ARMADA_4W_ORCH.json` | queue: jobs unfinished at the window's end | 0 to 24, 0 to 24, 0 to 24 |
| omni-v12 | `results/live/V12_CRANE_4W_BOTH.json` | pod start wait, total (s) | 80.9%, 68.8%, 71.8% |
| omni-v12 | `results/live/V12_CRANE_4W_ORCH.json` | response time (ms), mean | 2.6%, 3.2%, 2.9% |
| omni-v12 | `results/live/V12_KAI_4W_BOTH.json` | response time (ms), 95th percentile | 41.9%, 45.9%, 57.5% |
| omni-v12 | `results/live/V12_KAI_4W_BOTH.json` | response time (ms), 99th percentile | 45.2%, 48.9%, 62.1% |
| omni-v12 | `results/live/V12_KAI_4W_BOTH.json` | batch: queue finished (s) | 5.1%, 6.9%, 5.1% |
| omni-v12 | `results/live/V12_KAI_4W_BOTH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.05417 to 1.004, 0.0625 to 1.079, 915.8% |
| omni-v12 | `results/live/V12_KAI_4W_BOTH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 550.0%, 650.0%, 128.6% |
| omni-v12 | `results/live/V12_KAI_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 48.0%, 51.3%, 52.5% |
| omni-v12 | `results/live/V12_KAI_4W_ORCH.json` | response time (ms), mean | 13.2%, 15.8%, 18.3% |
| omni-v12 | `results/live/V12_KAI_4W_ORCH.json` | response time (ms), 95th percentile | 38.1%, 41.1%, 50.8% |
| omni-v12 | `results/live/V12_KAI_4W_ORCH.json` | response time (ms), 99th percentile | 39.9%, 44.0%, 61.3% |
| omni-v12 | `results/live/V12_KAI_4W_ORCH.json` | batch: queue finished (s) | 4.2%, 5.7%, 4.6% |
| omni-v12 | `results/live/V12_KAI_4W_ORCH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.05417 to 0.8458, 0.0625 to 1.071, 968.4% |
| omni-v12 | `results/live/V12_KAI_4W_ORCH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 300.0%, 550.0%, 100.0% |
| omni-v12 | `results/live/V12_KAI_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 40.1%, 42.1%, 45.2% |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | response time (ms), mean | 45.7%, 33.1%, 25.0% |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | response time (ms), 95th percentile | 81.3%, 62.1%, 38.8% |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | response time (ms), 99th percentile | 73.4%, 64.1%, 36.5% |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | time over the response line (% of samples) | 17.9%, 12.6%, 22.4% |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 45.1%, 34.5%, 30.8% |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | batch: queue finished (s) | 16.5%, 15.7%, 14.3% |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 180.0%, 183.3%, 0.5 to 122.3 |
| omni-v12 | `results/live/V12_KARMADA_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 83.0%, 78.2%, 57.9% |
| omni-v12 | `results/live/V12_KARMADA_4W_ORCH.json` | response time (ms), mean | 27.9%, 20.4%, 21.6% |
| omni-v12 | `results/live/V12_KARMADA_4W_ORCH.json` | response time (ms), 95th percentile | 51.1%, 38.9%, 35.4% |
| omni-v12 | `results/live/V12_KARMADA_4W_ORCH.json` | response time (ms), 99th percentile | 54.9%, 47.7%, 31.3% |
| omni-v12 | `results/live/V12_KARMADA_4W_ORCH.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 34.3%, 22.1%, 31.7% |
| omni-v12 | `results/live/V12_KARMADA_4W_ORCH.json` | batch: queue finished (s) | 11.7%, 11.2%, 11.0% |
| omni-v12 | `results/live/V12_KARMADA_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 58.2%, 56.1%, 44.2% |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_BOTH.json` | batch: queue finished (s) | 79.6%, 82.5%, 90.2% |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_BOTH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.03333 to 110.9, 0.025 to 175.4, 0.0625 to 142.5 |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_BOTH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 to 518.5, 0.1 to 763.9, 0.5 to 684.4 |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 38.07 to 650.2, 849.4%, 55.45 to 789 |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_ORCH.json` | batch: queue finished (s) | 76.5%, 82.5%, 86.9% |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_ORCH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.03333 to 103.6, 0.025 to 171.5, 0.0625 to 146.3 |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_ORCH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 to 513.9, 0.1 to 798, 0.5 to 698.5 |
| omni-v12 | `results/live/V12_KOORDINATOR_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 38.07 to 614, 831.8%, 55.45 to 763.3 |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | response time (ms), mean | 85.7%, 85.1%, 67.0% |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | time over the response line (% of samples) | 212.8%, 223.2%, 207.9% |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 202.8%, 216.4%, 157.0% |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | batch: queue finished (s) | 89.3%, 80.1%, 80.8% |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.03241 to 637.5, 0.04167 to 536.6, 0.05417 to 677.6 |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 to 1113, 0.4 to 924.3, 0.4 to 1141 |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 81.79 to 955, 910.0%, 774.9% |
| omni-v12 | `results/live/V12_KUBERAY_4W_BOTH.json` | queue: jobs unfinished at the window's end | 0 to 13.44, 0 to 11.3, 0 to 14.5 |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | response time (ms), mean | 87.9%, 86.6%, 70.6% |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | time over the response line (% of samples) | 221.2%, 234.2%, 217.5% |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 204.2%, 219.2%, 159.1% |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | batch: queue finished (s) | 90.4%, 80.6%, 81.4% |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.03241 to 635, 0.04167 to 533.6, 0.05417 to 670.7 |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 to 1129, 0.4 to 914.7, 0.4 to 1145 |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 81.79 to 954.8, 927.0%, 779.3% |
| omni-v12 | `results/live/V12_KUBERAY_4W_ORCH.json` | queue: jobs unfinished at the window's end | 0 to 14.33, 0 to 11.1, 0 to 14.6 |
| omni-v12 | `results/live/V12_KUEUE_4W_BOTH.json` | response time (ms), 95th percentile | 9.5%, 13.4%, 15.4% |
| omni-v12 | `results/live/V12_KUEUE_4W_BOTH.json` | batch: queue finished (s) | 1.0%, 1.6%, 1.9% |
| omni-v12 | `results/live/V12_KUEUE_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 12.5%, 13.8%, 16.6% |
| omni-v12 | `results/live/V12_KUEUE_4W_ORCH.json` | response time (ms), mean | 7.3%, 6.4%, 8.9% |
| omni-v12 | `results/live/V12_KUEUE_4W_ORCH.json` | response time (ms), 95th percentile | 12.8%, 10.0%, 10.2% |
| omni-v12 | `results/live/V12_KUEUE_4W_ORCH.json` | queue: job wait, submitted to its first pod running, mean (s) | 178.6%, 118.2%, 537.5% |
| omni-v12 | `results/live/V12_KUEUE_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 11.5%, 9.3%, 12.7% |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | response time (ms), mean | 59.9%, 51.7%, 58.7% |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | response time (ms), 95th percentile | 51.5%, 55.2%, 55.0% |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | response time (ms), 99th percentile | 49.4%, 58.4%, 52.9% |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | time over the response line (% of samples) | 55.9%, 23.9%, 75.5% |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8%, 26.6%, 74.3% |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | batch: queue finished (s) | 21.4%, 19.4%, 19.1% |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.1542 to 22.47, 0.1167 to 18.62, 0.075 to 13.05 |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 to 159.5, 0.8 to 105.6, 0.5 to 85.4 |
| omni-v12 | `results/live/V12_OCM_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 70.9%, 67.7%, 76.8% |
| omni-v12 | `results/live/V12_OCM_4W_ORCH.json` | batch: queue finished (s) | 15.0%, 15.9%, 16.1% |
| omni-v12 | `results/live/V12_OCM_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 47.9%, 57.0%, 46.0% |
| omni-v12 | `results/live/V12_VOLCANO_4W_BOTH.json` | batch: queue finished (s) | 1.8%, 1.7%, 1.8% |
| omni-v12 | `results/live/V12_VOLCANO_4W_BOTH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.0625 to 0.7667, 0.075 to 0.8917, 0.05 to 0.7583 |
| omni-v12 | `results/live/V12_VOLCANO_4W_BOTH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 333.3%, 450.0%, 550.0% |
| omni-v12 | `results/live/V12_VOLCANO_4W_BOTH.json` | queue: job turnaround, submitted to done, mean (s) | 32.1%, 19.7%, 26.0% |
| omni-v12 | `results/live/V12_VOLCANO_4W_ORCH.json` | batch: queue finished (s) | 1.2%, 1.4%, 1.4% |
| omni-v12 | `results/live/V12_VOLCANO_4W_ORCH.json` | queue: job wait, submitted to its first pod running, mean (s) | 0.0625 to 0.7208, 866.7%, 0.05 to 0.7958 |
| omni-v12 | `results/live/V12_VOLCANO_4W_ORCH.json` | queue: job wait, submitted to its first pod running, 95th percentile (s) | 366.7%, 275.0%, 500.0% |
| omni-v12 | `results/live/V12_VOLCANO_4W_ORCH.json` | queue: job turnaround, submitted to done, mean (s) | 24.2%, 17.6%, 23.2% |

Each run's size is the change against the comparison's first arm, in percent of it, run by run; the direction is the gauge's, away from its aim in every run. The tables hold every number, its interval and its arms.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
