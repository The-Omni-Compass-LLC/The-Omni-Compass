# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.5 | 516.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.5 | 516.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 273.4 | 161.5 |
| response time (ms), 95th percentile | 712 | 310.7 |
| response time (ms), 99th percentile | 2231 | 1704 |
| time over the response line (% of samples) | 18.67 | 11.62 |
| failed requests (%) | 10.7 | 9.112 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.9 | 21.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1617 | 0.4317 |
| utilisation (used / allocatable) | 0.1024 | 0.1004 |
| CPU used (cores), mean | 2.458 | 2.409 |
| Omni's own CPU (cores), mean | 0 | 0.00929 |
| CPU used with Omni's own (cores), mean | 2.458 | 2.418 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298 | 303.4 |
| HPA replicas, mean | 9.587 | 9.867 |
| pods started | 5.4 | 6 |
| pod start wait, total (s) | 8.8 | 9.3 |
| pod start wait, mean (s) | 1.636 | 1.57 |
| host CPU busy, the real machine under kind (%) | 69.2 | 68.07 |
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
| node-hours | 4.515 | 4.515 | −0.0% | −0.0052 to +0.0035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.5 | 516.1 | −0.3% | −2.0262 to −0.7782 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.5 | 516.1 | −0.3% | −2.0262 to −0.7782 | yes: GAIN |
| response time (ms), mean | 273.4 | 161.5 | −40.9% | −135.1990 to −88.5946 | yes: GAIN |
| response time (ms), 95th percentile | 712 | 310.7 | −56.4% | −462.2397 to −340.4483 | yes: GAIN |
| response time (ms), 99th percentile | 2231 | 1704 | −23.6% | −1493.4546 to +440.8932 | no |
| time over the response line (% of samples) | 18.67 | 11.62 | −37.7% | −8.9963 to −5.0904 | yes: GAIN |
| failed requests (%) | 10.7 | 9.112 | −14.9% | −2.5160 to −0.6649 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.9 | 21.1 | −27.0% | −9.8456 to −5.7544 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 | +39.800 (native is 0) | +30.4565 to +49.1435 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1617 | 0.4317 | +167.0% | −0.0583 to +0.5983 | no |
| utilisation (used / allocatable) | 0.1024 | 0.1004 | −2.0% | −0.0026 to −0.0015 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.458 | 2.409 | −2.0% | −0.0630 to −0.0358 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00929 | +0.009 (native is 0) | +0.0084 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.418 | −1.6% | −0.0532 to −0.0269 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298 | 303.4 | +1.8% | +3.5658 to +7.4054 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.587 | 9.867 | +2.9% | −0.1857 to +0.7471 | no |
| pods started | 5.4 | 6 | +11.1% | −1.9945 to +3.1945 | no |
| pod start wait, total (s) | 8.8 | 9.3 | +5.7% | −4.0146 to +5.0146 | no |
| pod start wait, mean (s) | 1.636 | 1.57 | −4.1% | −0.4896 to +0.3566 | no |
| host CPU busy, the real machine under kind (%) | 69.2 | 68.07 | −1.6% | −1.4349 to −0.8153 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*