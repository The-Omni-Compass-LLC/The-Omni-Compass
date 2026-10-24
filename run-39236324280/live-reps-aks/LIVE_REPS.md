# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.831 | 1.831 |
| node-hours | 0.4625 | 0.4632 |
| energy, parked workers still on at idle power (Wh, declared model) | 87.16 | 85.85 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.27 | 82.27 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 506.7 | 498.1 |
| response time (ms), 95th percentile | 1172 | 1191 |
| response time (ms), 99th percentile | 4523 | 4002 |
| time over the response line (% of samples) | 28.07 | 28.09 |
| failed requests (%) | 4.394 | 4.035 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.92 | 13.97 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.41 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 7.843 |
| pods with no machine to take them (unschedulable) | 2.5 | 2.46 |
| time pods had no machine to take them, pod-minutes | 4.755 | 4.793 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.269 | 5.031 |
| utilisation (used / allocatable) | 0.4854 | 0.4845 |
| CPU used (cores), mean | 1.679 | 1.683 |
| Omni's own CPU (cores), mean | 0 | 0.004866 |
| CPU used with Omni's own (cores), mean | 1.679 | 1.688 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 194.3 | 193.6 |
| HPA replicas, mean | 9.317 | 9.362 |
| pods started | 5.08 | 4.89 |
| pod start wait, total (s) | 321 | 338.3 |
| pod start wait, mean (s) | 60.13 | 66.88 |
| machines billed, machine-hours | 0.5971 | 0.5896 |
| compute bill at list price ($) | 0.05732 | 0.0566 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped) vs native, 100 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.831 | 1.831 | -0.0% | -0.03634 to +0.03578 | no |
| node-hours | 0.4625 | 0.4632 | +0.1% | -0.008445 to +0.009773 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 87.16 | 85.85 | -1.5% | -3.153 to +0.5414 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.27 | 82.27 | +0.0% | -0.9954 to +1.001 | no |
| response time (ms), mean | 506.7 | 498.1 | -1.7% | -24.36 to +7.156 | no |
| response time (ms), 95th percentile | 1172 | 1191 | +1.7% | -53.92 to +93.1 | no |
| response time (ms), 99th percentile | 4523 | 4002 | -11.5% | -1055 to +13.18 | no |
| time over the response line (% of samples) | 28.07 | 28.09 | +0.1% | -0.9277 to +0.9613 | no |
| failed requests (%) | 4.394 | 4.035 | -8.2% | -0.8862 to +0.1693 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.92 | 13.97 | +0.4% | -0.2151 to +0.3151 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.41 | +24.4 (native is 0) | +23.74 to +25.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.5 | 2.46 | -1.6% | -0.3219 to +0.2419 | no |
| time pods had no machine to take them, pod-minutes | 4.755 | 4.793 | +0.8% | -2.35 to +2.427 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.269 | 5.031 | -4.5% | -0.665 to +0.188 | no |
| utilisation (used / allocatable) | 0.4854 | 0.4845 | -0.2% | -0.01104 to +0.009332 | no |
| CPU used (cores), mean | 1.679 | 1.683 | +0.2% | -0.01489 to +0.02173 | no |
| Omni's own CPU (cores), mean | 0 | 0.004866 | +0.00487 (native is 0) | +0.004691 to +0.005041 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.679 | 1.688 | +0.5% | -0.01003 to +0.0266 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 194.3 | 193.6 | -0.4% | -3.794 to +2.285 | no |
| HPA replicas, mean | 9.317 | 9.362 | +0.5% | -0.008144 to +0.09799 | no |
| pods started | 5.08 | 4.89 | -3.7% | -0.6436 to +0.2636 | no |
| pod start wait, total (s) | 321 | 338.3 | +5.4% | -138.2 to +172.8 | no |
| pod start wait, mean (s) | 60.13 | 66.88 | +11.2% | -22.63 to +36.12 | no |
| machines billed, machine-hours | 0.5971 | 0.5896 | -1.3% | -0.02339 to +0.008424 | no |
| compute bill at list price ($) | 0.05732 | 0.0566 | -1.3% | -0.002246 to +0.0008087 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*