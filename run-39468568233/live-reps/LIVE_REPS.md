# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.974 |
| node-hours | 2.514 | 2.086 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 239 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 205.9 | 166.6 |
| response time (ms), 95th percentile | 602.6 | 575.1 |
| response time (ms), 99th percentile | 921.9 | 898.8 |
| time over the response line (% of samples) | 5.604 | 5.133 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 4.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.69 | 13.79 |
| utilisation (used / allocatable) | 0.0563 | 0.06779 |
| CPU used (cores), mean | 1.351 | 1.338 |
| Omni's own CPU (cores), mean | 0 | 0.01729 |
| CPU used with Omni's own (cores), mean | 1.351 | 1.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.5 | 429.4 |
| HPA replicas, mean | 1.982 | 2.023 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.2 | 1.2 |
| pod start wait, mean (s) | 0.2 | 0.85 |
| host CPU busy, the real machine under kind (%) | 39.43 | 40.15 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 761.3 | 762.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.259 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.625 | 0.7042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 71.09 | 72.64 |
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
| worker nodes in service, mean | 6 | 4.974 | -17.1% | -1.702 to -0.3508 | yes: GAIN |
| node-hours | 2.514 | 2.086 | -17.0% | -0.7144 to -0.1403 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.2 | +0.1% | -0.5697 to +1.197 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 239 | -11.8% | -53.41 to -10.36 | yes: GAIN |
| response time (ms), mean | 205.9 | 166.6 | -19.1% | -51.6 to -27.1 | yes: GAIN |
| response time (ms), 95th percentile | 602.6 | 575.1 | -4.6% | -66.45 to +11.48 | no |
| response time (ms), 99th percentile | 921.9 | 898.8 | -2.5% | -93.25 to +47.1 | no |
| time over the response line (% of samples) | 5.604 | 5.133 | -8.4% | -1.432 to +0.4899 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.4 | 4.1 | -6.8% | -0.6455 to +0.04553 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 | +39.8 (native is 0) | +20.73 to +58.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.69 | 13.78 | +8.6% | -0.2268 to +2.42 | no |
| utilisation (used / allocatable) | 0.0563 | 0.06779 | +20.4% | +0.003297 to +0.01967 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.351 | 1.338 | -1.0% | -0.03804 to +0.01086 | no |
| Omni's own CPU (cores), mean | 0 | 0.01729 | +0.0173 (native is 0) | +0.01602 to +0.01856 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.351 | 1.355 | +0.3% | -0.02068 to +0.02808 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.5 | 429.4 | -12.3% | -103.9 to -16.19 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.982 | 2.023 | +2.1% | -0.04989 to +0.1331 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 1.2 | +500.0% | -0.5816 to +2.582 | no |
| pod start wait, mean (s) | 0.2 | 0.85 | +325.0% | -0.2105 to +1.511 | no |
| host CPU busy, the real machine under kind (%) | 39.43 | 40.15 | +1.8% | +0.5143 to +0.9259 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 761.3 | 762.8 | +0.2% | -0.502 to +3.502 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.259 | -29.0% | -2.958 to -0.5252 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.625 | 0.7042 | +12.7% | -0.04287 to +0.2012 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.1 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 71.09 | 72.64 | +2.2% | -1.019 to +4.127 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*