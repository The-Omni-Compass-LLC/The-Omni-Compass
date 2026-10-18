# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.973 |
| node-hours | 4.512 | 4.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 519.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 518.3 |
| response time (ms), mean | 297.1 | 156.7 |
| response time (ms), 95th percentile | 829.5 | 304.9 |
| response time (ms), 99th percentile | 2479 | 1521 |
| time over the response line (% of samples) | 22.77 | 13.67 |
| failed requests (%) | 13.29 | 11.69 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5033 | 0.5067 |
| utilisation (used / allocatable) | 0.1084 | 0.1064 |
| CPU used (cores), mean | 2.602 | 2.547 |
| Omni's own CPU (cores), mean | 0 | 0.00915 |
| CPU used with Omni's own (cores), mean | 2.602 | 2.556 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 284.5 | 290.5 |
| HPA replicas, mean | 9.538 | 9.455 |
| pods started | 4.7 | 3.9 |
| pod start wait, total (s) | 13.8 | 12.8 |
| pod start wait, mean (s) | 2.658 | 2.581 |
| host CPU busy, the real machine under kind (%) | 73.13 | 71.81 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.973 | -0.4% | -0.06703 to +0.01358 | no |
| node-hours | 4.512 | 4.492 | -0.5% | -0.05144 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 519.8 | -0.3% | -2.166 to -0.5619 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 518.3 | -0.6% | -5.423 to -0.3182 | yes, better |
| response time (ms), mean | 297.1 | 156.7 | -47.3% | -173 to -107.8 | yes, better |
| response time (ms), 95th percentile | 829.5 | 304.9 | -63.2% | -639.8 to -409.4 | yes, better |
| response time (ms), 99th percentile | 2479 | 1521 | -38.7% | -1370 to -546.9 | yes, better |
| time over the response line (% of samples) | 22.77 | 13.67 | -40.0% | -11.96 to -6.246 | yes, better |
| failed requests (%) | 13.29 | 11.69 | -12.1% | -2.276 to -0.9392 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5033 | 0.5067 | +0.7% | -0.3087 to +0.3153 | no |
| utilisation (used / allocatable) | 0.1084 | 0.1064 | -1.9% | -0.002755 to -0.001295 | yes, less |
| CPU used (cores), mean | 2.602 | 2.547 | -2.1% | -0.07281 to -0.03712 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00915 | +0.00915 (native is 0) | +0.007784 to +0.01052 | yes, more |
| CPU used with Omni's own (cores), mean | 2.602 | 2.556 | -1.8% | -0.06449 to -0.02714 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 284.5 | 290.5 | +2.1% | +1.205 to +10.89 | yes, more |
| HPA replicas, mean | 9.538 | 9.455 | -0.9% | -0.3117 to +0.1447 | no |
| pods started | 4.7 | 3.9 | -17.0% | -1.679 to +0.07931 | no |
| pod start wait, total (s) | 13.8 | 12.8 | -7.2% | -5.828 to +3.828 | no |
| pod start wait, mean (s) | 2.658 | 2.581 | -2.9% | -0.723 to +0.5687 | no |
| host CPU busy, the real machine under kind (%) | 73.13 | 71.81 | -1.8% | -1.869 to -0.7698 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 18.6 |  |  | 10 |
| compass | 27.6 | +48.4% | +6.0 to +12.0 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*