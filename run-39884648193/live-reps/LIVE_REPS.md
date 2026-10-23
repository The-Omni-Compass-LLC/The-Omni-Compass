# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.953 |
| node-hours | 2.516 | 2.497 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 270.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 142.2 | 109.4 |
| response time (ms), 95th percentile | 239.2 | 237.9 |
| response time (ms), 99th percentile | 342 | 354.3 |
| time over the response line (% of samples) | 0.1548 | 0.2318 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1118 | 1180 |
| utilisation (used / allocatable) | 0.05995 | 0.05867 |
| CPU used (cores), mean | 1.439 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0.04569 |
| CPU used with Omni's own (cores), mean | 1.439 | 1.444 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.5 | 461.7 |
| HPA replicas, mean | 2.042 | 2.165 |
| pods started | 0 | 0.9 |
| pod start wait, total (s) | 0 | 2.4 |
| pod start wait, mean (s) | 0 | 0.975 |
| host CPU busy, the real machine under kind (%) | 44.43 | 45.37 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1460 | 1469 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.28 |
| queue: job wait, submitted to its first pod running, mean (s) | 148.5 | 180 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 675.5 | 789.7 |
| queue: job turnaround, submitted to done, mean (s) | 838.8 | 881.2 |
| queue: jobs unfinished at the window's end | 9.6 | 11.1 |

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
| worker nodes in service, mean | 6 | 5.953 | -0.8% | -0.1525 to +0.05899 | no |
| node-hours | 2.516 | 2.497 | -0.8% | -0.06484 to +0.02673 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.8 | -0.2% | -2.003 to +0.7317 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 270.3 | -0.8% | -5.729 to +1.525 | no |
| response time (ms), mean | 142.2 | 109.4 | -23.0% | -39.35 to -26.16 | yes: GAIN |
| response time (ms), 95th percentile | 239.2 | 237.9 | -0.5% | -18.35 to +15.75 | no |
| response time (ms), 99th percentile | 342 | 354.3 | +3.6% | -11.27 to +36.04 | no |
| time over the response line (% of samples) | 0.1548 | 0.2318 | +49.8% | -0.0265 to +0.1806 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.2 | +26.2 (native is 0) | +16.25 to +36.15 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1118 | 1180 | +5.6% | +7.497 to +117.1 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05995 | 0.05867 | -2.1% | -0.002876 to +0.0003219 | no |
| CPU used (cores), mean | 1.439 | 1.398 | -2.8% | -0.07805 to -0.003492 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04569 | +0.0457 (native is 0) | +0.04258 to +0.0488 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.444 | +0.3% | -0.03368 to +0.04352 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.5 | 461.7 | +2.0% | -1.048 to +19.43 | no |
| HPA replicas, mean | 2.042 | 2.165 | +6.0% | -0.0704 to +0.3158 | no |
| pods started | 0 | 0.9 | +0.9 (native is 0) | -0.0802 to +1.88 | no |
| pod start wait, total (s) | 0 | 2.4 | +2.4 (native is 0) | -0.5819 to +5.382 | no |
| pod start wait, mean (s) | 0 | 0.975 | +0.975 (native is 0) | +0.04216 to +1.908 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.43 | 45.37 | +2.1% | -0.09134 to +1.957 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1460 | 1469 | +0.6% | -13.3 to +31.1 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.28 | -28.7% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 148.5 | 180 | +21.2% | +7.1 to +55.97 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 675.5 | 789.7 | +16.9% | -4.003 to +232.4 | no |
| queue: job turnaround, submitted to done, mean (s) | 838.8 | 881.2 | +5.1% | +10.04 to +74.68 | yes: LOSS |
| queue: jobs unfinished at the window's end | 9.6 | 11.1 | +15.6% | -1.425 to +4.425 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*