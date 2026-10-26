# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.267 | 5.973 |
| node-hours | 2.51 | 2.517 | 2.211 | 2.505 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 272 | 271.9 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 272 | 248.8 | 271.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 260.7 | 135.7 | 236.3 | 103 |
| response time (ms), 95th percentile | 789.5 | 235.2 | 859.8 | 227.4 |
| response time (ms), 99th percentile | 1138 | 340.3 | 1254 | 341.6 |
| time over the response line (% of samples) | 14.02 | 0.1541 | 14.78 | 0.2453 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 0 | 9.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 30.5 | 14.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 1115 | 8.588 | 1086 |
| utilisation (used / allocatable) | 0.05677 | 0.05876 | 0.06593 | 0.0598 |
| CPU used (cores), mean | 1.362 | 1.41 | 1.365 | 1.429 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01525 | 0.01247 |
| CPU used with Omni's own (cores), mean | 1.362 | 1.41 | 1.38 | 1.442 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.3 | 460.5 | 433.6 | 453.4 |
| HPA replicas, mean | 1.989 | 2.02 | 2.126 | 1.982 |
| pods started | 0.2 | 0 | 0 | 0 |
| pod start wait, total (s) | 0.4 | 0 | 0 | 0 |
| pod start wait, mean (s) | 0.2 | 0 | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 38.93 | 43.93 | 39.88 | 45.05 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 742.3 | 1453 | 745.6 | 1443 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.782 | 5.613 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 151.5 | 0.04167 | 146.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 689.8 | 0.3 | 646.7 |
| queue: job turnaround, submitted to done, mean (s) | 49.98 | 856.5 | 53.23 | 808.2 |
| queue: jobs unfinished at the window's end | 0 | 12.2 | 0 | 10.4 |

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
| worker nodes in service, mean | 6 | 5.973 | −0.4% | −0.0775 to +0.0239 | no |
| node-hours | 2.517 | 2.505 | −0.5% | −0.0336 to +0.0095 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.2 | +0.1% | −0.7289 to +1.2205 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.4 | −0.2% | −2.4744 to +1.2868 | no |
| response time (ms), mean | 135.7 | 103 | −24.1% | −39.6775 to −25.8193 | yes: GAIN |
| response time (ms), 95th percentile | 235.2 | 227.4 | −3.3% | −17.1236 to +1.5206 | no |
| response time (ms), 99th percentile | 340.3 | 341.6 | +0.4% | −18.6236 to +21.3096 | no |
| time over the response line (% of samples) | 0.1541 | 0.2453 | +59.2% | −0.0231 to +0.2056 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.9 | +14.900 (native is 0) | +10.7778 to +19.0222 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1115 | 1086 | −2.6% | −86.6268 to +28.8301 | no |
| utilisation (used / allocatable) | 0.05876 | 0.0598 | +1.8% | −0.0005 to +0.0026 | no |
| CPU used (cores), mean | 1.41 | 1.429 | +1.3% | −0.0167 to +0.0547 | no |
| Omni's own CPU (cores), mean | 0 | 0.01247 | +0.012 (native is 0) | +0.0115 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.442 | +2.2% | −0.0045 to +0.0675 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.5 | 453.4 | −1.5% | −17.8570 to +3.8188 | no |
| HPA replicas, mean | 2.02 | 1.982 | −1.9% | −0.2546 to +0.1778 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.93 | 45.05 | +2.6% | +0.1779 to +2.0721 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1453 | 1443 | −0.7% | −30.7717 to +11.5717 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.42 | −9.7% | −4.3241 to +3.1634 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 151.5 | 146.3 | −3.4% | −53.8648 to +43.4815 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 689.8 | 646.7 | −6.2% | −216.0688 to +129.8688 | no |
| queue: job turnaround, submitted to done, mean (s) | 856.5 | 808.2 | −5.7% | −112.9213 to +16.1296 | no |
| queue: jobs unfinished at the window's end | 12.2 | 10.4 | −14.8% | −3.8732 to +0.2732 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.51 | 2.517 | +0.3% | +0.0010 to +0.0126 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 272 | +0.5% | −0.1692 to +2.6545 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 272 | +0.5% | −0.1692 to +2.6545 | no |
| response time (ms), mean | 260.7 | 135.7 | −47.9% | −179.7186 to −70.2667 | yes: GAIN |
| response time (ms), 95th percentile | 789.5 | 235.2 | −70.2% | −799.7671 to −308.8109 | yes: GAIN |
| response time (ms), 99th percentile | 1138 | 340.3 | −70.1% | −1133.8437 to −462.4307 | yes: GAIN |
| time over the response line (% of samples) | 14.02 | 0.1541 | −98.9% | −21.3900 to −6.3498 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 0 | −100.0% | −13.3641 to −5.4359 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 1115 | +12042.2% | +868.8090 to +1342.1377 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05677 | 0.05876 | +3.5% | −0.0023 to +0.0063 | no |
| CPU used (cores), mean | 1.362 | 1.41 | +3.5% | −0.0563 to +0.1522 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.362 | 1.41 | +3.5% | −0.0563 to +0.1522 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.3 | 460.5 | −4.9% | −65.6481 to +17.9400 | no |
| HPA replicas, mean | 1.989 | 2.02 | +1.6% | −0.1687 to +0.2308 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.4 | 0 | −100.0% | −1.3048 to +0.5048 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 38.93 | 43.93 | +12.8% | +3.0122 to +6.9867 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 742.3 | 1453 | +95.7% | +629.5742 to +791.4258 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 151.5 | +330418.2% | +116.1776 to +186.7057 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 689.8 | +229833.3% | +562.2038 to +816.7962 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 49.98 | 856.6 | +1613.7% | +658.5979 to +954.5354 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.2 | +12.200 (native is 0) | +6.1229 to +18.2771 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.267 | −12.2% | −1.4943 to +0.0289 | no |
| node-hours | 2.51 | 2.211 | −11.9% | −0.6161 to +0.0186 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.9 | +0.4% | +0.4107 to +1.8589 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 248.8 | −8.1% | −45.6235 to +1.6764 | no |
| response time (ms), mean | 260.7 | 236.3 | −9.4% | −36.9509 to −11.9670 | yes: GAIN |
| response time (ms), 95th percentile | 789.5 | 859.8 | +8.9% | +2.5525 to +138.0635 | yes: LOSS |
| response time (ms), 99th percentile | 1138 | 1254 | +10.1% | +24.1331 to +206.2055 | yes: LOSS |
| time over the response line (% of samples) | 14.02 | 14.78 | +5.4% | +0.1469 to +1.3636 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.7 | +3.2% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.500 (native is 0) | +15.4606 to +45.5394 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 8.588 | −6.4% | −1.7865 to +0.6031 | no |
| utilisation (used / allocatable) | 0.05677 | 0.06593 | +16.1% | −0.0009 to +0.0192 | no |
| CPU used (cores), mean | 1.362 | 1.365 | +0.2% | −0.0174 to +0.0227 | no |
| Omni's own CPU (cores), mean | 0 | 0.01525 | +0.015 (native is 0) | +0.0142 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.362 | 1.38 | +1.3% | −0.0018 to +0.0377 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.3 | 433.6 | −10.5% | −107.9440 to +6.6161 | no |
| HPA replicas, mean | 1.989 | 2.126 | +6.9% | −0.0896 to +0.3625 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.4 | 0 | −100.0% | −1.3048 to +0.5048 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 38.93 | 39.88 | +2.4% | +0.4760 to +1.4164 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 742.3 | 745.6 | +0.4% | −1.4931 to +8.0931 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.782 | −20.3% | −2.4149 to −0.0209 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04167 | −9.1% | −0.0450 to +0.0367 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 49.98 | 53.23 | +6.5% | −0.0335 to +6.5252 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.267 | −12.2% | −1.4943 to +0.0289 | no |
| node-hours | 2.517 | 2.211 | −12.1% | −0.6223 to +0.0111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.9 | −0.0% | −1.2581 to +1.0424 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 248.8 | −8.5% | −48.0108 to +1.5784 | no |
| response time (ms), mean | 135.7 | 236.3 | +74.1% | +50.1311 to +150.9363 | yes: LOSS |
| response time (ms), 95th percentile | 235.2 | 859.8 | +265.5% | +373.2460 to +875.9480 | yes: LOSS |
| response time (ms), 99th percentile | 340.3 | 1254 | +268.4% | +562.0513 to +1264.5617 | yes: LOSS |
| time over the response line (% of samples) | 0.1541 | 14.78 | +9491.6% | +7.2388 to +22.0115 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 9.7 | +9.700 (native is 0) | +6.0519 to +13.3481 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.500 (native is 0) | +15.4606 to +45.5394 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1115 | 8.588 | −99.2% | −1342.7072 to −869.4228 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05876 | 0.06593 | +12.2% | +0.0007 to +0.0136 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.41 | 1.365 | −3.2% | −0.1474 to +0.0569 | no |
| Omni's own CPU (cores), mean | 0 | 0.01525 | +0.015 (native is 0) | +0.0142 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.38 | −2.1% | −0.1330 to +0.0730 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.5 | 433.6 | −5.8% | −48.5806 to −5.0394 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.02 | 2.126 | +5.2% | −0.1767 to +0.3876 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.93 | 39.88 | −9.2% | −5.9628 to −2.1437 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1453 | 745.6 | −48.7% | −786.0915 to −628.3085 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.041 | −66.0% | −4.4778 to −3.4406 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 151.5 | 0.04167 | −100.0% | −186.7198 to −116.1719 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 689.8 | 0.3 | −100.0% | −816.7958 to −562.2042 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 856.5 | 53.23 | −93.8% | −950.1875 to −656.4542 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.2 | 0 | −100.0% | −18.2771 to −6.1229 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.973 | −0.4% | −0.0775 to +0.0239 | no |
| node-hours | 2.51 | 2.505 | −0.2% | −0.0279 to +0.0175 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 272.2 | +0.5% | +0.0739 to +2.9029 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 271.4 | +0.2% | −0.8283 to +2.1260 | no |
| response time (ms), mean | 260.7 | 103 | −60.5% | −217.2102 to −98.2720 | yes: GAIN |
| response time (ms), 95th percentile | 789.5 | 227.4 | −71.2% | −804.2306 to −319.9504 | yes: GAIN |
| response time (ms), 99th percentile | 1138 | 341.6 | −70.0% | −1134.8304 to −458.7580 | yes: GAIN |
| time over the response line (% of samples) | 14.02 | 0.2453 | −98.3% | −21.2816 to −6.2757 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 0 | −100.0% | −13.3641 to −5.4359 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.9 | +14.900 (native is 0) | +10.7778 to +19.0222 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.18 | 1086 | +11727.4% | +835.1047 to +1318.0453 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05677 | 0.0598 | +5.4% | −0.0015 to +0.0076 | no |
| CPU used (cores), mean | 1.362 | 1.429 | +4.9% | −0.0336 to +0.1675 | no |
| Omni's own CPU (cores), mean | 0 | 0.01247 | +0.012 (native is 0) | +0.0115 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.362 | 1.442 | +5.8% | −0.0202 to +0.1791 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.3 | 453.4 | −6.4% | −74.4751 to +12.7288 | no |
| HPA replicas, mean | 1.989 | 1.982 | −0.4% | −0.1827 to +0.1680 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.4 | 0 | −100.0% | −1.3048 to +0.5048 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 38.93 | 45.05 | +15.7% | +4.3990 to +7.8499 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 742.3 | 1443 | +94.4% | +608.4211 to +793.3789 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.613 | −6.4% | −1.4954 to +0.7216 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 146.3 | +319090.9% | +100.1393 to +192.3607 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 646.7 | +215466.7% | +487.6139 to +805.1861 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 49.98 | 808.2 | +1516.8% | +606.0570 to +910.2846 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.4 | +10.400 (native is 0) | +5.1091 to +15.6909 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*