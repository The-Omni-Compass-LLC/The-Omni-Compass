# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.637 |
| node-hours | 4.333 | 4.069 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.5 | 478 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.5 | 458.3 |
| response time (ms), mean | 277.8 | 125.5 |
| response time (ms), 95th percentile | 713.9 | 208.6 |
| response time (ms), 99th percentile | 1515 | 590.3 |
| time over the response line (% of samples) | 13.21 | 2.142 |
| failed requests (%) | 1.194 | 0.9906 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.77 | 0.74 |
| utilisation (used / allocatable) | 0.0775 | 0.07782 |
| CPU used (cores), mean | 1.86 | 1.766 |
| Omni's own CPU (cores), mean | 0 | 0.00909 |
| CPU used with Omni's own (cores), mean | 1.86 | 1.775 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.2 | 396.1 |
| HPA replicas, mean | 9.674 | 9.074 |
| pods started | 5.2 | 7 |
| pod start wait, total (s) | 19 | 20.5 |
| pod start wait, mean (s) | 2.613 | 2.579 |
| host CPU busy, the real machine under kind (%) | 53.91 | 51.65 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.637 | -6.1% | -0.5178 to -0.2084 | yes, better |
| node-hours | 4.333 | 4.069 | -6.1% | -0.3735 to -0.1546 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 480.5 | 478 | -0.5% | -4.221 to -0.8151 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.5 | 458.3 | -4.6% | -29.89 to -14.5 | yes, better |
| response time (ms), mean | 277.8 | 125.5 | -54.8% | -217.8 to -86.91 | yes, better |
| response time (ms), 95th percentile | 713.9 | 208.6 | -70.8% | -715.3 to -295.3 | yes, better |
| response time (ms), 99th percentile | 1515 | 590.3 | -61.0% | -1381 to -468.3 | yes, better |
| time over the response line (% of samples) | 13.21 | 2.142 | -83.8% | -17.21 to -4.914 | yes, better |
| failed requests (%) | 1.194 | 0.9906 | -17.0% | -0.3706 to -0.03582 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.77 | 0.74 | -3.9% | -0.5263 to +0.4663 | no |
| utilisation (used / allocatable) | 0.0775 | 0.07782 | +0.4% | -0.001941 to +0.002576 | no |
| CPU used (cores), mean | 1.86 | 1.766 | -5.0% | -0.1351 to -0.0523 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00909 | +0.00909 (native is 0) | +0.00756 to +0.01062 | yes, more |
| CPU used with Omni's own (cores), mean | 1.86 | 1.775 | -4.5% | -0.1249 to -0.04436 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 400.2 | 396.1 | -1.0% | -16.36 to +8.141 | no |
| HPA replicas, mean | 9.674 | 9.074 | -6.2% | -0.9418 to -0.2591 | yes, better |
| pods started | 5.2 | 7 | +34.6% | +0.1899 to +3.41 | yes, worse |
| pod start wait, total (s) | 19 | 20.5 | +7.9% | -5.101 to +8.101 | no |
| pod start wait, mean (s) | 2.613 | 2.579 | -1.3% | -1.16 to +1.091 | no |
| host CPU busy, the real machine under kind (%) | 53.91 | 51.65 | -4.2% | -3.533 to -0.9825 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*