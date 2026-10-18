# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.932 | 1.936 |
| node-hours | 1.395 | 1.398 |
| energy, parked workers still on at idle power (Wh, declared model) | 305.3 | 305 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 301.6 | 301.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 945.7 | 1067 |
| response time (ms), 95th percentile | 3500 | 4276 |
| response time (ms), 99th percentile | 6979 | 7325 |
| time over the response line (% of samples) | 86.43 | 88.49 |
| failed requests (%) | 76.53 | 78.48 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 43.2 | 43.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 31.15 |
| pods with no machine to take them (unschedulable) | 3 | 3 |
| time pods had no machine to take them, pod-minutes | 4.017 | 3.76 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.373 | 7.697 |
| utilisation (used / allocatable) | 0.7876 | 0.7869 |
| CPU used (cores), mean | 2.891 | 2.895 |
| Omni's own CPU (cores), mean | 0 | 0.00396 |
| CPU used with Omni's own (cores), mean | 2.891 | 2.899 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 144.5 | 144.3 |
| HPA replicas, mean | 9.793 | 9.79 |
| pods started | 5.8 | 5.4 |
| pod start wait, total (s) | 285.8 | 270 |
| pod start wait, mean (s) | 51.92 | 50.27 |
| machines billed, machine-hours | 1.535 | 1.513 |
| compute bill at list price ($) | 0.1473 | 0.1452 |

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
| worker nodes in service, mean | 1.932 | 1.936 | +0.2% | -0.01041 to +0.01927 | no |
| node-hours | 1.395 | 1.398 | +0.2% | -0.009991 to +0.01532 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 305.3 | 305 | -0.1% | -4.9 to +4.239 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 301.6 | 301.5 | -0.0% | -4.426 to +4.248 | no |
| response time (ms), mean | 945.7 | 1067 | +12.8% | -190.2 to +432.9 | no |
| response time (ms), 95th percentile | 3500 | 4276 | +22.2% | -664.9 to +2216 | no |
| response time (ms), 99th percentile | 6979 | 7325 | +5.0% | -1558 to +2252 | no |
| time over the response line (% of samples) | 86.43 | 88.49 | +2.4% | -1.219 to +5.331 | no |
| failed requests (%) | 76.53 | 78.48 | +2.5% | -0.3527 to +4.252 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 43.2 | 43.2 | +0.0% | -0.8778 to +0.8778 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.2 | +59.2 (native is 0) | +55.14 to +63.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 3 | 3 | +0.0% | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 4.017 | 3.76 | -6.4% | -1.245 to +0.7312 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.373 | 7.697 | +4.4% | -1.296 to +1.943 | no |
| utilisation (used / allocatable) | 0.7876 | 0.7869 | -0.1% | -0.01704 to +0.01559 | no |
| CPU used (cores), mean | 2.891 | 2.895 | +0.1% | -0.04592 to +0.0538 | no |
| Omni's own CPU (cores), mean | 0 | 0.00396 | +0.00396 (native is 0) | +0.003088 to +0.004832 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.891 | 2.899 | +0.3% | -0.04222 to +0.05801 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 144.5 | 144.3 | -0.1% | -1.292 to +0.9209 | no |
| HPA replicas, mean | 9.793 | 9.79 | -0.0% | -0.0976 to +0.0918 | no |
| pods started | 5.8 | 5.4 | -6.9% | -2.283 to +1.483 | no |
| pod start wait, total (s) | 285.8 | 270 | -5.5% | -75.86 to +44.26 | no |
| pod start wait, mean (s) | 51.92 | 50.27 | -3.2% | -17.73 to +14.44 | no |
| machines billed, machine-hours | 1.535 | 1.513 | -1.4% | -0.08306 to +0.03973 | no |
| compute bill at list price ($) | 0.1473 | 0.1452 | -1.4% | -0.007974 to +0.003814 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*