# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.902 |
| node-hours | 1.489 | 1.494 |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 164.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.4 | 162.6 |
| response time (ms), mean | 209.8 | 100.2 |
| response time (ms), 95th percentile | 417.9 | 162.9 |
| response time (ms), 99th percentile | 1618 | 584.6 |
| time over the response line (% of samples) | 7.398 | 4.087 |
| failed requests (%) | 3.795 | 3.151 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.475 |
| utilisation (used / allocatable) | 0.06505 | 0.06318 |
| CPU used (cores), mean | 1.539 | 1.493 |
| Omni's own CPU (cores), mean | 0 | 0.00844 |
| CPU used with Omni's own (cores), mean | 1.539 | 1.501 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.5 | 454.2 |
| HPA replicas, mean | 8.427 | 8.587 |
| pods started | 4.9 | 4.1 |
| pod start wait, total (s) | 18.4 | 20.4 |
| pod start wait, mean (s) | 3.119 | 3.283 |
| host CPU busy, the real machine under kind (%) | 44.36 | 43.33 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.913 | 5.902 | -0.2% | -0.03395 to +0.01047 | no |
| node-hours | 1.489 | 1.494 | +0.4% | -0.00391 to +0.01474 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 164.5 | +0.3% | -0.4269 to +1.377 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.4 | 162.6 | +0.2% | -0.6776 to +1.165 | no |
| response time (ms), mean | 209.8 | 100.2 | -52.2% | -148.5 to -70.65 | yes, better |
| response time (ms), 95th percentile | 417.9 | 162.9 | -61.0% | -291.5 to -218.5 | yes, better |
| response time (ms), 99th percentile | 1618 | 584.6 | -63.9% | -1952 to -114.9 | yes, better |
| time over the response line (% of samples) | 7.398 | 4.087 | -44.8% | -4.179 to -2.444 | yes, better |
| failed requests (%) | 3.795 | 3.151 | -17.0% | -1.127 to -0.1607 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.475 | -1.0% | -0.3714 to +0.3614 | no |
| utilisation (used / allocatable) | 0.06505 | 0.06318 | -2.9% | -0.003038 to -0.0006959 | yes, less |
| CPU used (cores), mean | 1.539 | 1.493 | -3.0% | -0.07356 to -0.01833 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00844 | +0.00844 (native is 0) | +0.007293 to +0.009587 | yes, more |
| CPU used with Omni's own (cores), mean | 1.539 | 1.501 | -2.4% | -0.06416 to -0.01084 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.5 | 454.2 | +2.2% | +4.351 to +15.09 | yes, more |
| HPA replicas, mean | 8.427 | 8.587 | +1.9% | -0.1069 to +0.427 | no |
| pods started | 4.9 | 4.1 | -16.3% | -2.006 to +0.4064 | no |
| pod start wait, total (s) | 18.4 | 20.4 | +10.9% | -16.94 to +20.94 | no |
| pod start wait, mean (s) | 3.119 | 3.283 | +5.3% | -2.584 to +2.912 | no |
| host CPU busy, the real machine under kind (%) | 44.36 | 43.33 | -2.3% | -1.978 to -0.07924 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 76 | 15.1 |  |
| machine down | omni | 35 | 6.7 | -41 s (-53%) |
| spike | native | 228 | 51.4 |  |
| spike | omni | 197 | 42.9 | -31 s (-14%) |
| runaway pod started | native | 80 | 8.9 |  |
| runaway pod started | omni | 68 | 5.6 | -12 s (-15%) |
| probe blind | native | 61 | 0.2 |  |
| probe blind | omni | 60 | 0.0 | -1 s (-2%) |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*