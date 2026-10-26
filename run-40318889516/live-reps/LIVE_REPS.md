# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.751 |
| node-hours | 2.511 | 2.413 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 265.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 320.6 | 284.6 |
| response time (ms), 95th percentile | 1157 | 1197 |
| response time (ms), 99th percentile | 1874 | 1973 |
| time over the response line (% of samples) | 14.7 | 14.89 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 12.01 |
| utilisation (used / allocatable) | 0.06086 | 0.06312 |
| CPU used (cores), mean | 1.461 | 1.452 |
| Omni's own CPU (cores), mean | 0 | 0.01585 |
| CPU used with Omni's own (cores), mean | 1.461 | 1.468 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.7 | 437.5 |
| HPA replicas, mean | 2.127 | 2.176 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.6 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 41.74 | 42.57 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 764.8 | 767.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.507 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.06667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 78.15 | 81.26 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.751 | −4.1% | −0.5113 to +0.0133 | no |
| node-hours | 2.511 | 2.413 | −3.9% | −0.2082 to +0.0122 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 273 | +0.2% | +0.2085 to +1.1140 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 265.2 | −2.6% | −15.5522 to +1.2040 | no |
| response time (ms), mean | 320.6 | 284.6 | −11.2% | −53.7231 to −18.1547 | yes: GAIN |
| response time (ms), 95th percentile | 1157 | 1197 | +3.5% | −21.4747 to +103.3217 | no |
| response time (ms), 99th percentile | 1874 | 1973 | +5.3% | −118.4187 to +316.5407 | no |
| time over the response line (% of samples) | 14.7 | 14.89 | +1.3% | −1.6746 to +2.0573 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.9 | +2.8% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 | +32.300 (native is 0) | +21.1110 to +43.4890 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.31 | 12.01 | +6.2% | −1.0617 to +2.4617 | no |
| utilisation (used / allocatable) | 0.06086 | 0.06312 | +3.7% | −0.0002 to +0.0048 | no |
| CPU used (cores), mean | 1.461 | 1.452 | −0.6% | −0.0226 to +0.0061 | no |
| Omni's own CPU (cores), mean | 0 | 0.01585 | +0.016 (native is 0) | +0.0146 to +0.0171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.468 | +0.5% | −0.0073 to +0.0224 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.7 | 437.5 | −2.5% | −24.4438 to +2.0271 | no |
| HPA replicas, mean | 2.127 | 2.176 | +2.3% | −0.1628 to +0.2609 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| host CPU busy, the real machine under kind (%) | 41.74 | 42.57 | +2.0% | +0.7191 to +0.9280 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 764.8 | 767.8 | +0.4% | −0.4055 to +6.4055 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.507 | −8.2% | −1.0079 to +0.0217 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.06667 | −20.0% | −0.0677 to +0.0344 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.15 | 81.26 | +4.0% | +1.0026 to +5.2141 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*