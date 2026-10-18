# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.7 |
| response time (ms), mean | 203.4 | 86.94 |
| response time (ms), 95th percentile | 475.7 | 133.9 |
| response time (ms), 99th percentile | 632.5 | 218.7 |
| time over the response line (% of samples) | 4.736 | 0.2922 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4483 | 0.3183 |
| utilisation (used / allocatable) | 0.03162 | 0.04844 |
| CPU used (cores), mean | 0.7589 | 1.163 |
| Omni's own CPU (cores), mean | 0 | 0.00981 |
| CPU used with Omni's own (cores), mean | 0.7589 | 1.172 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 827 | 556.3 |
| HPA replicas, mean | 2.96 | 2.493 |
| pods started | 2.9 | 2.3 |
| pod start wait, total (s) | 25.5 | 24.2 |
| pod start wait, mean (s) | 8.767 | 10.37 |
| host CPU busy, the real machine under kind (%) | 23.87 | 35.77 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.044e-17 to +5.733e-16 | same (under one part in a million) |
| node-hours | 1.518 | 1.515 | -0.1% | -0.01023 to +0.005901 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.7 | +2.3% | +2.536 to +4.804 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.7 | +2.3% | +2.536 to +4.804 | yes, worse |
| response time (ms), mean | 203.4 | 86.94 | -57.3% | -133.7 to -99.35 | yes, better |
| response time (ms), 95th percentile | 475.7 | 133.9 | -71.9% | -384 to -299.8 | yes, better |
| response time (ms), 99th percentile | 632.5 | 218.7 | -65.4% | -469.3 to -358.2 | yes, better |
| time over the response line (% of samples) | 4.736 | 0.2922 | -93.8% | -6.181 to -2.707 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4483 | 0.3183 | -29.0% | -0.3171 to +0.05705 | no |
| utilisation (used / allocatable) | 0.03162 | 0.04844 | +53.2% | +0.01467 to +0.01897 | yes, more |
| CPU used (cores), mean | 0.7589 | 1.163 | +53.2% | +0.3522 to +0.4553 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.00981 | +0.00981 (native is 0) | +0.008564 to +0.01106 | yes, more |
| CPU used with Omni's own (cores), mean | 0.7589 | 1.172 | +54.5% | +0.361 to +0.466 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 827 | 556.3 | -32.7% | -284 to -257.4 | yes, less |
| HPA replicas, mean | 2.96 | 2.493 | -15.8% | -0.7291 to -0.2051 | yes, better |
| pods started | 2.9 | 2.3 | -20.7% | -0.9694 to -0.2306 | yes, better |
| pod start wait, total (s) | 25.5 | 24.2 | -5.1% | -6.459 to +3.859 | no |
| pod start wait, mean (s) | 8.767 | 10.37 | +18.3% | +0.51 to +2.69 | yes, worse |
| host CPU busy, the real machine under kind (%) | 23.87 | 35.77 | +49.8% | +10.29 to +13.51 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*