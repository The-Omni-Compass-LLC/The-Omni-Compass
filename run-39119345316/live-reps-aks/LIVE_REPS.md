# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.87 | 1.933 |
| node-hours | 0.9414 | 0.9694 |
| energy, parked workers still on at idle power (Wh, declared model) | 205.3 | 222.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 200.4 | 205 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 381.5 | 416.6 |
| response time (ms), 95th percentile | 805.3 | 974.5 |
| response time (ms), 99th percentile | 1974 | 4434 |
| time over the response line (% of samples) | 48.25 | 41.9 |
| failed requests (%) | 38.58 | 33.31 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 32.42 |
| pods with no machine to take them (unschedulable) | 2.4 | 3 |
| time pods had no machine to take them, pod-minutes | 19.87 | 3.667 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.74 | 7.563 |
| utilisation (used / allocatable) | 0.7536 | 0.741 |
| CPU used (cores), mean | 2.677 | 2.71 |
| Omni's own CPU (cores), mean | 0 | 0.00386 |
| CPU used with Omni's own (cores), mean | 2.677 | 2.713 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 148.8 | 150.9 |
| HPA replicas, mean | 9.495 | 9.622 |
| pods started | 5.2 | 3.8 |
| pod start wait, total (s) | 1229 | 1075 |
| pod start wait, mean (s) | 240.4 | 259.1 |
| machines billed, machine-hours | 1.122 | 1.176 |
| compute bill at list price ($) | 0.1077 | 0.1129 |

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
| worker nodes in service, mean | 1.87 | 1.933 | +3.3% | -0.1491 to +0.2738 | no |
| node-hours | 0.9414 | 0.9694 | +3.0% | -0.0808 to +0.1368 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 205.3 | 222.6 | +8.4% | -29.16 to +63.74 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 200.4 | 205 | +2.3% | -7.43 to +16.62 | no |
| response time (ms), mean | 381.5 | 416.6 | +9.2% | -75.78 to +145.9 | no |
| response time (ms), 95th percentile | 805.3 | 974.5 | +21.0% | -178.9 to +517.2 | no |
| response time (ms), 99th percentile | 1974 | 4434 | +124.6% | -92.6 to +5012 | no |
| time over the response line (% of samples) | 48.25 | 41.9 | -13.2% | -18.46 to +5.746 | no |
| failed requests (%) | 38.58 | 33.31 | -13.7% | -16.17 to +5.625 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 29 | -2.0% | -2.015 to +0.8155 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.2 | +40.2 (native is 0) | +35.13 to +45.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.4 | 3 | +25.0% | -1.283 to +2.483 | no |
| time pods had no machine to take them, pod-minutes | 19.87 | 3.667 | -81.5% | -63.61 to +31.2 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.74 | 7.563 | +12.2% | -1.483 to +3.13 | no |
| utilisation (used / allocatable) | 0.7536 | 0.741 | -1.7% | -0.07606 to +0.05082 | no |
| CPU used (cores), mean | 2.677 | 2.71 | +1.2% | -0.06814 to +0.1333 | no |
| Omni's own CPU (cores), mean | 0 | 0.00386 | +0.00386 (native is 0) | +0.002958 to +0.004762 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.677 | 2.713 | +1.4% | -0.06372 to +0.1366 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 148.8 | 150.9 | +1.4% | -5.6 to +9.84 | no |
| HPA replicas, mean | 9.495 | 9.622 | +1.3% | -0.3935 to +0.6471 | no |
| pods started | 5.2 | 3.8 | -26.9% | -6.993 to +4.193 | no |
| pod start wait, total (s) | 1229 | 1075 | -12.5% | -4230 to +3922 | no |
| pod start wait, mean (s) | 240.4 | 259.1 | +7.8% | -886.7 to +924.2 | no |
| machines billed, machine-hours | 1.122 | 1.176 | +4.9% | -0.1759 to +0.2849 | no |
| compute bill at list price ($) | 0.1077 | 0.1129 | +4.9% | -0.01688 to +0.02735 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*