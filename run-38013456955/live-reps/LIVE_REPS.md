# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.3 |
| response time (ms), mean | 366.9 | 222 |
| response time (ms), 95th percentile | 1092 | 635.4 |
| response time (ms), 99th percentile | 3354 | 2793 |
| time over the response line (% of samples) | 25.8 | 17.45 |
| failed requests (%) | 14 | 12.79 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6233 | 0.425 |
| utilisation (used / allocatable) | 0.1077 | 0.1062 |
| CPU used (cores), mean | 2.584 | 2.55 |
| Omni's own CPU (cores), mean | 0 | 0.01324 |
| CPU used with Omni's own (cores), mean | 2.584 | 2.563 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 288.5 | 290 |
| HPA replicas, mean | 9.428 | 9.606 |
| pods started | 5.3 | 3.6 |
| pod start wait, total (s) | 19.8 | 13.6 |
| pod start wait, mean (s) | 3.548 | 2.324 |
| host CPU busy, the real machine under kind (%) | 73.89 | 73.76 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 51.36 | 50.91 |
| robust: time over the line in the 120 s after the kill (% of samples) | 65.32 | 64.17 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +8.869e-17 to +9.771e-16 | same (under one part in a million) |
| node-hours | 1.513 | 1.513 | +0.0% | -0.006541 to +0.006874 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.3 | -0.2% | -0.8795 to +0.3351 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.3 | -0.2% | -0.8795 to +0.3351 | no |
| response time (ms), mean | 366.9 | 222 | -39.5% | -209.6 to -80.34 | yes, better |
| response time (ms), 95th percentile | 1092 | 635.4 | -41.8% | -677.4 to -236.3 | yes, better |
| response time (ms), 99th percentile | 3354 | 2793 | -16.7% | -1699 to +577.2 | no |
| time over the response line (% of samples) | 25.8 | 17.45 | -32.4% | -11.86 to -4.839 | yes, better |
| failed requests (%) | 14 | 12.79 | -8.6% | -2.258 to -0.1466 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6233 | 0.425 | -31.8% | -0.6435 to +0.2468 | no |
| utilisation (used / allocatable) | 0.1077 | 0.1062 | -1.4% | -0.00291 to -1.741e-06 | yes, less |
| CPU used (cores), mean | 2.584 | 2.55 | -1.4% | -0.06984 to -4.179e-05 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01324 | +0.0132 (native is 0) | +0.01217 to +0.01431 | yes, more |
| CPU used with Omni's own (cores), mean | 2.584 | 2.563 | -0.8% | -0.05585 to +0.01245 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 288.5 | 290 | +0.5% | -3.048 to +5.975 | no |
| HPA replicas, mean | 9.428 | 9.606 | +1.9% | +0.08073 to +0.2737 | yes, worse |
| pods started | 5.3 | 3.6 | -32.1% | -3.172 to -0.2283 | yes, better |
| pod start wait, total (s) | 19.8 | 13.6 | -31.3% | -14.97 to +2.572 | no |
| pod start wait, mean (s) | 3.548 | 2.324 | -34.5% | -2.461 to +0.01194 | no |
| host CPU busy, the real machine under kind (%) | 73.89 | 73.76 | -0.2% | -0.9643 to +0.7158 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 51.36 | 50.91 | -0.9% | -8.537 to +7.62 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 65.32 | 64.17 | -1.8% | -5.556 to +3.261 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*