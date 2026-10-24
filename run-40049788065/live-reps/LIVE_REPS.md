# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.517 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 150.2 | 112.9 |
| response time (ms), 95th percentile | 255.5 | 247.3 |
| response time (ms), 99th percentile | 363.5 | 371.7 |
| time over the response line (% of samples) | 0.1615 | 0.2899 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1168 | 1194 |
| utilisation (used / allocatable) | 0.0615 | 0.06036 |
| CPU used (cores), mean | 1.476 | 1.449 |
| Omni's own CPU (cores), mean | 0 | 0.01231 |
| CPU used with Omni's own (cores), mean | 1.476 | 1.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.2 | 448.9 |
| HPA replicas, mean | 2.024 | 1.963 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 45.58 | 45.7 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1505 | 1507 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 160.6 | 167.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 720.6 | 778.2 |
| queue: job turnaround, submitted to done, mean (s) | 875.1 | 890 |
| queue: jobs unfinished at the window's end | 12 | 12.4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.586e-16 to +6.033e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.517 | 2.514 | -0.1% | -0.01222 to +0.005886 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.2 | -0.3% | -1.783 to +0.3633 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.2 | -0.3% | -1.783 to +0.3633 | no |
| response time (ms), mean | 150.2 | 112.9 | -24.8% | -39.73 to -34.86 | yes: GAIN |
| response time (ms), 95th percentile | 255.5 | 247.3 | -3.2% | -17.28 to +0.8816 | no |
| response time (ms), 99th percentile | 363.5 | 371.7 | +2.3% | -17.74 to +34.17 | no |
| time over the response line (% of samples) | 0.1615 | 0.2899 | +79.5% | +0.007863 to +0.2488 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 | +11.6 (native is 0) | +9.976 to +13.22 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1168 | 1194 | +2.3% | -38.12 to +90.81 | no |
| utilisation (used / allocatable) | 0.0615 | 0.06036 | -1.9% | -0.00264 to +0.0003624 | no |
| CPU used (cores), mean | 1.476 | 1.449 | -1.9% | -0.06336 to +0.008698 | no |
| Omni's own CPU (cores), mean | 0 | 0.01231 | +0.0123 (native is 0) | +0.01151 to +0.01311 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.476 | 1.461 | -1.0% | -0.05133 to +0.02129 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.2 | 448.9 | +1.7% | -1.945 to +17.37 | no |
| HPA replicas, mean | 2.024 | 1.963 | -3.0% | -0.1453 to +0.02312 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 45.58 | 45.7 | +0.3% | -1.066 to +1.298 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1505 | 1507 | +0.1% | -7.148 to +11.15 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 160.6 | 167.5 | +4.3% | -39.8 to +53.46 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 720.6 | 778.2 | +8.0% | -157.4 to +272.6 | no |
| queue: job turnaround, submitted to done, mean (s) | 875.1 | 890 | +1.7% | -20.82 to +50.62 | no |
| queue: jobs unfinished at the window's end | 12 | 12.4 | +3.3% | -1.359 to +2.159 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*