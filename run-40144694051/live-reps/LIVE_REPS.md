# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.793 |
| node-hours | 2.518 | 2.429 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 270.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 263.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 103.6 | 76.05 |
| response time (ms), 95th percentile | 175.6 | 159.1 |
| response time (ms), 99th percentile | 249.3 | 246.2 |
| time over the response line (% of samples) | 0.1232 | 0.04456 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 700.6 | 732.7 |
| utilisation (used / allocatable) | 0.05459 | 0.05684 |
| CPU used (cores), mean | 1.31 | 1.322 |
| Omni's own CPU (cores), mean | 0 | 0.01102 |
| CPU used with Omni's own (cores), mean | 1.31 | 1.333 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.4 | 481.4 |
| HPA replicas, mean | 2.023 | 1.989 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.2 |
| host CPU busy, the real machine under kind (%) | 39.7 | 40.41 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1259 | 1269 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.173 |
| queue: job wait, submitted to its first pod running, mean (s) | 109.8 | 95.69 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 487.1 | 477.7 |
| queue: job turnaround, submitted to done, mean (s) | 555.1 | 605.9 |
| queue: jobs unfinished at the window's end | 3.9 | 3.9 |

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
| worker nodes in service, mean | 6 | 5.793 | −3.4% | −0.4602 to +0.0470 | no |
| node-hours | 2.518 | 2.429 | −3.5% | −0.1998 to +0.0220 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.3 | 270.3 | +0.0% | −1.2757 to +1.3458 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.3 | 263.9 | −2.4% | −14.9170 to +2.0245 | no |
| response time (ms), mean | 103.6 | 76.05 | −26.6% | −35.4582 to −19.5708 | yes: GAIN |
| response time (ms), 95th percentile | 175.6 | 159.1 | −9.4% | −24.0585 to −8.9805 | yes: GAIN |
| response time (ms), 99th percentile | 249.3 | 246.2 | −1.2% | −15.7267 to +9.4939 | no |
| time over the response line (% of samples) | 0.1232 | 0.04456 | −63.8% | −0.1745 to +0.0171 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.5 | +13.500 (native is 0) | +11.4145 to +15.5855 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 700.6 | 732.7 | +4.6% | −38.5319 to +102.7119 | no |
| utilisation (used / allocatable) | 0.05459 | 0.05684 | +4.1% | +0.0001 to +0.0043 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.31 | 1.322 | +0.9% | −0.0099 to +0.0342 | no |
| Omni's own CPU (cores), mean | 0 | 0.01102 | +0.011 (native is 0) | +0.0101 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.31 | 1.333 | +1.8% | +0.0011 to +0.0452 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.4 | 481.4 | −3.6% | −36.7723 to +0.7862 | no |
| HPA replicas, mean | 2.023 | 1.989 | −1.7% | −0.1476 to +0.0803 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 39.7 | 40.41 | +1.8% | +0.1398 to +1.2727 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1259 | 1269 | +0.8% | −7.8765 to +28.2765 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.173 | −13.8% | −1.7035 to +0.0491 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 109.8 | 95.69 | −12.8% | −46.2920 to +18.1503 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 487.1 | 477.7 | −1.9% | −65.6902 to +46.8902 | no |
| queue: job turnaround, submitted to done, mean (s) | 555.1 | 605.9 | +9.2% | −23.3439 to +124.9356 | no |
| queue: jobs unfinished at the window's end | 3.9 | 3.9 | ±0.0% | −1.2158 to +1.2158 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*