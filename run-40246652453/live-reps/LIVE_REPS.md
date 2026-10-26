# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 141.7 | 73.53 |
| response time (ms), 95th percentile | 317.3 | 108.4 |
| response time (ms), 99th percentile | 505.8 | 138.3 |
| time over the response line (% of samples) | 1.74 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1867 |
| utilisation (used / allocatable) | 0.03596 | 0.03445 |
| CPU used (cores), mean | 0.863 | 0.8269 |
| Omni's own CPU (cores), mean | 0 | 0.00781 |
| CPU used with Omni's own (cores), mean | 0.863 | 0.8347 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 784.4 | 815 |
| HPA replicas, mean | 8.179 | 7.665 |
| pods started | 5.5 | 2.8 |
| pod start wait, total (s) | 7.3 | 3.8 |
| pod start wait, mean (s) | 1.347 | 1.35 |
| host CPU busy, the real machine under kind (%) | 26.06 | 25.21 |
| host cores (the real machine under kind) | 4 | 4 |

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
| node-hours | 1.518 | 1.52 | +0.1% | −0.0004 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.8 | −0.1% | −0.4238 to −0.0117 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.8 | −0.1% | −0.4238 to −0.0117 | yes: GAIN |
| response time (ms), mean | 141.7 | 73.53 | −48.1% | −93.5843 to −42.7412 | yes: GAIN |
| response time (ms), 95th percentile | 317.3 | 108.4 | −65.8% | −281.8865 to −135.9425 | yes: GAIN |
| response time (ms), 99th percentile | 505.8 | 138.3 | −72.7% | −516.6941 to −218.3543 | yes: GAIN |
| time over the response line (% of samples) | 1.74 | 0 | −100.0% | −3.0473 to −0.4327 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.4617 to −0.3383 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15 | +15.000 (native is 0) | +12.5452 to +17.4548 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1867 | +75.0% | −0.0770 to +0.2370 | no |
| utilisation (used / allocatable) | 0.03596 | 0.03445 | −4.2% | −0.0022 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.863 | 0.8269 | −4.2% | −0.0520 to −0.0203 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00781 | +0.008 (native is 0) | +0.0066 to +0.0090 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.863 | 0.8347 | −3.3% | −0.0436 to −0.0131 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 784.4 | 815 | +3.9% | +16.6149 to +44.5927 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.179 | 7.665 | −6.3% | −1.1640 to +0.1361 | no |
| pods started | 5.5 | 2.8 | −49.1% | −3.1828 to −2.2172 | yes: GAIN |
| pod start wait, total (s) | 7.3 | 3.8 | −47.9% | −4.9005 to −2.0995 | yes: GAIN |
| pod start wait, mean (s) | 1.347 | 1.35 | +0.2% | −0.2357 to +0.2414 | no |
| host CPU busy, the real machine under kind (%) | 26.06 | 25.21 | −3.3% | −1.2084 to −0.4955 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*