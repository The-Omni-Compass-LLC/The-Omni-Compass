# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.241 |
| node-hours | 2.518 | 2.195 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 249 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 301.1 | 296.7 |
| response time (ms), 95th percentile | 1185 | 1296 |
| response time (ms), 99th percentile | 1886 | 1981 |
| time over the response line (% of samples) | 9.972 | 11.61 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.3 | 17.81 |
| utilisation (used / allocatable) | 0.06226 | 0.07187 |
| CPU used (cores), mean | 1.494 | 1.48 |
| Omni's own CPU (cores), mean | 0 | 0.01772 |
| CPU used with Omni's own (cores), mean | 1.494 | 1.497 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.4 | 405.6 |
| HPA replicas, mean | 2.03 | 2.297 |
| pods started | 0.1 | 0.8 |
| pod start wait, total (s) | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.375 |
| host CPU busy, the real machine under kind (%) | 43.27 | 44.37 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 801.8 | 807.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.74 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7458 | 0.8167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.9 |
| queue: job turnaround, submitted to done, mean (s) | 111 | 118.4 |
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
| worker nodes in service, mean | 6 | 5.241 | −12.7% | −1.5640 to +0.0454 | no |
| node-hours | 2.518 | 2.195 | −12.8% | −0.6576 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 272.8 | −0.3% | −1.5061 to +0.0186 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 249 | −9.0% | −50.0676 to +0.8634 | no |
| response time (ms), mean | 301.1 | 296.7 | −1.5% | −56.8917 to +48.1016 | no |
| response time (ms), 95th percentile | 1185 | 1296 | +9.4% | −158.1880 to +380.0440 | no |
| response time (ms), 99th percentile | 1886 | 1981 | +5.0% | −62.7665 to +252.1311 | no |
| time over the response line (% of samples) | 9.972 | 11.61 | +16.4% | −0.9190 to +4.1917 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.6 | +10.1% | −0.1294 to +1.5294 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.7 | +51.700 (native is 0) | +29.7793 to +73.6207 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.3 | 17.81 | +16.4% | −2.4411 to +7.4644 | no |
| utilisation (used / allocatable) | 0.06226 | 0.07187 | +15.4% | −0.0003 to +0.0196 | no |
| CPU used (cores), mean | 1.494 | 1.48 | −1.0% | −0.0506 to +0.0212 | no |
| Omni's own CPU (cores), mean | 0 | 0.01772 | +0.018 (native is 0) | +0.0163 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.494 | 1.497 | +0.2% | −0.0336 to +0.0397 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.4 | 405.6 | −8.9% | −81.0840 to +1.4947 | no |
| HPA replicas, mean | 2.03 | 2.297 | +13.1% | −0.0357 to +0.5688 | no |
| pods started | 0.1 | 0.8 | +700.0% | −0.3144 to +1.7144 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.6924 to +2.0924 | no |
| pod start wait, mean (s) | 0.2 | 0.375 | +87.5% | −0.5204 to +0.8704 | no |
| host CPU busy, the real machine under kind (%) | 43.27 | 44.37 | +2.5% | +0.5825 to +1.6227 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 801.8 | 807.2 | +0.7% | −4.2394 to +15.0394 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.74 | −21.0% | −2.5470 to +0.0279 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7458 | 0.8167 | +9.5% | −0.0618 to +0.2034 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.9 | +26.7% | −0.4396 to +1.2396 | no |
| queue: job turnaround, submitted to done, mean (s) | 111 | 118.4 | +6.6% | −2.7910 to +17.4326 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*