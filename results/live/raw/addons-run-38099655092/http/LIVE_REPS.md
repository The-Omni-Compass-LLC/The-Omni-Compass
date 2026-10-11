# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.646 |
| node-hours | 1.515 | 1.427 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 162 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 155.3 |
| response time (ms), mean | 213.8 | 88.23 |
| response time (ms), 95th percentile | 488.1 | 133.6 |
| response time (ms), 99th percentile | 668.1 | 196.2 |
| time over the response line (% of samples) | 4.809 | 0.146 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.3783 |
| utilisation (used / allocatable) | 0.03176 | 0.05224 |
| CPU used (cores), mean | 0.7622 | 1.177 |
| Omni's own CPU (cores), mean | 0 | 0.01235 |
| CPU used with Omni's own (cores), mean | 0.7622 | 1.189 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.4 | 524.1 |
| HPA replicas, mean | 2.961 | 2.556 |
| pods started | 2.9 | 2.5 |
| pod start wait, total (s) | 25.3 | 24.1 |
| pod start wait, mean (s) | 8.733 | 9.758 |
| host CPU busy, the real machine under kind (%) | 24.07 | 36.14 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.646 | -5.9% | -0.58 to -0.1272 | yes, better |
| node-hours | 1.515 | 1.427 | -5.8% | -0.1468 to -0.02946 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 162 | +2.6% | +3.514 to +4.687 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 155.3 | -1.6% | -6.971 to +1.775 | no |
| response time (ms), mean | 213.8 | 88.23 | -58.7% | -139 to -112.1 | yes, better |
| response time (ms), 95th percentile | 488.1 | 133.6 | -72.6% | -389.4 to -319.7 | yes, better |
| response time (ms), 99th percentile | 668.1 | 196.2 | -70.6% | -518.3 to -425.6 | yes, better |
| time over the response line (% of samples) | 4.809 | 0.146 | -97.0% | -6.324 to -3.001 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.3783 | +19.5% | -0.1345 to +0.2578 | no |
| utilisation (used / allocatable) | 0.03176 | 0.05224 | +64.5% | +0.01758 to +0.02339 | yes, more |
| CPU used (cores), mean | 0.7622 | 1.177 | +54.4% | +0.3751 to +0.4535 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01235 | +0.0123 (native is 0) | +0.0112 to +0.0135 | yes, more |
| CPU used with Omni's own (cores), mean | 0.7622 | 1.189 | +56.0% | +0.3875 to +0.4658 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 821.4 | 524.1 | -36.2% | -322.8 to -271.8 | yes, less |
| HPA replicas, mean | 2.961 | 2.556 | -13.7% | -0.6924 to -0.118 | yes, better |
| pods started | 2.9 | 2.5 | -13.8% | -1.003 to +0.2032 | no |
| pod start wait, total (s) | 25.3 | 24.1 | -4.7% | -7.452 to +5.052 | no |
| pod start wait, mean (s) | 8.733 | 9.758 | +11.7% | -0.08914 to +2.139 | no |
| host CPU busy, the real machine under kind (%) | 24.07 | 36.14 | +50.2% | +10.9 to +13.25 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*