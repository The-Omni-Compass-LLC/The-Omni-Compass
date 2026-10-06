# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.917 |
| node-hours | 1.494 | 1.495 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 165.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 164 |
| response time (ms), mean | 208.2 | 128.7 |
| response time (ms), 95th percentile | 361.1 | 130.3 |
| response time (ms), 99th percentile | 1441 | 1333 |
| time over the response line (% of samples) | 7.158 | 5.814 |
| failed requests (%) | 4.721 | 4.457 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3517 | 0.3 |
| utilisation (used / allocatable) | 0.07075 | 0.06951 |
| CPU used (cores), mean | 1.674 | 1.645 |
| Omni's own CPU (cores), mean | 0 | 0.00881 |
| CPU used with Omni's own (cores), mean | 1.674 | 1.654 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 395.3 | 399.8 |
| HPA replicas, mean | 8.838 | 8.913 |
| pods started | 4.6 | 4 |
| pod start wait, total (s) | 14.2 | 12.4 |
| pod start wait, mean (s) | 2.767 | 2.615 |
| host CPU busy, the real machine under kind (%) | 47.88 | 47.18 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.917 | +0.0% | -0.00555 to +0.009052 | no |
| node-hours | 1.494 | 1.495 | +0.1% | -0.007821 to +0.009377 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 165.6 | -0.2% | -1.197 to +0.6816 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 164 | -0.1% | -1.153 to +0.7046 | no |
| response time (ms), mean | 208.2 | 128.7 | -38.2% | -125.4 to -33.53 | yes, better |
| response time (ms), 95th percentile | 361.1 | 130.3 | -63.9% | -267 to -194.5 | yes, better |
| response time (ms), 99th percentile | 1441 | 1333 | -7.5% | -1240 to +1022 | no |
| time over the response line (% of samples) | 7.158 | 5.814 | -18.8% | -1.902 to -0.786 | yes, better |
| failed requests (%) | 4.721 | 4.457 | -5.6% | -0.6732 to +0.1454 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3517 | 0.3 | -14.7% | -0.3215 to +0.2182 | no |
| utilisation (used / allocatable) | 0.07075 | 0.06951 | -1.7% | -0.002376 to -9.007e-05 | yes, less |
| CPU used (cores), mean | 1.674 | 1.645 | -1.7% | -0.05488 to -0.002489 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00881 | +0.00881 (native is 0) | +0.007966 to +0.009654 | yes, more |
| CPU used with Omni's own (cores), mean | 1.674 | 1.654 | -1.2% | -0.04562 to +0.005879 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 395.3 | 399.8 | +1.1% | -3.475 to +12.34 | no |
| HPA replicas, mean | 8.838 | 8.913 | +0.9% | -0.2548 to +0.4065 | no |
| pods started | 4.6 | 4 | -13.0% | -2.224 to +1.024 | no |
| pod start wait, total (s) | 14.2 | 12.4 | -12.7% | -11.37 to +7.772 | no |
| pod start wait, mean (s) | 2.767 | 2.615 | -5.5% | -1.565 to +1.261 | no |
| host CPU busy, the real machine under kind (%) | 47.88 | 47.18 | -1.5% | -1.166 to -0.2285 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 60 | 13.2 |  |
| machine down | omni | 50 | 11.2 | -10 s (-16%) |
| spike | native | 255 | 57.0 |  |
| spike | omni | 251 | 55.1 | -4 s (-1%) |
| runaway pod started | native | 100 | 9.0 |  |
| runaway pod started | omni | 82 | 6.5 | -18 s (-18%) |
| probe blind | native | 59 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | +1 s (+1%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*