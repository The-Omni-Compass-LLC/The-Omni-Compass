# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.98 |
| node-hours | 2.51 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 271.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 136.7 | 104 |
| response time (ms), 95th percentile | 237.8 | 230.6 |
| response time (ms), 99th percentile | 343.6 | 358.8 |
| time over the response line (% of samples) | 0.2459 | 0.3203 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1140 | 1176 |
| utilisation (used / allocatable) | 0.05804 | 0.0591 |
| CPU used (cores), mean | 1.393 | 1.414 |
| Omni's own CPU (cores), mean | 0 | 0.01226 |
| CPU used with Omni's own (cores), mean | 1.393 | 1.426 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.2 | 457.9 |
| HPA replicas, mean | 2.062 | 2.033 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 43.9 | 44.54 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1430 | 1447 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.548 |
| queue: job wait, submitted to its first pod running, mean (s) | 161.4 | 148.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 715.6 | 642.4 |
| queue: job turnaround, submitted to done, mean (s) | 844.4 | 863.9 |
| queue: jobs unfinished at the window's end | 11.8 | 12.4 |

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
| worker nodes in service, mean | 6 | 5.98 | -0.3% | -0.06658 to +0.02576 | no |
| node-hours | 2.51 | 2.508 | -0.1% | -0.01845 to +0.01528 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 272 | +0.4% | +0.4169 to +1.796 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 271.3 | +0.2% | -1.14 to +2.066 | no |
| response time (ms), mean | 136.7 | 104 | -24.0% | -39.08 to -26.48 | yes: GAIN |
| response time (ms), 95th percentile | 237.8 | 230.6 | -3.0% | -19.04 to +4.64 | no |
| response time (ms), 99th percentile | 343.6 | 358.8 | +4.4% | -1.065 to +31.54 | no |
| time over the response line (% of samples) | 0.2459 | 0.3203 | +30.2% | -0.1447 to +0.2933 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.3 | +50.0% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.8 | +11.8 (native is 0) | +9.898 to +13.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1140 | 1176 | +3.2% | -33.78 to +106.2 | no |
| utilisation (used / allocatable) | 0.05804 | 0.0591 | +1.8% | +5.063e-05 to +0.002063 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.393 | 1.414 | +1.5% | -0.005815 to +0.04699 | no |
| Omni's own CPU (cores), mean | 0 | 0.01226 | +0.0123 (native is 0) | +0.01139 to +0.01313 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.393 | 1.426 | +2.4% | +0.006495 to +0.0592 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.2 | 457.9 | -1.6% | -14.77 to +0.008085 | no |
| HPA replicas, mean | 2.062 | 2.033 | -1.4% | -0.1947 to +0.1365 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 43.9 | 44.54 | +1.5% | -0.1171 to +1.397 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1430 | 1447 | +1.2% | -44.73 to +78.53 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.548 | -7.5% | -6.2 to +5.296 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 161.4 | 148.3 | -8.2% | -57.78 to +31.41 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 715.6 | 642.4 | -10.2% | -270.6 to +124.2 | no |
| queue: job turnaround, submitted to done, mean (s) | 844.4 | 863.9 | +2.3% | -24.63 to +63.61 | no |
| queue: jobs unfinished at the window's end | 11.8 | 12.4 | +5.1% | -1.401 to +2.601 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*