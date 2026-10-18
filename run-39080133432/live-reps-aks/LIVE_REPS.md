# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.805 | 1.836 |
| node-hours | 0.4545 | 0.4637 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.72 | 85.39 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.03 | 82.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 519.7 | 519.3 |
| response time (ms), 95th percentile | 1110 | 1389 |
| response time (ms), 99th percentile | 4834 | 4221 |
| time over the response line (% of samples) | 28.95 | 29.13 |
| failed requests (%) | 4.778 | 3.719 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 13.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 11.43 |
| pods with no machine to take them (unschedulable) | 2.6 | 2.6 |
| time pods had no machine to take them, pod-minutes | 2.91 | 2.787 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.55 | 4.347 |
| utilisation (used / allocatable) | 0.4971 | 0.4866 |
| CPU used (cores), mean | 1.704 | 1.696 |
| Omni's own CPU (cores), mean | 0 | 0.00482 |
| CPU used with Omni's own (cores), mean | 1.704 | 1.701 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 191.2 | 192.3 |
| HPA replicas, mean | 9.322 | 9.368 |
| pods started | 5.6 | 5.2 |
| pod start wait, total (s) | 216.8 | 206.6 |
| pod start wait, mean (s) | 39.15 | 39.53 |
| machines billed, machine-hours | 0.5806 | 0.5596 |
| compute bill at list price ($) | 0.05573 | 0.05372 |

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
| worker nodes in service, mean | 1.805 | 1.836 | +1.7% | -0.03706 to +0.1002 | no |
| node-hours | 0.4545 | 0.4637 | +2.0% | -0.007267 to +0.02571 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.72 | 85.39 | -0.4% | -3.508 to +2.85 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.03 | 82.3 | +0.3% | -1.723 to +2.247 | no |
| response time (ms), mean | 519.7 | 519.3 | -0.1% | -70.66 to +69.78 | no |
| response time (ms), 95th percentile | 1110 | 1389 | +25.2% | -180.1 to +738.5 | no |
| response time (ms), 99th percentile | 4834 | 4221 | -12.7% | -3761 to +2534 | no |
| time over the response line (% of samples) | 28.95 | 29.13 | +0.6% | -4.741 to +5.095 | no |
| failed requests (%) | 4.778 | 3.719 | -22.2% | -4.266 to +2.148 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14 | 13.4 | -4.3% | -1.28 to +0.07998 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.6 | +24.6 (native is 0) | +20.71 to +28.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.6 | 2.6 | +0.0% | -1.963 to +1.963 | no |
| time pods had no machine to take them, pod-minutes | 2.91 | 2.787 | -4.2% | -2.712 to +2.465 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.55 | 4.347 | -21.7% | -4.269 to +1.862 | no |
| utilisation (used / allocatable) | 0.4971 | 0.4866 | -2.1% | -0.05969 to +0.03872 | no |
| CPU used (cores), mean | 1.704 | 1.696 | -0.5% | -0.1244 to +0.1086 | no |
| Omni's own CPU (cores), mean | 0 | 0.00482 | +0.00482 (native is 0) | +0.004068 to +0.005572 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.704 | 1.701 | -0.2% | -0.119 to +0.1129 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 191.2 | 192.3 | +0.6% | -8.299 to +10.44 | no |
| HPA replicas, mean | 9.322 | 9.368 | +0.5% | -0.2005 to +0.2912 | no |
| pods started | 5.6 | 5.2 | -7.1% | -1.08 to +0.28 | no |
| pod start wait, total (s) | 216.8 | 206.6 | -4.7% | -188.9 to +168.5 | no |
| pod start wait, mean (s) | 39.15 | 39.53 | +1.0% | -28.06 to +28.81 | no |
| machines billed, machine-hours | 0.5806 | 0.5596 | -3.6% | -0.06695 to +0.02495 | no |
| compute bill at list price ($) | 0.05573 | 0.05372 | -3.6% | -0.006427 to +0.002395 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*