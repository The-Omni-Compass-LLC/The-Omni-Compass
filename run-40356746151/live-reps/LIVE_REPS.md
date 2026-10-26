# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.02 | 11.42 |
| node-hours | 5.024 | 5.025 | 4.623 | 4.776 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 526.7 | 526 | 527.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 526.7 | 495.2 | 509.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 568 | 916 | 546.4 | 1026 |
| response time (ms), 95th percentile | 2257 | 3778 | 2440 | 4307 |
| response time (ms), 99th percentile | 3309 | 5143 | 3554 | 5677 |
| time over the response line (% of samples) | 23.31 | 30.02 | 22.89 | 33.29 |
| failed requests (%) | 0 | 0.05418 | 0 | 0.118 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 14.3 | 11.6 | 16.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 66.6 | 43.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 24.77 | 14.1 | 20.03 |
| utilisation (used / allocatable) | 0.03442 | 0.03679 | 0.03741 | 0.04069 |
| CPU used (cores), mean | 1.652 | 1.766 | 1.642 | 1.868 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01205 | 0.01237 |
| CPU used with Omni's own (cores), mean | 1.652 | 1.766 | 1.654 | 1.88 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.3 | 735.2 | 728 | 663.7 |
| HPA replicas, mean | 3.938 | 4.082 | 4.233 | 4.198 |
| pods started | 0.1 | 0.4 | 0.3 | 1 |
| pod start wait, total (s) | 0.3 | 0.8 | 0.4 | 1.9 |
| pod start wait, mean (s) | 0.3 | 0.4 | 0.4 | 1.35 |
| host CPU busy, the real machine under kind (%) | 49.9 | 58.18 | 51.22 | 61.37 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 850.9 | 993.1 | 867.4 | 1032 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.4 | 10.84 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 7.796 | 0.0625 | 7.471 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 52.9 | 0.5 | 48.3 |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 269.7 | 173.8 | 322 |
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
| worker nodes in service, mean | 12 | 11.42 | −4.8% | −1.3912 to +0.2282 | no |
| node-hours | 5.025 | 4.776 | −4.9% | −0.5775 to +0.0809 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 527.9 | +0.2% | −0.2523 to +2.6316 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 509.6 | −3.2% | −41.3561 to +7.1396 | no |
| response time (ms), mean | 916 | 1026 | +12.0% | +61.6646 to +158.0537 | yes: LOSS |
| response time (ms), 95th percentile | 3778 | 4307 | +14.0% | +299.4200 to +758.3260 | yes: LOSS |
| response time (ms), 99th percentile | 5143 | 5677 | +10.4% | +222.9071 to +843.9447 | yes: LOSS |
| time over the response line (% of samples) | 30.02 | 33.29 | +10.9% | −0.6304 to +7.1644 | no |
| failed requests (%) | 0.05418 | 0.118 | +117.9% | −0.0634 to +0.1911 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 16.9 | +18.2% | −0.2850 to +5.4850 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.9 | +43.900 (native is 0) | +21.2538 to +66.5462 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.77 | 20.03 | −19.2% | −15.5249 to +6.0315 | no |
| utilisation (used / allocatable) | 0.03679 | 0.04069 | +10.6% | +0.0013 to +0.0065 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.766 | 1.868 | +5.8% | +0.0553 to +0.1485 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01237 | +0.012 (native is 0) | +0.0119 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.766 | 1.88 | +6.5% | +0.0677 to +0.1608 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 735.2 | 663.7 | −9.7% | −126.6045 to −16.2729 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.082 | 4.198 | +2.8% | −0.1989 to +0.4312 | no |
| pods started | 0.4 | 1 | +150.0% | −0.4228 to +1.6228 | no |
| pod start wait, total (s) | 0.8 | 1.9 | +137.5% | −0.9358 to +3.1358 | no |
| pod start wait, mean (s) | 0.4 | 1.35 | +237.5% | −0.1614 to +2.0614 | no |
| host CPU busy, the real machine under kind (%) | 58.18 | 61.37 | +5.5% | +2.3319 to +4.0509 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 993.1 | 1032 | +3.9% | +23.2199 to +54.7801 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.84 | −9.7% | −2.7718 to +0.4495 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.796 | 7.471 | −4.2% | −4.8448 to +4.1948 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 52.9 | 48.3 | −8.7% | −21.2298 to +12.0298 | no |
| queue: job turnaround, submitted to done, mean (s) | 269.7 | 322 | +19.4% | +39.8506 to +64.7161 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.024 | 5.025 | +0.0% | −0.0185 to +0.0192 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 526.7 | +0.3% | −0.7438 to +4.0239 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 526.7 | +0.3% | −0.7438 to +4.0239 | no |
| response time (ms), mean | 568 | 916 | +61.3% | +176.4358 to +519.5253 | yes: LOSS |
| response time (ms), 95th percentile | 2257 | 3778 | +67.4% | +799.9343 to +2243.8097 | yes: LOSS |
| response time (ms), 99th percentile | 3309 | 5143 | +55.4% | +922.1112 to +2745.3028 | yes: LOSS |
| time over the response line (% of samples) | 23.31 | 30.02 | +28.8% | +3.6511 to +9.7812 | yes: LOSS |
| failed requests (%) | 0 | 0.05418 | +0.054 (native is 0) | −0.0104 to +0.1188 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 14.3 | +31.2% | +1.2356 to +5.5644 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 24.77 | +131.2% | +1.2629 to +26.8538 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03442 | 0.03679 | +6.9% | +0.0007 to +0.0040 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.652 | 1.766 | +6.9% | +0.0338 to +0.1939 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.652 | 1.766 | +6.9% | +0.0338 to +0.1939 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.3 | 735.2 | −4.9% | −68.3837 to −7.7841 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.938 | 4.082 | +3.7% | −0.0050 to +0.2940 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.3786 to +0.9786 | no |
| pod start wait, total (s) | 0.3 | 0.8 | +166.7% | −1.0174 to +2.0174 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.8946 to +1.0946 | no |
| host CPU busy, the real machine under kind (%) | 49.9 | 58.18 | +16.6% | +5.8386 to +10.7143 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 850.9 | 993.1 | +16.7% | +75.9820 to +208.4180 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 7.796 | +16909.1% | +0.2920 to +15.2080 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 52.9 | +26350.0% | −11.8391 to +117.2391 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 269.7 | +64.0% | +54.9702 to +155.6632 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.02 | −8.2% | −2.3623 to +0.3990 | no |
| node-hours | 5.024 | 4.623 | −8.0% | −0.9892 to +0.1857 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 526 | +0.2% | −1.1704 to +2.9116 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 495.2 | −5.7% | −74.7933 to +15.0262 | no |
| response time (ms), mean | 568 | 546.4 | −3.8% | −33.1662 to −10.0272 | yes: GAIN |
| response time (ms), 95th percentile | 2257 | 2440 | +8.2% | +89.2706 to +278.5644 | yes: LOSS |
| response time (ms), 99th percentile | 3309 | 3554 | +7.4% | +67.4070 to +420.9508 | yes: LOSS |
| time over the response line (% of samples) | 23.31 | 22.89 | −1.8% | −1.2398 to +0.4043 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.6 | +6.4% | −0.1953 to +1.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.6 | +66.600 (native is 0) | +26.6861 to +106.5139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 14.1 | +31.6% | +1.3335 to +5.4465 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03442 | 0.03741 | +8.7% | −0.0007 to +0.0066 | no |
| CPU used (cores), mean | 1.652 | 1.642 | −0.6% | −0.0643 to +0.0437 | no |
| Omni's own CPU (cores), mean | 0 | 0.01205 | +0.012 (native is 0) | +0.0114 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.652 | 1.654 | +0.1% | −0.0525 to +0.0559 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.3 | 728 | −5.9% | −100.0167 to +9.5286 | no |
| HPA replicas, mean | 3.938 | 4.233 | +7.5% | +0.1385 to +0.4526 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.8204 to +1.0204 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.8204 to +1.0204 | no |
| host CPU busy, the real machine under kind (%) | 49.9 | 51.22 | +2.6% | +0.4424 to +2.1947 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 850.9 | 867.4 | +1.9% | +6.3210 to +26.6790 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.4 | −13.3% | −3.7737 to +0.5728 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.0625 | +36.4% | −0.0183 to +0.0517 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 173.8 | +5.7% | +3.6869 to +15.1047 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.02 | −8.2% | −2.3623 to +0.3990 | no |
| node-hours | 5.025 | 4.623 | −8.0% | −0.9821 to +0.1780 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 526 | −0.1% | −2.0811 to +0.5422 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 495.2 | −6.0% | −74.9112 to +11.8639 | no |
| response time (ms), mean | 916 | 546.4 | −40.3% | −540.0969 to −199.0576 | yes: GAIN |
| response time (ms), 95th percentile | 3778 | 2440 | −35.4% | −1987.7121 to −688.1969 | yes: GAIN |
| response time (ms), 99th percentile | 5143 | 3554 | −30.9% | −2411.5892 to −767.4670 | yes: GAIN |
| time over the response line (% of samples) | 30.02 | 22.89 | −23.8% | −10.4024 to −3.8654 | yes: GAIN |
| failed requests (%) | 0.05418 | 0 | −100.0% | −0.1188 to +0.0104 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.3 | 11.6 | −18.9% | −4.0924 to −1.3076 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.6 | +66.600 (native is 0) | +26.6861 to +106.5139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.77 | 14.1 | −43.1% | −23.7735 to +2.4368 | no |
| utilisation (used / allocatable) | 0.03679 | 0.03741 | +1.7% | −0.0041 to +0.0053 | no |
| CPU used (cores), mean | 1.766 | 1.642 | −7.0% | −0.1845 to −0.0639 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01205 | +0.012 (native is 0) | +0.0114 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.766 | 1.654 | −6.3% | −0.1722 to −0.0520 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 735.2 | 728 | −1.0% | −80.9569 to +66.6367 | no |
| HPA replicas, mean | 4.082 | 4.233 | +3.7% | −0.1013 to +0.4033 | no |
| pods started | 0.4 | 0.3 | −25.0% | −0.8872 to +0.6872 | no |
| pod start wait, total (s) | 0.8 | 0.4 | −50.0% | −1.8775 to +1.0775 | no |
| pod start wait, mean (s) | 0.4 | 0.4 | ±0.0% | −0.9079 to +0.9079 | no |
| host CPU busy, the real machine under kind (%) | 58.18 | 51.22 | −12.0% | −8.7324 to −5.1834 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 993.1 | 867.4 | −12.7% | −183.2496 to −68.1504 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.4 | −13.3% | −3.7737 to +0.5728 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.796 | 0.0625 | −99.2% | −15.1853 to −0.2814 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 52.9 | 0.5 | −99.1% | −116.8687 to +12.0687 | no |
| queue: job turnaround, submitted to done, mean (s) | 269.7 | 173.8 | −35.6% | −141.1957 to −50.6460 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.42 | −4.8% | −1.3912 to +0.2282 | no |
| node-hours | 5.024 | 4.776 | −4.9% | −0.5846 to +0.0887 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 527.9 | +0.5% | +0.6572 to +5.0023 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 509.6 | −2.9% | −41.4082 to +10.4719 | no |
| response time (ms), mean | 568 | 1026 | +80.6% | +262.8133 to +652.8661 | yes: LOSS |
| response time (ms), 95th percentile | 2257 | 4307 | +90.9% | +1235.1900 to +2866.3000 | yes: LOSS |
| response time (ms), 99th percentile | 3309 | 5677 | +71.5% | +1465.0401 to +3269.2257 | yes: LOSS |
| time over the response line (% of samples) | 23.31 | 33.29 | +42.8% | +7.0145 to +12.9517 | yes: LOSS |
| failed requests (%) | 0 | 0.118 | +0.118 (native is 0) | −0.0126 to +0.2486 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 16.9 | +55.0% | +3.7380 to +8.2620 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.9 | +43.900 (native is 0) | +21.2538 to +66.5462 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.71 | 20.03 | +86.9% | +4.8493 to +13.7740 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03442 | 0.04069 | +18.2% | +0.0047 to +0.0078 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.652 | 1.868 | +13.1% | +0.1489 to +0.2826 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01237 | +0.012 (native is 0) | +0.0119 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.652 | 1.88 | +13.8% | +0.1611 to +0.2951 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.3 | 663.7 | −14.2% | −144.4968 to −74.5485 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.938 | 4.198 | +6.6% | +0.0485 to +0.4728 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | +0.1887 to +1.6113 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.9 | +533.3% | +0.2854 to +2.9146 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.35 | +350.0% | +0.4551 to +1.6449 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.9 | 61.37 | +23.0% | +9.4261 to +13.5097 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 850.9 | 1032 | +21.3% | +107.7426 to +254.6574 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.84 | −9.7% | −2.7718 to +0.4495 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 7.471 | +16200.0% | −2.9245 to +17.7745 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 48.3 | +24050.0% | −23.5042 to +119.7042 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 322 | +95.8% | +97.6864 to +217.5136 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*