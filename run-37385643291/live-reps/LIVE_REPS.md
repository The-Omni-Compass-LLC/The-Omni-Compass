# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.996 |
| node-hours | 4.515 | 4.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 526.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 525.9 |
| response time (ms), mean | 331.3 | 186 |
| response time (ms), 95th percentile | 824.7 | 344.6 |
| response time (ms), 99th percentile | 3327 | 2209 |
| time over the response line (% of samples) | 25.54 | 16.14 |
| failed requests (%) | 15.33 | 13.4 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5483 | 0.2967 |
| utilisation (used / allocatable) | 0.1178 | 0.1156 |
| CPU used (cores), mean | 2.828 | 2.772 |
| Omni's own CPU (cores), mean | 0 | 0.0099 |
| CPU used with Omni's own (cores), mean | 2.828 | 2.782 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 249.6 | 253.8 |
| HPA replicas, mean | 9.773 | 9.795 |
| pods started | 4 | 2.6 |
| pod start wait, total (s) | 11.2 | 5.7 |
| pod start wait, mean (s) | 2.547 | 1.675 |
| host CPU busy, the real machine under kind (%) | 79.02 | 77.86 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01322 to +0.005113 | no |
| node-hours | 4.515 | 4.509 | -0.1% | -0.01607 to +0.004958 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 526.2 | -0.3% | -2.486 to -1.107 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 525.9 | -0.4% | -2.83 to -1.221 | yes, better |
| response time (ms), mean | 331.3 | 186 | -43.9% | -158.3 to -132.4 | yes, better |
| response time (ms), 95th percentile | 824.7 | 344.6 | -58.2% | -513 to -447.4 | yes, better |
| response time (ms), 99th percentile | 3327 | 2209 | -33.6% | -2027 to -209 | yes, better |
| time over the response line (% of samples) | 25.54 | 16.14 | -36.8% | -10.3 to -8.491 | yes, better |
| failed requests (%) | 15.33 | 13.4 | -12.6% | -2.495 to -1.371 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5483 | 0.2967 | -45.9% | -0.4309 to -0.0724 | yes, less |
| utilisation (used / allocatable) | 0.1178 | 0.1156 | -1.9% | -0.003035 to -0.001501 | yes, less |
| CPU used (cores), mean | 2.828 | 2.772 | -2.0% | -0.07361 to -0.03818 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0099 | +0.0099 (native is 0) | +0.009276 to +0.01052 | yes, more |
| CPU used with Omni's own (cores), mean | 2.828 | 2.782 | -1.6% | -0.06364 to -0.02835 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 249.6 | 253.8 | +1.7% | +2.925 to +5.456 | yes, more |
| HPA replicas, mean | 9.773 | 9.795 | +0.2% | -0.06712 to +0.1113 | no |
| pods started | 4 | 2.6 | -35.0% | -2.916 to +0.1155 | no |
| pod start wait, total (s) | 11.2 | 5.7 | -49.1% | -12.92 to +1.92 | no |
| pod start wait, mean (s) | 2.547 | 1.675 | -34.2% | -1.993 to +0.25 | no |
| host CPU busy, the real machine under kind (%) | 79.02 | 77.86 | -1.5% | -1.51 to -0.8005 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*