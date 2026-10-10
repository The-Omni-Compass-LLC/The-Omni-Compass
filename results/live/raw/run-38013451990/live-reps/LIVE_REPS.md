# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172 |
| response time (ms), mean | 327.3 | 218.2 |
| response time (ms), 95th percentile | 980.4 | 720.4 |
| response time (ms), 99th percentile | 3235 | 2963 |
| time over the response line (% of samples) | 22.12 | 14.23 |
| failed requests (%) | 12.2 | 10.45 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3033 | 0.3667 |
| utilisation (used / allocatable) | 0.09932 | 0.09721 |
| CPU used (cores), mean | 2.384 | 2.333 |
| Omni's own CPU (cores), mean | 0 | 0.01315 |
| CPU used with Omni's own (cores), mean | 2.384 | 2.346 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 317.7 | 325.1 |
| HPA replicas, mean | 9.384 | 9.448 |
| pods started | 5 | 4.3 |
| pod start wait, total (s) | 20.2 | 14.8 |
| pod start wait, mean (s) | 3.391 | 2.833 |
| host CPU busy, the real machine under kind (%) | 68.15 | 67.64 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 43.07 | 40.68 |
| robust: time over the line in the 120 s after the kill (% of samples) | 55.56 | 53.91 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.512 | 1.511 | -0.1% | -0.004897 to +0.002563 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172 | -0.3% | -1.1 to -0.08071 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 172 | -0.3% | -1.1 to -0.08071 | yes, better |
| response time (ms), mean | 327.3 | 218.2 | -33.3% | -169.6 to -48.48 | yes, better |
| response time (ms), 95th percentile | 980.4 | 720.4 | -26.5% | -494.9 to -25.12 | yes, better |
| response time (ms), 99th percentile | 3235 | 2963 | -8.4% | -1531 to +987.2 | no |
| time over the response line (% of samples) | 22.12 | 14.23 | -35.6% | -11.61 to -4.159 | yes, better |
| failed requests (%) | 12.2 | 10.45 | -14.3% | -3.19 to -0.3074 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3033 | 0.3667 | +20.9% | -0.4666 to +0.5932 | no |
| utilisation (used / allocatable) | 0.09932 | 0.09721 | -2.1% | -0.002836 to -0.001395 | yes, less |
| CPU used (cores), mean | 2.384 | 2.333 | -2.1% | -0.06806 to -0.03348 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01315 | +0.0132 (native is 0) | +0.01194 to +0.01436 | yes, more |
| CPU used with Omni's own (cores), mean | 2.384 | 2.346 | -1.6% | -0.05489 to -0.02036 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 317.7 | 325.1 | +2.3% | +2.58 to +12.12 | yes, more |
| HPA replicas, mean | 9.384 | 9.448 | +0.7% | -0.04339 to +0.1706 | no |
| pods started | 5 | 4.3 | -14.0% | -1.821 to +0.4209 | no |
| pod start wait, total (s) | 20.2 | 14.8 | -26.7% | -13.34 to +2.538 | no |
| pod start wait, mean (s) | 3.391 | 2.833 | -16.4% | -1.774 to +0.6589 | no |
| host CPU busy, the real machine under kind (%) | 68.15 | 67.64 | -0.7% | -1.114 to +0.09545 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 43.07 | 40.68 | -5.5% | -10.34 to +5.561 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 55.56 | 53.91 | -3.0% | -5.197 to +1.89 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 9 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*