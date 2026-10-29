# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.813 | 2.832 |
| node-hours | 0.7102 | 0.715 |
| energy, parked workers still on at idle power (Wh, declared model) | 86.65 | 87.77 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.72 | 83.24 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 516.7 | 503.3 |
| response time (ms), 95th percentile | 1244 | 1194 |
| response time (ms), 99th percentile | 4732 | 4215 |
| time over the response line (% of samples) | 29.13 | 28.83 |
| failed requests (%) | 4.827 | 4.938 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.06 | 13.91 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.91 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 9.179 |
| pods with no machine to take them (unschedulable) | 2.602 | 2.398 |
| time pods had no machine to take them, pod-minutes | 6.991 | 5.976 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.912 | 5.604 |
| utilisation (used / allocatable) | 0.3626 | 0.3607 |
| CPU used (cores), mean | 1.937 | 1.938 |
| Omni's own CPU (cores), mean | 0 | 0.00515 |
| CPU used with Omni's own (cores), mean | 1.937 | 1.943 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 169.4 | 170.4 |
| HPA replicas, mean | 9.368 | 9.35 |
| pods started | 5.051 | 4.755 |
| pod start wait, total (s) | 523.4 | 453.7 |
| pod start wait, mean (s) | 97.79 | 89.6 |
| machines billed, machine-hours | 0.5862 | 0.5928 |
| compute bill at list price ($) | 0.05627 | 0.05691 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped) vs native, 97 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.814 | 2.832 | +0.7% | −0.0098 to +0.0469 | no |
| node-hours | 0.7104 | 0.715 | +0.7% | −0.0024 to +0.0117 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 86.62 | 87.77 | +1.3% | −0.6670 to +2.9702 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.7 | 83.23 | +0.6% | −0.2945 to +1.3550 | no |
| response time (ms), mean | 517.1 | 503.1 | −2.7% | −29.7566 to +1.8811 | no |
| response time (ms), 95th percentile | 1245 | 1195 | −4.0% | −128.4729 to +28.5631 | no |
| response time (ms), 99th percentile | 4744 | 4222 | −11.0% | −1009.6926 to −34.3668 | yes: GAIN |
| time over the response line (% of samples) | 29.06 | 28.81 | −0.9% | −1.1301 to +0.6231 | no |
| failed requests (%) | 4.758 | 4.945 | +3.9% | −0.4799 to +0.8526 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.07 | 13.9 | −1.2% | −0.4116 to +0.0611 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.92 | +24.918 (native is 0) | +24.1653 to +25.6698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.598 | 2.392 | −7.9% | −0.5274 to +0.1151 | no |
| time pods had no machine to take them, pod-minutes | 7.018 | 5.993 | −14.6% | −4.1768 to +2.1273 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.9 | 5.573 | −5.6% | −0.7542 to +0.0989 | no |
| utilisation (used / allocatable) | 0.3622 | 0.3605 | −0.5% | −0.0069 to +0.0035 | no |
| CPU used (cores), mean | 1.935 | 1.937 | +0.1% | −0.0176 to +0.0208 | no |
| Omni's own CPU (cores), mean | 0 | 0.005163 | +0.005 (native is 0) | +0.0050 to +0.0053 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.935 | 1.942 | +0.4% | −0.0125 to +0.0260 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 169.5 | 170.5 | +0.6% | −1.1581 to +3.0914 | no |
| HPA replicas, mean | 9.371 | 9.348 | −0.2% | −0.0802 to +0.0340 | no |
| pods started | 5.01 | 4.753 | −5.1% | −0.7001 to +0.1847 | no |
| pod start wait, total (s) | 525.4 | 455.2 | −13.4% | −278.2501 to +137.6728 | no |
| pod start wait, mean (s) | 98.43 | 89.88 | −8.7% | −49.2406 to +32.1393 | no |
| machines billed, machine-hours | 0.586 | 0.5931 | +1.2% | −0.0074 to +0.0216 | no |
| compute bill at list price ($) | 0.05626 | 0.05694 | +1.2% | −0.0007 to +0.0021 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*