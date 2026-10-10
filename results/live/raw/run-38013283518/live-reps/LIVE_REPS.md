# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.446 |
| node-hours | 4.334 | 3.935 |
| energy, parked workers still on at idle power (Wh, declared model) | 473.9 | 472.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 473.9 | 442.1 |
| response time (ms), mean | 211 | 101.7 |
| response time (ms), 95th percentile | 538.7 | 180.7 |
| response time (ms), 99th percentile | 1004 | 387.5 |
| time over the response line (% of samples) | 8.712 | 1.639 |
| failed requests (%) | 0.754 | 0.668 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7767 | 0.7983 |
| utilisation (used / allocatable) | 0.06713 | 0.06889 |
| CPU used (cores), mean | 1.611 | 1.527 |
| Omni's own CPU (cores), mean | 0 | 0.00913 |
| CPU used with Omni's own (cores), mean | 1.611 | 1.536 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 444.3 |
| HPA replicas, mean | 9.461 | 8.674 |
| pods started | 7.6 | 8.5 |
| pod start wait, total (s) | 28.3 | 28.4 |
| pod start wait, mean (s) | 3.587 | 2.998 |
| host CPU busy, the real machine under kind (%) | 46.77 | 45.26 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.446 | -9.2% | -0.8866 to -0.2221 | yes, better |
| node-hours | 4.334 | 3.935 | -9.2% | -0.6388 to -0.1596 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 473.9 | 472.1 | -0.4% | -3.355 to -0.1954 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 473.9 | 442.1 | -6.7% | -49.02 to -14.61 | yes, better |
| response time (ms), mean | 211 | 101.7 | -51.8% | -164.9 to -53.66 | yes, better |
| response time (ms), 95th percentile | 538.7 | 180.7 | -66.5% | -519.4 to -196.7 | yes, better |
| response time (ms), 99th percentile | 1004 | 387.5 | -61.4% | -913.2 to -320.7 | yes, better |
| time over the response line (% of samples) | 8.712 | 1.639 | -81.2% | -12.46 to -1.681 | yes, better |
| failed requests (%) | 0.754 | 0.668 | -11.4% | -0.1715 to -0.0004584 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7767 | 0.7983 | +2.8% | -0.2576 to +0.301 | no |
| utilisation (used / allocatable) | 0.06713 | 0.06889 | +2.6% | -0.002487 to +0.006018 | no |
| CPU used (cores), mean | 1.611 | 1.527 | -5.2% | -0.1314 to -0.03702 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00913 | +0.00913 (native is 0) | +0.007257 to +0.011 | yes, more |
| CPU used with Omni's own (cores), mean | 1.611 | 1.536 | -4.7% | -0.1209 to -0.02927 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.1 | 444.3 | -4.1% | -44.45 to +6.84 | no |
| HPA replicas, mean | 9.461 | 8.674 | -8.3% | -1.268 to -0.3061 | yes, better |
| pods started | 7.6 | 8.5 | +11.8% | -0.8011 to +2.601 | no |
| pod start wait, total (s) | 28.3 | 28.4 | +0.4% | -6.969 to +7.169 | no |
| pod start wait, mean (s) | 3.587 | 2.998 | -16.4% | -1.652 to +0.4739 | no |
| host CPU busy, the real machine under kind (%) | 46.77 | 45.26 | -3.2% | -2.797 to -0.2392 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*