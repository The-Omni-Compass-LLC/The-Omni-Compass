# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.813 | 1.92 |
| node-hours | 0.4567 | 0.4846 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.65 | 93.77 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.11 | 84.69 |
| response time (ms), mean | 516 | 515.7 |
| response time (ms), 95th percentile | 1336 | 1178 |
| response time (ms), 99th percentile | 4154 | 4455 |
| time over the response line (% of samples) | 29.6 | 30.34 |
| failed requests (%) | 4.373 | 4.812 |
| pods with no machine to take them (unschedulable) | 2.4 | 2.6 |
| time pods had no machine to take them, pod-minutes | 3.423 | 3.277 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.567 | 6.713 |
| utilisation (used / allocatable) | 0.4983 | 0.484 |
| CPU used (cores), mean | 1.715 | 1.755 |
| Omni's own CPU (cores), mean | 0 | 0.01362 |
| CPU used with Omni's own (cores), mean | 1.715 | 1.769 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 190.2 | 192 |
| HPA replicas, mean | 9.357 | 9.488 |
| pods started | 5.4 | 4.2 |
| pod start wait, total (s) | 243.4 | 220.2 |
| pod start wait, mean (s) | 45.92 | 42.32 |
| machines billed, machine-hours | 0.5733 | 0.6254 |
| compute bill at list price ($) | 0.05504 | 0.06004 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 5 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.813 | 1.92 | +5.9% | -0.05529 to +0.2704 | no |
| node-hours | 0.4567 | 0.4846 | +6.1% | -0.01435 to +0.07013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.65 | 93.77 | +9.5% | -4.641 to +20.9 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.11 | 84.69 | +3.1% | -0.7226 to +5.877 | no |
| response time (ms), mean | 516 | 515.7 | -0.1% | -132.2 to +131.5 | no |
| response time (ms), 95th percentile | 1336 | 1178 | -11.8% | -978.1 to +662.2 | no |
| response time (ms), 99th percentile | 4154 | 4455 | +7.2% | -2147 to +2749 | no |
| time over the response line (% of samples) | 29.6 | 30.34 | +2.5% | -6.062 to +7.528 | no |
| failed requests (%) | 4.373 | 4.812 | +10.1% | -1.424 to +2.303 | no |
| pods with no machine to take them (unschedulable) | 2.4 | 2.6 | +8.3% | -1.641 to +2.041 | no |
| time pods had no machine to take them, pod-minutes | 3.423 | 3.277 | -4.3% | -2.647 to +2.353 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.567 | 6.713 | +2.2% | -1.938 to +2.231 | no |
| utilisation (used / allocatable) | 0.4983 | 0.484 | -2.9% | -0.07239 to +0.0439 | no |
| CPU used (cores), mean | 1.715 | 1.755 | +2.3% | -0.08662 to +0.1664 | no |
| Omni's own CPU (cores), mean | 0 | 0.01362 | +0.0136 (native is 0) | +0.0123 to +0.01494 | yes, more |
| CPU used with Omni's own (cores), mean | 1.715 | 1.769 | +3.1% | -0.07356 to +0.1806 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 190.2 | 192 | +0.9% | -11.33 to +14.87 | no |
| HPA replicas, mean | 9.357 | 9.488 | +1.4% | -0.2331 to +0.496 | no |
| pods started | 5.4 | 4.2 | -22.2% | -4.031 to +1.631 | no |
| pod start wait, total (s) | 243.4 | 220.2 | -9.5% | -243.3 to +196.9 | no |
| pod start wait, mean (s) | 45.92 | 42.32 | -7.8% | -50.15 to +42.95 | no |
| machines billed, machine-hours | 0.5733 | 0.6254 | +9.1% | -0.04102 to +0.1452 | no |
| compute bill at list price ($) | 0.05504 | 0.06004 | +9.1% | -0.003938 to +0.01394 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*