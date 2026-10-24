# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.983 |
| node-hours | 2.514 | 2.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 141.6 | 104 |
| response time (ms), 95th percentile | 243.7 | 224.3 |
| response time (ms), 99th percentile | 340.9 | 344.4 |
| time over the response line (% of samples) | 0.1616 | 0.2299 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1075 | 1113 |
| utilisation (used / allocatable) | 0.06 | 0.06008 |
| CPU used (cores), mean | 1.44 | 1.438 |
| Omni's own CPU (cores), mean | 0 | 0.0123 |
| CPU used with Omni's own (cores), mean | 1.44 | 1.45 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.2 | 451.6 |
| HPA replicas, mean | 2.079 | 2.063 |
| pods started | 0.2 | 0 |
| pod start wait, total (s) | 0.3 | 0 |
| pod start wait, mean (s) | 0.3 | 0 |
| host CPU busy, the real machine under kind (%) | 44.19 | 45.01 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1425 | 1450 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.706 |
| queue: job wait, submitted to its first pod running, mean (s) | 149.6 | 146.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 789.9 | 721 |
| queue: job turnaround, submitted to done, mean (s) | 802.1 | 836.4 |
| queue: jobs unfinished at the window's end | 10.7 | 10.1 |

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
| worker nodes in service, mean | 6 | 5.983 | -0.3% | -0.0471 to +0.01245 | no |
| node-hours | 2.514 | 2.513 | -0.0% | -0.01465 to +0.01243 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.8 | +0.3% | -0.1601 to +1.894 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272.3 | +0.1% | -1.113 to +1.755 | no |
| response time (ms), mean | 141.6 | 104 | -26.6% | -43.13 to -32.11 | yes: GAIN |
| response time (ms), 95th percentile | 243.7 | 224.3 | -8.0% | -29.14 to -9.716 | yes: GAIN |
| response time (ms), 99th percentile | 340.9 | 344.4 | +1.0% | -19.89 to +26.95 | no |
| time over the response line (% of samples) | 0.1616 | 0.2299 | +42.3% | -0.01833 to +0.1549 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.7 (native is 0) | +9.914 to +13.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1075 | 1113 | +3.6% | -57.58 to +134 | no |
| utilisation (used / allocatable) | 0.06 | 0.06008 | +0.1% | -0.001365 to +0.001527 | no |
| CPU used (cores), mean | 1.44 | 1.438 | -0.1% | -0.03886 to +0.03485 | no |
| Omni's own CPU (cores), mean | 0 | 0.0123 | +0.0123 (native is 0) | +0.01144 to +0.01316 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.44 | 1.45 | +0.7% | -0.02653 to +0.04713 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.2 | 451.6 | +0.1% | -9.989 to +10.77 | no |
| HPA replicas, mean | 2.079 | 2.063 | -0.7% | -0.1637 to +0.1326 | no |
| pods started | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, mean (s) | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| host CPU busy, the real machine under kind (%) | 44.19 | 45.01 | +1.8% | -0.1105 to +1.743 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1425 | 1450 | +1.7% | -22.46 to +71.86 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.706 | -4.9% | -1.084 to +0.4963 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 149.6 | 146.8 | -1.9% | -31.99 to +26.37 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 789.9 | 721 | -8.7% | -232.5 to +94.67 | no |
| queue: job turnaround, submitted to done, mean (s) | 802.1 | 836.4 | +4.3% | -21.61 to +90.38 | no |
| queue: jobs unfinished at the window's end | 10.7 | 10.1 | -5.6% | -1.871 to +0.6707 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*