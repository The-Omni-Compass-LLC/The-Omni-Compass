# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 161.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 162.7 | 85.32 |
| response time (ms), 95th percentile | 335.9 | 130.1 |
| response time (ms), 99th percentile | 483.2 | 166.4 |
| time over the response line (% of samples) | 0.8571 | 0.0122 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.8 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.08167 |
| utilisation (used / allocatable) | 0.03332 | 0.04938 |
| CPU used (cores), mean | 0.7996 | 1.185 |
| Omni's own CPU (cores), mean | 0 | 0.00901 |
| CPU used with Omni's own (cores), mean | 0.7996 | 1.194 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 784.3 | 541.2 |
| HPA replicas, mean | 9.618 | 9.882 |
| pods started | 3.3 | 1 |
| pod start wait, total (s) | 4.6 | 1.2 |
| pod start wait, mean (s) | 1.392 | 0.85 |
| host CPU busy, the real machine under kind (%) | 24.57 | 35.14 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.513 | 1.511 | -0.1% | -0.0122 to +0.008536 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 161.2 | +2.2% | +2.321 to +4.503 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 161.2 | +2.2% | +2.321 to +4.503 | yes: power given |
| response time (ms), mean | 162.7 | 85.32 | -47.6% | -85.29 to -69.49 | yes: GAIN |
| response time (ms), 95th percentile | 335.9 | 130.1 | -61.3% | -223.5 to -188.3 | yes: GAIN |
| response time (ms), 99th percentile | 483.2 | 166.4 | -65.6% | -361.8 to -271.7 | yes: GAIN |
| time over the response line (% of samples) | 0.8571 | 0.0122 | -98.6% | -1.382 to -0.308 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.8 | 0 | -100.0% | -1.679 to +0.07931 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 | +19.8 (native is 0) | +13.43 to +26.17 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.08167 | +58.1% | -0.1105 to +0.1705 | no |
| utilisation (used / allocatable) | 0.03332 | 0.04938 | +48.2% | +0.01472 to +0.0174 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7996 | 1.185 | +48.2% | +0.3533 to +0.4176 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00901 | +0.00901 (native is 0) | +0.007839 to +0.01018 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7996 | 1.194 | +49.3% | +0.3618 to +0.4271 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 784.3 | 541.2 | -31.0% | -263.6 to -222.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.618 | 9.882 | +2.7% | +0.1418 to +0.3859 | yes: power given |
| pods started | 3.3 | 1 | -69.7% | -2.979 to -1.621 | yes: GAIN |
| pod start wait, total (s) | 4.6 | 1.2 | -73.9% | -4.671 to -2.129 | yes: GAIN |
| pod start wait, mean (s) | 1.392 | 0.85 | -38.9% | -1.055 to -0.0287 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 24.57 | 35.14 | +43.0% | +9.871 to +11.27 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*