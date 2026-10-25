# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.822 | 2.807 |
| node-hours | 0.7116 | 0.7082 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.21 | 84.88 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.85 | 81.22 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 501.6 | 471.7 |
| response time (ms), 95th percentile | 1145 | 1011 |
| response time (ms), 99th percentile | 4923 | 4223 |
| time over the response line (% of samples) | 29.33 | 26.23 |
| failed requests (%) | 4.188 | 4.18 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 5.714 |
| pods with no machine to take them (unschedulable) | 2.8 | 3 |
| time pods had no machine to take them, pod-minutes | 3.313 | 3.21 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.99 | 5.07 |
| utilisation (used / allocatable) | 0.3548 | 0.3526 |
| CPU used (cores), mean | 1.902 | 1.879 |
| Omni's own CPU (cores), mean | 0 | 0.0049 |
| CPU used with Omni's own (cores), mean | 1.902 | 1.884 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 170.7 | 171.3 |
| HPA replicas, mean | 9.413 | 9.414 |
| pods started | 5 | 5 |
| pod start wait, total (s) | 240.2 | 234.8 |
| pod start wait, mean (s) | 48.04 | 46.96 |
| machines billed, machine-hours | 0.574 | 0.5819 |
| compute bill at list price ($) | 0.0551 | 0.05586 |

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
| worker nodes in service, mean | 2.822 | 2.807 | −0.6% | −0.0733 to +0.0416 | no |
| node-hours | 0.7116 | 0.7082 | −0.5% | −0.0166 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.21 | 84.88 | −0.4% | −1.6756 to +1.0258 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.85 | 81.22 | −0.8% | −1.5533 to +0.2952 | no |
| response time (ms), mean | 501.6 | 471.7 | −6.0% | −104.1921 to +44.3628 | no |
| response time (ms), 95th percentile | 1145 | 1011 | −11.7% | −270.3155 to +2.3695 | no |
| response time (ms), 99th percentile | 4923 | 4223 | −14.2% | −5125.9790 to +3725.2846 | no |
| time over the response line (% of samples) | 29.33 | 26.23 | −10.6% | −5.3729 to −0.8216 | yes: GAIN |
| failed requests (%) | 4.188 | 4.18 | −0.2% | −2.0607 to +2.0447 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.4 | 14.4 | +7.5% | −0.2415 to +2.2415 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.6 | +24.600 (native is 0) | +22.1799 to +27.0201 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.8 | 3 | +7.1% | −0.3552 to +0.7552 | no |
| time pods had no machine to take them, pod-minutes | 3.313 | 3.21 | −3.1% | −1.3638 to +1.1572 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.99 | 5.07 | +1.6% | −1.2045 to +1.3645 | no |
| utilisation (used / allocatable) | 0.3548 | 0.3526 | −0.6% | −0.0164 to +0.0120 | no |
| CPU used (cores), mean | 1.902 | 1.879 | −1.2% | −0.0662 to +0.0203 | no |
| Omni's own CPU (cores), mean | 0 | 0.0049 | +0.005 (native is 0) | +0.0034 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.902 | 1.884 | −1.0% | −0.0604 to +0.0243 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 170.7 | 171.3 | +0.4% | −3.2790 to +4.5401 | no |
| HPA replicas, mean | 9.413 | 9.414 | +0.0% | −0.3797 to +0.3814 | no |
| pods started | 5 | 5 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 240.2 | 234.8 | −2.2% | −89.9637 to +79.1637 | no |
| pod start wait, mean (s) | 48.04 | 46.96 | −2.2% | −17.9927 to +15.8327 | no |
| machines billed, machine-hours | 0.574 | 0.5819 | +1.4% | −0.0314 to +0.0471 | no |
| compute bill at list price ($) | 0.0551 | 0.05586 | +1.4% | −0.0030 to +0.0045 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*