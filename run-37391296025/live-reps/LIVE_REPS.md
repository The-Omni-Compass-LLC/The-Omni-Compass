# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.794 |
| node-hours | 1.513 | 1.458 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 154.1 |
| response time (ms), mean | 145.4 | 75.4 |
| response time (ms), 95th percentile | 319 | 110.4 |
| response time (ms), 99th percentile | 513.7 | 149.3 |
| time over the response line (% of samples) | 1.668 | 0.02424 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.45 | 0.2117 |
| utilisation (used / allocatable) | 0.03749 | 0.03667 |
| CPU used (cores), mean | 0.8998 | 0.8506 |
| Omni's own CPU (cores), mean | 0 | 0.00972 |
| CPU used with Omni's own (cores), mean | 0.8998 | 0.8604 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 747.3 |
| HPA replicas, mean | 8.553 | 8.251 |
| pods started | 5 | 3.5 |
| pod start wait, total (s) | 20.9 | 10 |
| pod start wait, mean (s) | 3.878 | 2.662 |
| host CPU busy, the real machine under kind (%) | 27.27 | 26.3 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.794 | -3.4% | -0.3781 to -0.03296 | yes, better |
| node-hours | 1.513 | 1.458 | -3.6% | -0.09799 to -0.01156 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158.7 | 158 | -0.5% | -1.478 to +0.03188 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.7 | 154.1 | -2.9% | -7.85 to -1.389 | yes, better |
| response time (ms), mean | 145.4 | 75.4 | -48.1% | -90.87 to -49.11 | yes, better |
| response time (ms), 95th percentile | 319 | 110.4 | -65.4% | -271.6 to -145.6 | yes, better |
| response time (ms), 99th percentile | 513.7 | 149.3 | -70.9% | -471.8 to -257.1 | yes, better |
| time over the response line (% of samples) | 1.668 | 0.02424 | -98.5% | -2.878 to -0.4108 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.45 | 0.2117 | -53.0% | -0.4457 to -0.03092 | yes, less |
| utilisation (used / allocatable) | 0.03749 | 0.03667 | -2.2% | -0.001982 to +0.0003451 | no |
| CPU used (cores), mean | 0.8998 | 0.8506 | -5.5% | -0.07016 to -0.02807 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00972 | +0.00972 (native is 0) | +0.008208 to +0.01123 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8998 | 0.8604 | -4.4% | -0.05918 to -0.01962 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.9 | 747.3 | +2.1% | -1.901 to +32.61 | no |
| HPA replicas, mean | 8.553 | 8.251 | -3.5% | -0.9136 to +0.3083 | no |
| pods started | 5 | 3.5 | -30.0% | -2.817 to -0.1832 | yes, better |
| pod start wait, total (s) | 20.9 | 10 | -52.2% | -21.37 to -0.4335 | yes, better |
| pod start wait, mean (s) | 3.878 | 2.662 | -31.4% | -2.548 to +0.1157 | no |
| host CPU busy, the real machine under kind (%) | 27.27 | 26.3 | -3.5% | -1.491 to -0.4404 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*