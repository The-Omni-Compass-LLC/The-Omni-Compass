# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.951 |
| node-hours | 4.508 | 4.481 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.8 | 512.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.8 | 509.8 |
| response time (ms), mean | 262.8 | 140.3 |
| response time (ms), 95th percentile | 694.6 | 275.3 |
| response time (ms), 99th percentile | 2468 | 1346 |
| time over the response line (% of samples) | 17.1 | 10.37 |
| failed requests (%) | 9.422 | 8.326 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4333 | 0.4783 |
| utilisation (used / allocatable) | 0.09684 | 0.095 |
| CPU used (cores), mean | 2.324 | 2.269 |
| Omni's own CPU (cores), mean | 0 | 0.00866 |
| CPU used with Omni's own (cores), mean | 2.324 | 2.277 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.3 | 327.7 |
| HPA replicas, mean | 9.401 | 9.105 |
| pods started | 4.9 | 4.6 |
| pod start wait, total (s) | 17.6 | 14.6 |
| pod start wait, mean (s) | 3.182 | 2.713 |
| host CPU busy, the real machine under kind (%) | 65.27 | 64.27 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.951 | -0.8% | -0.1064 to +0.008416 | no |
| node-hours | 4.508 | 4.481 | -0.6% | -0.07096 to +0.01651 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.8 | 512.6 | -0.0% | -0.8734 to +0.4847 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.8 | 509.8 | -0.6% | -6.163 to +0.2404 | no |
| response time (ms), mean | 262.8 | 140.3 | -46.6% | -164.9 to -79.94 | yes, better |
| response time (ms), 95th percentile | 694.6 | 275.3 | -60.4% | -540.1 to -298.6 | yes, better |
| response time (ms), 99th percentile | 2468 | 1346 | -45.5% | -1955 to -289.8 | yes, better |
| time over the response line (% of samples) | 17.1 | 10.37 | -39.4% | -9.796 to -3.666 | yes, better |
| failed requests (%) | 9.422 | 8.326 | -11.6% | -1.913 to -0.2795 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4333 | 0.4783 | +10.4% | -0.2407 to +0.3307 | no |
| utilisation (used / allocatable) | 0.09684 | 0.095 | -1.9% | -0.002668 to -0.001001 | yes, less |
| CPU used (cores), mean | 2.324 | 2.269 | -2.4% | -0.06579 to -0.04469 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00866 | +0.00866 (native is 0) | +0.007273 to +0.01005 | yes, more |
| CPU used with Omni's own (cores), mean | 2.324 | 2.277 | -2.0% | -0.05663 to -0.03653 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.3 | 327.7 | +1.7% | +3.253 to +7.603 | yes, more |
| HPA replicas, mean | 9.401 | 9.105 | -3.2% | -0.6188 to +0.02604 | no |
| pods started | 4.9 | 4.6 | -6.1% | -1.257 to +0.6567 | no |
| pod start wait, total (s) | 17.6 | 14.6 | -17.0% | -7.611 to +1.611 | no |
| pod start wait, mean (s) | 3.182 | 2.713 | -14.7% | -1.077 to +0.1394 | no |
| host CPU busy, the real machine under kind (%) | 65.27 | 64.27 | -1.5% | -1.407 to -0.5927 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 22.8 |  |  | 10 |
| compass | 32.4 | +42.1% | +6.6 to +12.6 | 10 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*