# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.925 |
| node-hours | 4.513 | 4.463 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 522.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 518.4 |
| response time (ms), mean | 315.6 | 172.6 |
| response time (ms), 95th percentile | 823.8 | 310.4 |
| response time (ms), 99th percentile | 3022 | 2349 |
| time over the response line (% of samples) | 22.44 | 14.26 |
| failed requests (%) | 13.28 | 11.68 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4517 | 0.295 |
| utilisation (used / allocatable) | 0.1114 | 0.1098 |
| CPU used (cores), mean | 2.674 | 2.616 |
| Omni's own CPU (cores), mean | 0 | 0.00943 |
| CPU used with Omni's own (cores), mean | 2.674 | 2.625 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.7 | 274.8 |
| HPA replicas, mean | 9.718 | 9.656 |
| pods started | 3.8 | 3.4 |
| pod start wait, total (s) | 11.1 | 8.8 |
| pod start wait, mean (s) | 2.613 | 2.234 |
| host CPU busy, the real machine under kind (%) | 74.62 | 73.49 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.925 | -1.2% | -0.2441 to +0.09445 | no |
| node-hours | 4.513 | 4.463 | -1.1% | -0.1783 to +0.07856 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.3 | 522.6 | -0.1% | -1.187 to -0.2045 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.3 | 518.4 | -0.9% | -14.33 to +4.483 | no |
| response time (ms), mean | 315.6 | 172.6 | -45.3% | -183.4 to -102.6 | yes, better |
| response time (ms), 95th percentile | 823.8 | 310.4 | -62.3% | -656.6 to -370.2 | yes, better |
| response time (ms), 99th percentile | 3022 | 2349 | -22.3% | -1695 to +349.1 | no |
| time over the response line (% of samples) | 22.44 | 14.26 | -36.4% | -10.17 to -6.19 | yes, better |
| failed requests (%) | 13.28 | 11.68 | -12.0% | -2.345 to -0.8416 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4517 | 0.295 | -34.7% | -0.3442 to +0.03084 | no |
| utilisation (used / allocatable) | 0.1114 | 0.1098 | -1.5% | -0.003771 to +0.0004675 | no |
| CPU used (cores), mean | 2.674 | 2.616 | -2.2% | -0.07446 to -0.04154 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00943 | +0.00943 (native is 0) | +0.008467 to +0.01039 | yes, more |
| CPU used with Omni's own (cores), mean | 2.674 | 2.625 | -1.8% | -0.06471 to -0.03244 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.7 | 274.8 | +0.4% | -7.474 to +9.77 | no |
| HPA replicas, mean | 9.718 | 9.656 | -0.6% | -0.1824 to +0.05959 | no |
| pods started | 3.8 | 3.4 | -10.5% | -1.578 to +0.7778 | no |
| pod start wait, total (s) | 11.1 | 8.8 | -20.7% | -7.779 to +3.179 | no |
| pod start wait, mean (s) | 2.613 | 2.234 | -14.5% | -1.169 to +0.4098 | no |
| host CPU busy, the real machine under kind (%) | 74.62 | 73.49 | -1.5% | -1.608 to -0.6502 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*