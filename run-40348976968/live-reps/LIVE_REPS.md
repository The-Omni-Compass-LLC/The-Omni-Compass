# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.232 | 5.423 |
| node-hours | 2.515 | 2.516 | 2.193 | 2.274 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | 272.1 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.7 | 247.9 | 253.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 304.1 | 285.7 | 273.4 | 244.2 |
| response time (ms), 95th percentile | 966.7 | 1030 | 1009 | 1032 |
| response time (ms), 99th percentile | 1469 | 1554 | 1456 | 1578 |
| time over the response line (% of samples) | 16.73 | 12.4 | 16.67 | 11.86 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.2 | 9.1 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 32.5 | 32.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.837 | 11.05 | 9.808 | 11.06 |
| utilisation (used / allocatable) | 0.05911 | 0.05739 | 0.06776 | 0.06476 |
| CPU used (cores), mean | 1.419 | 1.377 | 1.407 | 1.381 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01641 | 0.01573 |
| CPU used with Omni's own (cores), mean | 1.419 | 1.377 | 1.423 | 1.397 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 477.7 | 421.8 | 439.8 |
| HPA replicas, mean | 1.982 | 1.941 | 2.028 | 2.155 |
| pods started | 0 | 0 | 0.2 | 0.4 |
| pod start wait, total (s) | 0 | 0 | 0.5 | 0.5 |
| pod start wait, mean (s) | 0 | 0 | 0.5 | 0.4 |
| host CPU busy, the real machine under kind (%) | 40.28 | 39.81 | 41.09 | 40.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 760.4 | 755.9 | 763.8 | 758.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.606 | 5.069 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.075 | 0.05833 | 0.075 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | 0.5 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 67.51 | 65.26 | 71.63 | 67.74 |
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
| worker nodes in service, mean | 6 | 5.423 | −9.6% | −1.2766 to +0.1228 | no |
| node-hours | 2.516 | 2.274 | −9.6% | −0.5320 to +0.0482 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.7 | −0.0% | −0.8629 to +0.8623 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 253.6 | −6.7% | −39.7403 to +3.5564 | no |
| response time (ms), mean | 285.7 | 244.2 | −14.5% | −61.7862 to −21.3349 | yes: GAIN |
| response time (ms), 95th percentile | 1030 | 1032 | +0.2% | −104.8392 to +107.9722 | no |
| response time (ms), 99th percentile | 1554 | 1578 | +1.6% | −153.1464 to +201.6104 | no |
| time over the response line (% of samples) | 12.4 | 11.86 | −4.4% | −1.6069 to +0.5150 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.1 | −1.2% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.7 | +32.700 (native is 0) | +24.0697 to +41.3303 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 11.06 | +0.1% | −1.7114 to +1.7280 | no |
| utilisation (used / allocatable) | 0.05739 | 0.06476 | +12.8% | −0.0015 to +0.0162 | no |
| CPU used (cores), mean | 1.377 | 1.381 | +0.2% | −0.0177 to +0.0245 | no |
| Omni's own CPU (cores), mean | 0 | 0.01573 | +0.016 (native is 0) | +0.0137 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.377 | 1.397 | +1.4% | −0.0032 to +0.0414 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.7 | 439.8 | −7.9% | −81.6838 to +5.9294 | no |
| HPA replicas, mean | 1.941 | 2.155 | +11.0% | +0.0959 to +0.3330 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 39.81 | 40.75 | +2.4% | +0.6661 to +1.2081 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.9 | 758.7 | +0.4% | −1.0120 to +6.6120 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.069 | −15.5% | −2.0277 to +0.1665 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.075 | ±0.0% | −0.0716 to +0.0716 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.5840 to +0.5840 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.26 | 67.74 | +3.8% | −0.5875 to +5.5375 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.516 | +0.0% | −0.0068 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | −0.1% | −1.0826 to +0.4617 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.7 | −0.1% | −1.0826 to +0.4617 | no |
| response time (ms), mean | 304.1 | 285.7 | −6.1% | −34.7168 to −2.1302 | yes: GAIN |
| response time (ms), 95th percentile | 966.7 | 1030 | +6.5% | −14.1544 to +140.7094 | no |
| response time (ms), 99th percentile | 1469 | 1554 | +5.8% | −47.1170 to +217.0652 | no |
| time over the response line (% of samples) | 16.73 | 12.4 | −25.9% | −6.9056 to −1.7479 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.2 | −6.8% | −1.5048 to +0.3048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.837 | 11.05 | +12.4% | −0.5745 to +3.0112 | no |
| utilisation (used / allocatable) | 0.05911 | 0.05739 | −2.9% | −0.0024 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.377 | −2.9% | −0.0587 to −0.0235 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.419 | 1.377 | −2.9% | −0.0587 to −0.0235 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 477.7 | +2.8% | +6.8591 to +18.9676 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.982 | 1.941 | −2.1% | −0.1398 to +0.0576 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.28 | 39.81 | −1.2% | −0.7619 to −0.1723 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 760.4 | 755.9 | −0.6% | −11.6232 to +2.6232 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.075 | +5.9% | −0.0594 to +0.0677 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.51 | 65.26 | −3.3% | −6.0973 to +1.5973 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.232 | −12.8% | −1.4325 to −0.1043 | yes: GAIN |
| node-hours | 2.515 | 2.193 | −12.8% | −0.5980 to −0.0448 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.1 | +0.0% | −0.5032 to +0.6007 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 247.9 | −8.9% | −44.9209 to −3.2400 | yes: GAIN |
| response time (ms), mean | 304.1 | 273.4 | −10.1% | −38.8429 to −22.7305 | yes: GAIN |
| response time (ms), 95th percentile | 966.7 | 1009 | +4.4% | −8.4232 to +94.0592 | no |
| response time (ms), 99th percentile | 1469 | 1456 | −0.9% | −118.6586 to +92.8866 | no |
| time over the response line (% of samples) | 16.73 | 16.67 | −0.4% | −0.8094 to +0.6819 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.1 | +3.4% | −0.8209 to +1.4209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.5 | +32.500 (native is 0) | +19.3482 to +45.6518 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.837 | 9.808 | −0.3% | −1.8286 to +1.7719 | no |
| utilisation (used / allocatable) | 0.05911 | 0.06776 | +14.6% | +0.0010 to +0.0163 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.419 | 1.407 | −0.8% | −0.0385 to +0.0147 | no |
| Omni's own CPU (cores), mean | 0 | 0.01641 | +0.016 (native is 0) | +0.0147 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.423 | +0.3% | −0.0223 to +0.0313 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 421.8 | −9.2% | −82.1919 to −3.7550 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.982 | 2.028 | +2.3% | −0.0505 to +0.1417 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 40.28 | 41.09 | +2.0% | +0.3884 to +1.2405 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 760.4 | 763.8 | +0.4% | −1.3949 to +8.1949 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.606 | −23.2% | −2.5234 to −0.2652 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.05833 | −17.6% | −0.0441 to +0.0191 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.51 | 71.63 | +6.1% | −0.1606 to +8.3940 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.232 | −12.8% | −1.4325 to −0.1043 | yes: GAIN |
| node-hours | 2.516 | 2.193 | −12.8% | −0.5977 to −0.0468 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.1 | +0.1% | −0.5451 to +1.2635 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 247.9 | −8.7% | −44.5635 to −2.9764 | yes: GAIN |
| response time (ms), mean | 285.7 | 273.4 | −4.3% | −29.7987 to +5.0724 | no |
| response time (ms), 95th percentile | 1030 | 1009 | −2.0% | −83.2356 to +42.3166 | no |
| response time (ms), 99th percentile | 1554 | 1456 | −6.3% | −218.1285 to +22.4083 | no |
| time over the response line (% of samples) | 12.4 | 16.67 | +34.4% | +1.6424 to +6.8835 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 9.1 | +11.0% | −0.0204 to +1.8204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.5 | +32.500 (native is 0) | +19.3482 to +45.6518 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.05 | 9.808 | −11.3% | −2.6058 to +0.1125 | no |
| utilisation (used / allocatable) | 0.05739 | 0.06776 | +18.1% | +0.0028 to +0.0179 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.377 | 1.407 | +2.1% | +0.0003 to +0.0582 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01641 | +0.016 (native is 0) | +0.0147 to +0.0181 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.377 | 1.423 | +3.3% | +0.0164 to +0.0748 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 477.7 | 421.8 | −11.7% | −96.1817 to −15.5918 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.941 | 2.028 | +4.5% | −0.0557 to +0.2290 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 39.81 | 41.09 | +3.2% | +0.8556 to +1.7075 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.9 | 763.8 | +1.0% | −0.4313 to +16.2313 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.606 | −23.2% | −2.5234 to −0.2652 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.05833 | −22.2% | −0.0829 to +0.0495 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.26 | 71.63 | +9.8% | +0.2211 to +12.5122 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.423 | −9.6% | −1.2766 to +0.1228 | no |
| node-hours | 2.515 | 2.274 | −9.6% | −0.5323 to +0.0502 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | −0.1% | −0.9540 to +0.3325 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 253.6 | −6.8% | −40.0222 to +3.2174 | no |
| response time (ms), mean | 304.1 | 244.2 | −19.7% | −77.3946 to −42.5735 | yes: GAIN |
| response time (ms), 95th percentile | 966.7 | 1032 | +6.7% | −15.3135 to +145.0015 | no |
| response time (ms), 99th percentile | 1469 | 1578 | +7.4% | −37.0263 to +255.4385 | no |
| time over the response line (% of samples) | 16.73 | 11.86 | −29.1% | −7.6970 to −2.0483 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.1 | −8.0% | −1.4578 to +0.0578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.7 | +32.700 (native is 0) | +24.0697 to +41.3303 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.837 | 11.06 | +12.5% | −0.8228 to +3.2761 | no |
| utilisation (used / allocatable) | 0.05911 | 0.06476 | +9.6% | −0.0036 to +0.0149 | no |
| CPU used (cores), mean | 1.419 | 1.381 | −2.7% | −0.0594 to −0.0160 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01573 | +0.016 (native is 0) | +0.0137 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.397 | −1.5% | −0.0444 to +0.0005 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.8 | 439.8 | −5.4% | −70.4900 to +20.5622 | no |
| HPA replicas, mean | 1.982 | 2.155 | +8.7% | +0.0078 to +0.3387 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| host CPU busy, the real machine under kind (%) | 40.28 | 40.75 | +1.2% | +0.1748 to +0.7652 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 760.4 | 758.7 | −0.2% | −6.7247 to +3.3247 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.069 | −15.5% | −2.0277 to +0.1665 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.075 | +5.9% | −0.0342 to +0.0425 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.51 | 67.74 | +0.3% | −3.0093 to +3.4593 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*