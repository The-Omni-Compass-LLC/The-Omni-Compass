# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 161.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 161.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 126.6 | 79.74 |
| response time (ms), 95th percentile | 261.5 | 122.8 |
| response time (ms), 99th percentile | 369.8 | 155.4 |
| time over the response line (% of samples) | 0.3082 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.16 |
| utilisation (used / allocatable) | 0.03612 | 0.04629 |
| CPU used (cores), mean | 0.8669 | 1.111 |
| Omni's own CPU (cores), mean | 0 | 0.0125 |
| CPU used with Omni's own (cores), mean | 0.8669 | 1.123 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 727.5 | 583.1 |
| HPA replicas, mean | 8.875 | 8.873 |
| pods started | 4.9 | 4.9 |
| pod start wait, total (s) | 6.4 | 7 |
| pod start wait, mean (s) | 1.302 | 1.437 |
| host CPU busy, the real machine under kind (%) | 27.22 | 34.81 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.624e-16 to +6.953e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.517 | +0.0% | -0.01073 to +0.0114 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 161.1 | +1.5% | +0.8572 to +3.882 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 161.1 | +1.5% | +0.8572 to +3.882 | yes: power given |
| response time (ms), mean | 126.6 | 79.74 | -37.0% | -61.82 to -31.98 | yes: GAIN |
| response time (ms), 95th percentile | 261.5 | 122.8 | -53.1% | -167.4 to -110.2 | yes: GAIN |
| response time (ms), 99th percentile | 369.8 | 155.4 | -58.0% | -252.9 to -176 | yes: GAIN |
| time over the response line (% of samples) | 0.3082 | 0 | -100.0% | -0.5219 to -0.09452 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.1 | +18.1 (native is 0) | +17.12 to +19.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.16 | -45.5% | -0.3916 to +0.1249 | no |
| utilisation (used / allocatable) | 0.03612 | 0.04629 | +28.1% | +0.007365 to +0.01297 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8669 | 1.111 | +28.1% | +0.1768 to +0.3112 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0125 | +0.0125 (native is 0) | +0.01095 to +0.01405 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8669 | 1.123 | +29.6% | +0.1879 to +0.3251 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 727.5 | 583.1 | -19.9% | -169.9 to -119 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.875 | 8.873 | -0.0% | -0.288 to +0.2826 | no |
| pods started | 4.9 | 4.9 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, total (s) | 6.4 | 7 | +9.4% | -1.093 to +2.293 | no |
| pod start wait, mean (s) | 1.302 | 1.437 | +10.4% | -0.1836 to +0.4536 | no |
| host CPU busy, the real machine under kind (%) | 27.22 | 34.81 | +27.9% | +5.652 to +9.534 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*