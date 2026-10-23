# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.982 |
| node-hours | 2.515 | 2.091 |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 270.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 238.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 201.4 | 177.6 |
| response time (ms), 95th percentile | 636.2 | 714.7 |
| response time (ms), 99th percentile | 952.4 | 1059 |
| time over the response line (% of samples) | 7.267 | 6.901 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.833 | 9.45 |
| utilisation (used / allocatable) | 0.05267 | 0.06449 |
| CPU used (cores), mean | 1.264 | 1.268 |
| Omni's own CPU (cores), mean | 0 | 0.04261 |
| CPU used with Omni's own (cores), mean | 1.264 | 1.311 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 522.2 | 449.6 |
| HPA replicas, mean | 2.003 | 2.579 |
| pods started | 0 | 1.7 |
| pod start wait, total (s) | 0 | 4.2 |
| pod start wait, mean (s) | 0 | 1.377 |
| host CPU busy, the real machine under kind (%) | 36.25 | 38.34 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 737.5 | 741.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.195 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 46.46 | 51.66 |
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
| worker nodes in service, mean | 6 | 4.982 | -17.0% | -1.783 to -0.2527 | yes: GAIN |
| node-hours | 2.515 | 2.091 | -16.9% | -0.7435 to -0.1057 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 270.4 | +0.2% | -0.1153 to +1.048 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 238.4 | -11.7% | -55.46 to -7.691 | yes: GAIN |
| response time (ms), mean | 201.4 | 177.6 | -11.8% | -39.98 to -7.636 | yes: GAIN |
| response time (ms), 95th percentile | 636.2 | 714.7 | +12.3% | -48.98 to +205.8 | no |
| response time (ms), 99th percentile | 952.4 | 1059 | +11.2% | -53.96 to +266.6 | no |
| time over the response line (% of samples) | 7.267 | 6.901 | -5.0% | -1.394 to +0.6622 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.3 | +1.9% | -0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.3 | +117 (native is 0) | +85.51 to +149.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.833 | 9.45 | +7.0% | -1.289 to +2.522 | no |
| utilisation (used / allocatable) | 0.05267 | 0.06449 | +22.4% | +0.00299 to +0.02066 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.264 | 1.268 | +0.3% | -0.01835 to +0.02634 | no |
| Omni's own CPU (cores), mean | 0 | 0.04261 | +0.0426 (native is 0) | +0.03627 to +0.04895 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.264 | 1.311 | +3.7% | +0.02209 to +0.07112 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 522.2 | 449.6 | -13.9% | -130.1 to -14.87 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.579 | +28.8% | +0.09843 to +1.054 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +0.4361 to +2.964 | yes: power given |
| pod start wait, total (s) | 0 | 4.2 | +4.2 (native is 0) | +0.7978 to +7.602 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.377 | +1.38 (native is 0) | +0.4345 to +2.319 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.25 | 38.34 | +5.8% | +1.724 to +2.452 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 737.5 | 741.8 | +0.6% | +0.3814 to +8.219 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.195 | -30.1% | -3.082 to -0.5271 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0375 | -25.0% | -0.07051 to +0.04551 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.2 | -33.3% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 46.46 | 51.66 | +11.2% | -0.3902 to +10.79 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*