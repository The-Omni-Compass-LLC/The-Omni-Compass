# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.47 |
| node-hours | 1.518 | 1.377 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 150.3 |
| response time (ms), mean | 174.9 | 71.69 |
| response time (ms), 95th percentile | 429.6 | 109.7 |
| response time (ms), 99th percentile | 569 | 154.7 |
| time over the response line (% of samples) | 3.561 | 0.1097 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.35 |
| utilisation (used / allocatable) | 0.02991 | 0.04885 |
| CPU used (cores), mean | 0.7177 | 1.071 |
| Omni's own CPU (cores), mean | 0 | 0.01096 |
| CPU used with Omni's own (cores), mean | 0.7177 | 1.082 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 873.4 | 568 |
| HPA replicas, mean | 2.806 | 2.348 |
| pods started | 2.8 | 2.2 |
| pod start wait, total (s) | 22.3 | 19 |
| pod start wait, mean (s) | 7.883 | 8.65 |
| host CPU busy, the real machine under kind (%) | 22.83 | 33.04 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.47 | -8.8% | -0.7167 to -0.3429 | yes, better |
| node-hours | 1.518 | 1.377 | -9.3% | -0.1903 to -0.09239 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.3 | +1.6% | +1.177 to +3.924 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 150.3 | -4.7% | -11.65 to -3.228 | yes, better |
| response time (ms), mean | 174.9 | 71.69 | -59.0% | -130.4 to -76.09 | yes, better |
| response time (ms), 95th percentile | 429.6 | 109.7 | -74.5% | -394.6 to -245.3 | yes, better |
| response time (ms), 99th percentile | 569 | 154.7 | -72.8% | -512 to -316.5 | yes, better |
| time over the response line (% of samples) | 3.561 | 0.1097 | -96.9% | -5.933 to -0.9682 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.315 | 0.35 | +11.1% | -0.2429 to +0.3129 | no |
| utilisation (used / allocatable) | 0.02991 | 0.04885 | +63.3% | +0.01523 to +0.02266 | yes, more |
| CPU used (cores), mean | 0.7177 | 1.071 | +49.2% | +0.2672 to +0.4387 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01096 | +0.011 (native is 0) | +0.009073 to +0.01285 | yes, more |
| CPU used with Omni's own (cores), mean | 0.7177 | 1.082 | +50.7% | +0.2766 to +0.4512 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 873.4 | 568 | -35.0% | -339.9 to -270.8 | yes, less |
| HPA replicas, mean | 2.806 | 2.348 | -16.3% | -0.7596 to -0.1578 | yes, better |
| pods started | 2.8 | 2.2 | -21.4% | -1.203 to +0.0032 | no |
| pod start wait, total (s) | 22.3 | 19 | -14.8% | -8.769 to +2.169 | no |
| pod start wait, mean (s) | 7.883 | 8.65 | +9.7% | -0.01449 to +1.548 | no |
| host CPU busy, the real machine under kind (%) | 22.83 | 33.04 | +44.8% | +7.826 to +12.61 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*