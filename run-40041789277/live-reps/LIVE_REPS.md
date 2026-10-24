# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.887 |
| node-hours | 2.515 | 2.047 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 235.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 247.2 | 220.2 |
| response time (ms), 95th percentile | 741.2 | 809.6 |
| response time (ms), 99th percentile | 1163 | 1179 |
| time over the response line (% of samples) | 11.67 | 11.24 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.557 | 8.15 |
| utilisation (used / allocatable) | 0.05452 | 0.06857 |
| CPU used (cores), mean | 1.308 | 1.312 |
| Omni's own CPU (cores), mean | 0 | 0.01611 |
| CPU used with Omni's own (cores), mean | 1.308 | 1.328 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.9 | 429.6 |
| HPA replicas, mean | 1.99 | 2.17 |
| pods started | 0.2 | 0.5 |
| pod start wait, total (s) | 0.4 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.65 |
| host CPU busy, the real machine under kind (%) | 38.21 | 39 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 749.3 | 752.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.157 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.1292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 56.77 | 58.75 |
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
| worker nodes in service, mean | 6 | 4.887 | -18.5% | -1.914 to -0.3121 | yes: GAIN |
| node-hours | 2.515 | 2.047 | -18.6% | -0.803 to -0.1323 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 270.6 | +0.1% | -0.4853 to +1.016 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 235.6 | -12.8% | -59.66 to -9.809 | yes: GAIN |
| response time (ms), mean | 247.2 | 220.2 | -10.9% | -40.88 to -13.14 | yes: GAIN |
| response time (ms), 95th percentile | 741.2 | 809.6 | +9.2% | +0.8662 to +135.9 | yes: LOSS |
| response time (ms), 99th percentile | 1163 | 1179 | +1.4% | -111.4 to +143.6 | no |
| time over the response line (% of samples) | 11.67 | 11.24 | -3.7% | -1.2 to +0.3291 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.2 | -4.6% | -0.8889 to +0.2889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.7 | +54.7 (native is 0) | +36.03 to +73.37 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.557 | 8.15 | +7.9% | -0.9585 to +2.145 | no |
| utilisation (used / allocatable) | 0.05452 | 0.06857 | +25.8% | +0.003061 to +0.02505 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.308 | 1.312 | +0.3% | -0.02469 to +0.03167 | no |
| Omni's own CPU (cores), mean | 0 | 0.01611 | +0.0161 (native is 0) | +0.01442 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.308 | 1.328 | +1.5% | -0.00921 to +0.0484 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.9 | 429.6 | -14.7% | -132.1 to -16.46 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.99 | 2.17 | +9.0% | -0.07219 to +0.431 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.4578 to +1.058 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | -1.091 to +2.091 | no |
| pod start wait, mean (s) | 0.2 | 0.65 | +225.0% | -0.4493 to +1.349 | no |
| host CPU busy, the real machine under kind (%) | 38.21 | 39 | +2.1% | +0.1371 to +1.452 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 749.3 | 752.2 | +0.4% | -0.4796 to +6.28 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.157 | -30.7% | -3.066 to -0.6204 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.1292 | -6.1% | -0.05232 to +0.03565 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.7 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 56.77 | 58.75 | +3.5% | -2.103 to +6.07 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*