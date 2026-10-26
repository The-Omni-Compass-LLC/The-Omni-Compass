# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.1 | 515.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.1 | 515.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 279.7 | 153.6 |
| response time (ms), 95th percentile | 747.8 | 308 |
| response time (ms), 99th percentile | 2488 | 1624 |
| time over the response line (% of samples) | 19.31 | 12.59 |
| failed requests (%) | 11.57 | 10.16 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 21.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3217 | 0.3167 |
| utilisation (used / allocatable) | 0.1019 | 0.09971 |
| CPU used (cores), mean | 2.445 | 2.393 |
| Omni's own CPU (cores), mean | 0 | 0.00874 |
| CPU used with Omni's own (cores), mean | 2.445 | 2.402 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 310.5 | 317.8 |
| HPA replicas, mean | 9.571 | 9.584 |
| pods started | 5.1 | 4.6 |
| pod start wait, total (s) | 7.7 | 6.4 |
| pod start wait, mean (s) | 1.523 | 1.372 |
| host CPU busy, the real machine under kind (%) | 68.78 | 67.8 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.514 | +0.0% | −0.0065 to +0.0072 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.1 | 515.7 | −0.3% | −2.1871 to −0.5609 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.1 | 515.7 | −0.3% | −2.1871 to −0.5609 | yes: GAIN |
| response time (ms), mean | 279.7 | 153.6 | −45.1% | −166.4181 to −85.8902 | yes: GAIN |
| response time (ms), 95th percentile | 747.8 | 308 | −58.8% | −568.6169 to −311.0471 | yes: GAIN |
| response time (ms), 99th percentile | 2488 | 1624 | −34.7% | −1662.9086 to −64.7564 | yes: GAIN |
| time over the response line (% of samples) | 19.31 | 12.59 | −34.8% | −9.2632 to −4.1629 | yes: GAIN |
| failed requests (%) | 11.57 | 10.16 | −12.2% | −2.2223 to −0.5924 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 21.8 | −22.4% | −7.4209 to −5.1791 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.200 (native is 0) | +26.8835 to +41.5165 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3217 | 0.3167 | −1.6% | −0.2722 to +0.2622 | no |
| utilisation (used / allocatable) | 0.1019 | 0.09971 | −2.1% | −0.0032 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.445 | 2.393 | −2.1% | −0.0763 to −0.0285 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00874 | +0.009 (native is 0) | +0.0074 to +0.0100 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.445 | 2.402 | −1.8% | −0.0675 to −0.0198 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 310.5 | 317.8 | +2.3% | −0.8139 to +15.3691 | no |
| HPA replicas, mean | 9.571 | 9.584 | +0.1% | −0.3286 to +0.3547 | no |
| pods started | 5.1 | 4.6 | −9.8% | −2.3546 to +1.3546 | no |
| pod start wait, total (s) | 7.7 | 6.4 | −16.9% | −4.6047 to +2.0047 | no |
| pod start wait, mean (s) | 1.523 | 1.372 | −9.9% | −0.4429 to +0.1398 | no |
| host CPU busy, the real machine under kind (%) | 68.78 | 67.8 | −1.4% | −1.6568 to −0.3051 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*