# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.566 |
| node-hours | 2.513 | 1.913 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 225.9 |
| response time (ms), mean | 428.5 | 383.1 |
| response time (ms), 95th percentile | 2551 | 2566 |
| response time (ms), 99th percentile | 4090 | 4108 |
| time over the response line (% of samples) | 14.64 | 14.15 |
| failed requests (%) | 0.01093 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 171 | 173.4 |
| utilisation (used / allocatable) | 0.05641 | 0.07291 |
| CPU used (cores), mean | 1.354 | 1.333 |
| Omni's own CPU (cores), mean | 0 | 0.01743 |
| CPU used with Omni's own (cores), mean | 1.354 | 1.35 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.3 | 407.5 |
| HPA replicas, mean | 2.061 | 2.097 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 4.1 | 2.5 |
| pod start wait, mean (s) | 4.1 | 2.5 |
| host CPU busy, the real machine under kind (%) | 38.92 | 39.65 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 524.9 | 528.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.826 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.566 | -23.9% | -1.847 to -1.02 | yes, better |
| node-hours | 2.513 | 1.913 | -23.9% | -0.7744 to -0.4266 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.9 | -0.0% | -1.072 to +0.9869 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 225.9 | -16.6% | -58.14 to -31.97 | yes, better |
| response time (ms), mean | 428.5 | 383.1 | -10.6% | -62.86 to -28.04 | yes, better |
| response time (ms), 95th percentile | 2551 | 2566 | +0.6% | -137.3 to +167.3 | no |
| response time (ms), 99th percentile | 4090 | 4108 | +0.4% | -272.4 to +308.1 | no |
| time over the response line (% of samples) | 14.64 | 14.15 | -3.4% | -1.002 to +0.008993 | no |
| failed requests (%) | 0.01093 | 0 | -100.0% | -0.03565 to +0.01379 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 171 | 173.4 | +1.4% | -2.535 to +7.322 | no |
| utilisation (used / allocatable) | 0.05641 | 0.07291 | +29.2% | +0.01139 to +0.0216 | yes, more |
| CPU used (cores), mean | 1.354 | 1.333 | -1.6% | -0.0468 to +0.004421 | no |
| Omni's own CPU (cores), mean | 0 | 0.01743 | +0.0174 (native is 0) | +0.01501 to +0.01985 | yes, more |
| CPU used with Omni's own (cores), mean | 1.354 | 1.35 | -0.3% | -0.02987 to +0.02234 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 485.3 | 407.5 | -16.0% | -107.7 to -47.97 | yes, less |
| HPA replicas, mean | 2.061 | 2.097 | +1.7% | -0.2257 to +0.2976 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 4.1 | 2.5 | -39.0% | -12.99 to +9.786 | no |
| pod start wait, mean (s) | 4.1 | 2.5 | -39.0% | -12.99 to +9.786 | no |
| host CPU busy, the real machine under kind (%) | 38.92 | 39.65 | +1.9% | +0.3375 to +1.115 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 524.9 | 528.9 | +0.8% | -1.489 to +9.489 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.826 | -36.2% | -2.705 to -1.643 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*