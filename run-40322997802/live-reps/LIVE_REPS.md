# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.997 |
| node-hours | 2.516 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 139.9 | 103.8 |
| response time (ms), 95th percentile | 235.3 | 224.5 |
| response time (ms), 99th percentile | 340.1 | 341.3 |
| time over the response line (% of samples) | 0.1623 | 0.1854 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1076 | 1153 |
| utilisation (used / allocatable) | 0.05951 | 0.05897 |
| CPU used (cores), mean | 1.428 | 1.415 |
| Omni's own CPU (cores), mean | 0 | 0.01217 |
| CPU used with Omni's own (cores), mean | 1.428 | 1.427 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.1 | 459 |
| HPA replicas, mean | 2.023 | 1.963 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 44.59 | 44.63 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1475 | 1470 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.921 |
| queue: job wait, submitted to its first pod running, mean (s) | 172.8 | 150.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 756 | 701.7 |
| queue: job turnaround, submitted to done, mean (s) | 827.4 | 886.4 |
| queue: jobs unfinished at the window's end | 10.2 | 11 |

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
| worker nodes in service, mean | 6 | 5.997 | −0.1% | −0.0109 to +0.0042 | no |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0151 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.8 | −0.2% | −1.6843 to +0.8161 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.7 | −0.2% | −1.9113 to +0.8347 | no |
| response time (ms), mean | 139.9 | 103.8 | −25.8% | −40.8593 to −31.3719 | yes: GAIN |
| response time (ms), 95th percentile | 235.3 | 224.5 | −4.6% | −24.0071 to +2.4431 | no |
| response time (ms), 99th percentile | 340.1 | 341.3 | +0.3% | −28.4438 to +30.6994 | no |
| time over the response line (% of samples) | 0.1623 | 0.1854 | +14.3% | −0.1441 to +0.1905 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.3 | +11.300 (native is 0) | +9.7166 to +12.8834 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1076 | 1153 | +7.1% | +10.4664 to +143.1336 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05951 | 0.05897 | −0.9% | −0.0026 to +0.0015 | no |
| CPU used (cores), mean | 1.428 | 1.415 | −1.0% | −0.0643 to +0.0367 | no |
| Omni's own CPU (cores), mean | 0 | 0.01217 | +0.012 (native is 0) | +0.0115 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.428 | 1.427 | −0.1% | −0.0522 to +0.0489 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.1 | 459 | +0.8% | −10.7038 to +18.4008 | no |
| HPA replicas, mean | 2.023 | 1.963 | −3.0% | −0.2199 to +0.1005 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 44.59 | 44.63 | +0.1% | −0.9757 to +1.0608 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1475 | 1470 | −0.3% | −22.5464 to +12.9464 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.921 | −1.3% | −1.0821 to +0.9242 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 172.8 | 150.3 | −13.1% | −63.3105 to +18.1605 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 756 | 701.7 | −7.2% | −239.5835 to +130.9835 | no |
| queue: job turnaround, submitted to done, mean (s) | 827.4 | 886.4 | +7.1% | −2.5187 to +120.6520 | no |
| queue: jobs unfinished at the window's end | 10.2 | 11 | +7.8% | −1.1312 to +2.7312 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*