# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.954 |
| node-hours | 2.515 | 2.073 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 239.7 |
| response time (ms), mean | 525.4 | 456.3 |
| response time (ms), 95th percentile | 3216 | 3138 |
| response time (ms), 99th percentile | 4747 | 4657 |
| time over the response line (% of samples) | 15.46 | 14.85 |
| failed requests (%) | 0 | 0.01031 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 186.8 | 189.4 |
| utilisation (used / allocatable) | 0.06123 | 0.07318 |
| CPU used (cores), mean | 1.47 | 1.46 |
| Omni's own CPU (cores), mean | 0 | 0.01807 |
| CPU used with Omni's own (cores), mean | 1.47 | 1.353 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.3 | 399.8 |
| HPA replicas, mean | 2.087 | 2.196 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 8.3 |
| pod start wait, mean (s) | 0 | 8.3 |
| host CPU busy, the real machine under kind (%) | 42.34 | 43.08 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 576.9 | 578.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.359 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.954 | -17.4% | -1.476 to -0.6154 | yes, better |
| node-hours | 2.515 | 2.073 | -17.6% | -0.6211 to -0.2631 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.5 | -0.2% | -1.85 to +0.5362 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 239.7 | -12.2% | -47.3 to -19.61 | yes, better |
| response time (ms), mean | 525.4 | 456.3 | -13.1% | -80.5 to -57.55 | yes, better |
| response time (ms), 95th percentile | 3216 | 3138 | -2.4% | -171.9 to +15.33 | no |
| response time (ms), 99th percentile | 4747 | 4657 | -1.9% | -302.4 to +123.4 | no |
| time over the response line (% of samples) | 15.46 | 14.85 | -4.0% | -1.02 to -0.2086 | yes, better |
| failed requests (%) | 0 | 0.01031 | +0.0103 (native is 0) | -0.01301 to +0.03363 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 186.8 | 189.4 | +1.4% | -4.603 to +9.853 | no |
| utilisation (used / allocatable) | 0.06123 | 0.07318 | +19.5% | +0.007761 to +0.01613 | yes, more |
| CPU used (cores), mean | 1.47 | 1.46 | -0.7% | -0.07349 to +0.0534 | no |
| Omni's own CPU (cores), mean | 0 | 0.01807 | +0.0181 (native is 0) | +0.01178 to +0.02435 | yes, more |
| CPU used with Omni's own (cores), mean | 1.47 | 1.438 | -2.2% | -0.1294 to +0.06602 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.3 | 399.8 | -11.6% | -80.69 to -24.27 | yes, less |
| HPA replicas, mean | 2.087 | 2.196 | +5.2% | -0.2246 to +0.4434 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 8.3 | +8.3 (native is 0) | -4.227 to +20.83 | no |
| pod start wait, mean (s) | 0 | 8.3 | +8.3 (native is 0) | -4.227 to +20.83 | no |
| host CPU busy, the real machine under kind (%) | 42.34 | 43.08 | +1.7% | +0.4025 to +1.072 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 576.9 | 578.4 | +0.3% | -4.205 to +7.205 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.359 | -27.3% | -2.189 to -1.092 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*