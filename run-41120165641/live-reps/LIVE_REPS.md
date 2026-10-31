# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.1 | 516.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.1 | 516.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 313 | 181.6 |
| response time (ms), 95th percentile | 881.3 | 413.2 |
| response time (ms), 99th percentile | 3314 | 2404 |
| time over the response line (% of samples) | 20.14 | 12.1 |
| failed requests (%) | 10.52 | 9.414 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28 | 21 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.58 | 0.6 |
| utilisation (used / allocatable) | 0.1021 | 0.1003 |
| CPU used (cores), mean | 2.45 | 2.406 |
| Omni's own CPU (cores), mean | 0 | 0.00957 |
| CPU used with Omni's own (cores), mean | 2.45 | 2.416 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.2 | 310.7 |
| HPA replicas, mean | 9.433 | 9.417 |
| pods started | 5.3 | 7.2 |
| pod start wait, total (s) | 7.7 | 11.6 |
| pod start wait, mean (s) | 1.446 | 1.576 |
| host CPU busy, the real machine under kind (%) | 68.93 | 68.13 |
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
| node-hours | 4.514 | 4.515 | +0.0% | −0.0057 to +0.0067 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.1 | 516.1 | −0.2% | −2.1295 to +0.0173 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.1 | 516.1 | −0.2% | −2.1295 to +0.0173 | no |
| response time (ms), mean | 313 | 181.6 | −42.0% | −168.0553 to −94.7848 | yes: GAIN |
| response time (ms), 95th percentile | 881.3 | 413.2 | −53.1% | −670.6368 to −265.7342 | yes: GAIN |
| response time (ms), 99th percentile | 3314 | 2404 | −27.5% | −1532.5766 to −286.7752 | yes: GAIN |
| time over the response line (% of samples) | 20.14 | 12.1 | −39.9% | −11.0698 to −5.0122 | yes: GAIN |
| failed requests (%) | 10.52 | 9.414 | −10.6% | −1.9233 to −0.2980 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28 | 21 | −25.0% | −9.2620 to −4.7380 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38 | +38.000 (native is 0) | +27.7168 to +48.2832 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.58 | 0.6 | +3.4% | −0.4816 to +0.5216 | no |
| utilisation (used / allocatable) | 0.1021 | 0.1003 | −1.8% | −0.0030 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.45 | 2.406 | −1.8% | −0.0713 to −0.0150 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00957 | +0.010 (native is 0) | +0.0080 to +0.0111 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.416 | −1.4% | −0.0621 to −0.0050 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.2 | 310.7 | +2.2% | +0.1090 to +12.9903 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.433 | 9.417 | −0.2% | −0.5161 to +0.4842 | no |
| pods started | 5.3 | 7.2 | +35.8% | +0.2327 to +3.5673 | yes: power given |
| pod start wait, total (s) | 7.7 | 11.6 | +50.6% | −0.3446 to +8.1446 | no |
| pod start wait, mean (s) | 1.446 | 1.576 | +9.0% | −0.2136 to +0.4746 | no |
| host CPU busy, the real machine under kind (%) | 68.93 | 68.13 | −1.2% | −1.5540 to −0.0564 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.8 |  |  | 10 |
| compass | 31.2 | +57.6% | +10.0 to +12.8 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*