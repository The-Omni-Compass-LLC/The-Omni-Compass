# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 162.2 | 162 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.2 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 93.09 | 92.72 |
| response time (ms), 95th percentile | 143.1 | 140.8 |
| response time (ms), 99th percentile | 162.1 | 162.7 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.1383 |
| utilisation (used / allocatable) | 0.05207 | 0.05167 |
| CPU used (cores), mean | 1.25 | 1.24 |
| Omni's own CPU (cores), mean | 0 | 0.00957 |
| CPU used with Omni's own (cores), mean | 1.25 | 1.25 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 515.4 | 519.3 |
| HPA replicas, mean | 2.997 | 2.938 |
| pods started | 1.7 | 1.2 |
| pod start wait, total (s) | 8.6 | 5.9 |
| pod start wait, mean (s) | 4.367 | 3.75 |
| host CPU busy, the real machine under kind (%) | 38.4 | 38.85 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.718e-16 to +4.495e-16 | same (under one part in a million) |
| node-hours | 1.514 | 1.513 | -0.1% | -0.01184 to +0.008839 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 162.2 | 162 | -0.1% | -1.378 to +0.8937 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.2 | 162 | -0.1% | -1.378 to +0.8937 | no |
| response time (ms), mean | 93.09 | 92.72 | -0.4% | -1.774 to +1.042 | no |
| response time (ms), 95th percentile | 143.1 | 140.8 | -1.6% | -4.35 to -0.3047 | yes, lower |
| response time (ms), 99th percentile | 162.1 | 162.7 | +0.4% | -7.422 to +8.611 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1917 | 0.1383 | -27.8% | -0.2543 to +0.1476 | no |
| utilisation (used / allocatable) | 0.05207 | 0.05167 | -0.8% | -0.001098 to +0.000303 | no |
| CPU used (cores), mean | 1.25 | 1.24 | -0.8% | -0.02636 to +0.007272 | no |
| Omni's own CPU (cores), mean | 0 | 0.00957 | +0.00957 (native is 0) | +0.00882 to +0.01032 | yes, higher |
| CPU used with Omni's own (cores), mean | 1.25 | 1.25 | +0.0% | -0.01699 to +0.01704 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 515.4 | 519.3 | +0.8% | -2.785 to +10.66 | no |
| HPA replicas, mean | 2.997 | 2.938 | -2.0% | -0.2421 to +0.1245 | no |
| pods started | 1.7 | 1.2 | -29.4% | -1.108 to +0.1079 | no |
| pod start wait, total (s) | 8.6 | 5.9 | -31.4% | -6.205 to +0.8051 | no |
| pod start wait, mean (s) | 4.367 | 3.75 | -14.1% | -2.904 to +1.671 | no |
| host CPU busy, the real machine under kind (%) | 38.4 | 38.85 | +1.2% | +0.1826 to +0.7197 | yes, higher |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*