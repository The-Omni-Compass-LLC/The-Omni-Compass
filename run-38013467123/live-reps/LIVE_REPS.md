# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1389 | 1386 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1389 | 1386 |
| response time (ms), mean | 394.9 | 216.2 |
| response time (ms), 95th percentile | 1232 | 618.6 |
| response time (ms), 99th percentile | 4343 | 2716 |
| time over the response line (% of samples) | 21.38 | 11.69 |
| failed requests (%) | 8.11 | 7.463 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.544 | 2.256 |
| utilisation (used / allocatable) | 0.1092 | 0.1076 |
| CPU used (cores), mean | 2.621 | 2.582 |
| Omni's own CPU (cores), mean | 0 | 0.008 |
| CPU used with Omni's own (cores), mean | 2.621 | 2.348 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 268.1 | 272.2 |
| HPA replicas, mean | 9.935 | 9.95 |
| pods started | 5.667 | 3.667 |
| pod start wait, total (s) | 19.67 | 12.33 |
| pod start wait, mean (s) | 3.433 | 2.2 |
| host CPU busy, the real machine under kind (%) | 73.01 | 72.46 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.779e-16 to +1.57e-15 | same (under one part in a million) |
| node-hours | 12.01 | 12.01 | -0.0% | -0.04715 to +0.04049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1389 | 1386 | -0.3% | -16.03 to +8.965 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1389 | 1386 | -0.3% | -16.03 to +8.965 | no |
| response time (ms), mean | 394.9 | 216.2 | -45.2% | -296 to -61.19 | yes, better |
| response time (ms), 95th percentile | 1232 | 618.6 | -49.8% | -793.4 to -432.5 | yes, better |
| response time (ms), 99th percentile | 4343 | 2716 | -37.5% | -3201 to -52.54 | yes, better |
| time over the response line (% of samples) | 21.38 | 11.69 | -45.3% | -10.24 to -9.151 | yes, better |
| failed requests (%) | 8.11 | 7.463 | -8.0% | -1.618 to +0.3236 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.544 | 2.256 | +46.0% | -0.8548 to +2.277 | no |
| utilisation (used / allocatable) | 0.1092 | 0.1076 | -1.5% | -0.00584 to +0.002571 | no |
| CPU used (cores), mean | 2.621 | 2.582 | -1.5% | -0.1402 to +0.06171 | no |
| Omni's own CPU (cores), mean | 0 | 0.008 | +0.008 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 2.621 | 2.591 | -1.1% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 268.1 | 272.2 | +1.5% | -6.591 to +14.9 | no |
| HPA replicas, mean | 9.935 | 9.95 | +0.2% | -0.06891 to +0.09908 | no |
| pods started | 5.667 | 3.667 | -35.3% | -8.573 to +4.573 | no |
| pod start wait, total (s) | 19.67 | 12.33 | -37.3% | -24.78 to +10.12 | no |
| pod start wait, mean (s) | 3.433 | 2.2 | -35.9% | -4.785 to +2.318 | no |
| host CPU busy, the real machine under kind (%) | 73.01 | 72.46 | -0.8% | -2.887 to +1.773 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.040 | 118 | 98.3% | 1 (shown: API 500 for apis/autoscaling/v2/horizontalpodautoscalers) | 1.09 | yes |
| omni | 2 | long |  |  |  | 0 | 1.053 | 119 | 99.2% | 1 (shown: API 500 for apis/autoscaling/v2/horizontalpodautoscalers) | 1.27 | yes |
| omni | 3 | long |  |  |  | 0 | 1.035 | 117 | 97.5% | 1 (shown: API 500 for apis/autoscaling/v2/horizontalpodautoscalers) | 1.06 | yes |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*