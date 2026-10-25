# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.642 | 4.054 |
| node-hours | 2.516 | 2.514 | 1.949 | 1.696 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 269.9 | 270.3 | 269.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 269.9 | 227.6 | 208.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 205.8 | 168 | 175.3 | 131.3 |
| response time (ms), 95th percentile | 555.8 | 354.5 | 601.7 | 360.9 |
| response time (ms), 99th percentile | 824.2 | 552.1 | 852.4 | 599 |
| time over the response line (% of samples) | 6.389 | 3.375 | 6.603 | 3.789 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 2.7 | 5.3 | 2.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 55.7 | 40.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.943 | 11.31 | 7.517 | 11.87 |
| utilisation (used / allocatable) | 0.05387 | 0.0534 | 0.06909 | 0.07778 |
| CPU used (cores), mean | 1.293 | 1.282 | 1.265 | 1.235 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01563 | 0.01543 |
| CPU used with Omni's own (cores), mean | 1.293 | 1.282 | 1.28 | 1.251 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.2 | 508.5 | 430.4 | 402.7 |
| HPA replicas, mean | 1.899 | 1.998 | 2.068 | 2.13 |
| pods started | 0 | 0.1 | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.2 | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.2 | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 36.46 | 37.47 | 37.56 | 38.29 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 737.2 | 742.9 | 737.9 | 743.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.556 | 2.933 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.6042 | 0.025 | 0.6417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.1 | 0.1 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 44.73 | 50.48 | 45.39 | 52.06 |
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
| worker nodes in service, mean | 6 | 4.054 | −32.4% | −2.6948 to −1.1967 | yes: GAIN |
| node-hours | 2.514 | 1.696 | −32.5% | −1.1300 to −0.5042 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 269.2 | −0.3% | −1.4282 to +0.0214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 208.1 | −22.9% | −85.3532 to −38.1453 | yes: GAIN |
| response time (ms), mean | 168 | 131.3 | −21.8% | −45.8103 to −27.4709 | yes: GAIN |
| response time (ms), 95th percentile | 354.5 | 360.9 | +1.8% | −44.6720 to +57.2940 | no |
| response time (ms), 99th percentile | 552.1 | 599 | +8.5% | −57.5231 to +151.3403 | no |
| time over the response line (% of samples) | 3.375 | 3.789 | +12.3% | −0.6283 to +1.4564 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 2.8 | +3.7% | −0.6113 to +0.8113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.5 | +40.500 (native is 0) | +27.7744 to +53.2256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 11.87 | +4.9% | −1.3685 to +2.4752 | no |
| utilisation (used / allocatable) | 0.0534 | 0.07778 | +45.6% | +0.0144 to +0.0344 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.282 | 1.235 | −3.6% | −0.0862 to −0.0066 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01543 | +0.015 (native is 0) | +0.0139 to +0.0170 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.282 | 1.251 | −2.4% | −0.0719 to +0.0099 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.5 | 402.7 | −20.8% | −148.3042 to −63.1846 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.13 | +6.6% | −0.1041 to +0.3673 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 37.47 | 38.29 | +2.2% | +0.5058 to +1.1481 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 742.9 | 743.5 | +0.1% | −2.6025 to +3.8025 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.933 | −51.1% | −4.2350 to −1.8996 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6042 | 0.6417 | +6.2% | −0.0690 to +0.1440 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1 | −9.1% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 50.48 | 52.06 | +3.1% | −0.1712 to +3.3295 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0092 to +0.0049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 269.9 | −0.2% | −1.3078 to +0.4883 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 269.9 | −0.2% | −1.3078 to +0.4883 | no |
| response time (ms), mean | 205.8 | 168 | −18.4% | −70.5659 to −5.0795 | yes: GAIN |
| response time (ms), 95th percentile | 555.8 | 354.5 | −36.2% | −370.1423 to −32.2957 | yes: GAIN |
| response time (ms), 99th percentile | 824.2 | 552.1 | −33.0% | −486.4186 to −57.8392 | yes: GAIN |
| time over the response line (% of samples) | 6.389 | 3.375 | −47.2% | −6.4156 to +0.3880 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 2.7 | −41.3% | −3.6342 to −0.1658 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.943 | 11.31 | +42.4% | +1.8502 to +4.8898 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05387 | 0.0534 | −0.9% | −0.0014 to +0.0005 | no |
| CPU used (cores), mean | 1.293 | 1.282 | −0.9% | −0.0341 to +0.0117 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.293 | 1.282 | −0.9% | −0.0341 to +0.0117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.2 | 508.5 | +1.0% | −2.9380 to +13.3609 | no |
| HPA replicas, mean | 1.899 | 1.998 | +5.2% | −0.0025 to +0.2012 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 36.46 | 37.47 | +2.8% | +0.8016 to +1.2193 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 737.2 | 742.9 | +0.8% | +2.5359 to +8.8641 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.6042 | +2316.7% | +0.5083 to +0.6500 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.1 | +450.0% | +0.6738 to +1.1262 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 44.73 | 50.48 | +12.8% | +0.0474 to +11.4442 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.642 | −22.6% | −1.9535 to −0.7615 | yes: GAIN |
| node-hours | 2.516 | 1.949 | −22.5% | −0.8164 to −0.3168 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 270.3 | +0.0% | −0.4324 to +0.5884 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 227.6 | −15.8% | −61.5470 to −23.7845 | yes: GAIN |
| response time (ms), mean | 205.8 | 175.3 | −14.8% | −40.8150 to −20.2379 | yes: GAIN |
| response time (ms), 95th percentile | 555.8 | 601.7 | +8.3% | +3.5169 to +88.4501 | yes: LOSS |
| response time (ms), 99th percentile | 824.2 | 852.4 | +3.4% | −2.5631 to +58.8523 | no |
| time over the response line (% of samples) | 6.389 | 6.603 | +3.3% | −0.3239 to +0.7515 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 5.3 | +15.2% | −0.1953 to +1.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.7 | +55.700 (native is 0) | +37.5349 to +73.8651 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.943 | 7.517 | −5.4% | −2.0639 to +1.2106 | no |
| utilisation (used / allocatable) | 0.05387 | 0.06909 | +28.3% | +0.0080 to +0.0224 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.293 | 1.265 | −2.2% | −0.0581 to +0.0020 | no |
| Omni's own CPU (cores), mean | 0 | 0.01563 | +0.016 (native is 0) | +0.0139 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.293 | 1.28 | −1.0% | −0.0430 to +0.0182 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.2 | 430.4 | −14.5% | −106.8735 to −38.8269 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.899 | 2.068 | +8.9% | +0.0028 to +0.3366 | yes: power given |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 36.46 | 37.56 | +3.0% | +0.7652 to +1.4461 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 737.2 | 737.9 | +0.1% | −0.1294 to +1.5294 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.556 | −40.7% | −3.3973 to −1.4909 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.025 | ±0.0% | −0.0314 to +0.0314 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 44.73 | 45.39 | +1.5% | −0.1358 to +1.4525 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.642 | −22.6% | −1.9535 to −0.7615 | yes: GAIN |
| node-hours | 2.514 | 1.949 | −22.5% | −0.8133 to −0.3155 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 270.3 | +0.2% | −0.3147 to +1.2902 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 227.6 | −15.7% | −61.1814 to −23.3306 | yes: GAIN |
| response time (ms), mean | 168 | 175.3 | +4.3% | −23.2319 to +37.8245 | no |
| response time (ms), 95th percentile | 354.5 | 601.7 | +69.7% | +66.3176 to +428.0874 | yes: LOSS |
| response time (ms), 99th percentile | 552.1 | 852.4 | +54.4% | +77.6332 to +522.9138 | yes: LOSS |
| time over the response line (% of samples) | 3.375 | 6.603 | +95.6% | −0.2708 to +6.7261 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 5.3 | +96.3% | +0.7779 to +4.4221 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.7 | +55.700 (native is 0) | +37.5349 to +73.8651 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 7.517 | −33.6% | −5.5954 to −1.9980 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0534 | 0.06909 | +29.4% | +0.0088 to +0.0226 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.282 | 1.265 | −1.3% | −0.0487 to +0.0151 | no |
| Omni's own CPU (cores), mean | 0 | 0.01563 | +0.016 (native is 0) | +0.0139 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.282 | 1.28 | −0.1% | −0.0332 to +0.0308 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.5 | 430.4 | −15.4% | −110.1670 to −45.9563 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.068 | +3.5% | −0.1152 to +0.2559 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 37.47 | 37.56 | +0.3% | −0.2872 to +0.4777 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 742.9 | 737.9 | −0.7% | −7.6764 to −2.3236 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.556 | −40.7% | −3.3973 to −1.4909 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6042 | 0.025 | −95.9% | −0.6514 to −0.5069 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.1 | −90.9% | −1.3372 to −0.6628 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 50.48 | 45.39 | −10.1% | −10.4788 to +0.3038 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.054 | −32.4% | −2.6948 to −1.1967 | yes: GAIN |
| node-hours | 2.516 | 1.696 | −32.6% | −1.1327 to −0.5059 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 269.2 | −0.4% | −1.9338 to −0.2925 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 208.1 | −23.0% | −86.0203 to −38.2977 | yes: GAIN |
| response time (ms), mean | 205.8 | 131.3 | −36.2% | −103.2299 to −45.6967 | yes: GAIN |
| response time (ms), 95th percentile | 555.8 | 360.9 | −35.1% | −319.3706 to −70.4454 | yes: GAIN |
| response time (ms), 99th percentile | 824.2 | 599 | −27.3% | −344.2694 to −106.1712 | yes: GAIN |
| time over the response line (% of samples) | 6.389 | 3.789 | −40.7% | −5.1644 to −0.0352 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 2.8 | −39.1% | −3.3744 to −0.2256 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.5 | +40.500 (native is 0) | +27.7744 to +53.2256 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.943 | 11.87 | +49.4% | +2.4812 to +5.3655 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05387 | 0.07778 | +44.4% | +0.0145 to +0.0333 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.293 | 1.235 | −4.5% | −0.1052 to −0.0100 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01543 | +0.015 (native is 0) | +0.0139 to +0.0170 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.293 | 1.251 | −3.3% | −0.0907 to +0.0063 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.2 | 402.7 | −20.0% | −138.6993 to −62.3666 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.899 | 2.13 | +12.2% | +0.0002 to +0.4617 | yes: power given |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 36.46 | 38.29 | +5.0% | +1.6075 to +2.0673 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 737.2 | 743.5 | +0.9% | +0.8414 to +11.7586 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 2.933 | −51.1% | −4.2350 to −1.8996 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.6417 | +2466.7% | +0.5326 to +0.7007 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1 | +400.0% | +0.4984 to +1.1016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 44.73 | 52.06 | +16.4% | −0.0511 to +14.7011 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*