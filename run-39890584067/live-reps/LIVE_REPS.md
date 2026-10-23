# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.099 | 5.997 |
| node-hours | 2.515 | 2.512 | 2.134 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 285.8 | 270 | 286.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 285.8 | 241.7 | 286.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 238.3 | 579.2 | 224.6 | 563.2 |
| response time (ms), 95th percentile | 708.4 | 1258 | 828.1 | 1221 |
| response time (ms), 99th percentile | 1043 | 1712 | 1198 | 1667 |
| time over the response line (% of samples) | 11.16 | 48.83 | 11.86 | 47.88 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 23.9 | 6.2 | 23.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 138.2 | 23.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.428 | 1.68 | 9.257 | 2.325 |
| utilisation (used / allocatable) | 0.05519 | 0.09666 | 0.06372 | 0.09681 |
| CPU used (cores), mean | 1.324 | 2.32 | 1.3 | 2.322 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0449 | 0.02622 |
| CPU used with Omni's own (cores), mean | 1.324 | 2.32 | 1.345 | 2.349 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.8 | 295.4 | 449.5 | 294.9 |
| HPA replicas, mean | 1.963 | 1.936 | 2.43 | 2.644 |
| pods started | 0.1 | 0.2 | 0.7 | 1.1 |
| pod start wait, total (s) | 0.1 | 0.3 | 1.7 | 2.8 |
| pod start wait, mean (s) | 0.1 | 0.3 | 0.9333 | 1.5 |
| host CPU busy, the real machine under kind (%) | 37.42 | 73.67 | 39.49 | 74.6 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 744.5 | 1447 | 751.4 | 1452 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.291 | 5.912 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 532.6 | 0.0125 | 534.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1084 | 0.1 | 1101 |
| queue: job turnaround, submitted to done, mean (s) | 52.24 | 890.5 | 58.92 | 881.4 |
| queue: jobs unfinished at the window's end | 0 | 11.9 | 0 | 11.5 |

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
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.0104 to +0.004022 | no |
| node-hours | 2.512 | 2.515 | +0.1% | -0.00585 to +0.01252 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 286.3 | +0.2% | -0.592 to +1.608 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 286.2 | +0.1% | -0.6851 to +1.501 | no |
| response time (ms), mean | 579.2 | 563.2 | -2.8% | -48.7 to +16.69 | no |
| response time (ms), 95th percentile | 1258 | 1221 | -2.9% | -131.8 to +58.62 | no |
| response time (ms), 99th percentile | 1712 | 1667 | -2.6% | -167.3 to +78.14 | no |
| time over the response line (% of samples) | 48.83 | 47.88 | -2.0% | -3.662 to +1.744 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.9 | 23.9 | +0.0% | -0.584 to +0.584 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.6 | +23.6 (native is 0) | +18.93 to +28.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.68 | 2.325 | +38.4% | +0.04054 to +1.249 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09666 | 0.09681 | +0.2% | -0.0006714 to +0.0009728 | no |
| CPU used (cores), mean | 2.32 | 2.322 | +0.1% | -0.01641 to +0.0214 | no |
| Omni's own CPU (cores), mean | 0 | 0.02622 | +0.0262 (native is 0) | +0.02267 to +0.02977 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.32 | 2.349 | +1.2% | +0.01028 to +0.04716 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.4 | 294.9 | -0.2% | -2.656 to +1.634 | no |
| HPA replicas, mean | 1.936 | 2.644 | +36.6% | +0.4132 to +1.002 | yes: power given |
| pods started | 0.2 | 1.1 | +450.0% | +0.2737 to +1.526 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.8 | +833.3% | +0.6763 to +4.324 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.5 | +400.0% | +0.2735 to +2.127 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 73.67 | 74.6 | +1.3% | +0.3938 to +1.477 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1447 | 1452 | +0.4% | -7.652 to +18.65 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.912 | -1.5% | -1.209 to +1.033 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 532.6 | 534.9 | +0.4% | -80.59 to +85.3 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1084 | 1101 | +1.5% | -56.44 to +89.97 | no |
| queue: job turnaround, submitted to done, mean (s) | 890.5 | 881.4 | -1.0% | -35.28 to +17.14 | no |
| queue: jobs unfinished at the window's end | 11.9 | 11.5 | -3.4% | -2.024 to +1.224 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.097e-15 to -3.441e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.512 | -0.1% | -0.0119 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 285.8 | +5.6% | +12.23 to +18.12 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 285.8 | +5.6% | +12.23 to +18.12 | yes: power given |
| response time (ms), mean | 238.3 | 579.2 | +143.0% | +275.6 to +406.2 | yes: LOSS |
| response time (ms), 95th percentile | 708.4 | 1258 | +77.6% | +386.7 to +712.3 | yes: LOSS |
| response time (ms), 99th percentile | 1043 | 1712 | +64.1% | +405.7 to +931.4 | yes: LOSS |
| time over the response line (% of samples) | 11.16 | 48.83 | +337.7% | +28.4 to +46.96 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 23.9 | +279.4% | +13.92 to +21.28 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.428 | 1.68 | -80.1% | -8.671 to -4.825 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05519 | 0.09666 | +75.2% | +0.03461 to +0.04834 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.324 | 2.32 | +75.2% | +0.8307 to +1.16 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.324 | 2.32 | +75.2% | +0.8307 to +1.16 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.8 | 295.4 | -40.3% | -242.5 to -156.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 1.936 | -1.4% | -0.1136 to +0.06002 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.1 | 0.3 | +200.0% | -0.3642 to +0.7642 | no |
| pod start wait, mean (s) | 0.1 | 0.3 | +200.0% | -0.3642 to +0.7642 | no |
| host CPU busy, the real machine under kind (%) | 37.42 | 73.67 | +96.8% | +32.42 to +40.06 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 744.5 | 1447 | +94.3% | +614.1 to +790.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 532.6 | +1597669.0% | +283 to +782.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1084 | +542131.7% | +723.5 to +1445 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 52.24 | 890.5 | +1604.7% | +690 to +986.5 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.9 | +11.9 (native is 0) | +6.213 to +17.59 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.099 | -15.0% | -1.526 to -0.2767 | yes: GAIN |
| node-hours | 2.515 | 2.134 | -15.1% | -0.6404 to -0.1211 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 270 | -0.2% | -1.573 to +0.2834 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 241.7 | -10.7% | -48.98 to -8.89 | yes: GAIN |
| response time (ms), mean | 238.3 | 224.6 | -5.8% | -30.54 to +3.062 | no |
| response time (ms), 95th percentile | 708.4 | 828.1 | +16.9% | +11.38 to +227.9 | yes: LOSS |
| response time (ms), 99th percentile | 1043 | 1198 | +14.8% | -5.096 to +314.3 | no |
| time over the response line (% of samples) | 11.16 | 11.86 | +6.3% | -0.1688 to +1.574 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 6.2 | -1.6% | -1.337 to +1.137 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.2 | +138 (native is 0) | +82.56 to +193.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.428 | 9.257 | +9.8% | -0.05193 to +1.709 | no |
| utilisation (used / allocatable) | 0.05519 | 0.06372 | +15.5% | +0.003631 to +0.01344 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.324 | 1.3 | -1.8% | -0.07654 to +0.0285 | no |
| Omni's own CPU (cores), mean | 0 | 0.0449 | +0.0449 (native is 0) | +0.03899 to +0.05081 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.324 | 1.345 | +1.6% | -0.03604 to +0.0778 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.8 | 449.5 | -9.1% | -69.42 to -21.08 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 2.43 | +23.8% | +0.1805 to +0.755 | yes: power given |
| pods started | 0.1 | 0.7 | +600.0% | -0.2396 to +1.44 | no |
| pod start wait, total (s) | 0.1 | 1.7 | +1600.0% | -0.372 to +3.572 | no |
| pod start wait, mean (s) | 0.1 | 0.9333 | +833.3% | -0.1352 to +1.802 | no |
| host CPU busy, the real machine under kind (%) | 37.42 | 39.49 | +5.5% | +1.49 to +2.642 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 744.5 | 751.4 | +0.9% | +0.4362 to +13.36 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.291 | -28.5% | -2.886 to -0.5325 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.0125 | -62.5% | -0.0498 to +0.008131 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.1 | -50.0% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 52.24 | 58.92 | +12.8% | +0.1894 to +13.17 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.099 | -15.0% | -1.526 to -0.2767 | yes: GAIN |
| node-hours | 2.512 | 2.134 | -15.0% | -0.6392 to -0.1163 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 270 | -5.5% | -19.32 to -12.32 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 241.7 | -15.4% | -66.24 to -21.98 | yes: GAIN |
| response time (ms), mean | 579.2 | 224.6 | -61.2% | -417.8 to -291.5 | yes: GAIN |
| response time (ms), 95th percentile | 1258 | 828.1 | -34.2% | -680.1 to -179.7 | yes: GAIN |
| response time (ms), 99th percentile | 1712 | 1198 | -30.0% | -909.2 to -118.8 | yes: GAIN |
| time over the response line (% of samples) | 48.83 | 11.86 | -75.7% | -46.12 to -27.83 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.9 | 6.2 | -74.1% | -21.63 to -13.77 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.2 | +138 (native is 0) | +82.56 to +193.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.68 | 9.257 | +451.0% | +5.451 to +9.703 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09666 | 0.06372 | -34.1% | -0.03861 to -0.02727 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.32 | 1.3 | -43.9% | -1.225 to -0.814 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0449 | +0.0449 (native is 0) | +0.03899 to +0.05081 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.32 | 1.345 | -42.0% | -1.183 to -0.7658 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.4 | 449.5 | +52.2% | +124.7 to +183.4 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.936 | 2.43 | +25.5% | +0.1861 to +0.803 | yes: power given |
| pods started | 0.2 | 0.7 | +250.0% | -0.4079 to +1.408 | no |
| pod start wait, total (s) | 0.3 | 1.7 | +466.7% | -0.7112 to +3.511 | no |
| pod start wait, mean (s) | 0.3 | 0.9333 | +211.1% | -0.5209 to +1.788 | no |
| host CPU busy, the real machine under kind (%) | 73.67 | 39.49 | -46.4% | -38.33 to -30.02 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1447 | 751.4 | -48.1% | -783 to -608 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.776 | -53.7% | -3.224 to -3.224 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 532.6 | 0.0125 | -100.0% | -782.1 to -283 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1084 | 0.1 | -100.0% | -1445 to -723.6 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 890.5 | 58.92 | -93.4% | -976.2 to -687 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.9 | 0 | -100.0% | -17.59 to -6.213 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.0104 to +0.004022 | no |
| node-hours | 2.515 | 2.515 | +0.0% | -0.006192 to +0.006858 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 286.3 | +5.8% | +12.72 to +18.65 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 286.2 | +5.8% | +12.58 to +18.59 | yes: power given |
| response time (ms), mean | 238.3 | 563.2 | +136.3% | +269.5 to +380.3 | yes: LOSS |
| response time (ms), 95th percentile | 708.4 | 1221 | +72.4% | +300 to +725.9 | yes: LOSS |
| response time (ms), 99th percentile | 1043 | 1667 | +59.8% | +300.8 to +947.1 | yes: LOSS |
| time over the response line (% of samples) | 11.16 | 47.88 | +329.1% | +29.05 to +44.39 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 23.9 | +279.4% | +13.95 to +21.25 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.6 | +23.6 (native is 0) | +18.93 to +28.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.428 | 2.325 | -72.4% | -8.389 to -3.817 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05519 | 0.09681 | +75.4% | +0.03474 to +0.04852 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.324 | 2.322 | +75.3% | +0.8325 to +1.163 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02622 | +0.0262 (native is 0) | +0.02267 to +0.02977 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.324 | 2.349 | +77.3% | +0.861 to +1.187 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.8 | 294.9 | -40.4% | -243.3 to -156.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 2.644 | +34.7% | +0.4027 to +0.9591 | yes: power given |
| pods started | 0.1 | 1.1 | +1000.0% | +0.3256 to +1.674 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.8 | +2700.0% | +0.791 to +4.609 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.5 | +1400.0% | +0.4492 to +2.351 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.42 | 74.6 | +99.3% | +33.56 to +40.79 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 744.5 | 1452 | +95.1% | +624.4 to +791.4 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.912 | -1.5% | -1.209 to +1.033 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 534.9 | +1604725.7% | +294.5 to +775.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1101 | +550514.9% | +727.3 to +1475 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 52.24 | 881.4 | +1587.3% | +687.3 to +971 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.5 | +11.5 (native is 0) | +6.081 to +16.92 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*