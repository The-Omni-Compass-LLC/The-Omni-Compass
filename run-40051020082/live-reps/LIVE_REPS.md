# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.611 |
| node-hours | 2.511 | 1.934 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 270.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 227.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 235.2 | 207.7 |
| response time (ms), 95th percentile | 815 | 847.7 |
| response time (ms), 99th percentile | 1217 | 1328 |
| time over the response line (% of samples) | 9.997 | 9.714 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.982 | 10.03 |
| utilisation (used / allocatable) | 0.05453 | 0.07188 |
| CPU used (cores), mean | 1.309 | 1.297 |
| Omni's own CPU (cores), mean | 0 | 0.01549 |
| CPU used with Omni's own (cores), mean | 1.309 | 1.312 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.9 | 417.1 |
| HPA replicas, mean | 1.933 | 2.166 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 37.7 | 38.42 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 745.8 | 749 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.719 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 57.02 | 59.88 |
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
| worker nodes in service, mean | 6 | 4.611 | -23.2% | -2.243 to -0.5357 | yes: GAIN |
| node-hours | 2.511 | 1.934 | -23.0% | -0.9366 to -0.2177 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.2 | 270.8 | +0.2% | +0.06182 to +1.075 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.2 | 227.1 | -16.0% | -70.11 to -16.12 | yes: GAIN |
| response time (ms), mean | 235.2 | 207.7 | -11.7% | -39.44 to -15.66 | yes: GAIN |
| response time (ms), 95th percentile | 815 | 847.7 | +4.0% | -33.6 to +99.13 | no |
| response time (ms), 99th percentile | 1217 | 1328 | +9.1% | -0.1861 to +222.2 | no |
| time over the response line (% of samples) | 9.997 | 9.714 | -2.8% | -1.309 to +0.7419 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.5 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.9 (native is 0) | +31.96 to +43.84 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.982 | 10.03 | +11.7% | -0.2816 to +2.385 | no |
| utilisation (used / allocatable) | 0.05453 | 0.07188 | +31.8% | +0.006428 to +0.02828 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.309 | 1.297 | -0.9% | -0.03507 to +0.01137 | no |
| Omni's own CPU (cores), mean | 0 | 0.01549 | +0.0155 (native is 0) | +0.01322 to +0.01776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.309 | 1.312 | +0.3% | -0.01992 to +0.0272 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.9 | 417.1 | -17.2% | -143 to -30.63 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.933 | 2.166 | +12.0% | +0.03771 to +0.428 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.4079 to +1.408 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.4079 to +1.408 | no |
| host CPU busy, the real machine under kind (%) | 37.7 | 38.42 | +1.9% | +0.4128 to +1.023 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 745.8 | 749 | +0.4% | +0.2642 to +6.136 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.719 | -38.0% | -3.604 to -0.9576 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 | -18.7% | -0.05704 to +0.03204 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.02 | 59.88 | +5.0% | -0.4376 to +6.154 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*