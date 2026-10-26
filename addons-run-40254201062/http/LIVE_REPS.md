# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 205.7 | 87.54 |
| response time (ms), 95th percentile | 493.5 | 135.1 |
| response time (ms), 99th percentile | 688.5 | 274.1 |
| time over the response line (% of samples) | 5.406 | 0.2808 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.05333 |
| utilisation (used / allocatable) | 0.03058 | 0.0476 |
| CPU used (cores), mean | 0.7339 | 1.142 |
| Omni's own CPU (cores), mean | 0 | 0.01021 |
| CPU used with Omni's own (cores), mean | 0.7339 | 1.153 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.8 | 565.9 |
| HPA replicas, mean | 2.955 | 2.432 |
| pods started | 2.9 | 2.3 |
| pod start wait, total (s) | 3.7 | 2.9 |
| pod start wait, mean (s) | 1.283 | 1.267 |
| host CPU busy, the real machine under kind (%) | 23.18 | 34.93 |
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
| node-hours | 1.519 | 1.514 | −0.3% | −0.0111 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.4 | +2.1% | +2.4491 to +4.3241 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.4 | +2.1% | +2.4491 to +4.3241 | yes: power given |
| response time (ms), mean | 205.7 | 87.54 | −57.5% | −141.9070 to −94.4995 | yes: GAIN |
| response time (ms), 95th percentile | 493.5 | 135.1 | −72.6% | −415.3465 to −301.3255 | yes: GAIN |
| response time (ms), 99th percentile | 688.5 | 274.1 | −60.2% | −532.5917 to −296.1271 | yes: GAIN |
| time over the response line (% of samples) | 5.406 | 0.2808 | −94.8% | −7.2623 to −2.9882 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0.3 | −93.9% | −6.4835 to −2.7165 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.7 | +5.700 (native is 0) | +3.4118 to +7.9882 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.05333 | −31.9% | −0.0859 to +0.0359 | no |
| utilisation (used / allocatable) | 0.03058 | 0.0476 | +55.7% | +0.0148 to +0.0192 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7339 | 1.142 | +55.7% | +0.3560 to +0.4612 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01021 | +0.010 (native is 0) | +0.0089 to +0.0115 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7339 | 1.153 | +57.1% | +0.3651 to +0.4726 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.8 | 565.9 | −33.8% | −304.4516 to −273.3817 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.955 | 2.432 | −17.7% | −0.7268 to −0.3198 | yes: GAIN |
| pods started | 2.9 | 2.3 | −20.7% | −0.9694 to −0.2306 | yes: GAIN |
| pod start wait, total (s) | 3.7 | 2.9 | −21.6% | −1.3642 to −0.2358 | yes: GAIN |
| pod start wait, mean (s) | 1.283 | 1.267 | −1.3% | −0.3111 to +0.2778 | no |
| host CPU busy, the real machine under kind (%) | 23.18 | 34.93 | +50.7% | +10.1572 to +13.3415 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*