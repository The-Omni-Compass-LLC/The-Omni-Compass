# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161 |
| response time (ms), mean | 146.8 | 77 |
| response time (ms), 95th percentile | 308 | 116.9 |
| response time (ms), 99th percentile | 453.8 | 140.7 |
| time over the response line (% of samples) | 0.9247 | 0.01212 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 |
| utilisation (used / allocatable) | 0.03292 | 0.04745 |
| CPU used (cores), mean | 0.79 | 1.139 |
| Omni's own CPU (cores), mean | 0 | 0.00813 |
| CPU used with Omni's own (cores), mean | 0.79 | 1.147 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.9 | 566.1 |
| HPA replicas, mean | 9.738 | 9.803 |
| pods started | 2.5 | 1.2 |
| pod start wait, total (s) | 3.6 | 1.6 |
| pod start wait, mean (s) | 1.425 | 0.7667 |
| host CPU busy, the real machine under kind (%) | 24.12 | 33.88 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.206e-16 to +5.43e-16 | same (under one part in a million) |
| node-hours | 1.513 | 1.513 | -0.0% | -0.008186 to +0.007186 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161 | +2.1% | +2.457 to +4.095 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161 | +2.1% | +2.457 to +4.095 | yes, worse |
| response time (ms), mean | 146.8 | 77 | -47.5% | -82.98 to -56.56 | yes, better |
| response time (ms), 95th percentile | 308 | 116.9 | -62.1% | -220.7 to -161.6 | yes, better |
| response time (ms), 99th percentile | 453.8 | 140.7 | -69.0% | -366.4 to -259.7 | yes, better |
| time over the response line (% of samples) | 0.9247 | 0.01212 | -98.7% | -1.662 to -0.1632 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 | +0.08 (native is 0) | -0.01214 to +0.1721 | no |
| utilisation (used / allocatable) | 0.03292 | 0.04745 | +44.2% | +0.01178 to +0.0173 | yes, more |
| CPU used (cores), mean | 0.79 | 1.139 | +44.2% | +0.2827 to +0.4151 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.00813 | +0.00813 (native is 0) | +0.007247 to +0.009013 | yes, more |
| CPU used with Omni's own (cores), mean | 0.79 | 1.147 | +45.2% | +0.2902 to +0.4239 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 792.9 | 566.1 | -28.6% | -256.3 to -197.4 | yes, less |
| HPA replicas, mean | 9.738 | 9.803 | +0.7% | -0.1561 to +0.2868 | no |
| pods started | 2.5 | 1.2 | -52.0% | -2.692 to +0.09235 | no |
| pod start wait, total (s) | 3.6 | 1.6 | -55.6% | -4.133 to +0.1326 | no |
| pod start wait, mean (s) | 1.425 | 0.7667 | -46.2% | -1.35 to +0.03366 | no |
| host CPU busy, the real machine under kind (%) | 24.12 | 33.88 | +40.4% | +7.806 to +11.7 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*