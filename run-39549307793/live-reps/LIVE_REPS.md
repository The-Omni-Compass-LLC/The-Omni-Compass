# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 529.2 | 527.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 529.2 | 527.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 358.4 | 188.2 |
| response time (ms), 95th percentile | 953.2 | 405.3 |
| response time (ms), 99th percentile | 3557 | 1938 |
| time over the response line (% of samples) | 28.06 | 17.39 |
| failed requests (%) | 16.66 | 14.37 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 36.5 | 30.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4683 | 0.3317 |
| utilisation (used / allocatable) | 0.1202 | 0.1183 |
| CPU used (cores), mean | 2.884 | 2.838 |
| Omni's own CPU (cores), mean | 0 | 0.01003 |
| CPU used with Omni's own (cores), mean | 2.884 | 2.848 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 244.8 | 248.2 |
| HPA replicas, mean | 9.603 | 9.87 |
| pods started | 5.2 | 4.6 |
| pod start wait, total (s) | 8.6 | 8 |
| pod start wait, mean (s) | 1.653 | 1.551 |
| host CPU busy, the real machine under kind (%) | 80.69 | 79.68 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.213e-16 to +1.72e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.512 | -0.0% | -0.0106 to +0.009263 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 529.2 | 527.9 | -0.2% | -2.438 to -0.07101 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 529.2 | 527.9 | -0.2% | -2.438 to -0.07101 | yes: GAIN |
| response time (ms), mean | 358.4 | 188.2 | -47.5% | -195.1 to -145.2 | yes: GAIN |
| response time (ms), 95th percentile | 953.2 | 405.3 | -57.5% | -641.3 to -454.6 | yes: GAIN |
| response time (ms), 99th percentile | 3557 | 1938 | -45.5% | -2294 to -944.7 | yes: GAIN |
| time over the response line (% of samples) | 28.06 | 17.39 | -38.0% | -12.97 to -8.354 | yes: GAIN |
| failed requests (%) | 16.66 | 14.37 | -13.7% | -3.219 to -1.353 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 36.5 | 30.7 | -15.9% | -6.742 to -4.858 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36 | +36 (native is 0) | +28.17 to +43.83 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4683 | 0.3317 | -29.2% | -0.7289 to +0.4555 | no |
| utilisation (used / allocatable) | 0.1202 | 0.1183 | -1.6% | -0.002559 to -0.001274 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.884 | 2.838 | -1.6% | -0.06141 to -0.03057 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01003 | +0.01 (native is 0) | +0.009222 to +0.01084 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.884 | 2.848 | -1.2% | -0.05115 to -0.02078 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 244.8 | 248.2 | +1.4% | +2.263 to +4.651 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.603 | 9.87 | +2.8% | +0.06629 to +0.4672 | yes: power given |
| pods started | 5.2 | 4.6 | -11.5% | -2.764 to +1.564 | no |
| pod start wait, total (s) | 8.6 | 8 | -7.0% | -6.071 to +4.871 | no |
| pod start wait, mean (s) | 1.653 | 1.551 | -6.2% | -0.6384 to +0.4346 | no |
| host CPU busy, the real machine under kind (%) | 80.69 | 79.68 | -1.2% | -1.325 to -0.6767 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 12.6 |  |  | 10 |
| compass | 21.6 | +71.4% | +6.7 to +11.3 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*