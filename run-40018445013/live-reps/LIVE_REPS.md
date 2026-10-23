# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 515.8 | 514.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.8 | 514.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 270.7 | 154.4 |
| response time (ms), 95th percentile | 730 | 322.5 |
| response time (ms), 99th percentile | 2245 | 1466 |
| time over the response line (% of samples) | 17.59 | 10.92 |
| failed requests (%) | 9.082 | 8.499 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.2 | 21 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 12.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2517 | 0.2983 |
| utilisation (used / allocatable) | 0.1 | 0.09839 |
| CPU used (cores), mean | 2.401 | 2.361 |
| Omni's own CPU (cores), mean | 0 | 0.0084 |
| CPU used with Omni's own (cores), mean | 2.401 | 2.37 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.9 | 313.3 |
| HPA replicas, mean | 9.451 | 9.888 |
| pods started | 5.4 | 7.9 |
| pod start wait, total (s) | 8.3 | 12.9 |
| pod start wait, mean (s) | 1.572 | 1.584 |
| host CPU busy, the real machine under kind (%) | 67.36 | 66.67 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.615e-16 to +4.062e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.513 | -0.0% | -0.008326 to +0.004659 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515.8 | 514.6 | -0.2% | -2.752 to +0.458 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.8 | 514.6 | -0.2% | -2.752 to +0.458 | no |
| response time (ms), mean | 270.7 | 154.4 | -43.0% | -143.3 to -89.19 | yes: GAIN |
| response time (ms), 95th percentile | 730 | 322.5 | -55.8% | -491 to -324.2 | yes: GAIN |
| response time (ms), 99th percentile | 2245 | 1466 | -34.7% | -1331 to -227.2 | yes: GAIN |
| time over the response line (% of samples) | 17.59 | 10.92 | -37.9% | -8.893 to -4.43 | yes: GAIN |
| failed requests (%) | 9.082 | 8.499 | -6.4% | -1.207 to +0.04167 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.2 | 21 | -19.8% | -6.406 to -3.994 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.9 | +38.9 (native is 0) | +28.16 to +49.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2517 | 0.2983 | +18.5% | -0.5052 to +0.5985 | no |
| utilisation (used / allocatable) | 0.1 | 0.09839 | -1.6% | -0.003199 to -5.967e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.401 | 2.361 | -1.6% | -0.07678 to -0.001432 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0084 | +0.0084 (native is 0) | +0.007073 to +0.009727 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.401 | 2.37 | -1.3% | -0.0695 to +0.008095 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.9 | 313.3 | +3.1% | -1.482 to +20.13 | no |
| HPA replicas, mean | 9.451 | 9.888 | +4.6% | -0.2319 to +1.107 | no |
| pods started | 5.4 | 7.9 | +46.3% | +0.1097 to +4.89 | yes: power given |
| pod start wait, total (s) | 8.3 | 12.9 | +55.4% | -1.044 to +10.24 | no |
| pod start wait, mean (s) | 1.572 | 1.584 | +0.7% | -0.3375 to +0.3609 | no |
| host CPU busy, the real machine under kind (%) | 67.36 | 66.67 | -1.0% | -1.81 to +0.4353 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 21.0 |  |  | 10 |
| compass | 28.8 | +37.1% | +5.7 to +9.9 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*