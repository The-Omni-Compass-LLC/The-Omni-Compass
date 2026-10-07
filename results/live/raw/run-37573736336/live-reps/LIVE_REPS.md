# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.826 |
| node-hours | 1.512 | 1.471 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 154.9 |
| response time (ms), mean | 134.4 | 71.64 |
| response time (ms), 95th percentile | 294.8 | 102.7 |
| response time (ms), 99th percentile | 458.1 | 148.7 |
| time over the response line (% of samples) | 1.325 | 0.0119 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4433 | 0.3167 |
| utilisation (used / allocatable) | 0.03555 | 0.03486 |
| CPU used (cores), mean | 0.8531 | 0.8145 |
| Omni's own CPU (cores), mean | 0 | 0.00949 |
| CPU used with Omni's own (cores), mean | 0.8531 | 0.824 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 781.7 |
| HPA replicas, mean | 8.294 | 7.927 |
| pods started | 5.4 | 4.4 |
| pod start wait, total (s) | 21.4 | 14.9 |
| pod start wait, mean (s) | 3.823 | 3.003 |
| host CPU busy, the real machine under kind (%) | 26.03 | 25.38 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.826 | -2.9% | -0.2968 to -0.05139 | yes, better |
| node-hours | 1.512 | 1.471 | -2.7% | -0.07348 to -0.009523 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 158.2 | -0.0% | -0.5262 to +0.4921 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 154.9 | -2.1% | -5.696 to -0.9379 | yes, better |
| response time (ms), mean | 134.4 | 71.64 | -46.7% | -84.6 to -40.84 | yes, better |
| response time (ms), 95th percentile | 294.8 | 102.7 | -65.2% | -254.1 to -130.2 | yes, better |
| response time (ms), 99th percentile | 458.1 | 148.7 | -67.5% | -412.3 to -206.6 | yes, better |
| time over the response line (% of samples) | 1.325 | 0.0119 | -99.1% | -2.54 to -0.08597 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4433 | 0.3167 | -28.6% | -0.286 to +0.03271 | no |
| utilisation (used / allocatable) | 0.03555 | 0.03486 | -1.9% | -0.001971 to +0.0005922 | no |
| CPU used (cores), mean | 0.8531 | 0.8145 | -4.5% | -0.06751 to -0.009631 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00949 | +0.00949 (native is 0) | +0.008148 to +0.01083 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8531 | 0.824 | -3.4% | -0.05714 to -0.001022 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 774.2 | 781.7 | +1.0% | -14.8 to +29.93 | no |
| HPA replicas, mean | 8.294 | 7.927 | -4.4% | -0.864 to +0.13 | no |
| pods started | 5.4 | 4.4 | -18.5% | -2.118 to +0.1184 | no |
| pod start wait, total (s) | 21.4 | 14.9 | -30.4% | -13.66 to +0.6551 | no |
| pod start wait, mean (s) | 3.823 | 3.003 | -21.4% | -1.737 to +0.09729 | no |
| host CPU busy, the real machine under kind (%) | 26.03 | 25.38 | -2.5% | -1.427 to +0.1264 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*