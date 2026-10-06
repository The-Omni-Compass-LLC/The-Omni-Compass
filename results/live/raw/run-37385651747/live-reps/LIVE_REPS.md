# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.917 |
| node-hours | 1.496 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.6 | 165.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164 | 163.6 |
| response time (ms), mean | 192.1 | 122.3 |
| response time (ms), 95th percentile | 377.3 | 139.2 |
| response time (ms), 99th percentile | 1566 | 558.7 |
| time over the response line (% of samples) | 7.431 | 5.306 |
| failed requests (%) | 4.493 | 4.295 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6367 | 0.7517 |
| utilisation (used / allocatable) | 0.06894 | 0.06872 |
| CPU used (cores), mean | 1.631 | 1.627 |
| Omni's own CPU (cores), mean | 0 | 0.00887 |
| CPU used with Omni's own (cores), mean | 1.631 | 1.635 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.4 | 407.6 |
| HPA replicas, mean | 8.72 | 8.833 |
| pods started | 4.7 | 4.2 |
| pod start wait, total (s) | 31.9 | 23.1 |
| pod start wait, mean (s) | 5.894 | 4.261 |
| host CPU busy, the real machine under kind (%) | 46.85 | 47.14 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.917 | +0.0% | -0.002818 to +0.005534 | no |
| node-hours | 1.496 | 1.493 | -0.2% | -0.01036 to +0.003467 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.6 | 165.2 | -0.3% | -1.181 to +0.3427 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164 | 163.6 | -0.2% | -1.174 to +0.394 | no |
| response time (ms), mean | 192.1 | 122.3 | -36.4% | -103.6 to -36.07 | yes, better |
| response time (ms), 95th percentile | 377.3 | 139.2 | -63.1% | -289.5 to -186.5 | yes, better |
| response time (ms), 99th percentile | 1566 | 558.7 | -64.3% | -1916 to -98.94 | yes, better |
| time over the response line (% of samples) | 7.431 | 5.306 | -28.6% | -3.006 to -1.244 | yes, better |
| failed requests (%) | 4.493 | 4.295 | -4.4% | -0.9207 to +0.5253 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6367 | 0.7517 | +18.1% | -0.5383 to +0.7683 | no |
| utilisation (used / allocatable) | 0.06894 | 0.06872 | -0.3% | -0.001621 to +0.001195 | no |
| CPU used (cores), mean | 1.631 | 1.627 | -0.3% | -0.03808 to +0.02889 | no |
| Omni's own CPU (cores), mean | 0 | 0.00887 | +0.00887 (native is 0) | +0.007728 to +0.01001 | yes, more |
| CPU used with Omni's own (cores), mean | 1.631 | 1.635 | +0.3% | -0.02888 to +0.03743 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.4 | 407.6 | +0.0% | -7.08 to +7.417 | no |
| HPA replicas, mean | 8.72 | 8.833 | +1.3% | -0.2537 to +0.479 | no |
| pods started | 4.7 | 4.2 | -10.6% | -2.126 to +1.126 | no |
| pod start wait, total (s) | 31.9 | 23.1 | -27.6% | -42.3 to +24.7 | no |
| pod start wait, mean (s) | 5.894 | 4.261 | -27.7% | -7.691 to +4.426 | no |
| host CPU busy, the real machine under kind (%) | 46.85 | 47.14 | +0.6% | -0.2221 to +0.8064 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 64 | 15.1 |  |
| machine down | omni | 43 | 8.8 | -21 s (-33%) |
| spike | native | 248 | 52.6 |  |
| spike | omni | 235 | 53.5 | -13 s (-5%) |
| runaway pod started | native | 81 | 8.1 |  |
| runaway pod started | omni | 80 | 7.4 | -2 s (-2%) |
| probe blind | native | 59 | 0.6 |  |
| probe blind | omni | 60 | 0.1 | +1 s (+1%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*