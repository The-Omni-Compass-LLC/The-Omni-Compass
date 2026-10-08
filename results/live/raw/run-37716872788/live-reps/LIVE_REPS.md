# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.3 | 171.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.3 | 171.8 |
| response time (ms), mean | 310.6 | 210.2 |
| response time (ms), 95th percentile | 946.7 | 546.3 |
| response time (ms), 99th percentile | 3131 | 3068 |
| time over the response line (% of samples) | 19.99 | 13.13 |
| failed requests (%) | 10.35 | 8.846 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5667 | 0.4217 |
| utilisation (used / allocatable) | 0.09712 | 0.09541 |
| CPU used (cores), mean | 2.331 | 2.29 |
| Omni's own CPU (cores), mean | 0 | 0.01256 |
| CPU used with Omni's own (cores), mean | 2.331 | 2.302 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.4 | 328 |
| HPA replicas, mean | 9.362 | 9.414 |
| pods started | 5.5 | 5 |
| pod start wait, total (s) | 19.2 | 18.6 |
| pod start wait, mean (s) | 3.367 | 3.144 |
| host CPU busy, the real machine under kind (%) | 66.82 | 66.16 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 36.1 | 32.86 |
| robust: time over the line in the 120 s after the kill (% of samples) | 51.01 | 51.11 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | same (under one part in a million) |
| node-hours | 1.513 | 1.513 | -0.0% | -0.002276 to +0.0009427 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.3 | 171.8 | -0.3% | -0.6647 to -0.2091 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.3 | 171.8 | -0.3% | -0.6647 to -0.2091 | yes, better |
| response time (ms), mean | 310.6 | 210.2 | -32.3% | -139.1 to -61.66 | yes, better |
| response time (ms), 95th percentile | 946.7 | 546.3 | -42.3% | -709.9 to -90.78 | yes, better |
| response time (ms), 99th percentile | 3131 | 3068 | -2.0% | -1591 to +1465 | no |
| time over the response line (% of samples) | 19.99 | 13.13 | -34.3% | -10.31 to -3.418 | yes, better |
| failed requests (%) | 10.35 | 8.846 | -14.5% | -2.842 to -0.1622 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5667 | 0.4217 | -25.6% | -0.6616 to +0.3716 | no |
| utilisation (used / allocatable) | 0.09712 | 0.09541 | -1.8% | -0.002373 to -0.001032 | yes, less |
| CPU used (cores), mean | 2.331 | 2.29 | -1.8% | -0.05694 to -0.02476 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01256 | +0.0126 (native is 0) | +0.01132 to +0.0138 | yes, more |
| CPU used with Omni's own (cores), mean | 2.331 | 2.302 | -1.2% | -0.04428 to -0.0123 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.4 | 328 | +1.8% | +2.919 to +8.445 | yes, more |
| HPA replicas, mean | 9.362 | 9.414 | +0.6% | -0.03085 to +0.1344 | no |
| pods started | 5.5 | 5 | -9.1% | -1.408 to +0.4079 | no |
| pod start wait, total (s) | 19.2 | 18.6 | -3.1% | -10.85 to +9.651 | no |
| pod start wait, mean (s) | 3.367 | 3.144 | -6.6% | -1.718 to +1.273 | no |
| host CPU busy, the real machine under kind (%) | 66.82 | 66.16 | -1.0% | -1.116 to -0.2101 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 36.1 | 32.86 | -9.0% | -11.06 to +4.577 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 51.01 | 51.11 | +0.2% | -4.539 to +4.729 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`).

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions |
|---|---:|---|---:|---|---|---:|---:|---:|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 2 | kill | 7 | yes | yes | 1 |  | 14 |
| omni | 3 | kill | 9 | yes | yes | 1 |  | 14 |
| omni | 4 | kill | 9 | yes | yes | 1 |  | 14 |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |
| omni | 6 | kill | 8 | yes | yes | 1 |  | 14 |
| omni | 7 | kill | 9 | yes | yes | 1 |  | 14 |
| omni | 8 | kill | 11 | yes | yes | 1 |  | 14 |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 14 |
| omni | 10 | kill | 8 | yes | yes | 1 |  | 14 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*