# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.957 |
| node-hours | 1.517 | 1.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.7 |
| response time (ms), mean | 113.1 | 72.18 |
| response time (ms), 95th percentile | 242 | 113.9 |
| response time (ms), 99th percentile | 366.4 | 146.6 |
| time over the response line (% of samples) | 0.4735 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4483 | 0.1067 |
| utilisation (used / allocatable) | 0.0362 | 0.04533 |
| CPU used (cores), mean | 0.8687 | 1.081 |
| Omni's own CPU (cores), mean | 0 | 0.01432 |
| CPU used with Omni's own (cores), mean | 0.8687 | 1.095 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.2 | 597.5 |
| HPA replicas, mean | 8.841 | 8.872 |
| pods started | 4.9 | 5.1 |
| pod start wait, total (s) | 13.1 | 15 |
| pod start wait, mean (s) | 2.543 | 2.818 |
| host CPU busy, the real machine under kind (%) | 27.02 | 33.49 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.957 | -0.7% | -0.08326 to -0.003134 | yes, better |
| node-hours | 1.517 | 1.503 | -0.9% | -0.02187 to -0.00691 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160.5 | +1.0% | +0.3723 to +2.922 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.7 | +0.5% | -0.5015 to +2.163 | no |
| response time (ms), mean | 113.1 | 72.18 | -36.2% | -57.93 to -23.87 | yes, better |
| response time (ms), 95th percentile | 242 | 113.9 | -52.9% | -160.1 to -96.13 | yes, better |
| response time (ms), 99th percentile | 366.4 | 146.6 | -60.0% | -268 to -171.7 | yes, better |
| time over the response line (% of samples) | 0.4735 | 0 | -100.0% | -0.8219 to -0.125 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4483 | 0.1067 | -76.2% | -0.5617 to -0.1217 | yes, less |
| utilisation (used / allocatable) | 0.0362 | 0.04533 | +25.2% | +0.005642 to +0.01263 | yes, more |
| CPU used (cores), mean | 0.8687 | 1.081 | +24.4% | +0.126 to +0.2978 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01432 | +0.0143 (native is 0) | +0.01217 to +0.01647 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8687 | 1.095 | +26.0% | +0.1382 to +0.3142 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 725.2 | 597.5 | -17.6% | -163.1 to -92.26 | yes, less |
| HPA replicas, mean | 8.841 | 8.872 | +0.3% | -0.2551 to +0.3152 | no |
| pods started | 4.9 | 5.1 | +4.1% | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 13.1 | 15 | +14.5% | -0.1358 to +3.936 | no |
| pod start wait, mean (s) | 2.543 | 2.818 | +10.8% | -0.155 to +0.705 | no |
| host CPU busy, the real machine under kind (%) | 27.02 | 33.49 | +23.9% | +4.025 to +8.91 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*