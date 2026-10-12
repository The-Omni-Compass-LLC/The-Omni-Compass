# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 0.62 | 0.62 |
| energy, parked workers still on at idle power (Wh, declared model) | 65 | 65.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65 | 65.5 |
| response time (ms), mean | 75.04 | 51.79 |
| response time (ms), 95th percentile | 177.8 | 78.08 |
| response time (ms), 99th percentile | 268.9 | 99.82 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0 |
| utilisation (used / allocatable) | 0.03672 | 0.04229 |
| CPU used (cores), mean | 0.8813 | 1.015 |
| Omni's own CPU (cores), mean | 0 | 0.0084 |
| CPU used with Omni's own (cores), mean | 0.8813 | 1.023 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 624.6 |
| HPA replicas, mean | 10 | 10 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 26.57 | 31.2 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +nan to +nan | no |
| node-hours | 0.62 | 0.62 | +0.0% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 65 | 65.5 | +0.8% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65 | 65.5 | +0.8% | +nan to +nan | no |
| response time (ms), mean | 75.04 | 51.79 | -31.0% | +nan to +nan | no |
| response time (ms), 95th percentile | 177.8 | 78.08 | -56.1% | +nan to +nan | no |
| response time (ms), 99th percentile | 268.9 | 99.82 | -62.9% | +nan to +nan | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| utilisation (used / allocatable) | 0.03672 | 0.04229 | +15.2% | +nan to +nan | no |
| CPU used (cores), mean | 0.8813 | 1.015 | +15.2% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0084 | +0.0084 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 0.8813 | 1.023 | +16.1% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 624.6 | -12.5% | +nan to +nan | no |
| HPA replicas, mean | 10 | 10 | +0.0% | +nan to +nan | no |
| pods started | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 26.57 | 31.2 | +17.4% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*