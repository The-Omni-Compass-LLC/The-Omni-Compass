# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.898 |
| node-hours | 4.515 | 4.435 |
| energy, parked workers still on at idle power (Wh, declared model) | 519.2 | 517.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.2 | 512 |
| response time (ms), mean | 288.8 | 157.6 |
| response time (ms), 95th percentile | 790.4 | 307.8 |
| response time (ms), 99th percentile | 2388 | 1430 |
| time over the response line (% of samples) | 20.93 | 12.75 |
| failed requests (%) | 11.89 | 10.45 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 0.455 |
| utilisation (used / allocatable) | 0.105 | 0.1043 |
| CPU used (cores), mean | 2.52 | 2.476 |
| Omni's own CPU (cores), mean | 0 | 0.00909 |
| CPU used with Omni's own (cores), mean | 2.52 | 2.485 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.5 | 293.4 |
| HPA replicas, mean | 9.533 | 9.414 |
| pods started | 4.6 | 3.8 |
| pod start wait, total (s) | 16.8 | 11.6 |
| pod start wait, mean (s) | 3.087 | 2.497 |
| host CPU busy, the real machine under kind (%) | 70.95 | 70.16 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.898 | -1.7% | -0.3017 to +0.09714 | no |
| node-hours | 4.515 | 4.435 | -1.8% | -0.2243 to +0.06399 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 519.2 | 517.8 | -0.3% | -2.665 to -0.2304 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519.2 | 512 | -1.4% | -17.68 to +3.214 | no |
| response time (ms), mean | 288.8 | 157.6 | -45.4% | -165.5 to -96.93 | yes, better |
| response time (ms), 95th percentile | 790.4 | 307.8 | -61.1% | -605.8 to -359.5 | yes, better |
| response time (ms), 99th percentile | 2388 | 1430 | -40.1% | -1439 to -477.7 | yes, better |
| time over the response line (% of samples) | 20.93 | 12.75 | -39.1% | -11.03 to -5.314 | yes, better |
| failed requests (%) | 11.89 | 10.45 | -12.1% | -2.316 to -0.5581 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4867 | 0.455 | -6.5% | -0.2743 to +0.211 | no |
| utilisation (used / allocatable) | 0.105 | 0.1043 | -0.7% | -0.003171 to +0.001714 | no |
| CPU used (cores), mean | 2.52 | 2.476 | -1.8% | -0.06168 to -0.02688 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00909 | +0.00909 (native is 0) | +0.007768 to +0.01041 | yes, more |
| CPU used with Omni's own (cores), mean | 2.52 | 2.485 | -1.4% | -0.05226 to -0.01812 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293.5 | 293.4 | -0.1% | -10.15 to +9.805 | no |
| HPA replicas, mean | 9.533 | 9.414 | -1.2% | -0.3086 to +0.07046 | no |
| pods started | 4.6 | 3.8 | -17.4% | -1.679 to +0.07931 | no |
| pod start wait, total (s) | 16.8 | 11.6 | -31.0% | -11.05 to +0.6482 | no |
| pod start wait, mean (s) | 3.087 | 2.497 | -19.1% | -1.467 to +0.2878 | no |
| host CPU busy, the real machine under kind (%) | 70.95 | 70.16 | -1.1% | -1.107 to -0.476 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.2 |  |  | 10 |
| compass | 27.6 | +43.8% | +6.2 to +10.6 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*