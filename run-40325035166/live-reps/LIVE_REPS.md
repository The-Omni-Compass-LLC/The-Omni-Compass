# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.977 |
| node-hours | 2.511 | 2.504 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 271.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 150 | 110.7 |
| response time (ms), 95th percentile | 258.5 | 238.9 |
| response time (ms), 99th percentile | 378.5 | 349.6 |
| time over the response line (% of samples) | 0.2931 | 0.2235 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1206 | 1194 |
| utilisation (used / allocatable) | 0.0586 | 0.06062 |
| CPU used (cores), mean | 1.406 | 1.45 |
| Omni's own CPU (cores), mean | 0 | 0.01274 |
| CPU used with Omni's own (cores), mean | 1.406 | 1.462 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.4 | 447.8 |
| HPA replicas, mean | 2.103 | 2.05 |
| pods started | 0.2 | 0 |
| pod start wait, total (s) | 0.4 | 0 |
| pod start wait, mean (s) | 0.2 | 0 |
| host CPU busy, the real machine under kind (%) | 44.13 | 45.26 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1463 | 1471 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 |
| queue: job wait, submitted to its first pod running, mean (s) | 157.1 | 171.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 666.7 | 761.3 |
| queue: job turnaround, submitted to done, mean (s) | 894.1 | 871.6 |
| queue: jobs unfinished at the window's end | 13.6 | 13.1 |

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
| worker nodes in service, mean | 6 | 5.977 | −0.4% | −0.0754 to +0.0292 | no |
| node-hours | 2.511 | 2.504 | −0.3% | −0.0333 to +0.0183 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 272.2 | +0.3% | −0.1955 to +1.8305 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 271.4 | +0.0% | −2.2424 to +2.4274 | no |
| response time (ms), mean | 150 | 110.7 | −26.2% | −44.2221 to −34.4390 | yes: GAIN |
| response time (ms), 95th percentile | 258.5 | 238.9 | −7.6% | −27.9355 to −11.2855 | yes: GAIN |
| response time (ms), 99th percentile | 378.5 | 349.6 | −7.6% | −45.8671 to −11.9431 | yes: GAIN |
| time over the response line (% of samples) | 0.2931 | 0.2235 | −23.8% | −0.1659 to +0.0266 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.2 | +12.200 (native is 0) | +9.7498 to +14.6502 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1206 | 1194 | −1.0% | −53.6080 to +29.3114 | no |
| utilisation (used / allocatable) | 0.0586 | 0.06062 | +3.4% | +0.0010 to +0.0030 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.406 | 1.45 | +3.1% | +0.0148 to +0.0718 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01274 | +0.013 (native is 0) | +0.0120 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.462 | +4.0% | +0.0271 to +0.0850 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.4 | 447.8 | −2.9% | −20.4373 to −6.7404 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.103 | 2.05 | −2.5% | −0.1893 to +0.0833 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.4 | 0 | −100.0% | −1.3048 to +0.5048 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 44.13 | 45.26 | +2.6% | +0.4360 to +1.8334 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1463 | 1471 | +0.5% | −4.8448 to +20.2448 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 | −8.3% | −6.8530 to +5.8530 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 157.1 | 171.7 | +9.3% | −26.5042 to +55.6626 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 666.7 | 761.3 | +14.2% | −106.2238 to +295.4238 | no |
| queue: job turnaround, submitted to done, mean (s) | 894.1 | 871.6 | −2.5% | −68.8923 to +23.8590 | no |
| queue: jobs unfinished at the window's end | 13.6 | 13.1 | −3.7% | −2.0174 to +1.0174 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*