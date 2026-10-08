# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.989 |
| node-hours | 12.02 | 11.99 |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1378 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1377 |
| response time (ms), mean | 391.5 | 211.5 |
| response time (ms), 95th percentile | 1231 | 503.5 |
| response time (ms), 99th percentile | 4445 | 3084 |
| time over the response line (% of samples) | 21.64 | 11.15 |
| failed requests (%) | 8.085 | 7.176 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.25 | 2.428 |
| utilisation (used / allocatable) | 0.1058 | 0.1034 |
| CPU used (cores), mean | 2.54 | 2.477 |
| Omni's own CPU (cores), mean | 0 | 0.0099 |
| CPU used with Omni's own (cores), mean | 2.54 | 2.009 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 278.7 | 285.5 |
| HPA replicas, mean | 9.937 | 9.926 |
| pods started | 5 | 6 |
| pod start wait, total (s) | 17 | 20.33 |
| pod start wait, mean (s) | 3.4 | 3.074 |
| host CPU busy, the real machine under kind (%) | 71.24 | 70.01 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.989 | -0.2% | -0.05941 to +0.03701 | no |
| node-hours | 12.02 | 11.99 | -0.2% | -0.1355 to +0.07624 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1378 | -0.4% | -16.44 to +6.161 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1377 | -0.5% | -20.34 to +6.701 | no |
| response time (ms), mean | 391.5 | 211.5 | -46.0% | -313.6 to -46.43 | yes, better |
| response time (ms), 95th percentile | 1231 | 503.5 | -59.1% | -1424 to -31.29 | yes, better |
| response time (ms), 99th percentile | 4445 | 3084 | -30.6% | -2057 to -666.3 | yes, better |
| time over the response line (% of samples) | 21.64 | 11.15 | -48.5% | -20.74 to -0.234 | yes, better |
| failed requests (%) | 8.085 | 7.176 | -11.2% | -3.573 to +1.756 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.25 | 2.428 | +7.9% | -2.321 to +2.676 | no |
| utilisation (used / allocatable) | 0.1058 | 0.1034 | -2.3% | -0.007084 to +0.002172 | no |
| CPU used (cores), mean | 2.54 | 2.477 | -2.5% | -0.1726 to +0.04716 | no |
| Omni's own CPU (cores), mean | 0 | 0.0099 | +0.0099 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 2.54 | 2.487 | -2.1% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 278.7 | 285.5 | +2.4% | -5.914 to +19.46 | no |
| HPA replicas, mean | 9.937 | 9.926 | -0.1% | -0.09553 to +0.07311 | no |
| pods started | 5 | 6 | +20.0% | -6.453 to +8.453 | no |
| pod start wait, total (s) | 17 | 20.33 | +19.6% | -33.88 to +40.54 | no |
| pod start wait, mean (s) | 3.4 | 3.074 | -9.6% | -2.945 to +2.293 | no |
| host CPU busy, the real machine under kind (%) | 71.24 | 70.01 | -1.7% | -3.997 to +1.539 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`).

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions |
|---|---:|---|---:|---|---|---:|---:|---:|
| omni | 1 | long |  |  |  | 0 | 1.024 | 117 |
| omni | 2 | long |  |  |  | 0 | 1.046 | 118 |
| omni | 3 | long |  |  |  | 0 | 1.048 | 119 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*