# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.895 |
| node-hours | 4.513 | 4.439 |
| energy, parked workers still on at idle power (Wh, declared model) | 515.3 | 513.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.3 | 507.9 |
| response time (ms), mean | 270.6 | 145.9 |
| response time (ms), 95th percentile | 750.3 | 288.1 |
| response time (ms), 99th percentile | 2153 | 1292 |
| time over the response line (% of samples) | 18.04 | 9.839 |
| failed requests (%) | 8.941 | 7.705 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4567 | 0.5067 |
| utilisation (used / allocatable) | 0.09931 | 0.09747 |
| CPU used (cores), mean | 2.384 | 2.312 |
| Omni's own CPU (cores), mean | 0 | 0.00885 |
| CPU used with Omni's own (cores), mean | 2.384 | 2.321 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.3 | 310.8 |
| HPA replicas, mean | 9.495 | 9.262 |
| pods started | 4.8 | 5.2 |
| pod start wait, total (s) | 18.4 | 19.5 |
| pod start wait, mean (s) | 3.254 | 3.317 |
| host CPU busy, the real machine under kind (%) | 67.02 | 65.37 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.895 | -1.8% | -0.304 to +0.09367 | no |
| node-hours | 4.513 | 4.439 | -1.7% | -0.2273 to +0.07773 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515.3 | 513.8 | -0.3% | -2.511 to -0.3157 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.3 | 507.9 | -1.4% | -19.31 to +4.613 | no |
| response time (ms), mean | 270.6 | 145.9 | -46.1% | -157.6 to -91.9 | yes, better |
| response time (ms), 95th percentile | 750.3 | 288.1 | -61.6% | -561.3 to -363.2 | yes, better |
| response time (ms), 99th percentile | 2153 | 1292 | -40.0% | -1546 to -175.5 | yes, better |
| time over the response line (% of samples) | 18.04 | 9.839 | -45.5% | -11 to -5.405 | yes, better |
| failed requests (%) | 8.941 | 7.705 | -13.8% | -2.053 to -0.421 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4567 | 0.5067 | +10.9% | -0.2028 to +0.3028 | no |
| utilisation (used / allocatable) | 0.09931 | 0.09747 | -1.9% | -0.003372 to -0.0003199 | yes, less |
| CPU used (cores), mean | 2.384 | 2.312 | -3.0% | -0.0976 to -0.04495 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00885 | +0.00885 (native is 0) | +0.00754 to +0.01016 | yes, more |
| CPU used with Omni's own (cores), mean | 2.384 | 2.321 | -2.6% | -0.08962 to -0.03522 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.3 | 310.8 | +2.1% | -0.326 to +13.28 | no |
| HPA replicas, mean | 9.495 | 9.262 | -2.5% | -0.3159 to -0.1497 | yes, better |
| pods started | 4.8 | 5.2 | +8.3% | -0.5048 to +1.305 | no |
| pod start wait, total (s) | 18.4 | 19.5 | +6.0% | -5.284 to +7.484 | no |
| pod start wait, mean (s) | 3.254 | 3.317 | +1.9% | -0.9719 to +1.098 | no |
| host CPU busy, the real machine under kind (%) | 67.02 | 65.37 | -2.5% | -2.428 to -0.8711 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 21.0 |  |  | 10 |
| compass | 31.2 | +48.6% | +8.1 to +12.3 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*