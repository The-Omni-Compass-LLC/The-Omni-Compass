# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.512 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 150.5 | 116.2 |
| response time (ms), 95th percentile | 262.8 | 258.9 |
| response time (ms), 99th percentile | 366.9 | 398.1 |
| time over the response line (% of samples) | 0.1619 | 0.4113 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1205 | 1241 |
| utilisation (used / allocatable) | 0.05962 | 0.05976 |
| CPU used (cores), mean | 1.431 | 1.434 |
| Omni's own CPU (cores), mean | 0 | 0.04834 |
| CPU used with Omni's own (cores), mean | 1.431 | 1.482 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454 | 453.3 |
| HPA replicas, mean | 2.011 | 2.128 |
| pods started | 0 | 0.7 |
| pod start wait, total (s) | 0 | 1.3 |
| pod start wait, mean (s) | 0 | 0.475 |
| host CPU busy, the real machine under kind (%) | 44.87 | 46.88 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1484 | 1501 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 178 | 186.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 825.1 | 860.7 |
| queue: job turnaround, submitted to done, mean (s) | 892.1 | 886.7 |
| queue: jobs unfinished at the window's end | 12.9 | 12.2 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.073e-17 to +1.432e-15 | EVEN, the same (under one part in a million) |
| node-hours | 2.512 | 2.514 | +0.1% | -0.005525 to +0.009192 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.1 | +0.1% | -0.8963 to +1.441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.1 | +0.1% | -0.8963 to +1.441 | no |
| response time (ms), mean | 150.5 | 116.2 | -22.8% | -37.82 to -30.7 | yes: GAIN |
| response time (ms), 95th percentile | 262.8 | 258.9 | -1.5% | -13.32 to +5.491 | no |
| response time (ms), 99th percentile | 366.9 | 398.1 | +8.5% | +5.519 to +56.83 | yes: LOSS |
| time over the response line (% of samples) | 0.1619 | 0.4113 | +154.0% | +0.1096 to +0.3892 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 | +37 (native is 0) | +24.9 to +49.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1205 | 1241 | +2.9% | -28 to +98.48 | no |
| utilisation (used / allocatable) | 0.05962 | 0.05976 | +0.2% | -0.001891 to +0.002153 | no |
| CPU used (cores), mean | 1.431 | 1.434 | +0.2% | -0.04539 to +0.05167 | no |
| Omni's own CPU (cores), mean | 0 | 0.04834 | +0.0483 (native is 0) | +0.04488 to +0.0518 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.482 | +3.6% | +0.002439 to +0.1005 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454 | 453.3 | -0.2% | -14.18 to +12.79 | no |
| HPA replicas, mean | 2.011 | 2.128 | +5.8% | -0.08921 to +0.323 | no |
| pods started | 0 | 0.7 | +0.7 (native is 0) | -0.2567 to +1.657 | no |
| pod start wait, total (s) | 0 | 1.3 | +1.3 (native is 0) | -0.7525 to +3.352 | no |
| pod start wait, mean (s) | 0 | 0.475 | +0.475 (native is 0) | -0.1118 to +1.062 | no |
| host CPU busy, the real machine under kind (%) | 44.87 | 46.88 | +4.5% | +0.9052 to +3.111 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1484 | 1501 | +1.1% | -20.01 to +53.41 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 178 | 186.3 | +4.6% | -16.86 to +33.4 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 825.1 | 860.7 | +4.3% | -147.8 to +219 | no |
| queue: job turnaround, submitted to done, mean (s) | 892.1 | 886.7 | -0.6% | -46.67 to +35.92 | no |
| queue: jobs unfinished at the window's end | 12.9 | 12.2 | -5.4% | -3.602 to +2.202 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*