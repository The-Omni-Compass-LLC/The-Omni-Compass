# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.269 |
| node-hours | 2.515 | 2.207 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 270.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 247.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 321.7 | 271.3 |
| response time (ms), 95th percentile | 1082 | 1034 |
| response time (ms), 99th percentile | 1560 | 1457 |
| time over the response line (% of samples) | 16.34 | 15.46 |
| failed requests (%) | 0.01163 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.482 | 8.493 |
| utilisation (used / allocatable) | 0.05666 | 0.06343 |
| CPU used (cores), mean | 1.36 | 1.344 |
| Omni's own CPU (cores), mean | 0 | 0.01617 |
| CPU used with Omni's own (cores), mean | 1.36 | 1.36 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.7 | 453.9 |
| HPA replicas, mean | 2.084 | 2.252 |
| pods started | 0 | 0.7 |
| pod start wait, total (s) | 0 | 2.1 |
| pod start wait, mean (s) | 0 | 1.75 |
| host CPU busy, the real machine under kind (%) | 40.13 | 40.71 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 771.5 | 768.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.656 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 0.1917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 78.35 | 74.97 |
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
| worker nodes in service, mean | 6 | 5.269 | -12.2% | -1.392 to -0.07034 | yes: GAIN |
| node-hours | 2.515 | 2.207 | -12.3% | -0.5868 to -0.03064 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 270.8 | -0.2% | -1.283 to +0.2826 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 247.8 | -8.6% | -44.4 to -2.48 | yes: GAIN |
| response time (ms), mean | 321.7 | 271.3 | -15.7% | -70.96 to -29.74 | yes: GAIN |
| response time (ms), 95th percentile | 1082 | 1034 | -4.4% | -115.7 to +20.69 | no |
| response time (ms), 99th percentile | 1560 | 1457 | -6.6% | -209.1 to +4.16 | no |
| time over the response line (% of samples) | 16.34 | 15.46 | -5.4% | -1.74 to -0.0252 | yes: GAIN |
| failed requests (%) | 0.01163 | 0 | -100.0% | -0.03793 to +0.01467 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 8.3 | -5.7% | -1.469 to +0.4685 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.8 | +42.8 (native is 0) | +22.93 to +62.67 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.482 | 8.493 | +0.1% | -2.409 to +2.432 | no |
| utilisation (used / allocatable) | 0.05666 | 0.06343 | +11.9% | -1.297e-05 to +0.01355 | no |
| CPU used (cores), mean | 1.36 | 1.344 | -1.1% | -0.06002 to +0.02877 | no |
| Omni's own CPU (cores), mean | 0 | 0.01617 | +0.0162 (native is 0) | +0.01531 to +0.01703 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.36 | 1.36 | +0.0% | -0.04353 to +0.04462 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.7 | 453.9 | -8.8% | -87.87 to +0.3779 | no |
| HPA replicas, mean | 2.084 | 2.252 | +8.1% | -0.09452 to +0.4315 | no |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.2172 to +1.183 | yes: power given |
| pod start wait, total (s) | 0 | 2.1 | +2.1 (native is 0) | +0.3658 to +3.834 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.75 | +1.75 (native is 0) | +0.4522 to +3.048 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.13 | 40.71 | +1.5% | +0.2041 to +0.965 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 771.5 | 768.9 | -0.3% | -8.039 to +2.839 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.656 | -22.4% | -2.518 to -0.1707 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2583 | 0.1917 | -25.8% | -0.2553 to +0.1219 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.8 | +33.3% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.35 | 74.97 | -4.3% | -9.016 to +2.241 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*