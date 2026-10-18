# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.789 |
| node-hours | 4.512 | 4.359 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.3 | 512.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.3 | 500.2 |
| response time (ms), mean | 256 | 137.8 |
| response time (ms), 95th percentile | 670.6 | 287 |
| response time (ms), 99th percentile | 2242 | 1102 |
| time over the response line (% of samples) | 16.49 | 10.11 |
| failed requests (%) | 8.897 | 8.015 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6183 | 0.655 |
| utilisation (used / allocatable) | 0.09524 | 0.09576 |
| CPU used (cores), mean | 2.286 | 2.248 |
| Omni's own CPU (cores), mean | 0 | 0.0086 |
| CPU used with Omni's own (cores), mean | 2.286 | 2.256 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 331.1 | 326.5 |
| HPA replicas, mean | 9.505 | 9.439 |
| pods started | 5.6 | 4.2 |
| pod start wait, total (s) | 22.9 | 17.2 |
| pod start wait, mean (s) | 3.836 | 2.922 |
| host CPU busy, the real machine under kind (%) | 64.46 | 63.8 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.789 | -3.5% | -0.4727 to +0.05095 | no |
| node-hours | 4.512 | 4.359 | -3.4% | -0.3529 to +0.04736 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.3 | 512.1 | -0.0% | -1.733 to +1.37 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.3 | 500.2 | -2.4% | -27.48 to +3.307 | no |
| response time (ms), mean | 256 | 137.8 | -46.2% | -159 to -77.31 | yes, better |
| response time (ms), 95th percentile | 670.6 | 287 | -57.2% | -492.6 to -274.7 | yes, better |
| response time (ms), 99th percentile | 2242 | 1102 | -50.8% | -1942 to -337.7 | yes, better |
| time over the response line (% of samples) | 16.49 | 10.11 | -38.7% | -9.138 to -3.618 | yes, better |
| failed requests (%) | 8.897 | 8.015 | -9.9% | -1.636 to -0.1271 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6183 | 0.655 | +5.9% | -0.451 to +0.5243 | no |
| utilisation (used / allocatable) | 0.09524 | 0.09576 | +0.5% | -0.002159 to +0.003205 | no |
| CPU used (cores), mean | 2.286 | 2.248 | -1.7% | -0.07939 to +0.00354 | no |
| Omni's own CPU (cores), mean | 0 | 0.0086 | +0.0086 (native is 0) | +0.007269 to +0.009931 | yes, more |
| CPU used with Omni's own (cores), mean | 2.286 | 2.256 | -1.3% | -0.07073 to +0.01208 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 331.1 | 326.5 | -1.4% | -13.85 to +4.611 | no |
| HPA replicas, mean | 9.505 | 9.439 | -0.7% | -0.2642 to +0.1339 | no |
| pods started | 5.6 | 4.2 | -25.0% | -3.159 to +0.3586 | no |
| pod start wait, total (s) | 22.9 | 17.2 | -24.9% | -14.36 to +2.963 | no |
| pod start wait, mean (s) | 3.836 | 2.922 | -23.8% | -1.922 to +0.09477 | no |
| host CPU busy, the real machine under kind (%) | 64.46 | 63.8 | -1.0% | -1.755 to +0.4401 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*