# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.888 | 1.884 |
| node-hours | 0.9482 | 0.9489 |
| energy, parked workers still on at idle power (Wh, declared model) | 204.9 | 205.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 200.7 | 200.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 467.5 | 422.3 |
| response time (ms), 95th percentile | 801.6 | 812.8 |
| response time (ms), 99th percentile | 4431 | 2594 |
| time over the response line (% of samples) | 50.97 | 45.04 |
| failed requests (%) | 40.5 | 33.85 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.8 | 29.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 28.21 |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 |
| time pods had no machine to take them, pod-minutes | 4.37 | 2.913 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.293 | 7.46 |
| utilisation (used / allocatable) | 0.7403 | 0.7465 |
| CPU used (cores), mean | 2.656 | 2.673 |
| Omni's own CPU (cores), mean | 0 | 0.004 |
| CPU used with Omni's own (cores), mean | 2.656 | 2.677 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 150.5 | 149.4 |
| HPA replicas, mean | 9.614 | 9.471 |
| pods started | 5.4 | 3.8 |
| pod start wait, total (s) | 316.8 | 211.8 |
| pod start wait, mean (s) | 58.53 | 42.9 |
| machines billed, machine-hours | 1.101 | 1.145 |
| compute bill at list price ($) | 0.1057 | 0.1099 |

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
| worker nodes in service, mean | 1.888 | 1.884 | -0.2% | -0.1117 to +0.1042 | no |
| node-hours | 0.9482 | 0.9489 | +0.1% | -0.05196 to +0.05329 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 204.9 | 205.3 | +0.2% | -7.365 to +8.063 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 200.7 | 200.9 | +0.1% | -10.92 to +11.31 | no |
| response time (ms), mean | 467.5 | 422.3 | -9.7% | -112.7 to +22.33 | no |
| response time (ms), 95th percentile | 801.6 | 812.8 | +1.4% | -161.6 to +184.1 | no |
| response time (ms), 99th percentile | 4431 | 2594 | -41.5% | -5217 to +1544 | no |
| time over the response line (% of samples) | 50.97 | 45.04 | -11.6% | -16.4 to +4.548 | no |
| failed requests (%) | 40.5 | 33.85 | -16.4% | -16.78 to +3.488 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29.8 | 29.6 | -0.7% | -0.7552 to +0.3552 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.8 | +37.8 (native is 0) | +35.11 to +40.49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.6 | 1.8 | -30.8% | -2.84 to +1.24 | no |
| time pods had no machine to take them, pod-minutes | 4.37 | 2.913 | -33.3% | -4.854 to +1.941 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.293 | 7.46 | -19.7% | -9.514 to +5.848 | no |
| utilisation (used / allocatable) | 0.7403 | 0.7465 | +0.8% | -0.02896 to +0.0413 | no |
| CPU used (cores), mean | 2.656 | 2.673 | +0.7% | -0.2008 to +0.2358 | no |
| Omni's own CPU (cores), mean | 0 | 0.004 | +0.004 (native is 0) | +0.002932 to +0.005068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.656 | 2.677 | +0.8% | -0.1971 to +0.2401 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 150.5 | 149.4 | -0.8% | -4.913 to +2.645 | no |
| HPA replicas, mean | 9.614 | 9.471 | -1.5% | -0.5098 to +0.2246 | no |
| pods started | 5.4 | 3.8 | -29.6% | -3.266 to +0.0656 | no |
| pod start wait, total (s) | 316.8 | 211.8 | -33.1% | -350.7 to +140.7 | no |
| pod start wait, mean (s) | 58.53 | 42.9 | -26.7% | -68.18 to +36.92 | no |
| machines billed, machine-hours | 1.101 | 1.145 | +4.0% | -0.03216 to +0.1202 | no |
| compute bill at list price ($) | 0.1057 | 0.1099 | +4.0% | -0.003087 to +0.01154 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*