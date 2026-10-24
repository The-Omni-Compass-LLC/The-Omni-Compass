# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.1 | 171.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.1 | 171.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 455.2 | 395.1 |
| response time (ms), 95th percentile | 1820 | 1781 |
| response time (ms), 99th percentile | 4817 | 4634 |
| time over the response line (% of samples) | 20.65 | 19.43 |
| failed requests (%) | 4.042 | 3.192 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4983 | 0.82 |
| utilisation (used / allocatable) | 0.09129 | 0.09021 |
| CPU used (cores), mean | 2.191 | 2.165 |
| Omni's own CPU (cores), mean | 0 | 0.01178 |
| CPU used with Omni's own (cores), mean | 2.191 | 2.177 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 326.5 | 330.5 |
| HPA replicas, mean | 14.7 | 15.07 |
| pods started | 5.6 | 5.2 |
| pod start wait, total (s) | 8.8 | 9.4 |
| pod start wait, mean (s) | 1.583 | 1.738 |
| host CPU busy, the real machine under kind (%) | 63.92 | 63.9 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 310.4 | 326.3 |
| second app: response time (ms), 99th percentile | 1881 | 1805 |
| second app: time over the response line (% of samples) | 12.7 | 13 |
| second app: failed requests (%) | 10.92 | 10.97 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.2% | -0.0009049 to +0.005572 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.1 | 171.1 | +0.0% | -0.4868 to +0.5255 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.1 | 171.1 | +0.0% | -0.4868 to +0.5255 | no |
| response time (ms), mean | 455.2 | 395.1 | -13.2% | -124.4 to +4.129 | no |
| response time (ms), 95th percentile | 1820 | 1781 | -2.1% | -519.5 to +442.2 | no |
| response time (ms), 99th percentile | 4817 | 4634 | -3.8% | -1092 to +725.7 | no |
| time over the response line (% of samples) | 20.65 | 19.43 | -5.9% | -2.743 to +0.3152 | no |
| failed requests (%) | 4.042 | 3.192 | -21.0% | -2.015 to +0.3143 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.1 | +0.0% | -0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44 | +44 (native is 0) | +36.24 to +51.76 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4983 | 0.82 | +64.5% | -0.6673 to +1.311 | no |
| utilisation (used / allocatable) | 0.09129 | 0.09021 | -1.2% | -0.002491 to +0.000341 | no |
| CPU used (cores), mean | 2.191 | 2.165 | -1.2% | -0.0598 to +0.008183 | no |
| Omni's own CPU (cores), mean | 0 | 0.01178 | +0.0118 (native is 0) | +0.01038 to +0.01318 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.191 | 2.177 | -0.6% | -0.04812 to +0.02007 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 326.5 | 330.5 | +1.2% | -4.288 to +12.35 | no |
| HPA replicas, mean | 14.7 | 15.07 | +2.5% | -0.007473 to +0.747 | no |
| pods started | 5.6 | 5.2 | -7.1% | -1.24 to +0.4396 | no |
| pod start wait, total (s) | 8.8 | 9.4 | +6.8% | -2.476 to +3.676 | no |
| pod start wait, mean (s) | 1.583 | 1.738 | +9.8% | -0.2811 to +0.5906 | no |
| host CPU busy, the real machine under kind (%) | 63.92 | 63.9 | -0.0% | -0.3503 to +0.3023 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 310.4 | 326.3 | +5.1% | -22.46 to +54.13 | no |
| second app: response time (ms), 99th percentile | 1881 | 1805 | -4.0% | -1431 to +1279 | no |
| second app: time over the response line (% of samples) | 12.7 | 13 | +2.4% | -0.1643 to +0.7669 | no |
| second app: failed requests (%) | 10.92 | 10.97 | +0.5% | -0.4813 to +0.5822 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*