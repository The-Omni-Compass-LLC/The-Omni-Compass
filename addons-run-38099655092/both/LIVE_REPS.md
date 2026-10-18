# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.966 |
| node-hours | 1.515 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160.7 |
| response time (ms), mean | 124.3 | 79.78 |
| response time (ms), 95th percentile | 253.1 | 124.5 |
| response time (ms), 99th percentile | 385 | 153 |
| time over the response line (% of samples) | 0.5007 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2717 |
| utilisation (used / allocatable) | 0.0367 | 0.04705 |
| CPU used (cores), mean | 0.8807 | 1.124 |
| Omni's own CPU (cores), mean | 0 | 0.01517 |
| CPU used with Omni's own (cores), mean | 0.8807 | 1.139 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.3 | 574.6 |
| HPA replicas, mean | 8.857 | 8.969 |
| pods started | 4.7 | 4.9 |
| pod start wait, total (s) | 11.6 | 14.1 |
| pod start wait, mean (s) | 2.385 | 2.678 |
| host CPU busy, the real machine under kind (%) | 27.36 | 35.12 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.966 | -0.6% | -0.07434 to +0.005813 | no |
| node-hours | 1.515 | 1.509 | -0.4% | -0.02029 to +0.007015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 161.4 | +1.6% | +1.352 to +3.79 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160.7 | +1.2% | +0.2183 to +3.628 | yes, worse |
| response time (ms), mean | 124.3 | 79.78 | -35.8% | -61.04 to -28.02 | yes, better |
| response time (ms), 95th percentile | 253.1 | 124.5 | -50.8% | -157.7 to -99.61 | yes, better |
| response time (ms), 99th percentile | 385 | 153 | -60.3% | -281 to -183 | yes, better |
| time over the response line (% of samples) | 0.5007 | 0 | -100.0% | -0.8615 to -0.1398 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2133 | 0.2717 | +27.3% | -0.3847 to +0.5014 | no |
| utilisation (used / allocatable) | 0.0367 | 0.04705 | +28.2% | +0.007562 to +0.01314 | yes, more |
| CPU used (cores), mean | 0.8807 | 1.124 | +27.6% | +0.1713 to +0.3146 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01517 | +0.0152 (native is 0) | +0.01309 to +0.01725 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8807 | 1.139 | +29.3% | +0.1844 to +0.3318 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.3 | 574.6 | -19.8% | -166.4 to -116.9 | yes, less |
| HPA replicas, mean | 8.857 | 8.969 | +1.3% | -0.1674 to +0.3915 | no |
| pods started | 4.7 | 4.9 | +4.3% | -0.6121 to +1.012 | no |
| pod start wait, total (s) | 11.6 | 14.1 | +21.6% | -4.187 to +9.187 | no |
| pod start wait, mean (s) | 2.385 | 2.678 | +12.3% | -0.7561 to +1.343 | no |
| host CPU busy, the real machine under kind (%) | 27.36 | 35.12 | +28.3% | +5.523 to +9.988 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*