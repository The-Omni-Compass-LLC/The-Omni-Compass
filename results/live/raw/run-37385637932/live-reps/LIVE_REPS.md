# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.6 |
| node-hours | 2.518 | 1.927 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 228.2 |
| response time (ms), mean | 475.3 | 414.6 |
| response time (ms), 95th percentile | 2836 | 2800 |
| response time (ms), 99th percentile | 4327 | 4387 |
| time over the response line (% of samples) | 14.93 | 14.34 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 175.4 | 179.9 |
| utilisation (used / allocatable) | 0.0592 | 0.07597 |
| CPU used (cores), mean | 1.421 | 1.404 |
| Omni's own CPU (cores), mean | 0 | 0.01914 |
| CPU used with Omni's own (cores), mean | 1.421 | 1.423 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.3 | 393 |
| HPA replicas, mean | 2.045 | 2.114 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 10.7 |
| pod start wait, mean (s) | 0 | 7.15 |
| host CPU busy, the real machine under kind (%) | 40.59 | 41.47 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 547.7 | 552.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.815 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.6 | -23.3% | -1.723 to -1.077 | yes, better |
| node-hours | 2.518 | 1.927 | -23.5% | -0.7244 to -0.4584 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.2 | -0.1% | -1.107 to +0.7447 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 228.2 | -16.2% | -54.12 to -34.25 | yes, better |
| response time (ms), mean | 475.3 | 414.6 | -12.8% | -73.7 to -47.71 | yes, better |
| response time (ms), 95th percentile | 2836 | 2800 | -1.2% | -201.2 to +130.8 | no |
| response time (ms), 99th percentile | 4327 | 4387 | +1.4% | -193 to +312.7 | no |
| time over the response line (% of samples) | 14.93 | 14.34 | -3.9% | -1.18 to +0.006049 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 175.4 | 179.9 | +2.6% | -0.8948 to +10.01 | no |
| utilisation (used / allocatable) | 0.0592 | 0.07597 | +28.3% | +0.01328 to +0.02026 | yes, more |
| CPU used (cores), mean | 1.421 | 1.404 | -1.2% | -0.03154 to -0.002127 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01914 | +0.0191 (native is 0) | +0.01619 to +0.02209 | yes, more |
| CPU used with Omni's own (cores), mean | 1.421 | 1.423 | +0.2% | -0.01217 to +0.01678 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.3 | 393 | -15.9% | -104.8 to -43.93 | yes, less |
| HPA replicas, mean | 2.045 | 2.114 | +3.4% | -0.217 to +0.3549 | no |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 10.7 | +10.7 (native is 0) | -6.481 to +27.88 | no |
| pod start wait, mean (s) | 0 | 7.15 | +7.15 (native is 0) | -3.633 to +17.93 | no |
| host CPU busy, the real machine under kind (%) | 40.59 | 41.47 | +2.2% | +0.5766 to +1.18 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 547.7 | 552.5 | +0.9% | +1.431 to +8.169 | yes, worse |
| batch: worker machines in service after the queue finished, mean | 6 | 3.815 | -36.4% | -2.543 to -1.827 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*