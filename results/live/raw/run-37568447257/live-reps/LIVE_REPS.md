# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.993 |
| node-hours | 1.512 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.7 | 170.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.7 | 170.5 |
| response time (ms), mean | 428.8 | 397.7 |
| response time (ms), 95th percentile | 1758 | 1752 |
| response time (ms), 99th percentile | 4354 | 4813 |
| time over the response line (% of samples) | 19.74 | 18.33 |
| failed requests (%) | 2.631 | 2.196 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.365 | 1.657 |
| utilisation (used / allocatable) | 0.09052 | 0.09013 |
| CPU used (cores), mean | 2.172 | 2.161 |
| Omni's own CPU (cores), mean | 0 | 0.01274 |
| CPU used with Omni's own (cores), mean | 2.172 | 2.174 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.9 | 323.3 |
| HPA replicas, mean | 14.87 | 14.73 |
| pods started | 4.7 | 4.6 |
| pod start wait, total (s) | 11.9 | 15.3 |
| pod start wait, mean (s) | 2.185 | 2.681 |
| host CPU busy, the real machine under kind (%) | 62.41 | 62.66 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 446.7 | 407.8 |
| second app: response time (ms), 99th percentile | 2763 | 2224 |
| second app: time over the response line (% of samples) | 13.35 | 13.38 |
| second app: failed requests (%) | 10.1 | 10.26 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.993 | -0.1% | -0.02307 to +0.008925 | no |
| node-hours | 1.512 | 1.51 | -0.2% | -0.007571 to +0.003016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 170.7 | 170.6 | -0.0% | -0.7327 to +0.5939 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.7 | 170.5 | -0.1% | -0.8547 to +0.4492 | no |
| response time (ms), mean | 428.8 | 397.7 | -7.2% | -87.97 to +25.82 | no |
| response time (ms), 95th percentile | 1758 | 1752 | -0.3% | -448.8 to +437.5 | no |
| response time (ms), 99th percentile | 4354 | 4813 | +10.5% | -324.8 to +1243 | no |
| time over the response line (% of samples) | 19.74 | 18.33 | -7.1% | -3.201 to +0.3821 | no |
| failed requests (%) | 2.631 | 2.196 | -16.5% | -1.439 to +0.5695 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.365 | 1.657 | +21.4% | -0.678 to +1.261 | no |
| utilisation (used / allocatable) | 0.09052 | 0.09013 | -0.4% | -0.001434 to +0.0006522 | no |
| CPU used (cores), mean | 2.172 | 2.161 | -0.5% | -0.03378 to +0.0107 | no |
| Omni's own CPU (cores), mean | 0 | 0.01274 | +0.0127 (native is 0) | +0.01021 to +0.01527 | yes, more |
| CPU used with Omni's own (cores), mean | 2.172 | 2.174 | +0.1% | -0.01926 to +0.02166 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.9 | 323.3 | +0.1% | -2.742 to +3.597 | no |
| HPA replicas, mean | 14.87 | 14.73 | -1.0% | -0.3556 to +0.06609 | no |
| pods started | 4.7 | 4.6 | -2.1% | -0.9564 to +0.7564 | no |
| pod start wait, total (s) | 11.9 | 15.3 | +28.6% | -0.1237 to +6.924 | no |
| pod start wait, mean (s) | 2.185 | 2.681 | +22.7% | -0.2895 to +1.281 | no |
| host CPU busy, the real machine under kind (%) | 62.41 | 62.66 | +0.4% | -0.31 to +0.7978 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 446.7 | 407.8 | -8.7% | -268.2 to +190.3 | no |
| second app: response time (ms), 99th percentile | 2763 | 2224 | -19.5% | -2207 to +1129 | no |
| second app: time over the response line (% of samples) | 13.35 | 13.38 | +0.2% | -0.8486 to +0.8975 | no |
| second app: failed requests (%) | 10.1 | 10.26 | +1.5% | -0.3124 to +0.6198 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*