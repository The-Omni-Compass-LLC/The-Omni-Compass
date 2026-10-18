# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.897 |
| node-hours | 1.519 | 1.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 156.2 |
| response time (ms), mean | 142.7 | 73.87 |
| response time (ms), 95th percentile | 318.3 | 113.2 |
| response time (ms), 99th percentile | 546.3 | 148.3 |
| time over the response line (% of samples) | 1.837 | 0.02374 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.47 | 0.3433 |
| utilisation (used / allocatable) | 0.03666 | 0.03519 |
| CPU used (cores), mean | 0.8799 | 0.8307 |
| Omni's own CPU (cores), mean | 0 | 0.00979 |
| CPU used with Omni's own (cores), mean | 0.8799 | 0.8404 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.5 | 798.4 |
| HPA replicas, mean | 8.371 | 8.151 |
| pods started | 4.7 | 4.2 |
| pod start wait, total (s) | 15.3 | 15.3 |
| pod start wait, mean (s) | 3.065 | 3.224 |
| host CPU busy, the real machine under kind (%) | 26.57 | 25.57 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.897 | -1.7% | -0.1346 to -0.07107 | yes, better |
| node-hours | 1.519 | 1.488 | -2.0% | -0.046 to -0.01556 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.2 | -0.6% | -2.038 to +0.1635 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 156.2 | -1.8% | -4.28 to -1.486 | yes, better |
| response time (ms), mean | 142.7 | 73.87 | -48.2% | -93.74 to -43.89 | yes, better |
| response time (ms), 95th percentile | 318.3 | 113.2 | -64.4% | -266.9 to -143.3 | yes, better |
| response time (ms), 99th percentile | 546.3 | 148.3 | -72.9% | -537 to -259 | yes, better |
| time over the response line (% of samples) | 1.837 | 0.02374 | -98.7% | -2.958 to -0.6674 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.47 | 0.3433 | -27.0% | -0.3379 to +0.0846 | no |
| utilisation (used / allocatable) | 0.03666 | 0.03519 | -4.0% | -0.002451 to -0.000487 | yes, less |
| CPU used (cores), mean | 0.8799 | 0.8307 | -5.6% | -0.07286 to -0.02562 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00979 | +0.00979 (native is 0) | +0.008132 to +0.01145 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8799 | 0.8404 | -4.5% | -0.06192 to -0.01698 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.5 | 798.4 | +3.1% | +6.769 to +41.12 | yes, more |
| HPA replicas, mean | 8.371 | 8.151 | -2.6% | -0.4674 to +0.02674 | no |
| pods started | 4.7 | 4.2 | -10.6% | -1.408 to +0.4079 | no |
| pod start wait, total (s) | 15.3 | 15.3 | +0.0% | -5.51 to +5.51 | no |
| pod start wait, mean (s) | 3.065 | 3.224 | +5.2% | -0.8812 to +1.2 | no |
| host CPU busy, the real machine under kind (%) | 26.57 | 25.57 | -3.7% | -1.561 to -0.4272 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*