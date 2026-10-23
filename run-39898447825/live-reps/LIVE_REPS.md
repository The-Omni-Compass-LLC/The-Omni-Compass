# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.919 | 4.931 |
| node-hours | 2.517 | 2.514 | 2.063 | 2.065 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.8 | 271.3 | 270.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 270.8 | 237.4 | 237.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 311.1 | 311.2 | 323.2 | 326 |
| response time (ms), 95th percentile | 1140 | 1153 | 1213 | 1284 |
| response time (ms), 99th percentile | 1724 | 1911 | 1872 | 1999 |
| time over the response line (% of samples) | 14.69 | 13.7 | 14.94 | 14.68 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.2 | 7.8 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 45.6 | 42.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 84 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 9.582 | 10.72 | 12.21 |
| utilisation (used / allocatable) | 0.05785 | 0.05658 | 0.06937 | 0.06827 |
| CPU used (cores), mean | 1.388 | 1.358 | 1.363 | 1.346 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03722 | 0.04074 |
| CPU used with Omni's own (cores), mean | 1.388 | 1.358 | 1.4 | 1.387 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.7 | 494.7 | 420.4 | 426.6 |
| HPA replicas, mean | 2.082 | 2.132 | 2.405 | 2.519 |
| pods started | 0 | 0.1 | 1.3 | 1.4 |
| pod start wait, total (s) | 0 | 0.3 | 2.4 | 3.1 |
| pod start wait, mean (s) | 0 | 0.3 | 1.2 | 1.125 |
| host CPU busy, the real machine under kind (%) | 39.46 | 40.26 | 41.12 | 42.01 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 773.1 | 778.7 | 778.7 | 784.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.031 | 4.044 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.1792 | 0.06667 | 0.1708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.7 | 0.5 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 82.19 | 89.04 | 85.81 | 94.21 |
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
| worker nodes in service, mean | 6 | 4.931 | -17.8% | -1.874 to -0.2642 | yes: GAIN |
| node-hours | 2.514 | 2.065 | -17.9% | -0.7846 to -0.1138 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.8 | +0.0% | -1.184 to +1.214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 237.2 | -12.4% | -58.84 to -8.391 | yes: GAIN |
| response time (ms), mean | 311.2 | 326 | +4.8% | +3.077 to +26.55 | yes: LOSS |
| response time (ms), 95th percentile | 1153 | 1284 | +11.4% | +21.63 to +241.3 | yes: LOSS |
| response time (ms), 99th percentile | 1911 | 1999 | +4.6% | -130.2 to +307.8 | no |
| time over the response line (% of samples) | 13.7 | 14.68 | +7.1% | +0.183 to +1.774 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.8 | +8.3% | -0.4228 to +1.623 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.5 | +42.5 (native is 0) | +25.08 to +59.92 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.582 | 12.21 | +27.5% | +0.8659 to +4.397 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05658 | 0.06827 | +20.7% | +0.003167 to +0.02021 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.358 | 1.346 | -0.9% | -0.05656 to +0.03286 | no |
| Omni's own CPU (cores), mean | 0 | 0.04074 | +0.0407 (native is 0) | +0.03436 to +0.04712 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.358 | 1.387 | +2.1% | -0.01835 to +0.07613 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.7 | 426.6 | -13.8% | -119.6 to -16.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.132 | 2.519 | +18.2% | -0.03267 to +0.8075 | no |
| pods started | 0.1 | 1.4 | +1300.0% | +0.03607 to +2.564 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.1 | +933.3% | -0.05725 to +5.657 | no |
| pod start wait, mean (s) | 0.3 | 1.125 | +275.0% | -0.4424 to +2.092 | no |
| host CPU busy, the real machine under kind (%) | 40.26 | 42.01 | +4.3% | +1.4 to +2.102 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 778.7 | 784.2 | +0.7% | +0.4957 to +10.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.044 | -32.6% | -3.418 to -0.494 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1792 | 0.1708 | -4.7% | -0.06925 to +0.05259 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.04 | 94.21 | +5.8% | +1.148 to +9.194 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.115e-15 to +7.599e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.514 | -0.1% | -0.01159 to +0.006258 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.8 | -0.3% | -1.974 to +0.3779 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 270.8 | -0.3% | -1.974 to +0.3779 | no |
| response time (ms), mean | 311.1 | 311.2 | +0.0% | -8.873 to +9.081 | no |
| response time (ms), 95th percentile | 1140 | 1153 | +1.1% | -53.01 to +78.26 | no |
| response time (ms), 99th percentile | 1724 | 1911 | +10.8% | -48.23 to +422.1 | no |
| time over the response line (% of samples) | 14.69 | 13.7 | -6.7% | -1.745 to -0.2341 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.2 | -1.4% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 9.582 | -8.1% | -2.059 to +0.3622 | no |
| utilisation (used / allocatable) | 0.05785 | 0.05658 | -2.2% | -0.002927 to +0.0003921 | no |
| CPU used (cores), mean | 1.388 | 1.358 | -2.2% | -0.07025 to +0.00941 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.388 | 1.358 | -2.2% | -0.07025 to +0.00941 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.7 | 494.7 | +3.3% | -2.133 to +34.07 | no |
| HPA replicas, mean | 2.082 | 2.132 | +2.4% | -0.0949 to +0.1937 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 39.46 | 40.26 | +2.0% | +0.5588 to +1.047 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.1 | 778.7 | +0.7% | +0.9496 to +10.25 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.1792 | +186.7% | +0.05908 to +0.1743 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.7 | +75.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.19 | 89.04 | +8.3% | +1.122 to +12.58 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.919 | -18.0% | -1.845 to -0.3169 | yes: GAIN |
| node-hours | 2.517 | 2.063 | -18.1% | -0.7779 to -0.131 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.3 | -0.1% | -1.323 to +0.7969 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 237.4 | -12.6% | -58.86 to -9.574 | yes: GAIN |
| response time (ms), mean | 311.1 | 323.2 | +3.9% | +2.13 to +22.13 | yes: LOSS |
| response time (ms), 95th percentile | 1140 | 1213 | +6.4% | +10.39 to +135.5 | yes: LOSS |
| response time (ms), 99th percentile | 1724 | 1872 | +8.6% | -97.63 to +393.7 | no |
| time over the response line (% of samples) | 14.69 | 14.94 | +1.7% | -0.2462 to +0.7316 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.8 | +6.8% | -0.2726 to +1.273 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.6 | +45.6 (native is 0) | +26.51 to +64.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 10.73 | +2.8% | -1.193 to +1.783 | no |
| utilisation (used / allocatable) | 0.05785 | 0.06937 | +19.9% | +0.003764 to +0.01927 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.388 | 1.363 | -1.9% | -0.06379 to +0.01202 | no |
| Omni's own CPU (cores), mean | 0 | 0.03722 | +0.0372 (native is 0) | +0.0306 to +0.04384 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.388 | 1.4 | +0.8% | -0.03274 to +0.05541 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.7 | 420.4 | -12.2% | -97.91 to -18.71 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.082 | 2.405 | +15.5% | -0.06663 to +0.7116 | no |
| pods started | 0 | 1.3 | +1.3 (native is 0) | +0.3433 to +2.257 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.4 (native is 0) | +0.428 to +4.372 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | +0.5427 to +1.857 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.46 | 41.12 | +4.2% | +1.189 to +2.132 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.1 | 778.7 | +0.7% | -0.1145 to +11.31 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.031 | -32.8% | -3.321 to -0.6173 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.06667 | +6.7% | -0.07077 to +0.07911 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.19 | 85.81 | +4.4% | +0.2138 to +7.028 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.919 | -18.0% | -1.845 to -0.3169 | yes: GAIN |
| node-hours | 2.514 | 2.063 | -18.0% | -0.7736 to -0.1299 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | +0.2% | -0.4916 to +1.561 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 237.4 | -12.3% | -57.47 to -9.368 | yes: GAIN |
| response time (ms), mean | 311.2 | 323.2 | +3.9% | -4.806 to +28.86 | no |
| response time (ms), 95th percentile | 1153 | 1213 | +5.2% | -28.94 to +149.6 | no |
| response time (ms), 99th percentile | 1911 | 1872 | -2.0% | -389.3 to +311.6 | no |
| time over the response line (% of samples) | 13.7 | 14.94 | +9.0% | +0.4871 to +1.977 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.8 | +8.3% | -0.2396 to +1.44 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.6 | +45.6 (native is 0) | +26.51 to +64.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.582 | 10.72 | +11.9% | -1.145 to +3.432 | no |
| utilisation (used / allocatable) | 0.05658 | 0.06937 | +22.6% | +0.003852 to +0.02172 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.358 | 1.363 | +0.3% | -0.01771 to +0.02678 | no |
| Omni's own CPU (cores), mean | 0 | 0.03722 | +0.0372 (native is 0) | +0.0306 to +0.04384 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.358 | 1.4 | +3.1% | +0.01598 to +0.06753 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.7 | 420.4 | -15.0% | -128.1 to -20.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.132 | 2.405 | +12.8% | -0.05316 to +0.5993 | no |
| pods started | 0.1 | 1.3 | +1200.0% | +0.1444 to +2.256 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.4 | +700.0% | -0.1733 to +4.373 | no |
| pod start wait, mean (s) | 0.3 | 1.2 | +300.0% | -0.241 to +2.041 | no |
| host CPU busy, the real machine under kind (%) | 40.26 | 41.12 | +2.1% | +0.405 to +1.311 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 778.7 | 778.7 | +0.0% | -2.079 to +2.079 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.031 | -32.8% | -3.321 to -0.6173 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1792 | 0.06667 | -62.8% | -0.1842 to -0.04079 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.5 | -28.6% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.04 | 85.81 | -3.6% | -6.204 to -0.2546 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.931 | -17.8% | -1.874 to -0.2642 | yes: GAIN |
| node-hours | 2.517 | 2.065 | -18.0% | -0.7884 to -0.1153 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 270.8 | -0.3% | -1.981 to +0.4156 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 237.2 | -12.7% | -60.17 to -8.652 | yes: GAIN |
| response time (ms), mean | 311.1 | 326 | +4.8% | +5.208 to +24.63 | yes: LOSS |
| response time (ms), 95th percentile | 1140 | 1284 | +12.6% | +44.58 to +243.6 | yes: LOSS |
| response time (ms), 99th percentile | 1724 | 1999 | +16.0% | +5.238 to +546.2 | yes: LOSS |
| time over the response line (% of samples) | 14.69 | 14.68 | -0.1% | -0.7245 to +0.703 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.8 | +6.8% | -0.343 to +1.343 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.5 | +42.5 (native is 0) | +25.08 to +59.92 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.43 | 12.21 | +17.1% | +0.4816 to +3.085 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05785 | 0.06827 | +18.0% | +0.003026 to +0.01782 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.388 | 1.346 | -3.0% | -0.1039 to +0.01938 | no |
| Omni's own CPU (cores), mean | 0 | 0.04074 | +0.0407 (native is 0) | +0.03436 to +0.04712 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.388 | 1.387 | -0.1% | -0.06778 to +0.06473 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 478.7 | 426.6 | -10.9% | -90.28 to -14.05 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.082 | 2.519 | +21.0% | -0.03923 to +0.9129 | no |
| pods started | 0 | 1.4 | +1.4 (native is 0) | +0.2222 to +2.578 | yes: power given |
| pod start wait, total (s) | 0 | 3.1 | +3.1 (native is 0) | +0.522 to +5.678 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.125 | +1.12 (native is 0) | +0.252 to +1.998 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.46 | 42.01 | +6.5% | +2.177 to +2.931 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.1 | 784.2 | +1.4% | +2.227 to +19.97 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.044 | -32.6% | -3.418 to -0.494 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.1708 | +173.3% | +0.0378 to +0.1789 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.7 | +75.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.19 | 94.21 | +14.6% | +3.127 to +20.91 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*