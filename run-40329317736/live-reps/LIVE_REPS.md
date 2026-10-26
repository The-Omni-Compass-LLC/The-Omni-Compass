# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.796 | 4.717 |
| node-hours | 2.515 | 2.517 | 2.015 | 1.981 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.7 | 270.6 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 270.7 | 232.7 | 230.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 222.4 | 213.4 | 192.5 | 179.9 |
| response time (ms), 95th percentile | 641.1 | 685.5 | 697.7 | 680.6 |
| response time (ms), 99th percentile | 928.2 | 1030 | 967.2 | 1076 |
| time over the response line (% of samples) | 9.583 | 7.072 | 8.948 | 6.819 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 5.4 | 6.2 | 5.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 49.4 | 47.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.617 | 8.867 | 8.873 | 9.157 |
| utilisation (used / allocatable) | 0.05469 | 0.05433 | 0.06808 | 0.07061 |
| CPU used (cores), mean | 1.313 | 1.304 | 1.279 | 1.297 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01649 | 0.01594 |
| CPU used with Omni's own (cores), mean | 1.313 | 1.304 | 1.296 | 1.313 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.6 | 501.9 | 435.1 | 423 |
| HPA replicas, mean | 2.084 | 1.974 | 2.036 | 2.056 |
| pods started | 0 | 0.2 | 0.1 | 0.3 |
| pod start wait, total (s) | 0 | 0.3 | 0.1 | 0.5 |
| pod start wait, mean (s) | 0 | 0.15 | 0.1 | 0.35 |
| host CPU busy, the real machine under kind (%) | 37.5 | 37.79 | 38.29 | 38.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 741.6 | 740.8 | 741.9 | 740 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.984 | 3.854 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.0625 | 0.04167 | 0.05417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | 0.4 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 48.45 | 49.45 | 49.4 | 50.7 |
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
| worker nodes in service, mean | 6 | 4.717 | −21.4% | −2.1015 to −0.4651 | yes: GAIN |
| node-hours | 2.517 | 1.981 | −21.3% | −0.8798 to −0.1937 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 271.1 | +0.1% | +0.0308 to +0.7410 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 230.7 | −14.8% | −65.7418 to −14.2948 | yes: GAIN |
| response time (ms), mean | 213.4 | 179.9 | −15.7% | −42.6257 to −24.2990 | yes: GAIN |
| response time (ms), 95th percentile | 685.5 | 680.6 | −0.7% | −46.7117 to +36.9227 | no |
| response time (ms), 99th percentile | 1030 | 1076 | +4.4% | −34.1137 to +125.5503 | no |
| time over the response line (% of samples) | 7.072 | 6.819 | −3.6% | −0.8897 to +0.3829 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 5.7 | +5.6% | −1.0924 to +1.6924 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 | +47.300 (native is 0) | +36.9230 to +57.6770 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.867 | 9.157 | +3.3% | −1.0429 to +1.6229 | no |
| utilisation (used / allocatable) | 0.05433 | 0.07061 | +30.0% | +0.0058 to +0.0268 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.304 | 1.297 | −0.5% | −0.0273 to +0.0144 | no |
| Omni's own CPU (cores), mean | 0 | 0.01594 | +0.016 (native is 0) | +0.0143 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.304 | 1.313 | +0.7% | −0.0122 to +0.0312 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 501.9 | 423 | −15.7% | −132.4911 to −25.4430 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.974 | 2.056 | +4.1% | −0.0801 to +0.2430 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | −0.9081 to +1.3081 | no |
| pod start wait, mean (s) | 0.15 | 0.35 | +133.3% | −0.4786 to +0.8786 | no |
| host CPU busy, the real machine under kind (%) | 37.79 | 38.38 | +1.6% | +0.1612 to +1.0164 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 740.8 | 740 | −0.1% | −3.6771 to +2.0771 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.854 | −35.8% | −3.4628 to −0.8299 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05417 | −13.3% | −0.0391 to +0.0224 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 49.45 | 50.7 | +2.5% | −2.1733 to +4.6817 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.517 | +0.1% | −0.0045 to +0.0092 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.7 | +0.1% | −0.6472 to +1.1179 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 270.7 | +0.1% | −0.6472 to +1.1179 | no |
| response time (ms), mean | 222.4 | 213.4 | −4.1% | −27.4625 to +9.3378 | no |
| response time (ms), 95th percentile | 641.1 | 685.5 | +6.9% | −58.2501 to +146.8871 | no |
| response time (ms), 99th percentile | 928.2 | 1030 | +11.0% | −67.8943 to +272.0797 | no |
| time over the response line (% of samples) | 9.583 | 7.072 | −26.2% | −5.4562 to +0.4340 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 5.4 | −16.9% | −3.2709 to +1.0709 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.617 | 8.867 | +2.9% | −0.8108 to +1.3108 | no |
| utilisation (used / allocatable) | 0.05469 | 0.05433 | −0.7% | −0.0016 to +0.0009 | no |
| CPU used (cores), mean | 1.313 | 1.304 | −0.7% | −0.0379 to +0.0205 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.313 | 1.304 | −0.7% | −0.0379 to +0.0205 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.6 | 501.9 | +0.3% | −10.3500 to +12.9899 | no |
| HPA replicas, mean | 2.084 | 1.974 | −5.3% | −0.2619 to +0.0426 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.15 | +0.150 (native is 0) | −0.1893 to +0.4893 | no |
| host CPU busy, the real machine under kind (%) | 37.5 | 37.79 | +0.8% | −0.4670 to +1.0319 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 741.6 | 740.8 | −0.1% | −5.7189 to +4.1189 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.0625 | +50.0% | −0.0143 to +0.0560 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.3642 to +0.7642 | no |
| queue: job turnaround, submitted to done, mean (s) | 48.45 | 49.45 | +2.1% | −3.3638 to +5.3721 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.796 | −20.1% | −2.0133 to −0.3938 | yes: GAIN |
| node-hours | 2.515 | 2.015 | −19.9% | −0.8402 to −0.1604 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.6 | +0.1% | −0.4972 to +0.8506 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 232.7 | −13.9% | −63.3357 to −12.1067 | yes: GAIN |
| response time (ms), mean | 222.4 | 192.5 | −13.5% | −51.1647 to −8.7245 | yes: GAIN |
| response time (ms), 95th percentile | 641.1 | 697.7 | +8.8% | −61.0247 to +174.0947 | no |
| response time (ms), 99th percentile | 928.2 | 967.2 | +4.2% | −112.0461 to +190.1333 | no |
| time over the response line (% of samples) | 9.583 | 8.948 | −6.6% | −1.5115 to +0.2410 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.2 | −4.6% | −1.1953 to +0.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.4 | +49.400 (native is 0) | +33.3903 to +65.4097 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.617 | 8.873 | +3.0% | −1.7898 to +2.3032 | no |
| utilisation (used / allocatable) | 0.05469 | 0.06808 | +24.5% | +0.0035 to +0.0232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.313 | 1.279 | −2.6% | −0.0571 to −0.0100 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01649 | +0.016 (native is 0) | +0.0144 to +0.0186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.313 | 1.296 | −1.3% | −0.0405 to +0.0065 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.6 | 435.1 | −13.1% | −115.2134 to −15.8876 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.084 | 2.036 | −2.3% | −0.2366 to +0.1397 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 37.5 | 38.29 | +2.1% | +0.3138 to +1.2557 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 741.6 | 741.9 | +0.0% | −4.7473 to +5.3473 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.984 | −33.6% | −3.3342 to −0.6987 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.04167 | =0.0% | −0.0344 to +0.0344 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 48.45 | 49.4 | +2.0% | −3.9246 to +5.8330 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.796 | −20.1% | −2.0133 to −0.3938 | yes: GAIN |
| node-hours | 2.517 | 2.015 | −20.0% | −0.8406 to −0.1646 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.6 | −0.0% | −1.2106 to +1.0933 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 232.7 | −14.0% | −63.5731 to −12.3400 | yes: GAIN |
| response time (ms), mean | 213.4 | 192.5 | −9.8% | −39.2072 to −2.5573 | yes: GAIN |
| response time (ms), 95th percentile | 685.5 | 697.7 | +1.8% | −69.9087 to +94.3417 | no |
| response time (ms), 99th percentile | 1030 | 967.2 | −6.1% | −193.1433 to +67.0451 | no |
| time over the response line (% of samples) | 7.072 | 8.948 | +26.5% | −0.9278 to +4.6794 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 6.2 | +14.8% | −0.5821 to +2.1821 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.4 | +49.400 (native is 0) | +33.3903 to +65.4097 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.867 | 8.873 | +0.1% | −2.4240 to +2.4373 | no |
| utilisation (used / allocatable) | 0.05433 | 0.06808 | +25.3% | +0.0042 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.304 | 1.279 | −1.9% | −0.0673 to +0.0177 | no |
| Omni's own CPU (cores), mean | 0 | 0.01649 | +0.016 (native is 0) | +0.0144 to +0.0186 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.304 | 1.296 | −0.6% | −0.0516 to +0.0349 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 501.9 | 435.1 | −13.3% | −113.5301 to −20.2108 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.974 | 2.036 | +3.1% | −0.1305 to +0.2527 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.15 | 0.1 | −33.3% | −0.4782 to +0.3782 | no |
| host CPU busy, the real machine under kind (%) | 37.79 | 38.29 | +1.3% | −0.2507 to +1.2553 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 740.8 | 741.9 | +0.1% | −5.5459 to +7.7459 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.984 | −33.6% | −3.3342 to −0.6987 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.04167 | −33.3% | −0.0498 to +0.0081 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 49.45 | 49.4 | −0.1% | −5.5123 to +5.4123 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.717 | −21.4% | −2.1015 to −0.4651 | yes: GAIN |
| node-hours | 2.515 | 1.981 | −21.2% | −0.8775 to −0.1913 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 271.1 | +0.2% | −0.1273 to +1.3698 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 230.7 | −14.7% | −65.2677 to −14.2981 | yes: GAIN |
| response time (ms), mean | 222.4 | 179.9 | −19.1% | −61.8460 to −23.2035 | yes: GAIN |
| response time (ms), 95th percentile | 641.1 | 680.6 | +6.1% | −43.6406 to +122.4886 | no |
| response time (ms), 99th percentile | 928.2 | 1076 | +15.9% | −32.8649 to +328.4869 | no |
| time over the response line (% of samples) | 9.583 | 6.819 | −28.8% | −6.1853 to +0.6563 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 5.7 | −12.3% | −1.9081 to +0.3081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 | +47.300 (native is 0) | +36.9230 to +57.6770 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.617 | 9.157 | +6.3% | −0.7985 to +1.8785 | no |
| utilisation (used / allocatable) | 0.05469 | 0.07061 | +29.1% | +0.0049 to +0.0270 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.313 | 1.297 | −1.2% | −0.0494 to +0.0191 | no |
| Omni's own CPU (cores), mean | 0 | 0.01594 | +0.016 (native is 0) | +0.0143 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.313 | 1.313 | +0.1% | −0.0338 to +0.0355 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.6 | 423 | −15.5% | −137.0951 to −18.1991 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.084 | 2.056 | −1.4% | −0.1973 to +0.1410 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.350 (native is 0) | −0.1845 to +0.8845 | no |
| host CPU busy, the real machine under kind (%) | 37.5 | 38.38 | +2.3% | +0.0764 to +1.6661 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 741.6 | 740 | −0.2% | −5.9209 to +2.7209 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.854 | −35.8% | −3.4628 to −0.8299 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05417 | +30.0% | −0.0120 to +0.0370 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 48.45 | 50.7 | +4.7% | −3.1127 to +7.6294 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*