# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.152 |
| node-hours | 2.519 | 2.162 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 244.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 261.3 | 237.1 |
| response time (ms), 95th percentile | 791.9 | 875.4 |
| response time (ms), 99th percentile | 1197 | 1286 |
| time over the response line (% of samples) | 13.59 | 13.46 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.655 | 10.57 |
| utilisation (used / allocatable) | 0.05655 | 0.06656 |
| CPU used (cores), mean | 1.357 | 1.344 |
| Omni's own CPU (cores), mean | 0 | 0.01512 |
| CPU used with Omni's own (cores), mean | 1.357 | 1.359 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.2 | 435 |
| HPA replicas, mean | 1.952 | 2.35 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.7 |
| pod start wait, mean (s) | 0 | 0.7 |
| host CPU busy, the real machine under kind (%) | 38.88 | 39.73 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 750.8 | 752.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.592 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 57.22 | 59.87 |
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
| worker nodes in service, mean | 6 | 5.152 | −14.1% | −1.6690 to −0.0274 | yes: GAIN |
| node-hours | 2.519 | 2.162 | −14.2% | −0.7007 to −0.0132 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.5 | −0.1% | −0.9601 to +0.6568 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 244.8 | −9.9% | −52.8018 to −0.8932 | yes: GAIN |
| response time (ms), mean | 261.3 | 237.1 | −9.3% | −35.6006 to −12.8473 | yes: GAIN |
| response time (ms), 95th percentile | 791.9 | 875.4 | +10.5% | +11.7684 to +155.2936 | yes: LOSS |
| response time (ms), 99th percentile | 1197 | 1286 | +7.4% | −17.0087 to +195.2567 | no |
| time over the response line (% of samples) | 13.59 | 13.46 | −1.0% | −1.1929 to +0.9332 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.3 | +2.5% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42 | +42.000 (native is 0) | +26.1804 to +57.8196 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.655 | 10.57 | +9.5% | −0.3583 to +2.1883 | no |
| utilisation (used / allocatable) | 0.05655 | 0.06656 | +17.7% | +0.0003 to +0.0197 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.357 | 1.344 | −1.0% | −0.0442 to +0.0176 | no |
| Omni's own CPU (cores), mean | 0 | 0.01512 | +0.015 (native is 0) | +0.0136 to +0.0166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.357 | 1.359 | +0.1% | −0.0299 to +0.0335 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.2 | 435 | −10.3% | −97.4526 to −2.9306 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.35 | +20.4% | +0.2198 to +0.5763 | yes: power given |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| host CPU busy, the real machine under kind (%) | 38.88 | 39.73 | +2.2% | +0.4480 to +1.2395 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 750.8 | 752.7 | +0.3% | −1.6438 to +5.4438 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.592 | −23.5% | −2.7145 to −0.1022 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0625 | −11.8% | −0.0709 to +0.0542 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | −20.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 57.22 | 59.87 | +4.6% | −1.7448 to +7.0448 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*