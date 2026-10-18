# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.851 |
| node-hours | 1.498 | 1.48 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.8 | 164.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.2 | 161.7 |
| response time (ms), mean | 230.8 | 145.9 |
| response time (ms), 95th percentile | 394.4 | 162.7 |
| response time (ms), 99th percentile | 1671 | 1013 |
| time over the response line (% of samples) | 7.267 | 4.825 |
| failed requests (%) | 4.022 | 3.442 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4733 | 0.445 |
| utilisation (used / allocatable) | 0.06451 | 0.06417 |
| CPU used (cores), mean | 1.526 | 1.505 |
| Omni's own CPU (cores), mean | 0 | 0.00846 |
| CPU used with Omni's own (cores), mean | 1.526 | 1.514 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 443.1 |
| HPA replicas, mean | 8.529 | 8.403 |
| pods started | 4.5 | 4.9 |
| pod start wait, total (s) | 24.3 | 24.9 |
| pod start wait, mean (s) | 4.389 | 4 |
| host CPU busy, the real machine under kind (%) | 43.78 | 43.62 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.851 | -1.1% | -0.2142 to +0.08767 | no |
| node-hours | 1.498 | 1.48 | -1.2% | -0.05556 to +0.02073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.8 | 164.5 | -0.2% | -1.2 to +0.596 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.2 | 161.7 | -0.9% | -4.329 to +1.312 | no |
| response time (ms), mean | 230.8 | 145.9 | -36.8% | -148.5 to -21.28 | yes, better |
| response time (ms), 95th percentile | 394.4 | 162.7 | -58.7% | -279 to -184.4 | yes, better |
| response time (ms), 99th percentile | 1671 | 1013 | -39.4% | -1154 to -160.5 | yes, better |
| time over the response line (% of samples) | 7.267 | 4.825 | -33.6% | -3.431 to -1.454 | yes, better |
| failed requests (%) | 4.022 | 3.442 | -14.4% | -1.056 to -0.1038 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4733 | 0.445 | -6.0% | -0.6261 to +0.5695 | no |
| utilisation (used / allocatable) | 0.06451 | 0.06417 | -0.5% | -0.002667 to +0.001991 | no |
| CPU used (cores), mean | 1.526 | 1.505 | -1.4% | -0.06501 to +0.02358 | no |
| Omni's own CPU (cores), mean | 0 | 0.00846 | +0.00846 (native is 0) | +0.007346 to +0.009574 | yes, more |
| CPU used with Omni's own (cores), mean | 1.526 | 1.514 | -0.8% | -0.05584 to +0.03133 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 443.1 | -0.8% | -20.07 to +12.87 | no |
| HPA replicas, mean | 8.529 | 8.403 | -1.5% | -0.4288 to +0.1767 | no |
| pods started | 4.5 | 4.9 | +8.9% | -0.9572 to +1.757 | no |
| pod start wait, total (s) | 24.3 | 24.9 | +2.5% | -30.12 to +31.32 | no |
| pod start wait, mean (s) | 4.389 | 4 | -8.8% | -5.648 to +4.871 | no |
| host CPU busy, the real machine under kind (%) | 43.78 | 43.62 | -0.4% | -1.004 to +0.6843 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 53 | 13.7 |  |
| machine down | omni | 38 | 8.4 | -15 s (-28%) |
| spike | native | 231 | 53.8 |  |
| spike | omni | 203 | 46.9 | -28 s (-12%) |
| runaway pod started | native | 128 | 10.4 |  |
| runaway pod started | omni | 71 | 6.4 | -57 s (-44%) |
| probe blind | native | 71 | 0.9 |  |
| probe blind | omni | 48 | 0.2 | -23 s (-32%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*