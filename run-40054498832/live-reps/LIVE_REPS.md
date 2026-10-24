# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.136 | 5.402 |
| node-hours | 2.516 | 2.515 | 2.151 | 2.265 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.3 | 272 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.3 | 244.9 | 253.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 326.2 | 336.7 | 295.1 | 286.2 |
| response time (ms), 95th percentile | 1084 | 1196 | 1131 | 1215 |
| response time (ms), 99th percentile | 1562 | 1787 | 1720 | 1746 |
| time over the response line (% of samples) | 16.78 | 12.62 | 16.78 | 12.41 |
| failed requests (%) | 0 | 0.01418 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.6 | 9 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 34.2 | 41.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 18.32 | 10.34 | 14.83 |
| utilisation (used / allocatable) | 0.05895 | 0.05922 | 0.07006 | 0.0668 |
| CPU used (cores), mean | 1.415 | 1.421 | 1.42 | 1.417 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01614 | 0.01622 |
| CPU used with Omni's own (cores), mean | 1.415 | 1.421 | 1.436 | 1.433 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 469.8 | 412.6 | 429.4 |
| HPA replicas, mean | 1.948 | 2.024 | 2.322 | 2.446 |
| pods started | 0 | 0 | 0.6 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 1.1 | 0.9 |
| pod start wait, mean (s) | 0 | 0 | 0.9 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.28 | 40.71 | 41.37 | 41.56 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 768.7 | 778 | 773.7 | 774.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.485 | 5.04 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 0.3667 | 0.08333 | 0.2458 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.6 | 0.4 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 77.33 | 88.38 | 78.8 | 84.49 |
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
| worker nodes in service, mean | 6 | 5.402 | -10.0% | -1.343 to +0.1483 | no |
| node-hours | 2.515 | 2.265 | -10.0% | -0.5628 to +0.06187 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.4 | +0.0% | -0.9635 to +1.112 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 253.6 | -6.9% | -42.1 to +4.581 | no |
| response time (ms), mean | 336.7 | 286.2 | -15.0% | -97 to -4.009 | yes: GAIN |
| response time (ms), 95th percentile | 1196 | 1215 | +1.6% | -76.4 to +114.1 | no |
| response time (ms), 99th percentile | 1787 | 1746 | -2.3% | -217.2 to +134.7 | no |
| time over the response line (% of samples) | 12.62 | 12.41 | -1.7% | -2.033 to +1.613 | no |
| failed requests (%) | 0.01418 | 0 | -100.0% | -0.04627 to +0.0179 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 9.3 | +8.1% | -1.148 to +2.548 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.1 | +41.1 (native is 0) | +29.29 to +52.91 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.32 | 14.83 | -19.1% | -13.37 to +6.386 | no |
| utilisation (used / allocatable) | 0.05922 | 0.0668 | +12.8% | -0.002618 to +0.01779 | no |
| CPU used (cores), mean | 1.421 | 1.417 | -0.3% | -0.04794 to +0.03979 | no |
| Omni's own CPU (cores), mean | 0 | 0.01622 | +0.0162 (native is 0) | +0.01463 to +0.01781 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.433 | +0.9% | -0.03103 to +0.05532 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.8 | 429.4 | -8.6% | -89.72 to +8.854 | no |
| HPA replicas, mean | 2.024 | 2.446 | +20.8% | +0.1919 to +0.6512 | yes: power given |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.71 | 41.56 | +2.1% | -0.16 to +1.864 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 778 | 774.4 | -0.5% | -19.78 to +12.58 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.04 | -16.0% | -2.1 to +0.1789 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3667 | 0.2458 | -33.0% | -0.4177 to +0.176 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.4 | -12.5% | -1.079 to +0.6793 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.38 | 84.49 | -4.4% | -19.21 to +11.42 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.594e-16 to +7.818e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.515 | -0.0% | -0.004854 to +0.002521 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.3 | +0.1% | -0.8169 to +1.132 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.3 | +0.1% | -0.8169 to +1.132 | no |
| response time (ms), mean | 326.2 | 336.7 | +3.2% | -59.07 to +80.17 | no |
| response time (ms), 95th percentile | 1084 | 1196 | +10.4% | -118.4 to +343.7 | no |
| response time (ms), 99th percentile | 1562 | 1787 | +14.4% | +0.9553 to +450.1 | yes: LOSS |
| time over the response line (% of samples) | 16.78 | 12.62 | -24.8% | -7.498 to -0.8287 | yes: GAIN |
| failed requests (%) | 0 | 0.01418 | +0.0142 (native is 0) | -0.0179 to +0.04627 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.6 | -5.5% | -1.526 to +0.5256 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 18.32 | +67.6% | -7.796 to +22.58 | no |
| utilisation (used / allocatable) | 0.05895 | 0.05922 | +0.5% | -0.00188 to +0.002422 | no |
| CPU used (cores), mean | 1.415 | 1.421 | +0.5% | -0.04513 to +0.05812 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.415 | 1.421 | +0.5% | -0.04513 to +0.05812 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 469.8 | +0.3% | -9.03 to +11.78 | no |
| HPA replicas, mean | 1.948 | 2.024 | +3.9% | -0.04561 to +0.1966 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 40.28 | 40.71 | +1.1% | -0.936 to +1.798 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768.7 | 778 | +1.2% | -18.14 to +36.74 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 0.3667 | +151.4% | -0.3007 to +0.7424 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.6 | +60.0% | -0.7985 to +1.998 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.33 | 88.38 | +14.3% | -14 to +36.11 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.136 | -14.4% | -1.625 to -0.1016 | yes: GAIN |
| node-hours | 2.516 | 2.151 | -14.5% | -0.6848 to -0.04504 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272 | -0.1% | -1.28 to +0.994 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 244.9 | -10.0% | -51.37 to -3.156 | yes: GAIN |
| response time (ms), mean | 326.2 | 295.1 | -9.5% | -60.32 to -1.845 | yes: GAIN |
| response time (ms), 95th percentile | 1084 | 1131 | +4.4% | -91.58 to +186.2 | no |
| response time (ms), 99th percentile | 1562 | 1720 | +10.1% | -39.38 to +355.1 | no |
| time over the response line (% of samples) | 16.78 | 16.78 | -0.0% | -1.19 to +1.187 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | -1.1% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +22.96 to +45.44 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 10.34 | -5.4% | -3.793 to +2.606 | no |
| utilisation (used / allocatable) | 0.05895 | 0.07006 | +18.9% | +0.001249 to +0.02098 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.415 | 1.42 | +0.4% | -0.01474 to +0.02541 | no |
| Omni's own CPU (cores), mean | 0 | 0.01614 | +0.0161 (native is 0) | +0.01508 to +0.0172 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.436 | +1.5% | +0.001249 to +0.0417 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 412.6 | -11.9% | -105.3 to -6.452 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.948 | 2.322 | +19.2% | +0.1438 to +0.6042 | yes: power given |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.09985 to +1.1 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | +0.1198 to +2.08 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.28 | 41.37 | +2.7% | +0.7873 to +1.4 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768.7 | 773.7 | +0.7% | +0.3643 to +9.636 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.485 | -25.2% | -2.803 to -0.2258 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 0.08333 | -42.9% | -0.1471 to +0.02209 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.4 | -60.0% | -1.728 to +0.5285 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.33 | 78.8 | +1.9% | -7.026 to +9.968 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.136 | -14.4% | -1.625 to -0.1016 | yes: GAIN |
| node-hours | 2.515 | 2.151 | -14.5% | -0.6853 to -0.04219 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272 | -0.1% | -2.15 to +1.549 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 244.9 | -10.1% | -51.55 to -3.291 | yes: GAIN |
| response time (ms), mean | 336.7 | 295.1 | -12.4% | -136.6 to +53.36 | no |
| response time (ms), 95th percentile | 1196 | 1131 | -5.5% | -407.7 to +277 | no |
| response time (ms), 99th percentile | 1787 | 1720 | -3.8% | -354.2 to +218.9 | no |
| time over the response line (% of samples) | 12.62 | 16.78 | +33.0% | +0.392 to +7.932 | yes: LOSS |
| failed requests (%) | 0.01418 | 0 | -100.0% | -0.04627 to +0.0179 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 9 | +4.7% | -0.5656 to +1.366 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +22.96 to +45.44 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.32 | 10.34 | -43.6% | -25.6 to +9.627 | no |
| utilisation (used / allocatable) | 0.05922 | 0.07006 | +18.3% | +0.0002909 to +0.02139 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.421 | 1.42 | -0.1% | -0.05471 to +0.05239 | no |
| Omni's own CPU (cores), mean | 0 | 0.01614 | +0.0161 (native is 0) | +0.01508 to +0.0172 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.421 | 1.436 | +1.1% | -0.03825 to +0.06821 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.8 | 412.6 | -12.2% | -109.7 to -4.791 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.024 | 2.322 | +14.7% | +0.04864 to +0.5484 | yes: power given |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.09985 to +1.1 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | +0.1198 to +2.08 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.1887 to +1.611 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.71 | 41.37 | +1.6% | -0.7338 to +2.059 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 778 | 773.7 | -0.6% | -32.37 to +23.77 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.485 | -25.2% | -2.803 to -0.2258 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3667 | 0.08333 | -77.3% | -0.8825 to +0.3159 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 0.4 | -75.0% | -3.673 to +1.273 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.38 | 78.8 | -10.8% | -42.16 to +22.99 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.402 | -10.0% | -1.343 to +0.1483 | no |
| node-hours | 2.516 | 2.265 | -10.0% | -0.5632 to +0.06002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.4 | +0.1% | -0.3983 to +0.8615 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 253.6 | -6.8% | -41.93 to +4.722 | no |
| response time (ms), mean | 326.2 | 286.2 | -12.2% | -71.44 to -8.457 | yes: GAIN |
| response time (ms), 95th percentile | 1084 | 1215 | +12.1% | -82.31 to +345.3 | no |
| response time (ms), 99th percentile | 1562 | 1746 | +11.8% | +9.721 to +358.8 | yes: LOSS |
| time over the response line (% of samples) | 16.78 | 12.41 | -26.1% | -7.55 to -1.197 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.3 | +2.2% | -1.182 to +1.582 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.1 | +41.1 (native is 0) | +29.29 to +52.91 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.93 | 14.83 | +35.7% | -1.907 to +9.71 | no |
| utilisation (used / allocatable) | 0.05895 | 0.0668 | +13.3% | -0.002073 to +0.01778 | no |
| CPU used (cores), mean | 1.415 | 1.417 | +0.2% | -0.02879 to +0.03363 | no |
| Omni's own CPU (cores), mean | 0 | 0.01622 | +0.0162 (native is 0) | +0.01463 to +0.01781 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.433 | +1.3% | -0.01239 to +0.04967 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.5 | 429.4 | -8.3% | -87.39 to +9.272 | no |
| HPA replicas, mean | 1.948 | 2.446 | +25.5% | +0.2961 to +0.698 | yes: power given |
| pods started | 0 | 0.6 | +0.6 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.28 | 41.56 | +3.2% | +0.4824 to +2.084 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768.7 | 774.4 | +0.7% | -6.407 to +17.81 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.04 | -16.0% | -2.1 to +0.1789 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1458 | 0.2458 | +68.6% | -0.1292 to +0.3292 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.4 | +40.0% | -0.3689 to +1.169 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.33 | 84.49 | +9.3% | -3.018 to +17.33 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*