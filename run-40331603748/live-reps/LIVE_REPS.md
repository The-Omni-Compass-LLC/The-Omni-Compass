# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.458 | 5.988 |
| node-hours | 2.515 | 2.517 | 2.286 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.2 | 271.5 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 272.2 | 254.5 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 281.4 | 141.2 | 242.8 | 105.9 |
| response time (ms), 95th percentile | 879.3 | 247.3 | 905 | 235.2 |
| response time (ms), 99th percentile | 1257 | 357.5 | 1263 | 342.8 |
| time over the response line (% of samples) | 15.93 | 0.2534 | 15.29 | 0.1414 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 0.2 | 10.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 29.8 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.063 | 1185 | 8.712 | 1161 |
| utilisation (used / allocatable) | 0.05741 | 0.05918 | 0.06418 | 0.05946 |
| CPU used (cores), mean | 1.378 | 1.42 | 1.39 | 1.424 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01656 | 0.01256 |
| CPU used with Omni's own (cores), mean | 1.378 | 1.42 | 1.407 | 1.437 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 457.7 | 437.1 | 455.7 |
| HPA replicas, mean | 1.919 | 2.045 | 2.047 | 2.04 |
| pods started | 0 | 0.2 | 0.2 | 0.1 |
| pod start wait, total (s) | 0 | 0.4 | 0.5 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 | 0.25 | 0.2 |
| host CPU busy, the real machine under kind (%) | 39.72 | 44.64 | 40.6 | 45.15 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 744.4 | 1478 | 746.4 | 1473 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5 | 5.738 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 144.5 | 0.05417 | 159.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 578.3 | 0.4 | 754.9 |
| queue: job turnaround, submitted to done, mean (s) | 53.85 | 888.8 | 54.29 | 861.8 |
| queue: jobs unfinished at the window's end | 0 | 12.8 | 0 | 11.8 |

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
| worker nodes in service, mean | 6 | 5.988 | −0.2% | −0.0389 to +0.0151 | no |
| node-hours | 2.517 | 2.51 | −0.3% | −0.0181 to +0.0041 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.1 | −0.0% | −1.1775 to +0.9286 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.7 | −0.2% | −1.8596 to +0.8607 | no |
| response time (ms), mean | 141.2 | 105.9 | −25.0% | −40.4684 to −30.1847 | yes: GAIN |
| response time (ms), 95th percentile | 247.3 | 235.2 | −4.9% | −31.2688 to +6.9978 | no |
| response time (ms), 99th percentile | 357.5 | 342.8 | −4.1% | −47.8355 to +18.5179 | no |
| time over the response line (% of samples) | 0.2534 | 0.1414 | −44.2% | −0.2310 to +0.0071 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.700 (native is 0) | +9.6200 to +13.7800 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1185 | 1161 | −2.0% | −78.9234 to +30.3534 | no |
| utilisation (used / allocatable) | 0.05918 | 0.05946 | +0.5% | −0.0017 to +0.0022 | no |
| CPU used (cores), mean | 1.42 | 1.424 | +0.3% | −0.0441 to +0.0521 | no |
| Omni's own CPU (cores), mean | 0 | 0.01256 | +0.013 (native is 0) | +0.0117 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.42 | 1.437 | +1.2% | −0.0317 to +0.0648 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.7 | 455.7 | −0.4% | −15.2569 to +11.3236 | no |
| HPA replicas, mean | 2.045 | 2.04 | −0.2% | −0.1427 to +0.1341 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.4 | 0.2 | −50.0% | −1.2556 to +0.8556 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 44.64 | 45.15 | +1.1% | −0.7960 to +1.8200 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1478 | 1473 | −0.3% | −8.6607 to −0.3393 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.476 | −8.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 144.5 | 159.6 | +10.4% | −31.7759 to +61.9676 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 578.3 | 754.9 | +30.5% | −2.7507 to +355.9507 | no |
| queue: job turnaround, submitted to done, mean (s) | 888.8 | 861.8 | −3.0% | −59.8228 to +5.7645 | no |
| queue: jobs unfinished at the window's end | 12.8 | 11.8 | −7.8% | −3.3604 to +1.3604 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 2.515 | 2.517 | +0.1% | −0.0067 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.2 | +0.3% | −1.4115 to +2.9202 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 272.2 | +0.3% | −1.4115 to +2.9202 | no |
| response time (ms), mean | 281.4 | 141.2 | −49.8% | −201.0314 to −79.3618 | yes: GAIN |
| response time (ms), 95th percentile | 879.3 | 247.3 | −71.9% | −907.6017 to −356.3663 | yes: GAIN |
| response time (ms), 99th percentile | 1257 | 357.5 | −71.6% | −1281.0989 to −518.3405 | yes: GAIN |
| time over the response line (% of samples) | 15.93 | 0.2534 | −98.4% | −23.1609 to −8.1958 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 0.2 | −98.0% | −13.0089 to −6.1911 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.063 | 1185 | +12976.9% | +974.3403 to +1377.9330 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05741 | 0.05918 | +3.1% | −0.0025 to +0.0060 | no |
| CPU used (cores), mean | 1.378 | 1.42 | +3.1% | −0.0598 to +0.1448 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.378 | 1.42 | +3.1% | −0.0598 to +0.1448 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 457.7 | −3.9% | −55.4262 to +18.7135 | no |
| HPA replicas, mean | 1.919 | 2.045 | +6.5% | −0.0636 to +0.3144 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 39.72 | 44.64 | +12.4% | +2.6760 to +7.1658 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744.4 | 1478 | +98.5% | +661.7161 to +804.4839 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 144.5 | +315263.6% | +108.3709 to +180.6208 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 578.3 | +192666.7% | +475.4499 to +680.5501 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 53.85 | 888.8 | +1550.6% | +723.7923 to +946.1244 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.8 | +12.800 (native is 0) | +8.2037 to +17.3963 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.458 | −9.0% | −1.1684 to +0.0842 | no |
| node-hours | 2.515 | 2.286 | −9.1% | −0.4871 to +0.0286 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.5 | +0.0% | −0.9445 to +0.9874 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 254.5 | −6.3% | −36.1253 to +2.1556 | no |
| response time (ms), mean | 281.4 | 242.8 | −13.7% | −51.5136 to −25.8754 | yes: GAIN |
| response time (ms), 95th percentile | 879.3 | 905 | +2.9% | −30.6473 to +82.1013 | no |
| response time (ms), 99th percentile | 1257 | 1263 | +0.5% | −88.6142 to +100.2438 | no |
| time over the response line (% of samples) | 15.93 | 15.29 | −4.0% | −1.9330 to +0.6469 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 10.2 | +4.1% | −0.6228 to +1.4228 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.800 (native is 0) | +14.8838 to +44.7162 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.063 | 8.712 | −3.9% | −2.6755 to +1.9722 | no |
| utilisation (used / allocatable) | 0.05741 | 0.06418 | +11.8% | −0.0003 to +0.0138 | no |
| CPU used (cores), mean | 1.378 | 1.39 | +0.9% | −0.0164 to +0.0416 | no |
| Omni's own CPU (cores), mean | 0 | 0.01656 | +0.017 (native is 0) | +0.0146 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.378 | 1.407 | +2.1% | +0.0015 to +0.0569 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 437.1 | −8.2% | −80.4867 to +2.4469 | no |
| HPA replicas, mean | 1.919 | 2.047 | +6.7% | −0.0762 to +0.3315 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.25 | +0.250 (native is 0) | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 39.72 | 40.6 | +2.2% | +0.6511 to +1.0998 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744.4 | 746.4 | +0.3% | −0.7601 to +4.7601 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5 | −16.7% | −2.1541 to +0.1542 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05417 | +18.2% | −0.0152 to +0.0318 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 53.85 | 54.29 | +0.8% | −1.9645 to +2.8562 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.458 | −9.0% | −1.1684 to +0.0842 | no |
| node-hours | 2.517 | 2.286 | −9.2% | −0.4945 to +0.0324 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.5 | −0.3% | −2.7506 to +1.2848 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 254.5 | −6.5% | −38.8257 to +3.3474 | no |
| response time (ms), mean | 141.2 | 242.8 | +71.9% | +51.3701 to +151.6340 | yes: LOSS |
| response time (ms), 95th percentile | 247.3 | 905 | +266.0% | +412.3591 to +903.0629 | yes: LOSS |
| response time (ms), 99th percentile | 357.5 | 1263 | +253.3% | +565.7669 to +1245.3021 | yes: LOSS |
| time over the response line (% of samples) | 0.2534 | 15.29 | +5934.2% | +8.2272 to +21.8433 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 10.2 | +5000.0% | +7.2194 to +12.7806 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.800 (native is 0) | +14.8838 to +44.7162 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1185 | 8.712 | −99.3% | −1378.1623 to −974.8143 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05918 | 0.06418 | +8.4% | +0.0012 to +0.0088 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.42 | 1.39 | −2.1% | −0.1340 to +0.0742 | no |
| Omni's own CPU (cores), mean | 0 | 0.01656 | +0.017 (native is 0) | +0.0146 to +0.0185 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.42 | 1.407 | −0.9% | −0.1163 to +0.0896 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.7 | 437.1 | −4.5% | −34.8014 to −6.5258 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.045 | 2.047 | +0.1% | −0.0871 to +0.0917 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | −1.4249 to +1.6249 | no |
| pod start wait, mean (s) | 0.2 | 0.25 | +25.0% | −0.7124 to +0.8124 | no |
| host CPU busy, the real machine under kind (%) | 44.64 | 40.6 | −9.1% | −6.1286 to −1.9624 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1478 | 746.4 | −49.5% | −801.9378 to −660.2622 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.49 | −58.5% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 144.5 | 0.05417 | −100.0% | −180.6091 to −108.3659 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 578.3 | 0.4 | −99.9% | −680.3266 to −475.4734 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 888.8 | 54.29 | −93.9% | −945.5531 to −723.4719 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.8 | 0 | −100.0% | −17.3963 to −8.2037 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.988 | −0.2% | −0.0389 to +0.0151 | no |
| node-hours | 2.515 | 2.51 | −0.2% | −0.0161 to +0.0058 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 272.1 | +0.2% | −1.2545 to +2.5143 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 271.7 | +0.1% | −1.3456 to +1.8553 | no |
| response time (ms), mean | 281.4 | 105.9 | −62.4% | −237.9753 to −113.0709 | yes: GAIN |
| response time (ms), 95th percentile | 879.3 | 235.2 | −73.3% | −913.0662 to −375.1728 | yes: GAIN |
| response time (ms), 99th percentile | 1257 | 342.8 | −72.7% | −1275.1573 to −553.5997 | yes: GAIN |
| time over the response line (% of samples) | 15.93 | 0.1414 | −99.1% | −23.2801 to −8.3004 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 0 | −100.0% | −13.2848 to −6.3152 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.700 (native is 0) | +9.6200 to +13.7800 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.063 | 1161 | +12708.9% | +943.5735 to +1360.1299 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05741 | 0.05946 | +3.6% | −0.0015 to +0.0056 | no |
| CPU used (cores), mean | 1.378 | 1.424 | +3.4% | −0.0355 to +0.1285 | no |
| Omni's own CPU (cores), mean | 0 | 0.01256 | +0.013 (native is 0) | +0.0117 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.378 | 1.437 | +4.3% | −0.0222 to +0.1404 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 476.1 | 455.7 | −4.3% | −53.1187 to +12.4727 | no |
| HPA replicas, mean | 1.919 | 2.04 | +6.3% | −0.0481 to +0.2902 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 39.72 | 45.15 | +13.7% | +3.9468 to +6.9190 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 744.4 | 1473 | +97.9% | +655.8398 to +801.3602 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.738 | −4.4% | −3.5897 to +3.0659 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 159.6 | +348200.0% | +114.4509 to +204.7324 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 754.9 | +251533.3% | +548.1052 to +961.0948 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 53.85 | 861.8 | +1500.4% | +685.7994 to +930.0589 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.8 | +11.800 (native is 0) | +6.9980 to +16.6020 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*