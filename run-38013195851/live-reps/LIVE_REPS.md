# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.881 |
| node-hours | 1.512 | 1.486 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 156.2 |
| response time (ms), mean | 141.5 | 74.66 |
| response time (ms), 95th percentile | 314.7 | 111.4 |
| response time (ms), 99th percentile | 502.7 | 152.5 |
| time over the response line (% of samples) | 1.761 | 0.03636 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.34 | 0.3417 |
| utilisation (used / allocatable) | 0.03648 | 0.03554 |
| CPU used (cores), mean | 0.8754 | 0.8363 |
| Omni's own CPU (cores), mean | 0 | 0.00977 |
| CPU used with Omni's own (cores), mean | 0.8754 | 0.846 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 781.3 | 787.2 |
| HPA replicas, mean | 8.28 | 8.189 |
| pods started | 4.4 | 4.2 |
| pod start wait, total (s) | 17.9 | 14.9 |
| pod start wait, mean (s) | 3.767 | 3.048 |
| host CPU busy, the real machine under kind (%) | 26.68 | 25.98 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.881 | -2.0% | -0.1284 to -0.1095 | yes, better |
| node-hours | 1.512 | 1.486 | -1.7% | -0.0316 to -0.01923 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.5 | +0.1% | -0.4785 to +0.7249 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 156.2 | -1.3% | -2.726 to -1.54 | yes, better |
| response time (ms), mean | 141.5 | 74.66 | -47.2% | -92.99 to -40.69 | yes, better |
| response time (ms), 95th percentile | 314.7 | 111.4 | -64.6% | -275.5 to -131.1 | yes, better |
| response time (ms), 99th percentile | 502.7 | 152.5 | -69.7% | -467.5 to -232.8 | yes, better |
| time over the response line (% of samples) | 1.761 | 0.03636 | -97.9% | -2.933 to -0.5155 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.34 | 0.3417 | +0.5% | -0.227 to +0.2303 | no |
| utilisation (used / allocatable) | 0.03648 | 0.03554 | -2.6% | -0.002238 to +0.0003735 | no |
| CPU used (cores), mean | 0.8754 | 0.8363 | -4.5% | -0.07296 to -0.005306 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00977 | +0.00977 (native is 0) | +0.008234 to +0.01131 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8754 | 0.846 | -3.4% | -0.06177 to +0.003042 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 781.3 | 787.2 | +0.8% | -23.07 to +34.95 | no |
| HPA replicas, mean | 8.28 | 8.189 | -1.1% | -0.2535 to +0.072 | no |
| pods started | 4.4 | 4.2 | -4.5% | -0.9388 to +0.5388 | no |
| pod start wait, total (s) | 17.9 | 14.9 | -16.8% | -8.246 to +2.246 | no |
| pod start wait, mean (s) | 3.767 | 3.048 | -19.1% | -1.803 to +0.3661 | no |
| host CPU busy, the real machine under kind (%) | 26.68 | 25.98 | -2.6% | -1.55 to +0.1648 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*