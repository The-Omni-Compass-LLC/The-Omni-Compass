# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 476.2 | 475.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 476.2 | 475.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 231 | 120.9 |
| response time (ms), 95th percentile | 598.3 | 253.2 |
| response time (ms), 99th percentile | 1067 | 543.6 |
| time over the response line (% of samples) | 10.54 | 2.737 |
| failed requests (%) | 1.026 | 0.9059 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.2 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8167 | 1.333 |
| utilisation (used / allocatable) | 0.07091 | 0.0687 |
| CPU used (cores), mean | 1.702 | 1.649 |
| Omni's own CPU (cores), mean | 0 | 0.00855 |
| CPU used with Omni's own (cores), mean | 1.702 | 1.657 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443 | 454.1 |
| HPA replicas, mean | 9.521 | 10.1 |
| pods started | 7.2 | 14.9 |
| pod start wait, total (s) | 26.5 | 40.2 |
| pod start wait, mean (s) | 3.591 | 2.967 |
| host CPU busy, the real machine under kind (%) | 49.21 | 48.3 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.718e-16 to +8.494e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.338 | +0.1% | -0.001287 to +0.01029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 476.2 | 475.4 | -0.2% | -1.86 to +0.1027 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 476.2 | 475.4 | -0.2% | -1.86 to +0.1027 | no |
| response time (ms), mean | 231 | 120.9 | -47.6% | -161.2 to -58.96 | yes: GAIN |
| response time (ms), 95th percentile | 598.3 | 253.2 | -57.7% | -485.8 to -204.5 | yes: GAIN |
| response time (ms), 99th percentile | 1067 | 543.6 | -49.1% | -757.5 to -290 | yes: GAIN |
| time over the response line (% of samples) | 10.54 | 2.737 | -74.0% | -12.97 to -2.646 | yes: GAIN |
| failed requests (%) | 1.026 | 0.9059 | -11.7% | -0.2382 to -0.001715 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.2 | 7.8 | -57.1% | -16.99 to -3.808 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54 | +54 (native is 0) | +34.58 to +73.42 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8167 | 1.333 | +63.3% | -0.2019 to +1.235 | no |
| utilisation (used / allocatable) | 0.07091 | 0.0687 | -3.1% | -0.003525 to -0.0009025 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.702 | 1.649 | -3.1% | -0.0846 to -0.02166 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00855 | +0.00855 (native is 0) | +0.006503 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.702 | 1.657 | -2.6% | -0.07494 to -0.01422 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443 | 454.1 | +2.5% | -1.931 to +24.12 | no |
| HPA replicas, mean | 9.521 | 10.1 | +6.1% | -0.8811 to +2.033 | no |
| pods started | 7.2 | 14.9 | +106.9% | +2.967 to +12.43 | yes: power given |
| pod start wait, total (s) | 26.5 | 40.2 | +51.7% | +4.312 to +23.09 | yes: LOSS |
| pod start wait, mean (s) | 3.591 | 2.967 | -17.4% | -1.864 to +0.6166 | no |
| host CPU busy, the real machine under kind (%) | 49.21 | 48.3 | -1.8% | -1.834 to +0.0216 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*