# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.2 | 511.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.2 | 511.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 245.6 | 157.2 |
| response time (ms), 95th percentile | 672.9 | 326.3 |
| response time (ms), 99th percentile | 1961 | 2068 |
| time over the response line (% of samples) | 16.77 | 11.44 |
| failed requests (%) | 9.553 | 9.045 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.7 | 18.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.3517 |
| utilisation (used / allocatable) | 0.09473 | 0.09433 |
| CPU used (cores), mean | 2.273 | 2.264 |
| Omni's own CPU (cores), mean | 0 | 0.00817 |
| CPU used with Omni's own (cores), mean | 2.273 | 2.272 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 332.2 | 335.7 |
| HPA replicas, mean | 9.355 | 9.246 |
| pods started | 5.7 | 6.7 |
| pod start wait, total (s) | 8.9 | 10.3 |
| pod start wait, mean (s) | 1.572 | 1.553 |
| host CPU busy, the real machine under kind (%) | 64.14 | 64.4 |
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
| node-hours | 4.514 | 4.512 | −0.0% | −0.0107 to +0.0064 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.2 | 511.9 | −0.1% | −1.3698 to +0.7019 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.2 | 511.9 | −0.1% | −1.3698 to +0.7019 | no |
| response time (ms), mean | 245.6 | 157.2 | −36.0% | −118.8780 to −57.9859 | yes: GAIN |
| response time (ms), 95th percentile | 672.9 | 326.3 | −51.5% | −454.1892 to −238.8368 | yes: GAIN |
| response time (ms), 99th percentile | 1961 | 2068 | +5.5% | −965.0682 to +1179.7704 | no |
| time over the response line (% of samples) | 16.77 | 11.44 | −31.8% | −7.8234 to −2.8532 | yes: GAIN |
| failed requests (%) | 9.553 | 9.045 | −5.3% | −1.1776 to +0.1622 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.7 | 18.9 | −20.3% | −6.8176 to −2.7824 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.9 | +30.900 (native is 0) | +23.7354 to +38.0646 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.3517 | +31.9% | −0.1734 to +0.3434 | no |
| utilisation (used / allocatable) | 0.09473 | 0.09433 | −0.4% | −0.0016 to +0.0008 | no |
| CPU used (cores), mean | 2.273 | 2.264 | −0.4% | −0.0390 to +0.0201 | no |
| Omni's own CPU (cores), mean | 0 | 0.00817 | +0.008 (native is 0) | +0.0067 to +0.0096 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.273 | 2.272 | −0.1% | −0.0314 to +0.0289 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 332.2 | 335.7 | +1.1% | −1.4037 to +8.4974 | no |
| HPA replicas, mean | 9.355 | 9.246 | −1.2% | −1.1699 to +0.9523 | no |
| pods started | 5.7 | 6.7 | +17.5% | −0.5816 to +2.5816 | no |
| pod start wait, total (s) | 8.9 | 10.3 | +15.7% | −1.7488 to +4.5488 | no |
| pod start wait, mean (s) | 1.572 | 1.553 | −1.2% | −0.3017 to +0.2641 | no |
| host CPU busy, the real machine under kind (%) | 64.14 | 64.4 | +0.4% | −0.5403 to +1.0449 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 24.0 |  |  | 10 |
| compass | 31.2 | +30.0% | +5.4 to +9.0 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*