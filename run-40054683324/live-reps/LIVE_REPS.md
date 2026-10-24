# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.541 | 4.602 |
| node-hours | 2.513 | 2.513 | 1.899 | 1.927 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.7 | 269.3 | 269.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 269.7 | 223.5 | 225.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 213.2 | 230.4 | 185.1 | 207.5 |
| response time (ms), 95th percentile | 646.8 | 833.3 | 671.3 | 893.1 |
| response time (ms), 99th percentile | 933.7 | 1312 | 983.1 | 1429 |
| time over the response line (% of samples) | 8.805 | 7.755 | 8.8 | 8.228 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 5.5 | 5 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.9 | 37.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.063 | 12.88 | 8.362 | 13.36 |
| utilisation (used / allocatable) | 0.05276 | 0.05295 | 0.07086 | 0.06948 |
| CPU used (cores), mean | 1.266 | 1.271 | 1.255 | 1.249 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01461 | 0.01588 |
| CPU used with Omni's own (cores), mean | 1.266 | 1.271 | 1.269 | 1.265 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.4 | 518 | 425.9 | 433.1 |
| HPA replicas, mean | 1.922 | 1.959 | 2.275 | 2.094 |
| pods started | 0 | 0 | 0.1 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 0.1 | 0.4 |
| pod start wait, mean (s) | 0 | 0 | 0.1 | 0.4 |
| host CPU busy, the real machine under kind (%) | 35.9 | 38.08 | 36.92 | 38.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 740.7 | 756.2 | 742.6 | 758.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.642 | 3.75 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.6792 | 0.0375 | 0.6833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1.2 | 0.2 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 47.31 | 65.87 | 48.84 | 66.67 |
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
| worker nodes in service, mean | 6 | 4.602 | -23.3% | -2.29 to -0.5066 | yes: GAIN |
| node-hours | 2.513 | 1.927 | -23.3% | -0.9614 to -0.2104 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.7 | -0.0% | -0.9846 to +0.9241 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 225.8 | -16.3% | -72.35 to -15.53 | yes: GAIN |
| response time (ms), mean | 230.4 | 207.5 | -9.9% | -38.57 to -7.162 | yes: GAIN |
| response time (ms), 95th percentile | 833.3 | 893.1 | +7.2% | -94.7 to +214.4 | no |
| response time (ms), 99th percentile | 1312 | 1429 | +8.9% | -126.8 to +361.1 | no |
| time over the response line (% of samples) | 7.755 | 8.228 | +6.1% | -0.6194 to +1.566 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.5 | 5.8 | +5.5% | -0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.1 (native is 0) | +31.18 to +43.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.88 | 13.36 | +3.8% | -1.192 to +2.159 | no |
| utilisation (used / allocatable) | 0.05295 | 0.06948 | +31.2% | +0.00612 to +0.02695 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.271 | 1.249 | -1.7% | -0.06458 to +0.02115 | no |
| Omni's own CPU (cores), mean | 0 | 0.01588 | +0.0159 (native is 0) | +0.01361 to +0.01815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.271 | 1.265 | -0.5% | -0.05035 to +0.03869 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518 | 433.1 | -16.4% | -140 to -29.89 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.959 | 2.094 | +6.9% | -0.1017 to +0.3735 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2911 to +1.091 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2911 to +1.091 | no |
| host CPU busy, the real machine under kind (%) | 38.08 | 38.75 | +1.7% | +0.1243 to +1.203 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 758.6 | +0.3% | -3.394 to +8.194 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.75 | -37.5% | -3.608 to -0.8907 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6792 | 0.6833 | +0.6% | -0.05106 to +0.05939 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.2 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.87 | 66.67 | +1.2% | -3.656 to +5.273 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.355e-15 to +4.668e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.513 | +0.0% | -0.005206 to +0.006539 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.7 | +0.0% | -0.6123 to +0.8318 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 269.7 | +0.0% | -0.6123 to +0.8318 | no |
| response time (ms), mean | 213.2 | 230.4 | +8.1% | -9.884 to +44.26 | no |
| response time (ms), 95th percentile | 646.8 | 833.3 | +28.8% | -28.26 to +401.2 | no |
| response time (ms), 99th percentile | 933.7 | 1312 | +40.6% | -50.18 to +807.6 | no |
| time over the response line (% of samples) | 8.805 | 7.755 | -11.9% | -3.996 to +1.896 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 5.5 | +14.6% | -0.4705 to +1.871 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.063 | 12.88 | +59.7% | +3.042 to +6.582 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05276 | 0.05295 | +0.3% | -0.001141 to +0.001507 | no |
| CPU used (cores), mean | 1.266 | 1.271 | +0.3% | -0.02738 to +0.03617 | no |
| Omni's own CPU (cores), mean | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| CPU used with Omni's own (cores), mean | 1.266 | 1.271 | +0.3% | -0.02738 to +0.03617 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.4 | 518 | -0.7% | -18.42 to +11.64 | no |
| HPA replicas, mean | 1.922 | 1.959 | +1.9% | -0.09068 to +0.1645 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 35.9 | 38.08 | +6.1% | +1.085 to +3.281 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 740.7 | 756.2 | +2.1% | +2.5 to +28.5 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.6792 | +3160.0% | +0.5553 to +0.7614 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1.2 | +1100.0% | +0.8738 to +1.326 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 47.31 | 65.87 | +39.2% | +3.951 to +33.16 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.541 | -24.3% | -2.345 to -0.5723 | yes: GAIN |
| node-hours | 2.513 | 1.899 | -24.4% | -0.9819 to -0.2448 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.3 | -0.1% | -1.246 to +0.647 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 223.5 | -17.1% | -73.53 to -18.67 | yes: GAIN |
| response time (ms), mean | 213.2 | 185.1 | -13.2% | -45.88 to -10.34 | yes: GAIN |
| response time (ms), 95th percentile | 646.8 | 671.3 | +3.8% | -61.42 to +110.5 | no |
| response time (ms), 99th percentile | 933.7 | 983.1 | +5.3% | -26.97 to +125.7 | no |
| time over the response line (% of samples) | 8.805 | 8.8 | -0.1% | -0.7877 to +0.7774 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 5 | +4.2% | -0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.9 | +49.9 (native is 0) | +33.6 to +66.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.063 | 8.362 | +3.7% | -1.45 to +2.047 | no |
| utilisation (used / allocatable) | 0.05276 | 0.07086 | +34.3% | +0.006658 to +0.02955 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.266 | 1.255 | -0.9% | -0.04616 to +0.02268 | no |
| Omni's own CPU (cores), mean | 0 | 0.01461 | +0.0146 (native is 0) | +0.01319 to +0.01603 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.266 | 1.269 | +0.2% | -0.0321 to +0.03783 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.4 | 425.9 | -18.3% | -159.6 to -31.45 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.922 | 2.275 | +18.4% | +0.01102 to +0.6952 | yes: power given |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 35.9 | 36.92 | +2.8% | +0.5189 to +1.525 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 740.7 | 742.6 | +0.3% | -2.968 to +6.768 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.642 | -39.3% | -3.765 to -0.9511 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.0375 | +80.0% | -0.008467 to +0.0418 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 47.31 | 48.84 | +3.2% | -3.909 to +6.959 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.541 | -24.3% | -2.345 to -0.5723 | yes: GAIN |
| node-hours | 2.513 | 1.899 | -24.4% | -0.9852 to -0.2428 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.7 | 269.3 | -0.2% | -1.256 to +0.437 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.7 | 223.5 | -17.1% | -73.94 to -18.48 | yes: GAIN |
| response time (ms), mean | 230.4 | 185.1 | -19.7% | -75.77 to -14.83 | yes: GAIN |
| response time (ms), 95th percentile | 833.3 | 671.3 | -19.4% | -375.9 to +52.01 | no |
| response time (ms), 99th percentile | 1312 | 983.1 | -25.1% | -720.7 to +62.05 | no |
| time over the response line (% of samples) | 7.755 | 8.8 | +13.5% | -1.852 to +3.942 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.5 | 5 | -9.1% | -2.228 to +1.228 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.9 | +49.9 (native is 0) | +33.6 to +66.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.88 | 8.362 | -35.1% | -6.492 to -2.535 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05295 | 0.07086 | +33.8% | +0.006482 to +0.02936 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.271 | 1.255 | -1.3% | -0.04778 to +0.01551 | no |
| Omni's own CPU (cores), mean | 0 | 0.01461 | +0.0146 (native is 0) | +0.01319 to +0.01603 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.271 | 1.269 | -0.1% | -0.03383 to +0.03078 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 518 | 425.9 | -17.8% | -153.3 to -30.97 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.959 | 2.275 | +16.1% | -0.02581 to +0.6582 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 38.08 | 36.92 | -3.0% | -2.298 to -0.02312 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 756.2 | 742.6 | -1.8% | -25.92 to -1.279 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.642 | -39.3% | -3.765 to -0.9511 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6792 | 0.0375 | -94.5% | -0.7659 to -0.5174 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.2 | -83.3% | -1.477 to -0.5231 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 65.87 | 48.84 | -25.9% | -31.05 to -3.01 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.602 | -23.3% | -2.29 to -0.5066 | yes: GAIN |
| node-hours | 2.513 | 1.927 | -23.3% | -0.9582 to -0.2123 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.6 | 269.7 | +0.0% | -1.117 to +1.276 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.6 | 225.8 | -16.3% | -71.96 to -15.7 | yes: GAIN |
| response time (ms), mean | 213.2 | 207.5 | -2.7% | -33.98 to +22.62 | no |
| response time (ms), 95th percentile | 646.8 | 893.1 | +38.1% | -27.73 to +520.4 | no |
| response time (ms), 99th percentile | 933.7 | 1429 | +53.1% | -61.24 to +1053 | no |
| time over the response line (% of samples) | 8.805 | 8.228 | -6.6% | -4.326 to +3.172 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 5.8 | +20.8% | -0.5452 to +2.545 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.1 (native is 0) | +31.18 to +43.02 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.063 | 13.36 | +65.7% | +3.363 to +7.227 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05276 | 0.06948 | +31.7% | +0.0061 to +0.02734 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.266 | 1.249 | -1.4% | -0.07864 to +0.04401 | no |
| Omni's own CPU (cores), mean | 0 | 0.01588 | +0.0159 (native is 0) | +0.01361 to +0.01815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.266 | 1.265 | -0.1% | -0.06396 to +0.06108 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.4 | 433.1 | -16.9% | -148.9 to -27.76 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.922 | 2.094 | +9.0% | -0.01159 to +0.3572 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2911 to +1.091 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2911 to +1.091 | no |
| host CPU busy, the real machine under kind (%) | 35.9 | 38.75 | +7.9% | +1.782 to +3.91 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 740.7 | 758.6 | +2.4% | +1.858 to +33.94 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.75 | -37.5% | -3.608 to -0.8907 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.6833 | +3180.0% | +0.5754 to +0.7496 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 1.2 | +1100.0% | +0.8738 to +1.326 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 47.31 | 66.68 | +40.9% | +2.94 to +35.79 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*