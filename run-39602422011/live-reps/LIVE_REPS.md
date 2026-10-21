# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.3 | 173.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.3 | 173.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 583.6 | 510.2 |
| response time (ms), 95th percentile | 2392 | 2418 |
| response time (ms), 99th percentile | 5994 | 5868 |
| time over the response line (% of samples) | 27.23 | 24.81 |
| failed requests (%) | 4.321 | 3.898 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.115 | 1.568 |
| utilisation (used / allocatable) | 0.1022 | 0.102 |
| CPU used (cores), mean | 2.453 | 2.448 |
| Omni's own CPU (cores), mean | 0 | 0.0127 |
| CPU used with Omni's own (cores), mean | 2.453 | 2.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.7 | 286.5 |
| HPA replicas, mean | 15.1 | 15.5 |
| pods started | 5.1 | 3.1 |
| pod start wait, total (s) | 8.8 | 4.5 |
| pod start wait, mean (s) | 1.735 | 1.395 |
| host CPU busy, the real machine under kind (%) | 71.64 | 71.3 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 330.3 | 291.3 |
| second app: response time (ms), 99th percentile | 1241 | 1043 |
| second app: time over the response line (% of samples) | 16.13 | 16.26 |
| second app: failed requests (%) | 14.58 | 14.46 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.451e-16 to +4.675e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.518 | +0.4% | +0.001604 to +0.009396 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 173.3 | 173.9 | +0.3% | +0.06652 to +1.04 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.3 | 173.9 | +0.3% | +0.06652 to +1.04 | yes: power given |
| response time (ms), mean | 583.6 | 510.2 | -12.6% | -107.5 to -39.19 | yes: GAIN |
| response time (ms), 95th percentile | 2392 | 2418 | +1.1% | -263.7 to +314.7 | no |
| response time (ms), 99th percentile | 5994 | 5868 | -2.1% | -938 to +685.4 | no |
| time over the response line (% of samples) | 27.23 | 24.81 | -8.9% | -3.903 to -0.9339 | yes: GAIN |
| failed requests (%) | 4.321 | 3.898 | -9.8% | -1.085 to +0.2392 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9 | -1.1% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.1 (native is 0) | +26.51 to +47.69 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.115 | 1.568 | -25.8% | -1.257 to +0.1635 | no |
| utilisation (used / allocatable) | 0.1022 | 0.102 | -0.2% | -0.001018 to +0.00064 | no |
| CPU used (cores), mean | 2.453 | 2.448 | -0.2% | -0.02442 to +0.01536 | no |
| Omni's own CPU (cores), mean | 0 | 0.0127 | +0.0127 (native is 0) | +0.01194 to +0.01346 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.453 | 2.461 | +0.3% | -0.0113 to +0.02764 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.7 | 286.5 | -0.1% | -3.702 to +3.218 | no |
| HPA replicas, mean | 15.1 | 15.5 | +2.7% | +0.1562 to +0.6461 | yes: power given |
| pods started | 5.1 | 3.1 | -39.2% | -2.826 to -1.174 | yes: GAIN |
| pod start wait, total (s) | 8.8 | 4.5 | -48.9% | -6.148 to -2.452 | yes: GAIN |
| pod start wait, mean (s) | 1.735 | 1.395 | -19.6% | -0.6348 to -0.04522 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 71.64 | 71.3 | -0.5% | -0.7217 to +0.04946 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 330.3 | 291.3 | -11.8% | -229.5 to +151.4 | no |
| second app: response time (ms), 99th percentile | 1241 | 1043 | -16.0% | -1207 to +810.9 | no |
| second app: time over the response line (% of samples) | 16.13 | 16.26 | +0.8% | -1.03 to +1.295 | no |
| second app: failed requests (%) | 14.58 | 14.46 | -0.8% | -0.6699 to +0.4357 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*