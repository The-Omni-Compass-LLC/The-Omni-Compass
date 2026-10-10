# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.881 |
| node-hours | 1.518 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 156.3 |
| response time (ms), mean | 139.9 | 73.29 |
| response time (ms), 95th percentile | 324.6 | 111.6 |
| response time (ms), 99th percentile | 525.3 | 162.8 |
| time over the response line (% of samples) | 2.07 | 0.06032 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.395 |
| utilisation (used / allocatable) | 0.03588 | 0.03449 |
| CPU used (cores), mean | 0.8611 | 0.812 |
| Omni's own CPU (cores), mean | 0 | 0.00939 |
| CPU used with Omni's own (cores), mean | 0.8611 | 0.8214 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.6 | 820.1 |
| HPA replicas, mean | 8.049 | 7.914 |
| pods started | 5.1 | 3.8 |
| pod start wait, total (s) | 22.6 | 15.1 |
| pod start wait, mean (s) | 4.253 | 3.358 |
| host CPU busy, the real machine under kind (%) | 25.98 | 25.2 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.881 | -2.0% | -0.1568 to -0.08158 | yes, better |
| node-hours | 1.518 | 1.489 | -1.9% | -0.03828 to -0.02038 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.6 | -0.2% | -0.8841 to +0.1711 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 156.3 | -1.6% | -3.171 to -2.067 | yes, better |
| response time (ms), mean | 139.9 | 73.29 | -47.6% | -95.62 to -37.6 | yes, better |
| response time (ms), 95th percentile | 324.6 | 111.6 | -65.6% | -292 to -134 | yes, better |
| response time (ms), 99th percentile | 525.3 | 162.8 | -69.0% | -495 to -230.2 | yes, better |
| time over the response line (% of samples) | 2.07 | 0.06032 | -97.1% | -3.305 to -0.7141 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.395 | -21.8% | -0.29 to +0.07003 | no |
| utilisation (used / allocatable) | 0.03588 | 0.03449 | -3.9% | -0.002934 to +0.0001522 | no |
| CPU used (cores), mean | 0.8611 | 0.812 | -5.7% | -0.08525 to -0.01288 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00939 | +0.00939 (native is 0) | +0.007756 to +0.01102 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8611 | 0.8214 | -4.6% | -0.07473 to -0.004619 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 805.6 | 820.1 | +1.8% | -15.13 to +44.13 | no |
| HPA replicas, mean | 8.049 | 7.914 | -1.7% | -0.4277 to +0.1573 | no |
| pods started | 5.1 | 3.8 | -25.5% | -2.195 to -0.4047 | yes, better |
| pod start wait, total (s) | 22.6 | 15.1 | -33.2% | -12.31 to -2.693 | yes, better |
| pod start wait, mean (s) | 4.253 | 3.358 | -21.0% | -1.822 to +0.03157 | no |
| host CPU busy, the real machine under kind (%) | 25.98 | 25.2 | -3.0% | -1.666 to +0.1181 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*