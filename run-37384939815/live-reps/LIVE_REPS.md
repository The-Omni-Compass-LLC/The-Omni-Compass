# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.884 |
| node-hours | 1.519 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.6 | 160.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.6 | 157.9 |
| response time (ms), mean | 176.5 | 87.07 |
| response time (ms), 95th percentile | 388 | 121.7 |
| response time (ms), 99th percentile | 630.2 | 169.4 |
| time over the response line (% of samples) | 2.768 | 0.04863 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.1617 |
| utilisation (used / allocatable) | 0.0426 | 0.04137 |
| CPU used (cores), mean | 1.022 | 0.9734 |
| Omni's own CPU (cores), mean | 0 | 0.01063 |
| CPU used with Omni's own (cores), mean | 1.022 | 0.9841 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 637.3 | 656.7 |
| HPA replicas, mean | 9.054 | 8.942 |
| pods started | 3.8 | 2.9 |
| pod start wait, total (s) | 10.6 | 8.2 |
| pod start wait, mean (s) | 2.37 | 2.04 |
| host CPU busy, the real machine under kind (%) | 30.87 | 29.92 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.884 | -1.9% | -0.1217 to -0.1113 | yes, better |
| node-hours | 1.519 | 1.489 | -2.0% | -0.03307 to -0.0266 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 160.6 | 160.1 | -0.3% | -0.8783 to -0.07637 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.6 | 157.9 | -1.7% | -3.102 to -2.278 | yes, better |
| response time (ms), mean | 176.5 | 87.07 | -50.7% | -110 to -68.74 | yes, better |
| response time (ms), 95th percentile | 388 | 121.7 | -68.6% | -332.2 to -200.5 | yes, better |
| response time (ms), 99th percentile | 630.2 | 169.4 | -73.1% | -574.3 to -347.2 | yes, better |
| time over the response line (% of samples) | 2.768 | 0.04863 | -98.2% | -4.009 to -1.43 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1883 | 0.1617 | -14.2% | -0.1424 to +0.08908 | no |
| utilisation (used / allocatable) | 0.0426 | 0.04137 | -2.9% | -0.002044 to -0.0004263 | yes, less |
| CPU used (cores), mean | 1.022 | 0.9734 | -4.8% | -0.06942 to -0.02864 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01063 | +0.0106 (native is 0) | +0.009951 to +0.01131 | yes, more |
| CPU used with Omni's own (cores), mean | 1.022 | 0.9841 | -3.8% | -0.05835 to -0.01844 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 637.3 | 656.7 | +3.0% | +6.688 to +32.03 | yes, more |
| HPA replicas, mean | 9.054 | 8.942 | -1.2% | -0.3917 to +0.1665 | no |
| pods started | 3.8 | 2.9 | -23.7% | -1.99 to +0.19 | no |
| pod start wait, total (s) | 10.6 | 8.2 | -22.6% | -7.787 to +2.987 | no |
| pod start wait, mean (s) | 2.37 | 2.04 | -13.9% | -1.14 to +0.4802 | no |
| host CPU busy, the real machine under kind (%) | 30.87 | 29.92 | -3.1% | -1.496 to -0.4005 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*