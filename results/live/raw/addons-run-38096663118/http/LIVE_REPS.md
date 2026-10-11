# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.534 |
| node-hours | 1.515 | 1.391 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.2 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.2 | 150.6 |
| response time (ms), mean | 144.1 | 59.04 |
| response time (ms), 95th percentile | 351.2 | 84.65 |
| response time (ms), 99th percentile | 470.6 | 131.2 |
| time over the response line (% of samples) | 1.278 | 0.04783 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3933 | 0.3467 |
| utilisation (used / allocatable) | 0.02842 | 0.04489 |
| CPU used (cores), mean | 0.6821 | 0.9911 |
| Omni's own CPU (cores), mean | 0 | 0.00912 |
| CPU used with Omni's own (cores), mean | 0.6821 | 1 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 916 | 612.1 |
| HPA replicas, mean | 2.7 | 2.311 |
| pods started | 2.5 | 2.2 |
| pod start wait, total (s) | 19.3 | 18.1 |
| pod start wait, mean (s) | 7.7 | 8.183 |
| host CPU busy, the real machine under kind (%) | 21.6 | 30.6 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.534 | -7.8% | -0.6847 to -0.2467 | yes, better |
| node-hours | 1.515 | 1.391 | -8.2% | -0.1786 to -0.07112 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 157.2 | 159.4 | +1.4% | +0.806 to +3.547 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.2 | 150.6 | -4.2% | -10.87 to -2.355 | yes, better |
| response time (ms), mean | 144.1 | 59.04 | -59.0% | -106.2 to -63.92 | yes, better |
| response time (ms), 95th percentile | 351.2 | 84.66 | -75.9% | -312.5 to -220.6 | yes, better |
| response time (ms), 99th percentile | 470.6 | 131.2 | -72.1% | -382.6 to -296.2 | yes, better |
| time over the response line (% of samples) | 1.278 | 0.04783 | -96.3% | -2.368 to -0.09288 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3933 | 0.3467 | -11.9% | -0.3371 to +0.2438 | no |
| utilisation (used / allocatable) | 0.02842 | 0.04489 | +58.0% | +0.0134 to +0.01955 | yes, more |
| CPU used (cores), mean | 0.6821 | 0.9911 | +45.3% | +0.2438 to +0.3743 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.00912 | +0.00912 (native is 0) | +0.008026 to +0.01021 | yes, more |
| CPU used with Omni's own (cores), mean | 0.6821 | 1 | +46.6% | +0.2524 to +0.3839 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 916 | 612.1 | -33.2% | -325.9 to -281.8 | yes, less |
| HPA replicas, mean | 2.7 | 2.311 | -14.4% | -0.6451 to -0.1327 | yes, better |
| pods started | 2.5 | 2.2 | -12.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 19.3 | 18.1 | -6.2% | -5.671 to +3.271 | no |
| pod start wait, mean (s) | 7.7 | 8.183 | +6.3% | -0.6469 to +1.614 | no |
| host CPU busy, the real machine under kind (%) | 21.6 | 30.6 | +41.6% | +7.477 to +10.51 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*