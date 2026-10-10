# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.908 |
| node-hours | 1.491 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.7 | 164.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.1 | 162.7 |
| response time (ms), mean | 198 | 114.7 |
| response time (ms), 95th percentile | 373.1 | 139.2 |
| response time (ms), 99th percentile | 1424 | 860.2 |
| time over the response line (% of samples) | 7.04 | 4.622 |
| failed requests (%) | 4.291 | 3.516 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5383 | 0.6683 |
| utilisation (used / allocatable) | 0.06706 | 0.06534 |
| CPU used (cores), mean | 1.586 | 1.544 |
| Omni's own CPU (cores), mean | 0 | 0.00873 |
| CPU used with Omni's own (cores), mean | 1.586 | 1.553 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.6 | 434.9 |
| HPA replicas, mean | 8.667 | 8.649 |
| pods started | 4.8 | 4.2 |
| pod start wait, total (s) | 16.6 | 21 |
| pod start wait, mean (s) | 2.991 | 4.125 |
| host CPU busy, the real machine under kind (%) | 45.44 | 44.6 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.908 | -0.1% | -0.0224 to +0.01188 | no |
| node-hours | 1.491 | 1.491 | -0.0% | -0.00563 to +0.00463 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.7 | 164.4 | -0.2% | -0.7508 to +0.215 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.1 | 162.7 | -0.2% | -0.9308 to +0.195 | no |
| response time (ms), mean | 198 | 114.7 | -42.1% | -127.3 to -39.28 | yes, better |
| response time (ms), 95th percentile | 373.1 | 139.2 | -62.7% | -258.7 to -209.1 | yes, better |
| response time (ms), 99th percentile | 1424 | 860.2 | -39.6% | -1399 to +270.8 | no |
| time over the response line (% of samples) | 7.04 | 4.622 | -34.4% | -3.3 to -1.537 | yes, better |
| failed requests (%) | 4.291 | 3.516 | -18.1% | -1.488 to -0.06335 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5383 | 0.6683 | +24.1% | -0.4505 to +0.7105 | no |
| utilisation (used / allocatable) | 0.06706 | 0.06534 | -2.6% | -0.003256 to -0.0001963 | yes, less |
| CPU used (cores), mean | 1.586 | 1.544 | -2.6% | -0.07786 to -0.006091 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00873 | +0.00873 (native is 0) | +0.007424 to +0.01004 | yes, more |
| CPU used with Omni's own (cores), mean | 1.586 | 1.553 | -2.1% | -0.06843 to +0.001929 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.6 | 434.9 | +1.9% | +1.13 to +15.34 | yes, more |
| HPA replicas, mean | 8.667 | 8.649 | -0.2% | -0.3061 to +0.2715 | no |
| pods started | 4.8 | 4.2 | -12.5% | -1.957 to +0.7572 | no |
| pod start wait, total (s) | 16.6 | 21 | +26.5% | -13.46 to +22.26 | no |
| pod start wait, mean (s) | 2.991 | 4.125 | +37.9% | -2.394 to +4.663 | no |
| host CPU busy, the real machine under kind (%) | 45.44 | 44.6 | -1.8% | -1.684 to +0.01017 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 54 | 13.6 |  |
| machine down | omni | 35 | 8.2 | -19 s (-36%) |
| spike | native | 239 | 53.5 |  |
| spike | omni | 213 | 44.9 | -27 s (-11%) |
| runaway pod started | native | 104 | 9.0 |  |
| runaway pod started | omni | 67 | 5.3 | -37 s (-36%) |
| probe blind | native | 60 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | +0 s (+0%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*