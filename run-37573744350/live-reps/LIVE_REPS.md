# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.993 |
| node-hours | 1.513 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.7 | 172.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.7 | 172.3 |
| response time (ms), mean | 540.5 | 481 |
| response time (ms), 95th percentile | 2303 | 2220 |
| response time (ms), 99th percentile | 5663 | 5833 |
| time over the response line (% of samples) | 24.69 | 22.59 |
| failed requests (%) | 4.373 | 3.764 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9417 | 1.673 |
| utilisation (used / allocatable) | 0.09907 | 0.09778 |
| CPU used (cores), mean | 2.378 | 2.345 |
| Omni's own CPU (cores), mean | 0 | 0.01451 |
| CPU used with Omni's own (cores), mean | 2.378 | 2.359 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.8 | 299.9 |
| HPA replicas, mean | 15.15 | 15.35 |
| pods started | 4.5 | 3.1 |
| pod start wait, total (s) | 9.2 | 9.8 |
| pod start wait, mean (s) | 1.866 | 2.42 |
| host CPU busy, the real machine under kind (%) | 69.1 | 68.67 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 265.5 | 283.1 |
| second app: response time (ms), 99th percentile | 889.7 | 1397 |
| second app: time over the response line (% of samples) | 14.92 | 14.91 |
| second app: failed requests (%) | 13.74 | 13.43 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.993 | -0.1% | -0.02261 to +0.008747 | no |
| node-hours | 1.513 | 1.511 | -0.1% | -0.006389 to +0.003222 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.7 | 172.4 | -0.2% | -0.5619 to -0.007683 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.7 | 172.3 | -0.2% | -0.8873 to +0.05524 | no |
| response time (ms), mean | 540.5 | 481 | -11.0% | -102.8 to -16.4 | yes, better |
| response time (ms), 95th percentile | 2303 | 2220 | -3.6% | -339.2 to +171.9 | no |
| response time (ms), 99th percentile | 5663 | 5833 | +3.0% | -885.4 to +1226 | no |
| time over the response line (% of samples) | 24.69 | 22.59 | -8.5% | -4.36 to +0.1715 | no |
| failed requests (%) | 4.373 | 3.764 | -13.9% | -1.601 to +0.3834 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9417 | 1.673 | +77.7% | -0.01233 to +1.476 | no |
| utilisation (used / allocatable) | 0.09907 | 0.09778 | -1.3% | -0.00179 to -0.000789 | yes, less |
| CPU used (cores), mean | 2.378 | 2.345 | -1.4% | -0.04814 to -0.01741 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01451 | +0.0145 (native is 0) | +0.01214 to +0.01688 | yes, more |
| CPU used with Omni's own (cores), mean | 2.378 | 2.359 | -0.8% | -0.03455 to -0.001987 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.8 | 299.9 | +1.4% | +0.8789 to +7.332 | yes, more |
| HPA replicas, mean | 15.15 | 15.35 | +1.3% | -0.2134 to +0.6014 | no |
| pods started | 4.5 | 3.1 | -31.1% | -2.715 to -0.08536 | yes, better |
| pod start wait, total (s) | 9.2 | 9.8 | +6.5% | -6.491 to +7.691 | no |
| pod start wait, mean (s) | 1.866 | 2.42 | +29.7% | -0.3284 to +1.436 | no |
| host CPU busy, the real machine under kind (%) | 69.1 | 68.67 | -0.6% | -1.031 to +0.1776 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 265.5 | 283.1 | +6.6% | -12.5 to +47.66 | no |
| second app: response time (ms), 99th percentile | 889.7 | 1397 | +57.0% | -408.7 to +1423 | no |
| second app: time over the response line (% of samples) | 14.92 | 14.91 | -0.0% | -0.666 to +0.6515 | no |
| second app: failed requests (%) | 13.74 | 13.43 | -2.3% | -0.6226 to +0.002823 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*