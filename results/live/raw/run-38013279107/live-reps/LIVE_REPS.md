# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.552 |
| node-hours | 4.332 | 4.011 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.4 | 479 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.4 | 454.8 |
| response time (ms), mean | 259 | 125.8 |
| response time (ms), 95th percentile | 665.8 | 239 |
| response time (ms), 99th percentile | 1259 | 502.4 |
| time over the response line (% of samples) | 11.61 | 2.164 |
| failed requests (%) | 1.081 | 0.888 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6283 | 0.7183 |
| utilisation (used / allocatable) | 0.07763 | 0.07953 |
| CPU used (cores), mean | 1.863 | 1.79 |
| Omni's own CPU (cores), mean | 0 | 0.00966 |
| CPU used with Omni's own (cores), mean | 1.863 | 1.8 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 380.9 | 368.1 |
| HPA replicas, mean | 9.786 | 9.342 |
| pods started | 5.2 | 7.4 |
| pod start wait, total (s) | 15.4 | 18.6 |
| pod start wait, mean (s) | 2.792 | 2.23 |
| host CPU busy, the real machine under kind (%) | 53.66 | 52.26 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.552 | -7.5% | -0.8309 to -0.06423 | yes, better |
| node-hours | 4.332 | 4.011 | -7.4% | -0.5999 to -0.04033 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 480.4 | 479 | -0.3% | -2.321 to -0.3957 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.4 | 454.8 | -5.3% | -46.23 to -5.01 | yes, better |
| response time (ms), mean | 259 | 125.8 | -51.4% | -175.1 to -91.29 | yes, better |
| response time (ms), 95th percentile | 665.8 | 239 | -64.1% | -551.3 to -302.3 | yes, better |
| response time (ms), 99th percentile | 1259 | 502.4 | -60.1% | -982.9 to -531.2 | yes, better |
| time over the response line (% of samples) | 11.61 | 2.164 | -81.4% | -14.26 to -4.643 | yes, better |
| failed requests (%) | 1.081 | 0.888 | -17.8% | -0.3476 to -0.0375 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6283 | 0.7183 | +14.3% | -0.3332 to +0.5132 | no |
| utilisation (used / allocatable) | 0.07763 | 0.07953 | +2.4% | -0.00241 to +0.006203 | no |
| CPU used (cores), mean | 1.863 | 1.79 | -3.9% | -0.09425 to -0.05213 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00966 | +0.00966 (native is 0) | +0.008609 to +0.01071 | yes, more |
| CPU used with Omni's own (cores), mean | 1.863 | 1.8 | -3.4% | -0.0841 to -0.04295 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 380.9 | 368.1 | -3.4% | -38.17 to +12.62 | no |
| HPA replicas, mean | 9.786 | 9.342 | -4.5% | -0.6811 to -0.2066 | yes, better |
| pods started | 5.2 | 7.4 | +42.3% | +0.8179 to +3.582 | yes, worse |
| pod start wait, total (s) | 15.4 | 18.6 | +20.8% | -6.336 to +12.74 | no |
| pod start wait, mean (s) | 2.792 | 2.23 | -20.1% | -1.699 to +0.5764 | no |
| host CPU busy, the real machine under kind (%) | 53.66 | 52.26 | -2.6% | -2.003 to -0.8001 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*