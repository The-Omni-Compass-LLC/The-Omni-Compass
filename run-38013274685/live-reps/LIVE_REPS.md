# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.562 |
| node-hours | 4.336 | 4.017 |
| energy, parked workers still on at idle power (Wh, declared model) | 481.2 | 479 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.2 | 455.3 |
| response time (ms), mean | 260 | 123.1 |
| response time (ms), 95th percentile | 668.2 | 233.4 |
| response time (ms), 99th percentile | 1250 | 479.6 |
| time over the response line (% of samples) | 11.42 | 2.034 |
| failed requests (%) | 1.093 | 0.9279 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5217 | 0.615 |
| utilisation (used / allocatable) | 0.07794 | 0.07998 |
| CPU used (cores), mean | 1.871 | 1.793 |
| Omni's own CPU (cores), mean | 0 | 0.00987 |
| CPU used with Omni's own (cores), mean | 1.871 | 1.803 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 372.6 | 364.2 |
| HPA replicas, mean | 9.816 | 9.44 |
| pods started | 5.2 | 7.3 |
| pod start wait, total (s) | 17.2 | 19.1 |
| pod start wait, mean (s) | 3.019 | 2.361 |
| host CPU busy, the real machine under kind (%) | 54.09 | 52.54 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.562 | -7.3% | -0.7901 to -0.0851 | yes, better |
| node-hours | 4.336 | 4.017 | -7.4% | -0.57 to -0.06868 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 481.2 | 479 | -0.4% | -3.391 to -0.9275 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.2 | 455.3 | -5.4% | -44.21 to -7.56 | yes, better |
| response time (ms), mean | 260 | 123.1 | -52.7% | -174.4 to -99.52 | yes, better |
| response time (ms), 95th percentile | 668.2 | 233.4 | -65.1% | -538.5 to -331.1 | yes, better |
| response time (ms), 99th percentile | 1250 | 479.6 | -61.6% | -992.6 to -548.4 | yes, better |
| time over the response line (% of samples) | 11.42 | 2.034 | -82.2% | -13.87 to -4.892 | yes, better |
| failed requests (%) | 1.093 | 0.9279 | -15.1% | -0.3286 to -0.0009311 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5217 | 0.615 | +17.9% | -0.3515 to +0.5382 | no |
| utilisation (used / allocatable) | 0.07794 | 0.07998 | +2.6% | -0.002422 to +0.006484 | no |
| CPU used (cores), mean | 1.871 | 1.793 | -4.2% | -0.0976 to -0.05806 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00987 | +0.00987 (native is 0) | +0.009063 to +0.01068 | yes, more |
| CPU used with Omni's own (cores), mean | 1.871 | 1.803 | -3.6% | -0.08767 to -0.04825 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 372.6 | 364.2 | -2.3% | -26.56 to +9.73 | no |
| HPA replicas, mean | 9.816 | 9.44 | -3.8% | -0.5261 to -0.2256 | yes, better |
| pods started | 5.2 | 7.3 | +40.4% | +0.8182 to +3.382 | yes, worse |
| pod start wait, total (s) | 17.2 | 19.1 | +11.0% | -5.874 to +9.674 | no |
| pod start wait, mean (s) | 3.019 | 2.361 | -21.8% | -1.413 to +0.09571 | no |
| host CPU busy, the real machine under kind (%) | 54.09 | 52.54 | -2.9% | -2.194 to -0.9003 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*