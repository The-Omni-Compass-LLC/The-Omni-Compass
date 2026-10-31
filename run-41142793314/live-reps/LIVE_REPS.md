# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.049 |
| node-hours | 2.516 | 2.111 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 243.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 323.2 | 302.1 |
| response time (ms), 95th percentile | 1187 | 1387 |
| response time (ms), 99th percentile | 2058 | 2286 |
| time over the response line (% of samples) | 12.12 | 11.68 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.6 | 17.51 |
| utilisation (used / allocatable) | 0.06302 | 0.07503 |
| CPU used (cores), mean | 1.512 | 1.514 |
| Omni's own CPU (cores), mean | 0 | 0.01872 |
| CPU used with Omni's own (cores), mean | 1.512 | 1.533 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.9 | 387.6 |
| HPA replicas, mean | 2.03 | 2.009 |
| pods started | 0.2 | 0.1 |
| pod start wait, total (s) | 0.3 | 0.2 |
| pod start wait, mean (s) | 0.3 | 0.2 |
| host CPU busy, the real machine under kind (%) | 43.78 | 44.93 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 812.5 | 816.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.259 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7167 | 0.9042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 2.2 |
| queue: job turnaround, submitted to done, mean (s) | 123 | 128.5 |
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
| worker nodes in service, mean | 6 | 5.049 | −15.8% | −1.5769 to −0.3244 | yes: GAIN |
| node-hours | 2.516 | 2.111 | −16.1% | −0.6681 to −0.1420 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273 | −0.3% | −1.5155 to +0.0058 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 243.2 | −11.2% | −50.2675 to −10.8963 | yes: GAIN |
| response time (ms), mean | 323.2 | 302.1 | −6.5% | −42.3890 to +0.2726 | no |
| response time (ms), 95th percentile | 1187 | 1387 | +16.9% | +4.3123 to +396.4537 | yes: LOSS |
| response time (ms), 99th percentile | 2058 | 2286 | +11.1% | −26.6752 to +483.0040 | no |
| time over the response line (% of samples) | 12.12 | 11.68 | −3.6% | −1.3804 to +0.5060 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.7 | ±0.0% | −1.1184 to +1.1184 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.5 | +48.500 (native is 0) | +22.8634 to +74.1366 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.6 | 17.51 | +12.2% | −0.1715 to +3.9915 | no |
| utilisation (used / allocatable) | 0.06302 | 0.07503 | +19.1% | +0.0042 to +0.0198 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.512 | 1.514 | +0.1% | −0.0246 to +0.0275 | no |
| Omni's own CPU (cores), mean | 0 | 0.01872 | +0.019 (native is 0) | +0.0174 to +0.0200 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.512 | 1.533 | +1.3% | −0.0057 to +0.0460 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.9 | 387.6 | −12.5% | −93.1649 to −17.4553 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.03 | 2.009 | −1.0% | −0.1061 to +0.0641 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.3 | 0.2 | −33.3% | −0.8113 to +0.6113 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.8113 to +0.6113 | no |
| host CPU busy, the real machine under kind (%) | 43.78 | 44.93 | +2.6% | +0.9138 to +1.3867 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 816.6 | +0.5% | −0.0222 to +8.2222 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.259 | −29.0% | −2.7850 to −0.6973 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7167 | 0.9042 | +26.2% | −0.0803 to +0.4553 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 2.2 | +57.1% | −1.0714 to +2.6714 | no |
| queue: job turnaround, submitted to done, mean (s) | 123 | 128.5 | +4.5% | +0.3971 to +10.6862 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*