# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.956 | 6 |
| node-hours | 2.516 | 2.515 | 2.494 | 2.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 286.4 | 274.2 | 285.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 286.4 | 272.8 | 285.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 412.1 | 764 | 377.4 | 751.6 |
| response time (ms), 95th percentile | 1409 | 1577 | 1440 | 1534 |
| response time (ms), 99th percentile | 1989 | 2084 | 2177 | 2068 |
| time over the response line (% of samples) | 27.21 | 68.95 | 26.91 | 68.87 |
| failed requests (%) | 0 | 0 | 0.009756 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 25 | 13.3 | 25 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 17.8 | 15.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 2.405 | 12.77 | 2.48 |
| utilisation (used / allocatable) | 0.06461 | 0.09726 | 0.06602 | 0.09695 |
| CPU used (cores), mean | 1.551 | 2.334 | 1.572 | 2.327 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01568 | 0.00994 |
| CPU used with Omni's own (cores), mean | 1.551 | 2.334 | 1.588 | 2.337 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.1 | 292.7 | 414.7 | 293.5 |
| HPA replicas, mean | 1.998 | 2.098 | 2.018 | 2.862 |
| pods started | 0 | 0.1 | 0.2 | 0.5 |
| pod start wait, total (s) | 0 | 0.3 | 0.3 | 1.1 |
| pod start wait, mean (s) | 0 | 0.3 | 0.3 | 0.85 |
| host CPU busy, the real machine under kind (%) | 44.08 | 76.89 | 45.05 | 77.26 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 787.8 | 1510 | 793.3 | 1508 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 5.907 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 868.3 | 0.0625 | 891.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1416 | 0.5 | 1432 |
| queue: job turnaround, submitted to done, mean (s) | 98.69 | 1080 | 102.7 | 1092 |
| queue: jobs unfinished at the window's end | 0 | 18.7 | 0 | 19.3 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.511 | −0.2% | −0.0135 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.4 | 285.8 | −0.2% | −1.6691 to +0.5371 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.4 | 285.8 | −0.2% | −1.6691 to +0.5371 | no |
| response time (ms), mean | 764 | 751.6 | −1.6% | −48.0014 to +23.1451 | no |
| response time (ms), 95th percentile | 1577 | 1534 | −2.7% | −141.5127 to +55.7257 | no |
| response time (ms), 99th percentile | 2084 | 2068 | −0.7% | −206.7049 to +175.8881 | no |
| time over the response line (% of samples) | 68.95 | 68.87 | −0.1% | −2.3204 to +2.1722 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 25 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.6 | +15.600 (native is 0) | +14.6344 to +16.5656 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.405 | 2.48 | +3.1% | +0.0015 to +0.1485 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09726 | 0.09695 | −0.3% | −0.0008 to +0.0002 | no |
| CPU used (cores), mean | 2.334 | 2.327 | −0.3% | −0.0197 to +0.0048 | no |
| Omni's own CPU (cores), mean | 0 | 0.00994 | +0.010 (native is 0) | +0.0097 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.334 | 2.337 | +0.1% | −0.0098 to +0.0148 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292.7 | 293.5 | +0.3% | −0.5955 to +2.2419 | no |
| HPA replicas, mean | 2.098 | 2.862 | +36.4% | +0.6526 to +0.8754 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | −0.7379 to +2.3379 | no |
| pod start wait, mean (s) | 0.3 | 0.85 | +183.3% | −0.6710 to +1.7710 | no |
| host CPU busy, the real machine under kind (%) | 76.89 | 77.26 | +0.5% | +0.3002 to +0.4345 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 1508 | −0.1% | −5.7813 to +1.3813 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 868.3 | 891.7 | +2.7% | −48.8311 to +95.7222 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1416 | 1432 | +1.1% | −31.4979 to +63.0979 | no |
| queue: job turnaround, submitted to done, mean (s) | 1080 | 1092 | +1.1% | −31.8483 to +54.6066 | no |
| queue: jobs unfinished at the window's end | 18.7 | 19.3 | +3.2% | −0.7572 to +1.9572 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.515 | −0.0% | −0.0103 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 286.4 | +4.4% | +10.7399 to +13.3229 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 286.4 | +4.4% | +10.7399 to +13.3229 | yes: power given |
| response time (ms), mean | 412.1 | 764 | +85.4% | +301.1495 to +402.6283 | yes: LOSS |
| response time (ms), 95th percentile | 1409 | 1577 | +11.9% | −24.1678 to +359.2498 | no |
| response time (ms), 99th percentile | 1989 | 2084 | +4.8% | −158.1567 to +347.2501 | no |
| time over the response line (% of samples) | 27.21 | 68.95 | +153.4% | +38.8869 to +44.5807 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 25 | +89.4% | +11.4984 to +12.1016 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 2.405 | −79.8% | −10.9184 to −8.0816 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06461 | 0.09726 | +50.5% | +0.0316 to +0.0337 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.551 | 2.334 | +50.5% | +0.7596 to +0.8079 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.551 | 2.334 | +50.5% | +0.7596 to +0.8079 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.1 | 292.7 | −30.7% | −135.7825 to −123.1683 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.098 | +5.0% | −0.0348 to +0.2363 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 44.08 | 76.89 | +74.4% | +31.9423 to +33.6848 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 787.8 | 1510 | +91.7% | +707.9942 to +737.2058 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 868.3 | +1225703.0% | +828.4954 to +907.9172 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1416 | +283120.0% | +1376.4832 to +1454.7168 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 98.69 | 1080 | +994.7% | +938.4246 to +1024.9254 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 18.7 | +18.700 (native is 0) | +17.9422 to +19.4578 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.956 | −0.7% | −0.1225 to +0.0348 | no |
| node-hours | 2.516 | 2.494 | −0.9% | −0.0583 to +0.0133 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.2 | −0.1% | −0.9714 to +0.6750 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 272.8 | −0.6% | −4.3288 to +1.2824 | no |
| response time (ms), mean | 412.1 | 377.4 | −8.4% | −47.8799 to −21.5574 | yes: GAIN |
| response time (ms), 95th percentile | 1409 | 1440 | +2.2% | −48.6897 to +111.2117 | no |
| response time (ms), 99th percentile | 1989 | 2177 | +9.4% | +71.8396 to +303.9432 | yes: LOSS |
| time over the response line (% of samples) | 27.21 | 26.91 | −1.1% | −1.2386 to +0.6339 | no |
| failed requests (%) | 0 | 0.009756 | +0.010 (native is 0) | −0.0123 to +0.0318 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 13.3 | +0.8% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +13.8850 to +21.7150 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 12.77 | +7.3% | −1.1241 to +2.8541 | no |
| utilisation (used / allocatable) | 0.06461 | 0.06602 | +2.2% | +0.0002 to +0.0026 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.551 | 1.572 | +1.4% | +0.0005 to +0.0430 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01568 | +0.016 (native is 0) | +0.0151 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.551 | 1.588 | +2.4% | +0.0160 to +0.0588 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.1 | 414.7 | −1.8% | −13.5867 to −1.2143 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.018 | +1.0% | −0.1169 to +0.1574 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 44.08 | 45.05 | +2.2% | +0.6330 to +1.3096 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 787.8 | 793.3 | +0.7% | +1.0616 to +9.9384 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.907 | −1.6% | −0.2593 to +0.0727 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0625 | −11.8% | −0.0476 to +0.0309 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.69 | 102.7 | +4.1% | +0.1066 to +7.9351 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.956 | −0.7% | −0.1225 to +0.0348 | no |
| node-hours | 2.515 | 2.494 | −0.9% | −0.0533 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.4 | 274.2 | −4.3% | −13.1230 to −11.2362 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.4 | 272.8 | −4.7% | −15.9816 to −11.1276 | yes: GAIN |
| response time (ms), mean | 764 | 377.4 | −50.6% | −430.8488 to −342.3664 | yes: GAIN |
| response time (ms), 95th percentile | 1577 | 1440 | −8.6% | −304.0213 to +31.4613 | no |
| response time (ms), 99th percentile | 2084 | 2177 | +4.5% | −166.9439 to +353.6333 | no |
| time over the response line (% of samples) | 68.95 | 26.91 | −61.0% | −44.3504 to −39.7219 | yes: GAIN |
| failed requests (%) | 0 | 0.009756 | +0.010 (native is 0) | −0.0123 to +0.0318 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 13.3 | −46.8% | −12.0455 to −11.3545 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.800 (native is 0) | +13.8850 to +21.7150 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.405 | 12.77 | +431.0% | +8.8308 to +11.8992 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09726 | 0.06602 | −32.1% | −0.0328 to −0.0297 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.334 | 1.572 | −32.6% | −0.7927 to −0.7312 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01568 | +0.016 (native is 0) | +0.0151 to +0.0163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.334 | 1.588 | −32.0% | −0.7768 to −0.7157 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292.7 | 414.7 | +41.7% | +113.7783 to +130.3715 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.098 | 2.018 | −3.8% | −0.1914 to +0.0305 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.3 | 0.3 | ±0.0% | −0.8921 to +0.8921 | no |
| pod start wait, mean (s) | 0.3 | 0.3 | ±0.0% | −0.8921 to +0.8921 | no |
| host CPU busy, the real machine under kind (%) | 76.89 | 45.05 | −41.4% | −32.8001 to −30.8844 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 793.3 | −47.5% | −732.3690 to −701.8310 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 868.3 | 0.0625 | −100.0% | −907.9388 to −828.4905 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1416 | 0.5 | −100.0% | −1454.5055 to −1376.6945 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1080 | 102.7 | −90.5% | −1020.5777 to −934.7307 | yes: GAIN |
| queue: jobs unfinished at the window's end | 18.7 | 0 | −100.0% | −19.4578 to −17.9422 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to −0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.516 | 2.511 | −0.2% | −0.0141 to +0.0044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 285.8 | +4.2% | +10.1440 to +12.7868 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 285.8 | +4.2% | +10.1440 to +12.7868 | yes: power given |
| response time (ms), mean | 412.1 | 751.6 | +82.4% | +289.2219 to +389.6996 | yes: LOSS |
| response time (ms), 95th percentile | 1409 | 1534 | +8.8% | −71.1542 to +320.4492 | no |
| response time (ms), 99th percentile | 1989 | 2068 | +4.0% | −283.0614 to +441.3380 | no |
| time over the response line (% of samples) | 27.21 | 68.87 | +153.1% | +39.3005 to +44.0189 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 25 | +89.4% | +11.4984 to +12.1016 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.6 | +15.600 (native is 0) | +14.6344 to +16.5656 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.9 | 2.48 | −79.2% | −10.8256 to −8.0244 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06461 | 0.09695 | +50.1% | +0.0310 to +0.0337 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.551 | 2.327 | +50.1% | +0.7449 to +0.8077 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00994 | +0.010 (native is 0) | +0.0097 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.551 | 2.337 | +50.7% | +0.7547 to +0.8177 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 422.1 | 293.5 | −30.5% | −135.7725 to −121.5319 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.862 | +43.3% | +0.7613 to +0.9682 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.1367 to +2.3367 | no |
| pod start wait, mean (s) | 0 | 0.85 | +0.850 (native is 0) | −0.0105 to +1.7105 | no |
| host CPU busy, the real machine under kind (%) | 44.08 | 77.26 | +75.3% | +32.2800 to +34.0818 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 787.8 | 1508 | +91.4% | +704.9763 to +735.8237 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 891.7 | +1258802.5% | +825.3258 to +957.9778 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1432 | +286280.0% | +1404.2451 to +1458.5549 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 98.69 | 1092 | +1006.2% | +964.6534 to +1021.4549 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 19.3 | +19.300 (native is 0) | +17.9919 to +20.6081 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*