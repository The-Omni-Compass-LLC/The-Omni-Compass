# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.985 |
| node-hours | 4.513 | 4.5 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.6 | 522 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.6 | 521.1 |
| response time (ms), mean | 321 | 165.7 |
| response time (ms), 95th percentile | 879.9 | 335.7 |
| response time (ms), 99th percentile | 3110 | 1609 |
| time over the response line (% of samples) | 23.28 | 14.42 |
| failed requests (%) | 13.71 | 11.86 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.385 |
| utilisation (used / allocatable) | 0.1118 | 0.1098 |
| CPU used (cores), mean | 2.683 | 2.631 |
| Omni's own CPU (cores), mean | 0 | 0.00931 |
| CPU used with Omni's own (cores), mean | 2.683 | 2.641 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 270.4 | 274.9 |
| HPA replicas, mean | 9.559 | 9.555 |
| pods started | 4.7 | 3.7 |
| pod start wait, total (s) | 13.1 | 9.2 |
| pod start wait, mean (s) | 2.538 | 2.083 |
| host CPU busy, the real machine under kind (%) | 75.2 | 74.16 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.985 | -0.2% | -0.04823 to +0.01866 | no |
| node-hours | 4.513 | 4.5 | -0.3% | -0.03978 to +0.0125 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.6 | 522 | -0.3% | -2.126 to -1.069 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.6 | 521.1 | -0.5% | -4.485 to -0.3812 | yes, better |
| response time (ms), mean | 321 | 165.7 | -48.4% | -186.8 to -123.7 | yes, better |
| response time (ms), 95th percentile | 879.9 | 335.7 | -61.9% | -665.9 to -422.5 | yes, better |
| response time (ms), 99th percentile | 3110 | 1609 | -48.3% | -2155 to -847.8 | yes, better |
| time over the response line (% of samples) | 23.28 | 14.42 | -38.1% | -11.04 to -6.685 | yes, better |
| failed requests (%) | 13.71 | 11.86 | -13.6% | -2.616 to -1.101 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.385 | -10.1% | -0.4563 to +0.3696 | no |
| utilisation (used / allocatable) | 0.1118 | 0.1098 | -1.8% | -0.002514 to -0.001483 | yes, less |
| CPU used (cores), mean | 2.683 | 2.631 | -1.9% | -0.06119 to -0.04178 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00931 | +0.00931 (native is 0) | +0.00826 to +0.01036 | yes, more |
| CPU used with Omni's own (cores), mean | 2.683 | 2.641 | -1.6% | -0.05198 to -0.03237 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 270.4 | 274.9 | +1.7% | +3.222 to +5.719 | yes, more |
| HPA replicas, mean | 9.559 | 9.555 | -0.0% | -0.1383 to +0.1303 | no |
| pods started | 4.7 | 3.7 | -21.3% | -2.118 to +0.1184 | no |
| pod start wait, total (s) | 13.1 | 9.2 | -29.8% | -11.53 to +3.726 | no |
| pod start wait, mean (s) | 2.538 | 2.083 | -17.9% | -1.582 to +0.6733 | no |
| host CPU busy, the real machine under kind (%) | 75.2 | 74.16 | -1.4% | -1.235 to -0.8419 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.8 |  |  | 10 |
| compass | 25.8 | +53.6% | +6.0 to +12.0 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*