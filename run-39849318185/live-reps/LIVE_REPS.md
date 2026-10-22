# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.253 |
| node-hours | 2.511 | 2.202 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 248 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 324.8 | 307.8 |
| response time (ms), 95th percentile | 1094 | 1229 |
| response time (ms), 99th percentile | 1626 | 1800 |
| time over the response line (% of samples) | 18.63 | 18.76 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.813 | 9.658 |
| utilisation (used / allocatable) | 0.05635 | 0.06521 |
| CPU used (cores), mean | 1.352 | 1.375 |
| Omni's own CPU (cores), mean | 0 | 0.0502 |
| CPU used with Omni's own (cores), mean | 1.352 | 1.425 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.2 | 438.5 |
| HPA replicas, mean | 1.989 | 2.781 |
| pods started | 0 | 1.7 |
| pod start wait, total (s) | 0 | 3.7 |
| pod start wait, mean (s) | 0 | 1.46 |
| host CPU busy, the real machine under kind (%) | 40.09 | 42.29 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 770.3 | 779.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.688 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1792 | 0.2375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 78.43 | 86.38 |
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
| worker nodes in service, mean | 6 | 5.253 | -12.5% | -1.473 to -0.021 | yes: GAIN |
| node-hours | 2.511 | 2.202 | -12.3% | -0.6137 to -0.004899 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 271.5 | +0.3% | +0.06967 to +1.775 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 248 | -8.3% | -45.15 to -0.001233 | yes: GAIN |
| response time (ms), mean | 324.8 | 307.8 | -5.2% | -35.15 to +1.154 | no |
| response time (ms), 95th percentile | 1094 | 1229 | +12.4% | +14.17 to +256.4 | yes: LOSS |
| response time (ms), 99th percentile | 1626 | 1800 | +10.8% | +50.3 to +299.3 | yes: LOSS |
| time over the response line (% of samples) | 18.63 | 18.76 | +0.7% | -0.9764 to +1.228 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.4 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.5 | +114 (native is 0) | +68.52 to +158.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.813 | 9.658 | +9.6% | -0.3495 to +2.039 | no |
| utilisation (used / allocatable) | 0.05635 | 0.06521 | +15.7% | +0.000845 to +0.01688 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.352 | 1.375 | +1.7% | -0.007605 to +0.05234 | no |
| Omni's own CPU (cores), mean | 0 | 0.0502 | +0.0502 (native is 0) | +0.04417 to +0.05623 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.352 | 1.425 | +5.4% | +0.0438 to +0.1013 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.2 | 438.5 | -13.7% | -144.1 to +4.679 | no |
| HPA replicas, mean | 1.989 | 2.781 | +39.8% | +0.3607 to +1.224 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +0.5295 to +2.871 | yes: power given |
| pod start wait, total (s) | 0 | 3.7 | +3.7 (native is 0) | +0.7983 to +6.602 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.46 | +1.46 (native is 0) | +0.6998 to +2.22 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.09 | 42.29 | +5.5% | +1.733 to +2.667 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 770.3 | 779.4 | +1.2% | +1.694 to +16.51 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.688 | -21.9% | -2.482 to -0.1413 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1792 | 0.2375 | +32.6% | +0.003557 to +0.1131 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.9 | +12.5% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 78.43 | 86.38 | +10.1% | +1.145 to +14.75 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*