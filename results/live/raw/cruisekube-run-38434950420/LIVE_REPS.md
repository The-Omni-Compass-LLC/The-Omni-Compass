# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.852 |
| node-hours | 1.513 | 1.476 |
| energy, parked workers still on at idle power (Wh, declared model) | 161 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161 | 158.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 76.69 | 77.5 |
| response time (ms), 95th percentile | 118.7 | 119.7 |
| response time (ms), 99th percentile | 139.4 | 136.3 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1383 |
| utilisation (used / allocatable) | 0.04727 | 0.04879 |
| CPU used (cores), mean | 1.135 | 1.137 |
| Omni's own CPU (cores), mean | 0 | 0.00915 |
| CPU used with Omni's own (cores), mean | 1.135 | 1.147 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 573 | 562.2 |
| HPA replicas, mean | 2.698 | 2.85 |
| pods started | 1.1 | 1.5 |
| pod start wait, total (s) | 2.6 | 6.1 |
| pod start wait, mean (s) | 1.85 | 2.967 |
| host CPU busy, the real machine under kind (%) | 35.15 | 35.81 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 9 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.852 | -2.5% | -0.4837 to +0.1871 | no |
| node-hours | 1.513 | 1.476 | -2.4% | -0.1195 to +0.04573 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161 | 161.5 | +0.3% | -1.016 to +1.954 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161 | 158.7 | -1.4% | -7.617 to +2.951 | no |
| response time (ms), mean | 76.69 | 77.5 | +1.1% | +0.0003059 to +1.624 | yes, higher |
| response time (ms), 95th percentile | 118.7 | 119.7 | +0.8% | -0.174 to +2.044 | no |
| response time (ms), 99th percentile | 139.4 | 136.3 | -2.3% | -11.54 to +5.17 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.1383 | +29.7% | -0.1604 to +0.2237 | no |
| utilisation (used / allocatable) | 0.04727 | 0.04879 | +3.2% | -0.001439 to +0.004478 | no |
| CPU used (cores), mean | 1.135 | 1.137 | +0.2% | -0.01771 to +0.02329 | no |
| Omni's own CPU (cores), mean | 0 | 0.00915 | +0.00915 (native is 0) | +0.007682 to +0.01062 | yes, higher |
| CPU used with Omni's own (cores), mean | 1.135 | 1.147 | +1.1% | -0.008085 to +0.03196 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 573 | 562.2 | -1.9% | -30.38 to +8.943 | no |
| HPA replicas, mean | 2.698 | 2.85 | +5.6% | -0.0658 to +0.3705 | no |
| pods started | 1.1 | 1.5 | +36.4% | -0.4396 to +1.24 | no |
| pod start wait, total (s) | 2.6 | 6.1 | +134.6% | -2.125 to +9.125 | no |
| pod start wait, mean (s) | 1.85 | 2.967 | +60.4% | -1.404 to +3.637 | no |
| host CPU busy, the real machine under kind (%) | 35.15 | 35.81 | +1.9% | +0.08803 to +1.221 | yes, higher |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*