# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.65 |
| node-hours | 2.517 | 1.949 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 228.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 190.3 | 161.1 |
| response time (ms), 95th percentile | 432.8 | 454 |
| response time (ms), 99th percentile | 691.3 | 788.8 |
| time over the response line (% of samples) | 4.947 | 5.897 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.51 | 13.05 |
| utilisation (used / allocatable) | 0.05541 | 0.07198 |
| CPU used (cores), mean | 1.33 | 1.314 |
| Omni's own CPU (cores), mean | 0 | 0.01645 |
| CPU used with Omni's own (cores), mean | 1.33 | 1.331 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 414.7 |
| HPA replicas, mean | 2.002 | 2.048 |
| pods started | 0.3 | 0 |
| pod start wait, total (s) | 0.9 | 0 |
| pod start wait, mean (s) | 0.9 | 0 |
| host CPU busy, the real machine under kind (%) | 38.91 | 39.8 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 755.5 | 758.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.721 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6667 | 0.7042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 67.15 | 68.94 |
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
| worker nodes in service, mean | 6 | 4.65 | −22.5% | −2.1662 to −0.5344 | yes: GAIN |
| node-hours | 2.517 | 1.949 | −22.6% | −0.9089 to −0.2273 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.6 | −0.1% | −1.0662 to +0.6489 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 228.2 | −15.8% | −68.4319 to −16.8978 | yes: GAIN |
| response time (ms), mean | 190.3 | 161.1 | −15.3% | −42.4346 to −15.9227 | yes: GAIN |
| response time (ms), 95th percentile | 432.8 | 454 | +4.9% | −29.8478 to +72.3518 | no |
| response time (ms), 99th percentile | 691.3 | 788.8 | +14.1% | −59.3981 to +254.2309 | no |
| time over the response line (% of samples) | 4.947 | 5.897 | +19.2% | −0.5347 to +2.4333 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.9 | +13.5% | −0.0578 to +1.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 | +39.800 (native is 0) | +22.4980 to +57.1020 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.51 | 13.05 | +4.4% | −1.6869 to +2.7769 | no |
| utilisation (used / allocatable) | 0.05541 | 0.07198 | +29.9% | +0.0066 to +0.0265 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.33 | 1.314 | −1.2% | −0.0462 to +0.0155 | no |
| Omni's own CPU (cores), mean | 0 | 0.01645 | +0.016 (native is 0) | +0.0141 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.33 | 1.331 | +0.1% | −0.0291 to +0.0313 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 414.7 | −16.4% | −130.1845 to −32.1123 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.048 | +2.3% | −0.0909 to +0.1835 | no |
| pods started | 0.3 | 0 | −100.0% | −0.6455 to +0.0455 | no |
| pod start wait, total (s) | 0.9 | 0 | −100.0% | −1.9900 to +0.1900 | no |
| pod start wait, mean (s) | 0.9 | 0 | −100.0% | −1.9900 to +0.1900 | no |
| host CPU busy, the real machine under kind (%) | 38.91 | 39.8 | +2.3% | +0.6496 to +1.1249 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.5 | 758.4 | +0.4% | −0.2352 to +6.0352 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.721 | −38.0% | −3.6050 to −0.9524 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6667 | 0.7042 | +5.6% | −0.0507 to +0.1257 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.3 | +8.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.15 | 68.94 | +2.7% | −2.0431 to +5.6098 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*