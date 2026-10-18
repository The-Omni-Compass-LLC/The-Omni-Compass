# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.9 |
| node-hours | 1.493 | 1.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.5 | 163 |
| response time (ms), mean | 206.9 | 122.6 |
| response time (ms), 95th percentile | 374.8 | 199.6 |
| response time (ms), 99th percentile | 1167 | 631.6 |
| time over the response line (% of samples) | 7.153 | 5.549 |
| failed requests (%) | 4.414 | 4.09 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.655 |
| utilisation (used / allocatable) | 0.06819 | 0.06774 |
| CPU used (cores), mean | 1.613 | 1.6 |
| Omni's own CPU (cores), mean | 0 | 0.00912 |
| CPU used with Omni's own (cores), mean | 1.613 | 1.609 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417 | 417.2 |
| HPA replicas, mean | 8.658 | 8.646 |
| pods started | 4.9 | 4.3 |
| pod start wait, total (s) | 17.6 | 20.3 |
| pod start wait, mean (s) | 3.186 | 4.068 |
| host CPU busy, the real machine under kind (%) | 46.15 | 46.09 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.9 | -0.3% | -0.03646 to +0.004931 | no |
| node-hours | 1.493 | 1.488 | -0.3% | -0.01234 to +0.002396 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.9 | -0.2% | -1.326 to +0.8081 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.5 | 163 | -0.3% | -1.449 to +0.3354 | no |
| response time (ms), mean | 206.9 | 122.6 | -40.8% | -145.8 to -22.88 | yes, better |
| response time (ms), 95th percentile | 374.8 | 199.6 | -46.7% | -268.1 to -82.29 | yes, better |
| response time (ms), 99th percentile | 1167 | 631.6 | -45.9% | -710.1 to -360.3 | yes, better |
| time over the response line (% of samples) | 7.153 | 5.549 | -22.4% | -2.858 to -0.3498 | yes, better |
| failed requests (%) | 4.414 | 4.09 | -7.3% | -1.021 to +0.3732 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.655 | +41.9% | -0.4403 to +0.827 | no |
| utilisation (used / allocatable) | 0.06819 | 0.06774 | -0.7% | -0.001982 to +0.001087 | no |
| CPU used (cores), mean | 1.613 | 1.6 | -0.9% | -0.04839 to +0.02079 | no |
| Omni's own CPU (cores), mean | 0 | 0.00912 | +0.00912 (native is 0) | +0.008378 to +0.009862 | yes, more |
| CPU used with Omni's own (cores), mean | 1.613 | 1.609 | -0.3% | -0.03907 to +0.02971 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417 | 417.2 | +0.1% | -8.134 to +8.611 | no |
| HPA replicas, mean | 8.658 | 8.646 | -0.1% | -0.358 to +0.3337 | no |
| pods started | 4.9 | 4.3 | -12.2% | -1.957 to +0.7572 | no |
| pod start wait, total (s) | 17.6 | 20.3 | +15.3% | -19.15 to +24.55 | no |
| pod start wait, mean (s) | 3.186 | 4.068 | +27.7% | -3.25 to +5.013 | no |
| host CPU busy, the real machine under kind (%) | 46.15 | 46.09 | -0.1% | -0.8766 to +0.7473 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 46 | 13.2 |  |
| machine down | omni | 35 | 10.1 | -12 s (-25%) |
| spike | native | 240 | 53.2 |  |
| spike | omni | 231 | 50.5 | -9 s (-4%) |
| runaway pod started | native | 86 | 9.8 |  |
| runaway pod started | omni | 83 | 6.9 | -3 s (-4%) |
| probe blind | native | 62 | 0.4 |  |
| probe blind | omni | 60 | 0.1 | -2 s (-3%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*