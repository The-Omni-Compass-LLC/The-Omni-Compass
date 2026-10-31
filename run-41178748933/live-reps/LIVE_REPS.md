# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.518 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 515.4 | 514.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.4 | 514.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 284.9 | 147.2 |
| response time (ms), 95th percentile | 773.4 | 302.5 |
| response time (ms), 99th percentile | 3112 | 1397 |
| time over the response line (% of samples) | 18.49 | 11.09 |
| failed requests (%) | 9.592 | 8.86 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.3 | 19.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7117 | 0.5233 |
| utilisation (used / allocatable) | 0.09883 | 0.09797 |
| CPU used (cores), mean | 2.372 | 2.351 |
| Omni's own CPU (cores), mean | 0 | 0.00942 |
| CPU used with Omni's own (cores), mean | 2.372 | 2.361 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.3 | 314 |
| HPA replicas, mean | 9.413 | 9.411 |
| pods started | 5.5 | 7.5 |
| pod start wait, total (s) | 9 | 12.1 |
| pod start wait, mean (s) | 1.595 | 1.594 |
| host CPU busy, the real machine under kind (%) | 66.76 | 66.59 |
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
| node-hours | 4.518 | 4.514 | −0.1% | −0.0110 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515.4 | 514.5 | −0.2% | −1.4725 to −0.3033 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.4 | 514.5 | −0.2% | −1.4725 to −0.3033 | yes: GAIN |
| response time (ms), mean | 284.9 | 147.2 | −48.4% | −183.7341 to −91.8137 | yes: GAIN |
| response time (ms), 95th percentile | 773.4 | 302.5 | −60.9% | −595.8602 to −345.8358 | yes: GAIN |
| response time (ms), 99th percentile | 3112 | 1397 | −55.1% | −2937.9575 to −492.1339 | yes: GAIN |
| time over the response line (% of samples) | 18.49 | 11.09 | −40.0% | −10.3567 to −4.4417 | yes: GAIN |
| failed requests (%) | 9.592 | 8.86 | −7.6% | −1.5197 to +0.0552 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.3 | 19.4 | −26.2% | −8.7910 to −5.0090 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.9 | +37.900 (native is 0) | +28.5952 to +47.2048 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7117 | 0.5233 | −26.5% | −0.7112 to +0.3345 | no |
| utilisation (used / allocatable) | 0.09883 | 0.09797 | −0.9% | −0.0020 to +0.0002 | no |
| CPU used (cores), mean | 2.372 | 2.351 | −0.9% | −0.0469 to +0.0054 | no |
| Omni's own CPU (cores), mean | 0 | 0.00942 | +0.009 (native is 0) | +0.0080 to +0.0109 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.372 | 2.361 | −0.5% | −0.0370 to +0.0143 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.3 | 314 | +0.6% | −0.9612 to +4.5569 | no |
| HPA replicas, mean | 9.413 | 9.411 | −0.0% | −0.7480 to +0.7435 | no |
| pods started | 5.5 | 7.5 | +36.4% | +0.3481 to +3.6519 | yes: power given |
| pod start wait, total (s) | 9 | 12.1 | +34.4% | −0.4277 to +6.6277 | no |
| pod start wait, mean (s) | 1.595 | 1.594 | −0.0% | −0.2848 to +0.2834 | no |
| host CPU busy, the real machine under kind (%) | 66.76 | 66.59 | −0.3% | −0.8919 to +0.5426 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 22.2 |  |  | 10 |
| compass | 31.8 | +43.2% | +6.6 to +12.6 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*