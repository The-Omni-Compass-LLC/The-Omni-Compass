# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.926 | 2.088 |
| node-hours | 0.9673 | 1.047 |
| energy, parked workers still on at idle power (Wh, declared model) | 220.7 | 219.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 202.8 | 215.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 412.1 | 439.2 |
| response time (ms), 95th percentile | 847.9 | 1088 |
| response time (ms), 99th percentile | 2777 | 3425 |
| time over the response line (% of samples) | 46.69 | 41.06 |
| failed requests (%) | 37.35 | 28.88 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 27.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 24.55 |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 |
| time pods had no machine to take them, pod-minutes | 3.377 | 2.32 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.087 | 4.583 |
| utilisation (used / allocatable) | 0.7306 | 0.7197 |
| CPU used (cores), mean | 2.664 | 2.772 |
| Omni's own CPU (cores), mean | 0 | 0.00416 |
| CPU used with Omni's own (cores), mean | 2.664 | 2.777 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 151.6 | 154.5 |
| HPA replicas, mean | 9.576 | 9.484 |
| pods started | 4.8 | 5 |
| pod start wait, total (s) | 250 | 175.4 |
| pod start wait, mean (s) | 52.09 | 35.08 |
| machines billed, machine-hours | 1.155 | 1.243 |
| compute bill at list price ($) | 0.1109 | 0.1193 |

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
| worker nodes in service, mean | 1.926 | 2.088 | +8.4% | -0.5238 to +0.8485 | no |
| node-hours | 0.9673 | 1.047 | +8.2% | -0.266 to +0.4254 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 220.7 | 219.6 | -0.5% | -67.66 to +65.56 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 202.8 | 215.4 | +6.2% | -29.91 to +55.17 | no |
| response time (ms), mean | 412.1 | 439.2 | +6.6% | -63.77 to +118 | no |
| response time (ms), 95th percentile | 847.9 | 1088 | +28.3% | -651 to +1131 | no |
| response time (ms), 99th percentile | 2777 | 3425 | +23.3% | -3244 to +4539 | no |
| time over the response line (% of samples) | 46.69 | 41.06 | -12.1% | -19.33 to +8.057 | no |
| failed requests (%) | 37.35 | 28.88 | -22.7% | -23.66 to +6.733 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 27.6 | -6.8% | -6.561 to +2.561 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.4 | +35.4 (native is 0) | +31.72 to +39.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 | -30.8% | -3.344 to +1.744 | no |
| time pods had no machine to take them, pod-minutes | 3.377 | 2.32 | -31.3% | -4.272 to +2.159 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.087 | 4.583 | -35.3% | -8.111 to +3.104 | no |
| utilisation (used / allocatable) | 0.7306 | 0.7197 | -1.5% | -0.155 to +0.1331 | no |
| CPU used (cores), mean | 2.664 | 2.772 | +4.1% | -0.1569 to +0.3747 | no |
| Omni's own CPU (cores), mean | 0 | 0.00416 | +0.00416 (native is 0) | +0.003667 to +0.004653 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.664 | 2.777 | +4.2% | -0.1523 to +0.3784 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 151.6 | 154.5 | +1.9% | -16.93 to +22.75 | no |
| HPA replicas, mean | 9.576 | 9.484 | -1.0% | -0.5493 to +0.3651 | no |
| pods started | 4.8 | 5 | +4.2% | -0.8387 to +1.239 | no |
| pod start wait, total (s) | 250 | 175.4 | -29.8% | -304.2 to +155 | no |
| pod start wait, mean (s) | 52.09 | 35.08 | -32.7% | -55.26 to +21.24 | no |
| machines billed, machine-hours | 1.155 | 1.243 | +7.6% | -0.3291 to +0.5037 | no |
| compute bill at list price ($) | 0.1109 | 0.1193 | +7.6% | -0.0316 to +0.04835 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*