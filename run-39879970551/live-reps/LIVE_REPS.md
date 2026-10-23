# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.951 |
| node-hours | 2.515 | 2.496 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 270 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 136.9 | 107.4 |
| response time (ms), 95th percentile | 229.3 | 233.2 |
| response time (ms), 99th percentile | 328.8 | 352.5 |
| time over the response line (% of samples) | 0.1616 | 0.2246 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1067 | 1184 |
| utilisation (used / allocatable) | 0.05855 | 0.05832 |
| CPU used (cores), mean | 1.405 | 1.389 |
| Omni's own CPU (cores), mean | 0 | 0.04571 |
| CPU used with Omni's own (cores), mean | 1.405 | 1.434 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.8 | 464.3 |
| HPA replicas, mean | 2.033 | 2.124 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.8 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 43.78 | 44.93 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1430 | 1446 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.857 |
| queue: job wait, submitted to its first pod running, mean (s) | 142.9 | 176.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 640.4 | 721.2 |
| queue: job turnaround, submitted to done, mean (s) | 807.9 | 845.1 |
| queue: jobs unfinished at the window's end | 11 | 12.1 |

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
| worker nodes in service, mean | 6 | 5.951 | -0.8% | -0.1249 to +0.02679 | no |
| node-hours | 2.515 | 2.496 | -0.7% | -0.04787 to +0.01026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.6 | -0.0% | -1.239 to +1.214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 270 | -0.6% | -3.396 to +0.2754 | no |
| response time (ms), mean | 136.9 | 107.4 | -21.6% | -36.37 to -22.73 | yes: GAIN |
| response time (ms), 95th percentile | 229.3 | 233.2 | +1.7% | -4.669 to +12.48 | no |
| response time (ms), 99th percentile | 328.8 | 352.5 | +7.2% | -2.605 to +50.02 | no |
| time over the response line (% of samples) | 0.1616 | 0.2246 | +39.0% | -0.02842 to +0.1544 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.5 | +29.5 (native is 0) | +17.2 to +41.8 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1067 | 1184 | +11.0% | +48.4 to +185.8 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05855 | 0.05832 | -0.4% | -0.002128 to +0.001665 | no |
| CPU used (cores), mean | 1.405 | 1.389 | -1.2% | -0.04987 to +0.0169 | no |
| Omni's own CPU (cores), mean | 0 | 0.04571 | +0.0457 (native is 0) | +0.04123 to +0.05019 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.405 | 1.434 | +2.1% | -0.001561 to +0.06 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.8 | 464.3 | +0.3% | -12.06 to +14.98 | no |
| HPA replicas, mean | 2.033 | 2.124 | +4.5% | -0.08643 to +0.2676 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.8 (native is 0) | -0.2003 to +1.8 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.09105 to +1.291 | no |
| host CPU busy, the real machine under kind (%) | 43.78 | 44.93 | +2.6% | +0.4644 to +1.83 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1430 | 1446 | +1.1% | -11.76 to +42.96 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.857 | -19.0% | -2.958 to +0.6723 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 142.9 | 176.4 | +23.4% | -9.867 to +76.85 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 640.4 | 721.2 | +12.6% | -41.95 to +203.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 807.9 | 845.1 | +4.6% | -13.52 to +88 | no |
| queue: jobs unfinished at the window's end | 11 | 12.1 | +10.0% | -0.9077 to +3.108 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*