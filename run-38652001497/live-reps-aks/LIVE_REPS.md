# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.945 | 1.921 |
| node-hours | 0.9762 | 0.9636 |
| energy, parked workers still on at idle power (Wh, declared model) | 220.7 | 214.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 203.6 | 203.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 450.8 | 454.5 |
| response time (ms), 95th percentile | 991.3 | 1043 |
| response time (ms), 99th percentile | 4925 | 5481 |
| time over the response line (% of samples) | 46.29 | 41.92 |
| failed requests (%) | 36.41 | 32.61 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 28.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 37.55 |
| pods with no machine to take them (unschedulable) | 2.6 | 2.4 |
| time pods had no machine to take them, pod-minutes | 3.35 | 3.38 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.757 | 6.537 |
| utilisation (used / allocatable) | 0.7256 | 0.7508 |
| CPU used (cores), mean | 2.676 | 2.741 |
| Omni's own CPU (cores), mean | 0 | 0.00462 |
| CPU used with Omni's own (cores), mean | 2.676 | 2.746 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 151.8 | 148.3 |
| HPA replicas, mean | 9.641 | 9.685 |
| pods started | 5.8 | 5.2 |
| pod start wait, total (s) | 251.6 | 250.6 |
| pod start wait, mean (s) | 45.16 | 47.98 |
| machines billed, machine-hours | 1.129 | 1.11 |
| compute bill at list price ($) | 0.1083 | 0.1066 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.945 | 1.921 | -1.3% | -0.08191 to +0.0328 | no |
| node-hours | 0.9762 | 0.9636 | -1.3% | -0.04157 to +0.01635 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 220.7 | 214.3 | -2.9% | -53.68 to +40.93 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 203.6 | 203.8 | +0.1% | -5.127 to +5.608 | no |
| response time (ms), mean | 450.8 | 454.5 | +0.8% | -97.68 to +105.2 | no |
| response time (ms), 95th percentile | 991.3 | 1043 | +5.2% | -454 to +556.9 | no |
| response time (ms), 99th percentile | 4925 | 5481 | +11.3% | -3317 to +4429 | no |
| time over the response line (% of samples) | 46.29 | 41.92 | -9.4% | -9.957 to +1.216 | no |
| failed requests (%) | 36.41 | 32.61 | -10.4% | -10.61 to +3.006 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.6 | 28.2 | -4.7% | -2.815 to +0.01549 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 | +39.2 (native is 0) | +36.37 to +42.03 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.6 | 2.4 | -7.7% | -2.041 to +1.641 | no |
| time pods had no machine to take them, pod-minutes | 3.35 | 3.38 | +0.9% | -2.593 to +2.653 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.757 | 6.537 | -15.7% | -7.841 to +5.401 | no |
| utilisation (used / allocatable) | 0.7256 | 0.7508 | +3.5% | -0.06182 to +0.1124 | no |
| CPU used (cores), mean | 2.676 | 2.741 | +2.4% | -0.2057 to +0.3366 | no |
| Omni's own CPU (cores), mean | 0 | 0.00462 | +0.00462 (native is 0) | +0.00379 to +0.00545 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.676 | 2.746 | +2.6% | -0.2007 to +0.3408 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 151.8 | 148.3 | -2.3% | -15.12 to +8.209 | no |
| HPA replicas, mean | 9.641 | 9.685 | +0.5% | -0.03498 to +0.1227 | no |
| pods started | 5.8 | 5.2 | -10.3% | -3.02 to +1.82 | no |
| pod start wait, total (s) | 251.6 | 250.6 | -0.4% | -186.5 to +184.5 | no |
| pod start wait, mean (s) | 45.16 | 47.98 | +6.2% | -36.05 to +41.68 | no |
| machines billed, machine-hours | 1.129 | 1.11 | -1.6% | -0.1298 to +0.09332 | no |
| compute bill at list price ($) | 0.1083 | 0.1066 | -1.6% | -0.01246 to +0.008959 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*