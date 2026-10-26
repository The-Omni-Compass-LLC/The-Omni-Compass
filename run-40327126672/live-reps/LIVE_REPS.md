# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.375 | 5.228 |
| node-hours | 2.522 | 2.515 | 2.252 | 2.19 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.7 | 271.6 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.7 | 252 | 247.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 281.8 | 301.6 | 247.1 | 271.2 |
| response time (ms), 95th percentile | 864.7 | 955.7 | 910 | 1021 |
| response time (ms), 99th percentile | 1285 | 1458 | 1302 | 1508 |
| time over the response line (% of samples) | 15.11 | 15.69 | 14.47 | 15.76 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 8.8 | 9.2 | 8.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 38.5 | 52.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.827 | 10.07 | 9.69 | 9.928 |
| utilisation (used / allocatable) | 0.05799 | 0.05783 | 0.06487 | 0.06623 |
| CPU used (cores), mean | 1.392 | 1.388 | 1.388 | 1.378 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01593 | 0.01707 |
| CPU used with Omni's own (cores), mean | 1.392 | 1.388 | 1.404 | 1.395 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.4 | 475.5 | 434.8 | 430.1 |
| HPA replicas, mean | 2.042 | 2 | 2.028 | 2.186 |
| pods started | 0.2 | 0.1 | 0.5 | 0.5 |
| pod start wait, total (s) | 0.6 | 0.1 | 1.2 | 0.8 |
| pod start wait, mean (s) | 0.6 | 0.1 | 0.85 | 0.8 |
| host CPU busy, the real machine under kind (%) | 39.59 | 40.48 | 40.58 | 41.47 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 753.7 | 759.6 | 754.9 | 765 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.866 | 4.606 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.175 | 0.04583 | 0.2167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | 0.3 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 60.23 | 66.95 | 62.85 | 70.42 |
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
| worker nodes in service, mean | 6 | 5.228 | −12.9% | −1.4456 to −0.0975 | yes: GAIN |
| node-hours | 2.515 | 2.19 | −13.0% | −0.6104 to −0.0411 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.4 | −0.1% | −1.4352 to +0.7437 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 247.1 | −9.0% | −46.1505 to −3.0034 | yes: GAIN |
| response time (ms), mean | 301.6 | 271.2 | −10.1% | −43.8832 to −16.9092 | yes: GAIN |
| response time (ms), 95th percentile | 955.7 | 1021 | +6.8% | −13.8291 to +144.7291 | no |
| response time (ms), 99th percentile | 1458 | 1508 | +3.4% | −121.8718 to +221.1440 | no |
| time over the response line (% of samples) | 15.69 | 15.76 | +0.4% | −0.7020 to +0.8365 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.9 | +1.1% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.1 | +52.100 (native is 0) | +27.7879 to +76.4121 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 9.928 | −1.4% | −2.1805 to +1.8905 | no |
| utilisation (used / allocatable) | 0.05783 | 0.06623 | +14.5% | +0.0012 to +0.0157 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.388 | 1.378 | −0.7% | −0.0296 to +0.0089 | no |
| Omni's own CPU (cores), mean | 0 | 0.01707 | +0.017 (native is 0) | +0.0159 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.388 | 1.395 | +0.5% | −0.0129 to +0.0263 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.5 | 430.1 | −9.6% | −86.3807 to −4.5824 | yes, down (shown, not judged) |
| HPA replicas, mean | 2 | 2.186 | +9.3% | −0.0272 to +0.3989 | no |
| pods started | 0.1 | 0.5 | +400.0% | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.1 | 0.8 | +700.0% | +0.1111 to +1.2889 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 0.8 | +700.0% | +0.1111 to +1.2889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.48 | 41.47 | +2.4% | +0.6299 to +1.3386 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.6 | 765 | +0.7% | +2.0415 to +8.7585 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.606 | −23.2% | −2.5499 to −0.2388 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.2167 | +23.8% | −0.0145 to +0.0979 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1 | +25.0% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 66.95 | 70.42 | +5.2% | −0.7511 to +7.6845 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.522 | 2.515 | −0.3% | −0.0153 to +0.0026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.7 | −0.3% | −1.3839 to −0.0622 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.7 | −0.3% | −1.3839 to −0.0622 | yes: GAIN |
| response time (ms), mean | 281.8 | 301.6 | +7.0% | +5.9813 to +33.4850 | yes: LOSS |
| response time (ms), 95th percentile | 864.7 | 955.7 | +10.5% | +25.8098 to +156.2012 | yes: LOSS |
| response time (ms), 99th percentile | 1285 | 1458 | +13.5% | +45.0841 to +300.6791 | yes: LOSS |
| time over the response line (% of samples) | 15.11 | 15.69 | +3.8% | −0.7469 to +1.9023 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 8.8 | −1.1% | −0.7263 to +0.5263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.827 | 10.07 | +14.1% | −0.6302 to +3.1235 | no |
| utilisation (used / allocatable) | 0.05799 | 0.05783 | −0.3% | −0.0014 to +0.0011 | no |
| CPU used (cores), mean | 1.392 | 1.388 | −0.3% | −0.0342 to +0.0263 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.392 | 1.388 | −0.3% | −0.0342 to +0.0263 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.4 | 475.5 | +0.9% | −10.6152 to +18.9636 | no |
| HPA replicas, mean | 2.042 | 2 | −2.1% | −0.1592 to +0.0744 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.6 | 0.1 | −83.3% | −1.4685 to +0.4685 | no |
| pod start wait, mean (s) | 0.6 | 0.1 | −83.3% | −1.4685 to +0.4685 | no |
| host CPU busy, the real machine under kind (%) | 39.59 | 40.48 | +2.3% | +0.5746 to +1.2122 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 753.7 | 759.6 | +0.8% | +1.6421 to +10.1579 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.175 | +250.0% | +0.0806 to +0.1694 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | +166.7% | +0.1230 to +0.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 60.23 | 66.95 | +11.2% | +2.0680 to +11.3820 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.375 | −10.4% | −1.1958 to −0.0537 | yes: GAIN |
| node-hours | 2.522 | 2.252 | −10.7% | −0.5072 to −0.0318 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.6 | −0.3% | −1.6031 to −0.0471 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 252 | −7.5% | −38.3573 to −2.5137 | yes: GAIN |
| response time (ms), mean | 281.8 | 247.1 | −12.3% | −46.8751 to −22.5847 | yes: GAIN |
| response time (ms), 95th percentile | 864.7 | 910 | +5.2% | +5.4115 to +85.2865 | yes: LOSS |
| response time (ms), 99th percentile | 1285 | 1302 | +1.3% | −78.7813 to +112.6455 | no |
| time over the response line (% of samples) | 15.11 | 14.47 | −4.3% | −1.7949 to +0.5083 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.2 | +3.4% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 | +38.500 (native is 0) | +16.7716 to +60.2284 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.827 | 9.69 | +9.8% | −0.5945 to +2.3211 | no |
| utilisation (used / allocatable) | 0.05799 | 0.06487 | +11.8% | +0.0008 to +0.0129 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.388 | −0.3% | −0.0267 to +0.0197 | no |
| Omni's own CPU (cores), mean | 0 | 0.01593 | +0.016 (native is 0) | +0.0145 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.404 | +0.9% | −0.0115 to +0.0364 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.4 | 434.8 | −7.8% | −67.6631 to −5.4204 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.042 | 2.028 | −0.7% | −0.1937 to +0.1658 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.6 | 1.2 | +100.0% | −1.2531 to +2.4531 | no |
| pod start wait, mean (s) | 0.6 | 0.85 | +41.7% | −0.9803 to +1.4803 | no |
| host CPU busy, the real machine under kind (%) | 39.59 | 40.58 | +2.5% | +0.6787 to +1.3006 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 753.7 | 754.9 | +0.2% | −0.3379 to +2.7379 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.866 | −18.9% | −2.1340 to −0.1330 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.04583 | −8.3% | −0.0370 to +0.0286 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.23 | 62.85 | +4.4% | +0.4713 to +4.7704 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.375 | −10.4% | −1.1958 to −0.0537 | yes: GAIN |
| node-hours | 2.515 | 2.252 | −10.5% | −0.5062 to −0.0201 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 | −0.0% | −0.9514 to +0.7473 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 252 | −7.3% | −37.8758 to −1.5491 | yes: GAIN |
| response time (ms), mean | 301.6 | 247.1 | −18.1% | −70.2660 to −38.6601 | yes: GAIN |
| response time (ms), 95th percentile | 955.7 | 910 | −4.8% | −108.3739 to +17.0609 | no |
| response time (ms), 99th percentile | 1458 | 1302 | −10.7% | −326.5899 to +14.6909 | no |
| time over the response line (% of samples) | 15.69 | 14.47 | −7.8% | −2.3149 to −0.1271 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.2 | +4.5% | −0.4396 to +1.2396 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 | +38.500 (native is 0) | +16.7716 to +60.2284 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 9.69 | −3.8% | −2.2857 to +1.5190 | no |
| utilisation (used / allocatable) | 0.05783 | 0.06487 | +12.2% | −0.0001 to +0.0141 | no |
| CPU used (cores), mean | 1.388 | 1.388 | +0.0% | −0.0164 to +0.0173 | no |
| Omni's own CPU (cores), mean | 0 | 0.01593 | +0.016 (native is 0) | +0.0145 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.388 | 1.404 | +1.2% | +0.0002 to +0.0325 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.5 | 434.8 | −8.6% | −84.2893 to +2.8574 | no |
| HPA replicas, mean | 2 | 2.028 | +1.4% | −0.1000 to +0.1570 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.1 | 1.2 | +1100.0% | −0.5329 to +2.7329 | no |
| pod start wait, mean (s) | 0.1 | 0.85 | +750.0% | −0.2222 to +1.7222 | no |
| host CPU busy, the real machine under kind (%) | 40.48 | 40.58 | +0.2% | −0.1751 to +0.3676 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.6 | 754.9 | −0.6% | −8.3481 to −1.0519 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.866 | −18.9% | −2.1340 to −0.1330 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.04583 | −73.8% | −0.1942 to −0.0641 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.3 | −62.5% | −0.8770 to −0.1230 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 66.95 | 62.85 | −6.1% | −7.5504 to −0.6579 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.228 | −12.9% | −1.4456 to −0.0975 | yes: GAIN |
| node-hours | 2.522 | 2.19 | −13.2% | −0.6114 to −0.0528 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.4 | −0.4% | −1.7032 to −0.4343 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 247.1 | −9.3% | −46.6229 to −3.9771 | yes: GAIN |
| response time (ms), mean | 281.8 | 271.2 | −3.8% | −31.1847 to +9.8586 | no |
| response time (ms), 95th percentile | 864.7 | 1021 | +18.1% | +40.9558 to +271.9552 | yes: LOSS |
| response time (ms), 99th percentile | 1285 | 1508 | +17.3% | +43.5359 to +401.4995 | yes: LOSS |
| time over the response line (% of samples) | 15.11 | 15.76 | +4.3% | −0.6397 to +1.9295 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 8.9 | ±0.0% | −0.8260 to +0.8260 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.1 | +52.100 (native is 0) | +27.7879 to +76.4121 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.827 | 9.928 | +12.5% | −0.6433 to +2.8466 | no |
| utilisation (used / allocatable) | 0.05799 | 0.06623 | +14.2% | +0.0019 to +0.0146 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.378 | −1.0% | −0.0596 to +0.0310 | no |
| Omni's own CPU (cores), mean | 0 | 0.01707 | +0.017 (native is 0) | +0.0159 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.395 | +0.2% | −0.0433 to +0.0488 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.4 | 430.1 | −8.8% | −71.9982 to −10.6166 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.042 | 2.186 | +7.0% | −0.0420 to +0.3289 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.6 | 0.8 | +33.3% | −0.8556 to +1.2556 | no |
| pod start wait, mean (s) | 0.6 | 0.8 | +33.3% | −0.8556 to +1.2556 | no |
| host CPU busy, the real machine under kind (%) | 39.59 | 41.47 | +4.7% | +1.5633 to +2.1919 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 753.7 | 765 | +1.5% | +5.0092 to +17.5908 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.606 | −23.2% | −2.5499 to −0.2388 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.2167 | +333.3% | +0.1038 to +0.2295 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1 | +233.3% | +0.3545 to +1.0455 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 60.23 | 70.42 | +16.9% | +3.5521 to +16.8313 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*