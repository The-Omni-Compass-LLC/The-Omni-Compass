# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.95 | 5.975 |
| node-hours | 2.509 | 2.518 | 2.073 | 2.504 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.1 | 272.3 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 272.1 | 239.3 | 271 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 355.1 | 131.2 | 325.7 | 98.8 |
| response time (ms), 95th percentile | 1283 | 234.3 | 1372 | 221.1 |
| response time (ms), 99th percentile | 1874 | 345.6 | 2010 | 332.5 |
| time over the response line (% of samples) | 17.73 | 0.2311 | 17.38 | 0.2762 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.1 | 9 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 41.3 | 12.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 66.67 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.927 | 1120 | 10.51 | 1127 |
| utilisation (used / allocatable) | 0.05989 | 0.05873 | 0.07329 | 0.05904 |
| CPU used (cores), mean | 1.437 | 1.409 | 1.43 | 1.411 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01829 | 0.01219 |
| CPU used with Omni's own (cores), mean | 1.437 | 1.409 | 1.448 | 1.424 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.7 | 460.5 | 401.2 | 458.8 |
| HPA replicas, mean | 2.016 | 1.962 | 2.054 | 2.022 |
| pods started | 0 | 0.1 | 0.2 | 0.3 |
| pod start wait, total (s) | 0 | 0.3 | 0.2 | 0.7 |
| pod start wait, mean (s) | 0 | 0.3 | 0.2 | 0.7 |
| host CPU busy, the real machine under kind (%) | 40.94 | 44.04 | 41.98 | 44.37 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 778.8 | 1421 | 783.4 | 1421 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.226 | 5.626 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 171.5 | 0.0625 | 175.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 798 | 0.4 | 763.9 |
| queue: job turnaround, submitted to done, mean (s) | 85.79 | 799.3 | 89.12 | 814.5 |
| queue: jobs unfinished at the window's end | 0 | 9.4 | 0 | 10.7 |

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
| worker nodes in service, mean | 6 | 5.975 | -0.4% | -0.07097 to +0.02099 | no |
| node-hours | 2.518 | 2.504 | -0.6% | -0.03147 to +0.00247 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.8 | -0.1% | -1.055 to +0.5212 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271 | -0.4% | -2.319 to +0.2108 | no |
| response time (ms), mean | 131.2 | 98.8 | -24.7% | -40.03 to -24.85 | yes: GAIN |
| response time (ms), 95th percentile | 234.3 | 221.1 | -5.6% | -30.47 to +4.098 | no |
| response time (ms), 99th percentile | 345.6 | 332.5 | -3.8% | -40.82 to +14.73 | no |
| time over the response line (% of samples) | 0.2311 | 0.2762 | +19.5% | -0.06965 to +0.1597 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.5 (native is 0) | +10.84 to +14.16 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1120 | 1127 | +0.6% | -49.39 to +63.74 | no |
| utilisation (used / allocatable) | 0.05873 | 0.05904 | +0.5% | -0.0005713 to +0.001194 | no |
| CPU used (cores), mean | 1.409 | 1.411 | +0.1% | -0.01835 to +0.02219 | no |
| Omni's own CPU (cores), mean | 0 | 0.01219 | +0.0122 (native is 0) | +0.01113 to +0.01325 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.424 | +1.0% | -0.006474 to +0.03469 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.5 | 458.8 | -0.4% | -7.894 to +4.534 | no |
| HPA replicas, mean | 1.962 | 2.022 | +3.1% | -0.0544 to +0.1758 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.3 | 0.7 | +133.3% | -0.7778 to +1.578 | no |
| pod start wait, mean (s) | 0.3 | 0.7 | +133.3% | -0.7778 to +1.578 | no |
| host CPU busy, the real machine under kind (%) | 44.04 | 44.37 | +0.7% | -0.232 to +0.8916 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1421 | 1421 | -0.0% | -11.26 to +10.86 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.626 | -6.2% | -1.428 to +0.6795 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 171.5 | 175.4 | +2.2% | -36.34 to +44.02 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 798 | 763.9 | -4.3% | -213.2 to +145 | no |
| queue: job turnaround, submitted to done, mean (s) | 799.3 | 814.5 | +1.9% | -37.28 to +67.57 | no |
| queue: jobs unfinished at the window's end | 9.4 | 10.7 | +13.8% | +0.1295 to +2.471 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.51e-15 to -1.043e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.509 | 2.518 | +0.4% | +0.004401 to +0.01493 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.1 | +0.1% | -1.59 to +2.274 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 272.1 | +0.1% | -1.59 to +2.274 | no |
| response time (ms), mean | 355.1 | 131.2 | -63.0% | -358.6 to -89.14 | yes: GAIN |
| response time (ms), 95th percentile | 1283 | 234.3 | -81.7% | -1703 to -394.1 | yes: GAIN |
| response time (ms), 99th percentile | 1874 | 345.6 | -81.6% | -2455 to -601.6 | yes: GAIN |
| time over the response line (% of samples) | 17.73 | 0.2311 | -98.7% | -28.07 to -6.932 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.1 | -98.9% | -13.38 to -3.817 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.927 | 1120 | +11180.9% | +839.6 to +1380 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05989 | 0.05873 | -1.9% | -0.007649 to +0.005315 | no |
| CPU used (cores), mean | 1.437 | 1.409 | -1.9% | -0.1836 to +0.1276 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.437 | 1.409 | -1.9% | -0.1836 to +0.1276 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.7 | 460.5 | -0.7% | -52.54 to +46.06 | no |
| HPA replicas, mean | 2.016 | 1.962 | -2.7% | -0.1803 to +0.07176 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 40.94 | 44.04 | +7.6% | -0.3056 to +6.507 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 778.8 | 1421 | +82.5% | +567.3 to +717.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 171.5 | +686083.3% | +109.8 to +233.3 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 798 | +797900.0% | +545.5 to +1050 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 85.79 | 799.3 | +831.8% | +593.2 to +833.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.4 | +9.4 (native is 0) | +3.509 to +15.29 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.95 | -17.5% | -1.883 to -0.2167 | yes: GAIN |
| node-hours | 2.509 | 2.073 | -17.4% | -0.7854 to -0.08612 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.3 | +0.2% | -0.2583 to +1.32 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 239.3 | -11.9% | -58.82 to -6.027 | yes: GAIN |
| response time (ms), mean | 355.1 | 325.7 | -8.3% | -49.76 to -8.998 | yes: GAIN |
| response time (ms), 95th percentile | 1283 | 1372 | +6.9% | -16.03 to +194 | no |
| response time (ms), 99th percentile | 1874 | 2010 | +7.3% | -30.29 to +302.3 | no |
| time over the response line (% of samples) | 17.73 | 17.38 | -2.0% | -1.072 to +0.3673 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9 | +3.4% | -0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.3 | +41.3 (native is 0) | +25.47 to +57.13 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.927 | 10.51 | +5.9% | -0.6523 to +1.819 | no |
| utilisation (used / allocatable) | 0.05989 | 0.07329 | +22.4% | +0.0031 to +0.02368 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.437 | 1.43 | -0.5% | -0.04432 to +0.02979 | no |
| Omni's own CPU (cores), mean | 0 | 0.01829 | +0.0183 (native is 0) | +0.01554 to +0.02104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.437 | 1.448 | +0.8% | -0.02628 to +0.04833 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.7 | 401.2 | -13.5% | -110.6 to -14.36 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.054 | +1.9% | -0.1558 to +0.2311 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 40.94 | 41.98 | +2.5% | +0.6208 to +1.459 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 778.8 | 783.4 | +0.6% | +0.3857 to +8.814 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.226 | -29.6% | -3.08 to -0.4672 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.0625 | +150.0% | -0.01004 to +0.08504 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 | +300.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.79 | 89.12 | +3.9% | -0.08257 to +6.758 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.95 | -17.5% | -1.883 to -0.2167 | yes: GAIN |
| node-hours | 2.518 | 2.073 | -17.7% | -0.7922 to -0.09861 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.3 | +0.1% | -2.045 to +2.422 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 239.3 | -12.0% | -60.83 to -4.705 | yes: GAIN |
| response time (ms), mean | 131.2 | 325.7 | +148.2% | +72.94 to +316.1 | yes: LOSS |
| response time (ms), 95th percentile | 234.3 | 1372 | +485.5% | +499 to +1776 | yes: LOSS |
| response time (ms), 99th percentile | 345.6 | 2010 | +481.6% | +732.7 to +2596 | yes: LOSS |
| time over the response line (% of samples) | 0.2311 | 17.38 | +7419.5% | +7.084 to +27.21 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 9 | +8900.0% | +4.446 to +13.35 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.3 | +41.3 (native is 0) | +25.47 to +57.13 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1120 | 10.51 | -99.1% | -1379 to -839.1 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05873 | 0.07329 | +24.8% | +0.009098 to +0.02002 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.409 | 1.43 | +1.5% | -0.1554 to +0.1969 | no |
| Omni's own CPU (cores), mean | 0 | 0.01829 | +0.0183 (native is 0) | +0.01554 to +0.02104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.448 | +2.8% | -0.1382 to +0.2162 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.5 | 401.2 | -12.9% | -76.05 to -42.43 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.962 | 2.054 | +4.7% | -0.05603 to +0.2398 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.3 | 0.2 | -33.3% | -0.8872 to +0.6872 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | -33.3% | -0.8872 to +0.6872 | no |
| host CPU busy, the real machine under kind (%) | 44.04 | 41.98 | -4.7% | -5.519 to +1.398 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1421 | 783.4 | -44.9% | -711.5 to -564.3 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.129 | -64.5% | -4.112 to -3.629 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 171.5 | 0.0625 | -100.0% | -233.2 to -109.7 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 798 | 0.4 | -99.9% | -1050 to -545.3 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 799.3 | 89.12 | -88.9% | -828.8 to -591.6 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.4 | 0 | -100.0% | -15.29 to -3.509 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.975 | -0.4% | -0.07097 to +0.02099 | no |
| node-hours | 2.509 | 2.504 | -0.2% | -0.02212 to +0.01245 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.8 | +0.0% | -2.046 to +2.197 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271 | -0.3% | -2.609 to +1.185 | no |
| response time (ms), mean | 355.1 | 98.8 | -72.2% | -396.8 to -115.9 | yes: GAIN |
| response time (ms), 95th percentile | 1283 | 221.1 | -82.8% | -1716 to -407.9 | yes: GAIN |
| response time (ms), 99th percentile | 1874 | 332.5 | -82.3% | -2462 to -620.8 | yes: GAIN |
| time over the response line (% of samples) | 17.73 | 0.2762 | -98.4% | -27.98 to -6.933 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.2 | -97.7% | -13.21 to -3.788 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.5 (native is 0) | +10.84 to +14.16 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.927 | 1127 | +11253.2% | +818.3 to +1416 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05989 | 0.05904 | -1.4% | -0.007349 to +0.005637 | no |
| CPU used (cores), mean | 1.437 | 1.411 | -1.8% | -0.1779 to +0.1257 | no |
| Omni's own CPU (cores), mean | 0 | 0.01219 | +0.0122 (native is 0) | +0.01113 to +0.01325 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.437 | 1.424 | -1.0% | -0.1648 to +0.137 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.7 | 458.8 | -1.1% | -53.93 to +44.09 | no |
| HPA replicas, mean | 2.016 | 2.022 | +0.3% | -0.1816 to +0.1945 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.7 (native is 0) | -0.1294 to +1.529 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.7 (native is 0) | -0.1294 to +1.529 | no |
| host CPU busy, the real machine under kind (%) | 40.94 | 44.37 | +8.4% | +0.1216 to +6.739 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 778.8 | 1421 | +82.5% | +562.5 to +722.1 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.626 | -6.2% | -1.428 to +0.6795 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 175.4 | +701433.3% | +125.7 to +225.1 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 763.9 | +763800.0% | +530 to +997.6 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 85.79 | 814.5 | +849.4% | +579.6 to +877.8 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.7 | +10.7 (native is 0) | +4.049 to +17.35 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*