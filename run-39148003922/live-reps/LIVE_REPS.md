# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.511 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.2 | 521.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.2 | 521.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 303.8 | 172 |
| response time (ms), 95th percentile | 822.3 | 337.7 |
| response time (ms), 99th percentile | 3093 | 2035 |
| time over the response line (% of samples) | 23.65 | 14.84 |
| failed requests (%) | 14.24 | 12.35 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.2 | 26 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.515 | 0.5717 |
| utilisation (used / allocatable) | 0.1102 | 0.1086 |
| CPU used (cores), mean | 2.644 | 2.607 |
| Omni's own CPU (cores), mean | 0 | 0.0091 |
| CPU used with Omni's own (cores), mean | 2.644 | 2.616 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 280.6 | 282.3 |
| HPA replicas, mean | 9.528 | 9.547 |
| pods started | 4.5 | 3.4 |
| pod start wait, total (s) | 14.2 | 10.6 |
| pod start wait, mean (s) | 2.839 | 2.284 |
| host CPU busy, the real machine under kind (%) | 74.34 | 73.63 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.167e-15 to +6.345e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.511 | 4.513 | +0.0% | -0.007426 to +0.01109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.2 | 521.5 | -0.1% | -2.438 to +1.156 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.2 | 521.5 | -0.1% | -2.438 to +1.156 | no |
| response time (ms), mean | 303.8 | 172 | -43.4% | -166.4 to -97.12 | yes: GAIN |
| response time (ms), 95th percentile | 822.3 | 337.7 | -58.9% | -596.1 to -373.1 | yes: GAIN |
| response time (ms), 99th percentile | 3093 | 2035 | -34.2% | -1927 to -189.8 | yes: GAIN |
| time over the response line (% of samples) | 23.65 | 14.84 | -37.2% | -11.64 to -5.973 | yes: GAIN |
| failed requests (%) | 14.24 | 12.35 | -13.3% | -2.65 to -1.123 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.2 | 26 | -16.7% | -6.142 to -4.258 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.1 (native is 0) | +26.41 to +37.79 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.515 | 0.5717 | +11.0% | -0.4881 to +0.6014 | no |
| utilisation (used / allocatable) | 0.1102 | 0.1086 | -1.4% | -0.003054 to -5.396e-07 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.644 | 2.607 | -1.4% | -0.07329 to -1.295e-05 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0091 | +0.0091 (native is 0) | +0.007961 to +0.01024 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.644 | 2.616 | -1.0% | -0.06342 to +0.008324 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 280.6 | 282.3 | +0.6% | -5.186 to +8.535 | no |
| HPA replicas, mean | 9.528 | 9.547 | +0.2% | -0.2982 to +0.3361 | no |
| pods started | 4.5 | 3.4 | -24.4% | -2.137 to -0.06342 | yes: GAIN |
| pod start wait, total (s) | 14.2 | 10.6 | -25.4% | -10.06 to +2.862 | no |
| pod start wait, mean (s) | 2.839 | 2.284 | -19.5% | -1.435 to +0.3267 | no |
| host CPU busy, the real machine under kind (%) | 74.34 | 73.63 | -1.0% | -1.825 to +0.3944 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 18.6 |  |  | 10 |
| compass | 24.6 | +32.3% | +4.0 to +8.0 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*