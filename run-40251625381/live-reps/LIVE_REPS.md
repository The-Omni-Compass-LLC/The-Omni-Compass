# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.214 |
| node-hours | 2.512 | 2.191 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 247.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 429.4 | 379 |
| response time (ms), 95th percentile | 2577 | 2568 |
| response time (ms), 99th percentile | 4029 | 4021 |
| time over the response line (% of samples) | 14.71 | 14 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 171.3 | 170 |
| utilisation (used / allocatable) | 0.05703 | 0.06535 |
| CPU used (cores), mean | 1.369 | 1.347 |
| Omni's own CPU (cores), mean | 0 | 0.01551 |
| CPU used with Omni's own (cores), mean | 1.369 | 1.362 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.9 | 440.7 |
| HPA replicas, mean | 1.968 | 2.256 |
| pods started | 0 | 1 |
| pod start wait, total (s) | 0 | 4 |
| pod start wait, mean (s) | 0 | 2.2 |
| host CPU busy, the real machine under kind (%) | 39.25 | 39.62 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 529.7 | 528.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.834 |

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
| worker nodes in service, mean | 6 | 5.214 | −13.1% | −1.3784 to −0.1937 | yes: GAIN |
| node-hours | 2.512 | 2.191 | −12.8% | −0.5716 to −0.0718 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.8 | +0.3% | −0.7605 to +2.1763 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 247.1 | −8.9% | −42.7751 to −5.2383 | yes: GAIN |
| response time (ms), mean | 429.4 | 379 | −11.7% | −67.2451 to −33.5768 | yes: GAIN |
| response time (ms), 95th percentile | 2577 | 2568 | −0.4% | −130.7948 to +111.4548 | no |
| response time (ms), 99th percentile | 4029 | 4021 | −0.2% | −179.3254 to +163.2674 | no |
| time over the response line (% of samples) | 14.71 | 14 | −4.8% | −1.2831 to −0.1327 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.2 | +1.1% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.600 (native is 0) | +11.0112 to +14.1888 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 171.3 | 170 | −0.8% | −5.3416 to +2.7383 | no |
| utilisation (used / allocatable) | 0.05703 | 0.06535 | +14.6% | −0.0002 to +0.0168 | no |
| CPU used (cores), mean | 1.369 | 1.347 | −1.6% | −0.0689 to +0.0244 | no |
| Omni's own CPU (cores), mean | 0 | 0.01551 | +0.016 (native is 0) | +0.0143 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.369 | 1.362 | −0.5% | −0.0530 to +0.0395 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.9 | 440.7 | −8.4% | −84.6585 to +4.2164 | no |
| HPA replicas, mean | 1.968 | 2.256 | +14.7% | −0.2254 to +0.8020 | no |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.4160 to +1.5840 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | −0.2519 to +8.2519 | no |
| pod start wait, mean (s) | 0 | 2.2 | +2.200 (native is 0) | +0.1475 to +4.2525 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.25 | 39.62 | +0.9% | −0.0500 to +0.7819 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 529.7 | 528.7 | −0.2% | −6.9466 to +4.9466 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.834 | −19.4% | −2.0276 to −0.3035 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*