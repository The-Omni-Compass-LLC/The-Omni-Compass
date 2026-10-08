# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.2 |
| response time (ms), mean | 351.3 | 220.3 |
| response time (ms), 95th percentile | 1083 | 599.8 |
| response time (ms), 99th percentile | 3283 | 2875 |
| time over the response line (% of samples) | 27.82 | 18.7 |
| failed requests (%) | 16.54 | 14.43 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.54 | 0.2667 |
| utilisation (used / allocatable) | 0.1083 | 0.1065 |
| CPU used (cores), mean | 2.6 | 2.556 |
| Omni's own CPU (cores), mean | 0 | 0.0134 |
| CPU used with Omni's own (cores), mean | 2.6 | 2.57 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.7 | 300.9 |
| HPA replicas, mean | 9.536 | 9.489 |
| pods started | 4.1 | 4 |
| pod start wait, total (s) | 16.6 | 15.3 |
| pod start wait, mean (s) | 3.067 | 3.003 |
| host CPU busy, the real machine under kind (%) | 74.36 | 74.01 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 59.05 | 57.45 |
| robust: time over the line in the 120 s after the kill (% of samples) | 69.1 | 68.04 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | no |
| node-hours | 1.511 | 1.511 | +0.0% | -0.003026 to +0.003026 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.2 | -0.2% | -0.8444 to -0.003718 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.2 | -0.2% | -0.8444 to -0.003718 | yes, better |
| response time (ms), mean | 351.3 | 220.3 | -37.3% | -196.1 to -66.03 | yes, better |
| response time (ms), 95th percentile | 1083 | 599.8 | -44.6% | -940.1 to -26.12 | yes, better |
| response time (ms), 99th percentile | 3283 | 2875 | -12.4% | -1525 to +708.7 | no |
| time over the response line (% of samples) | 27.82 | 18.7 | -32.8% | -13.15 to -5.08 | yes, better |
| failed requests (%) | 16.54 | 14.43 | -12.7% | -3.432 to -0.7825 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.54 | 0.2667 | -50.6% | -0.689 to +0.1423 | no |
| utilisation (used / allocatable) | 0.1083 | 0.1065 | -1.7% | -0.002586 to -0.001063 | yes, less |
| CPU used (cores), mean | 2.6 | 2.556 | -1.7% | -0.06206 to -0.02551 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0134 | +0.0134 (native is 0) | +0.01215 to +0.01465 | yes, more |
| CPU used with Omni's own (cores), mean | 2.6 | 2.57 | -1.2% | -0.04858 to -0.01219 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.7 | 300.9 | +1.7% | -0.1414 to +10.45 | no |
| HPA replicas, mean | 9.536 | 9.489 | -0.5% | -0.1619 to +0.06654 | no |
| pods started | 4.1 | 4 | -2.4% | -1.137 to +0.9366 | no |
| pod start wait, total (s) | 16.6 | 15.3 | -7.8% | -8.93 to +6.33 | no |
| pod start wait, mean (s) | 3.067 | 3.003 | -2.1% | -1.177 to +1.048 | no |
| host CPU busy, the real machine under kind (%) | 74.36 | 74.01 | -0.5% | -0.9514 to +0.2466 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 59.05 | 57.45 | -2.7% | -10.33 to +7.145 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 69.1 | 68.04 | -1.5% | -5.226 to +3.108 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`).

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions |
|---|---:|---|---:|---|---|---:|---:|---:|
| omni | 1 | kill | 8 | yes | yes | 1 |  | 14 |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 3 | kill | 7 | yes | yes | 1 |  | 14 |
| omni | 4 | kill | 8 | yes | yes | 1 |  | 14 |
| omni | 5 | kill | 7 | yes | yes | 1 |  | 14 |
| omni | 6 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 7 | kill | 11 | yes | yes | 1 |  | 14 |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 10 | kill | 9 | yes | yes | 1 |  | 14 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*