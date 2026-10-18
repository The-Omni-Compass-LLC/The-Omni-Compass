# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.638 |
| node-hours | 2.508 | 1.945 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 228.9 |
| response time (ms), mean | 482.8 | 416.4 |
| response time (ms), 95th percentile | 2943 | 2795 |
| response time (ms), 99th percentile | 4388 | 4267 |
| time over the response line (% of samples) | 15.11 | 14.75 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 181.5 | 183.5 |
| utilisation (used / allocatable) | 0.06023 | 0.07301 |
| CPU used (cores), mean | 1.446 | 1.36 |
| Omni's own CPU (cores), mean | 0 | 0.0191 |
| CPU used with Omni's own (cores), mean | 1.446 | 1.379 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 408.8 |
| HPA replicas, mean | 1.992 | 2.158 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 4.1 | 9.4 |
| pod start wait, mean (s) | 4.1 | 9.4 |
| host CPU busy, the real machine under kind (%) | 41.15 | 41.58 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 555.4 | 555.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.876 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.638 | -22.7% | -1.695 to -1.029 | yes, better |
| node-hours | 2.508 | 1.945 | -22.5% | -0.7068 to -0.4197 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 | -0.1% | -1.607 to +1.245 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 228.9 | -15.8% | -53.97 to -32.11 | yes, better |
| response time (ms), mean | 482.8 | 416.4 | -13.7% | -90.21 to -42.43 | yes, better |
| response time (ms), 95th percentile | 2943 | 2795 | -5.0% | -272.3 to -22.95 | yes, better |
| response time (ms), 99th percentile | 4388 | 4267 | -2.8% | -362.2 to +119.9 | no |
| time over the response line (% of samples) | 15.11 | 14.75 | -2.4% | -0.7026 to -0.02137 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 181.5 | 183.5 | +1.1% | -3.655 to +7.635 | no |
| utilisation (used / allocatable) | 0.06023 | 0.07301 | +21.2% | +0.007804 to +0.01776 | yes, more |
| CPU used (cores), mean | 1.446 | 1.36 | -5.9% | -0.1475 to -0.02331 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0191 | +0.0191 (native is 0) | +0.01583 to +0.02237 | yes, more |
| CPU used with Omni's own (cores), mean | 1.446 | 1.379 | -4.6% | -0.1293 to -0.003353 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 408.8 | -10.9% | -83.32 to -17.15 | yes, less |
| HPA replicas, mean | 1.992 | 2.158 | +8.3% | -0.07287 to +0.4043 | no |
| pods started | 0.1 | 0.3 | +200.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 4.1 | 9.4 | +129.3% | -10.48 to +21.08 | no |
| pod start wait, mean (s) | 4.1 | 9.4 | +129.3% | -10.48 to +21.08 | no |
| host CPU busy, the real machine under kind (%) | 41.15 | 41.58 | +1.1% | -0.1677 to +1.037 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 555.4 | 555.3 | -0.0% | -9.508 to +9.308 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.876 | -35.4% | -2.51 to -1.737 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*