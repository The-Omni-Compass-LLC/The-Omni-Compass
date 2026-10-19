# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.919 | 1.929 |
| node-hours | 0.9652 | 0.9674 |
| energy, parked workers still on at idle power (Wh, declared model) | 208.2 | 212.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 205.2 | 202.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 450.9 | 432.6 |
| response time (ms), 95th percentile | 818.6 | 849.1 |
| response time (ms), 99th percentile | 5012 | 3723 |
| time over the response line (% of samples) | 42.66 | 47.04 |
| failed requests (%) | 33.14 | 36.74 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.8 | 29.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 35.88 |
| pods with no machine to take them (unschedulable) | 2.2 | 2.8 |
| time pods had no machine to take them, pod-minutes | 2.83 | 3.527 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.42 | 6.007 |
| utilisation (used / allocatable) | 0.7538 | 0.7337 |
| CPU used (cores), mean | 2.75 | 2.688 |
| Omni's own CPU (cores), mean | 0 | 0.0041 |
| CPU used with Omni's own (cores), mean | 2.75 | 2.692 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 148.5 | 150.2 |
| HPA replicas, mean | 9.64 | 9.686 |
| pods started | 5.8 | 5 |
| pod start wait, total (s) | 215.8 | 263.2 |
| pod start wait, mean (s) | 36.24 | 52.64 |
| machines billed, machine-hours | 1.118 | 1.111 |
| compute bill at list price ($) | 0.1073 | 0.1067 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped) vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.919 | 1.929 | +0.5% | -0.09141 to +0.1112 | no |
| node-hours | 0.9652 | 0.9674 | +0.2% | -0.04874 to +0.05318 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 208.2 | 212.6 | +2.1% | -24.12 to +32.76 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 205.2 | 202.4 | -1.4% | -16.29 to +10.64 | no |
| response time (ms), mean | 450.9 | 432.6 | -4.0% | -45.12 to +8.594 | no |
| response time (ms), 95th percentile | 818.6 | 849.1 | +3.7% | -145.6 to +206.6 | no |
| response time (ms), 99th percentile | 5012 | 3723 | -25.7% | -3964 to +1385 | no |
| time over the response line (% of samples) | 42.66 | 47.04 | +10.3% | -2.199 to +10.95 | no |
| failed requests (%) | 33.14 | 36.74 | +10.9% | -3.028 to +10.23 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.8 | 29.2 | +1.4% | -1.266 to +2.066 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40 | +40 (native is 0) | +34.81 to +45.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.2 | 2.8 | +27.3% | -1.283 to +2.483 | no |
| time pods had no machine to take them, pod-minutes | 2.83 | 3.527 | +24.6% | -1.888 to +3.281 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.42 | 6.007 | +35.9% | -2.889 to +6.062 | no |
| utilisation (used / allocatable) | 0.7538 | 0.7337 | -2.7% | -0.0486 to +0.008327 | no |
| CPU used (cores), mean | 2.75 | 2.688 | -2.3% | -0.2489 to +0.1251 | no |
| Omni's own CPU (cores), mean | 0 | 0.0041 | +0.0041 (native is 0) | +0.003381 to +0.004819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.75 | 2.692 | -2.1% | -0.2444 to +0.1288 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 148.5 | 150.2 | +1.1% | -0.7431 to +4.054 | no |
| HPA replicas, mean | 9.64 | 9.686 | +0.5% | -0.1331 to +0.2255 | no |
| pods started | 5.8 | 5 | -13.8% | -3.021 to +1.421 | no |
| pod start wait, total (s) | 215.8 | 263.2 | +22.0% | -134.4 to +229.2 | no |
| pod start wait, mean (s) | 36.24 | 52.64 | +45.2% | -13.95 to +46.75 | no |
| machines billed, machine-hours | 1.118 | 1.111 | -0.6% | -0.1311 to +0.118 | no |
| compute bill at list price ($) | 0.1073 | 0.1067 | -0.6% | -0.01259 to +0.01133 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*