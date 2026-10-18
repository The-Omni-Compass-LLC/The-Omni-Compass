# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 511.1 | 509.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.1 | 509.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 249.3 | 135.8 |
| response time (ms), 95th percentile | 692.9 | 269.8 |
| response time (ms), 99th percentile | 1933 | 1392 |
| time over the response line (% of samples) | 14.97 | 8.117 |
| failed requests (%) | 7.169 | 6.155 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.2 | 15.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 0.395 |
| utilisation (used / allocatable) | 0.09341 | 0.09066 |
| CPU used (cores), mean | 2.242 | 2.176 |
| Omni's own CPU (cores), mean | 0 | 0.00808 |
| CPU used with Omni's own (cores), mean | 2.242 | 2.184 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 324.8 | 336.6 |
| HPA replicas, mean | 9.422 | 9.468 |
| pods started | 5.2 | 7.1 |
| pod start wait, total (s) | 19.6 | 21.4 |
| pod start wait, mean (s) | 3.249 | 2.814 |
| host CPU busy, the real machine under kind (%) | 63.29 | 61.85 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.247e-16 to +1.391e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.514 | +0.0% | -0.003255 to +0.007588 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 511.1 | 509.5 | -0.3% | -2.038 to -1.138 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.1 | 509.5 | -0.3% | -2.038 to -1.138 | yes: GAIN |
| response time (ms), mean | 249.3 | 135.8 | -45.5% | -141.7 to -85.27 | yes: GAIN |
| response time (ms), 95th percentile | 692.9 | 269.8 | -61.1% | -530.5 to -315.6 | yes: GAIN |
| response time (ms), 99th percentile | 1933 | 1392 | -28.0% | -1110 to +26.54 | no |
| time over the response line (% of samples) | 14.97 | 8.117 | -45.8% | -9.6 to -4.111 | yes: GAIN |
| failed requests (%) | 7.169 | 6.155 | -14.1% | -2.022 to -0.00577 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.2 | 15.9 | -34.3% | -10.02 to -6.579 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 | +39.2 (native is 0) | +30.46 to +47.94 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 0.395 | -18.8% | -0.3285 to +0.1451 | no |
| utilisation (used / allocatable) | 0.09341 | 0.09066 | -2.9% | -0.003584 to -0.001913 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.242 | 2.176 | -2.9% | -0.08601 to -0.04592 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00808 | +0.00808 (native is 0) | +0.00675 to +0.00941 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.242 | 2.184 | -2.6% | -0.07854 to -0.03724 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 324.8 | 336.6 | +3.6% | +3.949 to +19.67 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.422 | 9.468 | +0.5% | -0.4573 to +0.5487 | no |
| pods started | 5.2 | 7.1 | +36.5% | -0.9503 to +4.75 | no |
| pod start wait, total (s) | 19.6 | 21.4 | +9.2% | -7.754 to +11.35 | no |
| pod start wait, mean (s) | 3.249 | 2.814 | -13.4% | -1.285 to +0.4171 | no |
| host CPU busy, the real machine under kind (%) | 63.29 | 61.85 | -2.3% | -2.122 to -0.7574 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 22.8 |  |  | 10 |
| compass | 33.6 | +47.4% | +7.4 to +14.2 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*