# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.436 | 6.916 |
| node-hours | 5.03 | 5.026 | 3.949 | 2.895 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.5 | 504.2 | 522.3 | 504.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.5 | 504.2 | 441.8 | 344.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 360.6 | 104.7 | 365.6 | 61.18 |
| response time (ms), 95th percentile | 1363 | 144 | 1553 | 79.49 |
| response time (ms), 99th percentile | 2005 | 168.1 | 2249 | 103.7 |
| time over the response line (% of samples) | 12.95 | 0 | 13.5 | 0.003997 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 0 | 6.8 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 101.6 | 25.22 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.94 | 0 | 10.44 | 0.05926 |
| utilisation (used / allocatable) | 0.0302 | 0.005548 | 0.03922 | 0.008034 |
| CPU used (cores), mean | 1.449 | 0.2663 | 1.46 | 0.2234 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01383 | 0.007956 |
| CPU used with Omni's own (cores), mean | 1.449 | 0.2663 | 1.474 | 0.2313 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 884.4 | 4642 | 728.3 | 3811 |
| HPA replicas, mean | 3.987 | 4.123 | 4.161 | 4.285 |
| pods started | 0.1 | 0.8889 | 0.8 | 1.222 |
| pod start wait, total (s) | 0.2 | 1.111 | 2 | 1.778 |
| pod start wait, mean (s) | 0.2 | 0.5556 | 0.63 | 1.167 |
| host CPU busy, the real machine under kind (%) | 44.65 | 13.11 | 46.71 | 13.86 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 790.5 | 1506 | 806.5 | 1505 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 7.848 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1159 | 0.05833 | 1158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1475 | 0.4 | 1474 |
| queue: job turnaround, submitted to done, mean (s) | 100.3 | 1159 | 114.6 | 1158 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.916 | −42.4% | −5.2789 to −4.8895 | yes: GAIN |
| node-hours | 5.026 | 2.895 | −42.4% | −2.2157 to −2.0464 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.2 | 504.1 | −0.0% | −1.3354 to +1.0087 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.2 | 344.4 | −31.7% | −166.2393 to −153.3559 | yes: GAIN |
| response time (ms), mean | 104.7 | 61.18 | −41.6% | −55.3194 to −31.6695 | yes: GAIN |
| response time (ms), 95th percentile | 144 | 79.49 | −44.8% | −80.3994 to −48.6639 | yes: GAIN |
| response time (ms), 99th percentile | 168.1 | 103.7 | −38.3% | −76.5245 to −52.2426 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.003997 | +0.004 (native is 0) | −0.0052 to +0.0132 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.22 | +25.222 (native is 0) | +23.9032 to +26.5412 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05926 | +0.059 (native is 0) | −0.0774 to +0.1959 | no |
| utilisation (used / allocatable) | 0.005548 | 0.008034 | +44.8% | +0.0021 to +0.0029 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2663 | 0.2234 | −16.1% | −0.0490 to −0.0368 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.007956 | +0.008 (native is 0) | +0.0067 to +0.0092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2663 | 0.2313 | −13.1% | −0.0413 to −0.0286 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4642 | 3811 | −17.9% | −981.6293 to −680.5055 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.123 | 4.285 | +3.9% | −0.0250 to +0.3485 | no |
| pods started | 0.8889 | 1.222 | +37.5% | −0.7537 to +1.4204 | no |
| pod start wait, total (s) | 1.111 | 1.778 | +60.0% | −0.5487 to +1.8820 | no |
| pod start wait, mean (s) | 0.5556 | 1.167 | +110.0% | −0.0484 to +1.2706 | no |
| host CPU busy, the real machine under kind (%) | 13.11 | 13.86 | +5.8% | +0.3690 to +1.1485 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1505 | −0.0% | −4.4323 to +3.0990 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1158 | −0.1% | −4.6125 to +2.8718 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1474 | −0.1% | −4.9630 to +2.7408 | no |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1158 | −0.1% | −4.6125 to +2.8718 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.031 | 5.026 | −0.1% | −0.0258 to +0.0154 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.1 | 504.2 | −3.4% | −21.8723 to −13.8379 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.1 | 504.2 | −3.4% | −21.8723 to −13.8379 | yes: GAIN |
| response time (ms), mean | 319.3 | 104.7 | −67.2% | −420.5892 to −8.6157 | yes: GAIN |
| response time (ms), 95th percentile | 1164 | 144 | −87.6% | −2053.4752 to +14.0440 | no |
| response time (ms), 99th percentile | 1727 | 168.1 | −90.3% | −3072.1644 to −46.2473 | yes: GAIN |
| time over the response line (% of samples) | 10.87 | 0 | −100.0% | −23.0082 to +1.2586 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.333 | 0 | −100.0% | −10.9556 to +0.2890 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.01 | 0 | −100.0% | −14.2794 to −5.7428 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.02944 | 0.005548 | −81.2% | −0.0272 to −0.0205 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.413 | 0.2663 | −81.2% | −1.3075 to −0.9863 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.413 | 0.2663 | −81.2% | −1.3075 to −0.9863 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 903.9 | 4642 | +413.6% | +3237.6887 to +4239.1095 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.995 | 4.123 | +3.2% | −0.0818 to +0.3389 | no |
| pods started | 0.1111 | 0.8889 | +700.0% | +0.0308 to +1.5248 | yes: power given |
| pod start wait, total (s) | 0.2222 | 1.111 | +400.0% | −0.1597 to +1.9375 | no |
| pod start wait, mean (s) | 0.2222 | 0.5556 | +150.0% | −0.3040 to +0.9707 | no |
| host CPU busy, the real machine under kind (%) | 43.65 | 13.11 | −70.0% | −35.3961 to −25.6882 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.7 | 1506 | +93.4% | +662.7749 to +791.2251 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 1159 | +3130137.5% | +1155.4459 to +1163.1745 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2222 | 1475 | +663850.0% | +1471.2138 to +1479.2307 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 87.79 | 1159 | +1220.6% | +1003.5771 to +1139.5433 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.436 | −21.4% | −4.2957 to −0.8328 | yes: GAIN |
| node-hours | 5.03 | 3.949 | −21.5% | −1.8011 to −0.3608 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.5 | 522.3 | −0.0% | −1.7741 to +1.4735 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.5 | 441.8 | −15.5% | −134.8772 to −26.6192 | yes: GAIN |
| response time (ms), mean | 360.6 | 365.6 | +1.4% | −31.6505 to +41.5798 | no |
| response time (ms), 95th percentile | 1363 | 1553 | +13.9% | −15.0799 to +394.7709 | no |
| response time (ms), 99th percentile | 2005 | 2249 | +12.2% | +13.1027 to +474.1605 | yes: LOSS |
| time over the response line (% of samples) | 12.95 | 13.5 | +4.2% | +0.1653 to +0.9284 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.3 | 6.8 | +7.9% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.6 | +101.600 (native is 0) | +53.4913 to +149.7087 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.94 | 10.44 | −4.5% | −2.7557 to +1.7657 | no |
| utilisation (used / allocatable) | 0.0302 | 0.03922 | +29.9% | +0.0036 to +0.0145 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.449 | 1.46 | +0.7% | −0.0334 to +0.0545 | no |
| Omni's own CPU (cores), mean | 0 | 0.01383 | +0.014 (native is 0) | +0.0128 to +0.0148 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.449 | 1.474 | +1.7% | −0.0197 to +0.0684 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 884.4 | 728.3 | −17.6% | −246.7325 to −65.4213 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.987 | 4.161 | +4.4% | −0.0764 to +0.4257 | no |
| pods started | 0.1 | 0.8 | +700.0% | −0.4209 to +1.8209 | no |
| pod start wait, total (s) | 0.2 | 2 | +900.0% | −1.3416 to +4.9416 | no |
| pod start wait, mean (s) | 0.2 | 0.63 | +215.0% | −0.2116 to +1.0716 | no |
| host CPU busy, the real machine under kind (%) | 44.65 | 46.71 | +4.6% | +1.1097 to +3.0078 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 790.5 | 806.5 | +2.0% | −0.7347 to +32.7347 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 7.848 | −34.6% | −6.8624 to −1.4408 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05833 | +16.7% | −0.0439 to +0.0605 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.3 | 114.6 | +14.2% | +0.7879 to +27.7121 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.169 | −23.6% | −4.6808 to −0.9819 | yes: GAIN |
| node-hours | 5.026 | 3.837 | −23.6% | −1.9650 to −0.4119 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.2 | 521.8 | +3.5% | +14.4058 to +20.7477 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.2 | 432.8 | −14.2% | −132.4435 to −10.3937 | yes: GAIN |
| response time (ms), mean | 104.7 | 309.5 | +195.7% | −11.5462 to +421.2410 | no |
| response time (ms), 95th percentile | 144 | 1270 | +782.1% | +10.7826 to +2241.9429 | yes: LOSS |
| response time (ms), 99th percentile | 168.1 | 1878 | +1017.0% | +97.1756 to +3321.9904 | yes: LOSS |
| time over the response line (% of samples) | 0 | 11.28 | +11.281 (native is 0) | −0.8841 to +23.4454 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 5.778 | +5.778 (native is 0) | −0.0608 to +11.6163 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 108.7 | +108.667 (native is 0) | +56.9485 to +160.3849 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 9.683 | +9.683 (native is 0) | +4.3408 to +15.0258 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005548 | 0.03927 | +607.9% | +0.0304 to +0.0371 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2663 | 1.418 | +432.5% | +0.9560 to +1.3475 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01368 | +0.014 (native is 0) | +0.0126 to +0.0148 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2663 | 1.432 | +437.7% | +0.9702 to +1.3606 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4642 | 733.7 | −84.2% | −4498.4776 to −3318.7439 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.123 | 4.182 | +1.4% | −0.2012 to +0.3191 | no |
| pods started | 0.8889 | 0.8889 | ±0.0% | −1.6753 to +1.6753 | no |
| pod start wait, total (s) | 1.111 | 2.222 | +100.0% | −2.8912 to +5.1134 | no |
| pod start wait, mean (s) | 0.5556 | 0.7 | +26.0% | −0.9562 to +1.2451 | no |
| host CPU busy, the real machine under kind (%) | 13.11 | 45.48 | +247.0% | +27.1109 to +37.6333 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 789.4 | −47.6% | −792.9444 to −639.5000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.05556 | −100.0% | −1163.1264 to −1155.4570 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.3333 | −100.0% | −1478.9050 to −1471.3172 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 97.7 | −91.6% | −1139.2408 to −984.0463 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.916 | −42.4% | −5.2789 to −4.8895 | yes: GAIN |
| node-hours | 5.031 | 2.895 | −42.5% | −2.2125 to −2.0599 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.1 | 504.1 | −3.5% | −22.1720 to −13.8649 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.1 | 344.4 | −34.0% | −181.2044 to −174.1009 | yes: GAIN |
| response time (ms), mean | 319.3 | 61.18 | −80.8% | −474.6191 to −41.5746 | yes: GAIN |
| response time (ms), 95th percentile | 1164 | 79.49 | −93.2% | −2129.9817 to −38.5128 | yes: GAIN |
| response time (ms), 99th percentile | 1727 | 103.7 | −94.0% | −3140.2432 to −106.9357 | yes: GAIN |
| time over the response line (% of samples) | 10.87 | 0.003997 | −100.0% | −22.9998 to +1.2582 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.333 | 0 | −100.0% | −10.9556 to +0.2890 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.22 | +25.222 (native is 0) | +23.9032 to +26.5412 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.01 | 0.05926 | −99.4% | −14.2393 to −5.6644 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.02944 | 0.008034 | −72.7% | −0.0244 to −0.0184 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.413 | 0.2234 | −84.2% | −1.3492 to −1.0303 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.007956 | +0.008 (native is 0) | +0.0067 to +0.0092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.413 | 0.2313 | −83.6% | −1.3401 to −1.0236 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 903.9 | 3811 | +321.6% | +2485.7206 to +3328.9428 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.995 | 4.285 | +7.3% | +0.0364 to +0.5444 | yes: power given |
| pods started | 0.1111 | 1.222 | +1000.0% | +0.2143 to +2.0079 | yes: power given |
| pod start wait, total (s) | 0.2222 | 1.778 | +700.0% | +0.1639 to +2.9472 | yes: LOSS |
| pod start wait, mean (s) | 0.2222 | 1.167 | +425.0% | −0.0438 to +1.9326 | no |
| host CPU busy, the real machine under kind (%) | 43.65 | 13.86 | −68.2% | −34.3787 to −25.1881 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.7 | 1505 | +93.3% | +661.4208 to +791.2459 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03704 | 1158 | +3127787.5% | +1154.6124 to +1162.2672 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2222 | 1474 | +663350.0% | +1470.1833 to +1478.0389 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 87.79 | 1158 | +1219.6% | +1002.0781 to +1139.3016 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*