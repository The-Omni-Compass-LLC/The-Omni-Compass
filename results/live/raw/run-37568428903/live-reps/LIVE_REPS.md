# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.899 |
| node-hours | 1.51 | 1.486 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 156.3 |
| response time (ms), mean | 146.4 | 75.77 |
| response time (ms), 95th percentile | 321.1 | 110.8 |
| response time (ms), 99th percentile | 517.6 | 146.6 |
| time over the response line (% of samples) | 1.757 | 0.0119 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.3417 |
| utilisation (used / allocatable) | 0.03768 | 0.03644 |
| CPU used (cores), mean | 0.9044 | 0.8598 |
| Omni's own CPU (cores), mean | 0 | 0.0098 |
| CPU used with Omni's own (cores), mean | 0.9044 | 0.8696 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.5 | 750.2 |
| HPA replicas, mean | 8.659 | 8.333 |
| pods started | 4.5 | 4.2 |
| pod start wait, total (s) | 16.2 | 14.4 |
| pod start wait, mean (s) | 3.108 | 2.88 |
| host CPU busy, the real machine under kind (%) | 27.47 | 26.64 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.899 | -1.7% | -0.1279 to -0.07467 | yes, better |
| node-hours | 1.51 | 1.486 | -1.6% | -0.03682 to -0.0129 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.2 | -0.2% | -1.419 to +0.7758 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 156.3 | -1.4% | -3.387 to -1.085 | yes, better |
| response time (ms), mean | 146.4 | 75.77 | -48.2% | -93.72 to -47.55 | yes, better |
| response time (ms), 95th percentile | 321.1 | 110.8 | -65.5% | -274.7 to -145.9 | yes, better |
| response time (ms), 99th percentile | 517.6 | 146.6 | -71.7% | -502.1 to -239.9 | yes, better |
| time over the response line (% of samples) | 1.757 | 0.0119 | -99.3% | -3.172 to -0.3178 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.3417 | +6.8% | -0.2027 to +0.246 | no |
| utilisation (used / allocatable) | 0.03768 | 0.03644 | -3.3% | -0.002507 to +1.422e-05 | no |
| CPU used (cores), mean | 0.9044 | 0.8598 | -4.9% | -0.07637 to -0.01284 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0098 | +0.0098 (native is 0) | +0.008469 to +0.01113 | yes, more |
| CPU used with Omni's own (cores), mean | 0.9044 | 0.8696 | -3.8% | -0.06575 to -0.003865 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 732.5 | 750.2 | +2.4% | -0.4006 to +35.83 | no |
| HPA replicas, mean | 8.659 | 8.333 | -3.8% | -0.648 to -0.00559 | yes, better |
| pods started | 4.5 | 4.2 | -6.7% | -1.257 to +0.6567 | no |
| pod start wait, total (s) | 16.2 | 14.4 | -11.1% | -8.584 to +4.984 | no |
| pod start wait, mean (s) | 3.108 | 2.88 | -7.3% | -1.241 to +0.7845 | no |
| host CPU busy, the real machine under kind (%) | 27.47 | 26.64 | -3.0% | -1.695 to +0.01896 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*