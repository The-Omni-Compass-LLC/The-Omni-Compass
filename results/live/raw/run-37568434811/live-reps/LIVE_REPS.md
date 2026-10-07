# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.971 |
| node-hours | 4.515 | 4.495 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.3 | 520 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.3 | 518.4 |
| response time (ms), mean | 309.9 | 162.1 |
| response time (ms), 95th percentile | 820.4 | 306.2 |
| response time (ms), 99th percentile | 2987 | 1788 |
| time over the response line (% of samples) | 21.9 | 13.39 |
| failed requests (%) | 12.29 | 10.85 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.435 | 0.4067 |
| utilisation (used / allocatable) | 0.108 | 0.106 |
| CPU used (cores), mean | 2.593 | 2.538 |
| Omni's own CPU (cores), mean | 0 | 0.00975 |
| CPU used with Omni's own (cores), mean | 2.593 | 2.548 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 282.9 | 288 |
| HPA replicas, mean | 9.685 | 9.666 |
| pods started | 4.3 | 2.9 |
| pod start wait, total (s) | 16.1 | 10.9 |
| pod start wait, mean (s) | 3.137 | 2.419 |
| host CPU busy, the real machine under kind (%) | 72.8 | 71.53 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.971 | -0.5% | -0.07832 to +0.02115 | no |
| node-hours | 4.515 | 4.495 | -0.5% | -0.05898 to +0.01798 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.3 | 520 | -0.3% | -2.245 to -0.4126 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.3 | 518.4 | -0.6% | -6.002 to +0.1193 | no |
| response time (ms), mean | 309.9 | 162.1 | -47.7% | -185.1 to -110.5 | yes, better |
| response time (ms), 95th percentile | 820.4 | 306.2 | -62.7% | -620.1 to -408.4 | yes, better |
| response time (ms), 99th percentile | 2987 | 1788 | -40.1% | -2102 to -296.3 | yes, better |
| time over the response line (% of samples) | 21.9 | 13.39 | -38.8% | -10.85 to -6.165 | yes, better |
| failed requests (%) | 12.29 | 10.85 | -11.7% | -2.078 to -0.8027 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.435 | 0.4067 | -6.5% | -0.2686 to +0.212 | no |
| utilisation (used / allocatable) | 0.108 | 0.106 | -1.8% | -0.002497 to -0.001499 | yes, less |
| CPU used (cores), mean | 2.593 | 2.538 | -2.1% | -0.06415 to -0.04542 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00975 | +0.00975 (native is 0) | +0.008677 to +0.01082 | yes, more |
| CPU used with Omni's own (cores), mean | 2.593 | 2.548 | -1.7% | -0.05503 to -0.03503 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 282.9 | 288 | +1.8% | +3.099 to +7.27 | yes, more |
| HPA replicas, mean | 9.685 | 9.666 | -0.2% | -0.162 to +0.1235 | no |
| pods started | 4.3 | 2.9 | -32.6% | -2.671 to -0.1293 | yes, better |
| pod start wait, total (s) | 16.1 | 10.9 | -32.3% | -10.66 to +0.256 | no |
| pod start wait, mean (s) | 3.137 | 2.419 | -22.9% | -1.565 to +0.1289 | no |
| host CPU busy, the real machine under kind (%) | 72.8 | 71.53 | -1.8% | -1.424 to -1.13 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*