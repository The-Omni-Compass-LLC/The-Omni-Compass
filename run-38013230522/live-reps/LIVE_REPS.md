# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.976 |
| node-hours | 4.51 | 4.497 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.1 | 520.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.1 | 519 |
| response time (ms), mean | 320.9 | 170.1 |
| response time (ms), 95th percentile | 843.8 | 316.7 |
| response time (ms), 99th percentile | 3279 | 1968 |
| time over the response line (% of samples) | 21.94 | 13.02 |
| failed requests (%) | 12.05 | 10.73 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4033 | 0.485 |
| utilisation (used / allocatable) | 0.1088 | 0.1068 |
| CPU used (cores), mean | 2.611 | 2.555 |
| Omni's own CPU (cores), mean | 0 | 0.00906 |
| CPU used with Omni's own (cores), mean | 2.611 | 2.564 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 275 | 280.9 |
| HPA replicas, mean | 9.546 | 9.458 |
| pods started | 5 | 4.4 |
| pod start wait, total (s) | 16.1 | 14.3 |
| pod start wait, mean (s) | 3.075 | 2.917 |
| host CPU busy, the real machine under kind (%) | 73.28 | 71.98 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.976 | -0.4% | -0.06127 to +0.01252 | no |
| node-hours | 4.51 | 4.497 | -0.3% | -0.04629 to +0.02029 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.1 | 520.3 | -0.1% | -1.957 to +0.4233 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.1 | 519 | -0.4% | -5.137 to +0.8536 | no |
| response time (ms), mean | 320.9 | 170.1 | -47.0% | -177.5 to -124 | yes, better |
| response time (ms), 95th percentile | 843.8 | 316.7 | -62.5% | -626.4 to -427.8 | yes, better |
| response time (ms), 99th percentile | 3279 | 1968 | -40.0% | -2626 to +4.698 | no |
| time over the response line (% of samples) | 21.94 | 13.02 | -40.6% | -11.05 to -6.781 | yes, better |
| failed requests (%) | 12.05 | 10.73 | -11.0% | -2.023 to -0.6201 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4033 | 0.485 | +20.2% | -0.2276 to +0.3909 | no |
| utilisation (used / allocatable) | 0.1088 | 0.1068 | -1.8% | -0.00278 to -0.001142 | yes, less |
| CPU used (cores), mean | 2.611 | 2.555 | -2.1% | -0.07318 to -0.03872 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00906 | +0.00906 (native is 0) | +0.008085 to +0.01004 | yes, more |
| CPU used with Omni's own (cores), mean | 2.611 | 2.564 | -1.8% | -0.06474 to -0.02904 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 275 | 280.9 | +2.2% | +1.214 to +10.68 | yes, more |
| HPA replicas, mean | 9.546 | 9.458 | -0.9% | -0.2575 to +0.08181 | no |
| pods started | 5 | 4.4 | -12.0% | -1.369 to +0.1689 | no |
| pod start wait, total (s) | 16.1 | 14.3 | -11.2% | -7.933 to +4.333 | no |
| pod start wait, mean (s) | 3.075 | 2.917 | -5.1% | -1.047 to +0.7316 | no |
| host CPU busy, the real machine under kind (%) | 73.28 | 71.98 | -1.8% | -1.725 to -0.8866 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.8 |  |  | 10 |
| compass | 28.2 | +67.9% | +9.0 to +13.8 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*