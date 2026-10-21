# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.33 | 5.949 |
| node-hours | 2.513 | 2.515 | 2.234 | 2.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.9 | 272.5 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.9 | 251.4 | 269.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 378.6 | 142.3 | 336.1 | 107.1 |
| response time (ms), 95th percentile | 1359 | 246.1 | 1354 | 239.2 |
| response time (ms), 99th percentile | 2000 | 359.1 | 1911 | 347.6 |
| time over the response line (% of samples) | 18.52 | 0.2091 | 18.23 | 0.2095 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | 10.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 37 | 12.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.4 | 1171 | 9.685 | 1199 |
| utilisation (used / allocatable) | 0.06032 | 0.05909 | 0.06682 | 0.05897 |
| CPU used (cores), mean | 1.448 | 1.418 | 1.432 | 1.405 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01569 | 0.01202 |
| CPU used with Omni's own (cores), mean | 1.448 | 1.418 | 1.448 | 1.417 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 460 | 427.1 | 460.4 |
| HPA replicas, mean | 1.938 | 1.99 | 2.184 | 2.009 |
| pods started | 0 | 0 | 0.2 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 0.3 | 0.4 |
| pod start wait, mean (s) | 0 | 0 | 0.3 | 0.2 |
| host CPU busy, the real machine under kind (%) | 41.39 | 44.62 | 42.06 | 44.8 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 785 | 1452 | 786.6 | 1455 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.74 | 5.161 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 142.3 | 0.0625 | 151.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 629.6 | 0.3 | 737.6 |
| queue: job turnaround, submitted to done, mean (s) | 91.83 | 854.2 | 93.2 | 858 |
| queue: jobs unfinished at the window's end | 0 | 12 | 0 | 11.9 |

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
| worker nodes in service, mean | 6 | 5.949 | -0.8% | -0.165 to +0.06385 | no |
| node-hours | 2.515 | 2.492 | -0.9% | -0.07291 to +0.02552 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.3 | -0.2% | -1.625 to +0.4599 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 269.8 | -0.8% | -6.001 to +1.657 | no |
| response time (ms), mean | 142.3 | 107.1 | -24.8% | -42.21 to -28.24 | yes: GAIN |
| response time (ms), 95th percentile | 246.1 | 239.2 | -2.8% | -19.09 to +5.36 | no |
| response time (ms), 99th percentile | 359.1 | 347.6 | -3.2% | -38.17 to +15.21 | no |
| time over the response line (% of samples) | 0.2091 | 0.2095 | +0.2% | -0.1199 to +0.1207 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 | +12.2 (native is 0) | +9.528 to +14.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1171 | 1199 | +2.5% | -9.491 to +66.94 | no |
| utilisation (used / allocatable) | 0.05909 | 0.05897 | -0.2% | -0.00177 to +0.001528 | no |
| CPU used (cores), mean | 1.418 | 1.405 | -0.9% | -0.04639 to +0.02026 | no |
| Omni's own CPU (cores), mean | 0 | 0.01202 | +0.012 (native is 0) | +0.01088 to +0.01316 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.417 | -0.1% | -0.03437 to +0.03228 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460 | 460.4 | +0.1% | -10.96 to +11.66 | no |
| HPA replicas, mean | 1.99 | 2.009 | +0.9% | -0.1006 to +0.1378 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.62 | 44.8 | +0.4% | -0.8769 to +1.232 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1452 | 1455 | +0.2% | -21.44 to +27.04 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.321 | -28.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 142.3 | 151.7 | +6.6% | -36.34 to +55.23 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 629.6 | 737.6 | +17.2% | -44.64 to +260.6 | no |
| queue: job turnaround, submitted to done, mean (s) | 854.2 | 858 | +0.4% | -35.39 to +42.99 | no |
| queue: jobs unfinished at the window's end | 12 | 11.9 | -0.8% | -1.137 to +0.9366 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.025e-15 to +1.166e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.516 | +0.1% | -0.003763 to +0.009763 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.9 | -0.1% | -2.557 to +1.8 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.9 | -0.1% | -2.557 to +1.8 | no |
| response time (ms), mean | 378.6 | 142.3 | -62.4% | -374.1 to -98.52 | yes: GAIN |
| response time (ms), 95th percentile | 1359 | 246.1 | -81.9% | -1769 to -457.1 | yes: GAIN |
| response time (ms), 99th percentile | 2000 | 359.1 | -82.0% | -2608 to -674.2 | yes: GAIN |
| time over the response line (% of samples) | 18.52 | 0.2091 | -98.9% | -29 to -7.621 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | -100.0% | -13.66 to -4.942 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.4 | 1171 | +10168.0% | +856.3 to +1462 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06032 | 0.05909 | -2.0% | -0.007088 to +0.004627 | no |
| CPU used (cores), mean | 1.448 | 1.418 | -2.0% | -0.1701 to +0.111 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.448 | 1.418 | -2.0% | -0.1701 to +0.111 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 460 | -0.5% | -45.81 to +41.44 | no |
| HPA replicas, mean | 1.938 | 1.99 | +2.7% | -0.07396 to +0.1791 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 44.62 | +7.8% | +0.04921 to +6.422 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 785 | 1452 | +84.9% | +553.8 to +779.8 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 142.3 | +341310.0% | +95.51 to +188.9 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 629.6 | +209766.7% | +469.5 to +789.1 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 91.83 | 854.2 | +830.3% | +613.5 to +911.3 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12 | +12 (native is 0) | +5.453 to +18.55 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.33 | -11.2% | -1.292 to -0.04745 | yes: GAIN |
| node-hours | 2.513 | 2.234 | -11.1% | -0.5399 to -0.01618 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.5 | +0.1% | -0.7001 to +1.01 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 251.4 | -7.7% | -41.01 to -0.8658 | yes: GAIN |
| response time (ms), mean | 378.6 | 336.1 | -11.2% | -60.88 to -24.12 | yes: GAIN |
| response time (ms), 95th percentile | 1359 | 1354 | -0.3% | -84.4 to +75 | no |
| response time (ms), 99th percentile | 2000 | 1911 | -4.4% | -217 to +39.9 | no |
| time over the response line (% of samples) | 18.52 | 18.23 | -1.6% | -1.181 to +0.5994 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10.1 | +8.6% | -0.07931 to +1.679 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 | +37 (native is 0) | +13.29 to +60.71 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.4 | 9.685 | -15.1% | -4.13 to +0.6963 | no |
| utilisation (used / allocatable) | 0.06032 | 0.06682 | +10.8% | +0.0008105 to +0.01218 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.448 | 1.432 | -1.1% | -0.05282 to +0.02116 | no |
| Omni's own CPU (cores), mean | 0 | 0.01569 | +0.0157 (native is 0) | +0.01437 to +0.01701 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.448 | -0.0% | -0.03685 to +0.03657 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 427.1 | -7.6% | -66.29 to -4.061 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.938 | 2.184 | +12.7% | -0.03776 to +0.5301 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 42.06 | +1.6% | +0.3129 to +1.023 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 785 | 786.6 | +0.2% | -4.223 to +7.423 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.74 | -21.0% | -2.409 to -0.1103 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.0625 | +50.0% | -0.01952 to +0.06119 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | +0.0% | -0.584 to +0.584 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.83 | 93.2 | +1.5% | -3.489 to +6.239 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.33 | -11.2% | -1.292 to -0.04745 | yes: GAIN |
| node-hours | 2.515 | 2.234 | -11.2% | -0.5418 to -0.02031 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.5 | +0.2% | -1.871 to +2.938 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 251.4 | -7.6% | -42.36 to +1.242 | no |
| response time (ms), mean | 142.3 | 336.1 | +136.2% | +63.63 to +324 | yes: LOSS |
| response time (ms), 95th percentile | 246.1 | 1354 | +450.4% | +473.6 to +1743 | yes: LOSS |
| response time (ms), 99th percentile | 359.1 | 1911 | +432.3% | +686.8 to +2418 | yes: LOSS |
| time over the response line (% of samples) | 0.2091 | 18.23 | +8616.7% | +7.823 to +28.21 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.1 | +10.1 (native is 0) | +5.937 to +14.26 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 | +37 (native is 0) | +13.29 to +60.71 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1171 | 9.685 | -99.2% | -1465 to -856.8 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05909 | 0.06682 | +13.1% | +0.005496 to +0.009956 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.418 | 1.432 | +1.0% | -0.1504 to +0.1778 | no |
| Omni's own CPU (cores), mean | 0 | 0.01569 | +0.0157 (native is 0) | +0.01437 to +0.01701 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.448 | +2.1% | -0.134 to +0.1928 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460 | 427.1 | -7.2% | -49.5 to -16.48 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.99 | 2.184 | +9.7% | -0.1329 to +0.5201 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 44.62 | 42.06 | -5.8% | -5.693 to +0.5579 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1452 | 786.6 | -45.8% | -778.1 to -552.3 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.837 | -52.7% | -11.98 to +5.653 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 142.3 | 0.0625 | -100.0% | -188.9 to -95.51 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 629.6 | 0.3 | -100.0% | -789 to -469.6 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 854.2 | 93.2 | -89.1% | -908.9 to -613.1 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12 | 0 | -100.0% | -18.55 to -5.453 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.949 | -0.8% | -0.165 to +0.06385 | no |
| node-hours | 2.513 | 2.492 | -0.8% | -0.07068 to +0.02929 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.3 | -0.4% | -2.612 to +0.6902 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 269.8 | -0.9% | -6.18 to +1.079 | no |
| response time (ms), mean | 378.6 | 107.1 | -71.7% | -414.2 to -128.9 | yes: GAIN |
| response time (ms), 95th percentile | 1359 | 239.2 | -82.4% | -1774 to -465.3 | yes: GAIN |
| response time (ms), 99th percentile | 2000 | 347.6 | -82.6% | -2613 to -691.8 | yes: GAIN |
| time over the response line (% of samples) | 18.52 | 0.2095 | -98.9% | -28.98 to -7.632 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | -100.0% | -13.66 to -4.942 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 | +12.2 (native is 0) | +9.528 to +14.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.4 | 1199 | +10420.0% | +894.7 to +1481 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06032 | 0.05897 | -2.2% | -0.007505 to +0.004801 | no |
| CPU used (cores), mean | 1.448 | 1.405 | -2.9% | -0.1819 to +0.0967 | no |
| Omni's own CPU (cores), mean | 0 | 0.01202 | +0.012 (native is 0) | +0.01088 to +0.01316 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.417 | -2.1% | -0.1689 to +0.1077 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 460.4 | -0.4% | -48.4 to +44.74 | no |
| HPA replicas, mean | 1.938 | 2.009 | +3.7% | -0.05868 to +0.201 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 41.39 | 44.8 | +8.2% | +0.592 to +6.234 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 785 | 1455 | +85.3% | +575.9 to +763.3 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.161 | -14.0% | -11.5 to +9.825 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 151.7 | +363980.0% | +108 to +195.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 737.6 | +245766.7% | +565.5 to +909.1 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 91.83 | 858 | +834.4% | +626.5 to +905.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.9 | +11.9 (native is 0) | +5.93 to +17.87 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*