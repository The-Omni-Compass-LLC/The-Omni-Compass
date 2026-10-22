# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.25 | 10.82 |
| node-hours | 5.02 | 5.027 | 4.292 | 4.536 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 525.8 | 524.8 | 526.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 525.8 | 469.7 | 489.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 522.5 | 755.5 | 518.8 | 824.7 |
| response time (ms), 95th percentile | 2052 | 2879 | 2234 | 3199 |
| response time (ms), 99th percentile | 2898 | 3962 | 3191 | 4233 |
| time over the response line (% of samples) | 19.83 | 25.72 | 20.08 | 26.57 |
| failed requests (%) | 0 | 0.008264 | 0 | 0.137 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 11.7 | 9.7 | 12.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 85 | 74.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.49 | 18.43 | 13.49 | 20.77 |
| utilisation (used / allocatable) | 0.03301 | 0.03506 | 0.03946 | 0.03884 |
| CPU used (cores), mean | 1.584 | 1.683 | 1.595 | 1.694 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01243 | 0.01288 |
| CPU used with Omni's own (cores), mean | 1.584 | 1.683 | 1.607 | 1.707 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.4 | 772.7 | 712 | 710 |
| HPA replicas, mean | 4.01 | 3.95 | 4.606 | 4.416 |
| pods started | 0.2 | 0.3 | 1.6 | 1.6 |
| pod start wait, total (s) | 0.5 | 0.5 | 2.7 | 3.8 |
| pod start wait, mean (s) | 0.5 | 0.3 | 1.142 | 1.633 |
| host CPU busy, the real machine under kind (%) | 48.57 | 55.22 | 50.43 | 57.37 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 847 | 947.7 | 860.9 | 975.2 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.276 | 10.06 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 10.78 | 0.05 | 18.31 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 68 | 0.3 | 107.6 |
| queue: job turnaround, submitted to done, mean (s) | 155.5 | 227.1 | 164.5 | 256.3 |
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
| worker nodes in service, mean | 12 | 10.82 | -9.8% | -2.448 to +0.09324 | no |
| node-hours | 5.027 | 4.536 | -9.8% | -1.023 to +0.04186 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 526.5 | +0.1% | -0.8452 to +2.312 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 489.5 | -6.9% | -76.8 to +4.116 | no |
| response time (ms), mean | 755.5 | 824.7 | +9.2% | -62.72 to +201.1 | no |
| response time (ms), 95th percentile | 2879 | 3199 | +11.1% | -265.7 to +907.3 | no |
| response time (ms), 99th percentile | 3962 | 4233 | +6.8% | -420.2 to +962.1 | no |
| time over the response line (% of samples) | 25.72 | 26.57 | +3.3% | -0.1775 to +1.878 | no |
| failed requests (%) | 0.008264 | 0.137 | +1558.3% | -0.1281 to +0.3857 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.6 | +7.7% | +0.04362 to +1.756 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.1 | +74.1 (native is 0) | +38.53 to +109.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.43 | 20.78 | +12.7% | -5.817 to +10.51 | no |
| utilisation (used / allocatable) | 0.03506 | 0.03884 | +10.8% | +0.0007844 to +0.006786 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.683 | 1.694 | +0.7% | -0.06117 to +0.08305 | no |
| Omni's own CPU (cores), mean | 0 | 0.01288 | +0.0129 (native is 0) | +0.01207 to +0.01369 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.683 | 1.707 | +1.4% | -0.04871 to +0.09635 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 772.7 | 710 | -8.1% | -115.1 to -10.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.95 | 4.416 | +11.8% | +0.1733 to +0.7585 | yes: power given |
| pods started | 0.3 | 1.6 | +433.3% | +0.08188 to +2.518 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.8 | +660.0% | +0.2456 to +6.354 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.633 | +444.4% | +0.05548 to +2.611 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.22 | 57.37 | +3.9% | +1.134 to +3.163 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 947.7 | 975.2 | +2.9% | +4.543 to +50.46 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.06 | -16.2% | -3.985 to +0.1082 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 10.78 | 18.31 | +70.0% | -10.76 to +25.83 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 68 | 107.6 | +58.2% | -58.24 to +137.4 | no |
| queue: job turnaround, submitted to done, mean (s) | 227.1 | 256.3 | +12.9% | -6.995 to +65.4 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | +0.0% | -1.941e-15 to +4.073e-15 | EVEN, the same (under one part in a million) |
| node-hours | 5.02 | 5.027 | +0.1% | -0.005848 to +0.01851 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 525.8 | +0.4% | +0.06804 to +3.822 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 525.8 | +0.4% | +0.06804 to +3.822 | yes: power given |
| response time (ms), mean | 522.5 | 755.5 | +44.6% | +72.49 to +393.6 | yes: LOSS |
| response time (ms), 95th percentile | 2052 | 2879 | +40.3% | +215.3 to +1438 | yes: LOSS |
| response time (ms), 99th percentile | 2898 | 3962 | +36.7% | +300.5 to +1828 | yes: LOSS |
| time over the response line (% of samples) | 19.83 | 25.72 | +29.7% | +2.039 to +9.742 | yes: LOSS |
| failed requests (%) | 0 | 0.008264 | +0.00826 (native is 0) | -0.01043 to +0.02696 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 11.7 | +24.5% | +1.082 to +3.518 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.49 | 18.43 | +27.2% | -3.744 to +11.62 | no |
| utilisation (used / allocatable) | 0.03301 | 0.03506 | +6.2% | +0.0007966 to +0.003301 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.584 | 1.683 | +6.2% | +0.03824 to +0.1584 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.584 | 1.683 | +6.2% | +0.03824 to +0.1584 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.4 | 772.7 | -5.4% | -67.49 to -19.87 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.01 | 3.95 | -1.5% | -0.2619 to +0.1419 | no |
| pods started | 0.2 | 0.3 | +50.0% | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.5 | 0.5 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.5 | 0.3 | -40.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 48.57 | 55.22 | +13.7% | +4.318 to +8.983 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 847 | 947.7 | +11.9% | +35.69 to +165.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 10.78 | +13510.5% | -1.46 to +22.85 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 68 | +16900.0% | -9.531 to +144.7 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.5 | 227.1 | +46.1% | +25.11 to +118.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.25 | -14.6% | -3.54 to +0.03125 | no |
| node-hours | 5.02 | 4.292 | -14.5% | -1.476 to +0.02056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 524.8 | +0.2% | -0.8488 to +2.648 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 469.7 | -10.3% | -110.6 to +2.267 | no |
| response time (ms), mean | 522.5 | 518.8 | -0.7% | -32.5 to +25.21 | no |
| response time (ms), 95th percentile | 2052 | 2234 | +8.9% | -2.388 to +366.9 | no |
| response time (ms), 99th percentile | 2898 | 3191 | +10.1% | +15.2 to +571.2 | yes: LOSS |
| time over the response line (% of samples) | 19.83 | 20.08 | +1.3% | -0.1934 to +0.6981 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.7 | +3.2% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85 | +85 (native is 0) | +40.01 to +130 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.49 | 13.49 | -6.9% | -5.002 to +3.005 | no |
| utilisation (used / allocatable) | 0.03301 | 0.03946 | +19.6% | +0.0006028 to +0.01231 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.584 | 1.595 | +0.6% | -0.05218 to +0.07252 | no |
| Omni's own CPU (cores), mean | 0 | 0.01243 | +0.0124 (native is 0) | +0.01148 to +0.01338 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.584 | 1.607 | +1.4% | -0.0396 to +0.08481 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.4 | 712 | -12.8% | -202 to -6.75 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.01 | 4.606 | +14.9% | +0.2174 to +0.9758 | yes: power given |
| pods started | 0.2 | 1.6 | +700.0% | +0.3231 to +2.477 | yes: power given |
| pod start wait, total (s) | 0.5 | 2.7 | +440.0% | -0.1068 to +4.507 | no |
| pod start wait, mean (s) | 0.5 | 1.142 | +128.3% | -0.4781 to +1.761 | no |
| host CPU busy, the real machine under kind (%) | 48.57 | 50.43 | +3.8% | +1.074 to +2.63 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 847 | 860.9 | +1.6% | -0.6756 to +28.48 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.276 | -22.7% | -5.419 to -0.02842 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.05 | -36.8% | -0.09049 to +0.03216 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | -25.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.5 | 164.5 | +5.8% | -0.9648 to +19.06 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.25 | -14.6% | -3.54 to +0.03125 | no |
| node-hours | 5.027 | 4.292 | -14.6% | -1.487 to +0.01813 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 524.8 | -0.2% | -2.799 to +0.7079 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 469.7 | -10.7% | -112.6 to +0.3242 | no |
| response time (ms), mean | 755.5 | 518.8 | -31.3% | -389.5 to -83.89 | yes: GAIN |
| response time (ms), 95th percentile | 2879 | 2234 | -22.4% | -1217 to -72.17 | yes: GAIN |
| response time (ms), 99th percentile | 3962 | 3191 | -19.5% | -1499 to -42.63 | yes: GAIN |
| time over the response line (% of samples) | 25.72 | 20.08 | -21.9% | -9.223 to -2.054 | yes: GAIN |
| failed requests (%) | 0.008264 | 0 | -100.0% | -0.02696 to +0.01043 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 9.7 | -17.1% | -3.012 to -0.9884 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85 | +85 (native is 0) | +40.01 to +130 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.43 | 13.49 | -26.8% | -12.3 to +2.431 | no |
| utilisation (used / allocatable) | 0.03506 | 0.03946 | +12.6% | -0.001948 to +0.01076 | no |
| CPU used (cores), mean | 1.683 | 1.595 | -5.2% | -0.1574 to -0.01891 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01243 | +0.0124 (native is 0) | +0.01148 to +0.01338 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.683 | 1.607 | -4.5% | -0.145 to -0.006471 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 772.7 | 712 | -7.9% | -154.4 to +32.93 | no |
| HPA replicas, mean | 3.95 | 4.606 | +16.6% | +0.2434 to +1.07 | yes: power given |
| pods started | 0.3 | 1.6 | +433.3% | +0.1791 to +2.421 | yes: power given |
| pod start wait, total (s) | 0.5 | 2.7 | +440.0% | +0.04615 to +4.354 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.142 | +280.6% | +0.04765 to +1.636 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.22 | 50.43 | -8.7% | -6.663 to -2.935 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 947.7 | 860.9 | -9.2% | -141.4 to -32.2 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.276 | -22.7% | -5.419 to -0.02842 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 10.78 | 0.05 | -99.5% | -22.91 to +1.463 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 68 | 0.3 | -99.6% | -145 to +9.565 | no |
| queue: job turnaround, submitted to done, mean (s) | 227.1 | 164.5 | -27.6% | -104.4 to -20.76 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.82 | -9.8% | -2.448 to +0.09324 | no |
| node-hours | 5.02 | 4.536 | -9.6% | -1.012 to +0.0438 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.9 | 526.5 | +0.5% | +1.022 to +4.335 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.9 | 489.5 | -6.6% | -74.74 to +5.944 | no |
| response time (ms), mean | 522.5 | 824.7 | +57.8% | +87.25 to +517.2 | yes: LOSS |
| response time (ms), 95th percentile | 2052 | 3199 | +55.9% | +289 to +2006 | yes: LOSS |
| response time (ms), 99th percentile | 2898 | 4233 | +46.1% | +297.4 to +2373 | yes: LOSS |
| time over the response line (% of samples) | 19.83 | 26.57 | +34.0% | +2.889 to +10.59 | yes: LOSS |
| failed requests (%) | 0 | 0.137 | +0.137 (native is 0) | -0.1166 to +0.3907 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 12.6 | +34.0% | +1.39 to +5.01 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.1 | +74.1 (native is 0) | +38.53 to +109.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.49 | 20.78 | +43.4% | +2.255 to +10.31 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03301 | 0.03884 | +17.7% | +0.003142 to +0.008526 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.584 | 1.694 | +6.9% | +0.02129 to +0.1973 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01288 | +0.0129 (native is 0) | +0.01207 to +0.01369 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.584 | 1.707 | +7.7% | +0.03389 to +0.2104 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 816.4 | 710 | -13.0% | -166.7 to -46.11 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.01 | 4.416 | +10.1% | +0.1383 to +0.6734 | yes: power given |
| pods started | 0.2 | 1.6 | +700.0% | +0.3231 to +2.477 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.8 | +660.0% | +0.3594 to +6.241 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.633 | +226.7% | -0.2499 to +2.517 | no |
| host CPU busy, the real machine under kind (%) | 48.57 | 57.37 | +18.1% | +5.864 to +11.73 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 847 | 975.2 | +15.1% | +48.42 to +208 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.06 | -16.2% | -3.985 to +0.1082 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 18.31 | +23031.6% | -4.158 to +40.62 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 107.6 | +26800.0% | -18.63 to +233 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.5 | 256.3 | +64.9% | +36.29 to +165.4 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*