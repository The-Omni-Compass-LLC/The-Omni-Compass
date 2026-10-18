# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.91 |
| node-hours | 1.512 | 1.494 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 157 |
| response time (ms), mean | 142.1 | 75.18 |
| response time (ms), 95th percentile | 315.5 | 107 |
| response time (ms), 99th percentile | 492 | 144.3 |
| time over the response line (% of samples) | 1.646 | 0.01212 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3367 | 0.3717 |
| utilisation (used / allocatable) | 0.03721 | 0.03624 |
| CPU used (cores), mean | 0.8929 | 0.857 |
| Omni's own CPU (cores), mean | 0 | 0.00915 |
| CPU used with Omni's own (cores), mean | 0.8929 | 0.8662 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.5 | 757.6 |
| HPA replicas, mean | 8.509 | 8.101 |
| pods started | 4.3 | 4.6 |
| pod start wait, total (s) | 17.3 | 18.7 |
| pod start wait, mean (s) | 3.47 | 3.723 |
| host CPU busy, the real machine under kind (%) | 27.1 | 26.53 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.91 | -1.5% | -0.1248 to -0.05585 | yes, better |
| node-hours | 1.512 | 1.494 | -1.2% | -0.02619 to -0.008862 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.7 | +0.1% | -0.3532 to +0.7643 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 157 | -1.0% | -2.101 to -0.9168 | yes, better |
| response time (ms), mean | 142.1 | 75.18 | -47.1% | -89.99 to -43.85 | yes, better |
| response time (ms), 95th percentile | 315.5 | 107 | -66.1% | -273.1 to -143.9 | yes, better |
| response time (ms), 99th percentile | 492 | 144.3 | -70.7% | -465 to -230.3 | yes, better |
| time over the response line (% of samples) | 1.646 | 0.01212 | -99.3% | -2.927 to -0.3403 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3367 | 0.3717 | +10.4% | -0.1306 to +0.2006 | no |
| utilisation (used / allocatable) | 0.03721 | 0.03624 | -2.6% | -0.002046 to +0.0001119 | no |
| CPU used (cores), mean | 0.8929 | 0.857 | -4.0% | -0.06315 to -0.008657 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00915 | +0.00915 (native is 0) | +0.007819 to +0.01048 | yes, more |
| CPU used with Omni's own (cores), mean | 0.8929 | 0.8662 | -3.0% | -0.05309 to -0.0004081 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 744.5 | 757.6 | +1.8% | -3.6 to +29.79 | no |
| HPA replicas, mean | 8.509 | 8.101 | -4.8% | -0.6158 to -0.201 | yes, better |
| pods started | 4.3 | 4.6 | +7.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 17.3 | 18.7 | +8.1% | -3.57 to +6.37 | no |
| pod start wait, mean (s) | 3.47 | 3.723 | +7.3% | -0.6505 to +1.157 | no |
| host CPU busy, the real machine under kind (%) | 27.1 | 26.53 | -2.1% | -1.172 to +0.03002 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*