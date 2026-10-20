# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.633 | 5.848 |
| node-hours | 2.514 | 2.514 | 1.944 | 2.453 |
| energy, parked workers still on at idle power (Wh, declared model) | 268.8 | 270.5 | 269.3 | 270.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 268.8 | 270.5 | 226.3 | 265.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 187.1 | 113 | 158.7 | 82.35 |
| response time (ms), 95th percentile | 536.2 | 194.7 | 567.1 | 177.4 |
| response time (ms), 99th percentile | 767.9 | 291 | 818.7 | 274.7 |
| time over the response line (% of samples) | 7.411 | 0.1615 | 7.237 | 0.1113 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 0 | 4.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 64 | 14.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 70 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.838 | 755.1 | 8.708 | 815.7 |
| utilisation (used / allocatable) | 0.05006 | 0.05651 | 0.06582 | 0.05668 |
| CPU used (cores), mean | 1.201 | 1.356 | 1.207 | 1.33 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01674 | 0.01124 |
| CPU used with Omni's own (cores), mean | 1.201 | 1.356 | 1.224 | 1.341 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.7 | 481.4 | 451.5 | 480.6 |
| HPA replicas, mean | 1.983 | 1.943 | 1.984 | 1.909 |
| pods started | 0.1 | 0.5 | 0 | 0.2 |
| pod start wait, total (s) | 0.2 | 1.1 | 0 | 0.3 |
| pod start wait, mean (s) | 0.2 | 0.65 | 0 | 0.15 |
| host CPU busy, the real machine under kind (%) | 34.65 | 41.01 | 35.57 | 41.22 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 731 | 1290 | 732.1 | 1313 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.573 | 5.417 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 103.6 | 0.04583 | 110.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 513.9 | 0.2 | 518.5 |
| queue: job turnaround, submitted to done, mean (s) | 38.07 | 614 | 40.1 | 650.2 |
| queue: jobs unfinished at the window's end | 0 | 4.9 | 0 | 5.3 |

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
| worker nodes in service, mean | 6 | 5.848 | -2.5% | -0.3729 to +0.06899 | no |
| node-hours | 2.514 | 2.453 | -2.4% | -0.1576 to +0.03665 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270.5 | -0.0% | -0.9457 to +0.9252 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 265.8 | -1.8% | -12.27 to +2.726 | no |
| response time (ms), mean | 113 | 82.35 | -27.1% | -38.99 to -22.32 | yes: GAIN |
| response time (ms), 95th percentile | 194.7 | 177.4 | -8.9% | -27.89 to -6.731 | yes: GAIN |
| response time (ms), 99th percentile | 291 | 274.7 | -5.6% | -40.47 to +7.84 | no |
| time over the response line (% of samples) | 0.1615 | 0.1113 | -31.1% | -0.116 to +0.01549 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.2 | +14.2 (native is 0) | +11.13 to +17.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 755.1 | 815.7 | +8.0% | -16.46 to +137.6 | no |
| utilisation (used / allocatable) | 0.05651 | 0.05668 | +0.3% | -0.002137 to +0.002475 | no |
| CPU used (cores), mean | 1.356 | 1.33 | -2.0% | -0.06369 to +0.01029 | no |
| Omni's own CPU (cores), mean | 0 | 0.01124 | +0.0112 (native is 0) | +0.01006 to +0.01242 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.356 | 1.341 | -1.1% | -0.05198 to +0.02106 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.4 | 480.6 | -0.2% | -17.39 to +15.73 | no |
| HPA replicas, mean | 1.943 | 1.909 | -1.7% | -0.1318 to +0.06447 | no |
| pods started | 0.5 | 0.2 | -60.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 1.1 | 0.3 | -72.7% | -1.958 to +0.3583 | no |
| pod start wait, mean (s) | 0.65 | 0.15 | -76.9% | -1.174 to +0.1744 | no |
| host CPU busy, the real machine under kind (%) | 41.01 | 41.22 | +0.5% | -0.7395 to +1.164 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1290 | 1313 | +1.8% | -48.08 to +93.28 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.417 | -9.7% | -1.413 to +0.2468 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 103.6 | 110.9 | +7.1% | -29.12 to +43.75 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 513.9 | 518.5 | +0.9% | -163.9 to +173.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 614 | 650.2 | +5.9% | -13.89 to +86.34 | no |
| queue: jobs unfinished at the window's end | 4.9 | 5.3 | +8.2% | -1.359 to +2.159 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.537e-15 to -9.702e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.514 | 2.514 | -0.0% | -0.006433 to +0.005766 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 268.8 | 270.5 | +0.6% | +0.7036 to +2.781 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 268.8 | 270.5 | +0.6% | +0.7036 to +2.781 | yes: power given |
| response time (ms), mean | 187.1 | 113 | -39.6% | -128.3 to -19.8 | yes: GAIN |
| response time (ms), 95th percentile | 536.2 | 194.7 | -63.7% | -581.7 to -101.2 | yes: GAIN |
| response time (ms), 99th percentile | 767.9 | 291 | -62.1% | -796.5 to -157.3 | yes: GAIN |
| time over the response line (% of samples) | 7.411 | 0.1615 | -97.8% | -14.65 to +0.1509 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 0 | -100.0% | -9.291 to -0.9094 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.838 | 755.1 | +9533.6% | +474.1 to +1020 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05006 | 0.05651 | +12.9% | +0.002497 to +0.01041 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.201 | 1.356 | +12.9% | +0.05992 to +0.2499 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.201 | 1.356 | +12.9% | +0.05992 to +0.2499 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.7 | 481.4 | -13.5% | -128.4 to -22.21 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 1.943 | -2.0% | -0.1677 to +0.08658 | no |
| pods started | 0.1 | 0.5 | +400.0% | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | -0.2898 to +2.09 | no |
| pod start wait, mean (s) | 0.2 | 0.65 | +225.0% | -0.2338 to +1.134 | no |
| host CPU busy, the real machine under kind (%) | 34.65 | 41.01 | +18.3% | +4.655 to +8.059 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 731 | 1290 | +76.5% | +395.8 to +723.2 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 103.6 | +310637.5% | +55.6 to +151.5 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 513.9 | +171200.0% | +273.4 to +753.8 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 38.07 | 614 | +1512.7% | +384.9 to +766.9 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 4.9 | +4.9 (native is 0) | -0.7971 to +10.6 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.633 | -22.8% | -2.041 to -0.692 | yes: GAIN |
| node-hours | 2.514 | 1.944 | -22.7% | -0.855 to -0.285 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 268.8 | 269.3 | +0.2% | -0.1777 to +1.271 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 268.8 | 226.3 | -15.8% | -63.65 to -21.28 | yes: GAIN |
| response time (ms), mean | 187.1 | 158.7 | -15.2% | -40.38 to -16.33 | yes: GAIN |
| response time (ms), 95th percentile | 536.2 | 567.1 | +5.8% | +8.762 to +53.09 | yes: LOSS |
| response time (ms), 99th percentile | 767.9 | 818.7 | +6.6% | -35.82 to +137.4 | no |
| time over the response line (% of samples) | 7.411 | 7.237 | -2.3% | -0.7914 to +0.4439 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 4.9 | -3.9% | -0.7642 to +0.3642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64 | +64 (native is 0) | +51.18 to +76.82 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.838 | 8.708 | +11.1% | -0.4897 to +2.23 | no |
| utilisation (used / allocatable) | 0.05006 | 0.06582 | +31.5% | +0.007133 to +0.0244 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.201 | 1.207 | +0.5% | -0.03155 to +0.04326 | no |
| Omni's own CPU (cores), mean | 0 | 0.01674 | +0.0167 (native is 0) | +0.01529 to +0.01819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.201 | 1.224 | +1.9% | -0.0142 to +0.0594 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.7 | 451.5 | -18.9% | -172.8 to -37.59 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 1.984 | +0.0% | -0.1219 to +0.1222 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 34.65 | 35.57 | +2.7% | +0.4955 to +1.351 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 731 | 732.1 | +0.2% | -2.824 to +5.024 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.573 | -40.5% | -3.572 to -1.282 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.04583 | +37.5% | -0.01204 to +0.03704 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | -33.3% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 38.07 | 40.1 | +5.3% | -1.776 to +5.826 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.633 | -22.8% | -2.041 to -0.692 | yes: GAIN |
| node-hours | 2.514 | 1.944 | -22.7% | -0.8514 to -0.288 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 269.3 | -0.4% | -2.352 to -0.03873 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 226.3 | -16.3% | -65.95 to -22.47 | yes: GAIN |
| response time (ms), mean | 113 | 158.7 | +40.4% | -3.414 to +94.81 | no |
| response time (ms), 95th percentile | 194.7 | 567.1 | +191.2% | +123.9 to +620.9 | yes: LOSS |
| response time (ms), 99th percentile | 291 | 818.7 | +181.3% | +165.5 to +889.8 | yes: LOSS |
| time over the response line (% of samples) | 0.1615 | 7.237 | +4381.5% | -0.2121 to +14.36 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 4.9 | +4.9 (native is 0) | +0.7503 to +9.05 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64 | +64 (native is 0) | +51.18 to +76.82 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 755.1 | 8.708 | -98.8% | -1019 to -474.2 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05651 | 0.06582 | +16.5% | +0.002983 to +0.01564 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.356 | 1.207 | -11.0% | -0.2378 to -0.06032 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01674 | +0.0167 (native is 0) | +0.01529 to +0.01819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.356 | 1.224 | -9.8% | -0.2217 to -0.04287 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.4 | 451.5 | -6.2% | -56.95 to -2.929 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.943 | 1.984 | +2.1% | -0.1047 to +0.1863 | no |
| pods started | 0.5 | 0 | -100.0% | -1.108 to +0.1079 | no |
| pod start wait, total (s) | 1.1 | 0 | -100.0% | -2.468 to +0.2676 | no |
| pod start wait, mean (s) | 0.65 | 0 | -100.0% | -1.405 to +0.1049 | no |
| host CPU busy, the real machine under kind (%) | 41.01 | 35.57 | -13.3% | -7.057 to -3.81 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1290 | 732.1 | -43.3% | -721.3 to -395.5 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.764 | -53.9% | -4.203 to -2.268 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 103.6 | 0.04583 | -100.0% | -151.5 to -55.59 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 513.9 | 0.2 | -100.0% | -754 to -273.4 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 614 | 40.1 | -93.5% | -763.1 to -384.6 | yes: GAIN |
| queue: jobs unfinished at the window's end | 4.9 | 0 | -100.0% | -10.6 to +0.7971 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.848 | -2.5% | -0.3729 to +0.06899 | no |
| node-hours | 2.514 | 2.453 | -2.4% | -0.1565 to +0.03491 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 268.8 | 270.5 | +0.6% | +0.5843 to +2.879 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 268.8 | 265.8 | -1.1% | -9.883 to +3.826 | no |
| response time (ms), mean | 187.1 | 82.35 | -56.0% | -166 to -43.45 | yes: GAIN |
| response time (ms), 95th percentile | 536.2 | 177.4 | -66.9% | -599.9 to -117.6 | yes: GAIN |
| response time (ms), 99th percentile | 767.9 | 274.7 | -64.2% | -807.9 to -178.4 | yes: GAIN |
| time over the response line (% of samples) | 7.411 | 0.1113 | -98.5% | -14.73 to +0.1351 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 0 | -100.0% | -9.291 to -0.9094 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.2 | +14.2 (native is 0) | +11.13 to +17.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.838 | 815.7 | +10306.6% | +498.9 to +1117 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05006 | 0.05668 | +13.2% | +0.0009441 to +0.0123 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.201 | 1.33 | +10.7% | +0.01675 to +0.2397 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01124 | +0.0112 (native is 0) | +0.01006 to +0.01242 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.201 | 1.341 | +11.6% | +0.02887 to +0.25 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.7 | 480.6 | -13.7% | -142.9 to -9.347 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 1.909 | -3.7% | -0.1848 to +0.0363 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.2 | 0.3 | +50.0% | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0.2 | 0.15 | -25.0% | -0.1631 to +0.0631 | no |
| host CPU busy, the real machine under kind (%) | 34.65 | 41.22 | +19.0% | +4.529 to +8.61 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 731 | 1313 | +79.6% | +419.7 to +744.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.417 | -9.7% | -1.413 to +0.2468 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 110.9 | +332575.0% | +68.06 to +153.7 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 518.5 | +172733.3% | +314.2 to +722.2 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 38.07 | 650.2 | +1607.8% | +411.6 to +812.6 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 5.3 | +5.3 (native is 0) | -0.8906 to +11.49 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*