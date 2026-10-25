# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.783 |
| node-hours | 2.516 | 2.004 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 270.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 232.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 276.2 | 251.5 |
| response time (ms), 95th percentile | 1060 | 1126 |
| response time (ms), 99th percentile | 1611 | 1750 |
| time over the response line (% of samples) | 10.94 | 10.93 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.5 | 13.78 |
| utilisation (used / allocatable) | 0.05442 | 0.06928 |
| CPU used (cores), mean | 1.306 | 1.298 |
| Omni's own CPU (cores), mean | 0 | 0.01649 |
| CPU used with Omni's own (cores), mean | 1.306 | 1.314 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.1 | 430.5 |
| HPA replicas, mean | 1.921 | 2.242 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.1 | 1 |
| pod start wait, mean (s) | 0.1 | 0.8 |
| host CPU busy, the real machine under kind (%) | 39.46 | 40.48 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 766.3 | 772.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.155 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.75 | 0.8167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 75.35 | 83.58 |
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
| worker nodes in service, mean | 6 | 4.783 | −20.3% | −2.1386 to −0.2947 | yes: GAIN |
| node-hours | 2.516 | 2.004 | −20.3% | −0.8998 to −0.1228 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 270.3 | −0.1% | −1.7144 to +1.0270 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 232.2 | −14.2% | −67.9202 to −8.9671 | yes: GAIN |
| response time (ms), mean | 276.2 | 251.5 | −8.9% | −46.0222 to −3.3820 | yes: GAIN |
| response time (ms), 95th percentile | 1060 | 1126 | +6.2% | −72.0167 to +203.3647 | no |
| response time (ms), 99th percentile | 1611 | 1750 | +8.6% | −82.5423 to +360.3477 | no |
| time over the response line (% of samples) | 10.94 | 10.93 | −0.1% | −1.2752 to +1.2546 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.8 | +37.800 (native is 0) | +30.3449 to +45.2551 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.5 | 13.78 | +2.1% | −1.7494 to +2.3061 | no |
| utilisation (used / allocatable) | 0.05442 | 0.06928 | +27.3% | +0.0038 to +0.0259 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.306 | 1.298 | −0.6% | −0.0502 to +0.0339 | no |
| Omni's own CPU (cores), mean | 0 | 0.01649 | +0.016 (native is 0) | +0.0141 to +0.0189 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.306 | 1.314 | +0.6% | −0.0345 to +0.0512 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.1 | 430.5 | −15.3% | −133.6103 to −21.6282 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.921 | 2.242 | +16.7% | +0.1392 to +0.5032 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0.1 | 1 | +900.0% | −0.0802 to +1.8802 | no |
| pod start wait, mean (s) | 0.1 | 0.8 | +700.0% | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.46 | 40.48 | +2.6% | +0.5418 to +1.5043 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 766.3 | 772.3 | +0.8% | −0.5124 to +12.5124 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.155 | −30.7% | −3.2364 to −0.4526 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.75 | 0.8167 | +8.9% | −0.0519 to +0.1852 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.4 | +7.7% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.35 | 83.58 | +10.9% | +0.7812 to +15.6688 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*