# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.827 | 1.795 |
| node-hours | 0.4599 | 0.4508 |
| energy, parked workers still on at idle power (Wh, declared model) | 84.8 | 85.56 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.53 | 81.69 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 495.7 | 516.7 |
| response time (ms), 95th percentile | 1127 | 1176 |
| response time (ms), 99th percentile | 3908 | 4977 |
| time over the response line (% of samples) | 29.76 | 28.39 |
| failed requests (%) | 4.04 | 4.945 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 13.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 7.253 |
| pods with no machine to take them (unschedulable) | 2.8 | 2.4 |
| time pods had no machine to take them, pod-minutes | 3.317 | 2.763 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.57 | 5.317 |
| utilisation (used / allocatable) | 0.487 | 0.5045 |
| CPU used (cores), mean | 1.69 | 1.72 |
| Omni's own CPU (cores), mean | 0 | 0.0045 |
| CPU used with Omni's own (cores), mean | 1.69 | 1.725 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 191.7 | 189.1 |
| HPA replicas, mean | 9.397 | 9.305 |
| pods started | 5.2 | 4.4 |
| pod start wait, total (s) | 244.6 | 202.4 |
| pod start wait, mean (s) | 47.85 | 38.96 |
| machines billed, machine-hours | 0.5687 | 0.5831 |
| compute bill at list price ($) | 0.05459 | 0.05597 |

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
| worker nodes in service, mean | 1.827 | 1.795 | -1.7% | -0.07202 to +0.008843 | no |
| node-hours | 0.4599 | 0.4508 | -2.0% | -0.01635 to -0.001758 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 84.8 | 85.56 | +0.9% | -0.8982 to +2.403 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.53 | 81.69 | +0.2% | -1.437 to +1.767 | no |
| response time (ms), mean | 495.7 | 516.7 | +4.2% | -47.16 to +89.2 | no |
| response time (ms), 95th percentile | 1127 | 1176 | +4.3% | -213.4 to +311.4 | no |
| response time (ms), 99th percentile | 3908 | 4977 | +27.3% | -761.3 to +2899 | no |
| time over the response line (% of samples) | 29.76 | 28.39 | -4.6% | -6.684 to +3.935 | no |
| failed requests (%) | 4.04 | 4.945 | +22.4% | -0.261 to +2.071 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 13.6 | -1.4% | -1.819 to +1.419 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 | +23 (native is 0) | +19.28 to +26.72 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.8 | 2.4 | -14.3% | -2.283 to +1.483 | no |
| time pods had no machine to take them, pod-minutes | 3.317 | 2.763 | -16.7% | -3.04 to +1.933 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.57 | 5.317 | -4.5% | -1.761 to +1.254 | no |
| utilisation (used / allocatable) | 0.487 | 0.5045 | +3.6% | -0.007273 to +0.04235 | no |
| CPU used (cores), mean | 1.69 | 1.72 | +1.8% | -0.03716 to +0.09814 | no |
| Omni's own CPU (cores), mean | 0 | 0.0045 | +0.0045 (native is 0) | +0.003609 to +0.005391 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.69 | 1.725 | +2.1% | -0.033 to +0.103 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 191.7 | 189.1 | -1.4% | -9.46 to +4.277 | no |
| HPA replicas, mean | 9.397 | 9.305 | -1.0% | -0.3433 to +0.1574 | no |
| pods started | 5.2 | 4.4 | -15.4% | -3.188 to +1.588 | no |
| pod start wait, total (s) | 244.6 | 202.4 | -17.3% | -231.2 to +146.8 | no |
| pod start wait, mean (s) | 47.85 | 38.96 | -18.6% | -47.58 to +29.8 | no |
| machines billed, machine-hours | 0.5687 | 0.5831 | +2.5% | -0.01743 to +0.0462 | no |
| compute bill at list price ($) | 0.05459 | 0.05597 | +2.5% | -0.001673 to +0.004436 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*