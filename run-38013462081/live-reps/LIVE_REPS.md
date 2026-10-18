# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.888 |
| node-hours | 12.02 | 11.79 |
| energy, parked workers still on at idle power (Wh, declared model) | 1370 | 1366 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1370 | 1349 |
| response time (ms), mean | 341.4 | 191.4 |
| response time (ms), 95th percentile | 1035 | 428.2 |
| response time (ms), 99th percentile | 3474 | 2848 |
| time over the response line (% of samples) | 21.19 | 12.13 |
| failed requests (%) | 10.57 | 9.235 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.772 | 3.189 |
| utilisation (used / allocatable) | 0.09861 | 0.09666 |
| CPU used (cores), mean | 2.367 | 2.294 |
| Omni's own CPU (cores), mean | 0 | 0.0063 |
| CPU used with Omni's own (cores), mean | 2.367 | 1.316 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 321.7 | 329.4 |
| HPA replicas, mean | 9.895 | 9.456 |
| pods started | 7 | 7.667 |
| pod start wait, total (s) | 22 | 23 |
| pod start wait, mean (s) | 2.843 | 2.956 |
| host CPU busy, the real machine under kind (%) | 66.32 | 64.93 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.888 | -1.9% | -0.5947 to +0.3704 | no |
| node-hours | 12.02 | 11.79 | -1.9% | -1.175 to +0.7293 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1370 | 1366 | -0.4% | -9.537 to -0.1799 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1370 | 1349 | -1.6% | -96.49 to +53.08 | no |
| response time (ms), mean | 341.4 | 191.4 | -43.9% | -386.1 to +86.3 | no |
| response time (ms), 95th percentile | 1035 | 428.2 | -58.6% | -1586 to +372 | no |
| response time (ms), 99th percentile | 3474 | 2848 | -18.0% | -1413 to +159.8 | no |
| time over the response line (% of samples) | 21.19 | 12.13 | -42.8% | -26.78 to +8.662 | no |
| failed requests (%) | 10.57 | 9.235 | -12.6% | -5.671 to +2.998 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.772 | 3.189 | +79.9% | -4.573 to +7.406 | no |
| utilisation (used / allocatable) | 0.09861 | 0.09666 | -2.0% | -0.005425 to +0.001525 | no |
| CPU used (cores), mean | 2.367 | 2.294 | -3.1% | -0.1449 to -0.0006028 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0063 | +0.0063 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 2.367 | 2.278 | -3.7% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 321.7 | 329.4 | +2.4% | -4.214 to +19.48 | no |
| HPA replicas, mean | 9.895 | 9.456 | -4.4% | -2.369 to +1.489 | no |
| pods started | 7 | 7.667 | +9.5% | -6.505 to +7.838 | no |
| pod start wait, total (s) | 22 | 23 | +4.5% | -25.29 to +27.29 | no |
| pod start wait, mean (s) | 2.843 | 2.956 | +3.9% | -4.161 to +4.386 | no |
| host CPU busy, the real machine under kind (%) | 66.32 | 64.93 | -2.1% | -2.944 to +0.161 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.044 | 118 | 98.3% | 1 (shown: API 500 for apis/autoscaling/v2/horizontalpodautoscalers) | 1.15 | yes |
| omni | 2 | long |  |  |  | 0 | 1.067 | 120 | 100.0% | 0 | 1.11 | yes |
| omni | 3 | long |  |  |  | 0 | 1.028 | 117 | 97.5% | 0 | 1.08 | yes |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*