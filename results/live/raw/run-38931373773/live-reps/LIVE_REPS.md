# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 522 | 521.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522 | 521.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 305 | 183.7 |
| response time (ms), 95th percentile | 801.4 | 355.5 |
| response time (ms), 99th percentile | 2810 | 2293 |
| time over the response line (% of samples) | 22.92 | 14.53 |
| failed requests (%) | 13.07 | 11.68 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.6 | 25.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.5433 |
| utilisation (used / allocatable) | 0.1097 | 0.1084 |
| CPU used (cores), mean | 2.633 | 2.602 |
| Omni's own CPU (cores), mean | 0 | 0.00923 |
| CPU used with Omni's own (cores), mean | 2.633 | 2.611 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 276.1 | 280.3 |
| HPA replicas, mean | 9.565 | 10.03 |
| pods started | 4.5 | 6 |
| pod start wait, total (s) | 14.9 | 15.8 |
| pod start wait, mean (s) | 2.856 | 2.429 |
| host CPU busy, the real machine under kind (%) | 73.85 | 73.39 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.051e-15 to -1.929e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.512 | +0.0% | -0.004715 to +0.005048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522 | 521.4 | -0.1% | -1.761 to +0.4472 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522 | 521.4 | -0.1% | -1.761 to +0.4472 | no |
| response time (ms), mean | 305 | 183.7 | -39.8% | -157.8 to -84.8 | yes: GAIN |
| response time (ms), 95th percentile | 801.4 | 355.5 | -55.6% | -534.7 to -357 | yes: GAIN |
| response time (ms), 99th percentile | 2810 | 2293 | -18.4% | -1783 to +749.1 | no |
| time over the response line (% of samples) | 22.92 | 14.53 | -36.6% | -11.14 to -5.637 | yes: GAIN |
| failed requests (%) | 13.07 | 11.68 | -10.6% | -2.361 to -0.4049 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.6 | 25.3 | -19.9% | -7.988 to -4.612 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.3 | +36.3 (native is 0) | +29.55 to +43.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.5433 | +84.2% | -0.2649 to +0.7616 | no |
| utilisation (used / allocatable) | 0.1097 | 0.1084 | -1.2% | -0.002506 to -3.263e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.633 | 2.602 | -1.2% | -0.06013 to -0.0007832 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00923 | +0.00923 (native is 0) | +0.008185 to +0.01028 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.633 | 2.611 | -0.8% | -0.05125 to +0.008793 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 276.1 | 280.3 | +1.5% | +0.04079 to +8.313 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.565 | 10.03 | +4.9% | -0.153 to +1.082 | no |
| pods started | 4.5 | 6 | +33.3% | -0.8664 to +3.866 | no |
| pod start wait, total (s) | 14.9 | 15.8 | +6.0% | -7.287 to +9.087 | no |
| pod start wait, mean (s) | 2.856 | 2.429 | -14.9% | -1.334 to +0.4813 | no |
| host CPU busy, the real machine under kind (%) | 73.85 | 73.39 | -0.6% | -1.312 to +0.3921 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.8 |  |  | 10 |
| compass | 27.0 | +60.7% | +7.3 to +13.1 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*