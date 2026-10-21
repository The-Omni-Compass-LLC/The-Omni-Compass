# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.511 | 4.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 519 | 518 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519 | 518 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 295.3 | 164.9 |
| response time (ms), 95th percentile | 757.7 | 329.6 |
| response time (ms), 99th percentile | 2917 | 2181 |
| time over the response line (% of samples) | 19.47 | 11.97 |
| failed requests (%) | 10.51 | 9.166 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 30.5 | 22.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.5767 |
| utilisation (used / allocatable) | 0.1053 | 0.1029 |
| CPU used (cores), mean | 2.528 | 2.47 |
| Omni's own CPU (cores), mean | 0 | 0.00911 |
| CPU used with Omni's own (cores), mean | 2.528 | 2.479 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.8 | 293.1 |
| HPA replicas, mean | 9.641 | 10.52 |
| pods started | 5.3 | 7.2 |
| pod start wait, total (s) | 7.5 | 10.7 |
| pod start wait, mean (s) | 1.427 | 1.551 |
| host CPU busy, the real machine under kind (%) | 70.82 | 69.61 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | no |
| node-hours | 4.511 | 4.515 | +0.1% | -0.00318 to +0.01118 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 519 | 518 | -0.2% | -1.856 to -0.234 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519 | 518 | -0.2% | -1.856 to -0.234 | yes: GAIN |
| response time (ms), mean | 295.3 | 164.9 | -44.1% | -156.8 to -103.8 | yes: GAIN |
| response time (ms), 95th percentile | 757.7 | 329.6 | -56.5% | -508.1 to -348.1 | yes: GAIN |
| response time (ms), 99th percentile | 2917 | 2181 | -25.2% | -1414 to -57.75 | yes: GAIN |
| time over the response line (% of samples) | 19.47 | 11.97 | -38.5% | -9.516 to -5.487 | yes: GAIN |
| failed requests (%) | 10.51 | 9.166 | -12.8% | -1.897 to -0.7889 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 30.5 | 22.8 | -25.2% | -10.62 to -4.779 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.6 | +45.6 (native is 0) | +35.19 to +56.01 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4833 | 0.5767 | +19.3% | -0.4024 to +0.5891 | no |
| utilisation (used / allocatable) | 0.1053 | 0.1029 | -2.3% | -0.003051 to -0.00177 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.528 | 2.47 | -2.3% | -0.07321 to -0.04249 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00911 | +0.00911 (native is 0) | +0.008016 to +0.0102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.528 | 2.479 | -1.9% | -0.06413 to -0.03335 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.8 | 293.1 | +2.2% | +3.965 to +8.575 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.641 | 10.52 | +9.2% | -0.08506 to +1.853 | no |
| pods started | 5.3 | 7.2 | +35.8% | +0.2671 to +3.533 | yes: power given |
| pod start wait, total (s) | 7.5 | 10.7 | +42.7% | +1.39 to +5.01 | yes: LOSS |
| pod start wait, mean (s) | 1.427 | 1.551 | +8.7% | -0.208 to +0.456 | no |
| host CPU busy, the real machine under kind (%) | 70.82 | 69.61 | -1.7% | -1.592 to -0.8253 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*