# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.141 | 5.385 |
| node-hours | 2.515 | 2.514 | 2.155 | 2.258 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 | 271.6 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.7 | 244.6 | 252.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 303.8 | 320.1 | 259.7 | 285.6 |
| response time (ms), 95th percentile | 972.9 | 1055 | 957.6 | 1090 |
| response time (ms), 99th percentile | 1449 | 1557 | 1404 | 1607 |
| time over the response line (% of samples) | 16.57 | 17.43 | 16.13 | 17.09 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.1 | 9 | 9.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 36.4 | 48 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.1 | 9.552 | 9.993 | 9.908 |
| utilisation (used / allocatable) | 0.05855 | 0.05823 | 0.06702 | 0.06626 |
| CPU used (cores), mean | 1.405 | 1.397 | 1.368 | 1.402 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01615 | 0.01666 |
| CPU used with Omni's own (cores), mean | 1.405 | 1.397 | 1.384 | 1.419 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 473.2 | 428.6 | 430.6 |
| HPA replicas, mean | 1.983 | 2.033 | 2.349 | 2.477 |
| pods started | 0 | 0.1 | 0.5 | 0.6 |
| pod start wait, total (s) | 0 | 0.3 | 1.6 | 1.5 |
| pod start wait, mean (s) | 0 | 0.3 | 1.2 | 1.5 |
| host CPU busy, the real machine under kind (%) | 39.82 | 40.55 | 40.42 | 41.48 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 759.9 | 766.8 | 758.4 | 769 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.535 | 5.004 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.1917 | 0.02917 | 0.2125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.8 | 0.1 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 74.77 | 65.89 | 75.6 |
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
| worker nodes in service, mean | 6 | 5.385 | −10.3% | −1.3839 to +0.1530 | no |
| node-hours | 2.514 | 2.258 | −10.2% | −0.5804 to +0.0679 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272 | +0.1% | −0.5694 to +1.2127 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 252.7 | −7.0% | −43.2898 to +5.3206 | no |
| response time (ms), mean | 320.1 | 285.6 | −10.8% | −48.9364 to −20.1009 | yes: GAIN |
| response time (ms), 95th percentile | 1055 | 1090 | +3.3% | −42.6463 to +111.6133 | no |
| response time (ms), 99th percentile | 1557 | 1607 | +3.2% | −82.8972 to +181.4812 | no |
| time over the response line (% of samples) | 17.43 | 17.09 | −2.0% | −1.1310 to +0.4380 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.1 | ±0.0% | −1.0116 to +1.0116 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 | +48.000 (native is 0) | +24.7846 to +71.2154 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.552 | 9.908 | +3.7% | −2.0009 to +2.7143 | no |
| utilisation (used / allocatable) | 0.05823 | 0.06626 | +13.8% | −0.0019 to +0.0180 | no |
| CPU used (cores), mean | 1.397 | 1.402 | +0.3% | −0.0105 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.017 (native is 0) | +0.0156 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.397 | 1.419 | +1.5% | +0.0065 to +0.0362 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.2 | 430.6 | −9.0% | −93.9442 to +8.7435 | no |
| HPA replicas, mean | 2.033 | 2.477 | +21.8% | +0.1665 to +0.7217 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0.3 | 1.5 | +400.0% | −0.9801 to +3.3801 | no |
| pod start wait, mean (s) | 0.3 | 1.5 | +400.0% | −0.9801 to +3.3801 | no |
| host CPU busy, the real machine under kind (%) | 40.55 | 41.48 | +2.3% | +0.7009 to +1.1532 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 766.8 | 769 | +0.3% | −2.3089 to +6.7089 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.004 | −16.6% | −2.2097 to +0.2180 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.2125 | +10.9% | −0.0170 to +0.0587 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.8 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 74.77 | 75.6 | +1.1% | −2.9815 to +4.6481 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.514 | −0.1% | −0.0100 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 | −0.1% | −1.1758 to +0.7399 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.7 | −0.1% | −1.1758 to +0.7399 | no |
| response time (ms), mean | 303.8 | 320.1 | +5.4% | +1.7506 to +30.8851 | yes: LOSS |
| response time (ms), 95th percentile | 972.9 | 1055 | +8.5% | +10.4647 to +154.4163 | yes: LOSS |
| response time (ms), 99th percentile | 1449 | 1557 | +7.5% | −46.7035 to +263.3601 | no |
| time over the response line (% of samples) | 16.57 | 17.43 | +5.2% | +0.1734 to +1.5655 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.1 | +3.4% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.1 | 9.552 | −13.9% | −4.3273 to +1.2373 | no |
| utilisation (used / allocatable) | 0.05855 | 0.05823 | −0.5% | −0.0012 to +0.0006 | no |
| CPU used (cores), mean | 1.405 | 1.397 | −0.5% | −0.0298 to +0.0144 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.405 | 1.397 | −0.5% | −0.0298 to +0.0144 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 473.2 | +0.9% | −4.2375 to +13.1300 | no |
| HPA replicas, mean | 1.983 | 2.033 | +2.5% | −0.1098 to +0.2095 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 39.82 | 40.55 | +1.8% | +0.5010 to +0.9574 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.9 | 766.8 | +0.9% | +2.0316 to +11.7684 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.1917 | +820.0% | +0.1014 to +0.2403 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.8 | +0.800 (native is 0) | +0.4984 to +1.1016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 74.77 | +10.8% | +1.9311 to +12.6606 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.141 | −14.3% | −1.6233 to −0.0945 | yes: GAIN |
| node-hours | 2.515 | 2.155 | −14.3% | −0.6790 to −0.0408 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.6 | −0.1% | −1.2949 to +0.6652 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 244.6 | −10.1% | −51.7313 to −2.9359 | yes: GAIN |
| response time (ms), mean | 303.8 | 259.7 | −14.5% | −65.7022 to −22.4479 | yes: GAIN |
| response time (ms), 95th percentile | 972.9 | 957.6 | −1.6% | −104.3888 to +73.7618 | no |
| response time (ms), 99th percentile | 1449 | 1404 | −3.1% | −260.4322 to +170.7592 | no |
| time over the response line (% of samples) | 16.57 | 16.13 | −2.7% | −1.5025 to +0.6224 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9 | +2.3% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.4 | +36.400 (native is 0) | +18.7358 to +54.0642 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.1 | 9.993 | −9.9% | −2.4402 to +0.2335 | no |
| utilisation (used / allocatable) | 0.05855 | 0.06702 | +14.5% | +0.0010 to +0.0159 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.405 | 1.368 | −2.6% | −0.0914 to +0.0170 | no |
| Omni's own CPU (cores), mean | 0 | 0.01615 | +0.016 (native is 0) | +0.0154 to +0.0169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.405 | 1.384 | −1.5% | −0.0756 to +0.0335 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 428.6 | −8.6% | −75.3266 to −4.8613 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.349 | +18.5% | +0.0765 to +0.6556 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | −0.2531 to +3.4531 | no |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.0417 to +2.3583 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.82 | 40.42 | +1.5% | +0.1516 to +1.0461 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.9 | 758.4 | −0.2% | −6.3191 to +3.3191 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.535 | −24.4% | −2.6974 to −0.2336 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.02917 | +40.0% | −0.0105 to +0.0272 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 65.89 | −2.3% | −7.1393 to +3.9727 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.141 | −14.3% | −1.6233 to −0.0945 | yes: GAIN |
| node-hours | 2.514 | 2.155 | −14.3% | −0.6790 to −0.0378 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 | −0.0% | −1.2553 to +1.0614 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 244.6 | −10.0% | −51.4536 to −2.7777 | yes: GAIN |
| response time (ms), mean | 320.1 | 259.7 | −18.9% | −87.6941 to −33.0918 | yes: GAIN |
| response time (ms), 95th percentile | 1055 | 957.6 | −9.3% | −212.5139 to +17.0059 | no |
| response time (ms), 99th percentile | 1557 | 1404 | −9.8% | −337.4270 to +31.0974 | no |
| time over the response line (% of samples) | 17.43 | 16.13 | −7.5% | −2.7401 to +0.1211 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | −1.1% | −0.8113 to +0.6113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.4 | +36.400 (native is 0) | +18.7358 to +54.0642 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.552 | 9.993 | +4.6% | −1.7246 to +2.6080 | no |
| utilisation (used / allocatable) | 0.05823 | 0.06702 | +15.1% | +0.0008 to +0.0168 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.397 | 1.368 | −2.1% | −0.0711 to +0.0122 | no |
| Omni's own CPU (cores), mean | 0 | 0.01615 | +0.016 (native is 0) | +0.0154 to +0.0169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.397 | 1.384 | −1.0% | −0.0553 to +0.0286 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.2 | 428.6 | −9.4% | −85.9153 to −3.1649 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.033 | 2.349 | +15.6% | +0.0509 to +0.5816 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.3 | 1.6 | +433.3% | −0.8072 to +3.4072 | no |
| pod start wait, mean (s) | 0.3 | 1.2 | +300.0% | −0.5871 to +2.3871 | no |
| host CPU busy, the real machine under kind (%) | 40.55 | 40.42 | −0.3% | −0.5765 to +0.3158 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 766.8 | 758.4 | −1.1% | −15.4425 to −1.3575 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.535 | −24.4% | −2.6974 to −0.2336 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.02917 | −84.8% | −0.2291 to −0.0959 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.1 | −87.5% | −1.0455 to −0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 74.77 | 65.89 | −11.9% | −16.9374 to −0.8209 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.385 | −10.3% | −1.3839 to +0.1530 | no |
| node-hours | 2.515 | 2.258 | −10.2% | −0.5803 to +0.0648 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 | +0.0% | −1.1632 to +1.3705 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 252.7 | −7.1% | −43.5961 to +5.1910 | no |
| response time (ms), mean | 303.8 | 285.6 | −6.0% | −34.2040 to −2.1975 | yes: GAIN |
| response time (ms), 95th percentile | 972.9 | 1090 | +12.0% | +12.9224 to +220.9256 | yes: LOSS |
| response time (ms), 99th percentile | 1449 | 1607 | +10.9% | −31.9994 to +347.2400 | no |
| time over the response line (% of samples) | 16.57 | 17.09 | +3.2% | −0.0445 to +1.0904 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.1 | +3.4% | −0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48 | +48.000 (native is 0) | +24.7846 to +71.2154 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.1 | 9.908 | −10.7% | −3.3135 to +0.9369 | no |
| utilisation (used / allocatable) | 0.05855 | 0.06626 | +13.2% | −0.0016 to +0.0170 | no |
| CPU used (cores), mean | 1.405 | 1.402 | −0.2% | −0.0275 to +0.0214 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.017 (native is 0) | +0.0156 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.405 | 1.419 | +1.0% | −0.0112 to +0.0385 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468.7 | 430.6 | −8.1% | −81.7791 to +5.4708 | no |
| HPA replicas, mean | 1.983 | 2.477 | +24.9% | +0.1309 to +0.8570 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 1.5 | +1.500 (native is 0) | −0.4444 to +3.4444 | no |
| pod start wait, mean (s) | 0 | 1.5 | +1.500 (native is 0) | −0.4444 to +3.4444 | no |
| host CPU busy, the real machine under kind (%) | 39.82 | 41.48 | +4.2% | +1.4467 to +1.8659 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 759.9 | 769 | +1.2% | +2.1448 to +16.0552 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.004 | −16.6% | −2.2097 to +0.2180 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.2125 | +920.0% | +0.1048 to +0.2785 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0.8 | +0.800 (native is 0) | +0.4984 to +1.1016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 67.47 | 75.6 | +12.0% | +1.5452 to +14.7132 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*