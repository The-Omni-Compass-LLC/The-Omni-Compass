# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.1 |
| node-hours | 2.517 | 2.131 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 246.1 |
| response time (ms), mean | 598 | 531.9 |
| response time (ms), 95th percentile | 3507 | 3519 |
| response time (ms), 99th percentile | 5055 | 5180 |
| time over the response line (% of samples) | 16.84 | 16.25 |
| failed requests (%) | 0.01058 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 202.6 | 206.5 |
| utilisation (used / allocatable) | 0.06616 | 0.07817 |
| CPU used (cores), mean | 1.588 | 1.593 |
| Omni's own CPU (cores), mean | 0 | 0.02258 |
| CPU used with Omni's own (cores), mean | 1.588 | 1.616 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.6 | 370.3 |
| HPA replicas, mean | 2.097 | 2.327 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 9.7 |
| pod start wait, mean (s) | 0 | 9.7 |
| host CPU busy, the real machine under kind (%) | 45.72 | 46.68 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 626.6 | 631.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.45 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.1 | -15.0% | -1.125 to -0.6759 | yes, better |
| node-hours | 2.517 | 2.131 | -15.3% | -0.4779 to -0.2931 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 274.3 | -0.3% | -1.684 to +0.03825 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 246.1 | -10.6% | -36.03 to -22.09 | yes, better |
| response time (ms), mean | 598 | 531.9 | -11.1% | -80.22 to -51.98 | yes, better |
| response time (ms), 95th percentile | 3507 | 3519 | +0.3% | -100.7 to +125 | no |
| response time (ms), 99th percentile | 5055 | 5180 | +2.5% | -60 to +310.1 | no |
| time over the response line (% of samples) | 16.84 | 16.25 | -3.5% | -0.9339 to -0.2505 | yes, better |
| failed requests (%) | 0.01058 | 0 | -100.0% | -0.03452 to +0.01335 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 202.6 | 206.5 | +1.9% | -1.905 to +9.665 | no |
| utilisation (used / allocatable) | 0.06616 | 0.07817 | +18.1% | +0.008869 to +0.01514 | yes, more |
| CPU used (cores), mean | 1.588 | 1.593 | +0.3% | -0.02662 to +0.03717 | no |
| Omni's own CPU (cores), mean | 0 | 0.02258 | +0.0226 (native is 0) | +0.01955 to +0.02561 | yes, more |
| CPU used with Omni's own (cores), mean | 1.588 | 1.616 | +1.8% | -0.006447 to +0.06215 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.6 | 370.3 | -10.7% | -58.05 to -30.48 | yes, less |
| HPA replicas, mean | 2.097 | 2.327 | +11.0% | -0.04419 to +0.5051 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 9.7 | +9.7 (native is 0) | -5.006 to +24.41 | no |
| pod start wait, mean (s) | 0 | 9.7 | +9.7 (native is 0) | -5.006 to +24.41 | no |
| host CPU busy, the real machine under kind (%) | 45.72 | 46.68 | +2.1% | +0.6042 to +1.305 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 626.6 | 631.1 | +0.7% | +0.1132 to +8.887 | yes, worse |
| batch: worker machines in service after the queue finished, mean | 6 | 4.45 | -25.8% | -1.898 to -1.201 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*