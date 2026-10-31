# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.03 |
| node-hours | 2.514 | 2.107 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 241.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 366.9 | 322.8 |
| response time (ms), 95th percentile | 1346 | 1314 |
| response time (ms), 99th percentile | 1907 | 1871 |
| time over the response line (% of samples) | 14.67 | 14.62 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.52 | 9.727 |
| utilisation (used / allocatable) | 0.05886 | 0.06914 |
| CPU used (cores), mean | 1.413 | 1.394 |
| Omni's own CPU (cores), mean | 0 | 0.01625 |
| CPU used with Omni's own (cores), mean | 1.413 | 1.41 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.6 | 428.6 |
| HPA replicas, mean | 1.969 | 2.021 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.1 |
| pod start wait, mean (s) | 0 | 0.1 |
| host CPU busy, the real machine under kind (%) | 41.37 | 42.14 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 793.2 | 794.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.356 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.1917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 98.9 | 100.3 |
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
| worker nodes in service, mean | 6 | 5.03 | −16.2% | −1.7802 to −0.1590 | yes: GAIN |
| node-hours | 2.514 | 2.107 | −16.2% | −0.7475 to −0.0677 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.6 | −0.2% | −1.4811 to +0.6174 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 241.2 | −11.3% | −56.9087 to −4.8009 | yes: GAIN |
| response time (ms), mean | 366.9 | 322.8 | −12.0% | −65.8505 to −22.2729 | yes: GAIN |
| response time (ms), 95th percentile | 1346 | 1314 | −2.4% | −120.0023 to +55.2803 | no |
| response time (ms), 99th percentile | 1907 | 1871 | −1.9% | −235.1222 to +163.4120 | no |
| time over the response line (% of samples) | 14.67 | 14.62 | −0.4% | −0.5752 to +0.4625 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.6 | −5.0% | −1.0032 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 | +44.400 (native is 0) | +22.5725 to +66.2275 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.52 | 9.727 | +14.2% | −1.5750 to +3.9884 | no |
| utilisation (used / allocatable) | 0.05886 | 0.06914 | +17.4% | +0.0016 to +0.0190 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.413 | 1.394 | −1.3% | −0.0692 to +0.0316 | no |
| Omni's own CPU (cores), mean | 0 | 0.01625 | +0.016 (native is 0) | +0.0149 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.413 | 1.41 | −0.2% | −0.0536 to +0.0485 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.6 | 428.6 | −10.8% | −94.7347 to −9.3280 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.021 | +2.6% | −0.1035 to +0.2072 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 41.37 | 42.14 | +1.9% | +0.4549 to +1.0759 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.2 | 794.5 | +0.2% | −3.8033 to +6.4033 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.356 | −27.4% | −2.9660 to −0.3220 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.1917 | +17.9% | −0.0154 to +0.0737 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.9 | 100.3 | +1.4% | −2.2918 to +5.1251 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*