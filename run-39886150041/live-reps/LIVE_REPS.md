# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.269 | 5.057 |
| node-hours | 2.513 | 2.516 | 2.207 | 2.12 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.1 | 271 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271.1 | 248 | 241.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 268.8 | 204.9 | 253.4 | 187.1 |
| response time (ms), 95th percentile | 833.9 | 477.4 | 948.9 | 597.8 |
| response time (ms), 99th percentile | 1207 | 775.2 | 1428 | 1022 |
| time over the response line (% of samples) | 13.59 | 7.387 | 14.41 | 7.844 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 6.8 | 8 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 141 | 116.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 75 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.243 | 13.38 | 10.44 | 13.59 |
| utilisation (used / allocatable) | 0.0571 | 0.05606 | 0.06413 | 0.06698 |
| CPU used (cores), mean | 1.37 | 1.345 | 1.35 | 1.349 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04762 | 0.04937 |
| CPU used with Omni's own (cores), mean | 1.37 | 1.345 | 1.398 | 1.398 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.2 | 492.9 | 443.2 | 431.2 |
| HPA replicas, mean | 1.997 | 2.127 | 2.685 | 2.447 |
| pods started | 0.2 | 0.2 | 1.2 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.5 | 3.1 | 1.2 |
| pod start wait, mean (s) | 0.4 | 0.5 | 1.07 | 0.7 |
| host CPU busy, the real machine under kind (%) | 38.6 | 39.63 | 40.72 | 41.52 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 752.4 | 762.9 | 759.1 | 768.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.635 | 4.222 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.5875 | 0.04583 | 0.7042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | 0.2 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 59.63 | 74.35 | 66.36 | 79.36 |
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
| worker nodes in service, mean | 6 | 5.057 | -15.7% | -1.626 to -0.2609 | yes: GAIN |
| node-hours | 2.516 | 2.12 | -15.7% | -0.6777 to -0.1141 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 | +0.1% | -0.5937 to +0.9257 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 241.6 | -10.9% | -50.56 to -8.441 | yes: GAIN |
| response time (ms), mean | 204.9 | 187.1 | -8.7% | -41.2 to +5.451 | no |
| response time (ms), 95th percentile | 477.4 | 597.8 | +25.2% | -57.97 to +298.8 | no |
| response time (ms), 99th percentile | 775.2 | 1022 | +31.8% | -126.3 to +619 | no |
| time over the response line (% of samples) | 7.387 | 7.844 | +6.2% | -1.628 to +2.542 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.3 | +7.4% | -0.1952 to +1.195 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.8 | +117 (native is 0) | +80.08 to +153.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.38 | 13.59 | +1.6% | -1.438 to +1.858 | no |
| utilisation (used / allocatable) | 0.05606 | 0.06698 | +19.5% | +0.003436 to +0.01842 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.345 | 1.349 | +0.3% | -0.03504 to +0.04179 | no |
| Omni's own CPU (cores), mean | 0 | 0.04937 | +0.0494 (native is 0) | +0.04235 to +0.05639 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.345 | 1.398 | +3.9% | +0.01024 to +0.09525 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.9 | 431.2 | -12.5% | -105.6 to -17.73 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.127 | 2.447 | +15.1% | +0.005858 to +0.6344 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | -0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.5 | 1.2 | +140.0% | -1.824 to +3.224 | no |
| pod start wait, mean (s) | 0.5 | 0.7 | +40.0% | -1.338 to +1.738 | no |
| host CPU busy, the real machine under kind (%) | 39.63 | 41.52 | +4.8% | +1.15 to +2.633 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.9 | 768.2 | +0.7% | -0.08516 to +10.69 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.222 | -29.6% | -3.052 to -0.5045 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5875 | 0.7042 | +19.9% | +0.03378 to +0.1995 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.4 | +27.3% | -0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 74.35 | 79.36 | +6.7% | -1.818 to +11.85 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.062e-15 to +1.733e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.516 | +0.1% | -0.00747 to +0.0118 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.1 | -0.0% | -1.269 to +1.158 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271.1 | -0.0% | -1.269 to +1.158 | no |
| response time (ms), mean | 268.8 | 204.9 | -23.8% | -103.3 to -24.44 | yes: GAIN |
| response time (ms), 95th percentile | 833.9 | 477.4 | -42.7% | -578.3 to -134.5 | yes: GAIN |
| response time (ms), 99th percentile | 1207 | 775.2 | -35.8% | -737.9 to -124.8 | yes: GAIN |
| time over the response line (% of samples) | 13.59 | 7.387 | -45.6% | -11.08 to -1.33 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 6.8 | -6.8% | -1.343 to +0.343 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.243 | 13.38 | +44.7% | +1.647 to +6.62 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0571 | 0.05606 | -1.8% | -0.002622 to +0.0005425 | no |
| CPU used (cores), mean | 1.37 | 1.345 | -1.8% | -0.06292 to +0.01302 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.37 | 1.345 | -1.8% | -0.06292 to +0.01302 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.2 | 492.9 | +2.4% | -8.31 to +31.65 | no |
| HPA replicas, mean | 1.997 | 2.127 | +6.5% | -0.05772 to +0.3174 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | -1.041 to +1.241 | no |
| pod start wait, mean (s) | 0.4 | 0.5 | +25.0% | -1.041 to +1.241 | no |
| host CPU busy, the real machine under kind (%) | 38.6 | 39.63 | +2.6% | +0.6745 to +1.368 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.4 | 762.9 | +1.4% | +3.67 to +17.33 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.5875 | +1181.8% | +0.4634 to +0.6199 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | +175.0% | +0.3545 to +1.046 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.63 | 74.35 | +24.7% | +4.674 to +24.76 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.269 | -12.2% | -1.35 to -0.1127 | yes: GAIN |
| node-hours | 2.513 | 2.207 | -12.2% | -0.5673 to -0.04619 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271 | -0.0% | -1.209 to +0.9833 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 248 | -8.5% | -43.01 to -3.15 | yes: GAIN |
| response time (ms), mean | 268.8 | 253.4 | -5.8% | -32.03 to +1.064 | no |
| response time (ms), 95th percentile | 833.9 | 948.9 | +13.8% | +6.862 to +223.2 | yes: LOSS |
| response time (ms), 99th percentile | 1207 | 1428 | +18.3% | +36.61 to +405.6 | yes: LOSS |
| time over the response line (% of samples) | 13.59 | 14.41 | +6.0% | -0.1066 to +1.744 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 8 | +9.6% | -0.2567 to +1.657 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 141 | +141 (native is 0) | +80.62 to +201.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.243 | 10.44 | +13.0% | -0.7428 to +3.143 | no |
| utilisation (used / allocatable) | 0.0571 | 0.06413 | +12.3% | +0.001259 to +0.01281 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.37 | 1.35 | -1.5% | -0.06165 to +0.02101 | no |
| Omni's own CPU (cores), mean | 0 | 0.04762 | +0.0476 (native is 0) | +0.04184 to +0.0534 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.37 | 1.398 | +2.0% | -0.01626 to +0.07086 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.2 | 443.2 | -7.9% | -70.41 to -5.758 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.685 | +34.5% | +0.2715 to +1.105 | yes: power given |
| pods started | 0.2 | 1.2 | +500.0% | -0.2158 to +2.216 | no |
| pod start wait, total (s) | 0.4 | 3.1 | +675.0% | -1.276 to +6.676 | no |
| pod start wait, mean (s) | 0.4 | 1.07 | +167.5% | -0.4484 to +1.788 | no |
| host CPU busy, the real machine under kind (%) | 38.6 | 40.72 | +5.5% | +1.396 to +2.829 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.4 | 759.1 | +0.9% | -1.737 to +15.14 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.635 | -22.7% | -2.489 to -0.24 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04583 | +0.0% | -0.03974 to +0.03974 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.2 | -50.0% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.63 | 66.36 | +11.3% | -2.301 to +15.77 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.269 | -12.2% | -1.35 to -0.1127 | yes: GAIN |
| node-hours | 2.516 | 2.207 | -12.3% | -0.5661 to -0.05173 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271 | -0.0% | -0.9056 to +0.7916 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 248 | -8.5% | -42.24 to -3.807 | yes: GAIN |
| response time (ms), mean | 204.9 | 253.4 | +23.6% | -3.298 to +100.1 | no |
| response time (ms), 95th percentile | 477.4 | 948.9 | +98.8% | +164.4 to +778.6 | yes: LOSS |
| response time (ms), 99th percentile | 775.2 | 1428 | +84.2% | +204.9 to +1100 | yes: LOSS |
| time over the response line (% of samples) | 7.387 | 14.41 | +95.1% | +1.795 to +12.25 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 8 | +17.6% | -0.4792 to +2.879 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 141 | +141 (native is 0) | +80.62 to +201.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.38 | 10.44 | -21.9% | -4.53 to -1.337 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05606 | 0.06413 | +14.4% | +0.001686 to +0.01446 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.345 | 1.35 | +0.3% | -0.01828 to +0.02754 | no |
| Omni's own CPU (cores), mean | 0 | 0.04762 | +0.0476 (native is 0) | +0.04184 to +0.0534 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.345 | 1.398 | +3.9% | +0.02481 to +0.07968 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.9 | 443.2 | -10.1% | -92.73 to -6.78 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.127 | 2.685 | +26.2% | +0.2246 to +0.892 | yes: power given |
| pods started | 0.2 | 1.2 | +500.0% | -0.3903 to +2.39 | no |
| pod start wait, total (s) | 0.5 | 3.1 | +520.0% | -1.491 to +6.691 | no |
| pod start wait, mean (s) | 0.5 | 1.07 | +114.0% | -0.4759 to +1.616 | no |
| host CPU busy, the real machine under kind (%) | 39.63 | 40.72 | +2.8% | +0.5177 to +1.665 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 762.9 | 759.1 | -0.5% | -10.97 to +3.367 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.635 | -22.7% | -2.489 to -0.24 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5875 | 0.04583 | -92.2% | -0.6211 to -0.4622 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.2 | -81.8% | -1.306 to -0.494 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 74.35 | 66.36 | -10.7% | -16.87 to +0.9032 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.057 | -15.7% | -1.626 to -0.2609 | yes: GAIN |
| node-hours | 2.513 | 2.12 | -15.7% | -0.6827 to -0.1048 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 | +0.0% | -0.9643 to +1.185 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 241.6 | -10.9% | -51.56 to -7.557 | yes: GAIN |
| response time (ms), mean | 268.8 | 187.1 | -30.4% | -112.4 to -51.18 | yes: GAIN |
| response time (ms), 95th percentile | 833.9 | 597.8 | -28.3% | -380 to -92.02 | yes: GAIN |
| response time (ms), 99th percentile | 1207 | 1022 | -15.3% | -425.3 to +55.29 | no |
| time over the response line (% of samples) | 13.59 | 7.844 | -42.3% | -10.01 to -1.482 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.3 | +0.0% | -0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.8 | +117 (native is 0) | +80.08 to +153.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.243 | 13.59 | +47.0% | +1.959 to +6.728 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0571 | 0.06698 | +17.3% | +0.002338 to +0.01744 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.37 | 1.349 | -1.6% | -0.06696 to +0.02381 | no |
| Omni's own CPU (cores), mean | 0 | 0.04937 | +0.0494 (native is 0) | +0.04235 to +0.05639 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.37 | 1.398 | +2.0% | -0.02298 to +0.07857 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.2 | 431.2 | -10.4% | -88.63 to -11.35 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.447 | +22.5% | +0.0883 to +0.8117 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.4 | 1.2 | +200.0% | -0.845 to +2.445 | no |
| pod start wait, mean (s) | 0.4 | 0.7 | +75.0% | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 38.6 | 41.52 | +7.5% | +2.09 to +3.736 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 752.4 | 768.2 | +2.1% | +5.25 to +26.35 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.222 | -29.6% | -3.052 to -0.5045 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.7042 | +1436.4% | +0.5708 to +0.7459 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 | +250.0% | +0.6628 to +1.337 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 59.63 | 79.36 | +33.1% | +4.92 to +34.55 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*