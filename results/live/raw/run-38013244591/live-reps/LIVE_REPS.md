# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.1 | 172.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.1 | 172.8 |
| response time (ms), mean | 525.5 | 505.8 |
| response time (ms), 95th percentile | 2279 | 2464 |
| response time (ms), 99th percentile | 5428 | 5790 |
| time over the response line (% of samples) | 24.09 | 23.4 |
| failed requests (%) | 3.59 | 2.53 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.228 | 1.76 |
| utilisation (used / allocatable) | 0.0989 | 0.09881 |
| CPU used (cores), mean | 2.374 | 2.371 |
| Omni's own CPU (cores), mean | 0 | 0.01438 |
| CPU used with Omni's own (cores), mean | 2.374 | 2.386 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292.2 | 291.9 |
| HPA replicas, mean | 15.25 | 15.33 |
| pods started | 4.6 | 4 |
| pod start wait, total (s) | 8.6 | 8.8 |
| pod start wait, mean (s) | 1.773 | 2.06 |
| host CPU busy, the real machine under kind (%) | 68.4 | 68.7 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 270.8 | 267.4 |
| second app: response time (ms), 99th percentile | 1870 | 1558 |
| second app: time over the response line (% of samples) | 15.27 | 15.36 |
| second app: failed requests (%) | 12.95 | 13.46 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.566e-16 to +7.895e-16 | same (under one part in a million) |
| node-hours | 1.516 | 1.514 | -0.2% | -0.007521 to +0.002854 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.1 | 172.8 | -0.2% | -0.7926 to +0.2629 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.1 | 172.8 | -0.2% | -0.7926 to +0.2629 | no |
| response time (ms), mean | 525.5 | 505.8 | -3.8% | -64.05 to +24.57 | no |
| response time (ms), 95th percentile | 2279 | 2464 | +8.1% | -206.6 to +576.8 | no |
| response time (ms), 99th percentile | 5428 | 5790 | +6.7% | -787 to +1512 | no |
| time over the response line (% of samples) | 24.09 | 23.4 | -2.9% | -1.584 to +0.2057 | no |
| failed requests (%) | 3.59 | 2.53 | -29.5% | -1.843 to -0.2769 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.228 | 1.76 | +43.3% | +0.07612 to +0.9872 | yes, more |
| utilisation (used / allocatable) | 0.0989 | 0.09881 | -0.1% | -0.001072 to +0.0008938 | no |
| CPU used (cores), mean | 2.374 | 2.371 | -0.1% | -0.02574 to +0.02145 | no |
| Omni's own CPU (cores), mean | 0 | 0.01438 | +0.0144 (native is 0) | +0.01232 to +0.01644 | yes, more |
| CPU used with Omni's own (cores), mean | 2.374 | 2.386 | +0.5% | -0.01028 to +0.03475 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292.2 | 291.9 | -0.1% | -3.69 to +3.062 | no |
| HPA replicas, mean | 15.25 | 15.33 | +0.5% | -0.1861 to +0.3472 | no |
| pods started | 4.6 | 4 | -13.0% | -1.871 to +0.6707 | no |
| pod start wait, total (s) | 8.6 | 8.8 | +2.3% | -3.995 to +4.395 | no |
| pod start wait, mean (s) | 1.773 | 2.06 | +16.2% | -0.3007 to +0.8745 | no |
| host CPU busy, the real machine under kind (%) | 68.4 | 68.7 | +0.4% | -0.1653 to +0.769 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 270.8 | 267.4 | -1.3% | -56.79 to +50.01 | no |
| second app: response time (ms), 99th percentile | 1870 | 1558 | -16.7% | -1003 to +379.9 | no |
| second app: time over the response line (% of samples) | 15.27 | 15.36 | +0.5% | -0.682 to +0.8488 | no |
| second app: failed requests (%) | 12.95 | 13.46 | +3.9% | -0.02925 to +1.051 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*