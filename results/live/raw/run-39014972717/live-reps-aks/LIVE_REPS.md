# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.899 | 1.915 |
| node-hours | 0.9554 | 0.9612 |
| energy, parked workers still on at idle power (Wh, declared model) | 218 | 216.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 214.2 | 213.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 368.6 | 397.7 |
| response time (ms), 95th percentile | 682.7 | 735.1 |
| response time (ms), 99th percentile | 3651 | 3585 |
| time over the response line (% of samples) | 45.33 | 45.37 |
| failed requests (%) | 37.07 | 37.6 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 26.9 |
| pods with no machine to take them (unschedulable) | 2 | 2.8 |
| time pods had no machine to take them, pod-minutes | 2.51 | 3.567 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.23 | 6.783 |
| utilisation (used / allocatable) | 0.8239 | 0.8216 |
| CPU used (cores), mean | 2.975 | 2.99 |
| Omni's own CPU (cores), mean | 0 | 0.00376 |
| CPU used with Omni's own (cores), mean | 2.975 | 2.993 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 143.3 | 142.2 |
| HPA replicas, mean | 9.515 | 9.679 |
| pods started | 5.2 | 5 |
| pod start wait, total (s) | 190.2 | 262.8 |
| pod start wait, mean (s) | 36.12 | 52.56 |
| machines billed, machine-hours | 1.147 | 1.081 |
| compute bill at list price ($) | 0.1101 | 0.1037 |

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
| worker nodes in service, mean | 1.899 | 1.915 | +0.8% | -0.08652 to +0.1177 | no |
| node-hours | 0.9554 | 0.9612 | +0.6% | -0.04394 to +0.05549 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 218 | 216.5 | -0.7% | -15.06 to +11.93 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 214.2 | 213.3 | -0.5% | -17.16 to +15.23 | no |
| response time (ms), mean | 368.6 | 397.7 | +7.9% | -94.06 to +152.4 | no |
| response time (ms), 95th percentile | 682.7 | 735.1 | +7.7% | -38.7 to +143.5 | no |
| response time (ms), 99th percentile | 3651 | 3585 | -1.8% | -6412 to +6280 | no |
| time over the response line (% of samples) | 45.33 | 45.37 | +0.1% | -4.691 to +4.775 | no |
| failed requests (%) | 37.07 | 37.6 | +1.4% | -1.359 to +2.428 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29.6 | +0.0% | -1.241 to +1.241 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.8 (native is 0) | +31.55 to +40.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2 | 2.8 | +40.0% | -0.8187 to +2.419 | no |
| time pods had no machine to take them, pod-minutes | 2.51 | 3.567 | +42.1% | -0.9744 to +3.088 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.23 | 6.783 | +60.4% | -0.7303 to +5.837 | no |
| utilisation (used / allocatable) | 0.8239 | 0.8216 | -0.3% | -0.06856 to +0.06395 | no |
| CPU used (cores), mean | 2.975 | 2.99 | +0.5% | -0.3181 to +0.3479 | no |
| Omni's own CPU (cores), mean | 0 | 0.00376 | +0.00376 (native is 0) | +0.003123 to +0.004397 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.975 | 2.993 | +0.6% | -0.314 to +0.3513 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 143.3 | 142.2 | -0.8% | -6.214 to +3.97 | no |
| HPA replicas, mean | 9.515 | 9.679 | +1.7% | -0.1351 to +0.463 | no |
| pods started | 5.2 | 5 | -3.8% | -0.7552 to +0.3552 | no |
| pod start wait, total (s) | 190.2 | 262.8 | +38.2% | -72.38 to +217.6 | no |
| pod start wait, mean (s) | 36.12 | 52.56 | +45.5% | -11.32 to +44.2 | no |
| machines billed, machine-hours | 1.147 | 1.081 | -5.8% | -0.1743 to +0.04233 | no |
| compute bill at list price ($) | 0.1101 | 0.1037 | -5.8% | -0.01674 to +0.004064 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*