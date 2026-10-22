# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.062 |
| node-hours | 2.515 | 2.118 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 242.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 241.8 | 228.1 |
| response time (ms), 95th percentile | 750.6 | 879.3 |
| response time (ms), 99th percentile | 1193 | 1325 |
| time over the response line (% of samples) | 8.386 | 8.723 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.86 | 16.63 |
| utilisation (used / allocatable) | 0.05803 | 0.06938 |
| CPU used (cores), mean | 1.393 | 1.404 |
| Omni's own CPU (cores), mean | 0 | 0.04762 |
| CPU used with Omni's own (cores), mean | 1.393 | 1.451 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.7 | 417.6 |
| HPA replicas, mean | 1.969 | 2.471 |
| pods started | 0.2 | 1.2 |
| pod start wait, total (s) | 0.2 | 3 |
| pod start wait, mean (s) | 0.1 | 0.95 |
| host CPU busy, the real machine under kind (%) | 40.47 | 42.78 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 785.2 | 789.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.205 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7417 | 0.725 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 96.81 | 99.14 |
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
| worker nodes in service, mean | 6 | 5.062 | -15.6% | -1.648 to -0.2282 | yes: GAIN |
| node-hours | 2.515 | 2.118 | -15.8% | -0.6923 to -0.1008 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 | -0.1% | -1.12 to +0.844 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 242.1 | -10.9% | -51.67 to -7.511 | yes: GAIN |
| response time (ms), mean | 241.8 | 228.1 | -5.7% | -35.45 to +8.008 | no |
| response time (ms), 95th percentile | 750.6 | 879.3 | +17.1% | -103.1 to +360.5 | no |
| response time (ms), 99th percentile | 1193 | 1325 | +11.1% | +8.393 to +255.6 | yes: LOSS |
| time over the response line (% of samples) | 8.386 | 8.723 | +4.0% | -0.8386 to +1.512 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.8 | +1.5% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.1 | +101 (native is 0) | +69.1 to +133.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.86 | 16.63 | -1.4% | -2.533 to +2.067 | no |
| utilisation (used / allocatable) | 0.05803 | 0.06938 | +19.6% | +0.003333 to +0.01938 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.393 | 1.404 | +0.8% | -0.01519 to +0.03706 | no |
| Omni's own CPU (cores), mean | 0 | 0.04762 | +0.0476 (native is 0) | +0.04053 to +0.05471 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.393 | 1.451 | +4.2% | +0.03151 to +0.0856 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.7 | 417.6 | -13.3% | -110.3 to -17.91 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.471 | +25.5% | -0.003529 to +1.008 | no |
| pods started | 0.2 | 1.2 | +500.0% | -0.3488 to +2.349 | no |
| pod start wait, total (s) | 0.2 | 3 | +1400.0% | -0.5686 to +6.169 | no |
| pod start wait, mean (s) | 0.1 | 0.95 | +850.0% | -0.006379 to +1.706 | no |
| host CPU busy, the real machine under kind (%) | 40.47 | 42.78 | +5.7% | +1.953 to +2.661 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 785.2 | 789.1 | +0.5% | -0.06765 to +7.868 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.205 | -29.9% | -3.152 to -0.4375 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7417 | 0.725 | -2.2% | -0.1648 to +0.1315 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.4 | -12.5% | -0.9388 to +0.5388 | no |
| queue: job turnaround, submitted to done, mean (s) | 96.81 | 99.14 | +2.4% | -0.8917 to +5.55 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*