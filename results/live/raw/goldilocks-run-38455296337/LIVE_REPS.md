# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 148.9 | 80.01 |
| response time (ms), 95th percentile | 310.7 | 118.9 |
| response time (ms), 99th percentile | 449.5 | 142.3 |
| time over the response line (% of samples) | 0.9213 | 0.0122 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05 |
| utilisation (used / allocatable) | 0.03367 | 0.04808 |
| CPU used (cores), mean | 0.808 | 1.154 |
| Omni's own CPU (cores), mean | 0 | 0.00799 |
| CPU used with Omni's own (cores), mean | 0.808 | 1.162 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777 | 562 |
| HPA replicas, mean | 9.744 | 9.884 |
| pods started | 2.4 | 0.8 |
| pod start wait, total (s) | 4.1 | 1.2 |
| pod start wait, mean (s) | 1.208 | 0.4667 |
| host CPU busy, the real machine under kind (%) | 24.64 | 34.2 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.702e-16 to +1.003e-15 | same (under one part in a million) |
| node-hours | 1.515 | 1.513 | -0.1% | -0.009096 to +0.006762 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.2 | +2.0% | +2.392 to +3.881 | yes, higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.2 | +2.0% | +2.392 to +3.881 | yes, higher |
| response time (ms), mean | 148.9 | 80.01 | -46.3% | -89.5 to -48.3 | yes, lower |
| response time (ms), 95th percentile | 310.7 | 118.9 | -61.7% | -233.3 to -150.2 | yes, lower |
| response time (ms), 99th percentile | 449.5 | 142.3 | -68.3% | -369.6 to -244.8 | yes, lower |
| time over the response line (% of samples) | 0.9213 | 0.0122 | -98.7% | -1.586 to -0.2319 | yes, lower |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05 | +87.5% | -0.03376 to +0.08043 | no |
| utilisation (used / allocatable) | 0.03367 | 0.04808 | +42.8% | +0.01097 to +0.01785 | yes, higher |
| CPU used (cores), mean | 0.808 | 1.154 | +42.8% | +0.2633 to +0.4284 | yes, higher |
| Omni's own CPU (cores), mean | 0 | 0.00799 | +0.00799 (native is 0) | +0.007133 to +0.008847 | yes, higher |
| CPU used with Omni's own (cores), mean | 0.808 | 1.162 | +43.8% | +0.2707 to +0.4371 | yes, higher |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777 | 562 | -27.7% | -248.3 to -181.8 | yes, lower |
| HPA replicas, mean | 9.744 | 9.884 | +1.4% | -0.08528 to +0.3663 | no |
| pods started | 2.4 | 0.8 | -66.7% | -3.116 to -0.08448 | yes, lower |
| pod start wait, total (s) | 4.1 | 1.2 | -70.7% | -5.868 to +0.06754 | no |
| pod start wait, mean (s) | 1.208 | 0.4667 | -61.4% | -1.715 to +0.2319 | no |
| host CPU busy, the real machine under kind (%) | 24.64 | 34.2 | +38.8% | +7.442 to +11.69 | yes, higher |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*