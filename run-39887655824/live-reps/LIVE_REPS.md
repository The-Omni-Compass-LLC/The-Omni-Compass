# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.401 | 5.246 |
| node-hours | 2.518 | 2.515 | 2.264 | 2.2 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | 272 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.6 | 253.1 | 248.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 301.1 | 214.2 | 289.2 | 194.5 |
| response time (ms), 95th percentile | 964.7 | 510 | 1117 | 608.6 |
| response time (ms), 99th percentile | 1450 | 816.1 | 1644 | 1122 |
| time over the response line (% of samples) | 16.54 | 7.459 | 17.37 | 7.913 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.3 | 8.6 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 136.6 | 102.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.383 | 14.78 | 10.28 | 14.87 |
| utilisation (used / allocatable) | 0.05761 | 0.05771 | 0.06489 | 0.06729 |
| CPU used (cores), mean | 1.383 | 1.385 | 1.403 | 1.406 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04983 | 0.0523 |
| CPU used with Omni's own (cores), mean | 1.383 | 1.385 | 1.453 | 1.458 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 478.6 | 434.1 | 423.6 |
| HPA replicas, mean | 1.995 | 1.995 | 2.641 | 2.509 |
| pods started | 0.1 | 0 | 1.4 | 0.2 |
| pod start wait, total (s) | 0.2 | 0 | 2.7 | 0.4 |
| pod start wait, mean (s) | 0.2 | 0 | 1.35 | 0.2 |
| host CPU busy, the real machine under kind (%) | 39.51 | 40.57 | 42.01 | 43.03 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 759.5 | 771.1 | 768.9 | 779.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.843 | 4.56 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.6708 | 0.05833 | 0.6625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.1 | 0.4 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 67.88 | 83.26 | 76.69 | 90.93 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.246 | -12.6% | -1.433 to -0.07404 | yes: GAIN |
| node-hours | 2.515 | 2.2 | -12.5% | -0.6023 to -0.02669 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272.1 | +0.2% | -0.4595 to +1.415 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 248.4 | -8.5% | -44.95 to -1.419 | yes: GAIN |
| response time (ms), mean | 214.2 | 194.5 | -9.2% | -42.12 to +2.65 | no |
| response time (ms), 95th percentile | 510 | 608.6 | +19.3% | -46 to +243.2 | no |
| response time (ms), 99th percentile | 816.1 | 1122 | +37.5% | -62.79 to +674.4 | no |
| time over the response line (% of samples) | 7.459 | 7.913 | +6.1% | -1.662 to +2.571 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.8 | +6.8% | -0.631 to +1.631 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.2 | +102 (native is 0) | +55.86 to +148.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.78 | 14.87 | +0.6% | -1.799 to +1.976 | no |
| utilisation (used / allocatable) | 0.05771 | 0.06729 | +16.6% | +0.0021 to +0.01707 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.385 | 1.406 | +1.5% | -0.01119 to +0.05276 | no |
| Omni's own CPU (cores), mean | 0 | 0.0523 | +0.0523 (native is 0) | +0.0461 to +0.0585 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.385 | 1.458 | +5.3% | +0.0394 to +0.1068 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.6 | 423.6 | -11.5% | -98.47 to -11.54 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.509 | +25.7% | +0.1447 to +0.8821 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.57 | 43.03 | +6.1% | +2.006 to +2.929 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.1 | 779.9 | +1.1% | +3.241 to +14.36 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.56 | -24.0% | -2.726 to -0.1533 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6708 | 0.6625 | -1.2% | -0.08241 to +0.06575 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.3 | +18.2% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.26 | 90.93 | +9.2% | +1.094 to +14.26 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.487e-15 to -2.892e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.515 | -0.1% | -0.01006 to +0.003065 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | -0.1% | -1.211 to +0.5267 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.6 | -0.1% | -1.211 to +0.5267 | no |
| response time (ms), mean | 301.1 | 214.2 | -28.8% | -132.6 to -41.11 | yes: GAIN |
| response time (ms), 95th percentile | 964.7 | 510 | -47.1% | -697.2 to -212.1 | yes: GAIN |
| response time (ms), 99th percentile | 1450 | 816.1 | -43.7% | -980 to -287.5 | yes: GAIN |
| time over the response line (% of samples) | 16.54 | 7.459 | -54.9% | -14.72 to -3.45 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.3 | -8.8% | -1.595 to +0.1953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.383 | 14.78 | +57.5% | +4.512 to +6.282 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05761 | 0.05771 | +0.2% | -0.000776 to +0.0009755 | no |
| CPU used (cores), mean | 1.383 | 1.385 | +0.2% | -0.01862 to +0.02341 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.383 | 1.385 | +0.2% | -0.01862 to +0.02341 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 478.6 | -0.2% | -7.175 to +5.337 | no |
| HPA replicas, mean | 1.995 | 1.995 | +0.0% | -0.1546 to +0.1562 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 39.51 | 40.57 | +2.7% | +0.81 to +1.295 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.5 | 771.1 | +1.5% | +5.408 to +17.79 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.6708 | +1050.0% | +0.5512 to +0.6738 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.1 | +120.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.88 | 83.26 | +22.6% | +6.711 to +24.04 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.401 | -10.0% | -1.163 to -0.03581 | yes: GAIN |
| node-hours | 2.518 | 2.264 | -10.1% | -0.4908 to -0.01807 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 | +0.0% | -0.9748 to +1.09 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 253.1 | -6.9% | -36.55 to -1.024 | yes: GAIN |
| response time (ms), mean | 301.1 | 289.2 | -3.9% | -26.83 to +3.073 | no |
| response time (ms), 95th percentile | 964.7 | 1117 | +15.8% | +37.51 to +267 | yes: LOSS |
| response time (ms), 99th percentile | 1450 | 1644 | +13.4% | +44.15 to +344.8 | yes: LOSS |
| time over the response line (% of samples) | 16.54 | 17.37 | +5.0% | +0.1208 to +1.529 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.6 | +7.5% | -0.09105 to +1.291 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.6 | +137 (native is 0) | +78.03 to +195.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.383 | 10.28 | +9.5% | -1.049 to +2.833 | no |
| utilisation (used / allocatable) | 0.05761 | 0.06489 | +12.6% | +0.001411 to +0.01315 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 1.403 | +1.5% | -0.0002031 to +0.04114 | no |
| Omni's own CPU (cores), mean | 0 | 0.04983 | +0.0498 (native is 0) | +0.04484 to +0.05482 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.383 | 1.453 | +5.1% | +0.04794 to +0.09266 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 434.1 | -9.5% | -83.81 to -6.928 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.641 | +32.4% | +0.285 to +1.008 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.3433 to +2.257 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.7 | +1250.0% | +0.615 to +4.385 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.35 | +575.0% | +0.1662 to +2.134 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.51 | 42.01 | +6.3% | +2.033 to +2.963 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.5 | 768.9 | +1.2% | +2.398 to +16.4 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.843 | -19.3% | -2.235 to -0.07933 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.05833 | +0.0% | -0.04215 to +0.04215 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.88 | 76.69 | +13.0% | +2.458 to +15.15 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.401 | -10.0% | -1.163 to -0.03581 | yes: GAIN |
| node-hours | 2.515 | 2.264 | -10.0% | -0.4904 to -0.01145 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 272 | +0.1% | -0.4594 to +1.259 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 253.1 | -6.8% | -36.59 to -0.2989 | yes: GAIN |
| response time (ms), mean | 214.2 | 289.2 | +35.0% | +17.79 to +132.2 | yes: LOSS |
| response time (ms), 95th percentile | 510 | 1117 | +119.0% | +268.8 to +945 | yes: LOSS |
| response time (ms), 99th percentile | 816.1 | 1644 | +101.5% | +345.9 to +1311 | yes: LOSS |
| time over the response line (% of samples) | 7.459 | 17.37 | +132.9% | +3.996 to +15.83 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 8.6 | +17.8% | +0.1295 to +2.471 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.6 | +137 (native is 0) | +78.03 to +195.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.78 | 10.28 | -30.5% | -6.154 to -2.856 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05771 | 0.06489 | +12.4% | +0.001375 to +0.01299 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.385 | 1.403 | +1.3% | -0.003726 to +0.03988 | no |
| Omni's own CPU (cores), mean | 0 | 0.04983 | +0.0498 (native is 0) | +0.04484 to +0.05482 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.385 | 1.453 | +4.9% | +0.04415 to +0.09167 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.6 | 434.1 | -9.3% | -82.23 to -6.67 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.641 | +32.3% | +0.2707 to +1.02 | yes: power given |
| pods started | 0 | 1.4 | +1.4 (native is 0) | +0.5604 to +2.24 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.7 (native is 0) | +1.046 to +4.354 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.35 | +1.35 (native is 0) | +0.6745 to +2.025 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.57 | 42.01 | +3.6% | +0.9722 to +1.919 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.1 | 768.9 | -0.3% | -5.982 to +1.582 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.843 | -19.3% | -2.235 to -0.07933 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6708 | 0.05833 | -91.3% | -0.6957 to -0.5293 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.4 | -63.6% | -1.046 to -0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 83.26 | 76.69 | -7.9% | -11.97 to -1.176 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.246 | -12.6% | -1.433 to -0.07404 | yes: GAIN |
| node-hours | 2.518 | 2.2 | -12.6% | -0.6042 to -0.03179 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.1 | +0.0% | -0.9543 to +1.226 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 248.4 | -8.7% | -45.14 to -1.914 | yes: GAIN |
| response time (ms), mean | 301.1 | 194.5 | -35.4% | -146.2 to -66.98 | yes: GAIN |
| response time (ms), 95th percentile | 964.7 | 608.6 | -36.9% | -543.1 to -169 | yes: GAIN |
| response time (ms), 99th percentile | 1450 | 1122 | -22.6% | -573.6 to -82.34 | yes: GAIN |
| time over the response line (% of samples) | 16.54 | 7.913 | -52.2% | -13.86 to -3.403 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.8 | -2.5% | -0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.2 | +102 (native is 0) | +55.86 to +148.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.383 | 14.87 | +58.5% | +3.809 to +7.161 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05761 | 0.06729 | +16.8% | +0.002257 to +0.01711 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 1.406 | +1.7% | -0.003075 to +0.04943 | no |
| Omni's own CPU (cores), mean | 0 | 0.0523 | +0.0523 (native is 0) | +0.0461 to +0.0585 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.383 | 1.458 | +5.5% | +0.04802 to +0.1029 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.5 | 423.6 | -11.7% | -99.25 to -12.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.509 | +25.8% | +0.1465 to +0.8818 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | -0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | -0.8556 to +1.256 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 39.51 | 43.03 | +8.9% | +2.983 to +4.058 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.5 | 779.9 | +2.7% | +9.17 to +31.63 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.56 | -24.0% | -2.726 to -0.1533 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.6625 | +1035.7% | +0.5097 to +0.6987 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.3 | +160.0% | +0.3476 to +1.252 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.88 | 90.93 | +34.0% | +9.363 to +36.74 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*