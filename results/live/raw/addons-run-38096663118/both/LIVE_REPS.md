# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.966 |
| node-hours | 1.519 | 1.506 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 160.8 |
| response time (ms), mean | 136.7 | 84.06 |
| response time (ms), 95th percentile | 278.7 | 129.8 |
| response time (ms), 99th percentile | 416.1 | 157 |
| time over the response line (% of samples) | 0.4837 | 0.01363 |
| failed requests (%) | 0.01372 | 0.01363 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1759 | 0.4241 |
| utilisation (used / allocatable) | 0.03678 | 0.04882 |
| CPU used (cores), mean | 0.8828 | 1.166 |
| Omni's own CPU (cores), mean | 0 | 0.01499 |
| CPU used with Omni's own (cores), mean | 0.8828 | 1.181 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.6 | 553.1 |
| HPA replicas, mean | 8.881 | 9.153 |
| pods started | 4.778 | 4.778 |
| pod start wait, total (s) | 13.89 | 12 |
| pod start wait, mean (s) | 2.848 | 2.363 |
| host CPU busy, the real machine under kind (%) | 27.3 | 35.82 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.966 | -0.6% | -0.07395 to +0.005256 | no |
| node-hours | 1.519 | 1.506 | -0.8% | -0.0199 to -0.005222 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.4 | +1.4% | +1.6 to +2.94 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 160.8 | +1.0% | +0.5958 to +2.643 | yes, worse |
| response time (ms), mean | 136.7 | 84.06 | -38.5% | -64.66 to -40.55 | yes, better |
| response time (ms), 95th percentile | 278.7 | 129.8 | -53.4% | -174.4 to -123.4 | yes, better |
| response time (ms), 99th percentile | 416.1 | 157 | -62.3% | -290.8 to -227.5 | yes, better |
| time over the response line (% of samples) | 0.4837 | 0.01363 | -97.2% | -0.7711 to -0.1691 | yes, better |
| failed requests (%) | 0.01372 | 0.01363 | -0.6% | -0.04739 to +0.04722 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1759 | 0.4241 | +141.1% | -0.1232 to +0.6195 | no |
| utilisation (used / allocatable) | 0.03678 | 0.04882 | +32.7% | +0.009112 to +0.01496 | yes, more |
| CPU used (cores), mean | 0.8828 | 1.166 | +32.0% | +0.2082 to +0.3577 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01499 | +0.015 (native is 0) | +0.0133 to +0.01668 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8828 | 1.181 | +33.7% | +0.2221 to +0.3738 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.6 | 553.1 | -22.5% | -190.7 to -130.1 | yes, less |
| HPA replicas, mean | 8.881 | 9.153 | +3.1% | +0.07788 to +0.4657 | yes, worse |
| pods started | 4.778 | 4.778 | +0.0% | -0.7687 to +0.7687 | no |
| pod start wait, total (s) | 13.89 | 12 | -13.6% | -6.681 to +2.903 | no |
| pod start wait, mean (s) | 2.848 | 2.363 | -17.0% | -1.189 to +0.2188 | no |
| host CPU busy, the real machine under kind (%) | 27.3 | 35.82 | +31.2% | +6.639 to +10.39 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*