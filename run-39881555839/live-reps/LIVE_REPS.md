# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.102 |
| node-hours | 2.511 | 2.141 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 242.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 234.3 | 211 |
| response time (ms), 95th percentile | 719.8 | 763.3 |
| response time (ms), 99th percentile | 1023 | 1118 |
| time over the response line (% of samples) | 11.33 | 12.28 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.457 | 10.01 |
| utilisation (used / allocatable) | 0.05557 | 0.06451 |
| CPU used (cores), mean | 1.334 | 1.316 |
| Omni's own CPU (cores), mean | 0 | 0.04528 |
| CPU used with Omni's own (cores), mean | 1.334 | 1.362 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.6 | 442.9 |
| HPA replicas, mean | 1.943 | 2.503 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.8 |
| pod start wait, mean (s) | 0 | 0.65 |
| host CPU busy, the real machine under kind (%) | 37.66 | 39.17 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 744.3 | 748.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.291 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 51.67 | 55.2 |
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
| worker nodes in service, mean | 6 | 5.102 | -15.0% | -1.505 to -0.2908 | yes: GAIN |
| node-hours | 2.511 | 2.141 | -14.8% | -0.6248 to -0.1164 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.4 | 271 | +0.2% | -0.1352 to +1.378 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.4 | 242.8 | -10.2% | -46.96 to -8.344 | yes: GAIN |
| response time (ms), mean | 234.3 | 211 | -10.0% | -45.52 to -1.113 | yes: GAIN |
| response time (ms), 95th percentile | 719.8 | 763.3 | +6.0% | -76.43 to +163.4 | no |
| response time (ms), 99th percentile | 1023 | 1118 | +9.3% | -118 to +307.5 | no |
| time over the response line (% of samples) | 11.33 | 12.28 | +8.4% | -1.212 to +3.117 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.9 | +6.2% | -0.2032 to +1.003 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 154.7 | +155 (native is 0) | +99.01 to +210.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.457 | 10.01 | +18.4% | -0.3156 to +3.426 | no |
| utilisation (used / allocatable) | 0.05557 | 0.06451 | +16.1% | +0.003168 to +0.01471 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.334 | 1.316 | -1.3% | -0.05213 to +0.01762 | no |
| Omni's own CPU (cores), mean | 0 | 0.04528 | +0.0453 (native is 0) | +0.03873 to +0.05183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.334 | 1.362 | +2.1% | -0.01161 to +0.06767 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.6 | 442.9 | -10.1% | -82.12 to -17.27 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.943 | 2.503 | +28.8% | +0.1869 to +0.9335 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | -0.1417 to +1.742 | no |
| pod start wait, mean (s) | 0 | 0.65 | +0.65 (native is 0) | -0.1417 to +1.442 | no |
| host CPU busy, the real machine under kind (%) | 37.66 | 39.17 | +4.0% | +0.6107 to +2.4 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 744.3 | 748.2 | +0.5% | -3.961 to +11.76 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.291 | -28.5% | -2.856 to -0.5627 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04583 | +0.0% | -0.03974 to +0.03974 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| queue: job turnaround, submitted to done, mean (s) | 51.67 | 55.2 | +6.8% | -4.023 to +11.1 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*