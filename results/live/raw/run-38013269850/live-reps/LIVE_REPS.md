# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.058 |
| node-hours | 2.519 | 2.122 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 244.2 |
| response time (ms), mean | 534.5 | 466.9 |
| response time (ms), 95th percentile | 3185 | 3125 |
| response time (ms), 99th percentile | 4742 | 4673 |
| time over the response line (% of samples) | 15.8 | 15.33 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.5 | 192.6 |
| utilisation (used / allocatable) | 0.0611 | 0.07342 |
| CPU used (cores), mean | 1.466 | 1.484 |
| Omni's own CPU (cores), mean | 0 | 0.0186 |
| CPU used with Omni's own (cores), mean | 1.466 | 1.395 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.2 | 394.6 |
| HPA replicas, mean | 2.235 | 2.078 |
| pods started | 0.2 | 0.1 |
| pod start wait, total (s) | 10.5 | 0.2 |
| pod start wait, mean (s) | 5.25 | 0.2 |
| host CPU busy, the real machine under kind (%) | 42.84 | 43.67 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 584.6 | 587.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.457 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.058 | -15.7% | -1.174 to -0.7102 | yes, better |
| node-hours | 2.519 | 2.122 | -15.8% | -0.4976 to -0.2964 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 | +0.1% | -0.9343 to +1.365 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 244.2 | -10.8% | -37.49 to -21.33 | yes, better |
| response time (ms), mean | 534.5 | 466.9 | -12.6% | -81.63 to -53.59 | yes, better |
| response time (ms), 95th percentile | 3185 | 3125 | -1.9% | -158.5 to +38.85 | no |
| response time (ms), 99th percentile | 4742 | 4673 | -1.4% | -210.4 to +72.94 | no |
| time over the response line (% of samples) | 15.8 | 15.33 | -3.0% | -1.123 to +0.1829 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 190.5 | 192.6 | +1.1% | -6.506 to +10.78 | no |
| utilisation (used / allocatable) | 0.0611 | 0.07342 | +20.2% | +0.01015 to +0.01449 | yes, more |
| CPU used (cores), mean | 1.466 | 1.484 | +1.2% | -0.02409 to +0.05991 | no |
| Omni's own CPU (cores), mean | 0 | 0.0186 | +0.0186 (native is 0) | +0.01519 to +0.02201 | yes, more |
| CPU used with Omni's own (cores), mean | 1.466 | 1.503 | +2.5% | -0.02301 to +0.09633 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.2 | 394.6 | -12.0% | -65.38 to -41.91 | yes, less |
| HPA replicas, mean | 2.235 | 2.078 | -7.0% | -0.4717 to +0.1591 | no |
| pods started | 0.2 | 0.1 | -50.0% | -0.6278 to +0.4278 | no |
| pod start wait, total (s) | 10.5 | 0.2 | -98.1% | -34.11 to +13.51 | no |
| pod start wait, mean (s) | 5.25 | 0.2 | -96.2% | -16.98 to +6.884 | no |
| host CPU busy, the real machine under kind (%) | 42.84 | 43.67 | +1.9% | +0.4047 to +1.245 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 584.6 | 587.6 | +0.5% | -3.308 to +9.308 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.457 | -25.7% | -1.877 to -1.209 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*