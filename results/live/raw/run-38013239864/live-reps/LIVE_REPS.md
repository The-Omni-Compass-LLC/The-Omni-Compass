# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.4 |
| response time (ms), mean | 534.8 | 505.8 |
| response time (ms), 95th percentile | 2338 | 2496 |
| response time (ms), 99th percentile | 5296 | 5768 |
| time over the response line (% of samples) | 24.47 | 23.11 |
| failed requests (%) | 3.962 | 3.32 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6817 | 1.34 |
| utilisation (used / allocatable) | 0.09853 | 0.09765 |
| CPU used (cores), mean | 2.365 | 2.344 |
| Omni's own CPU (cores), mean | 0 | 0.0142 |
| CPU used with Omni's own (cores), mean | 2.365 | 2.358 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.7 | 301.7 |
| HPA replicas, mean | 15.27 | 15.29 |
| pods started | 3.9 | 3.3 |
| pod start wait, total (s) | 6.8 | 7.4 |
| pod start wait, mean (s) | 1.698 | 1.757 |
| host CPU busy, the real machine under kind (%) | 68.37 | 68.38 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 261.3 | 277.8 |
| second app: response time (ms), 99th percentile | 1247 | 889.7 |
| second app: time over the response line (% of samples) | 14.74 | 14.57 |
| second app: failed requests (%) | 13.5 | 13.41 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.788e-16 to +3.235e-16 | same (under one part in a million) |
| node-hours | 1.514 | 1.512 | -0.1% | -0.008365 to +0.006032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.4 | -0.1% | -1.071 to +0.6362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172.4 | -0.1% | -1.071 to +0.6362 | no |
| response time (ms), mean | 534.8 | 505.8 | -5.4% | -73.58 to +15.55 | no |
| response time (ms), 95th percentile | 2338 | 2496 | +6.8% | -283 to +599.1 | no |
| response time (ms), 99th percentile | 5296 | 5768 | +8.9% | -318.5 to +1262 | no |
| time over the response line (% of samples) | 24.47 | 23.11 | -5.5% | -2.967 to +0.2527 | no |
| failed requests (%) | 3.962 | 3.32 | -16.2% | -1.215 to -0.07003 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6817 | 1.34 | +96.6% | -0.0769 to +1.394 | no |
| utilisation (used / allocatable) | 0.09853 | 0.09765 | -0.9% | -0.001527 to -0.0002331 | yes, less |
| CPU used (cores), mean | 2.365 | 2.344 | -0.9% | -0.03666 to -0.005595 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0142 | +0.0142 (native is 0) | +0.01175 to +0.01665 | yes, more |
| CPU used with Omni's own (cores), mean | 2.365 | 2.358 | -0.3% | -0.02265 to +0.008804 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.7 | 301.7 | +1.0% | +0.2811 to +5.811 | yes, more |
| HPA replicas, mean | 15.27 | 15.29 | +0.2% | -0.3039 to +0.3533 | no |
| pods started | 3.9 | 3.3 | -15.4% | -1.566 to +0.3656 | no |
| pod start wait, total (s) | 6.8 | 7.4 | +8.8% | -2.792 to +3.992 | no |
| pod start wait, mean (s) | 1.698 | 1.757 | +3.5% | -0.4979 to +0.6155 | no |
| host CPU busy, the real machine under kind (%) | 68.37 | 68.38 | +0.0% | -0.4351 to +0.4576 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 261.3 | 277.8 | +6.3% | -13.19 to +46.33 | no |
| second app: response time (ms), 99th percentile | 1247 | 889.7 | -28.7% | -1008 to +292.7 | no |
| second app: time over the response line (% of samples) | 14.74 | 14.57 | -1.2% | -0.5005 to +0.1598 | no |
| second app: failed requests (%) | 13.5 | 13.41 | -0.7% | -0.5313 to +0.3449 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*