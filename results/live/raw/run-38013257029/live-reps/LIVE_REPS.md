# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.841 |
| node-hours | 1.5 | 1.478 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 165.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 162.2 |
| response time (ms), mean | 189.9 | 126.1 |
| response time (ms), 95th percentile | 343.9 | 131.9 |
| response time (ms), 99th percentile | 1394 | 1163 |
| time over the response line (% of samples) | 6.943 | 5.093 |
| failed requests (%) | 4.428 | 3.76 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4533 | 0.3733 |
| utilisation (used / allocatable) | 0.06785 | 0.06718 |
| CPU used (cores), mean | 1.605 | 1.575 |
| Omni's own CPU (cores), mean | 0 | 0.00913 |
| CPU used with Omni's own (cores), mean | 1.605 | 1.584 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.8 | 419.3 |
| HPA replicas, mean | 8.582 | 8.632 |
| pods started | 5 | 4.7 |
| pod start wait, total (s) | 24.4 | 13.9 |
| pod start wait, mean (s) | 4.524 | 2.652 |
| host CPU busy, the real machine under kind (%) | 45.92 | 45.29 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.841 | -1.2% | -0.2226 to +0.075 | no |
| node-hours | 1.5 | 1.478 | -1.5% | -0.06035 to +0.01607 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 165.2 | -0.4% | -1.409 to +0.1265 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 162.2 | -1.2% | -4.846 to +0.7673 | no |
| response time (ms), mean | 189.9 | 126.1 | -33.6% | -107.3 to -20.35 | yes, better |
| response time (ms), 95th percentile | 343.9 | 131.9 | -61.7% | -264.2 to -159.9 | yes, better |
| response time (ms), 99th percentile | 1394 | 1163 | -16.5% | -1150 to +689.2 | no |
| time over the response line (% of samples) | 6.943 | 5.093 | -26.6% | -3.078 to -0.6221 | yes, better |
| failed requests (%) | 4.428 | 3.76 | -15.1% | -1.29 to -0.04705 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4533 | 0.3733 | -17.6% | -0.3064 to +0.1464 | no |
| utilisation (used / allocatable) | 0.06785 | 0.06718 | -1.0% | -0.003027 to +0.001693 | no |
| CPU used (cores), mean | 1.605 | 1.575 | -1.9% | -0.07172 to +0.01085 | no |
| Omni's own CPU (cores), mean | 0 | 0.00913 | +0.00913 (native is 0) | +0.008191 to +0.01007 | yes, more |
| CPU used with Omni's own (cores), mean | 1.605 | 1.584 | -1.3% | -0.06238 to +0.01976 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.8 | 419.3 | +0.1% | -14.3 to +15.21 | no |
| HPA replicas, mean | 8.582 | 8.632 | +0.6% | -0.2626 to +0.3624 | no |
| pods started | 5 | 4.7 | -6.0% | -1.733 to +1.133 | no |
| pod start wait, total (s) | 24.4 | 13.9 | -43.0% | -31.28 to +10.28 | no |
| pod start wait, mean (s) | 4.524 | 2.652 | -41.4% | -5.937 to +2.194 | no |
| host CPU busy, the real machine under kind (%) | 45.92 | 45.29 | -1.4% | -1.439 to +0.1785 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 50 | 13.2 |  |
| machine down | omni | 30 | 8.8 | -19 s (-39%) |
| spike | native | 243 | 54.5 |  |
| spike | omni | 226 | 51.9 | -18 s (-7%) |
| runaway pod started | native | 84 | 8.5 |  |
| runaway pod started | omni | 73 | 6.4 | -11 s (-13%) |
| probe blind | native | 63 | 0.1 |  |
| probe blind | omni | 60 | 0.1 | -2 s (-4%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*