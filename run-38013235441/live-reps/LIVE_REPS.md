# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 172 | 171.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172 | 171.8 |
| response time (ms), mean | 498 | 477.8 |
| response time (ms), 95th percentile | 1887 | 2225 |
| response time (ms), 99th percentile | 4959 | 5366 |
| time over the response line (% of samples) | 23.59 | 22.6 |
| failed requests (%) | 2.646 | 2.506 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.468 | 1.15 |
| utilisation (used / allocatable) | 0.09624 | 0.09564 |
| CPU used (cores), mean | 2.31 | 2.295 |
| Omni's own CPU (cores), mean | 0 | 0.01376 |
| CPU used with Omni's own (cores), mean | 2.31 | 2.309 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.5 | 304.7 |
| HPA replicas, mean | 15.06 | 15.14 |
| pods started | 4.6 | 4.1 |
| pod start wait, total (s) | 8.8 | 10.3 |
| pod start wait, mean (s) | 1.663 | 1.92 |
| host CPU busy, the real machine under kind (%) | 66.41 | 67.07 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 323.4 | 299.8 |
| second app: response time (ms), 99th percentile | 1792 | 1340 |
| second app: time over the response line (% of samples) | 14.82 | 14.28 |
| second app: failed requests (%) | 12.17 | 12.39 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.147e-15 to +8.087e-17 | same (under one part in a million) |
| node-hours | 1.512 | 1.512 | -0.0% | -0.002752 to +0.001752 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172 | 171.8 | -0.1% | -0.5303 to +0.137 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172 | 171.8 | -0.1% | -0.5303 to +0.137 | no |
| response time (ms), mean | 498 | 477.8 | -4.1% | -53.45 to +13.03 | no |
| response time (ms), 95th percentile | 1887 | 2225 | +17.9% | +69.17 to +606.3 | yes, worse |
| response time (ms), 99th percentile | 4959 | 5366 | +8.2% | -360.7 to +1174 | no |
| time over the response line (% of samples) | 23.59 | 22.6 | -4.2% | -2.94 to +0.9649 | no |
| failed requests (%) | 2.646 | 2.506 | -5.3% | -0.4745 to +0.1954 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.468 | 1.15 | -21.7% | -1.248 to +0.6111 | no |
| utilisation (used / allocatable) | 0.09624 | 0.09564 | -0.6% | -0.001371 to +0.0001757 | no |
| CPU used (cores), mean | 2.31 | 2.295 | -0.6% | -0.03291 to +0.004217 | no |
| Omni's own CPU (cores), mean | 0 | 0.01376 | +0.0138 (native is 0) | +0.01158 to +0.01594 | yes, more |
| CPU used with Omni's own (cores), mean | 2.31 | 2.309 | -0.0% | -0.0192 to +0.01802 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 302.5 | 304.7 | +0.7% | -1.458 to +5.806 | no |
| HPA replicas, mean | 15.06 | 15.14 | +0.5% | -0.2651 to +0.4288 | no |
| pods started | 4.6 | 4.1 | -10.9% | -1.9 to +0.9005 | no |
| pod start wait, total (s) | 8.8 | 10.3 | +17.0% | -3.424 to +6.424 | no |
| pod start wait, mean (s) | 1.663 | 1.92 | +15.4% | -0.4884 to +1.001 | no |
| host CPU busy, the real machine under kind (%) | 66.41 | 67.07 | +1.0% | +0.1465 to +1.176 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 323.4 | 299.8 | -7.3% | -83.16 to +35.99 | no |
| second app: response time (ms), 99th percentile | 1792 | 1340 | -25.2% | -1334 to +430.1 | no |
| second app: time over the response line (% of samples) | 14.82 | 14.28 | -3.6% | -1.1 to +0.01843 | no |
| second app: failed requests (%) | 12.17 | 12.39 | +1.8% | -0.4254 to +0.8695 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*