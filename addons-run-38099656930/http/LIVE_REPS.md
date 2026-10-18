# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.543 |
| node-hours | 1.519 | 1.395 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 152.1 |
| response time (ms), mean | 196.8 | 80.18 |
| response time (ms), 95th percentile | 465.7 | 124.6 |
| response time (ms), 99th percentile | 652.9 | 196.7 |
| time over the response line (% of samples) | 4.539 | 0.1699 |
| failed requests (%) | 0 | 0.01227 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.3267 |
| utilisation (used / allocatable) | 0.03062 | 0.05033 |
| CPU used (cores), mean | 0.735 | 1.117 |
| Omni's own CPU (cores), mean | 0 | 0.01096 |
| CPU used with Omni's own (cores), mean | 0.735 | 1.128 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.7 | 549.5 |
| HPA replicas, mean | 2.836 | 2.426 |
| pods started | 2.8 | 2.4 |
| pod start wait, total (s) | 23.4 | 22.4 |
| pod start wait, mean (s) | 8.35 | 9.333 |
| host CPU busy, the real machine under kind (%) | 23.23 | 34.56 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.543 | -7.6% | -0.6833 to -0.23 | yes, better |
| node-hours | 1.519 | 1.395 | -8.2% | -0.1829 to -0.06662 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 160.7 | +1.7% | +1.72 to +3.651 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 152.1 | -3.7% | -10.72 to -1.123 | yes, better |
| response time (ms), mean | 196.8 | 80.18 | -59.3% | -141.4 to -91.89 | yes, better |
| response time (ms), 95th percentile | 465.7 | 124.6 | -73.2% | -403.3 to -279 | yes, better |
| response time (ms), 99th percentile | 652.9 | 196.7 | -69.9% | -545.2 to -367.1 | yes, better |
| time over the response line (% of samples) | 4.539 | 0.1699 | -96.3% | -6.616 to -2.122 | yes, better |
| failed requests (%) | 0 | 0.01227 | +0.0123 (native is 0) | -0.01548 to +0.04002 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.3267 | -4.4% | -0.2433 to +0.2133 | no |
| utilisation (used / allocatable) | 0.03062 | 0.05033 | +64.3% | +0.01689 to +0.02252 | yes, more |
| CPU used (cores), mean | 0.735 | 1.117 | +52.0% | +0.3131 to +0.4516 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01096 | +0.011 (native is 0) | +0.009652 to +0.01227 | yes, more |
| CPU used with Omni's own (cores), mean | 0.735 | 1.128 | +53.5% | +0.3233 to +0.4634 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 854.7 | 549.5 | -35.7% | -323.6 to -286.9 | yes, less |
| HPA replicas, mean | 2.836 | 2.426 | -14.5% | -0.5477 to -0.2736 | yes, better |
| pods started | 2.8 | 2.4 | -14.3% | -0.9001 to +0.1001 | no |
| pod start wait, total (s) | 23.4 | 22.4 | -4.3% | -5.239 to +3.239 | no |
| pod start wait, mean (s) | 8.35 | 9.333 | +11.8% | -0.04137 to +2.008 | no |
| host CPU busy, the real machine under kind (%) | 23.23 | 34.56 | +48.8% | +9.312 to +13.35 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*