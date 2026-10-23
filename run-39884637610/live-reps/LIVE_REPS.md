# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.868 |
| node-hours | 2.516 | 2.459 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 267 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 127.4 | 99.28 |
| response time (ms), 95th percentile | 219.7 | 222.3 |
| response time (ms), 99th percentile | 313.5 | 334.6 |
| time over the response line (% of samples) | 0.1831 | 0.1931 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1003 | 1086 |
| utilisation (used / allocatable) | 0.05831 | 0.05858 |
| CPU used (cores), mean | 1.399 | 1.378 |
| Omni's own CPU (cores), mean | 0 | 0.04442 |
| CPU used with Omni's own (cores), mean | 1.399 | 1.423 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.7 | 465.3 |
| HPA replicas, mean | 1.972 | 2.147 |
| pods started | 0.3 | 0.9 |
| pod start wait, total (s) | 0.5 | 1.4 |
| pod start wait, mean (s) | 0.35 | 0.4267 |
| host CPU busy, the real machine under kind (%) | 43.19 | 44.57 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1408 | 1412 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.105 |
| queue: job wait, submitted to its first pod running, mean (s) | 112.4 | 141.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 651.3 | 653.2 |
| queue: job turnaround, submitted to done, mean (s) | 773.6 | 809.9 |
| queue: jobs unfinished at the window's end | 9.8 | 10.2 |

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
| worker nodes in service, mean | 6 | 5.868 | -2.2% | -0.3702 to +0.1053 | no |
| node-hours | 2.516 | 2.459 | -2.3% | -0.1579 to +0.04369 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.1 | -0.2% | -1.194 to +0.2117 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 267 | -1.7% | -12.25 to +2.974 | no |
| response time (ms), mean | 127.4 | 99.28 | -22.1% | -34.11 to -22.15 | yes: GAIN |
| response time (ms), 95th percentile | 219.7 | 222.3 | +1.2% | -7.975 to +13.28 | no |
| response time (ms), 99th percentile | 313.5 | 334.6 | +6.7% | -6.218 to +48.34 | no |
| time over the response line (% of samples) | 0.1831 | 0.1931 | +5.5% | -0.158 to +0.1781 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.1 | +26.1 (native is 0) | +19.92 to +32.28 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1003 | 1086 | +8.3% | -0.2947 to +166.1 | no |
| utilisation (used / allocatable) | 0.05831 | 0.05858 | +0.5% | -0.00189 to +0.002431 | no |
| CPU used (cores), mean | 1.399 | 1.378 | -1.5% | -0.05845 to +0.01619 | no |
| Omni's own CPU (cores), mean | 0 | 0.04442 | +0.0444 (native is 0) | +0.04022 to +0.04862 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.423 | +1.7% | -0.01507 to +0.06165 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.7 | 465.3 | -0.3% | -15.65 to +12.81 | no |
| HPA replicas, mean | 1.972 | 2.147 | +8.8% | -0.05097 to +0.3999 | no |
| pods started | 0.3 | 0.9 | +200.0% | -0.3656 to +1.566 | no |
| pod start wait, total (s) | 0.5 | 1.4 | +180.0% | -0.7329 to +2.533 | no |
| pod start wait, mean (s) | 0.35 | 0.4267 | +21.9% | -0.5862 to +0.7395 | no |
| host CPU busy, the real machine under kind (%) | 43.19 | 44.57 | +3.2% | +0.4261 to +2.341 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1408 | 1412 | +0.3% | -12.43 to +21.03 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.105 | -31.6% | -10.25 to +6.456 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 112.4 | 141.1 | +25.6% | -23.31 to +80.76 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 651.3 | 653.2 | +0.3% | -245.4 to +249.2 | no |
| queue: job turnaround, submitted to done, mean (s) | 773.6 | 809.9 | +4.7% | -34.48 to +107.2 | no |
| queue: jobs unfinished at the window's end | 9.8 | 10.2 | +4.1% | -3.343 to +4.143 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*