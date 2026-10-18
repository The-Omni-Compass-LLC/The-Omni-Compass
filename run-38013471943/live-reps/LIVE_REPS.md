# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.755 |
| node-hours | 12.01 | 11.53 |
| energy, parked workers still on at idle power (Wh, declared model) | 1361 | 1360 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1361 | 1323 |
| response time (ms), mean | 334.1 | 222.2 |
| response time (ms), 95th percentile | 1040 | 603.9 |
| response time (ms), 99th percentile | 3214 | 3409 |
| time over the response line (% of samples) | 19.79 | 13.21 |
| failed requests (%) | 10.19 | 9.466 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.372 | 2.489 |
| utilisation (used / allocatable) | 0.0937 | 0.095 |
| CPU used (cores), mean | 2.249 | 2.217 |
| Omni's own CPU (cores), mean | 0 | 0.0083 |
| CPU used with Omni's own (cores), mean | 2.249 | 2.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 338.9 | 332.3 |
| HPA replicas, mean | 9.896 | 9.433 |
| pods started | 6.667 | 9 |
| pod start wait, total (s) | 19.33 | 29 |
| pod start wait, mean (s) | 2.689 | 2.676 |
| host CPU busy, the real machine under kind (%) | 63.77 | 63.36 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.755 | -4.1% | -1.205 to +0.7149 | no |
| node-hours | 12.01 | 11.53 | -4.0% | -2.444 to +1.473 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1361 | 1360 | -0.1% | -15.53 to +13.06 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1361 | 1323 | -2.8% | -183.4 to +107.3 | no |
| response time (ms), mean | 334.1 | 222.2 | -33.5% | -282.2 to +58.32 | no |
| response time (ms), 95th percentile | 1040 | 603.9 | -41.9% | -1067 to +194.7 | no |
| response time (ms), 99th percentile | 3214 | 3409 | +6.1% | -2087 to +2476 | no |
| time over the response line (% of samples) | 19.79 | 13.21 | -33.2% | -20.99 to +7.834 | no |
| failed requests (%) | 10.19 | 9.466 | -7.1% | -2.736 to +1.286 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.372 | 2.489 | +4.9% | -5.255 to +5.488 | no |
| utilisation (used / allocatable) | 0.0937 | 0.095 | +1.4% | -0.01216 to +0.01476 | no |
| CPU used (cores), mean | 2.249 | 2.217 | -1.4% | -0.2157 to +0.1513 | no |
| Omni's own CPU (cores), mean | 0 | 0.0083 | +0.0083 (native is 0) | -0.006947 to +0.02355 | no |
| CPU used with Omni's own (cores), mean | 2.249 | 2.265 | +0.7% | -0.2848 to +0.3182 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 338.9 | 332.3 | -2.0% | -67.73 to +54.44 | no |
| HPA replicas, mean | 9.896 | 9.433 | -4.7% | -2.372 to +1.445 | no |
| pods started | 6.667 | 9 | +35.0% | -8.869 to +13.54 | no |
| pod start wait, total (s) | 19.33 | 29 | +50.0% | -36.23 to +55.57 | no |
| pod start wait, mean (s) | 2.689 | 2.676 | -0.5% | -2.501 to +2.476 | no |
| host CPU busy, the real machine under kind (%) | 63.77 | 63.36 | -0.6% | -5.507 to +4.702 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.052 | 118 | 98.3% | 1 (shown: API 500 for apis/autoscaling/v2/horizontalpodautoscalers) | 0.97 | yes |
| omni | 2 | long |  |  |  | 0 | 1.028 | 117 | 97.5% | 3 (shown: API 500 for apis/autoscaling/v2/horizontalpodautoscalers) | 1.10 | yes |
| omni | 3 | long |  |  |  | 0 | 1.073 | 119 | 99.2% | 1 (shown: API 500 for apis/autoscaling/v2/horizontalpodautoscalers) | 1.30 | yes |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*