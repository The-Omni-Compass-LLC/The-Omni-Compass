# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.986 |
| node-hours | 4.514 | 4.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 522 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 521.2 |
| response time (ms), mean | 321.1 | 183 |
| response time (ms), 95th percentile | 864.5 | 368.1 |
| response time (ms), 99th percentile | 3055 | 2045 |
| time over the response line (% of samples) | 23.8 | 14.61 |
| failed requests (%) | 13.57 | 11.7 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.4283 |
| utilisation (used / allocatable) | 0.1114 | 0.1094 |
| CPU used (cores), mean | 2.674 | 2.623 |
| Omni's own CPU (cores), mean | 0 | 0.009211 |
| CPU used with Omni's own (cores), mean | 2.674 | 2.603 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 272.8 | 275.6 |
| HPA replicas, mean | 9.555 | 9.471 |
| pods started | 4.6 | 4 |
| pod start wait, total (s) | 14.7 | 11.5 |
| pod start wait, mean (s) | 2.933 | 2.472 |
| host CPU busy, the real machine under kind (%) | 74.89 | 73.97 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.986 | -0.2% | -0.04459 to +0.01725 | no |
| node-hours | 4.514 | 4.503 | -0.2% | -0.03226 to +0.01032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 522 | -0.3% | -2.454 to -0.2686 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 521.2 | -0.4% | -3.25 to -1.019 | yes, better |
| response time (ms), mean | 321.1 | 183 | -43.0% | -169.6 to -106.7 | yes, better |
| response time (ms), 95th percentile | 864.5 | 368.1 | -57.4% | -615.4 to -377.3 | yes, better |
| response time (ms), 99th percentile | 3055 | 2045 | -33.1% | -1728 to -291.7 | yes, better |
| time over the response line (% of samples) | 23.8 | 14.61 | -38.6% | -11.49 to -6.898 | yes, better |
| failed requests (%) | 13.57 | 11.7 | -13.8% | -2.601 to -1.141 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.4283 | -5.9% | -0.2192 to +0.1659 | no |
| utilisation (used / allocatable) | 0.1114 | 0.1094 | -1.8% | -0.003198 to -0.0008351 | yes, less |
| CPU used (cores), mean | 2.674 | 2.623 | -1.9% | -0.07303 to -0.03027 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.009211 | +0.00921 (native is 0) | +0.008043 to +0.01038 | yes, more |
| CPU used with Omni's own (cores), mean | 2.674 | 2.634 | -1.5% | -0.06393 to -0.01761 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 272.8 | 275.6 | +1.0% | -2.004 to +7.614 | no |
| HPA replicas, mean | 9.555 | 9.471 | -0.9% | -0.2584 to +0.08931 | no |
| pods started | 4.6 | 4 | -13.0% | -1.505 to +0.3048 | no |
| pod start wait, total (s) | 14.7 | 11.5 | -21.8% | -9.434 to +3.034 | no |
| pod start wait, mean (s) | 2.933 | 2.472 | -15.7% | -1.495 to +0.573 | no |
| host CPU busy, the real machine under kind (%) | 74.89 | 73.97 | -1.2% | -1.528 to -0.3101 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.2 |  |  | 10 |
| compass | 25.2 | +55.6% | +6.0 to +12.0 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*