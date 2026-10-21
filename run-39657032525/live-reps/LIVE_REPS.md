# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.527 |
| node-hours | 2.512 | 1.9 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 224.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 249.5 | 213.9 |
| response time (ms), 95th percentile | 824.5 | 838.5 |
| response time (ms), 99th percentile | 1124 | 1205 |
| time over the response line (% of samples) | 7.842 | 7.751 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.667 | 5.333 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.67 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.126 | 7.606 |
| utilisation (used / allocatable) | 0.0553 | 0.07401 |
| CPU used (cores), mean | 1.327 | 1.312 |
| Omni's own CPU (cores), mean | 0 | 0.01666 |
| CPU used with Omni's own (cores), mean | 1.327 | 1.329 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.5 | 409.8 |
| HPA replicas, mean | 2.086 | 2.033 |
| pods started | 0 | 0.1111 |
| pod start wait, total (s) | 0 | 0.2222 |
| pod start wait, mean (s) | 0 | 0.2222 |
| host CPU busy, the real machine under kind (%) | 37.72 | 38.69 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 757.6 | 757.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.548 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06019 | 0.03704 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 0.1111 |
| queue: job turnaround, submitted to done, mean (s) | 63.31 | 62.31 |
| queue: jobs unfinished at the window's end | 0 | 0 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.527 | -24.6% | -2.315 to -0.6315 | yes: GAIN |
| node-hours | 2.512 | 1.9 | -24.4% | -0.9642 to -0.2603 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 271 | +0.2% | +0.04531 to +1.187 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 224.7 | -16.9% | -71.97 to -19.38 | yes: GAIN |
| response time (ms), mean | 249.5 | 213.9 | -14.3% | -59.88 to -11.43 | yes: GAIN |
| response time (ms), 95th percentile | 824.5 | 838.5 | +1.7% | -40.03 to +67.88 | no |
| response time (ms), 99th percentile | 1124 | 1205 | +7.2% | -2.414 to +164.8 | no |
| time over the response line (% of samples) | 7.842 | 7.751 | -1.2% | -1.036 to +0.8541 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.667 | 5.333 | +14.3% | -0.2748 to +1.608 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.67 | +61.7 (native is 0) | +43.13 to +80.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.126 | 7.606 | -6.4% | -1.928 to +0.8876 | no |
| utilisation (used / allocatable) | 0.0553 | 0.07401 | +33.8% | +0.006621 to +0.03079 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.327 | 1.312 | -1.1% | -0.03737 to +0.007405 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.0167 (native is 0) | +0.01507 to +0.01824 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.327 | 1.329 | +0.1% | -0.01955 to +0.0229 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.5 | 409.8 | -17.8% | -144.1 to -33.21 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.086 | 2.033 | -2.5% | -0.3532 to +0.2473 | no |
| pods started | 0 | 0.1111 | +0.111 (native is 0) | -0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0 | 0.2222 | +0.222 (native is 0) | -0.2902 to +0.7347 | no |
| pod start wait, mean (s) | 0 | 0.2222 | +0.222 (native is 0) | -0.2902 to +0.7347 | no |
| host CPU busy, the real machine under kind (%) | 37.72 | 38.69 | +2.6% | +0.6916 to +1.238 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 757.6 | 757.2 | -0.0% | -2.095 to +1.428 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.548 | -40.9% | -3.731 to -1.172 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06019 | 0.03704 | -38.5% | -0.05139 to +0.005098 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 0.1111 | -66.7% | -0.5612 to +0.1167 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.31 | 62.31 | -1.6% | -3.739 to +1.758 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*