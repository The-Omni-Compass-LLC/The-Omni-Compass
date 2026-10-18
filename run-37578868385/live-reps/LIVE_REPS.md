# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.885 |
| node-hours | 4.513 | 4.431 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.8 | 512.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.8 | 505.6 |
| response time (ms), mean | 274 | 140.3 |
| response time (ms), 95th percentile | 761 | 281.1 |
| response time (ms), 99th percentile | 2617 | 1420 |
| time over the response line (% of samples) | 16.4 | 9.863 |
| failed requests (%) | 8.391 | 7.681 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3717 | 0.3983 |
| utilisation (used / allocatable) | 0.09569 | 0.09504 |
| CPU used (cores), mean | 2.297 | 2.252 |
| Omni's own CPU (cores), mean | 0 | 0.00912 |
| CPU used with Omni's own (cores), mean | 2.297 | 2.261 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 323.3 | 322.3 |
| HPA replicas, mean | 9.62 | 9.467 |
| pods started | 4.2 | 4.2 |
| pod start wait, total (s) | 14 | 13.8 |
| pod start wait, mean (s) | 2.636 | 2.521 |
| host CPU busy, the real machine under kind (%) | 64.63 | 63.98 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.885 | -1.9% | -0.315 to +0.08512 | no |
| node-hours | 4.513 | 4.431 | -1.8% | -0.2297 to +0.06538 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.8 | 512.1 | -0.1% | -1.719 to +0.3877 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.8 | 505.6 | -1.4% | -17.65 to +3.32 | no |
| response time (ms), mean | 274 | 140.3 | -48.8% | -183.7 to -83.74 | yes, better |
| response time (ms), 95th percentile | 761 | 281.1 | -63.1% | -695.3 to -264.5 | yes, better |
| response time (ms), 99th percentile | 2617 | 1420 | -45.7% | -1825 to -568.9 | yes, better |
| time over the response line (% of samples) | 16.4 | 9.863 | -39.9% | -8.994 to -4.078 | yes, better |
| failed requests (%) | 8.391 | 7.681 | -8.5% | -1.409 to -0.01132 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3717 | 0.3983 | +7.2% | -0.3557 to +0.4091 | no |
| utilisation (used / allocatable) | 0.09569 | 0.09504 | -0.7% | -0.003367 to +0.002067 | no |
| CPU used (cores), mean | 2.297 | 2.252 | -1.9% | -0.06295 to -0.0257 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00912 | +0.00912 (native is 0) | +0.007949 to +0.01029 | yes, more |
| CPU used with Omni's own (cores), mean | 2.297 | 2.261 | -1.5% | -0.05346 to -0.01695 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 323.3 | 322.3 | -0.3% | -14.68 to +12.71 | no |
| HPA replicas, mean | 9.62 | 9.467 | -1.6% | -0.3134 to +0.007675 | no |
| pods started | 4.2 | 4.2 | +0.0% | -1.262 to +1.262 | no |
| pod start wait, total (s) | 14 | 13.8 | -1.4% | -8.52 to +8.12 | no |
| pod start wait, mean (s) | 2.636 | 2.521 | -4.4% | -1.335 to +1.105 | no |
| host CPU busy, the real machine under kind (%) | 64.63 | 63.98 | -1.0% | -1.332 to +0.02955 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*