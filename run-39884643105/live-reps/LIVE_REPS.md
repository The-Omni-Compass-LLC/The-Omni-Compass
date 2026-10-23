# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.987 |
| node-hours | 2.515 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 128.7 | 98.25 |
| response time (ms), 95th percentile | 219.7 | 215 |
| response time (ms), 99th percentile | 318.1 | 314.6 |
| time over the response line (% of samples) | 0.1999 | 0.1486 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 984.9 | 1076 |
| utilisation (used / allocatable) | 0.05925 | 0.05883 |
| CPU used (cores), mean | 1.422 | 1.409 |
| Omni's own CPU (cores), mean | 0 | 0.04302 |
| CPU used with Omni's own (cores), mean | 1.422 | 1.452 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.8 | 459.9 |
| HPA replicas, mean | 2.033 | 1.976 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 0.4 | 0.6 |
| pod start wait, mean (s) | 0.2 | 0.2667 |
| host CPU busy, the real machine under kind (%) | 43.91 | 45.04 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1404 | 1437 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.8 |
| queue: job wait, submitted to its first pod running, mean (s) | 133.2 | 123.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 716.8 | 637.3 |
| queue: job turnaround, submitted to done, mean (s) | 756.2 | 798.8 |
| queue: jobs unfinished at the window's end | 7.4 | 8.2 |

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
| worker nodes in service, mean | 6 | 5.987 | -0.2% | -0.03185 to +0.006451 | no |
| node-hours | 2.515 | 2.515 | +0.0% | -0.01228 to +0.01295 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.2 | +0.1% | -0.9002 to +1.464 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.8 | -0.0% | -1.437 to +1.201 | no |
| response time (ms), mean | 128.7 | 98.25 | -23.7% | -38.12 to -22.75 | yes: GAIN |
| response time (ms), 95th percentile | 219.7 | 215 | -2.2% | -12.37 to +2.91 | no |
| response time (ms), 99th percentile | 318.1 | 314.6 | -1.1% | -21.49 to +14.41 | no |
| time over the response line (% of samples) | 0.1999 | 0.1486 | -25.7% | -0.1533 to +0.05066 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.6 | +26.6 (native is 0) | +16.74 to +36.46 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 984.9 | 1076 | +9.2% | +32.1 to +149.8 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05925 | 0.05883 | -0.7% | -0.001704 to +0.0008684 | no |
| CPU used (cores), mean | 1.422 | 1.409 | -0.9% | -0.04346 to +0.01774 | no |
| Omni's own CPU (cores), mean | 0 | 0.04302 | +0.043 (native is 0) | +0.0375 to +0.04854 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.422 | 1.452 | +2.1% | -0.001202 to +0.06153 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.8 | 459.9 | +0.7% | -5.765 to +11.94 | no |
| HPA replicas, mean | 2.033 | 1.976 | -2.8% | -0.2806 to +0.166 | no |
| pods started | 0.2 | 0.4 | +100.0% | -0.6793 to +1.079 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | -1.338 to +1.738 | no |
| pod start wait, mean (s) | 0.2 | 0.2667 | +33.3% | -0.5964 to +0.7297 | no |
| host CPU busy, the real machine under kind (%) | 43.91 | 45.04 | +2.6% | +0.5046 to +1.758 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1404 | 1437 | +2.4% | -10.97 to +78.17 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.8 | -3.3% | -0.5674 to +0.1674 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 133.2 | 123.6 | -7.2% | -45.52 to +26.34 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 716.8 | 637.3 | -11.1% | -214.7 to +55.75 | no |
| queue: job turnaround, submitted to done, mean (s) | 756.2 | 798.8 | +5.6% | -6.973 to +92.02 | no |
| queue: jobs unfinished at the window's end | 7.4 | 8.2 | +10.8% | -1.673 to +3.273 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*