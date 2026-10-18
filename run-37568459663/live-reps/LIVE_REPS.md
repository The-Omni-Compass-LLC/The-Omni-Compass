# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.89 |
| node-hours | 2.516 | 2.052 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 238.2 |
| response time (ms), mean | 501 | 441.6 |
| response time (ms), 95th percentile | 3051 | 2978 |
| response time (ms), 99th percentile | 4609 | 4570 |
| time over the response line (% of samples) | 15.07 | 14.5 |
| failed requests (%) | 0.01031 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 181.3 | 184.6 |
| utilisation (used / allocatable) | 0.06054 | 0.07319 |
| CPU used (cores), mean | 1.453 | 1.434 |
| Omni's own CPU (cores), mean | 0 | 0.01917 |
| CPU used with Omni's own (cores), mean | 1.453 | 1.453 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.4 | 399.4 |
| HPA replicas, mean | 2.087 | 2.047 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 41.53 | 42.27 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 562.5 | 564.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.288 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.89 | -18.5% | -1.587 to -0.6321 | yes, better |
| node-hours | 2.516 | 2.052 | -18.4% | -0.669 to -0.2579 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273 | +0.1% | -0.6042 to +1.053 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 238.2 | -12.7% | -50.07 to -19.25 | yes, better |
| response time (ms), mean | 501 | 441.6 | -11.9% | -80.9 to -37.93 | yes, better |
| response time (ms), 95th percentile | 3051 | 2978 | -2.4% | -205.7 to +60.01 | no |
| response time (ms), 99th percentile | 4609 | 4570 | -0.8% | -344.7 to +266.7 | no |
| time over the response line (% of samples) | 15.07 | 14.5 | -3.8% | -0.9642 to -0.1748 | yes, better |
| failed requests (%) | 0.01031 | 0 | -100.0% | -0.03363 to +0.01301 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 181.3 | 184.6 | +1.8% | -1.945 to +8.528 | no |
| utilisation (used / allocatable) | 0.06054 | 0.07319 | +20.9% | +0.00676 to +0.01855 | yes, more |
| CPU used (cores), mean | 1.453 | 1.434 | -1.3% | -0.05471 to +0.01647 | no |
| Omni's own CPU (cores), mean | 0 | 0.01917 | +0.0192 (native is 0) | +0.01666 to +0.02168 | yes, more |
| CPU used with Omni's own (cores), mean | 1.453 | 1.453 | +0.0% | -0.03477 to +0.03488 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.4 | 399.4 | -13.0% | -101.6 to -18.3 | yes, less |
| HPA replicas, mean | 2.087 | 2.047 | -1.9% | -0.3328 to +0.2516 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 41.53 | 42.27 | +1.8% | +0.07544 to +1.415 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 562.5 | 564.7 | +0.4% | -8.563 to +12.96 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.288 | -28.5% | -2.337 to -1.088 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*