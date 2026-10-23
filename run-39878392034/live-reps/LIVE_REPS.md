# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.147 |
| node-hours | 2.515 | 2.154 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 244.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 349.7 | 325.2 |
| response time (ms), 95th percentile | 1474 | 1525 |
| response time (ms), 99th percentile | 2377 | 2313 |
| time over the response line (% of samples) | 14.07 | 14.24 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.7 | 15.2 |
| utilisation (used / allocatable) | 0.0565 | 0.06733 |
| CPU used (cores), mean | 1.356 | 1.39 |
| Omni's own CPU (cores), mean | 0 | 0.05059 |
| CPU used with Omni's own (cores), mean | 1.356 | 1.44 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.8 | 426.6 |
| HPA replicas, mean | 1.989 | 2.495 |
| pods started | 0.1 | 1.7 |
| pod start wait, total (s) | 0.1 | 3 |
| pod start wait, mean (s) | 0.1 | 1.088 |
| host CPU busy, the real machine under kind (%) | 40.94 | 43.52 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 791.4 | 799.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.302 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8042 | 0.7792 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 101.4 | 108.9 |
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
| worker nodes in service, mean | 6 | 5.147 | -14.2% | -1.45 to -0.2555 | yes: GAIN |
| node-hours | 2.515 | 2.154 | -14.3% | -0.6056 to -0.1151 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.6 | +0.1% | -0.7372 to +1.376 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 244.8 | -9.8% | -44.72 to -8.29 | yes: GAIN |
| response time (ms), mean | 349.7 | 325.2 | -7.0% | -52.51 to +3.352 | no |
| response time (ms), 95th percentile | 1474 | 1525 | +3.4% | -102.5 to +203.5 | no |
| response time (ms), 99th percentile | 2377 | 2313 | -2.7% | -295 to +166.6 | no |
| time over the response line (% of samples) | 14.07 | 14.24 | +1.2% | -0.7514 to +1.085 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 8.7 | +3.6% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.4 | +102 (native is 0) | +81.51 to +123.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.7 | 15.2 | +3.4% | -1.214 to +2.221 | no |
| utilisation (used / allocatable) | 0.0565 | 0.06733 | +19.2% | +0.004334 to +0.01733 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.356 | 1.39 | +2.5% | -0.01049 to +0.07774 | no |
| Omni's own CPU (cores), mean | 0 | 0.05059 | +0.0506 (native is 0) | +0.04139 to +0.05979 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.356 | 1.44 | +6.2% | +0.04348 to +0.1249 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.8 | 426.6 | -14.3% | -124.2 to -18.22 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.989 | 2.495 | +25.4% | +0.1717 to +0.8407 | yes: power given |
| pods started | 0.1 | 1.7 | +1600.0% | +0.2428 to +2.957 | yes: power given |
| pod start wait, total (s) | 0.1 | 3 | +2900.0% | +0.3442 to +5.456 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.088 | +988.3% | +0.2351 to +1.742 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.94 | 43.52 | +6.3% | +1.81 to +3.366 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 791.4 | 799.8 | +1.1% | -3.815 to +20.61 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.302 | -28.3% | -2.851 to -0.5441 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8042 | 0.7792 | -3.1% | -0.09828 to +0.04828 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.6 | +6.7% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.4 | 108.9 | +7.4% | -5.659 to +20.63 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*