# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.9 | 174.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.9 | 174.9 |
| response time (ms), mean | 391.7 | 241 |
| response time (ms), 95th percentile | 1211 | 683.6 |
| response time (ms), 99th percentile | 4441 | 3607 |
| time over the response line (% of samples) | 24.51 | 17.77 |
| failed requests (%) | 13.7 | 12.54 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4083 | 0.3967 |
| utilisation (used / allocatable) | 0.1094 | 0.1081 |
| CPU used (cores), mean | 2.625 | 2.594 |
| Omni's own CPU (cores), mean | 0 | 0.01314 |
| CPU used with Omni's own (cores), mean | 2.625 | 2.608 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279.9 | 283.5 |
| HPA replicas, mean | 9.48 | 9.586 |
| pods started | 4.5 | 3.6 |
| pod start wait, total (s) | 17.5 | 10.4 |
| pod start wait, mean (s) | 3.16 | 2.377 |
| host CPU busy, the real machine under kind (%) | 75.03 | 74.5 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 47.93 | 52.49 |
| robust: time over the line in the 120 s after the kill (% of samples) | 68.22 | 66.89 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.512 | 1.514 | +0.1% | -0.004257 to +0.007924 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.9 | 174.9 | -0.0% | -0.8526 to +0.7289 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.9 | 174.9 | -0.0% | -0.8526 to +0.7289 | no |
| response time (ms), mean | 391.7 | 241 | -38.5% | -215.3 to -86.12 | yes, better |
| response time (ms), 95th percentile | 1211 | 683.6 | -43.5% | -962.5 to -91.83 | yes, better |
| response time (ms), 99th percentile | 4441 | 3607 | -18.8% | -2457 to +787.8 | no |
| time over the response line (% of samples) | 24.51 | 17.77 | -27.5% | -9.209 to -4.268 | yes, better |
| failed requests (%) | 13.7 | 12.54 | -8.5% | -2.109 to -0.2073 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4083 | 0.3967 | -2.9% | -0.5287 to +0.5053 | no |
| utilisation (used / allocatable) | 0.1094 | 0.1081 | -1.1% | -0.002098 to -0.0004094 | yes, less |
| CPU used (cores), mean | 2.625 | 2.594 | -1.1% | -0.05036 to -0.009826 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01314 | +0.0131 (native is 0) | +0.01221 to +0.01407 | yes, more |
| CPU used with Omni's own (cores), mean | 2.625 | 2.608 | -0.6% | -0.03721 to +0.003307 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279.9 | 283.5 | +1.3% | +0.7916 to +6.449 | yes, more |
| HPA replicas, mean | 9.48 | 9.586 | +1.1% | +0.02526 to +0.1861 | yes, worse |
| pods started | 4.5 | 3.6 | -20.0% | -1.88 to +0.0802 | no |
| pod start wait, total (s) | 17.5 | 10.4 | -40.6% | -15.77 to +1.572 | no |
| pod start wait, mean (s) | 3.16 | 2.377 | -24.8% | -1.947 to +0.3811 | no |
| host CPU busy, the real machine under kind (%) | 75.03 | 74.5 | -0.7% | -1.085 to +0.02574 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 47.93 | 52.49 | +9.5% | -2.348 to +11.45 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 68.22 | 66.89 | -1.9% | -7.522 to +4.873 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`).

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions |
|---|---:|---|---:|---|---|---:|---:|---:|
| omni | 1 | kill | 7 | yes | yes | 1 |  | 14 |
| omni | 2 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 3 | kill | 9 | yes | yes | 1 |  | 14 |
| omni | 4 | kill | 9 | yes | yes | 1 |  | 14 |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |
| omni | 6 | kill | 11 | yes | yes | 1 |  | 14 |
| omni | 7 | kill | 9 | yes | yes | 1 |  | 14 |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 9 | kill | 5 | yes | yes | 1 |  | 14 |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 14 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*