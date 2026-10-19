# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 516.6 | 515 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.6 | 515 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 275.2 | 152.5 |
| response time (ms), 95th percentile | 780.7 | 299.3 |
| response time (ms), 99th percentile | 2474 | 1880 |
| time over the response line (% of samples) | 19.69 | 11.4 |
| failed requests (%) | 10.81 | 9.336 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.1 | 20.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4133 | 0.2433 |
| utilisation (used / allocatable) | 0.1012 | 0.09889 |
| CPU used (cores), mean | 2.428 | 2.373 |
| Omni's own CPU (cores), mean | 0 | 0.0086 |
| CPU used with Omni's own (cores), mean | 2.428 | 2.382 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.3 | 311.3 |
| HPA replicas, mean | 9.403 | 9.442 |
| pods started | 5.8 | 4.5 |
| pod start wait, total (s) | 8.4 | 6 |
| pod start wait, mean (s) | 1.474 | 1.371 |
| host CPU busy, the real machine under kind (%) | 68.36 | 67.2 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | no |
| node-hours | 4.515 | 4.513 | -0.0% | -0.01274 to +0.009071 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 516.6 | 515 | -0.3% | -2.742 to -0.5378 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 516.6 | 515 | -0.3% | -2.742 to -0.5378 | yes: GAIN |
| response time (ms), mean | 275.2 | 152.5 | -44.6% | -149.2 to -96.1 | yes: GAIN |
| response time (ms), 95th percentile | 780.7 | 299.3 | -61.7% | -575.6 to -387.1 | yes: GAIN |
| response time (ms), 99th percentile | 2474 | 1880 | -24.0% | -1055 to -131.7 | yes: GAIN |
| time over the response line (% of samples) | 19.69 | 11.4 | -42.1% | -10.82 to -5.742 | yes: GAIN |
| failed requests (%) | 10.81 | 9.336 | -13.7% | -2.41 to -0.5444 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.1 | 20.3 | -25.1% | -8.873 to -4.727 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.1 | +30.1 (native is 0) | +22.47 to +37.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4133 | 0.2433 | -41.1% | -0.5979 to +0.2579 | no |
| utilisation (used / allocatable) | 0.1012 | 0.09889 | -2.3% | -0.002722 to -0.001853 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.428 | 2.373 | -2.3% | -0.06534 to -0.04447 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0086 | +0.0086 (native is 0) | +0.007369 to +0.009831 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.428 | 2.382 | -1.9% | -0.05754 to -0.03507 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.3 | 311.3 | +2.6% | +3.468 to +12.49 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.403 | 9.442 | +0.4% | -0.1715 to +0.2501 | no |
| pods started | 5.8 | 4.5 | -22.4% | -2.314 to -0.2856 | yes: GAIN |
| pod start wait, total (s) | 8.4 | 6 | -28.6% | -4.905 to +0.1053 | no |
| pod start wait, mean (s) | 1.474 | 1.371 | -7.0% | -0.4648 to +0.2581 | no |
| host CPU busy, the real machine under kind (%) | 68.36 | 67.2 | -1.7% | -1.497 to -0.8319 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 21.0 |  |  | 10 |
| compass | 30.0 | +42.9% | +6.7 to +11.3 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*