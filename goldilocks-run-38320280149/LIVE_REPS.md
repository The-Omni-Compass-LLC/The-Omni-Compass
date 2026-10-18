# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.5 |
| response time (ms), mean | 158.3 | 83.9 |
| response time (ms), 95th percentile | 331.1 | 132.7 |
| response time (ms), 99th percentile | 476.5 | 155.8 |
| time over the response line (% of samples) | 1.228 | 0.0122 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1067 |
| utilisation (used / allocatable) | 0.03385 | 0.04895 |
| CPU used (cores), mean | 0.8124 | 1.175 |
| Omni's own CPU (cores), mean | 0 | 0.00822 |
| CPU used with Omni's own (cores), mean | 0.8124 | 1.183 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.3 | 551.5 |
| HPA replicas, mean | 9.783 | 9.95 |
| pods started | 2.1 | 0.4 |
| pod start wait, total (s) | 2.9 | 0.5 |
| pod start wait, mean (s) | 1.167 | 0.4 |
| host CPU busy, the real machine under kind (%) | 24.43 | 34.56 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.161e-16 to +1.304e-15 | same (under one part in a million) |
| node-hours | 1.513 | 1.514 | +0.1% | -0.005607 to +0.007607 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.5 | +2.3% | +2.908 to +4.226 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.5 | +2.3% | +2.908 to +4.226 | yes, worse |
| response time (ms), mean | 158.3 | 83.9 | -47.0% | -91.89 to -56.89 | yes, better |
| response time (ms), 95th percentile | 331.1 | 132.7 | -59.9% | -236.6 to -160.2 | yes, better |
| response time (ms), 99th percentile | 476.5 | 155.8 | -67.3% | -371.9 to -269.6 | yes, better |
| time over the response line (% of samples) | 1.228 | 0.0122 | -99.0% | -1.787 to -0.6439 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.1067 | +300.0% | -0.04875 to +0.2087 | no |
| utilisation (used / allocatable) | 0.03385 | 0.04895 | +44.6% | +0.01215 to +0.01806 | yes, more |
| CPU used (cores), mean | 0.8124 | 1.175 | +44.6% | +0.2915 to +0.4333 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.00822 | +0.00822 (native is 0) | +0.007432 to +0.009008 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8124 | 1.183 | +45.6% | +0.299 to +0.4423 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.3 | 551.5 | -28.7% | -251 to -192.7 | yes, less |
| HPA replicas, mean | 9.783 | 9.95 | +1.7% | +0.05042 to +0.283 | yes, worse |
| pods started | 2.1 | 0.4 | -81.0% | -2.821 to -0.5791 | yes, better |
| pod start wait, total (s) | 2.9 | 0.5 | -82.8% | -4.283 to -0.5165 | yes, better |
| pod start wait, mean (s) | 1.167 | 0.4 | -65.7% | -1.54 to +0.006362 | no |
| host CPU busy, the real machine under kind (%) | 24.43 | 34.56 | +41.4% | +8.063 to +12.19 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*