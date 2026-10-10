# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.914 |
| node-hours | 1.5 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 163.5 | 162.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.9 | 161.2 |
| response time (ms), mean | 201.7 | 98.59 |
| response time (ms), 95th percentile | 404.8 | 171 |
| response time (ms), 99th percentile | 1569 | 902.2 |
| time over the response line (% of samples) | 6.249 | 3.583 |
| failed requests (%) | 2.804 | 2.417 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6333 | 0.5217 |
| utilisation (used / allocatable) | 0.05749 | 0.05739 |
| CPU used (cores), mean | 1.36 | 1.358 |
| Omni's own CPU (cores), mean | 0 | 0.0073 |
| CPU used with Omni's own (cores), mean | 1.36 | 1.365 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.1 | 492.1 |
| HPA replicas, mean | 8.04 | 8.02 |
| pods started | 5.8 | 5.5 |
| pod start wait, total (s) | 26 | 22.3 |
| pod start wait, mean (s) | 4.176 | 3.541 |
| host CPU busy, the real machine under kind (%) | 39.26 | 39.35 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.916 | 5.914 | -0.0% | -0.005535 to +0.001348 | no |
| node-hours | 1.5 | 1.493 | -0.4% | -0.01461 to +0.001717 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 163.5 | 162.8 | -0.4% | -1.587 to +0.2177 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.9 | 161.2 | -0.4% | -1.607 to +0.1706 | no |
| response time (ms), mean | 201.7 | 98.59 | -51.1% | -153.2 to -52.98 | yes, better |
| response time (ms), 95th percentile | 404.8 | 171 | -57.7% | -292.8 to -174.6 | yes, better |
| response time (ms), 99th percentile | 1569 | 902.2 | -42.5% | -1266 to -68.13 | yes, better |
| time over the response line (% of samples) | 6.249 | 3.583 | -42.7% | -3.677 to -1.656 | yes, better |
| failed requests (%) | 2.804 | 2.417 | -13.8% | -0.7712 to -0.003088 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6333 | 0.5217 | -17.6% | -0.2688 to +0.0455 | no |
| utilisation (used / allocatable) | 0.05749 | 0.05739 | -0.2% | -0.001446 to +0.001246 | no |
| CPU used (cores), mean | 1.36 | 1.358 | -0.2% | -0.03426 to +0.0288 | no |
| Omni's own CPU (cores), mean | 0 | 0.0073 | +0.0073 (native is 0) | +0.006109 to +0.008491 | yes, more |
| CPU used with Omni's own (cores), mean | 1.36 | 1.365 | +0.3% | -0.02621 to +0.03535 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.1 | 492.1 | -0.6% | -14.6 to +8.438 | no |
| HPA replicas, mean | 8.04 | 8.02 | -0.2% | -0.3032 to +0.2632 | no |
| pods started | 5.8 | 5.5 | -5.2% | -1.518 to +0.9181 | no |
| pod start wait, total (s) | 26 | 22.3 | -14.2% | -10.26 to +2.856 | no |
| pod start wait, mean (s) | 4.176 | 3.541 | -15.2% | -1.411 to +0.1401 | no |
| host CPU busy, the real machine under kind (%) | 39.26 | 39.35 | +0.2% | -0.6097 to +0.7777 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 61 | 14.4 |  |
| machine down | omni | 42 | 7.2 | -19 s (-31%) |
| spike | native | 203 | 36.1 |  |
| spike | omni | 153 | 30.3 | -50 s (-25%) |
| runaway pod started | native | 56 | 5.2 |  |
| runaway pod started | omni | 44 | 3.4 | -12 s (-22%) |
| probe blind | native | 63 | 0.4 |  |
| probe blind | omni | 60 | 0.0 | -3 s (-5%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*