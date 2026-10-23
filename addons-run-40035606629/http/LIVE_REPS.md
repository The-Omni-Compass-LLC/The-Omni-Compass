# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 206.2 | 87.51 |
| response time (ms), 95th percentile | 478.8 | 133 |
| response time (ms), 99th percentile | 645.6 | 242.6 |
| time over the response line (% of samples) | 4.706 | 0.08522 |
| failed requests (%) | 0.01333 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.08 |
| utilisation (used / allocatable) | 0.03037 | 0.04769 |
| CPU used (cores), mean | 0.7289 | 1.144 |
| Omni's own CPU (cores), mean | 0 | 0.0104 |
| CPU used with Omni's own (cores), mean | 0.7289 | 1.155 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.3 | 567.5 |
| HPA replicas, mean | 2.942 | 2.434 |
| pods started | 3 | 2.5 |
| pod start wait, total (s) | 3.9 | 3.5 |
| pod start wait, mean (s) | 1.292 | 1.425 |
| host CPU busy, the real machine under kind (%) | 23.14 | 35.16 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.024e-17 to +4.455e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.516 | -0.3% | -0.009341 to +0.001675 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.6 | +2.3% | +2.518 to +4.701 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.6 | +2.3% | +2.518 to +4.701 | yes: power given |
| response time (ms), mean | 206.2 | 87.51 | -57.6% | -139.4 to -98.04 | yes: GAIN |
| response time (ms), 95th percentile | 478.8 | 133 | -72.2% | -399.5 to -292.1 | yes: GAIN |
| response time (ms), 99th percentile | 645.6 | 242.6 | -62.4% | -480.9 to -325.3 | yes: GAIN |
| time over the response line (% of samples) | 4.706 | 0.08522 | -98.2% | -6.707 to -2.535 | yes: GAIN |
| failed requests (%) | 0.01333 | 0 | -100.0% | -0.04349 to +0.01683 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0 | -100.0% | -7.148 to -2.652 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.5 | +6.5 (native is 0) | +4.158 to +8.842 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1317 | 0.08 | -39.2% | -0.1707 to +0.06735 | no |
| utilisation (used / allocatable) | 0.03037 | 0.04769 | +57.0% | +0.01425 to +0.02038 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7289 | 1.144 | +57.0% | +0.3421 to +0.4891 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0104 | +0.0104 (native is 0) | +0.008962 to +0.01184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7289 | 1.155 | +58.4% | +0.3512 to +0.5007 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 858.3 | 567.5 | -33.9% | -313.3 to -268.2 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.942 | 2.434 | -17.3% | -0.6815 to -0.3354 | yes: GAIN |
| pods started | 3 | 2.5 | -16.7% | -1.108 to +0.1079 | no |
| pod start wait, total (s) | 3.9 | 3.5 | -10.3% | -1.715 to +0.9146 | no |
| pod start wait, mean (s) | 1.292 | 1.425 | +10.3% | -0.332 to +0.5986 | no |
| host CPU busy, the real machine under kind (%) | 23.14 | 35.16 | +52.0% | +10.11 to +13.94 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*