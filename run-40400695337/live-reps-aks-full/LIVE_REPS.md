# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 2.814 | 2.88 |
| node-hours | 0.4728 | 0.4875 |
| energy, parked workers still on at idle power (Wh, declared model) | 69.43 | 89.11 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 67.08 | 70.68 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 560.9 | 606.5 |
| response time (ms), 95th percentile | 1664 | 1016 |
| response time (ms), 99th percentile | 3781 | 5014 |
| time over the response line (% of samples) | 65.02 | 70.34 |
| failed requests (%) | 54.86 | 58.74 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 36.19 |
| pods with no machine to take them (unschedulable) | 2 | 12.67 |
| time pods had no machine to take them, pod-minutes | 2.467 | 35.02 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.783 | 44.79 |
| utilisation (used / allocatable) | 0.5327 | 0.5468 |
| CPU used (cores), mean | 2.853 | 2.988 |
| Omni's own CPU (cores), mean | 0 | 0.01163 |
| CPU used with Omni's own (cores), mean | 2.853 | 2.999 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 139.8 | 139.8 |
| HPA replicas, mean | 9.146 | 15.51 |
| pods started | 5 | 18.33 |
| pod start wait, total (s) | 183.3 | 2349 |
| pod start wait, mean (s) | 36.67 | 132 |
| machines billed, machine-hours | 0.4685 | 0.499 |
| compute bill at list price ($) | 0.04498 | 0.0479 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.814 | 2.88 | +2.4% | −0.1626 to +0.2957 | no |
| node-hours | 0.4728 | 0.4875 | +3.1% | −0.0307 to +0.0601 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 69.43 | 89.11 | +28.4% | +10.6487 to +28.7188 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 67.08 | 70.68 | +5.4% | −8.1677 to +15.3825 | no |
| response time (ms), mean | 560.9 | 606.5 | +8.1% | −752.5811 to +843.7920 | no |
| response time (ms), 95th percentile | 1664 | 1016 | −39.0% | −3534.8361 to +2237.9894 | no |
| response time (ms), 99th percentile | 3781 | 5014 | +32.6% | −10938.0998 to +13404.4271 | no |
| time over the response line (% of samples) | 65.02 | 70.34 | +8.2% | −23.2358 to +33.8825 | no |
| failed requests (%) | 54.86 | 58.74 | +7.1% | −45.8884 to +53.6478 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +9.3940 to +26.6060 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2 | 12.67 | +533.3% | −0.8080 to +22.1413 | no |
| time pods had no machine to take them, pod-minutes | 2.467 | 35.02 | +1319.6% | +27.1183 to +37.9817 | yes: LOSS |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.783 | 44.79 | +674.5% | +36.2927 to +41.7295 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.5327 | 0.5468 | +2.6% | −0.1113 to +0.1394 | no |
| CPU used (cores), mean | 2.853 | 2.988 | +4.7% | −0.6483 to +0.9176 | no |
| Omni's own CPU (cores), mean | 0 | 0.01163 | +0.012 (native is 0) | +0.0064 to +0.0169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.853 | 2.999 | +5.1% | −0.6347 to +0.9273 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 139.8 | 139.8 | −0.0% | −15.1407 to +15.0651 | no |
| HPA replicas, mean | 9.146 | 15.51 | +69.6% | +5.7778 to +6.9578 | yes: power given |
| pods started | 5 | 18.33 | +266.7% | +5.3473 to +21.3194 | yes: power given |
| pod start wait, total (s) | 183.3 | 2349 | +1181.3% | +1857.6054 to +2473.7279 | yes: LOSS |
| pod start wait, mean (s) | 36.67 | 132 | +260.1% | +75.9473 to +114.8085 | yes: LOSS |
| machines billed, machine-hours | 0.4685 | 0.499 | +6.5% | −0.1277 to +0.1887 | no |
| compute bill at list price ($) | 0.04498 | 0.0479 | +6.5% | −0.0123 to +0.0181 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*