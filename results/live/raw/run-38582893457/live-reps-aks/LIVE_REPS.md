# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.89 | 1.876 |
| node-hours | 0.9495 | 0.9432 |
| energy, parked workers still on at idle power (Wh, declared model) | 217.3 | 213.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 213.2 | 208.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 395.8 | 404.5 |
| response time (ms), 95th percentile | 699.4 | 734.2 |
| response time (ms), 99th percentile | 2946 | 2550 |
| time over the response line (% of samples) | 52.47 | 50.62 |
| failed requests (%) | 45.89 | 41.89 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.4 | 29.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 21.85 |
| pods with no machine to take them (unschedulable) | 3.2 | 2.2 |
| time pods had no machine to take them, pod-minutes | 20.95 | 3.29 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.793 | 7.33 |
| utilisation (used / allocatable) | 0.8359 | 0.8124 |
| CPU used (cores), mean | 3.001 | 2.895 |
| Omni's own CPU (cores), mean | 0 | 0.00438 |
| CPU used with Omni's own (cores), mean | 3.001 | 2.899 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 141.5 | 143.5 |
| HPA replicas, mean | 9.644 | 9.558 |
| pods started | 6.2 | 5.4 |
| pod start wait, total (s) | 1640 | 238.2 |
| pod start wait, mean (s) | 221.9 | 41.93 |
| machines billed, machine-hours | 1.1 | 1.11 |
| compute bill at list price ($) | 0.1056 | 0.1066 |

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
| worker nodes in service, mean | 1.89 | 1.876 | -0.7% | -0.09945 to +0.07295 | no |
| node-hours | 0.9495 | 0.9432 | -0.7% | -0.05126 to +0.0387 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 217.3 | 213.5 | -1.7% | -11.54 to +3.962 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 213.2 | 208.9 | -2.0% | -15.2 to +6.636 | no |
| response time (ms), mean | 395.8 | 404.5 | +2.2% | -71.23 to +88.64 | no |
| response time (ms), 95th percentile | 699.4 | 734.2 | +5.0% | -34.8 to +104.3 | no |
| response time (ms), 99th percentile | 2946 | 2550 | -13.4% | -2465 to +1673 | no |
| time over the response line (% of samples) | 52.47 | 50.62 | -3.5% | -5.202 to +1.497 | no |
| failed requests (%) | 45.89 | 41.89 | -8.7% | -6.446 to -1.539 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.4 | 29.6 | +0.7% | -0.8387 to +1.239 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | +33.2 (native is 0) | +30.66 to +35.74 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 3.2 | 2.2 | -31.2% | -3.15 to +1.15 | no |
| time pods had no machine to take them, pod-minutes | 20.95 | 3.29 | -84.3% | -61.33 to +26.01 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.793 | 7.33 | -25.2% | -5.731 to +0.8045 | no |
| utilisation (used / allocatable) | 0.8359 | 0.8124 | -2.8% | -0.05089 to +0.003885 | no |
| CPU used (cores), mean | 3.001 | 2.895 | -3.6% | -0.3376 to +0.1246 | no |
| Omni's own CPU (cores), mean | 0 | 0.00438 | +0.00438 (native is 0) | +0.003381 to +0.005379 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 3.001 | 2.899 | -3.4% | -0.3328 to +0.1284 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 141.5 | 143.5 | +1.5% | -1.714 to +5.881 | no |
| HPA replicas, mean | 9.644 | 9.558 | -0.9% | -0.4035 to +0.2318 | no |
| pods started | 6.2 | 5.4 | -12.9% | -1.839 to +0.2387 | no |
| pod start wait, total (s) | 1640 | 238.2 | -85.5% | -3915 to +1111 | no |
| pod start wait, mean (s) | 221.9 | 41.93 | -81.1% | -466.4 to +106.6 | no |
| machines billed, machine-hours | 1.1 | 1.11 | +1.0% | -0.07252 to +0.09352 | no |
| compute bill at list price ($) | 0.1056 | 0.1066 | +1.0% | -0.006962 to +0.008978 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*