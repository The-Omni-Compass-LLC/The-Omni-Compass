# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.5 | 10.77 |
| node-hours | 5.023 | 5.026 | 4.396 | 4.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.3 | 523.6 | 522.9 | 524.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.3 | 523.6 | 475.7 | 485.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 330.1 | 487.6 | 346.7 | 471.5 |
| response time (ms), 95th percentile | 1123 | 2140 | 1448 | 2227 |
| response time (ms), 99th percentile | 1725 | 2897 | 2080 | 3085 |
| time over the response line (% of samples) | 10.76 | 15.28 | 12.69 | 15.73 |
| failed requests (%) | 0 | 0.06897 | 0 | 0.2453 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 11.7 | 8.9 | 12.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 121.8 | 42.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.11 | 12.97 | 11.82 | 14.68 |
| utilisation (used / allocatable) | 0.0306 | 0.03194 | 0.03556 | 0.03553 |
| CPU used (cores), mean | 1.469 | 1.533 | 1.468 | 1.53 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01359 | 0.0092 |
| CPU used with Omni's own (cores), mean | 1.469 | 1.533 | 1.482 | 1.539 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.3 | 838.8 | 780.7 | 771.3 |
| HPA replicas, mean | 4.141 | 4.048 | 4.758 | 4.529 |
| pods started | 0.1 | 0 | 0.6 | 1.2 |
| pod start wait, total (s) | 0.2 | 0 | 0.7 | 2.3 |
| pod start wait, mean (s) | 0.2 | 0 | 0.5 | 1.6 |
| host CPU busy, the real machine under kind (%) | 45.13 | 50.86 | 47.11 | 52.39 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 778.8 | 850.1 | 793.9 | 866 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.541 | 9.798 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.3792 | 0.07083 | 1.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.2 | 0.4 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 88.26 | 156.3 | 102.8 | 171.7 |
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
| worker nodes in service, mean | 12 | 10.77 | −10.2% | −2.3266 to −0.1244 | yes: GAIN |
| node-hours | 5.026 | 4.519 | −10.1% | −0.9699 to −0.0447 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.6 | 524.4 | +0.2% | −1.2839 to +3.0508 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.6 | 485.9 | −7.2% | −72.4589 to −2.9200 | yes: GAIN |
| response time (ms), mean | 487.6 | 471.5 | −3.3% | −38.0314 to +5.7305 | no |
| response time (ms), 95th percentile | 2140 | 2227 | +4.1% | −20.3927 to +195.4217 | no |
| response time (ms), 99th percentile | 2897 | 3085 | +6.5% | −104.6977 to +482.2353 | no |
| time over the response line (% of samples) | 15.28 | 15.73 | +3.0% | −0.5005 to +1.4056 | no |
| failed requests (%) | 0.06897 | 0.2453 | +255.7% | −0.0482 to +0.4009 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.2 | +4.3% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.9 | +42.900 (native is 0) | +31.8573 to +53.9427 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.97 | 14.68 | +13.2% | −0.4314 to +3.8614 | no |
| utilisation (used / allocatable) | 0.03194 | 0.03553 | +11.2% | +0.0003 to +0.0069 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.533 | 1.53 | −0.2% | −0.0330 to +0.0275 | no |
| Omni's own CPU (cores), mean | 0 | 0.0092 | +0.009 (native is 0) | +0.0079 to +0.0105 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.533 | 1.539 | +0.4% | −0.0241 to +0.0370 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 838.8 | 771.3 | −8.1% | −127.0034 to −8.0528 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.048 | 4.529 | +11.9% | +0.2101 to +0.7530 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.6358 to +1.7642 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | +1.1295 to +3.4705 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.6 | +1.600 (native is 0) | +0.8128 to +2.3872 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.86 | 52.39 | +3.0% | +0.5285 to +2.5295 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 850.1 | 866 | +1.9% | −3.7285 to +35.5285 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.798 | −18.4% | −4.0394 to −0.3653 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3792 | 1.7 | +348.4% | −1.6469 to +4.2885 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 156.3 | 171.7 | +9.8% | −3.8990 to +34.6740 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 5.023 | 5.026 | +0.1% | −0.0143 to +0.0203 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.3 | 523.6 | +0.2% | −0.5503 to +3.0463 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.3 | 523.6 | +0.2% | −0.5503 to +3.0463 | no |
| response time (ms), mean | 330.1 | 487.6 | +47.7% | −2.7693 to +317.7043 | no |
| response time (ms), 95th percentile | 1123 | 2140 | +90.6% | +39.0111 to +1995.5219 | yes: LOSS |
| response time (ms), 99th percentile | 1725 | 2897 | +67.9% | +108.9645 to +2233.2617 | yes: LOSS |
| time over the response line (% of samples) | 10.76 | 15.28 | +42.1% | +1.0573 to +7.9883 | yes: LOSS |
| failed requests (%) | 0 | 0.06897 | +0.069 (native is 0) | −0.0870 to +0.2250 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 11.7 | +72.1% | +2.2567 to +7.5433 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.11 | 12.97 | +28.3% | −2.9298 to +8.6532 | no |
| utilisation (used / allocatable) | 0.0306 | 0.03194 | +4.4% | +0.0000 to +0.0026 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.469 | 1.533 | +4.4% | +0.0016 to +0.1265 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.469 | 1.533 | +4.4% | +0.0016 to +0.1265 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.3 | 838.8 | −3.1% | −49.3093 to −3.7397 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.141 | 4.048 | −2.2% | −0.2390 to +0.0537 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 45.13 | 50.86 | +12.7% | +3.3368 to +8.1277 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.8 | 850.1 | +9.2% | +2.1618 to +140.4382 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.3792 | +658.3% | +0.1479 to +0.5104 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.2 | +300.0% | +0.6738 to +1.1262 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 88.26 | 156.3 | +77.1% | +8.9490 to +127.1260 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.5 | −12.5% | −3.0123 to +0.0056 | no |
| node-hours | 5.023 | 4.396 | −12.5% | −1.2526 to −0.0011 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.3 | 522.9 | +0.1% | −0.8851 to +2.0905 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.3 | 475.7 | −8.9% | −93.6382 to +0.3102 | no |
| response time (ms), mean | 330.1 | 346.7 | +5.0% | −53.0041 to +86.1574 | no |
| response time (ms), 95th percentile | 1123 | 1448 | +29.0% | −69.6136 to +721.4606 | no |
| response time (ms), 99th percentile | 1725 | 2080 | +20.6% | −252.4077 to +961.9047 | no |
| time over the response line (% of samples) | 10.76 | 12.69 | +18.0% | −0.2267 to +4.1006 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 8.9 | +30.9% | +0.3658 to +3.8342 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.8 | +121.800 (native is 0) | +77.3258 to +166.2742 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.11 | 11.82 | +17.0% | −2.2554 to +5.6887 | no |
| utilisation (used / allocatable) | 0.0306 | 0.03556 | +16.2% | +0.0001 to +0.0098 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.469 | 1.468 | −0.1% | −0.0490 to +0.0473 | no |
| Omni's own CPU (cores), mean | 0 | 0.01359 | +0.014 (native is 0) | +0.0126 to +0.0146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.469 | 1.482 | +0.9% | −0.0349 to +0.0604 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.3 | 780.7 | −9.8% | −162.6255 to −6.5642 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.141 | 4.758 | +14.9% | +0.1770 to +1.0579 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | −0.1079 to +1.1079 | no |
| pod start wait, mean (s) | 0.2 | 0.5 | +150.0% | −0.2889 to +0.8889 | no |
| host CPU busy, the real machine under kind (%) | 45.13 | 47.11 | +4.4% | +0.8497 to +3.1109 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.8 | 793.9 | +1.9% | −9.0996 to +39.2996 | no |
| batch: worker machines in service after the queue finished, mean | 12 | 9.541 | −20.5% | −4.7247 to −0.1926 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.07083 | +41.7% | −0.0195 to +0.0612 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.26 | 102.8 | +16.4% | −5.1316 to +34.1233 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.5 | −12.5% | −3.0123 to +0.0056 | no |
| node-hours | 5.026 | 4.396 | −12.5% | −1.2629 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.6 | 522.9 | −0.1% | −2.4485 to +1.1578 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.6 | 475.7 | −9.2% | −95.3422 to −0.4818 | yes: GAIN |
| response time (ms), mean | 487.6 | 346.7 | −28.9% | −243.6073 to −38.1745 | yes: GAIN |
| response time (ms), 95th percentile | 2140 | 1448 | −32.3% | −1384.4291 to +1.7431 | no |
| response time (ms), 99th percentile | 2897 | 2080 | −28.2% | −1569.6782 to −63.0510 | yes: GAIN |
| time over the response line (% of samples) | 15.28 | 12.69 | −16.9% | −5.0513 to −0.1204 | yes: GAIN |
| failed requests (%) | 0.06897 | 0 | −100.0% | −0.2250 to +0.0870 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 8.9 | −23.9% | −5.1313 to −0.4687 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.8 | +121.800 (native is 0) | +77.3258 to +166.2742 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.97 | 11.82 | −8.8% | −4.1935 to +1.9035 | no |
| utilisation (used / allocatable) | 0.03194 | 0.03556 | +11.3% | −0.0016 to +0.0089 | no |
| CPU used (cores), mean | 1.533 | 1.468 | −4.2% | −0.1048 to −0.0249 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01359 | +0.014 (native is 0) | +0.0126 to +0.0146 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.533 | 1.482 | −3.3% | −0.0918 to −0.0108 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 838.8 | 780.7 | −6.9% | −139.0843 to +22.9436 | no |
| HPA replicas, mean | 4.048 | 4.758 | +17.5% | +0.2378 to +1.1826 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| host CPU busy, the real machine under kind (%) | 50.86 | 47.11 | −7.4% | −5.3235 to −2.1804 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 850.1 | 793.9 | −6.6% | −105.1064 to −7.2936 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.541 | −20.5% | −4.7247 to −0.1926 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3792 | 0.07083 | −81.3% | −0.4765 to −0.1402 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 0.4 | −66.7% | −1.1016 to −0.4984 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 156.3 | 102.8 | −34.3% | −96.2858 to −10.7976 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.77 | −10.2% | −2.3266 to −0.1244 | yes: GAIN |
| node-hours | 5.023 | 4.519 | −10.0% | −0.9609 to −0.0477 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 522.3 | 524.4 | +0.4% | +0.5649 to +3.6980 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.3 | 485.9 | −7.0% | −70.9045 to −1.9784 | yes: GAIN |
| response time (ms), mean | 330.1 | 471.5 | +42.8% | −24.1542 to +306.7885 | no |
| response time (ms), 95th percentile | 1123 | 2227 | +98.4% | +38.1819 to +2171.3801 | yes: LOSS |
| response time (ms), 99th percentile | 1725 | 3085 | +78.8% | +149.6741 to +2570.0897 | yes: LOSS |
| time over the response line (% of samples) | 10.76 | 15.73 | +46.3% | +1.8643 to +8.0863 | yes: LOSS |
| failed requests (%) | 0 | 0.2453 | +0.245 (native is 0) | −0.1058 to +0.5964 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 12.2 | +79.4% | +3.0348 to +7.7652 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.9 | +42.900 (native is 0) | +31.8573 to +53.9427 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.11 | 14.68 | +45.3% | −1.5913 to +10.7446 | no |
| utilisation (used / allocatable) | 0.0306 | 0.03553 | +16.1% | +0.0019 to +0.0080 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.469 | 1.53 | +4.2% | −0.0074 to +0.1299 | no |
| Omni's own CPU (cores), mean | 0 | 0.0092 | +0.009 (native is 0) | +0.0079 to +0.0105 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.469 | 1.539 | +4.8% | +0.0008 to +0.1402 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 865.3 | 771.3 | −10.9% | −153.1312 to −34.9741 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.141 | 4.529 | +9.4% | +0.2166 to +0.5611 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.5722 to +1.6278 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.3 | +1050.0% | +1.0100 to +3.1900 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.6 | +700.0% | +0.5436 to +2.2564 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.13 | 52.39 | +16.1% | +4.2581 to +10.2644 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.8 | 866 | +11.2% | +3.4050 to +170.9950 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.798 | −18.4% | −4.0394 to −0.3653 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1.7 | +3300.0% | −1.4662 to +4.7662 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.2 | +300.0% | +0.4940 to +1.3060 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 88.26 | 171.7 | +94.5% | +9.5698 to +157.2802 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*