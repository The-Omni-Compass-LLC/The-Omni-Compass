# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.467 | 5.457 |
| node-hours | 2.516 | 2.517 | 2.291 | 2.289 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 | 272.2 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.7 | 255.4 | 255 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 319.5 | 282.3 | 299.3 | 270.7 |
| response time (ms), 95th percentile | 1055 | 1045 | 1146 | 1223 |
| response time (ms), 99th percentile | 1544 | 1578 | 1752 | 1923 |
| time over the response line (% of samples) | 19.37 | 13.29 | 19.06 | 13.28 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | 9.4 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 100.8 | 95.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 11.73 | 10.29 | 12.98 |
| utilisation (used / allocatable) | 0.05881 | 0.05697 | 0.06459 | 0.06387 |
| CPU used (cores), mean | 1.411 | 1.367 | 1.416 | 1.396 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.04759 | 0.04756 |
| CPU used with Omni's own (cores), mean | 1.411 | 1.367 | 1.463 | 1.444 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.2 | 485.4 | 434.5 | 440.2 |
| HPA replicas, mean | 1.983 | 1.978 | 2.713 | 2.725 |
| pods started | 0 | 0 | 1.8 | 2 |
| pod start wait, total (s) | 0 | 0 | 4.4 | 4 |
| pod start wait, mean (s) | 0 | 0 | 1.967 | 1.29 |
| host CPU busy, the real machine under kind (%) | 40.01 | 39.3 | 42.35 | 41.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 765.1 | 758.1 | 772.4 | 769 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.969 | 4.98 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.0625 | 0.04167 | 0.05 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | 0.3 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 73.13 | 68.32 | 80.74 | 78.97 |
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
| worker nodes in service, mean | 6 | 5.457 | -9.1% | -1.17 to +0.08428 | no |
| node-hours | 2.517 | 2.289 | -9.1% | -0.4923 to +0.03581 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.2 | +0.2% | -0.2691 to +1.215 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 255 | -6.1% | -36.71 to +3.415 | no |
| response time (ms), mean | 282.3 | 270.7 | -4.1% | -38.94 to +15.62 | no |
| response time (ms), 95th percentile | 1045 | 1223 | +17.0% | -23.02 to +377.9 | no |
| response time (ms), 99th percentile | 1578 | 1923 | +21.9% | +100.5 to +589.3 | yes: LOSS |
| time over the response line (% of samples) | 13.29 | 13.28 | -0.1% | -2.136 to +2.112 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.2 | +2.2% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.5 | +95.5 (native is 0) | +66.51 to +124.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.73 | 12.98 | +10.7% | -0.8245 to +3.324 | no |
| utilisation (used / allocatable) | 0.05697 | 0.06387 | +12.1% | +0.0007362 to +0.01306 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.367 | 1.396 | +2.1% | -0.01484 to +0.07246 | no |
| Omni's own CPU (cores), mean | 0 | 0.04756 | +0.0476 (native is 0) | +0.0413 to +0.05382 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.367 | 1.444 | +5.6% | +0.02954 to +0.1232 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.4 | 440.2 | -9.3% | -87.56 to -2.942 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.725 | +37.7% | +0.3252 to +1.167 | yes: power given |
| pods started | 0 | 2 | +2 (native is 0) | +0.694 to +3.306 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4 (native is 0) | +0.8548 to +7.145 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.29 | +1.29 (native is 0) | +0.5651 to +2.015 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.3 | 41.75 | +6.2% | +1.988 to +2.902 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.1 | 769 | +1.4% | +3.937 to +17.86 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.98 | -17.0% | -2.2 to +0.1605 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05 | -20.0% | -0.0592 to +0.0342 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | -60.0% | -0.8889 to +0.2889 | no |
| queue: job turnaround, submitted to done, mean (s) | 68.32 | 78.97 | +15.6% | +4.344 to +16.95 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.517 | +0.0% | -0.005267 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 | -0.2% | -1.244 to +0.3735 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.7 | -0.2% | -1.244 to +0.3735 | no |
| response time (ms), mean | 319.5 | 282.3 | -11.6% | -61.84 to -12.41 | yes: GAIN |
| response time (ms), 95th percentile | 1055 | 1045 | -0.9% | -109.3 to +89.55 | no |
| response time (ms), 99th percentile | 1544 | 1578 | +2.2% | -42.75 to +110.3 | no |
| time over the response line (% of samples) | 19.37 | 13.29 | -31.4% | -9.487 to -2.671 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | -1.1% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 11.73 | +16.7% | -0.08147 to +3.441 | no |
| utilisation (used / allocatable) | 0.05881 | 0.05697 | -3.1% | -0.002414 to -0.001259 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.367 | -3.1% | -0.05793 to -0.03021 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.411 | 1.367 | -3.1% | -0.05793 to -0.03021 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.2 | 485.4 | +3.2% | +6.75 to +23.67 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.983 | 1.978 | -0.2% | -0.1104 to +0.1006 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 40.01 | 39.3 | -1.8% | -1.049 to -0.3703 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 765.1 | 758.1 | -0.9% | -11.92 to -2.079 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.0625 | -6.2% | -0.03697 to +0.02863 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.13 | 68.32 | -6.6% | -8.054 to -1.563 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.467 | -8.9% | -1.112 to +0.04536 | no |
| node-hours | 2.516 | 2.291 | -8.9% | -0.4622 to +0.01355 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.2 | +0.0% | -0.9933 to +1.255 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 255.4 | -6.1% | -34.4 to +1.032 | no |
| response time (ms), mean | 319.5 | 299.3 | -6.3% | -30.26 to -10.17 | yes: GAIN |
| response time (ms), 95th percentile | 1055 | 1146 | +8.6% | +34.93 to +147.4 | yes: LOSS |
| response time (ms), 99th percentile | 1544 | 1752 | +13.4% | +88.81 to +326.1 | yes: LOSS |
| time over the response line (% of samples) | 19.37 | 19.06 | -1.6% | -1.055 to +0.4374 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.4 | +3.3% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.8 | +101 (native is 0) | +66.47 to +135.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 10.29 | +2.4% | -1.536 to +2.01 | no |
| utilisation (used / allocatable) | 0.05881 | 0.06459 | +9.8% | +0.0001757 to +0.01139 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.411 | 1.416 | +0.3% | -0.01192 to +0.0206 | no |
| Omni's own CPU (cores), mean | 0 | 0.04759 | +0.0476 (native is 0) | +0.04098 to +0.0542 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.463 | +3.7% | +0.02999 to +0.07387 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.2 | 434.5 | -7.6% | -70.97 to -0.4517 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.713 | +36.8% | +0.3284 to +1.13 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.9207 to +2.679 | yes: power given |
| pod start wait, total (s) | 0 | 4.4 | +4.4 (native is 0) | +1.987 to +6.813 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.967 | +1.97 (native is 0) | +1.107 to +2.826 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.01 | 42.35 | +5.8% | +1.834 to +2.841 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 765.1 | 772.4 | +1.0% | +3.211 to +11.39 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.969 | -17.2% | -2.145 to +0.08194 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.04167 | -37.5% | -0.07202 to +0.02202 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.13 | 80.74 | +10.4% | +3.354 to +11.87 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.467 | -8.9% | -1.112 to +0.04536 | no |
| node-hours | 2.517 | 2.291 | -9.0% | -0.468 to +0.01704 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.2 | +0.2% | -0.1657 to +1.298 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 255.4 | -6.0% | -34.58 to +2.086 | no |
| response time (ms), mean | 282.3 | 299.3 | +6.0% | -9.571 to +43.4 | no |
| response time (ms), 95th percentile | 1045 | 1146 | +9.7% | -18.06 to +220.1 | no |
| response time (ms), 99th percentile | 1578 | 1752 | +11.0% | +31.06 to +316.3 | yes: LOSS |
| time over the response line (% of samples) | 13.29 | 19.06 | +43.4% | +2.541 to +9 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.4 | +4.4% | +0.03062 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.8 | +101 (native is 0) | +66.47 to +135.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.73 | 10.29 | -12.3% | -3.258 to +0.3712 | no |
| utilisation (used / allocatable) | 0.05697 | 0.06459 | +13.4% | +0.002041 to +0.0132 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.367 | 1.416 | +3.5% | +0.02851 to +0.06831 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04759 | +0.0476 (native is 0) | +0.04098 to +0.0542 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.367 | 1.463 | +7.0% | +0.07127 to +0.1207 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.4 | 434.5 | -10.5% | -90.94 to -10.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.713 | +37.1% | +0.3482 to +1.12 | yes: power given |
| pods started | 0 | 1.8 | +1.8 (native is 0) | +0.9207 to +2.679 | yes: power given |
| pod start wait, total (s) | 0 | 4.4 | +4.4 (native is 0) | +1.987 to +6.813 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.967 | +1.97 (native is 0) | +1.107 to +2.826 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.3 | 42.35 | +7.8% | +2.654 to +3.441 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.1 | 772.4 | +1.9% | +6.662 to +21.94 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.969 | -17.2% | -2.145 to +0.08194 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.04167 | -33.3% | -0.06119 to +0.01952 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | -40.0% | -0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 68.32 | 80.74 | +18.2% | +5.639 to +19.2 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.457 | -9.1% | -1.17 to +0.08428 | no |
| node-hours | 2.516 | 2.289 | -9.0% | -0.4865 to +0.03238 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.2 | +0.0% | -0.8643 to +0.94 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 255 | -6.3% | -36.53 to +2.365 | no |
| response time (ms), mean | 319.5 | 270.7 | -15.3% | -68.82 to -28.77 | yes: GAIN |
| response time (ms), 95th percentile | 1055 | 1223 | +15.9% | +23.44 to +311.8 | yes: LOSS |
| response time (ms), 99th percentile | 1544 | 1923 | +24.5% | +138.6 to +618.7 | yes: LOSS |
| time over the response line (% of samples) | 19.37 | 13.28 | -31.4% | -9.186 to -2.997 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.2 | +1.1% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.5 | +95.5 (native is 0) | +66.51 to +124.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.05 | 12.98 | +29.2% | +1.076 to +4.784 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05881 | 0.06387 | +8.6% | -0.001062 to +0.01119 | no |
| CPU used (cores), mean | 1.411 | 1.396 | -1.1% | -0.05083 to +0.02031 | no |
| Omni's own CPU (cores), mean | 0 | 0.04756 | +0.0476 (native is 0) | +0.0413 to +0.05382 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.411 | 1.444 | +2.3% | -0.007025 to +0.07163 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.2 | 440.2 | -6.4% | -66.77 to +6.691 | no |
| HPA replicas, mean | 1.983 | 2.725 | +37.4% | +0.288 to +1.195 | yes: power given |
| pods started | 0 | 2 | +2 (native is 0) | +0.694 to +3.306 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4 (native is 0) | +0.8548 to +7.145 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.29 | +1.29 (native is 0) | +0.5651 to +2.015 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.01 | 41.75 | +4.3% | +1.092 to +2.378 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 765.1 | 769 | +0.5% | -2.376 to +10.18 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.98 | -17.0% | -2.2 to +0.1605 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05 | -25.0% | -0.05437 to +0.02103 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.2 | -60.0% | -0.7828 to +0.1828 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.13 | 78.97 | +8.0% | +0.004356 to +11.67 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*