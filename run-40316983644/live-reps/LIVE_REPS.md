# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.971 |
| node-hours | 2.522 | 2.507 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 131.4 | 98.55 |
| response time (ms), 95th percentile | 223 | 210.4 |
| response time (ms), 99th percentile | 319 | 321.1 |
| time over the response line (% of samples) | 0.1692 | 0.1417 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1008 | 1000 |
| utilisation (used / allocatable) | 0.05929 | 0.05938 |
| CPU used (cores), mean | 1.423 | 1.418 |
| Omni's own CPU (cores), mean | 0 | 0.01184 |
| CPU used with Omni's own (cores), mean | 1.423 | 1.43 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.4 | 456.4 |
| HPA replicas, mean | 1.983 | 2.035 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 43.85 | 44.02 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1416 | 1391 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.731 |
| queue: job wait, submitted to its first pod running, mean (s) | 129.1 | 137.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 639.2 | 631.2 |
| queue: job turnaround, submitted to done, mean (s) | 782.1 | 743.7 |
| queue: jobs unfinished at the window's end | 8.4 | 8.6 |

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
| worker nodes in service, mean | 6 | 5.971 | −0.5% | −0.0662 to +0.0079 | no |
| node-hours | 2.522 | 2.507 | −0.6% | −0.0270 to −0.0029 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.3 | −0.1% | −1.0340 to +0.3483 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.3 | −0.5% | −2.3701 to −0.1531 | yes: GAIN |
| response time (ms), mean | 131.4 | 98.55 | −25.0% | −39.6983 to −25.9679 | yes: GAIN |
| response time (ms), 95th percentile | 223 | 210.4 | −5.7% | −22.5689 to −2.7741 | yes: GAIN |
| response time (ms), 99th percentile | 319 | 321.1 | +0.7% | −13.9702 to +18.1364 | no |
| time over the response line (% of samples) | 0.1692 | 0.1417 | −16.2% | −0.1423 to +0.0874 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.1 | +13.100 (native is 0) | +11.0365 to +15.1635 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1008 | 1000 | −0.8% | −70.4590 to +54.6990 | no |
| utilisation (used / allocatable) | 0.05929 | 0.05938 | +0.2% | −0.0013 to +0.0015 | no |
| CPU used (cores), mean | 1.423 | 1.418 | −0.3% | −0.0381 to +0.0292 | no |
| Omni's own CPU (cores), mean | 0 | 0.01184 | +0.012 (native is 0) | +0.0108 to +0.0129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.423 | 1.43 | +0.5% | −0.0264 to +0.0413 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.4 | 456.4 | +0.0% | −10.0843 to +10.1728 | no |
| HPA replicas, mean | 1.983 | 2.035 | +2.6% | −0.1052 to +0.2096 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.85 | 44.02 | +0.4% | −0.4274 to +0.7728 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1416 | 1391 | −1.8% | −59.5355 to +9.7355 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.731 | −4.5% | −0.6211 to +0.0827 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 129.1 | 137.9 | +6.8% | −8.5276 to +26.1359 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 639.2 | 631.2 | −1.3% | −156.5866 to +140.5866 | no |
| queue: job turnaround, submitted to done, mean (s) | 782.1 | 743.7 | −4.9% | −76.0706 to −0.8377 | yes: GAIN |
| queue: jobs unfinished at the window's end | 8.4 | 8.6 | +2.4% | −0.5388 to +0.9388 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*