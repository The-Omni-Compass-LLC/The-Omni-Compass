# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.209 | 5.348 |
| node-hours | 2.519 | 2.511 | 2.185 | 2.239 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 | 272.1 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.7 | 247.2 | 251.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 273.8 | 335.9 | 245.1 | 308.6 |
| response time (ms), 95th percentile | 851.9 | 1316 | 896.1 | 1387 |
| response time (ms), 99th percentile | 1185 | 2076 | 1317 | 2131 |
| time over the response line (% of samples) | 14.56 | 14.61 | 15.11 | 14.2 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.6 | 9.6 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 36.5 | 35.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 15.15 | 9.313 | 15.88 |
| utilisation (used / allocatable) | 0.058 | 0.05897 | 0.06782 | 0.06679 |
| CPU used (cores), mean | 1.392 | 1.415 | 1.401 | 1.41 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01691 | 0.01853 |
| CPU used with Omni's own (cores), mean | 1.392 | 1.415 | 1.418 | 1.428 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 463.3 | 421.3 | 426.8 |
| HPA replicas, mean | 1.936 | 2.052 | 1.971 | 1.998 |
| pods started | 0.1 | 0.1 | 0 | 0.2 |
| pod start wait, total (s) | 0.3 | 0.1 | 0 | 0.4 |
| pod start wait, mean (s) | 0.3 | 0.1 | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 40.09 | 42.8 | 41.13 | 43.78 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 749.7 | 781.9 | 752.9 | 786.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.521 | 4.786 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.7792 | 0.0625 | 0.8625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.3 | 0.5 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 57.26 | 93 | 60.66 | 96.74 |
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
| worker nodes in service, mean | 6 | 5.348 | −10.9% | −1.2607 to −0.0440 | yes: GAIN |
| node-hours | 2.511 | 2.239 | −10.9% | −0.5279 to −0.0170 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.9 | +0.1% | −0.8303 to +1.1736 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 251.4 | −7.5% | −39.7280 to −0.9245 | yes: GAIN |
| response time (ms), mean | 335.9 | 308.6 | −8.1% | −48.9648 to −5.5439 | yes: GAIN |
| response time (ms), 95th percentile | 1316 | 1387 | +5.4% | −74.0360 to +216.6920 | no |
| response time (ms), 99th percentile | 2076 | 2131 | +2.7% | −141.5539 to +252.1701 | no |
| time over the response line (% of samples) | 14.61 | 14.2 | −2.9% | −2.1291 to +1.2960 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.1 | +5.2% | −0.4685 to +1.4685 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.800 (native is 0) | +20.0243 to +51.5757 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.15 | 15.88 | +4.8% | −0.7056 to +2.1723 | no |
| utilisation (used / allocatable) | 0.05897 | 0.06679 | +13.3% | +0.0002 to +0.0154 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.415 | 1.41 | −0.4% | −0.0278 to +0.0171 | no |
| Omni's own CPU (cores), mean | 0 | 0.01853 | +0.019 (native is 0) | +0.0169 to +0.0202 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.428 | +0.9% | −0.0098 to +0.0362 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.3 | 426.8 | −7.9% | −69.7665 to −3.2017 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.052 | 1.998 | −2.6% | −0.2279 to +0.1198 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.1 | 0.4 | +300.0% | −0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0.1 | 0.4 | +300.0% | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 42.8 | 43.78 | +2.3% | +0.5707 to +1.3812 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.9 | 786.3 | +0.6% | +0.1722 to +8.6278 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.786 | −20.2% | −2.2150 to −0.2135 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.8625 | +10.7% | −0.0180 to +0.1846 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.7 | +30.8% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 93 | 96.74 | +4.0% | −0.6737 to +8.1487 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.519 | 2.511 | −0.3% | −0.0159 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 | −0.1% | −1.3060 to +0.6135 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.7 | −0.1% | −1.3060 to +0.6135 | no |
| response time (ms), mean | 273.8 | 335.9 | +22.7% | +25.6405 to +98.5160 | yes: LOSS |
| response time (ms), 95th percentile | 851.9 | 1316 | +54.5% | +180.1192 to +747.6368 | yes: LOSS |
| response time (ms), 99th percentile | 1185 | 2076 | +75.2% | +352.5471 to +1429.3689 | yes: LOSS |
| time over the response line (% of samples) | 14.56 | 14.61 | +0.4% | −3.4472 to +3.5586 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.6 | +2.1% | −0.7417 to +1.1417 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 15.15 | +48.6% | +2.3702 to +7.5331 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.058 | 0.05897 | +1.7% | +0.0003 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.415 | +1.7% | +0.0073 to +0.0392 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.392 | 1.415 | +1.7% | +0.0073 to +0.0392 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 463.3 | −1.4% | −11.3994 to −1.7695 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.936 | 2.052 | +6.0% | −0.0264 to +0.2589 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 40.09 | 42.8 | +6.8% | +2.2092 to +3.2237 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.7 | 781.9 | +4.3% | +15.2633 to +49.1367 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.7792 | +2237.5% | +0.6246 to +0.8671 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.3 | +333.3% | +0.6628 to +1.3372 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 57.26 | 93 | +62.4% | +17.4479 to +54.0438 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.209 | −13.2% | −1.3919 to −0.1898 | yes: GAIN |
| node-hours | 2.519 | 2.184 | −13.3% | −0.5865 to −0.0822 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | +0.0% | −0.7040 to +0.7362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 247.2 | −9.1% | −43.9057 to −5.8621 | yes: GAIN |
| response time (ms), mean | 273.8 | 245.1 | −10.5% | −43.3090 to −14.0617 | yes: GAIN |
| response time (ms), 95th percentile | 851.9 | 896.1 | +5.2% | −8.5172 to +96.9682 | no |
| response time (ms), 99th percentile | 1185 | 1317 | +11.2% | +19.1070 to +245.4514 | yes: LOSS |
| time over the response line (% of samples) | 14.56 | 15.11 | +3.8% | −1.4548 to +2.5616 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.6 | +2.1% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.5 | +36.500 (native is 0) | +22.4050 to +50.5950 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 9.313 | −8.6% | −2.4306 to +0.6672 | no |
| utilisation (used / allocatable) | 0.058 | 0.06782 | +16.9% | +0.0028 to +0.0169 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.401 | +0.6% | −0.0125 to +0.0296 | no |
| Omni's own CPU (cores), mean | 0 | 0.01691 | +0.017 (native is 0) | +0.0156 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.418 | +1.8% | +0.0040 to +0.0469 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 421.3 | −10.3% | −82.5388 to −14.6870 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.936 | 1.971 | +1.8% | −0.0638 to +0.1343 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 40.09 | 41.13 | +2.6% | +0.7018 to +1.3916 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.7 | 752.9 | +0.4% | −0.3494 to +6.7494 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.521 | −24.6% | −2.5597 to −0.3981 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.0625 | +87.5% | −0.0107 to +0.0690 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.26 | 60.66 | +5.9% | −0.2718 to +7.0718 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.209 | −13.2% | −1.3919 to −0.1898 | yes: GAIN |
| node-hours | 2.511 | 2.184 | −13.0% | −0.5807 to −0.0726 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.1 | +0.1% | −0.4959 to +1.2205 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 247.2 | −9.0% | −43.7510 to −5.3243 | yes: GAIN |
| response time (ms), mean | 335.9 | 245.1 | −27.0% | −131.0847 to −50.4424 | yes: GAIN |
| response time (ms), 95th percentile | 1316 | 896.1 | −31.9% | −711.8326 to −127.4724 | yes: GAIN |
| response time (ms), 99th percentile | 2076 | 1317 | −36.5% | −1272.9202 to −244.4374 | yes: GAIN |
| time over the response line (% of samples) | 14.61 | 15.11 | +3.4% | −1.4911 to +2.4866 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.6 | ±0.0% | −1.2158 to +1.2158 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.5 | +36.500 (native is 0) | +22.4050 to +50.5950 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.15 | 9.313 | −38.5% | −7.8510 to −3.8157 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05897 | 0.06782 | +15.0% | +0.0017 to +0.0160 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.415 | 1.401 | −1.0% | −0.0324 to +0.0030 | no |
| Omni's own CPU (cores), mean | 0 | 0.01691 | +0.017 (native is 0) | +0.0156 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.415 | 1.418 | +0.2% | −0.0152 to +0.0197 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.3 | 421.3 | −9.1% | −76.5816 to −7.4753 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.052 | 1.971 | −3.9% | −0.2155 to +0.0535 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, mean (s) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| host CPU busy, the real machine under kind (%) | 42.8 | 41.13 | −3.9% | −2.3147 to −1.0248 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.9 | 752.9 | −3.7% | −45.1328 to −12.8672 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.521 | −24.6% | −2.5597 to −0.3981 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.0625 | −92.0% | −0.8374 to −0.5960 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.5 | −61.5% | −1.3642 to −0.2358 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 93 | 60.66 | −34.8% | −49.8612 to −14.8305 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.348 | −10.9% | −1.2607 to −0.0440 | yes: GAIN |
| node-hours | 2.519 | 2.239 | −11.1% | −0.5343 to −0.0260 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.9 | −0.1% | −0.8951 to +0.5459 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 251.4 | −7.6% | −39.9847 to −1.3603 | yes: GAIN |
| response time (ms), mean | 273.8 | 308.6 | +12.7% | −7.4492 to +77.0970 | no |
| response time (ms), 95th percentile | 851.9 | 1387 | +62.8% | +186.1403 to +884.2717 | yes: LOSS |
| response time (ms), 99th percentile | 1185 | 2131 | +79.9% | +354.0264 to +1538.5058 | yes: LOSS |
| time over the response line (% of samples) | 14.56 | 14.2 | −2.5% | −3.7069 to +2.9852 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 10.1 | +7.4% | +0.3545 to +1.0455 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.800 (native is 0) | +20.0243 to +51.5757 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.2 | 15.88 | +55.8% | +3.4845 to +7.8855 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.058 | 0.06679 | +15.2% | +0.0015 to +0.0161 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.41 | +1.3% | −0.0131 to +0.0489 | no |
| Omni's own CPU (cores), mean | 0 | 0.01853 | +0.019 (native is 0) | +0.0169 to +0.0202 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.428 | +2.6% | +0.0049 to +0.0679 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.9 | 426.8 | −9.2% | −74.8415 to −11.2956 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.936 | 1.998 | +3.2% | −0.0374 to +0.1618 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| host CPU busy, the real machine under kind (%) | 40.09 | 43.78 | +9.2% | +2.9509 to +4.4340 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.7 | 786.3 | +4.9% | +16.7361 to +56.4639 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.786 | −20.2% | −2.2150 to −0.2135 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.8625 | +2487.5% | +0.6506 to +1.0077 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.7 | +466.7% | +0.8999 to +1.9001 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 57.26 | 96.74 | +69.0% | +19.0352 to +59.9314 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*