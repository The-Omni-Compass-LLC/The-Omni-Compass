# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.2 |
| response time (ms), mean | 130.1 | 73.49 |
| response time (ms), 95th percentile | 276.7 | 114.7 |
| response time (ms), 99th percentile | 418.4 | 134 |
| time over the response line (% of samples) | 0.7009 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.02667 |
| utilisation (used / allocatable) | 0.03332 | 0.04592 |
| CPU used (cores), mean | 0.7998 | 1.102 |
| Omni's own CPU (cores), mean | 0 | 0.00781 |
| CPU used with Omni's own (cores), mean | 0.7998 | 1.11 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785 | 588.7 |
| HPA replicas, mean | 9.776 | 9.851 |
| pods started | 1.7 | 1 |
| pod start wait, total (s) | 2.2 | 1.9 |
| pod start wait, mean (s) | 0.9917 | 0.7833 |
| host CPU busy, the real machine under kind (%) | 24.11 | 32.8 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.785e-16 to +8.338e-16 | same (under one part in a million) |
| node-hours | 1.518 | 1.518 | +0.1% | -0.006259 to +0.007925 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.2 | +1.9% | +2.017 to +3.951 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.2 | +1.9% | +2.017 to +3.951 | yes, worse |
| response time (ms), mean | 130.1 | 73.49 | -43.5% | -75.68 to -37.46 | yes, better |
| response time (ms), 95th percentile | 276.7 | 114.7 | -58.6% | -194.4 to -129.6 | yes, better |
| response time (ms), 99th percentile | 418.4 | 134 | -68.0% | -346.5 to -222.3 | yes, better |
| time over the response line (% of samples) | 0.7009 | 0 | -100.0% | -1.212 to -0.1894 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.02667 | +0.0% | -0.08992 to +0.08992 | no |
| utilisation (used / allocatable) | 0.03332 | 0.04592 | +37.8% | +0.009101 to +0.0161 | yes, more |
| CPU used (cores), mean | 0.7998 | 1.102 | +37.8% | +0.2184 to +0.3863 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.00781 | +0.00781 (native is 0) | +0.00701 to +0.00861 | yes, more |
| CPU used with Omni's own (cores), mean | 0.7998 | 1.11 | +38.8% | +0.2255 to +0.3949 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785 | 588.7 | -25.0% | -230 to -162.5 | yes, less |
| HPA replicas, mean | 9.776 | 9.851 | +0.8% | +0.02623 to +0.1242 | yes, worse |
| pods started | 1.7 | 1 | -41.2% | -1.046 to -0.3545 | yes, better |
| pod start wait, total (s) | 2.2 | 1.9 | -13.6% | -1.314 to +0.7144 | no |
| pod start wait, mean (s) | 0.9917 | 0.7833 | -21.0% | -1.032 to +0.6154 | no |
| host CPU busy, the real machine under kind (%) | 24.11 | 32.8 | +36.0% | +6.248 to +11.13 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*