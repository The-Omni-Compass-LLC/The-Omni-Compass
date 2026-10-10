# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.851 |
| node-hours | 4.513 | 4.402 |
| energy, parked workers still on at idle power (Wh, declared model) | 514.1 | 512.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.1 | 504.2 |
| response time (ms), mean | 267.9 | 134.6 |
| response time (ms), 95th percentile | 713.9 | 257.9 |
| response time (ms), 99th percentile | 2328 | 1194 |
| time over the response line (% of samples) | 16.83 | 9.833 |
| failed requests (%) | 8.883 | 7.86 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.605 | 0.4767 |
| utilisation (used / allocatable) | 0.09775 | 0.09668 |
| CPU used (cores), mean | 2.346 | 2.283 |
| Omni's own CPU (cores), mean | 0 | 0.00899 |
| CPU used with Omni's own (cores), mean | 2.346 | 2.292 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.7 | 315.9 |
| HPA replicas, mean | 9.586 | 9.475 |
| pods started | 4.9 | 4.2 |
| pod start wait, total (s) | 14.9 | 14.7 |
| pod start wait, mean (s) | 2.827 | 2.749 |
| host CPU busy, the real machine under kind (%) | 65.82 | 64.66 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.851 | -2.5% | -0.3644 to +0.06733 | no |
| node-hours | 4.513 | 4.402 | -2.5% | -0.2734 to +0.05208 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 514.1 | 512.6 | -0.3% | -2.551 to -0.5495 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 514.1 | 504.2 | -1.9% | -22.01 to +2.138 | no |
| response time (ms), mean | 267.9 | 134.6 | -49.8% | -172.3 to -94.33 | yes, better |
| response time (ms), 95th percentile | 713.9 | 257.9 | -63.9% | -562.2 to -349.8 | yes, better |
| response time (ms), 99th percentile | 2328 | 1194 | -48.7% | -1842 to -425.9 | yes, better |
| time over the response line (% of samples) | 16.83 | 9.833 | -41.6% | -9.421 to -4.57 | yes, better |
| failed requests (%) | 8.883 | 7.86 | -11.5% | -1.726 to -0.3214 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.605 | 0.4767 | -21.2% | -0.5882 to +0.3315 | no |
| utilisation (used / allocatable) | 0.09775 | 0.09668 | -1.1% | -0.003597 to +0.001459 | no |
| CPU used (cores), mean | 2.346 | 2.283 | -2.7% | -0.08323 to -0.04337 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00899 | +0.00899 (native is 0) | +0.00782 to +0.01016 | yes, more |
| CPU used with Omni's own (cores), mean | 2.346 | 2.292 | -2.3% | -0.07344 to -0.03518 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 315.7 | 315.9 | +0.1% | -10.02 to +10.36 | no |
| HPA replicas, mean | 9.586 | 9.475 | -1.2% | -0.2881 to +0.06563 | no |
| pods started | 4.9 | 4.2 | -14.3% | -2.092 to +0.6924 | no |
| pod start wait, total (s) | 14.9 | 14.7 | -1.3% | -6.452 to +6.052 | no |
| pod start wait, mean (s) | 2.827 | 2.749 | -2.8% | -0.8437 to +0.687 | no |
| host CPU busy, the real machine under kind (%) | 65.82 | 64.66 | -1.8% | -1.684 to -0.6369 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*