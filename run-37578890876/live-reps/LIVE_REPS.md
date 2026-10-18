# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.5 | 171.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.5 | 171.5 |
| response time (ms), mean | 465.2 | 450.1 |
| response time (ms), 95th percentile | 1903 | 2107 |
| response time (ms), 99th percentile | 4541 | 5132 |
| time over the response line (% of samples) | 21.39 | 21.05 |
| failed requests (%) | 2.702 | 1.892 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7883 | 1.273 |
| utilisation (used / allocatable) | 0.09299 | 0.09286 |
| CPU used (cores), mean | 2.232 | 2.229 |
| Omni's own CPU (cores), mean | 0 | 0.01362 |
| CPU used with Omni's own (cores), mean | 2.232 | 2.242 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 313 | 313 |
| HPA replicas, mean | 15.03 | 14.97 |
| pods started | 5.1 | 4.7 |
| pod start wait, total (s) | 13.3 | 11.7 |
| pod start wait, mean (s) | 2.323 | 2.044 |
| host CPU busy, the real machine under kind (%) | 64.29 | 64.89 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 450.9 | 545.3 |
| second app: response time (ms), 99th percentile | 2426 | 2486 |
| second app: time over the response line (% of samples) | 14.09 | 14.1 |
| second app: failed requests (%) | 10.56 | 11.1 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.84e-16 to +9.583e-17 | same (under one part in a million) |
| node-hours | 1.515 | 1.515 | +0.0% | -0.003728 to +0.003728 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 171.5 | 171.5 | -0.0% | -0.5189 to +0.495 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.5 | 171.5 | -0.0% | -0.5189 to +0.495 | no |
| response time (ms), mean | 465.2 | 450.1 | -3.2% | -66.44 to +36.32 | no |
| response time (ms), 95th percentile | 1903 | 2107 | +10.8% | -52.97 to +462.5 | no |
| response time (ms), 99th percentile | 4541 | 5132 | +13.0% | +95.24 to +1088 | yes, worse |
| time over the response line (% of samples) | 21.39 | 21.05 | -1.6% | -3.438 to +2.756 | no |
| failed requests (%) | 2.702 | 1.892 | -30.0% | -1.677 to +0.05775 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7883 | 1.273 | +61.5% | -0.09001 to +1.06 | no |
| utilisation (used / allocatable) | 0.09299 | 0.09286 | -0.1% | -0.001937 to +0.001662 | no |
| CPU used (cores), mean | 2.232 | 2.229 | -0.1% | -0.04648 to +0.03989 | no |
| Omni's own CPU (cores), mean | 0 | 0.01362 | +0.0136 (native is 0) | +0.01131 to +0.01593 | yes, more |
| CPU used with Omni's own (cores), mean | 2.232 | 2.242 | +0.5% | -0.0328 to +0.05345 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 313 | 313 | +0.0% | -6.133 to +6.163 | no |
| HPA replicas, mean | 15.03 | 14.97 | -0.4% | -0.4304 to +0.3182 | no |
| pods started | 5.1 | 4.7 | -7.8% | -1.757 to +0.9572 | no |
| pod start wait, total (s) | 13.3 | 11.7 | -12.0% | -4.89 to +1.69 | no |
| pod start wait, mean (s) | 2.323 | 2.044 | -12.0% | -0.7424 to +0.1833 | no |
| host CPU busy, the real machine under kind (%) | 64.29 | 64.89 | +0.9% | -0.3235 to +1.523 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 450.9 | 545.3 | +20.9% | -256.2 to +444.9 | no |
| second app: response time (ms), 99th percentile | 2426 | 2486 | +2.5% | -1370 to +1491 | no |
| second app: time over the response line (% of samples) | 14.09 | 14.1 | +0.1% | -0.8823 to +0.8972 | no |
| second app: failed requests (%) | 10.56 | 11.1 | +5.1% | -0.3386 to +1.421 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*