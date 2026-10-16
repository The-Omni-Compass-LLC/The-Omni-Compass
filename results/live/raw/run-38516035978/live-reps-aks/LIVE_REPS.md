# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.795 | 1.793 |
| node-hours | 0.4527 | 0.4516 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.5 | 84.59 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.62 | 80.68 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 549.2 | 563.3 |
| response time (ms), 95th percentile | 1281 | 1415 |
| response time (ms), 99th percentile | 5657 | 5832 |
| time over the response line (% of samples) | 31.37 | 30.44 |
| failed requests (%) | 5.613 | 4.621 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 13.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 8.571 |
| pods with no machine to take them (unschedulable) | 1.8 | 3.2 |
| time pods had no machine to take them, pod-minutes | 10.15 | 4.777 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.943 | 8.5 |
| utilisation (used / allocatable) | 0.4987 | 0.5011 |
| CPU used (cores), mean | 1.7 | 1.707 |
| Omni's own CPU (cores), mean | 0 | 0.00586 |
| CPU used with Omni's own (cores), mean | 1.7 | 1.713 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 190.4 | 187.7 |
| HPA replicas, mean | 9.361 | 9.4 |
| pods started | 4.6 | 5.2 |
| pod start wait, total (s) | 631.8 | 336.2 |
| pod start wait, mean (s) | 120.3 | 64.41 |
| machines billed, machine-hours | 0.583 | 0.5727 |
| compute bill at list price ($) | 0.05597 | 0.05498 |

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
| worker nodes in service, mean | 1.795 | 1.793 | -0.1% | -0.04299 to +0.03902 | no |
| node-hours | 0.4527 | 0.4516 | -0.3% | -0.01083 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.5 | 84.59 | -1.1% | -1.709 to -0.1043 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.62 | 80.68 | -1.1% | -1.89 to +0.01842 | no |
| response time (ms), mean | 549.2 | 563.3 | +2.6% | -30.79 to +59.06 | no |
| response time (ms), 95th percentile | 1281 | 1415 | +10.5% | -332.8 to +601.7 | no |
| response time (ms), 99th percentile | 5657 | 5832 | +3.1% | -1792 to +2142 | no |
| time over the response line (% of samples) | 31.37 | 30.44 | -3.0% | -3.15 to +1.291 | no |
| failed requests (%) | 5.613 | 4.621 | -17.7% | -3.033 to +1.048 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 13.8 | +0.0% | -1.963 to +1.963 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.4 | +24.4 (native is 0) | +20.42 to +28.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 1.8 | 3.2 | +77.8% | -0.4828 to +3.283 | no |
| time pods had no machine to take them, pod-minutes | 10.15 | 4.777 | -52.9% | -26.41 to +15.66 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.943 | 8.5 | +7.0% | -1.112 to +2.225 | no |
| utilisation (used / allocatable) | 0.4987 | 0.5011 | +0.5% | -0.01565 to +0.02035 | no |
| CPU used (cores), mean | 1.7 | 1.707 | +0.4% | -0.05166 to +0.06512 | no |
| Omni's own CPU (cores), mean | 0 | 0.00586 | +0.00586 (native is 0) | +0.004604 to +0.007116 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.7 | 1.713 | +0.7% | -0.04584 to +0.07103 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 190.4 | 187.7 | -1.4% | -8.345 to +2.989 | no |
| HPA replicas, mean | 9.361 | 9.4 | +0.4% | -0.1424 to +0.2201 | no |
| pods started | 4.6 | 5.2 | +13.0% | -3.384 to +4.584 | no |
| pod start wait, total (s) | 631.8 | 336.2 | -46.8% | -1549 to +957.4 | no |
| pod start wait, mean (s) | 120.3 | 64.41 | -46.5% | -317.2 to +205.3 | no |
| machines billed, machine-hours | 0.583 | 0.5727 | -1.8% | -0.01908 to -0.001587 | yes: GAIN |
| compute bill at list price ($) | 0.05597 | 0.05498 | -1.8% | -0.001832 to -0.0001524 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*