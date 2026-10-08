# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.989 |
| node-hours | 12.01 | 11.99 |
| energy, parked workers still on at idle power (Wh, declared model) | 1408 | 1405 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1408 | 1403 |
| response time (ms), mean | 510.8 | 295.9 |
| response time (ms), 95th percentile | 1806 | 835.4 |
| response time (ms), 99th percentile | 6029 | 4727 |
| time over the response line (% of samples) | 34.99 | 22.69 |
| failed requests (%) | 19.54 | 16.82 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.083 | 2.378 |
| utilisation (used / allocatable) | 0.1196 | 0.118 |
| CPU used (cores), mean | 2.87 | 2.828 |
| Omni's own CPU (cores), mean | 0 | 0.0095 |
| CPU used with Omni's own (cores), mean | 2.87 | 3.29 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 256.5 | 260.5 |
| HPA replicas, mean | 9.941 | 9.92 |
| pods started | 4.667 | 6.333 |
| pod start wait, total (s) | 18 | 22.33 |
| pod start wait, mean (s) | 3.489 | 3.607 |
| host CPU busy, the real machine under kind (%) | 80.37 | 79.66 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.989 | -0.2% | -0.05891 to +0.03669 | no |
| node-hours | 12.01 | 11.99 | -0.2% | -0.1279 to +0.08233 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1408 | 1405 | -0.2% | -8.807 to +2.953 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1408 | 1403 | -0.3% | -17.01 to +7.824 | no |
| response time (ms), mean | 510.8 | 295.9 | -42.1% | -469.3 to +39.36 | no |
| response time (ms), 95th percentile | 1806 | 835.4 | -53.8% | -2541 to +599.7 | no |
| response time (ms), 99th percentile | 6029 | 4727 | -21.6% | -3351 to +745.8 | no |
| time over the response line (% of samples) | 34.99 | 22.69 | -35.2% | -29.55 to +4.947 | no |
| failed requests (%) | 19.54 | 16.82 | -14.0% | -9.596 to +4.141 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.083 | 2.378 | +14.1% | -3.232 to +3.821 | no |
| utilisation (used / allocatable) | 0.1196 | 0.118 | -1.3% | -0.005743 to +0.00256 | no |
| CPU used (cores), mean | 2.87 | 2.828 | -1.5% | -0.148 to +0.06433 | no |
| Omni's own CPU (cores), mean | 0 | 0.0095 | +0.0095 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 2.87 | 2.887 | +0.6% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 256.5 | 260.5 | +1.6% | -7.275 to +15.34 | no |
| HPA replicas, mean | 9.941 | 9.92 | -0.2% | -0.05394 to +0.01286 | no |
| pods started | 4.667 | 6.333 | +35.7% | -2.128 to +5.462 | no |
| pod start wait, total (s) | 18 | 22.33 | +24.1% | -16.5 to +25.17 | no |
| pod start wait, mean (s) | 3.489 | 3.607 | +3.4% | -4.746 to +4.983 | no |
| host CPU busy, the real machine under kind (%) | 80.37 | 79.66 | -0.9% | -3.199 to +1.791 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`).

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions |
|---|---:|---|---:|---|---|---:|---:|---:|
| omni | 1 | long |  |  |  | 0 | 1.052 | 119 |
| omni | 2 | long |  |  |  | 0 | 1.033 | 117 |
| omni | 3 | long |  |  |  | 0 | 1.036 | 117 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*