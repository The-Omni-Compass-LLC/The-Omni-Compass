# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.909 |
| node-hours | 1.493 | 1.494 |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 164.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.4 | 162.3 |
| response time (ms), mean | 197.1 | 97.08 |
| response time (ms), 95th percentile | 441.3 | 168.8 |
| response time (ms), 99th percentile | 1418 | 531.9 |
| time over the response line (% of samples) | 7.302 | 4.256 |
| failed requests (%) | 3.459 | 3.213 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4533 | 0.5633 |
| utilisation (used / allocatable) | 0.06301 | 0.0621 |
| CPU used (cores), mean | 1.491 | 1.468 |
| Omni's own CPU (cores), mean | 0 | 0.00812 |
| CPU used with Omni's own (cores), mean | 1.491 | 1.476 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.3 | 457.9 |
| HPA replicas, mean | 8.386 | 8.271 |
| pods started | 5.3 | 5.1 |
| pod start wait, total (s) | 20.8 | 18 |
| pod start wait, mean (s) | 3.55 | 3.073 |
| host CPU busy, the real machine under kind (%) | 42.91 | 42.49 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.909 | -0.1% | -0.02281 to +0.01003 | no |
| node-hours | 1.493 | 1.494 | +0.1% | -0.005911 to +0.008911 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 164.1 | +0.1% | -0.8378 to +1.011 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.4 | 162.3 | -0.0% | -0.873 to +0.7966 | no |
| response time (ms), mean | 197.1 | 97.08 | -50.8% | -140.9 to -59.23 | yes, better |
| response time (ms), 95th percentile | 441.3 | 168.8 | -61.7% | -319.6 to -225.4 | yes, better |
| response time (ms), 99th percentile | 1418 | 531.9 | -62.5% | -1260 to -511.6 | yes, better |
| time over the response line (% of samples) | 7.302 | 4.256 | -41.7% | -4.271 to -1.82 | yes, better |
| failed requests (%) | 3.459 | 3.213 | -7.1% | -0.7324 to +0.2412 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4533 | 0.5633 | +24.3% | -0.1391 to +0.3591 | no |
| utilisation (used / allocatable) | 0.06301 | 0.0621 | -1.4% | -0.002533 to +0.0007256 | no |
| CPU used (cores), mean | 1.491 | 1.468 | -1.5% | -0.06139 to +0.01645 | no |
| Omni's own CPU (cores), mean | 0 | 0.00812 | +0.00812 (native is 0) | +0.006961 to +0.009279 | yes, more |
| CPU used with Omni's own (cores), mean | 1.491 | 1.476 | -1.0% | -0.05292 to +0.02422 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.3 | 457.9 | +1.0% | -4.97 to +14.23 | no |
| HPA replicas, mean | 8.386 | 8.271 | -1.4% | -0.272 to +0.04219 | no |
| pods started | 5.3 | 5.1 | -3.8% | -0.5016 to +0.1016 | no |
| pod start wait, total (s) | 20.8 | 18 | -13.5% | -5.637 to +0.03729 | no |
| pod start wait, mean (s) | 3.55 | 3.073 | -13.4% | -0.9793 to +0.02692 | no |
| host CPU busy, the real machine under kind (%) | 42.91 | 42.49 | -1.0% | -1.339 to +0.4857 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 63 | 15.6 |  |
| machine down | omni | 44 | 8.1 | -19 s (-30%) |
| spike | native | 221 | 45.4 |  |
| spike | omni | 179 | 38.9 | -43 s (-19%) |
| runaway pod started | native | 68 | 7.8 |  |
| runaway pod started | omni | 60 | 5.0 | -8 s (-12%) |
| probe blind | native | 65 | 0.5 |  |
| probe blind | omni | 60 | 0.0 | -5 s (-7%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*