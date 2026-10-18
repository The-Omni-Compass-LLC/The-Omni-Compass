# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.8 | 171.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.8 | 171.9 |
| response time (ms), mean | 478.7 | 440 |
| response time (ms), 95th percentile | 1982 | 2064 |
| response time (ms), 99th percentile | 4758 | 4997 |
| time over the response line (% of samples) | 22.11 | 21.02 |
| failed requests (%) | 2.719 | 2.794 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.06 | 1.213 |
| utilisation (used / allocatable) | 0.09431 | 0.09548 |
| CPU used (cores), mean | 2.263 | 2.291 |
| Omni's own CPU (cores), mean | 0 | 0.01343 |
| CPU used with Omni's own (cores), mean | 2.263 | 2.305 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.6 | 307.5 |
| HPA replicas, mean | 15.18 | 15.07 |
| pods started | 4 | 4.4 |
| pod start wait, total (s) | 10.4 | 12 |
| pod start wait, mean (s) | 2.004 | 2.131 |
| host CPU busy, the real machine under kind (%) | 65.29 | 65.98 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 255.2 | 265.1 |
| second app: response time (ms), 99th percentile | 1169 | 1765 |
| second app: time over the response line (% of samples) | 13.46 | 13.68 |
| second app: failed requests (%) | 11.96 | 12.29 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.108e-16 to +1.066e-15 | same (under one part in a million) |
| node-hours | 1.514 | 1.513 | -0.1% | -0.00741 to +0.003743 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.8 | 171.9 | +0.0% | -0.782 to +0.8456 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.8 | 171.9 | +0.0% | -0.782 to +0.8456 | no |
| response time (ms), mean | 478.7 | 440 | -8.1% | -111.6 to +34.27 | no |
| response time (ms), 95th percentile | 1982 | 2064 | +4.1% | -556.6 to +719.9 | no |
| response time (ms), 99th percentile | 4758 | 4997 | +5.0% | -748.9 to +1227 | no |
| time over the response line (% of samples) | 22.11 | 21.02 | -4.9% | -3.064 to +0.8869 | no |
| failed requests (%) | 2.719 | 2.794 | +2.8% | -0.8114 to +0.9625 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.06 | 1.213 | +14.5% | -0.3946 to +0.7013 | no |
| utilisation (used / allocatable) | 0.09431 | 0.09548 | +1.2% | -0.000541 to +0.002879 | no |
| CPU used (cores), mean | 2.263 | 2.291 | +1.2% | -0.01298 to +0.06909 | no |
| Omni's own CPU (cores), mean | 0 | 0.01343 | +0.0134 (native is 0) | +0.01071 to +0.01615 | yes, more |
| CPU used with Omni's own (cores), mean | 2.263 | 2.305 | +1.8% | +0.001976 to +0.08099 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.6 | 307.5 | -1.6% | -11.12 to +0.9081 | no |
| HPA replicas, mean | 15.18 | 15.07 | -0.7% | -0.308 to +0.09555 | no |
| pods started | 4 | 4.4 | +10.0% | -0.5048 to +1.305 | no |
| pod start wait, total (s) | 10.4 | 12 | +15.4% | -1.988 to +5.188 | no |
| pod start wait, mean (s) | 2.004 | 2.131 | +6.3% | -0.4817 to +0.7355 | no |
| host CPU busy, the real machine under kind (%) | 65.29 | 65.98 | +1.1% | -0.06212 to +1.448 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 255.2 | 265.1 | +3.9% | -14.32 to +34.05 | no |
| second app: response time (ms), 99th percentile | 1169 | 1765 | +51.0% | -709.1 to +1901 | no |
| second app: time over the response line (% of samples) | 13.46 | 13.68 | +1.7% | -0.1703 to +0.6175 | no |
| second app: failed requests (%) | 11.96 | 12.29 | +2.7% | -0.05344 to +0.7009 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*