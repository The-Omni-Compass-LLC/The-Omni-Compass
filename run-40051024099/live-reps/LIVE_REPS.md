# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.659 |
| node-hours | 2.517 | 2.373 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 262.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 339.2 | 305.4 |
| response time (ms), 95th percentile | 1085 | 1150 |
| response time (ms), 99th percentile | 1587 | 1717 |
| time over the response line (% of samples) | 20.23 | 19.93 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 11.18 |
| utilisation (used / allocatable) | 0.06088 | 0.06501 |
| CPU used (cores), mean | 1.461 | 1.469 |
| Omni's own CPU (cores), mean | 0 | 0.016 |
| CPU used with Omni's own (cores), mean | 1.461 | 1.485 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.4 | 427.1 |
| HPA replicas, mean | 2.005 | 2.557 |
| pods started | 0 | 0.9 |
| pod start wait, total (s) | 0 | 2.7 |
| pod start wait, mean (s) | 0 | 2.233 |
| host CPU busy, the real machine under kind (%) | 41.86 | 42.78 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 767.8 | 772.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.337 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.07917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 77.08 | 81.11 |
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
| worker nodes in service, mean | 6 | 5.659 | -5.7% | -0.8113 to +0.1299 | no |
| node-hours | 2.517 | 2.373 | -5.7% | -0.345 to +0.05578 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273 | -0.0% | -0.8322 to +0.6965 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 262.3 | -3.9% | -26.13 to +4.574 | no |
| response time (ms), mean | 339.2 | 305.4 | -10.0% | -49.33 to -18.44 | yes: GAIN |
| response time (ms), 95th percentile | 1085 | 1150 | +6.0% | -30.06 to +160 | no |
| response time (ms), 99th percentile | 1587 | 1717 | +8.2% | -35.57 to +296.5 | no |
| time over the response line (% of samples) | 20.23 | 19.93 | -1.5% | -1.421 to +0.8171 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 10.9 | -0.9% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.3 | +28.3 (native is 0) | +18.56 to +38.04 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 11.18 | +2.7% | -1.464 to +2.044 | no |
| utilisation (used / allocatable) | 0.06088 | 0.06501 | +6.8% | -0.0006638 to +0.00892 | no |
| CPU used (cores), mean | 1.461 | 1.469 | +0.6% | -0.01892 to +0.03523 | no |
| Omni's own CPU (cores), mean | 0 | 0.016 | +0.016 (native is 0) | +0.01521 to +0.01679 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.485 | +1.7% | -0.00324 to +0.05155 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.4 | 427.1 | -5.0% | -47.77 to +3.133 | no |
| HPA replicas, mean | 2.005 | 2.557 | +27.5% | +0.29 to +0.8147 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.7 (native is 0) | +0.8515 to +4.548 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.233 | +2.23 (native is 0) | +0.7335 to +3.733 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.86 | 42.78 | +2.2% | +0.6308 to +1.209 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 767.8 | 772.3 | +0.6% | -0.0771 to +9.077 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.337 | -11.1% | -1.577 to +0.2497 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.07917 | +26.7% | -0.04327 to +0.07661 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | -0.3642 to +0.7642 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.08 | 81.11 | +5.2% | -1.088 to +9.163 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*