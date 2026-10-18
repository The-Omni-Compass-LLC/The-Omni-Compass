# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.849 |
| node-hours | 4.512 | 4.403 |
| energy, parked workers still on at idle power (Wh, declared model) | 507.7 | 507.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 507.7 | 498.9 |
| response time (ms), mean | 237.9 | 130.4 |
| response time (ms), 95th percentile | 666.6 | 227.9 |
| response time (ms), 99th percentile | 2361 | 1603 |
| time over the response line (% of samples) | 13.92 | 8.166 |
| failed requests (%) | 7.434 | 6.628 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.525 | 0.5083 |
| utilisation (used / allocatable) | 0.0884 | 0.08865 |
| CPU used (cores), mean | 2.122 | 2.086 |
| Omni's own CPU (cores), mean | 0 | 0.00796 |
| CPU used with Omni's own (cores), mean | 2.122 | 2.094 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 351.8 | 350.3 |
| HPA replicas, mean | 9.33 | 9 |
| pods started | 5.4 | 5.3 |
| pod start wait, total (s) | 18.1 | 19.5 |
| pod start wait, mean (s) | 3.036 | 3.229 |
| host CPU busy, the real machine under kind (%) | 60.11 | 59.37 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.849 | -2.5% | -0.3498 to +0.04741 | no |
| node-hours | 4.512 | 4.403 | -2.4% | -0.2552 to +0.03688 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 507.7 | 507.4 | -0.0% | -1.5 to +1.018 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 507.7 | 498.9 | -1.7% | -20.05 to +2.471 | no |
| response time (ms), mean | 237.9 | 130.4 | -45.2% | -150 to -64.83 | yes, better |
| response time (ms), 95th percentile | 666.6 | 227.9 | -65.8% | -630.6 to -246.7 | yes, better |
| response time (ms), 99th percentile | 2361 | 1603 | -32.1% | -1880 to +364.2 | no |
| time over the response line (% of samples) | 13.92 | 8.166 | -41.3% | -8.97 to -2.536 | yes, better |
| failed requests (%) | 7.434 | 6.628 | -10.8% | -1.565 to -0.04728 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.525 | 0.5083 | -3.2% | -0.3073 to +0.274 | no |
| utilisation (used / allocatable) | 0.0884 | 0.08865 | +0.3% | -0.001764 to +0.002265 | no |
| CPU used (cores), mean | 2.122 | 2.086 | -1.7% | -0.06883 to -0.002978 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00796 | +0.00796 (native is 0) | +0.006568 to +0.009352 | yes, more |
| CPU used with Omni's own (cores), mean | 2.122 | 2.094 | -1.3% | -0.06074 to +0.004852 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 351.8 | 350.3 | -0.4% | -9.466 to +6.579 | no |
| HPA replicas, mean | 9.33 | 9 | -3.5% | -0.704 to +0.04331 | no |
| pods started | 5.4 | 5.3 | -1.9% | -0.9564 to +0.7564 | no |
| pod start wait, total (s) | 18.1 | 19.5 | +7.7% | -5.218 to +8.018 | no |
| pod start wait, mean (s) | 3.036 | 3.229 | +6.3% | -0.7035 to +1.089 | no |
| host CPU busy, the real machine under kind (%) | 60.11 | 59.37 | -1.2% | -1.595 to +0.114 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 25.8 |  |  | 10 |
| compass | 34.8 | +34.9% | +6.7 to +11.3 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*