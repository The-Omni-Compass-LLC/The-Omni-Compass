# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.5 | 11.46 |
| node-hours | 5.02 | 5.029 | 4.818 | 4.804 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 528 | 527.2 | 529 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 528 | 511.5 | 512.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 855.6 | 1102 | 811.7 | 1128 |
| response time (ms), 95th percentile | 3578 | 4941 | 3606 | 5221 |
| response time (ms), 99th percentile | 4824 | 6491 | 4845 | 6840 |
| time over the response line (% of samples) | 28.97 | 33.46 | 29.29 | 35.06 |
| failed requests (%) | 0.05833 | 0.5532 | 0.06349 | 0.7251 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 17.9 | 15 | 18.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 60 | 33.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.43 | 47.96 | 31.37 | 39.17 |
| utilisation (used / allocatable) | 0.03803 | 0.03755 | 0.03856 | 0.04074 |
| CPU used (cores), mean | 1.825 | 1.802 | 1.763 | 1.872 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01245 | 0.01056 |
| CPU used with Omni's own (cores), mean | 1.825 | 1.802 | 1.775 | 1.882 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 702.7 | 711 | 702.1 | 660.4 |
| HPA replicas, mean | 4.008 | 4.047 | 4.663 | 4.518 |
| pods started | 0 | 0 | 1.5 | 1.7 |
| pod start wait, total (s) | 0 | 0 | 2.4 | 6 |
| pod start wait, mean (s) | 0 | 0 | 1.3 | 3.05 |
| host CPU busy, the real machine under kind (%) | 55.79 | 62.86 | 57.12 | 65.28 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 950.2 | 1087 | 962.7 | 1125 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 11.17 | 11.12 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 4.758 | 0.1708 | 8.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.9 | 0.8 | 32.2 |
| queue: job turnaround, submitted to done, mean (s) | 255.1 | 389.3 | 263.6 | 430 |
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
| worker nodes in service, mean | 12 | 11.46 | -4.5% | -1.438 to +0.3667 | no |
| node-hours | 5.029 | 4.804 | -4.5% | -0.6066 to +0.1574 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 529 | +0.2% | -2.074 to +3.978 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 512.1 | -3.0% | -45.46 to +13.68 | no |
| response time (ms), mean | 1102 | 1128 | +2.4% | -56 to +109 | no |
| response time (ms), 95th percentile | 4941 | 5221 | +5.7% | -293.6 to +855 | no |
| response time (ms), 99th percentile | 6491 | 6840 | +5.4% | -198.1 to +896.2 | no |
| time over the response line (% of samples) | 33.46 | 35.06 | +4.8% | -0.837 to +4.054 | no |
| failed requests (%) | 0.5532 | 0.7251 | +31.1% | -0.2183 to +0.5621 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.9 | 18.6 | +3.9% | -0.05776 to +1.458 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.7 | +33.7 (native is 0) | +28.6 to +38.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 47.96 | 39.17 | -18.3% | -37.93 to +20.36 | no |
| utilisation (used / allocatable) | 0.03755 | 0.04074 | +8.5% | -0.0001392 to +0.006523 | no |
| CPU used (cores), mean | 1.802 | 1.872 | +3.8% | -0.06671 to +0.2054 | no |
| Omni's own CPU (cores), mean | 0 | 0.01056 | +0.0106 (native is 0) | +0.009723 to +0.0114 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.802 | 1.882 | +4.4% | -0.05648 to +0.2163 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711 | 660.4 | -7.1% | -100.3 to -1.055 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.047 | 4.518 | +11.6% | +0.2276 to +0.715 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +1.111 to +2.289 | yes: power given |
| pod start wait, total (s) | 0 | 6 | +6 (native is 0) | -0.8941 to +12.89 | no |
| pod start wait, mean (s) | 0 | 3.05 | +3.05 (native is 0) | -0.3616 to +6.462 | no |
| host CPU busy, the real machine under kind (%) | 62.86 | 65.28 | +3.9% | +1.057 to +3.794 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1087 | 1125 | +3.5% | +13.52 to +63.48 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.12 | -7.3% | -2.334 to +0.5747 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 4.758 | 8.7 | +82.8% | -2.202 to +10.09 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 32.2 | +1594.7% | -37.99 to +98.59 | no |
| queue: job turnaround, submitted to done, mean (s) | 389.3 | 430 | +10.4% | +12.76 to +68.55 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | -0.0% | -7.045e-15 to -6.006e-17 | EVEN, the same (under one part in a million) |
| node-hours | 5.02 | 5.029 | +0.2% | -0.01111 to +0.02911 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 528 | +0.2% | -1.629 to +3.308 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 528 | +0.2% | -1.629 to +3.308 | no |
| response time (ms), mean | 855.6 | 1102 | +28.8% | +145.7 to +347 | yes: LOSS |
| response time (ms), 95th percentile | 3578 | 4941 | +38.1% | +765 to +1960 | yes: LOSS |
| response time (ms), 99th percentile | 4824 | 6491 | +34.6% | +950.2 to +2384 | yes: LOSS |
| time over the response line (% of samples) | 28.97 | 33.46 | +15.5% | +0.591 to +8.387 | yes: LOSS |
| failed requests (%) | 0.05833 | 0.5532 | +848.3% | -0.2936 to +1.283 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 17.9 | +27.0% | +1.99 to +5.61 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.43 | 47.96 | +123.7% | -5.298 to +58.35 | no |
| utilisation (used / allocatable) | 0.03803 | 0.03755 | -1.3% | -0.002728 to +0.001765 | no |
| CPU used (cores), mean | 1.825 | 1.802 | -1.3% | -0.1309 to +0.08473 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.825 | 1.802 | -1.3% | -0.1309 to +0.08473 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 702.7 | 711 | +1.2% | -29.89 to +46.63 | no |
| HPA replicas, mean | 4.008 | 4.047 | +1.0% | -0.1836 to +0.2616 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 55.79 | 62.86 | +12.7% | +5.708 to +8.427 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 950.2 | 1087 | +14.4% | +91.81 to +181.4 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 4.758 | +5910.5% | -0.1027 to +9.461 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.9 | +216.7% | +0.5422 to +2.058 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 255.1 | 389.3 | +52.6% | +89.32 to +179.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.5 | -4.2% | -1.602 to +0.5988 | no |
| node-hours | 5.02 | 4.818 | -4.0% | -0.6649 to +0.2614 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 527.2 | +0.0% | -1.958 to +2.052 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 511.5 | -3.0% | -50.64 to +19.37 | no |
| response time (ms), mean | 855.6 | 811.7 | -5.1% | -80.53 to -7.278 | yes: GAIN |
| response time (ms), 95th percentile | 3578 | 3606 | +0.8% | -131 to +187.5 | no |
| response time (ms), 99th percentile | 4824 | 4845 | +0.4% | -284.9 to +326.8 | no |
| time over the response line (% of samples) | 28.97 | 29.29 | +1.1% | -0.9035 to +1.554 | no |
| failed requests (%) | 0.05833 | 0.06349 | +8.8% | -0.00651 to +0.01683 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 15 | +6.4% | -1.297 to +3.097 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60 | +60 (native is 0) | +22.36 to +97.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.43 | 31.37 | +46.4% | -5.358 to +25.23 | no |
| utilisation (used / allocatable) | 0.03803 | 0.03856 | +1.4% | -0.003264 to +0.004327 | no |
| CPU used (cores), mean | 1.825 | 1.763 | -3.4% | -0.1282 to +0.002785 | no |
| Omni's own CPU (cores), mean | 0 | 0.01245 | +0.0124 (native is 0) | +0.01185 to +0.01305 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.825 | 1.775 | -2.8% | -0.1156 to +0.015 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 702.7 | 702.1 | -0.1% | -51.31 to +50.08 | no |
| HPA replicas, mean | 4.008 | 4.663 | +16.4% | +0.3396 to +0.9715 | yes: power given |
| pods started | 0 | 1.5 | +1.5 (native is 0) | +0.8921 to +2.108 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.4 (native is 0) | +1.222 to +3.578 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.3 (native is 0) | +0.6874 to +1.913 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.79 | 57.12 | +2.4% | +0.513 to +2.152 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 950.2 | 962.7 | +1.3% | -0.8194 to +25.82 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 11.17 | -6.9% | -2.621 to +0.9639 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.1708 | +115.8% | +0.007601 to +0.1757 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 255.1 | 263.6 | +3.4% | -4.37 to +21.49 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.5 | -4.2% | -1.602 to +0.5988 | no |
| node-hours | 5.029 | 4.818 | -4.2% | -0.6817 to +0.2601 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 527.2 | -0.1% | -3.436 to +1.852 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 511.5 | -3.1% | -52.65 to +19.7 | no |
| response time (ms), mean | 1102 | 811.7 | -26.3% | -394.5 to -186 | yes: GAIN |
| response time (ms), 95th percentile | 4941 | 3606 | -27.0% | -1933 to -736 | yes: GAIN |
| response time (ms), 99th percentile | 6491 | 4845 | -25.4% | -2379 to -912.7 | yes: GAIN |
| time over the response line (% of samples) | 33.46 | 29.29 | -12.4% | -7.915 to -0.4121 | yes: GAIN |
| failed requests (%) | 0.5532 | 0.06349 | -88.5% | -1.267 to +0.2876 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.9 | 15 | -16.2% | -5.018 to -0.7821 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60 | +60 (native is 0) | +22.36 to +97.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 47.96 | 31.37 | -34.6% | -45.48 to +12.3 | no |
| utilisation (used / allocatable) | 0.03755 | 0.03856 | +2.7% | -0.003034 to +0.00506 | no |
| CPU used (cores), mean | 1.802 | 1.763 | -2.2% | -0.1626 to +0.08338 | no |
| Omni's own CPU (cores), mean | 0 | 0.01245 | +0.0124 (native is 0) | +0.01185 to +0.01305 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.802 | 1.775 | -1.5% | -0.1501 to +0.09572 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711 | 702.1 | -1.3% | -64.5 to +46.53 | no |
| HPA replicas, mean | 4.047 | 4.663 | +15.2% | +0.3677 to +0.8654 | yes: power given |
| pods started | 0 | 1.5 | +1.5 (native is 0) | +0.8921 to +2.108 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.4 (native is 0) | +1.222 to +3.578 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.3 | +1.3 (native is 0) | +0.6874 to +1.913 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 62.86 | 57.12 | -9.1% | -6.862 to -4.609 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1087 | 962.7 | -11.4% | -165 to -83.18 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 11.17 | -6.9% | -2.621 to +0.9639 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 4.758 | 0.1708 | -96.4% | -9.327 to +0.1519 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.8 | -57.9% | -1.811 to -0.3887 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 389.3 | 263.6 | -32.3% | -167.5 to -83.99 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.46 | -4.5% | -1.438 to +0.3667 | no |
| node-hours | 5.02 | 4.804 | -4.3% | -0.5933 to +0.1621 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.2 | 529 | +0.3% | -0.4711 to +4.054 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.2 | 512.1 | -2.9% | -43.72 to +13.61 | no |
| response time (ms), mean | 855.6 | 1128 | +31.9% | +166.1 to +379.6 | yes: LOSS |
| response time (ms), 95th percentile | 3578 | 5221 | +45.9% | +915.6 to +2371 | yes: LOSS |
| response time (ms), 99th percentile | 4824 | 6840 | +41.8% | +1116 to +2916 | yes: LOSS |
| time over the response line (% of samples) | 28.97 | 35.06 | +21.1% | +1.697 to +10.5 | yes: LOSS |
| failed requests (%) | 0.05833 | 0.7251 | +1143.0% | -0.4252 to +1.759 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.1 | 18.6 | +31.9% | +2.983 to +6.017 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.7 | +33.7 (native is 0) | +28.6 to +38.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.43 | 39.17 | +82.8% | +6.043 to +29.43 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03803 | 0.04074 | +7.1% | -0.0001848 to +0.005605 | no |
| CPU used (cores), mean | 1.825 | 1.872 | +2.5% | -0.03638 to +0.1289 | no |
| Omni's own CPU (cores), mean | 0 | 0.01056 | +0.0106 (native is 0) | +0.009723 to +0.0114 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.825 | 1.882 | +3.1% | -0.02589 to +0.1395 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 702.7 | 660.4 | -6.0% | -86.06 to +1.489 | no |
| HPA replicas, mean | 4.008 | 4.518 | +12.7% | +0.3307 to +0.6898 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +1.111 to +2.289 | yes: power given |
| pod start wait, total (s) | 0 | 6 | +6 (native is 0) | -0.8941 to +12.89 | no |
| pod start wait, mean (s) | 0 | 3.05 | +3.05 (native is 0) | -0.3616 to +6.462 | no |
| host CPU busy, the real machine under kind (%) | 55.79 | 65.28 | +17.0% | +7.207 to +11.78 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 950.2 | 1125 | +18.4% | +113.5 to +236.7 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.12 | -7.3% | -2.334 to +0.5747 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 8.7 | +10889.5% | +2.01 to +15.23 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 32.2 | +5266.7% | -36.61 to +99.81 | no |
| queue: job turnaround, submitted to done, mean (s) | 255.1 | 430 | +68.6% | +115.7 to +234.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*