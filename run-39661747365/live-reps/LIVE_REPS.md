# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.513 | 2.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 148.8 | 109.2 |
| response time (ms), 95th percentile | 265 | 244.5 |
| response time (ms), 99th percentile | 382.5 | 367.9 |
| time over the response line (% of samples) | 0.2934 | 0.2982 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1226 | 1323 |
| utilisation (used / allocatable) | 0.06035 | 0.05924 |
| CPU used (cores), mean | 1.448 | 1.422 |
| Omni's own CPU (cores), mean | 0 | 0.01237 |
| CPU used with Omni's own (cores), mean | 1.448 | 1.434 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.2 | 456.6 |
| HPA replicas, mean | 2.064 | 2.087 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 0.2 | 0 |
| pod start wait, mean (s) | 0.2 | 0 |
| host CPU busy, the real machine under kind (%) | 45.71 | 45.4 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1485 | 1483 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 194.9 | 162.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 870.2 | 711.8 |
| queue: job turnaround, submitted to done, mean (s) | 869.2 | 929.1 |
| queue: jobs unfinished at the window's end | 12.2 | 14.8 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.895e-16 to +2.566e-16 | EVEN, the same (under one part in a million) |
| node-hours | 2.513 | 2.517 | +0.2% | -0.007409 to +0.01574 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.2 | +0.0% | -1.5 to +1.567 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.2 | +0.0% | -1.5 to +1.567 | no |
| response time (ms), mean | 148.8 | 109.2 | -26.6% | -44.89 to -34.41 | yes: GAIN |
| response time (ms), 95th percentile | 265 | 244.5 | -7.7% | -37.98 to -3.042 | yes: GAIN |
| response time (ms), 99th percentile | 382.5 | 367.9 | -3.8% | -41.71 to +12.45 | no |
| time over the response line (% of samples) | 0.2934 | 0.2982 | +1.6% | -0.07949 to +0.08905 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.5 | +400.0% | -0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.3 | +11.3 (native is 0) | +10.34 to +12.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1226 | 1323 | +7.9% | +22.62 to +172 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06035 | 0.05924 | -1.8% | -0.002678 to +0.0004651 | no |
| CPU used (cores), mean | 1.448 | 1.422 | -1.8% | -0.06427 to +0.01116 | no |
| Omni's own CPU (cores), mean | 0 | 0.01237 | +0.0124 (native is 0) | +0.01109 to +0.01365 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.434 | -1.0% | -0.05176 to +0.0234 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.2 | 456.6 | +1.6% | -3.273 to +18.01 | no |
| HPA replicas, mean | 2.064 | 2.087 | +1.1% | -0.1289 to +0.1756 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | -100.0% | -0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 45.71 | 45.4 | -0.7% | -1.532 to +0.8997 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1485 | 1483 | -0.1% | -61.63 to +58.03 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | +0.0% | +0 to +0 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 194.9 | 162.4 | -16.7% | -76.59 to +11.48 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 870.2 | 711.8 | -18.2% | -438.4 to +121.6 | no |
| queue: job turnaround, submitted to done, mean (s) | 869.2 | 929.1 | +6.9% | -7.374 to +127.2 | no |
| queue: jobs unfinished at the window's end | 12.2 | 14.8 | +21.3% | -0.01628 to +5.216 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*