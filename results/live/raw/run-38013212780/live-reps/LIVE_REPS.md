# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.9 |
| node-hours | 4.52 | 4.438 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 522.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 516.4 |
| response time (ms), mean | 304.6 | 165.6 |
| response time (ms), 95th percentile | 763 | 332.2 |
| response time (ms), 99th percentile | 2773 | 1497 |
| time over the response line (% of samples) | 23.18 | 14.52 |
| failed requests (%) | 13.96 | 12.11 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.24 | 0.3767 |
| utilisation (used / allocatable) | 0.1118 | 0.1102 |
| CPU used (cores), mean | 2.683 | 2.622 |
| Omni's own CPU (cores), mean | 0 | 0.009567 |
| CPU used with Omni's own (cores), mean | 2.683 | 2.604 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 272.1 | 276.2 |
| HPA replicas, mean | 9.718 | 9.703 |
| pods started | 4.1 | 2.3 |
| pod start wait, total (s) | 12.2 | 7.3 |
| pod start wait, mean (s) | 2.522 | 1.892 |
| host CPU busy, the real machine under kind (%) | 75.2 | 73.78 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.9 | -1.7% | -0.3105 to +0.1108 | no |
| node-hours | 4.52 | 4.438 | -1.8% | -0.242 to +0.07919 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.4 | 522.1 | -0.4% | -3.487 to -1.139 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.4 | 516.4 | -1.5% | -20.81 to +4.926 | no |
| response time (ms), mean | 304.6 | 165.6 | -45.6% | -170.2 to -107.9 | yes, better |
| response time (ms), 95th percentile | 763 | 332.2 | -56.5% | -495.4 to -366.3 | yes, better |
| response time (ms), 99th percentile | 2773 | 1497 | -46.0% | -2381 to -170.5 | yes, better |
| time over the response line (% of samples) | 23.18 | 14.52 | -37.4% | -10.65 to -6.684 | yes, better |
| failed requests (%) | 13.96 | 12.11 | -13.3% | -2.625 to -1.085 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.24 | 0.3767 | +56.9% | -0.1782 to +0.4515 | no |
| utilisation (used / allocatable) | 0.1118 | 0.1102 | -1.4% | -0.002553 to -0.0005804 | yes, less |
| CPU used (cores), mean | 2.683 | 2.622 | -2.3% | -0.09602 to -0.02724 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.009567 | +0.00957 (native is 0) | +0.008442 to +0.01069 | yes, more |
| CPU used with Omni's own (cores), mean | 2.683 | 2.629 | -2.0% | -0.09376 to -0.01477 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 272.1 | 276.2 | +1.5% | +2.356 to +5.932 | yes, more |
| HPA replicas, mean | 9.718 | 9.703 | -0.2% | -0.2337 to +0.203 | no |
| pods started | 4.1 | 2.3 | -43.9% | -2.908 to -0.6919 | yes, better |
| pod start wait, total (s) | 12.2 | 7.3 | -40.2% | -8.91 to -0.8896 | yes, better |
| pod start wait, mean (s) | 2.522 | 1.892 | -25.0% | -1.473 to +0.2131 | no |
| host CPU busy, the real machine under kind (%) | 75.2 | 73.78 | -1.9% | -2.273 to -0.5603 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*