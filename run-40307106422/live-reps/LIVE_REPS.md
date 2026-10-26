# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.018 |
| node-hours | 2.512 | 2.101 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 240.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 349.3 | 332.2 |
| response time (ms), 95th percentile | 1398 | 1582 |
| response time (ms), 99th percentile | 2258 | 2328 |
| time over the response line (% of samples) | 12.75 | 12.46 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.39 | 16.56 |
| utilisation (used / allocatable) | 0.0579 | 0.06981 |
| CPU used (cores), mean | 1.39 | 1.372 |
| Omni's own CPU (cores), mean | 0 | 0.01641 |
| CPU used with Omni's own (cores), mean | 1.39 | 1.388 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.6 | 421.7 |
| HPA replicas, mean | 2.045 | 2.194 |
| pods started | 0.1 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.9 |
| host CPU busy, the real machine under kind (%) | 41.7 | 42.61 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 794 | 799.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.455 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8208 | 0.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 104.7 | 108.5 |
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
| worker nodes in service, mean | 6 | 5.018 | −16.4% | −1.8911 to −0.0729 | yes: GAIN |
| node-hours | 2.512 | 2.101 | −16.3% | −0.7931 to −0.0278 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.5 | +0.0% | −0.8089 to +1.0013 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 240.6 | −11.3% | −59.6487 to −1.9007 | yes: GAIN |
| response time (ms), mean | 349.3 | 332.2 | −4.9% | −27.0702 to −7.1195 | yes: GAIN |
| response time (ms), 95th percentile | 1398 | 1582 | +13.2% | +27.7335 to +340.8665 | yes: LOSS |
| response time (ms), 99th percentile | 2258 | 2328 | +3.1% | −144.7895 to +285.3969 | no |
| time over the response line (% of samples) | 12.75 | 12.46 | −2.3% | −1.1108 to +0.5209 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.8 | +2.6% | −0.6793 to +1.0793 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 | +41.200 (native is 0) | +27.2447 to +55.1553 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.39 | 16.56 | +7.6% | −0.7673 to +3.0973 | no |
| utilisation (used / allocatable) | 0.0579 | 0.06981 | +20.6% | +0.0007 to +0.0231 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.39 | 1.372 | −1.3% | −0.0526 to +0.0173 | no |
| Omni's own CPU (cores), mean | 0 | 0.01641 | +0.016 (native is 0) | +0.0148 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.39 | 1.388 | −0.1% | −0.0370 to +0.0345 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.6 | 421.7 | −12.1% | −115.3418 to −0.5463 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.045 | 2.194 | +7.3% | −0.0677 to +0.3660 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.3144 to +1.7144 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | −0.3144 to +1.7144 | no |
| host CPU busy, the real machine under kind (%) | 41.7 | 42.61 | +2.2% | +0.4296 to +1.3763 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794 | 799.1 | +0.6% | −0.9362 to +11.1362 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.455 | −25.8% | −2.9580 to −0.1327 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8208 | 0.9 | +9.6% | −0.0226 to +0.1809 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 104.7 | 108.5 | +3.6% | −3.1737 to +10.7987 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*