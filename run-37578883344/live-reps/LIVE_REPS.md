# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.911 |
| node-hours | 1.514 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 156.9 |
| response time (ms), mean | 149.9 | 78.52 |
| response time (ms), 95th percentile | 329.4 | 116.1 |
| response time (ms), 99th percentile | 524.1 | 168 |
| time over the response line (% of samples) | 1.648 | 0.04841 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3733 | 0.32 |
| utilisation (used / allocatable) | 0.03835 | 0.03721 |
| CPU used (cores), mean | 0.9204 | 0.88 |
| Omni's own CPU (cores), mean | 0 | 0.00968 |
| CPU used with Omni's own (cores), mean | 0.9204 | 0.8896 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711 | 725.5 |
| HPA replicas, mean | 8.693 | 8.049 |
| pods started | 4.6 | 4.2 |
| pod start wait, total (s) | 16.9 | 14.4 |
| pod start wait, mean (s) | 3.315 | 3.138 |
| host CPU busy, the real machine under kind (%) | 27.89 | 27.11 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.911 | -1.5% | -0.1226 to -0.05477 | yes, better |
| node-hours | 1.514 | 1.491 | -1.5% | -0.03163 to -0.01353 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | -0.3% | -0.6554 to -0.1447 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 156.9 | -1.3% | -2.813 to -1.349 | yes, better |
| response time (ms), mean | 149.9 | 78.52 | -47.6% | -89.51 to -53.22 | yes, better |
| response time (ms), 95th percentile | 329.4 | 116.1 | -64.8% | -267 to -159.8 | yes, better |
| response time (ms), 99th percentile | 524.1 | 168 | -68.0% | -440.9 to -271.4 | yes, better |
| time over the response line (% of samples) | 1.648 | 0.04841 | -97.1% | -2.65 to -0.549 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3733 | 0.32 | -14.3% | -0.2512 to +0.1446 | no |
| utilisation (used / allocatable) | 0.03835 | 0.03721 | -3.0% | -0.002193 to -9.234e-05 | yes, less |
| CPU used (cores), mean | 0.9204 | 0.88 | -4.4% | -0.06682 to -0.01401 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00968 | +0.00968 (native is 0) | +0.008418 to +0.01094 | yes, more |
| CPU used with Omni's own (cores), mean | 0.9204 | 0.8896 | -3.3% | -0.05622 to -0.005251 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711 | 725.5 | +2.0% | -6.322 to +35.26 | no |
| HPA replicas, mean | 8.693 | 8.049 | -7.4% | -0.9762 to -0.3104 | yes, better |
| pods started | 4.6 | 4.2 | -8.7% | -1.528 to +0.7285 | no |
| pod start wait, total (s) | 16.9 | 14.4 | -14.8% | -9.828 to +4.828 | no |
| pod start wait, mean (s) | 3.315 | 3.138 | -5.3% | -1.257 to +0.904 | no |
| host CPU busy, the real machine under kind (%) | 27.89 | 27.11 | -2.8% | -1.476 to -0.0859 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*