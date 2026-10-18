# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 0.6217 | 0.625 |
| energy, parked workers still on at idle power (Wh, declared model) | 65.41 | 66.38 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.41 | 66.38 |
| response time (ms), mean | 74.68 | 52.14 |
| response time (ms), 95th percentile | 176 | 78.88 |
| response time (ms), 99th percentile | 214.7 | 99.19 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0 |
| utilisation (used / allocatable) | 0.04001 | 0.04658 |
| CPU used (cores), mean | 0.9602 | 1.118 |
| Omni's own CPU (cores), mean | 0 | 0.0187 |
| CPU used with Omni's own (cores), mean | 0.9602 | 1.137 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 657.5 | 570.1 |
| HPA replicas, mean | 7.716 | 8.235 |
| pods started | 6 | 6 |
| pod start wait, total (s) | 18 | 23 |
| pod start wait, mean (s) | 3 | 3.833 |
| host CPU busy, the real machine under kind (%) | 28.3 | 32.26 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +nan to +nan | same (under one part in a million) |
| node-hours | 0.6217 | 0.625 | +0.5% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 65.41 | 66.38 | +1.5% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.41 | 66.38 | +1.5% | +nan to +nan | no |
| response time (ms), mean | 74.68 | 52.14 | -30.2% | +nan to +nan | no |
| response time (ms), 95th percentile | 176 | 78.88 | -55.2% | +nan to +nan | no |
| response time (ms), 99th percentile | 214.7 | 99.19 | -53.8% | +nan to +nan | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| utilisation (used / allocatable) | 0.04001 | 0.04658 | +16.4% | +nan to +nan | no |
| CPU used (cores), mean | 0.9602 | 1.118 | +16.4% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0187 | +0.0187 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 0.9602 | 1.137 | +18.4% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 657.5 | 570.1 | -13.3% | +nan to +nan | no |
| HPA replicas, mean | 7.716 | 8.235 | +6.7% | +nan to +nan | no |
| pods started | 6 | 6 | +0.0% | +nan to +nan | no |
| pod start wait, total (s) | 18 | 23 | +27.8% | +nan to +nan | no |
| pod start wait, mean (s) | 3 | 3.833 | +27.8% | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 28.3 | 32.26 | +14.0% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*