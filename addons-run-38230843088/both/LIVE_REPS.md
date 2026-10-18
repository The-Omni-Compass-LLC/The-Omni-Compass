# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 160.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 160.9 |
| response time (ms), mean | 133.4 | 78.96 |
| response time (ms), 95th percentile | 266.8 | 115.9 |
| response time (ms), 99th percentile | 395.7 | 142.1 |
| time over the response line (% of samples) | 0.4578 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2648 | 0.3259 |
| utilisation (used / allocatable) | 0.03693 | 0.04782 |
| CPU used (cores), mean | 0.8864 | 1.148 |
| Omni's own CPU (cores), mean | 0 | 0.01188 |
| CPU used with Omni's own (cores), mean | 0.8864 | 1.16 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711.1 | 561.1 |
| HPA replicas, mean | 8.833 | 9.114 |
| pods started | 4.778 | 5.222 |
| pod start wait, total (s) | 13.33 | 17.67 |
| pod start wait, mean (s) | 2.613 | 3.337 |
| host CPU busy, the real machine under kind (%) | 27.53 | 35.46 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 8 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.708e-16 to +9.395e-16 | same (under one part in a million) |
| node-hours | 1.52 | 1.51 | -0.7% | -0.01258 to -0.00742 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 160.7 | +0.9% | +0.5388 to +2.255 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 160.7 | +0.9% | +0.5388 to +2.255 | yes, worse |
| response time (ms), mean | 129.7 | 79.07 | -39.0% | -63.64 to -37.56 | yes, better |
| response time (ms), 95th percentile | 259.9 | 116.5 | -55.2% | -171.6 to -115.2 | yes, better |
| response time (ms), 99th percentile | 393.4 | 143.2 | -63.6% | -311.6 to -188.8 | yes, better |
| time over the response line (% of samples) | 0.4666 | 0 | -100.0% | -0.9968 to +0.06355 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1979 | 0.3 | +51.6% | -0.2539 to +0.4581 | no |
| utilisation (used / allocatable) | 0.03665 | 0.0477 | +30.2% | +0.008249 to +0.01386 | yes, more |
| CPU used (cores), mean | 0.8796 | 1.145 | +30.2% | +0.198 to +0.3327 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.012 | +0.012 (native is 0) | +0.01062 to +0.01338 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8796 | 1.157 | +31.5% | +0.209 to +0.3457 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.1 | 562.9 | -21.4% | -178.7 to -127.8 | yes, less |
| HPA replicas, mean | 8.836 | 9.105 | +3.0% | -0.07749 to +0.6149 | no |
| pods started | 4.625 | 5.25 | +13.5% | -0.2619 to +1.512 | no |
| pod start wait, total (s) | 12.25 | 17.38 | +41.8% | -3.874 to +14.12 | no |
| pod start wait, mean (s) | 2.481 | 3.254 | +31.2% | -0.5375 to +2.083 | no |
| host CPU busy, the real machine under kind (%) | 27.3 | 35.47 | +29.9% | +6.224 to +10.11 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*