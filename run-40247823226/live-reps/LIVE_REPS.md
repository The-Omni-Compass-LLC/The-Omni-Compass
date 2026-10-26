# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.5 | 159.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.5 | 159.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 177.2 | 86.27 | 91.85 |
| response time (ms), 95th percentile | 402 | 132.9 | 114.7 |
| response time (ms), 99th percentile | 671.7 | 174.1 | 146.6 |
| time over the response line (% of samples) | 3.128 | 0 | 0.3763 |
| failed requests (%) | 0 | 0 | 0.08597 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.8 | 0 | 0.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | 70.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1333 | 0.1583 |
| utilisation (used / allocatable) | 0.04241 | 0.03962 | 0.03911 |
| CPU used (cores), mean | 1.018 | 0.9509 | 0.9386 |
| Omni's own CPU (cores), mean | 0 | 0.00905 | 0.01283 |
| CPU used with Omni's own (cores), mean | 1.018 | 0.9599 | 0.9514 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 639.9 | 677 | 684.9 |
| HPA replicas, mean | 8.773 | 8.371 | 1 |
| pods started | 5.4 | 2.9 | 0 |
| pod start wait, total (s) | 7.6 | 5.5 | 0 |
| pod start wait, mean (s) | 1.422 | 1.812 | 0 |
| host CPU busy, the real machine under kind (%) | 30.37 | 28.89 | 28.56 |
| host cores (the real machine under kind) | 4 | 4 | 4 |

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
| node-hours | 1.513 | 1.516 | +0.2% | −0.0018 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.5 | −0.2% | −0.8797 to +0.2171 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.5 | −0.2% | −0.8797 to +0.2171 | no |
| response time (ms), mean | 177.2 | 86.27 | −51.3% | −111.3950 to −70.5554 | yes: GAIN |
| response time (ms), 95th percentile | 402 | 132.9 | −66.9% | −322.7344 to −215.4326 | yes: GAIN |
| response time (ms), 99th percentile | 671.7 | 174.1 | −74.1% | −604.6865 to −390.5105 | yes: GAIN |
| time over the response line (% of samples) | 3.128 | 0 | −100.0% | −4.3636 to −1.8921 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.8 | 0 | −100.0% | −5.3004 to −2.2996 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.9 | +17.900 (native is 0) | +15.3001 to +20.4999 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1333 | +25.0% | −0.2188 to +0.2721 | no |
| utilisation (used / allocatable) | 0.04241 | 0.03962 | −6.6% | −0.0040 to −0.0016 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.018 | 0.9509 | −6.6% | −0.0963 to −0.0378 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00905 | +0.009 (native is 0) | +0.0083 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.018 | 0.9599 | −5.7% | −0.0867 to −0.0294 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 639.9 | 677 | +5.8% | +21.6526 to +52.5639 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.773 | 8.371 | −4.6% | −1.1448 to +0.3411 | no |
| pods started | 5.4 | 2.9 | −46.3% | −3.7274 to −1.2726 | yes: GAIN |
| pod start wait, total (s) | 7.6 | 5.5 | −27.6% | −5.0290 to +0.8290 | no |
| pod start wait, mean (s) | 1.422 | 1.812 | +27.4% | +0.0825 to +0.6970 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.37 | 28.89 | −4.9% | −2.3029 to −0.6736 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.516 | +0.2% | −0.0015 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.8 | −0.0% | −0.6179 to +0.5166 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.8 | −0.0% | −0.6179 to +0.5166 | no |
| response time (ms), mean | 177.2 | 91.85 | −48.2% | −106.5649 to −64.2163 | yes: GAIN |
| response time (ms), 95th percentile | 402 | 114.7 | −71.5% | −347.8508 to −226.6322 | yes: GAIN |
| response time (ms), 99th percentile | 671.7 | 146.6 | −78.2% | −640.6451 to −409.6797 | yes: GAIN |
| time over the response line (% of samples) | 3.128 | 0.3763 | −88.0% | −4.0557 to −1.4474 | yes: GAIN |
| failed requests (%) | 0 | 0.08597 | +0.086 (native is 0) | +0.0435 to +0.1284 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.8 | 0.7 | −81.6% | −4.8011 to −1.3989 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.2 | +70.200 (native is 0) | +68.8179 to +71.5821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1583 | +48.4% | −0.1443 to +0.2477 | no |
| utilisation (used / allocatable) | 0.04241 | 0.03911 | −7.8% | −0.0048 to −0.0018 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.018 | 0.9386 | −7.8% | −0.1153 to −0.0435 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01283 | +0.013 (native is 0) | +0.0120 to +0.0136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.018 | 0.9514 | −6.5% | −0.1018 to −0.0314 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 639.9 | 684.9 | +7.0% | +23.0755 to +66.9016 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.773 | 1 | −88.6% | −8.0655 to −7.4809 | yes: GAIN |
| pods started | 5.4 | 0 | −100.0% | −5.9001 to −4.8999 | yes: GAIN |
| pod start wait, total (s) | 7.6 | 0 | −100.0% | −8.9146 to −6.2854 | yes: GAIN |
| pod start wait, mean (s) | 1.422 | 0 | −100.0% | −1.6956 to −1.1483 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 30.37 | 28.56 | −6.0% | −2.9007 to −0.7221 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | =0.0% | −0.0013 to +0.0013 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159.8 | +0.2% | +0.0304 to +0.5309 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159.8 | +0.2% | +0.0304 to +0.5309 | yes: power given |
| response time (ms), mean | 86.27 | 91.85 | +6.5% | +3.4917 to +7.6774 | yes: LOSS |
| response time (ms), 95th percentile | 132.9 | 114.7 | −13.7% | −26.7567 to −9.5593 | yes: GAIN |
| response time (ms), 99th percentile | 174.1 | 146.6 | −15.8% | −43.5275 to −11.6003 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.3763 | +0.376 (native is 0) | +0.2941 to +0.4585 | yes: LOSS |
| failed requests (%) | 0 | 0.08597 | +0.086 (native is 0) | +0.0435 to +0.1284 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.7 | +0.700 (native is 0) | +0.3545 to +1.0455 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 17.9 | 70.2 | +292.2% | +49.7088 to +54.8912 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1583 | +18.7% | −0.1649 to +0.2149 | no |
| utilisation (used / allocatable) | 0.03962 | 0.03911 | −1.3% | −0.0012 to +0.0001 | no |
| CPU used (cores), mean | 0.9509 | 0.9386 | −1.3% | −0.0280 to +0.0034 | no |
| Omni's own CPU (cores), mean | 0.00905 | 0.01283 | +41.8% | +0.0036 to +0.0040 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9599 | 0.9514 | −0.9% | −0.0243 to +0.0072 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 677 | 684.9 | +1.2% | −4.5408 to +20.3016 | no |
| HPA replicas, mean | 8.371 | 1 | −88.1% | −8.2795 to −6.4632 | yes: GAIN |
| pods started | 2.9 | 0 | −100.0% | −4.0410 to −1.7590 | yes: GAIN |
| pod start wait, total (s) | 5.5 | 0 | −100.0% | −8.2029 to −2.7971 | yes: GAIN |
| pod start wait, mean (s) | 1.812 | 0 | −100.0% | −2.0217 to −1.6017 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 28.89 | 28.56 | −1.1% | −0.8141 to +0.1676 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*