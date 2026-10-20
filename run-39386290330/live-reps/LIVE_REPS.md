# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.926 |
| node-hours | 2.516 | 2.063 |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 270 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 236.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 221.2 | 192.5 |
| response time (ms), 95th percentile | 637.6 | 702.4 |
| response time (ms), 99th percentile | 935 | 1039 |
| time over the response line (% of samples) | 8.859 | 9.687 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.95 | 6.917 |
| utilisation (used / allocatable) | 0.05332 | 0.06513 |
| CPU used (cores), mean | 1.28 | 1.28 |
| Omni's own CPU (cores), mean | 0 | 0.01742 |
| CPU used with Omni's own (cores), mean | 1.28 | 1.297 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516 | 447.2 |
| HPA replicas, mean | 1.959 | 1.953 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 0.3 | 0 |
| pod start wait, mean (s) | 0.3 | 0 |
| host CPU busy, the real machine under kind (%) | 37.9 | 38.87 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 741.2 | 744.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.99 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.15 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 47.49 | 53.35 |
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
| worker nodes in service, mean | 6 | 4.926 | -17.9% | -1.648 to -0.5013 | yes: GAIN |
| node-hours | 2.516 | 2.063 | -18.0% | -0.6911 to -0.2131 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 270 | +0.0% | -0.9804 to +0.9938 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 236.2 | -12.5% | -51.64 to -15.93 | yes: GAIN |
| response time (ms), mean | 221.2 | 192.5 | -13.0% | -42.96 to -14.6 | yes: GAIN |
| response time (ms), 95th percentile | 637.6 | 702.4 | +10.2% | -7.865 to +137.5 | no |
| response time (ms), 99th percentile | 935 | 1039 | +11.2% | -1.393 to +210 | no |
| time over the response line (% of samples) | 8.859 | 9.687 | +9.3% | -1.628 to +3.284 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 7.3 | +21.7% | +0.08188 to +2.518 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51 | +51 (native is 0) | +38.28 to +63.72 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.95 | 6.917 | -13.0% | -2.381 to +0.314 | no |
| utilisation (used / allocatable) | 0.05332 | 0.06513 | +22.2% | +0.005441 to +0.01819 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.28 | 1.28 | +0.0% | -0.03727 to +0.03813 | no |
| Omni's own CPU (cores), mean | 0 | 0.01742 | +0.0174 (native is 0) | +0.01574 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.28 | 1.297 | +1.4% | -0.01969 to +0.05539 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516 | 447.2 | -13.3% | -112.2 to -25.48 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.959 | 1.953 | -0.3% | -0.1674 to +0.1545 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | -100.0% | -0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 37.9 | 38.87 | +2.6% | +0.3231 to +1.619 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 741.2 | 744.2 | +0.4% | +0.119 to +5.881 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.99 | -33.5% | -2.996 to -1.025 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.15 | +33.3% | -0.03744 to +0.1124 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.8 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 47.49 | 53.35 | +12.3% | +0.04471 to +11.68 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*