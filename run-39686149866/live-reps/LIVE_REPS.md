# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.549 | 6 |
| node-hours | 2.51 | 2.518 | 1.905 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 286.1 | 270.4 | 285.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 286.1 | 224.9 | 285.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 239.8 | 528.7 | 217.7 | 516.1 |
| response time (ms), 95th percentile | 804.9 | 1153 | 861.9 | 1137 |
| response time (ms), 99th percentile | 1140 | 1522 | 1198 | 1552 |
| time over the response line (% of samples) | 8.854 | 43 | 9.243 | 42.92 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 23 | 5.2 | 22.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 63.6 | 19.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 80 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.828 | 2.198 | 8.908 | 2.17 |
| utilisation (used / allocatable) | 0.05562 | 0.09538 | 0.07343 | 0.0947 |
| CPU used (cores), mean | 1.335 | 2.289 | 1.308 | 2.273 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01667 | 0.00784 |
| CPU used with Omni's own (cores), mean | 1.335 | 2.289 | 1.325 | 2.281 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.3 | 299.5 | 416.6 | 301.4 |
| HPA replicas, mean | 1.955 | 2.084 | 2.099 | 2.393 |
| pods started | 0.2 | 0.5 | 0.4 | 0.5 |
| pod start wait, total (s) | 0.4 | 0.9 | 0.8 | 1 |
| pod start wait, mean (s) | 0.2 | 0.8 | 0.8 | 0.8 |
| host CPU busy, the real machine under kind (%) | 37.95 | 71.27 | 38.73 | 71.23 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 755.6 | 1384 | 758.8 | 1377 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 402.8 | 0.0375 | 436.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 767.7 | 0.3 | 768.7 |
| queue: job turnaround, submitted to done, mean (s) | 61.85 | 792.6 | 64.15 | 786.3 |
| queue: jobs unfinished at the window's end | 0 | 8.9 | 0 | 9.3 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.51e-15 to +1.155e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.518 | 2.515 | -0.1% | -0.01073 to +0.003393 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.1 | 285.4 | -0.2% | -1.466 to +0.1502 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.1 | 285.4 | -0.2% | -1.466 to +0.1502 | no |
| response time (ms), mean | 528.7 | 516.1 | -2.4% | -39.94 to +14.71 | no |
| response time (ms), 95th percentile | 1153 | 1137 | -1.4% | -97.13 to +64.2 | no |
| response time (ms), 99th percentile | 1522 | 1552 | +2.0% | -80 to +141.3 | no |
| time over the response line (% of samples) | 43 | 42.92 | -0.2% | -3.938 to +3.773 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23 | 22.6 | -1.7% | -0.7694 to -0.03062 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.4 | +19.4 (native is 0) | +16.18 to +22.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.198 | 2.17 | -1.3% | -0.3996 to +0.3429 | no |
| utilisation (used / allocatable) | 0.09538 | 0.0947 | -0.7% | -0.001663 to +0.0003042 | no |
| CPU used (cores), mean | 2.289 | 2.273 | -0.7% | -0.03991 to +0.0073 | no |
| Omni's own CPU (cores), mean | 0 | 0.00784 | +0.00784 (native is 0) | +0.006739 to +0.008941 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.289 | 2.281 | -0.4% | -0.03195 to +0.01502 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.5 | 301.4 | +0.6% | -0.8755 to +4.707 | no |
| HPA replicas, mean | 2.084 | 2.393 | +14.8% | +0.0111 to +0.6067 | yes: power given |
| pods started | 0.5 | 0.5 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.9 | 1 | +11.1% | -0.99 to +1.19 | no |
| pod start wait, mean (s) | 0.8 | 0.8 | +0.0% | -0.8921 to +0.8921 | no |
| host CPU busy, the real machine under kind (%) | 71.27 | 71.23 | -0.1% | -1.103 to +1.025 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1384 | 1377 | -0.5% | -28.38 to +14.78 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 402.8 | 436.3 | +8.3% | -17.18 to +84.34 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 767.7 | 768.7 | +0.1% | -55.82 to +57.79 | no |
| queue: job turnaround, submitted to done, mean (s) | 792.6 | 786.3 | -0.8% | -27.72 to +15.09 | no |
| queue: jobs unfinished at the window's end | 8.9 | 9.3 | +4.5% | -0.3689 to +1.169 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.244e-15 to -3.091e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.51 | 2.518 | +0.3% | +0.002867 to +0.01413 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 286.1 | +5.8% | +12.83 to +18.66 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 286.1 | +5.8% | +12.83 to +18.66 | yes: power given |
| response time (ms), mean | 239.8 | 528.7 | +120.5% | +226.8 to +351 | yes: LOSS |
| response time (ms), 95th percentile | 804.9 | 1153 | +43.3% | -55.29 to +751.9 | no |
| response time (ms), 99th percentile | 1140 | 1522 | +33.5% | -219.6 to +982.8 | no |
| time over the response line (% of samples) | 8.854 | 43 | +385.7% | +23.84 to +44.45 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 23 | +422.7% | +14.62 to +22.58 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.828 | 2.198 | -75.1% | -9.211 to -4.049 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05562 | 0.09538 | +71.5% | +0.031 to +0.04852 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.335 | 2.289 | +71.5% | +0.744 to +1.164 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.335 | 2.289 | +71.5% | +0.744 to +1.164 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.3 | 299.5 | -40.6% | -285.5 to -124.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.084 | +6.6% | -0.06966 to +0.3283 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | -0.5256 to +1.526 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 37.95 | 71.27 | +87.8% | +28.95 to +37.7 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 755.6 | 1384 | +83.2% | +531.7 to +725.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 402.8 | +743467.2% | +123.6 to +681.8 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 767.7 | +255791.0% | +321 to +1214 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 61.85 | 792.6 | +1181.4% | +559.1 to +902.5 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.9 | +8.9 (native is 0) | +2.01 to +15.79 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.549 | -24.2% | -2.323 to -0.5791 | yes: GAIN |
| node-hours | 2.51 | 1.905 | -24.1% | -0.9727 to -0.2376 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.4 | +0.0% | -0.6093 to +0.7248 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 224.9 | -16.8% | -73.17 to -17.77 | yes: GAIN |
| response time (ms), mean | 239.8 | 217.7 | -9.2% | -29.35 to -14.82 | yes: GAIN |
| response time (ms), 95th percentile | 804.9 | 861.9 | +7.1% | +25.1 to +88.9 | yes: LOSS |
| response time (ms), 99th percentile | 1140 | 1198 | +5.1% | -36.44 to +151.7 | no |
| time over the response line (% of samples) | 8.854 | 9.243 | +4.4% | -0.2014 to +0.9779 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 5.2 | +18.2% | -0.5403 to +2.14 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.6 | +63.6 (native is 0) | +39.07 to +88.13 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.828 | 8.908 | +0.9% | -2.085 to +2.245 | no |
| utilisation (used / allocatable) | 0.05562 | 0.07343 | +32.0% | +0.006796 to +0.02884 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.335 | 1.308 | -2.0% | -0.0566 to +0.003345 | no |
| Omni's own CPU (cores), mean | 0 | 0.01667 | +0.0167 (native is 0) | +0.01552 to +0.01782 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.335 | 1.325 | -0.7% | -0.03966 to +0.01975 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.3 | 416.6 | -17.4% | -145.8 to -29.71 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.099 | +7.3% | -0.108 to +0.3954 | no |
| pods started | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.4 | 0.8 | +100.0% | -0.5656 to +1.366 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 37.95 | 38.73 | +2.1% | +0.4962 to +1.073 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 755.6 | 758.8 | +0.4% | -0.7869 to +7.187 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.6 | -40.0% | -3.814 to -0.986 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0375 | -30.8% | -0.05165 to +0.01832 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 61.85 | 64.15 | +3.7% | -0.2634 to +4.863 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.549 | -24.2% | -2.323 to -0.5791 | yes: GAIN |
| node-hours | 2.518 | 1.905 | -24.4% | -0.9788 to -0.2486 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 286.1 | 270.4 | -5.5% | -18.73 to -12.65 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.1 | 224.9 | -21.4% | -90.06 to -32.37 | yes: GAIN |
| response time (ms), mean | 528.7 | 217.7 | -58.8% | -377.1 to -244.9 | yes: GAIN |
| response time (ms), 95th percentile | 1153 | 861.9 | -25.3% | -716.2 to +133.5 | no |
| response time (ms), 99th percentile | 1522 | 1198 | -21.3% | -973.9 to +326 | no |
| time over the response line (% of samples) | 43 | 9.243 | -78.5% | -43.81 to -23.7 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23 | 5.2 | -77.4% | -21.67 to -13.93 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63.6 | +63.6 (native is 0) | +39.07 to +88.13 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.198 | 8.908 | +305.2% | +3.136 to +10.28 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09538 | 0.07343 | -23.0% | -0.0336 to -0.01028 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.289 | 1.308 | -42.8% | -1.186 to -0.7761 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01667 | +0.0167 (native is 0) | +0.01552 to +0.01782 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.289 | 1.325 | -42.1% | -1.169 to -0.7597 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.5 | 416.6 | +39.1% | +69.92 to +164.4 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.084 | 2.099 | +0.7% | -0.1966 to +0.2253 | no |
| pods started | 0.5 | 0.4 | -20.0% | -0.7263 to +0.5263 | no |
| pod start wait, total (s) | 0.9 | 0.8 | -11.1% | -1.137 to +0.9366 | no |
| pod start wait, mean (s) | 0.8 | 0.8 | +0.0% | -0.9537 to +0.9537 | no |
| host CPU busy, the real machine under kind (%) | 71.27 | 38.73 | -45.7% | -36.96 to -28.13 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1384 | 758.8 | -45.2% | -721.2 to -529.2 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.087 | -65.2% | -4.113 to -3.712 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 402.8 | 0.0375 | -100.0% | -681.8 to -123.6 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 767.7 | 0.3 | -100.0% | -1214 to -321 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 792.6 | 64.15 | -91.9% | -898.7 to -558.2 | yes: GAIN |
| queue: jobs unfinished at the window's end | 8.9 | 0 | -100.0% | -15.79 to -2.01 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.589e-15 to -3.191e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.51 | 2.515 | +0.2% | -0.003661 to +0.01333 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 285.4 | +5.6% | +12.27 to +17.9 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 285.4 | +5.6% | +12.27 to +17.9 | yes: power given |
| response time (ms), mean | 239.8 | 516.1 | +115.2% | +214.4 to +338.1 | yes: LOSS |
| response time (ms), 95th percentile | 804.9 | 1137 | +41.2% | -108.3 to +772 | no |
| response time (ms), 99th percentile | 1140 | 1552 | +36.2% | -244.4 to +1069 | no |
| time over the response line (% of samples) | 8.854 | 42.92 | +384.7% | +24.82 to +43.31 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 22.6 | +413.6% | +14.31 to +22.09 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.4 | +19.4 (native is 0) | +16.18 to +22.62 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.828 | 2.17 | -75.4% | -9.156 to -4.161 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05562 | 0.0947 | +70.3% | +0.02996 to +0.0482 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.335 | 2.273 | +70.3% | +0.719 to +1.157 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00784 | +0.00784 (native is 0) | +0.006739 to +0.008941 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.335 | 2.281 | +70.9% | +0.7272 to +1.164 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.3 | 301.4 | -40.2% | -284.9 to -121.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.955 | 2.393 | +22.4% | +0.1223 to +0.7542 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | -0.4578 to +1.058 | no |
| pod start wait, total (s) | 0.4 | 1 | +150.0% | -0.9155 to +2.116 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | -0.3656 to +1.566 | no |
| host CPU busy, the real machine under kind (%) | 37.95 | 71.23 | +87.7% | +28.39 to +38.18 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 755.6 | 1377 | +82.3% | +521 to +722.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 436.3 | +805457.2% | +123.9 to +748.7 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 768.7 | +256118.4% | +298.3 to +1238 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 61.85 | 786.3 | +1171.2% | +552.6 to +896.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.3 | +9.3 (native is 0) | +2.044 to +16.56 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*