# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.977 |
| node-hours | 1.519 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 162.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 161.7 |
| response time (ms), mean | 148.2 | 90.81 |
| response time (ms), 95th percentile | 298.8 | 141.4 |
| response time (ms), 99th percentile | 424.2 | 177.3 |
| time over the response line (% of samples) | 0.4478 | 0.0122 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2417 |
| utilisation (used / allocatable) | 0.037 | 0.05099 |
| CPU used (cores), mean | 0.888 | 1.219 |
| Omni's own CPU (cores), mean | 0 | 0.01451 |
| CPU used with Omni's own (cores), mean | 0.888 | 1.234 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 708.8 | 525.1 |
| HPA replicas, mean | 8.837 | 9.221 |
| pods started | 4.8 | 5 |
| pod start wait, total (s) | 13.7 | 14 |
| pod start wait, mean (s) | 2.83 | 2.713 |
| host CPU busy, the real machine under kind (%) | 27.18 | 36.91 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.977 | -0.4% | -0.05689 to +0.01164 | no |
| node-hours | 1.519 | 1.512 | -0.5% | -0.01753 to +0.003083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 162.2 | +1.9% | +2.292 to +3.617 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 161.7 | +1.6% | +1.648 to +3.403 | yes, worse |
| response time (ms), mean | 148.2 | 90.81 | -38.7% | -62.15 to -52.68 | yes, better |
| response time (ms), 95th percentile | 298.8 | 141.4 | -52.7% | -169.9 to -144.9 | yes, better |
| response time (ms), 99th percentile | 424.2 | 177.3 | -58.2% | -264.9 to -228.9 | yes, better |
| time over the response line (% of samples) | 0.4478 | 0.0122 | -97.3% | -0.6257 to -0.2454 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2417 | +51.0% | -0.2032 to +0.3665 | no |
| utilisation (used / allocatable) | 0.037 | 0.05099 | +37.8% | +0.01308 to +0.01489 | yes, more |
| CPU used (cores), mean | 0.888 | 1.219 | +37.3% | +0.3092 to +0.3532 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01451 | +0.0145 (native is 0) | +0.01321 to +0.01581 | yes, more |
| CPU used with Omni's own (cores), mean | 0.888 | 1.234 | +38.9% | +0.3228 to +0.3686 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 708.8 | 525.1 | -25.9% | -194.7 to -172.7 | yes, less |
| HPA replicas, mean | 8.837 | 9.221 | +4.3% | +0.2971 to +0.471 | yes, worse |
| pods started | 4.8 | 5 | +4.2% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 13.7 | 14 | +2.2% | -3.456 to +4.056 | no |
| pod start wait, mean (s) | 2.83 | 2.713 | -4.1% | -0.6717 to +0.4383 | no |
| host CPU busy, the real machine under kind (%) | 27.18 | 36.91 | +35.8% | +9.1 to +10.35 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*