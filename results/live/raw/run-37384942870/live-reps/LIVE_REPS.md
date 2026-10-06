# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.953 |
| node-hours | 4.517 | 4.478 |
| energy, parked workers still on at idle power (Wh, declared model) | 519 | 517.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519 | 514.6 |
| response time (ms), mean | 283.1 | 151.6 |
| response time (ms), 95th percentile | 737.7 | 321.4 |
| response time (ms), 99th percentile | 2520 | 1469 |
| time over the response line (% of samples) | 18.78 | 11.86 |
| failed requests (%) | 10.49 | 9.266 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.74 | 0.555 |
| utilisation (used / allocatable) | 0.1043 | 0.1027 |
| CPU used (cores), mean | 2.503 | 2.453 |
| Omni's own CPU (cores), mean | 0 | 0.00938 |
| CPU used with Omni's own (cores), mean | 2.503 | 2.462 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.9 | 293 |
| HPA replicas, mean | 9.666 | 9.574 |
| pods started | 4.8 | 4.2 |
| pod start wait, total (s) | 16.7 | 14.3 |
| pod start wait, mean (s) | 3.065 | 2.895 |
| host CPU busy, the real machine under kind (%) | 70.05 | 69.15 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.953 | -0.8% | -0.1316 to +0.03677 | no |
| node-hours | 4.517 | 4.478 | -0.9% | -0.09981 to +0.02198 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 519 | 517.3 | -0.3% | -2.818 to -0.6284 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 519 | 514.6 | -0.8% | -8.54 to -0.2688 | yes, better |
| response time (ms), mean | 283.1 | 151.6 | -46.4% | -158.8 to -104.2 | yes, better |
| response time (ms), 95th percentile | 737.7 | 321.4 | -56.4% | -491.3 to -341.3 | yes, better |
| response time (ms), 99th percentile | 2520 | 1469 | -41.7% | -1753 to -347.6 | yes, better |
| time over the response line (% of samples) | 18.78 | 11.86 | -36.8% | -8.688 to -5.142 | yes, better |
| failed requests (%) | 10.49 | 9.266 | -11.7% | -1.944 to -0.5094 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.74 | 0.555 | -25.0% | -0.6327 to +0.2627 | no |
| utilisation (used / allocatable) | 0.1043 | 0.1027 | -1.5% | -0.003089 to -5.008e-05 | yes, less |
| CPU used (cores), mean | 2.503 | 2.453 | -2.0% | -0.07018 to -0.02945 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00938 | +0.00938 (native is 0) | +0.008382 to +0.01038 | yes, more |
| CPU used with Omni's own (cores), mean | 2.503 | 2.462 | -1.6% | -0.06006 to -0.02081 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.9 | 293 | +0.7% | -3.946 to +8.044 | no |
| HPA replicas, mean | 9.666 | 9.574 | -1.0% | -0.2339 to +0.04963 | no |
| pods started | 4.8 | 4.2 | -12.5% | -1.728 to +0.5285 | no |
| pod start wait, total (s) | 16.7 | 14.3 | -14.4% | -7.593 to +2.793 | no |
| pod start wait, mean (s) | 3.065 | 2.895 | -5.5% | -0.9117 to +0.5727 | no |
| host CPU busy, the real machine under kind (%) | 70.05 | 69.15 | -1.3% | -1.424 to -0.3763 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*