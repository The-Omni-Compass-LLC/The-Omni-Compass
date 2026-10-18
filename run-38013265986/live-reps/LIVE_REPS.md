# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.799 |
| node-hours | 2.514 | 2.011 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 236.1 |
| response time (ms), mean | 540.4 | 479.9 |
| response time (ms), 95th percentile | 3168 | 3173 |
| response time (ms), 99th percentile | 4895 | 4908 |
| time over the response line (% of samples) | 16 | 15.4 |
| failed requests (%) | 0.02542 | 0.0102 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.4 | 193.9 |
| utilisation (used / allocatable) | 0.06296 | 0.07802 |
| CPU used (cores), mean | 1.511 | 1.5 |
| Omni's own CPU (cores), mean | 0 | 0.0182 |
| CPU used with Omni's own (cores), mean | 1.511 | 1.465 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.1 | 378.1 |
| HPA replicas, mean | 2.095 | 2.2 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 10.8 |
| pod start wait, mean (s) | 0 | 10.8 |
| host CPU busy, the real machine under kind (%) | 43.38 | 44.04 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 593.3 | 595.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.05 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.799 | -20.0% | -1.575 to -0.8274 | yes, better |
| node-hours | 2.514 | 2.011 | -20.0% | -0.6566 to -0.3496 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.9 | +0.0% | -0.8987 to +1.105 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 236.1 | -13.8% | -48.99 to -26.37 | yes, better |
| response time (ms), mean | 540.4 | 479.9 | -11.2% | -80.52 to -40.48 | yes, better |
| response time (ms), 95th percentile | 3168 | 3173 | +0.2% | -149.7 to +160.2 | no |
| response time (ms), 99th percentile | 4895 | 4908 | +0.3% | -147.6 to +173.1 | no |
| time over the response line (% of samples) | 16 | 15.4 | -3.7% | -0.9384 to -0.2592 | yes, better |
| failed requests (%) | 0.02542 | 0.0102 | -59.9% | -0.07952 to +0.04908 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.4 | 193.9 | +1.8% | -2.141 to +9.058 | no |
| utilisation (used / allocatable) | 0.06296 | 0.07802 | +23.9% | +0.01009 to +0.02003 | yes, more |
| CPU used (cores), mean | 1.511 | 1.5 | -0.7% | -0.04546 to +0.02408 | no |
| Omni's own CPU (cores), mean | 0 | 0.0182 | +0.0182 (native is 0) | +0.01395 to +0.02245 | yes, more |
| CPU used with Omni's own (cores), mean | 1.511 | 1.526 | +1.0% | -0.03741 to +0.06783 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.1 | 378.1 | -14.3% | -97.77 to -28.21 | yes, less |
| HPA replicas, mean | 2.095 | 2.2 | +5.0% | -0.1553 to +0.3667 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 10.8 | +10.8 (native is 0) | -5.5 to +27.1 | no |
| pod start wait, mean (s) | 0 | 10.8 | +10.8 (native is 0) | -5.5 to +27.1 | no |
| host CPU busy, the real machine under kind (%) | 43.38 | 44.04 | +1.5% | +0.3692 to +0.9476 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 593.3 | 595.2 | +0.3% | -4.642 to +8.442 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.05 | -32.5% | -2.428 to -1.472 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*