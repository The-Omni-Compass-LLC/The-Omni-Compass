# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.431 |
| node-hours | 2.515 | 1.855 |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 269 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 219.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 195 | 164.8 |
| response time (ms), 95th percentile | 552.1 | 571.5 |
| response time (ms), 99th percentile | 811.6 | 833.2 |
| time over the response line (% of samples) | 6.041 | 6.327 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 3.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.137 | 7.503 |
| utilisation (used / allocatable) | 0.05074 | 0.07009 |
| CPU used (cores), mean | 1.218 | 1.219 |
| Omni's own CPU (cores), mean | 0 | 0.01543 |
| CPU used with Omni's own (cores), mean | 1.218 | 1.235 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 538.7 | 430.9 |
| HPA replicas, mean | 1.892 | 2.222 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 36.25 | 36.99 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 737.8 | 737.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.33 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 43.66 | 43.59 |
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
| worker nodes in service, mean | 6 | 4.431 | -26.2% | -2.335 to -0.8036 | yes: GAIN |
| node-hours | 2.515 | 1.855 | -26.3% | -0.9848 to -0.3364 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269 | 269 | -0.0% | -1.04 to +1.029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269 | 219.7 | -18.3% | -73.47 to -25.1 | yes: GAIN |
| response time (ms), mean | 195 | 164.8 | -15.5% | -42.89 to -17.64 | yes: GAIN |
| response time (ms), 95th percentile | 552.1 | 571.5 | +3.5% | -18.3 to +57.03 | no |
| response time (ms), 99th percentile | 811.6 | 833.2 | +2.7% | -26.33 to +69.59 | no |
| time over the response line (% of samples) | 6.041 | 6.327 | +4.7% | -0.02604 to +0.598 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.3 | 3.9 | +18.2% | -0.3048 to +1.505 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.5 | +60.5 (native is 0) | +42.63 to +78.37 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.137 | 7.503 | +5.1% | -1.235 to +1.968 | no |
| utilisation (used / allocatable) | 0.05074 | 0.07009 | +38.1% | +0.009186 to +0.0295 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.218 | 1.219 | +0.1% | -0.03183 to +0.03426 | no |
| Omni's own CPU (cores), mean | 0 | 0.01543 | +0.0154 (native is 0) | +0.01384 to +0.01702 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.218 | 1.235 | +1.4% | -0.0166 to +0.04988 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 538.7 | 430.9 | -20.0% | -167.6 to -48.04 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.892 | 2.222 | +17.5% | +0.1281 to +0.5327 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 36.25 | 36.99 | +2.0% | +0.4025 to +1.062 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 737.8 | 737.7 | -0.0% | -2.079 to +1.879 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.33 | -44.5% | -3.915 to -1.425 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.1 | +20.0% | -0.03035 to +0.06369 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.6 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 43.66 | 43.59 | -0.2% | -0.7809 to +0.6392 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*