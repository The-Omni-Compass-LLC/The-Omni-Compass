# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.03 |
| node-hours | 2.517 | 2.107 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 240.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 241.6 | 210.2 |
| response time (ms), 95th percentile | 734.5 | 759.4 |
| response time (ms), 99th percentile | 1100 | 1114 |
| time over the response line (% of samples) | 10.3 | 9.756 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.103 | 7.937 |
| utilisation (used / allocatable) | 0.05603 | 0.06913 |
| CPU used (cores), mean | 1.345 | 1.35 |
| Omni's own CPU (cores), mean | 0 | 0.01627 |
| CPU used with Omni's own (cores), mean | 1.345 | 1.366 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.4 | 426.4 |
| HPA replicas, mean | 1.858 | 2.119 |
| pods started | 0.3 | 0.4 |
| pod start wait, total (s) | 0.5 | 1 |
| pod start wait, mean (s) | 0.5 | 1 |
| host CPU busy, the real machine under kind (%) | 39.43 | 40.14 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 750.5 | 752.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.349 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1417 | 0.1417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 57.46 | 57.52 |
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
| worker nodes in service, mean | 6 | 5.03 | -16.2% | -1.794 to -0.1447 | yes: GAIN |
| node-hours | 2.517 | 2.107 | -16.3% | -0.7539 to -0.06489 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.2 | -0.0% | -0.5406 to +0.4904 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 240.7 | -11.2% | -56.47 to -4.495 | yes: GAIN |
| response time (ms), mean | 241.6 | 210.2 | -13.0% | -40.53 to -22.27 | yes: GAIN |
| response time (ms), 95th percentile | 734.5 | 759.4 | +3.4% | -22.61 to +72.42 | no |
| response time (ms), 99th percentile | 1100 | 1114 | +1.3% | -32.18 to +61.22 | no |
| time over the response line (% of samples) | 10.3 | 9.756 | -5.3% | -1.603 to +0.5152 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.1 | -1.4% | -0.9564 to +0.7564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 | +43.6 (native is 0) | +21.74 to +65.46 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.103 | 7.937 | -2.1% | -1.658 to +1.324 | no |
| utilisation (used / allocatable) | 0.05603 | 0.06913 | +23.4% | +0.002523 to +0.02367 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.345 | 1.35 | +0.4% | -0.02989 to +0.04033 | no |
| Omni's own CPU (cores), mean | 0 | 0.01627 | +0.0163 (native is 0) | +0.01507 to +0.01747 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.345 | 1.366 | +1.6% | -0.01311 to +0.05609 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.4 | 426.4 | -12.7% | -108.2 to -15.79 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.858 | 2.119 | +14.0% | +0.0426 to +0.4794 | yes: power given |
| pods started | 0.3 | 0.4 | +33.3% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 0.5 | 1 | +100.0% | -0.1952 to +1.195 | no |
| pod start wait, mean (s) | 0.5 | 1 | +100.0% | -0.1952 to +1.195 | no |
| host CPU busy, the real machine under kind (%) | 39.43 | 40.14 | +1.8% | +0.4777 to +0.9478 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.5 | 752.3 | +0.2% | -0.5796 to +4.18 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.349 | -27.5% | -3.012 to -0.29 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1417 | 0.1417 | +0.0% | -0.03974 to +0.03974 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.46 | 57.52 | +0.1% | -1.332 to +1.465 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*