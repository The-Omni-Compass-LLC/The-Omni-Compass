# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.5 | 173.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.5 | 173.2 |
| response time (ms), mean | 365.1 | 221.8 |
| response time (ms), 95th percentile | 1144 | 591 |
| response time (ms), 99th percentile | 3664 | 3071 |
| time over the response line (% of samples) | 22.21 | 14.21 |
| failed requests (%) | 10.59 | 9.594 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.55 |
| utilisation (used / allocatable) | 0.1036 | 0.1019 |
| CPU used (cores), mean | 2.487 | 2.444 |
| Omni's own CPU (cores), mean | 0 | 0.01241 |
| CPU used with Omni's own (cores), mean | 2.487 | 2.457 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293 | 297.4 |
| HPA replicas, mean | 9.453 | 9.528 |
| pods started | 5 | 4.2 |
| pod start wait, total (s) | 17.8 | 14.3 |
| pod start wait, mean (s) | 3.239 | 3.053 |
| host CPU busy, the real machine under kind (%) | 70.88 | 70.15 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 34.88 | 35.12 |
| robust: time over the line in the 120 s after the kill (% of samples) | 58.51 | 57.9 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.995e-16 to +2.995e-16 | no |
| node-hours | 1.511 | 1.511 | +0.0% | -0.00526 to +0.00626 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.5 | 173.2 | -0.2% | -1.155 to +0.4561 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.5 | 173.2 | -0.2% | -1.155 to +0.4561 | no |
| response time (ms), mean | 365.1 | 221.8 | -39.2% | -217.6 to -68.93 | yes, better |
| response time (ms), 95th percentile | 1144 | 591 | -48.3% | -1033 to -72.82 | yes, better |
| response time (ms), 99th percentile | 3664 | 3071 | -16.2% | -2266 to +1081 | no |
| time over the response line (% of samples) | 22.21 | 14.21 | -36.0% | -11.28 to -4.738 | yes, better |
| failed requests (%) | 10.59 | 9.594 | -9.4% | -2.459 to +0.4695 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4617 | 0.55 | +19.1% | -0.5234 to +0.7001 | no |
| utilisation (used / allocatable) | 0.1036 | 0.1019 | -1.7% | -0.00278 to -0.0007724 | yes, less |
| CPU used (cores), mean | 2.487 | 2.444 | -1.7% | -0.06671 to -0.01854 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01241 | +0.0124 (native is 0) | +0.01147 to +0.01335 | yes, more |
| CPU used with Omni's own (cores), mean | 2.487 | 2.457 | -1.2% | -0.05428 to -0.00615 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 293 | 297.4 | +1.5% | +0.07352 to +8.686 | yes, more |
| HPA replicas, mean | 9.453 | 9.528 | +0.8% | -0.006863 to +0.1575 | no |
| pods started | 5 | 4.2 | -16.0% | -1.742 to +0.1417 | no |
| pod start wait, total (s) | 17.8 | 14.3 | -19.7% | -9.002 to +2.002 | no |
| pod start wait, mean (s) | 3.239 | 3.053 | -5.7% | -1.187 to +0.8152 | no |
| host CPU busy, the real machine under kind (%) | 70.88 | 70.15 | -1.0% | -1.556 to +0.0907 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 34.88 | 35.12 | +0.7% | -6.336 to +6.829 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 58.51 | 57.9 | -1.0% | -4.89 to +3.676 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*