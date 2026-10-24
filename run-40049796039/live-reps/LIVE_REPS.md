# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.134 |
| node-hours | 2.515 | 2.154 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 244.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 253.5 | 222.1 |
| response time (ms), 95th percentile | 868.3 | 891.6 |
| response time (ms), 99th percentile | 1323 | 1469 |
| time over the response line (% of samples) | 10.65 | 10.54 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.98 | 10.75 |
| utilisation (used / allocatable) | 0.05678 | 0.06759 |
| CPU used (cores), mean | 1.363 | 1.351 |
| Omni's own CPU (cores), mean | 0 | 0.01552 |
| CPU used with Omni's own (cores), mean | 1.363 | 1.366 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.3 | 430 |
| HPA replicas, mean | 1.958 | 2.438 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.2 | 0.7 |
| pod start wait, mean (s) | 0.2 | 0.7 |
| host CPU busy, the real machine under kind (%) | 39.08 | 39.77 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 750.1 | 751.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.638 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 58.79 | 62.14 |
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
| worker nodes in service, mean | 6 | 5.134 | -14.4% | -1.728 to -0.003028 | yes: GAIN |
| node-hours | 2.515 | 2.154 | -14.4% | -0.7241 to +0.0009575 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.5 | +0.0% | -0.7115 to +0.7892 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 244.3 | -10.0% | -54.53 to +0.1444 | no |
| response time (ms), mean | 253.5 | 222.1 | -12.4% | -45.46 to -17.19 | yes: GAIN |
| response time (ms), 95th percentile | 868.3 | 891.6 | +2.7% | -92.16 to +138.7 | no |
| response time (ms), 99th percentile | 1323 | 1469 | +11.0% | -14.63 to +306.2 | no |
| time over the response line (% of samples) | 10.65 | 10.54 | -1.1% | -0.9288 to +0.7012 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.4 | -5.1% | -1.003 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 | +38 (native is 0) | +26.61 to +49.39 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.98 | 10.75 | +7.7% | -0.646 to +2.179 | no |
| utilisation (used / allocatable) | 0.05678 | 0.06759 | +19.1% | -0.0001958 to +0.02183 | no |
| CPU used (cores), mean | 1.363 | 1.351 | -0.9% | -0.03634 to +0.01281 | no |
| Omni's own CPU (cores), mean | 0 | 0.01552 | +0.0155 (native is 0) | +0.01395 to +0.01709 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.366 | +0.3% | -0.02143 to +0.02893 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.3 | 430 | -10.8% | -104.7 to +0.1843 | no |
| HPA replicas, mean | 1.958 | 2.438 | +24.5% | +0.1702 to +0.7901 | yes: power given |
| pods started | 0.1 | 0.4 | +300.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 0.7 | +250.0% | -0.4079 to +1.408 | no |
| pod start wait, mean (s) | 0.2 | 0.7 | +250.0% | -0.4079 to +1.408 | no |
| host CPU busy, the real machine under kind (%) | 39.08 | 39.77 | +1.8% | +0.4783 to +0.9138 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 750.1 | 751.4 | +0.2% | -2.317 to +4.917 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.638 | -22.7% | -2.684 to -0.04102 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05833 | -12.5% | -0.03572 to +0.01906 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | -20.0% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.79 | 62.14 | +5.7% | -0.3427 to +7.043 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*