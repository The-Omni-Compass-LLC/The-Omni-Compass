# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.641 | 2.687 |
| node-hours | 0.2781 | 0.4516 |
| energy, parked workers still on at idle power (Wh, declared model) | 65.78 | 107 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 61.23 | 90.48 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 598.5 | 897.8 |
| response time (ms), 95th percentile | 2195 | 4470 |
| response time (ms), 99th percentile | 4181 | 7088 |
| time over the response line (% of samples) | 59.18 | 49.47 |
| failed requests (%) | 45.53 | 28.45 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.33 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 11.43 |
| pods with no machine to take them (unschedulable) | 2.333 | 17 |
| time pods had no machine to take them, pod-minutes | 2.978 | 22.62 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.589 | 31.39 |
| utilisation (used / allocatable) | 0.7322 | 0.6391 |
| CPU used (cores), mean | 2.277 | 3.254 |
| Omni's own CPU (cores), mean | 0 | 0.01537 |
| CPU used with Omni's own (cores), mean | 2.277 | 3.27 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 158.8 | 165.4 |
| HPA replicas, mean | 8.636 | 20.03 |
| pods started | 7.333 | 22.33 |
| pod start wait, total (s) | 225.7 | 1671 |
| pod start wait, mean (s) | 33.33 | 73.6 |
| machines billed, machine-hours | 0.4504 | 0.6069 |
| compute bill at list price ($) | 0.04324 | 0.05826 |

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
| worker nodes in service, mean | 1.641 | 2.687 | +63.7% | +0.5352 to +1.557 | yes: power given |
| node-hours | 0.2781 | 0.4516 | +62.4% | +0.09175 to +0.2553 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 65.78 | 107 | +62.7% | +37.81 to +44.68 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 61.23 | 90.48 | +47.8% | +22.73 to +35.76 | yes: power given |
| response time (ms), mean | 598.5 | 897.8 | +50.0% | -638.8 to +1237 | no |
| response time (ms), 95th percentile | 2195 | 4470 | +103.6% | -5512 to +1.006e+04 | no |
| response time (ms), 99th percentile | 4181 | 7088 | +69.5% | -6758 to +1.257e+04 | no |
| time over the response line (% of samples) | 59.18 | 49.47 | -16.4% | -31.88 to +12.45 | no |
| failed requests (%) | 45.53 | 28.45 | -37.5% | -41.87 to +7.711 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.33 | +22.3 (native is 0) | +10.86 to +33.81 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.333 | 17 | +628.6% | -3.98 to +33.31 | no |
| time pods had no machine to take them, pod-minutes | 2.978 | 22.62 | +659.7% | -10.73 to +50.02 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.589 | 31.39 | +376.4% | -9.235 to +58.84 | no |
| utilisation (used / allocatable) | 0.7322 | 0.6391 | -12.7% | -0.2666 to +0.08043 | no |
| CPU used (cores), mean | 2.277 | 3.254 | +42.9% | +0.8944 to +1.06 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01537 | +0.0154 (native is 0) | +0.01302 to +0.01771 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.277 | 3.27 | +43.6% | +0.9116 to +1.074 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 158.8 | 165.4 | +4.2% | -12.89 to +26.23 | no |
| HPA replicas, mean | 8.636 | 20.03 | +132.0% | +5.789 to +17 | yes: power given |
| pods started | 7.333 | 22.33 | +204.5% | +8.427 to +21.57 | yes: power given |
| pod start wait, total (s) | 225.7 | 1671 | +640.5% | -518 to +3409 | no |
| pod start wait, mean (s) | 33.33 | 73.6 | +120.8% | -58.04 to +138.6 | no |
| machines billed, machine-hours | 0.4504 | 0.6069 | +34.7% | -0.0001704 to +0.3131 | no |
| compute bill at list price ($) | 0.04324 | 0.05826 | +34.7% | -1.635e-05 to +0.03006 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*