# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.429 |
| node-hours | 4.33 | 3.925 |
| energy, parked workers still on at idle power (Wh, declared model) | 477.2 | 476.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.2 | 445.3 |
| response time (ms), mean | 242.4 | 118.4 |
| response time (ms), 95th percentile | 624.2 | 216.2 |
| response time (ms), 99th percentile | 1205 | 615.9 |
| time over the response line (% of samples) | 10.55 | 2.009 |
| failed requests (%) | 0.9852 | 0.8605 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9283 | 0.7483 |
| utilisation (used / allocatable) | 0.07279 | 0.07556 |
| CPU used (cores), mean | 1.747 | 1.672 |
| Omni's own CPU (cores), mean | 0 | 0.0096 |
| CPU used with Omni's own (cores), mean | 1.747 | 1.681 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.9 | 403.3 |
| HPA replicas, mean | 9.62 | 9.012 |
| pods started | 6.2 | 7.6 |
| pod start wait, total (s) | 22.8 | 22.6 |
| pod start wait, mean (s) | 2.911 | 2.669 |
| host CPU busy, the real machine under kind (%) | 50.8 | 49.19 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.429 | -9.5% | -0.9673 to -0.1744 | yes, better |
| node-hours | 4.33 | 3.925 | -9.4% | -0.688 to -0.1225 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 477.2 | 476.2 | -0.2% | -2.483 to +0.6078 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.2 | 445.3 | -6.7% | -52.44 to -11.38 | yes, better |
| response time (ms), mean | 242.4 | 118.4 | -51.2% | -178.7 to -69.36 | yes, better |
| response time (ms), 95th percentile | 624.2 | 216.2 | -65.4% | -582.2 to -233.8 | yes, better |
| response time (ms), 99th percentile | 1205 | 615.9 | -48.9% | -843.6 to -333.8 | yes, better |
| time over the response line (% of samples) | 10.55 | 2.009 | -81.0% | -13.92 to -3.172 | yes, better |
| failed requests (%) | 0.9852 | 0.8605 | -12.7% | -0.247 to -0.002493 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9283 | 0.7483 | -19.4% | -0.7339 to +0.3739 | no |
| utilisation (used / allocatable) | 0.07279 | 0.07556 | +3.8% | -0.001819 to +0.007361 | no |
| CPU used (cores), mean | 1.747 | 1.672 | -4.3% | -0.09821 to -0.05197 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0096 | +0.0096 (native is 0) | +0.008135 to +0.01107 | yes, more |
| CPU used with Omni's own (cores), mean | 1.747 | 1.681 | -3.7% | -0.08723 to -0.04375 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.9 | 403.3 | -4.8% | -45.42 to +4.38 | no |
| HPA replicas, mean | 9.62 | 9.012 | -6.3% | -0.9883 to -0.2278 | yes, better |
| pods started | 6.2 | 7.6 | +22.6% | -0.5134 to +3.313 | no |
| pod start wait, total (s) | 22.8 | 22.6 | -0.9% | -8.135 to +7.735 | no |
| pod start wait, mean (s) | 2.911 | 2.669 | -8.3% | -1.099 to +0.616 | no |
| host CPU busy, the real machine under kind (%) | 50.8 | 49.19 | -3.2% | -2.197 to -1.024 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*