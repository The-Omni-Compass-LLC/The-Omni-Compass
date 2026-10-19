# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.813 | 1.826 |
| node-hours | 0.4574 | 0.4606 |
| energy, parked workers still on at idle power (Wh, declared model) | 86.21 | 85.88 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.66 | 82.59 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 562.6 | 514.6 |
| response time (ms), 95th percentile | 1402 | 1155 |
| response time (ms), 99th percentile | 5371 | 4351 |
| time over the response line (% of samples) | 31.77 | 29.63 |
| failed requests (%) | 5.853 | 4.437 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 14.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 5.824 |
| pods with no machine to take them (unschedulable) | 2.6 | 2.4 |
| time pods had no machine to take them, pod-minutes | 3.15 | 2.413 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.993 | 4.387 |
| utilisation (used / allocatable) | 0.5085 | 0.4996 |
| CPU used (cores), mean | 1.751 | 1.733 |
| Omni's own CPU (cores), mean | 0 | 0.00508 |
| CPU used with Omni's own (cores), mean | 1.751 | 1.738 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 187.2 | 189.3 |
| HPA replicas, mean | 9.209 | 9.289 |
| pods started | 6.2 | 5 |
| pod start wait, total (s) | 379.2 | 177.2 |
| pod start wait, mean (s) | 68.72 | 35.44 |
| machines billed, machine-hours | 0.5801 | 0.5727 |
| compute bill at list price ($) | 0.05569 | 0.05498 |

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
| worker nodes in service, mean | 1.813 | 1.826 | +0.8% | -0.05306 to +0.08071 | no |
| node-hours | 0.4574 | 0.4606 | +0.7% | -0.01392 to +0.02025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 86.21 | 85.88 | -0.4% | -2.351 to +1.687 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.66 | 82.59 | -0.1% | -1.075 to +0.9367 | no |
| response time (ms), mean | 562.6 | 514.6 | -8.5% | -86.8 to -9.34 | yes: GAIN |
| response time (ms), 95th percentile | 1402 | 1155 | -17.6% | -647.2 to +154 | no |
| response time (ms), 99th percentile | 5371 | 4351 | -19.0% | -3779 to +1739 | no |
| time over the response line (% of samples) | 31.77 | 29.63 | -6.7% | -5.599 to +1.32 | no |
| failed requests (%) | 5.853 | 4.437 | -24.2% | -4.663 to +1.831 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 14.6 | +1.4% | -0.8387 to +1.239 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.8 | +26.8 (native is 0) | +22.04 to +31.56 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.6 | 2.4 | -7.7% | -2.421 to +2.021 | no |
| time pods had no machine to take them, pod-minutes | 3.15 | 2.413 | -23.4% | -3.252 to +1.778 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.993 | 4.387 | -12.1% | -2.529 to +1.316 | no |
| utilisation (used / allocatable) | 0.5085 | 0.4996 | -1.8% | -0.03789 to +0.01999 | no |
| CPU used (cores), mean | 1.751 | 1.733 | -1.1% | -0.07133 to +0.03442 | no |
| Omni's own CPU (cores), mean | 0 | 0.00508 | +0.00508 (native is 0) | +0.003907 to +0.006253 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.751 | 1.738 | -0.8% | -0.06725 to +0.04051 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 187.2 | 189.3 | +1.1% | -2.218 to +6.322 | no |
| HPA replicas, mean | 9.209 | 9.289 | +0.9% | -0.2558 to +0.4154 | no |
| pods started | 6.2 | 5 | -19.4% | -3.24 to +0.8399 | no |
| pod start wait, total (s) | 379.2 | 177.2 | -53.3% | -608.6 to +204.6 | no |
| pod start wait, mean (s) | 68.72 | 35.44 | -48.4% | -118.2 to +51.62 | no |
| machines billed, machine-hours | 0.5801 | 0.5727 | -1.3% | -0.04988 to +0.03499 | no |
| compute bill at list price ($) | 0.05569 | 0.05498 | -1.3% | -0.004788 to +0.003359 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*