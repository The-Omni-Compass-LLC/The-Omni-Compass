# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.521 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 162.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 162.3 |
| response time (ms), mean | 165 | 88.02 |
| response time (ms), 95th percentile | 339.2 | 140.5 |
| response time (ms), 99th percentile | 503.1 | 162.3 |
| time over the response line (% of samples) | 1.385 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.105 |
| utilisation (used / allocatable) | 0.03413 | 0.04979 |
| CPU used (cores), mean | 0.8192 | 1.195 |
| Omni's own CPU (cores), mean | 0 | 0.00833 |
| CPU used with Omni's own (cores), mean | 0.8192 | 1.203 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.1 | 540.1 |
| HPA replicas, mean | 9.814 | 9.932 |
| pods started | 2.2 | 0.6 |
| pod start wait, total (s) | 3.4 | 0.8 |
| pod start wait, mean (s) | 0.9 | 0.3833 |
| host CPU busy, the real machine under kind (%) | 24.57 | 35.07 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.267e-16 to +1.294e-15 | same (under one part in a million) |
| node-hours | 1.515 | 1.521 | +0.3% | -8.884e-05 to +0.01042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 162.3 | +2.6% | +3.402 to +4.821 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 162.3 | +2.6% | +3.402 to +4.821 | yes, worse |
| response time (ms), mean | 165 | 88.02 | -46.6% | -91.92 to -61.99 | yes, better |
| response time (ms), 95th percentile | 339.2 | 140.5 | -58.6% | -229 to -168.5 | yes, better |
| response time (ms), 99th percentile | 503.1 | 162.3 | -67.7% | -384.4 to -297.3 | yes, better |
| time over the response line (% of samples) | 1.385 | 0 | -100.0% | -1.99 to -0.7807 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.105 | +0.105 (native is 0) | +0.007976 to +0.202 | yes, more |
| utilisation (used / allocatable) | 0.03413 | 0.04979 | +45.9% | +0.01315 to +0.01816 | yes, more |
| CPU used (cores), mean | 0.8192 | 1.195 | +45.9% | +0.3157 to +0.4359 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.00833 | +0.00833 (native is 0) | +0.007516 to +0.009144 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8192 | 1.203 | +46.9% | +0.3234 to +0.4448 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.1 | 540.1 | -29.5% | -255.2 to -196.7 | yes, less |
| HPA replicas, mean | 9.814 | 9.932 | +1.2% | -0.05212 to +0.2884 | no |
| pods started | 2.2 | 0.6 | -72.7% | -3.224 to +0.02417 | no |
| pod start wait, total (s) | 3.4 | 0.8 | -76.5% | -5.302 to +0.1018 | no |
| pod start wait, mean (s) | 0.9 | 0.3833 | -57.4% | -1.185 to +0.1517 | no |
| host CPU busy, the real machine under kind (%) | 24.57 | 35.07 | +42.8% | +8.894 to +12.12 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*