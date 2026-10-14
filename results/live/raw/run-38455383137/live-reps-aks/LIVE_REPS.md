# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.805 | 2.971 |
| node-hours | 0.4538 | 0.7517 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.25 | 129.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.58 | 110.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 505 | 322.7 |
| response time (ms), 95th percentile | 1120 | 725.5 |
| response time (ms), 99th percentile | 4196 | 1257 |
| time over the response line (% of samples) | 30 | 13.9 |
| failed requests (%) | 5.106 | 0.9023 |
| pods with no machine to take them (unschedulable) | 2.8 | 11.25 |
| time pods had no machine to take them, pod-minutes | 10.95 | 13.75 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.377 | 29.65 |
| utilisation (used / allocatable) | 0.502 | 0.2923 |
| CPU used (cores), mean | 1.721 | 1.646 |
| Omni's own CPU (cores), mean | 0 | 0.01405 |
| CPU used with Omni's own (cores), mean | 1.721 | 1.66 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 188.5 | 265.1 |
| HPA replicas, mean | 9.454 | 19.65 |
| pods started | 5.8 | 16.75 |
| pod start wait, total (s) | 697.2 | 994.2 |
| pod start wait, mean (s) | 96.47 | 60.03 |
| machines billed, machine-hours | 0.5765 | 0.8804 |
| compute bill at list price ($) | 0.05534 | 0.08452 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 4 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.797 | 2.971 | +65.4% | +0.9815 to +1.367 | yes, higher |
| node-hours | 0.4506 | 0.7517 | +66.8% | +0.2503 to +0.3519 | yes, higher |
| energy, parked workers still on at idle power (Wh, declared model) | 85.56 | 129.7 | +51.6% | +42.81 to +45.42 | yes, higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 81.75 | 110.2 | +34.8% | +24.13 to +32.71 | yes, higher |
| response time (ms), mean | 493.1 | 322.7 | -34.6% | -221.7 to -119.2 | yes, lower |
| response time (ms), 95th percentile | 1099 | 725.5 | -34.0% | -526.4 to -219.8 | yes, lower |
| response time (ms), 99th percentile | 4446 | 1257 | -71.7% | -5269 to -1109 | yes, lower |
| time over the response line (% of samples) | 29.31 | 13.9 | -52.6% | -18.23 to -12.6 | yes, lower |
| failed requests (%) | 5.425 | 0.9023 | -83.4% | -6.335 to -2.711 | yes, lower |
| pods with no machine to take them (unschedulable) | 2.75 | 11.25 | +309.1% | -1.77 to +18.77 | no |
| time pods had no machine to take them, pod-minutes | 12.95 | 13.75 | +6.2% | -38.99 to +40.6 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.625 | 29.65 | +288.8% | +11.05 to +32.99 | yes, higher |
| utilisation (used / allocatable) | 0.5068 | 0.2923 | -42.3% | -0.2525 to -0.1765 | yes, lower |
| CPU used (cores), mean | 1.73 | 1.646 | -4.9% | -0.1942 to +0.02578 | no |
| Omni's own CPU (cores), mean | 0 | 0.01405 | +0.014 (native is 0) | +0.01053 to +0.01757 | yes, higher |
| CPU used with Omni's own (cores), mean | 1.73 | 1.66 | -4.1% | -0.1786 to +0.03833 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 188.4 | 265.1 | +40.7% | +48.68 to +104.8 | yes, higher |
| HPA replicas, mean | 9.424 | 19.65 | +108.5% | +8.64 to +11.82 | yes, higher |
| pods started | 6 | 16.75 | +179.2% | -8.092 to +29.59 | no |
| pod start wait, total (s) | 814 | 994.2 | +22.1% | -2325 to +2685 | no |
| pod start wait, mean (s) | 109.1 | 60.03 | -45.0% | -217.1 to +119 | no |
| machines billed, machine-hours | 0.5822 | 0.8804 | +51.2% | +0.2352 to +0.3613 | yes, higher |
| compute bill at list price ($) | 0.05589 | 0.08452 | +51.2% | +0.02258 to +0.03469 | yes, higher |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*