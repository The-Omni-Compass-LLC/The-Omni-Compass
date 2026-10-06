# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.91 |
| node-hours | 4.513 | 4.447 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.5 | 511.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.5 | 506.6 |
| response time (ms), mean | 283.2 | 159.2 |
| response time (ms), 95th percentile | 804 | 343.3 |
| response time (ms), 99th percentile | 3292 | 1996 |
| time over the response line (% of samples) | 16.94 | 9.731 |
| failed requests (%) | 8.753 | 7.618 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6083 | 0.5617 |
| utilisation (used / allocatable) | 0.09539 | 0.09467 |
| CPU used (cores), mean | 2.289 | 2.249 |
| Omni's own CPU (cores), mean | 0 | 0.00846 |
| CPU used with Omni's own (cores), mean | 2.289 | 2.257 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 325.8 | 327.4 |
| HPA replicas, mean | 9.412 | 9.137 |
| pods started | 5.2 | 4 |
| pod start wait, total (s) | 22.3 | 13.9 |
| pod start wait, mean (s) | 3.72 | 2.464 |
| host CPU busy, the real machine under kind (%) | 64.57 | 63.67 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.91 | -1.5% | -0.187 to +0.007546 | no |
| node-hours | 4.513 | 4.447 | -1.5% | -0.1404 to +0.007806 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.5 | 511.7 | -0.2% | -1.668 to +0.06995 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.5 | 506.6 | -1.1% | -11.34 to -0.3771 | yes, better |
| response time (ms), mean | 283.2 | 159.2 | -43.8% | -168.8 to -79.13 | yes, better |
| response time (ms), 95th percentile | 804 | 343.3 | -57.3% | -621.1 to -300.3 | yes, better |
| response time (ms), 99th percentile | 3292 | 1996 | -39.4% | -2214 to -378.9 | yes, better |
| time over the response line (% of samples) | 16.94 | 9.731 | -42.6% | -10.4 to -4.022 | yes, better |
| failed requests (%) | 8.753 | 7.618 | -13.0% | -1.95 to -0.3197 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6083 | 0.5617 | -7.7% | -0.3509 to +0.2576 | no |
| utilisation (used / allocatable) | 0.09539 | 0.09467 | -0.8% | -0.002018 to +0.00058 | no |
| CPU used (cores), mean | 2.289 | 2.249 | -1.8% | -0.04562 to -0.03593 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00846 | +0.00846 (native is 0) | +0.007037 to +0.009883 | yes, more |
| CPU used with Omni's own (cores), mean | 2.289 | 2.257 | -1.4% | -0.03647 to -0.02816 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 325.8 | 327.4 | +0.5% | -1.979 to +5.194 | no |
| HPA replicas, mean | 9.412 | 9.137 | -2.9% | -0.623 to +0.07327 | no |
| pods started | 5.2 | 4 | -23.1% | -2.453 to +0.05264 | no |
| pod start wait, total (s) | 22.3 | 13.9 | -37.7% | -13.85 to -2.95 | yes, better |
| pod start wait, mean (s) | 3.72 | 2.464 | -33.8% | -2.058 to -0.4537 | yes, better |
| host CPU busy, the real machine under kind (%) | 64.57 | 63.67 | -1.4% | -1.081 to -0.7293 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 22.8 |  |  | 10 |
| compass | 33.0 | +44.7% | +6.7 to +13.7 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*