# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 511.6 | 510.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.6 | 510.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 255.5 | 138.7 |
| response time (ms), 95th percentile | 652.4 | 270.3 |
| response time (ms), 99th percentile | 2851 | 1260 |
| time over the response line (% of samples) | 16.64 | 10.26 |
| failed requests (%) | 9.103 | 8.437 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.9 | 18 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 60 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.425 | 0.5633 |
| utilisation (used / allocatable) | 0.09372 | 0.0915 |
| CPU used (cores), mean | 2.249 | 2.196 |
| Omni's own CPU (cores), mean | 0 | 0.00793 |
| CPU used with Omni's own (cores), mean | 2.249 | 2.204 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 336.6 | 349.7 |
| HPA replicas, mean | 9.351 | 9.485 |
| pods started | 5.6 | 7 |
| pod start wait, total (s) | 8.2 | 11.4 |
| pod start wait, mean (s) | 1.474 | 1.585 |
| host CPU busy, the real machine under kind (%) | 63.44 | 62.47 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.066e-15 to +7.108e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.515 | 4.516 | +0.0% | -0.009119 to +0.01112 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 511.6 | 510.3 | -0.3% | -2.937 to +0.2715 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.6 | 510.3 | -0.3% | -2.937 to +0.2715 | no |
| response time (ms), mean | 255.5 | 138.7 | -45.7% | -159.1 to -74.62 | yes: GAIN |
| response time (ms), 95th percentile | 652.4 | 270.3 | -58.6% | -497.7 to -266.5 | yes: GAIN |
| response time (ms), 99th percentile | 2851 | 1260 | -55.8% | -2752 to -429.8 | yes: GAIN |
| time over the response line (% of samples) | 16.64 | 10.26 | -38.4% | -9.834 to -2.933 | yes: GAIN |
| failed requests (%) | 9.103 | 8.437 | -7.3% | -1.654 to +0.3206 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.9 | 18 | -24.7% | -7.462 to -4.338 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.6 | +30.6 (native is 0) | +22.41 to +38.79 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.425 | 0.5633 | +32.5% | -0.3125 to +0.5892 | no |
| utilisation (used / allocatable) | 0.09372 | 0.0915 | -2.4% | -0.003673 to -0.0007821 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.249 | 2.196 | -2.4% | -0.08815 to -0.01877 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00793 | +0.00793 (native is 0) | +0.006292 to +0.009568 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.249 | 2.204 | -2.0% | -0.0813 to -0.009759 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 336.6 | 349.7 | +3.9% | +1.932 to +24.41 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.351 | 9.485 | +1.4% | -0.505 to +0.7745 | no |
| pods started | 5.6 | 7 | +25.0% | -0.8418 to +3.642 | no |
| pod start wait, total (s) | 8.2 | 11.4 | +39.0% | -1.384 to +7.784 | no |
| pod start wait, mean (s) | 1.474 | 1.585 | +7.5% | -0.1759 to +0.3974 | no |
| host CPU busy, the real machine under kind (%) | 63.44 | 62.47 | -1.5% | -1.955 to +0.02275 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 24.0 |  |  | 10 |
| compass | 33.0 | +37.5% | +6.0 to +12.0 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*