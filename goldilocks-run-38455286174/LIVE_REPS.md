# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 166.5 | 87.52 |
| response time (ms), 95th percentile | 349.4 | 140.7 |
| response time (ms), 99th percentile | 517.4 | 163.8 |
| time over the response line (% of samples) | 1.275 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1317 |
| utilisation (used / allocatable) | 0.03415 | 0.04969 |
| CPU used (cores), mean | 0.8196 | 1.193 |
| Omni's own CPU (cores), mean | 0 | 0.00877 |
| CPU used with Omni's own (cores), mean | 0.8196 | 1.201 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.6 | 539.2 |
| HPA replicas, mean | 9.781 | 9.904 |
| pods started | 2.1 | 0.8 |
| pod start wait, total (s) | 2.5 | 0.7 |
| pod start wait, mean (s) | 0.85 | 0.45 |
| host CPU busy, the real machine under kind (%) | 24.69 | 35.37 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.583e-17 to +9.84e-16 | same (under one part in a million) |
| node-hours | 1.515 | 1.512 | -0.2% | -0.01217 to +0.004834 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.3 | +2.0% | +2.32 to +3.924 | yes, higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.3 | +2.0% | +2.32 to +3.924 | yes, higher |
| response time (ms), mean | 166.5 | 87.52 | -47.4% | -91.98 to -65.92 | yes, lower |
| response time (ms), 95th percentile | 349.4 | 140.7 | -59.7% | -238.3 to -179.1 | yes, lower |
| response time (ms), 99th percentile | 517.4 | 163.8 | -68.3% | -410.2 to -297 | yes, lower |
| time over the response line (% of samples) | 1.275 | 0 | -100.0% | -2.066 to -0.4837 | yes, lower |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1317 | +0.132 (native is 0) | +0.03233 to +0.231 | yes, higher |
| utilisation (used / allocatable) | 0.03415 | 0.04969 | +45.5% | +0.01404 to +0.01704 | yes, higher |
| CPU used (cores), mean | 0.8196 | 1.193 | +45.5% | +0.3371 to +0.409 | yes, higher |
| Omni's own CPU (cores), mean | 0 | 0.00877 | +0.00877 (native is 0) | +0.00818 to +0.00936 | yes, higher |
| CPU used with Omni's own (cores), mean | 0.8196 | 1.201 | +46.6% | +0.3455 to +0.4181 | yes, higher |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.6 | 539.2 | -29.8% | -251.5 to -205.2 | yes, lower |
| HPA replicas, mean | 9.781 | 9.904 | +1.3% | -0.04396 to +0.2899 | no |
| pods started | 2.1 | 0.8 | -61.9% | -2.81 to +0.2099 | no |
| pod start wait, total (s) | 2.5 | 0.7 | -72.0% | -3.61 to +0.0096 | no |
| pod start wait, mean (s) | 0.85 | 0.45 | -47.1% | -1.091 to +0.2911 | no |
| host CPU busy, the real machine under kind (%) | 24.69 | 35.37 | +43.3% | +9.667 to +11.7 | yes, higher |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*