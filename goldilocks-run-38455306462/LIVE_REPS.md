# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 166.1 | 84.56 |
| response time (ms), 95th percentile | 344.9 | 131.1 |
| response time (ms), 99th percentile | 513 | 151.6 |
| time over the response line (% of samples) | 1.243 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1317 |
| utilisation (used / allocatable) | 0.03297 | 0.04959 |
| CPU used (cores), mean | 0.7913 | 1.19 |
| Omni's own CPU (cores), mean | 0 | 0.00822 |
| CPU used with Omni's own (cores), mean | 0.7913 | 1.198 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.5 | 539.9 |
| HPA replicas, mean | 9.745 | 9.893 |
| pods started | 2.4 | 0.8 |
| pod start wait, total (s) | 3.1 | 1 |
| pod start wait, mean (s) | 1.383 | 0.7 |
| host CPU busy, the real machine under kind (%) | 24.07 | 35.12 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | same (under one part in a million) |
| node-hours | 1.513 | 1.511 | -0.1% | -0.008538 to +0.006205 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.6 | 161.3 | +2.3% | +2.869 to +4.452 | yes, higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.6 | 161.3 | +2.3% | +2.869 to +4.452 | yes, higher |
| response time (ms), mean | 166.1 | 84.56 | -49.1% | -92.06 to -70.98 | yes, lower |
| response time (ms), 95th percentile | 344.9 | 131.1 | -62.0% | -238.4 to -189.2 | yes, lower |
| response time (ms), 99th percentile | 513 | 151.6 | -70.5% | -418.6 to -304.3 | yes, lower |
| time over the response line (% of samples) | 1.243 | 0 | -100.0% | -1.896 to -0.5894 | yes, lower |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1317 | +0.132 (native is 0) | -0.002326 to +0.2657 | no |
| utilisation (used / allocatable) | 0.03297 | 0.04959 | +50.4% | +0.01502 to +0.01823 | yes, higher |
| CPU used (cores), mean | 0.7913 | 1.19 | +50.4% | +0.3604 to +0.4375 | yes, higher |
| Omni's own CPU (cores), mean | 0 | 0.00822 | +0.00822 (native is 0) | +0.007396 to +0.009044 | yes, higher |
| CPU used with Omni's own (cores), mean | 0.7913 | 1.198 | +51.5% | +0.3681 to +0.4463 | yes, higher |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 791.5 | 539.9 | -31.8% | -266.1 to -237.1 | yes, lower |
| HPA replicas, mean | 9.745 | 9.893 | +1.5% | +0.04743 to +0.2492 | yes, higher |
| pods started | 2.4 | 0.8 | -66.7% | -2.44 to -0.7604 | yes, lower |
| pod start wait, total (s) | 3.1 | 1 | -67.7% | -3.468 to -0.7324 | yes, lower |
| pod start wait, mean (s) | 1.383 | 0.7 | -49.4% | -1.377 to +0.01057 | no |
| host CPU busy, the real machine under kind (%) | 24.07 | 35.12 | +45.9% | +9.94 to +12.16 | yes, higher |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*