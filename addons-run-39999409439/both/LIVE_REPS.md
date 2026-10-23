# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 162 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 139.8 | 86.39 |
| response time (ms), 95th percentile | 284.3 | 130.8 |
| response time (ms), 99th percentile | 410.9 | 173.4 |
| time over the response line (% of samples) | 0.487 | 0.0122 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.16 |
| utilisation (used / allocatable) | 0.03671 | 0.04857 |
| CPU used (cores), mean | 0.8812 | 1.166 |
| Omni's own CPU (cores), mean | 0 | 0.01648 |
| CPU used with Omni's own (cores), mean | 0.8812 | 1.182 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.5 | 551.9 |
| HPA replicas, mean | 8.955 | 10.32 |
| pods started | 4.5 | 6.9 |
| pod start wait, total (s) | 5.9 | 9.7 |
| pod start wait, mean (s) | 1.317 | 1.442 |
| host CPU busy, the real machine under kind (%) | 27.27 | 36.12 |
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
| node-hours | 1.517 | 1.52 | +0.2% | -0.005165 to +0.0105 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 162 | +1.9% | +2.328 to +3.699 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 162 | +1.9% | +2.328 to +3.699 | yes: power given |
| response time (ms), mean | 139.8 | 86.39 | -38.2% | -62.03 to -44.77 | yes: GAIN |
| response time (ms), 95th percentile | 284.3 | 130.8 | -54.0% | -165.1 to -142 | yes: GAIN |
| response time (ms), 99th percentile | 410.9 | 173.4 | -57.8% | -269.6 to -205.5 | yes: GAIN |
| time over the response line (% of samples) | 0.487 | 0.0122 | -97.5% | -0.8364 to -0.1132 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | -100.0% | -0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.9 | +33.9 (native is 0) | +22.5 to +45.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.16 | +50.0% | -0.2282 to +0.3348 | no |
| utilisation (used / allocatable) | 0.03671 | 0.04857 | +32.3% | +0.01 to +0.01372 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8812 | 1.166 | +32.3% | +0.24 to +0.3292 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01648 | +0.0165 (native is 0) | +0.01288 to +0.02008 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8812 | 1.182 | +34.2% | +0.2539 to +0.3483 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 714.5 | 551.9 | -22.7% | -178.7 to -146.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.955 | 10.32 | +15.3% | +0.656 to +2.079 | yes: power given |
| pods started | 4.5 | 6.9 | +53.3% | +1.56 to +3.24 | yes: power given |
| pod start wait, total (s) | 5.9 | 9.7 | +64.4% | +2.692 to +4.908 | yes: LOSS |
| pod start wait, mean (s) | 1.317 | 1.442 | +9.5% | -0.1703 to +0.4215 | no |
| host CPU busy, the real machine under kind (%) | 27.27 | 36.12 | +32.4% | +7.436 to +10.25 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*