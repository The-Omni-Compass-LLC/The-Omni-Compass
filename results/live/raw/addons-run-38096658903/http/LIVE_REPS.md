# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 0.625 | 0.6067 |
| energy, parked workers still on at idle power (Wh, declared model) | 65.09 | 65.14 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.09 | 65.14 |
| response time (ms), mean | 255.1 | 91.54 |
| response time (ms), 95th percentile | 621.7 | 145.8 |
| response time (ms), 99th percentile | 811.5 | 195.3 |
| time over the response line (% of samples) | 11.72 | 0.303 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0 |
| utilisation (used / allocatable) | 0.03109 | 0.05341 |
| CPU used (cores), mean | 0.7462 | 1.282 |
| Omni's own CPU (cores), mean | 0 | 0.0117 |
| CPU used with Omni's own (cores), mean | 0.7462 | 1.294 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 837.4 | 502.6 |
| HPA replicas, mean | 2.499 | 1.739 |
| pods started | 2 | 1 |
| pod start wait, total (s) | 15 | 7 |
| pod start wait, mean (s) | 7.5 | 7 |
| host CPU busy, the real machine under kind (%) | 23.75 | 39.27 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | +nan to +nan | same (under one part in a million) |
| node-hours | 0.625 | 0.6067 | -2.9% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 65.09 | 65.14 | +0.1% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 65.09 | 65.14 | +0.1% | +nan to +nan | no |
| response time (ms), mean | 255.1 | 91.54 | -64.1% | +nan to +nan | no |
| response time (ms), 95th percentile | 621.7 | 145.8 | -76.5% | +nan to +nan | no |
| response time (ms), 99th percentile | 811.5 | 195.3 | -75.9% | +nan to +nan | no |
| time over the response line (% of samples) | 11.72 | 0.303 | -97.4% | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0 | -100.0% | +nan to +nan | no |
| utilisation (used / allocatable) | 0.03109 | 0.05341 | +71.8% | +nan to +nan | no |
| CPU used (cores), mean | 0.7462 | 1.282 | +71.8% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0117 | +0.0117 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 0.7462 | 1.294 | +73.3% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 837.4 | 502.6 | -40.0% | +nan to +nan | no |
| HPA replicas, mean | 2.499 | 1.739 | -30.4% | +nan to +nan | no |
| pods started | 2 | 1 | -50.0% | +nan to +nan | no |
| pod start wait, total (s) | 15 | 7 | -53.3% | +nan to +nan | no |
| pod start wait, mean (s) | 7.5 | 7 | -6.7% | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 23.75 | 39.27 | +65.3% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*