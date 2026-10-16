# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.923 | 1.838 |
| node-hours | 0.4827 | 0.4629 |
| energy, parked workers still on at idle power (Wh, declared model) | 88.6 | 85.79 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.39 | 82.74 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 500.4 | 535.6 |
| response time (ms), 95th percentile | 1178 | 1369 |
| response time (ms), 99th percentile | 3147 | 4055 |
| time over the response line (% of samples) | 29.57 | 31.21 |
| failed requests (%) | 3.731 | 4.425 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 14.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 5.714 |
| pods with no machine to take them (unschedulable) | 1.8 | 2 |
| time pods had no machine to take them, pod-minutes | 2.15 | 2.11 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.647 | 5.203 |
| utilisation (used / allocatable) | 0.4673 | 0.4984 |
| CPU used (cores), mean | 1.684 | 1.74 |
| Omni's own CPU (cores), mean | 0 | 0.00514 |
| CPU used with Omni's own (cores), mean | 1.684 | 1.745 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 198.3 | 189.1 |
| HPA replicas, mean | 9.39 | 9.385 |
| pods started | 4.6 | 4.4 |
| pod start wait, total (s) | 157.6 | 160.8 |
| pod start wait, mean (s) | 31.28 | 29.74 |
| machines billed, machine-hours | 0.5992 | 0.5603 |
| compute bill at list price ($) | 0.05753 | 0.05379 |

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
| worker nodes in service, mean | 1.923 | 1.838 | -4.4% | -0.3624 to +0.1924 | no |
| node-hours | 0.4827 | 0.4629 | -4.1% | -0.08939 to +0.04973 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 88.6 | 85.79 | -3.2% | -14.32 to +8.694 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.39 | 82.74 | -0.8% | -7.078 to +5.766 | no |
| response time (ms), mean | 500.4 | 535.6 | +7.0% | -76.33 to +146.8 | no |
| response time (ms), 95th percentile | 1178 | 1369 | +16.2% | -159.4 to +541.7 | no |
| response time (ms), 99th percentile | 3147 | 4055 | +28.9% | -1996 to +3812 | no |
| time over the response line (% of samples) | 29.57 | 31.21 | +5.5% | -1.985 to +5.264 | no |
| failed requests (%) | 3.731 | 4.425 | +18.6% | -1.929 to +3.318 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 14.6 | +1.4% | -0.3552 to +0.7552 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.6 | +25.6 (native is 0) | +22.25 to +28.95 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 1.8 | 2 | +11.1% | -1.84 to +2.24 | no |
| time pods had no machine to take them, pod-minutes | 2.15 | 2.11 | -1.9% | -2.543 to +2.463 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 4.647 | 5.203 | +12.0% | -3.641 to +4.754 | no |
| utilisation (used / allocatable) | 0.4673 | 0.4984 | +6.7% | -0.04517 to +0.1074 | no |
| CPU used (cores), mean | 1.684 | 1.74 | +3.3% | -0.04963 to +0.1618 | no |
| Omni's own CPU (cores), mean | 0 | 0.00514 | +0.00514 (native is 0) | +0.004196 to +0.006084 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.684 | 1.745 | +3.6% | -0.04517 to +0.1676 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 198.3 | 189.1 | -4.6% | -34.71 to +16.37 | no |
| HPA replicas, mean | 9.39 | 9.385 | -0.1% | -0.194 to +0.1844 | no |
| pods started | 4.6 | 4.4 | -4.3% | -2.24 to +1.84 | no |
| pod start wait, total (s) | 157.6 | 160.8 | +2.0% | -169.3 to +175.7 | no |
| pod start wait, mean (s) | 31.28 | 29.74 | -4.9% | -38.99 to +35.91 | no |
| machines billed, machine-hours | 0.5992 | 0.5603 | -6.5% | -0.1171 to +0.03925 | no |
| compute bill at list price ($) | 0.05753 | 0.05379 | -6.5% | -0.01125 to +0.003768 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*