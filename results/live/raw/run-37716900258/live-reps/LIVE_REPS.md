# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.835 |
| node-hours | 12.02 | 11.69 |
| energy, parked workers still on at idle power (Wh, declared model) | 1389 | 1386 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1389 | 1361 |
| response time (ms), mean | 385.5 | 235.7 |
| response time (ms), 95th percentile | 1188 | 708.9 |
| response time (ms), 99th percentile | 4222 | 3635 |
| time over the response line (% of samples) | 27.72 | 19.36 |
| failed requests (%) | 16.97 | 14.82 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.794 | 2.267 |
| utilisation (used / allocatable) | 0.1087 | 0.1085 |
| CPU used (cores), mean | 2.608 | 2.564 |
| Omni's own CPU (cores), mean | 0 | 0.00825 |
| CPU used with Omni's own (cores), mean | 2.608 | 2.228 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.2 | 303.6 |
| HPA replicas, mean | 9.917 | 9.202 |
| pods started | 5 | 7.667 |
| pod start wait, total (s) | 18 | 21.67 |
| pod start wait, mean (s) | 2.589 | 2.378 |
| host CPU busy, the real machine under kind (%) | 73 | 72.15 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.835 | -2.7% | -0.8735 to +0.5441 | no |
| node-hours | 12.02 | 11.69 | -2.8% | -1.745 to +1.083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1389 | 1386 | -0.2% | -9.075 to +3.349 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1389 | 1361 | -2.0% | -138.2 to +82.99 | no |
| response time (ms), mean | 385.5 | 235.7 | -38.9% | -371.9 to +72.19 | no |
| response time (ms), 95th percentile | 1188 | 708.9 | -40.3% | -1298 to +340.6 | no |
| response time (ms), 99th percentile | 4222 | 3635 | -13.9% | -1255 to +80.28 | no |
| time over the response line (% of samples) | 27.72 | 19.36 | -30.2% | -24.48 to +7.759 | no |
| failed requests (%) | 16.97 | 14.82 | -12.7% | -7.004 to +2.71 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.794 | 2.267 | -18.9% | -3.883 to +2.827 | no |
| utilisation (used / allocatable) | 0.1087 | 0.1085 | -0.2% | -0.004186 to +0.003831 | no |
| CPU used (cores), mean | 2.608 | 2.564 | -1.7% | -0.1254 to +0.03809 | no |
| Omni's own CPU (cores), mean | 0 | 0.00825 | +0.00825 (native is 0) | -0.008903 to +0.0254 | no |
| CPU used with Omni's own (cores), mean | 2.608 | 2.558 | -1.9% | -0.3403 to +0.2407 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 303.2 | 303.6 | +0.1% | -4.97 to +5.743 | no |
| HPA replicas, mean | 9.917 | 9.202 | -7.2% | -3.728 to +2.297 | no |
| pods started | 5 | 7.667 | +53.3% | -2.505 to +7.838 | no |
| pod start wait, total (s) | 18 | 21.67 | +20.4% | -10.02 to +17.35 | no |
| pod start wait, mean (s) | 2.589 | 2.378 | -8.2% | -3.744 to +3.322 | no |
| host CPU busy, the real machine under kind (%) | 73 | 72.15 | -1.2% | -2.711 to +1.015 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`).

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions |
|---|---:|---|---:|---|---|---:|---:|---:|
| omni | 1 | long |  |  |  | 0 | 1.022 | 117 |
| omni | 2 | long |  |  |  | 0 | 1.040 | 117 |
| omni | 3 | long |  |  |  | 0 | 1.067 | 120 |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*