# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.895 |
| node-hours | 2.511 | 2.472 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 268 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 134 | 100.1 |
| response time (ms), 95th percentile | 231 | 220.7 |
| response time (ms), 99th percentile | 346.4 | 336.2 |
| time over the response line (% of samples) | 0.2547 | 0.2754 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1038 | 1041 |
| utilisation (used / allocatable) | 0.05712 | 0.05846 |
| CPU used (cores), mean | 1.371 | 1.38 |
| Omni's own CPU (cores), mean | 0 | 0.01265 |
| CPU used with Omni's own (cores), mean | 1.371 | 1.393 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.3 | 465 |
| HPA replicas, mean | 2.019 | 2.012 |
| pods started | 0.2 | 0 |
| pod start wait, total (s) | 0.5 | 0 |
| pod start wait, mean (s) | 0.5 | 0 |
| host CPU busy, the real machine under kind (%) | 42.51 | 43.49 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1391 | 1384 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.848 |
| queue: job wait, submitted to its first pod running, mean (s) | 158.2 | 167.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 674.5 | 770.8 |
| queue: job turnaround, submitted to done, mean (s) | 774 | 789.3 |
| queue: jobs unfinished at the window's end | 11.7 | 11.7 |

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
| worker nodes in service, mean | 6 | 5.895 | −1.7% | −0.2654 to +0.0554 | no |
| node-hours | 2.511 | 2.472 | −1.6% | −0.1126 to +0.0332 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | +0.2% | −0.5927 to +1.6444 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 268 | −1.0% | −8.4824 to +2.9591 | no |
| response time (ms), mean | 134 | 100.1 | −25.3% | −42.4733 to −25.2764 | yes: GAIN |
| response time (ms), 95th percentile | 231 | 220.7 | −4.4% | −22.8309 to +2.2699 | no |
| response time (ms), 99th percentile | 346.4 | 336.2 | −2.9% | −35.6787 to +15.2617 | no |
| time over the response line (% of samples) | 0.2547 | 0.2754 | +8.1% | −0.1633 to +0.2047 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 | +13.200 (native is 0) | +10.3427 to +16.0573 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1038 | 1041 | +0.3% | −45.8177 to +52.2344 | no |
| utilisation (used / allocatable) | 0.05712 | 0.05846 | +2.3% | −0.0006 to +0.0033 | no |
| CPU used (cores), mean | 1.371 | 1.38 | +0.7% | −0.0298 to +0.0488 | no |
| Omni's own CPU (cores), mean | 0 | 0.01265 | +0.013 (native is 0) | +0.0118 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.371 | 1.393 | +1.6% | −0.0170 to +0.0613 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.3 | 465 | −2.0% | −23.5815 to +4.9073 | no |
| HPA replicas, mean | 2.019 | 2.012 | −0.3% | −0.1172 to +0.1033 | no |
| pods started | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| pod start wait, mean (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| host CPU busy, the real machine under kind (%) | 42.51 | 43.49 | +2.3% | +0.3347 to +1.6241 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1391 | 1384 | −0.5% | −38.7817 to +24.9817 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.848 | −19.2% | −3.0862 to +0.7820 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 158.2 | 167.2 | +5.7% | −11.4038 to +29.4038 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 674.5 | 770.8 | +14.3% | −53.5109 to +246.1109 | no |
| queue: job turnaround, submitted to done, mean (s) | 774 | 789.3 | +2.0% | −42.8760 to +73.5677 | no |
| queue: jobs unfinished at the window's end | 11.7 | 11.7 | ±0.0% | −1.8774 to +1.8774 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*