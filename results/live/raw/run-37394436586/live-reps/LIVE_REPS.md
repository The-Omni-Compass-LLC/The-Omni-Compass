# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.967 |
| node-hours | 4.518 | 4.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 514.1 | 512.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.1 | 510.7 |
| response time (ms), mean | 269.2 | 148.5 |
| response time (ms), 95th percentile | 712.1 | 282.5 |
| response time (ms), 99th percentile | 2091 | 1468 |
| time over the response line (% of samples) | 16 | 8.998 |
| failed requests (%) | 7.619 | 6.73 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8217 | 0.5367 |
| utilisation (used / allocatable) | 0.09687 | 0.09494 |
| CPU used (cores), mean | 2.325 | 2.27 |
| Omni's own CPU (cores), mean | 0 | 0.00905 |
| CPU used with Omni's own (cores), mean | 2.325 | 2.279 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.7 | 317.1 |
| HPA replicas, mean | 9.661 | 9.533 |
| pods started | 4.3 | 3.6 |
| pod start wait, total (s) | 14.9 | 13.9 |
| pod start wait, mean (s) | 2.798 | 2.8 |
| host CPU busy, the real machine under kind (%) | 65.35 | 64.33 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.967 | -0.6% | -0.084 to +0.01769 | no |
| node-hours | 4.518 | 4.492 | -0.6% | -0.0629 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 514.1 | 512.6 | -0.3% | -2.003 to -1.002 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.1 | 510.7 | -0.7% | -6.555 to -0.1995 | yes, better |
| response time (ms), mean | 269.2 | 148.5 | -44.8% | -142.7 to -98.71 | yes, better |
| response time (ms), 95th percentile | 712.1 | 282.5 | -60.3% | -510.9 to -348.4 | yes, better |
| response time (ms), 99th percentile | 2091 | 1468 | -29.8% | -886.8 to -358.7 | yes, better |
| time over the response line (% of samples) | 16 | 8.998 | -43.8% | -8.877 to -5.127 | yes, better |
| failed requests (%) | 7.619 | 6.73 | -11.7% | -1.527 to -0.2499 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8217 | 0.5367 | -34.7% | -0.6431 to +0.07311 | no |
| utilisation (used / allocatable) | 0.09687 | 0.09494 | -2.0% | -0.002774 to -0.001102 | yes, less |
| CPU used (cores), mean | 2.325 | 2.27 | -2.4% | -0.08128 to -0.02869 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00905 | +0.00905 (native is 0) | +0.007917 to +0.01018 | yes, more |
| CPU used with Omni's own (cores), mean | 2.325 | 2.279 | -2.0% | -0.07255 to -0.01933 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.7 | 317.1 | +2.4% | +3.078 to +11.79 | yes, more |
| HPA replicas, mean | 9.661 | 9.533 | -1.3% | -0.2903 to +0.03417 | no |
| pods started | 4.3 | 3.6 | -16.3% | -1.769 to +0.369 | no |
| pod start wait, total (s) | 14.9 | 13.9 | -6.7% | -6.918 to +4.918 | no |
| pod start wait, mean (s) | 2.798 | 2.8 | +0.1% | -0.903 to +0.9078 | no |
| host CPU busy, the real machine under kind (%) | 65.35 | 64.33 | -1.6% | -1.667 to -0.3604 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*