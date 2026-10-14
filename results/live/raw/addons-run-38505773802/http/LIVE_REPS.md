# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 194.2 | 82.16 |
| response time (ms), 95th percentile | 462.1 | 128.7 |
| response time (ms), 99th percentile | 638.9 | 195.7 |
| time over the response line (% of samples) | 4.513 | 0.2311 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4 | 0.3317 |
| utilisation (used / allocatable) | 0.03191 | 0.04767 |
| CPU used (cores), mean | 0.7658 | 1.144 |
| Omni's own CPU (cores), mean | 0 | 0.00966 |
| CPU used with Omni's own (cores), mean | 0.7658 | 1.154 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.2 | 569.3 |
| HPA replicas, mean | 2.998 | 2.46 |
| pods started | 3 | 2.3 |
| pod start wait, total (s) | 24.9 | 23.4 |
| pod start wait, mean (s) | 8.342 | 10.2 |
| host CPU busy, the real machine under kind (%) | 24.07 | 34.99 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.363e-16 to +8.692e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.513 | -0.4% | -0.01032 to -0.0003445 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 161.3 | +1.9% | +2.156 to +3.952 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 161.3 | +1.9% | +2.156 to +3.952 | yes: power given |
| response time (ms), mean | 194.2 | 82.16 | -57.7% | -137.4 to -86.58 | yes: GAIN |
| response time (ms), 95th percentile | 462.1 | 128.7 | -72.2% | -390.6 to -276.3 | yes: GAIN |
| response time (ms), 99th percentile | 638.9 | 195.7 | -69.4% | -525.5 to -360.9 | yes: GAIN |
| time over the response line (% of samples) | 4.513 | 0.2311 | -94.9% | -6.358 to -2.207 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4 | 0.3317 | -17.1% | -0.2076 to +0.07098 | no |
| utilisation (used / allocatable) | 0.03191 | 0.04767 | +49.4% | +0.01277 to +0.01875 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7658 | 1.144 | +49.4% | +0.3064 to +0.4499 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00966 | +0.00966 (native is 0) | +0.008419 to +0.0109 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7658 | 1.154 | +50.6% | +0.3148 to +0.4608 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.2 | 569.3 | -30.7% | -271.9 to -231.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.998 | 2.46 | -17.9% | -0.717 to -0.3583 | yes: GAIN |
| pods started | 3 | 2.3 | -23.3% | -1.183 to -0.2172 | yes: GAIN |
| pod start wait, total (s) | 24.9 | 23.4 | -6.0% | -5.619 to +2.619 | no |
| pod start wait, mean (s) | 8.342 | 10.2 | +22.3% | +1.224 to +2.493 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 24.07 | 34.99 | +45.4% | +8.72 to +13.11 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*