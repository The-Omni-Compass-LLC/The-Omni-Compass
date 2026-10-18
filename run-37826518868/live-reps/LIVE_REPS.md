# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.649 |
| node-hours | 4.333 | 4.08 |
| energy, parked workers still on at idle power (Wh, declared model) | 482.7 | 480.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.7 | 461.7 |
| response time (ms), mean | 283.7 | 134.7 |
| response time (ms), 95th percentile | 756.5 | 243.4 |
| response time (ms), 99th percentile | 1415 | 553.1 |
| time over the response line (% of samples) | 13.89 | 2.539 |
| failed requests (%) | 1.381 | 1.27 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8517 | 0.9883 |
| utilisation (used / allocatable) | 0.08087 | 0.08145 |
| CPU used (cores), mean | 1.941 | 1.857 |
| Omni's own CPU (cores), mean | 0 | 0.00972 |
| CPU used with Omni's own (cores), mean | 1.941 | 1.866 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 373.6 | 368.3 |
| HPA replicas, mean | 9.749 | 9.282 |
| pods started | 5.5 | 7 |
| pod start wait, total (s) | 20 | 15.8 |
| pod start wait, mean (s) | 3.268 | 2.016 |
| host CPU busy, the real machine under kind (%) | 56.02 | 54.38 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.649 | -5.9% | -0.6322 to -0.0701 | yes, better |
| node-hours | 4.333 | 4.08 | -5.8% | -0.4571 to -0.04783 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 482.7 | 480.8 | -0.4% | -3.356 to -0.4758 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.7 | 461.7 | -4.3% | -35.88 to -5.994 | yes, better |
| response time (ms), mean | 283.7 | 134.7 | -52.5% | -195.6 to -102.4 | yes, better |
| response time (ms), 95th percentile | 756.5 | 243.4 | -67.8% | -663.4 to -362.8 | yes, better |
| response time (ms), 99th percentile | 1415 | 553.1 | -60.9% | -1121 to -603.5 | yes, better |
| time over the response line (% of samples) | 13.89 | 2.539 | -81.7% | -16.13 to -6.559 | yes, better |
| failed requests (%) | 1.381 | 1.27 | -8.0% | -0.2031 to -0.01923 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8517 | 0.9883 | +16.0% | -0.2114 to +0.4847 | no |
| utilisation (used / allocatable) | 0.08087 | 0.08145 | +0.7% | -0.003183 to +0.00436 | no |
| CPU used (cores), mean | 1.941 | 1.857 | -4.3% | -0.1081 to -0.0603 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00972 | +0.00972 (native is 0) | +0.008417 to +0.01102 | yes, more |
| CPU used with Omni's own (cores), mean | 1.941 | 1.866 | -3.8% | -0.09728 to -0.0517 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 373.6 | 368.3 | -1.4% | -21.44 to +10.72 | no |
| HPA replicas, mean | 9.749 | 9.282 | -4.8% | -0.7686 to -0.165 | yes, better |
| pods started | 5.5 | 7 | +27.3% | +0.09951 to +2.9 | yes, worse |
| pod start wait, total (s) | 20 | 15.8 | -21.0% | -10.59 to +2.187 | no |
| pod start wait, mean (s) | 3.268 | 2.016 | -38.3% | -1.971 to -0.5324 | yes, better |
| host CPU busy, the real machine under kind (%) | 56.02 | 54.38 | -2.9% | -2.237 to -1.053 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*