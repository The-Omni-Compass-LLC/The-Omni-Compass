# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.3 | 172.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.3 | 172.3 |
| response time (ms), mean | 499.9 | 454.5 |
| response time (ms), 95th percentile | 2170 | 2097 |
| response time (ms), 99th percentile | 4758 | 5414 |
| time over the response line (% of samples) | 23.26 | 21.88 |
| failed requests (%) | 2.117 | 1.98 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.182 | 1.243 |
| utilisation (used / allocatable) | 0.09624 | 0.09512 |
| CPU used (cores), mean | 2.31 | 2.283 |
| Omni's own CPU (cores), mean | 0 | 0.01333 |
| CPU used with Omni's own (cores), mean | 2.31 | 2.296 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.1 | 304 |
| HPA replicas, mean | 15.28 | 15.17 |
| pods started | 4.3 | 3.8 |
| pod start wait, total (s) | 8.6 | 9.1 |
| pod start wait, mean (s) | 1.704 | 1.857 |
| host CPU busy, the real machine under kind (%) | 66.06 | 65.94 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 234.2 | 249 |
| second app: response time (ms), 99th percentile | 2503 | 2869 |
| second app: time over the response line (% of samples) | 13.76 | 13.84 |
| second app: failed requests (%) | 11.74 | 11.76 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | same (under one part in a million) |
| node-hours | 1.516 | 1.517 | +0.1% | -0.003284 to +0.006284 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.3 | 172.3 | -0.0% | -0.4578 to +0.3415 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.3 | 172.3 | -0.0% | -0.4578 to +0.3415 | no |
| response time (ms), mean | 499.9 | 454.5 | -9.1% | -115.7 to +24.75 | no |
| response time (ms), 95th percentile | 2170 | 2097 | -3.3% | -541.3 to +395.9 | no |
| response time (ms), 99th percentile | 4758 | 5414 | +13.8% | -424.3 to +1737 | no |
| time over the response line (% of samples) | 23.26 | 21.88 | -6.0% | -3.108 to +0.3373 | no |
| failed requests (%) | 2.117 | 1.98 | -6.5% | -1.045 to +0.7705 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.182 | 1.243 | +5.2% | -0.661 to +0.7843 | no |
| utilisation (used / allocatable) | 0.09624 | 0.09512 | -1.2% | -0.002414 to +0.000183 | no |
| CPU used (cores), mean | 2.31 | 2.283 | -1.2% | -0.05793 to +0.004391 | no |
| Omni's own CPU (cores), mean | 0 | 0.01333 | +0.0133 (native is 0) | +0.01093 to +0.01573 | yes, more |
| CPU used with Omni's own (cores), mean | 2.31 | 2.296 | -0.6% | -0.0453 to +0.01842 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.1 | 304 | +1.0% | -1.281 to +7.105 | no |
| HPA replicas, mean | 15.28 | 15.17 | -0.7% | -0.5117 to +0.2986 | no |
| pods started | 4.3 | 3.8 | -11.6% | -2.161 to +1.161 | no |
| pod start wait, total (s) | 8.6 | 9.1 | +5.8% | -5.125 to +6.125 | no |
| pod start wait, mean (s) | 1.704 | 1.857 | +9.0% | -0.7705 to +1.077 | no |
| host CPU busy, the real machine under kind (%) | 66.06 | 65.94 | -0.2% | -1.001 to +0.7527 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 234.2 | 249 | +6.3% | -30.06 to +59.6 | no |
| second app: response time (ms), 99th percentile | 2503 | 2869 | +14.6% | -991.2 to +1724 | no |
| second app: time over the response line (% of samples) | 13.76 | 13.84 | +0.6% | -0.7925 to +0.9633 | no |
| second app: failed requests (%) | 11.74 | 11.76 | +0.2% | -0.501 to +0.5515 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*