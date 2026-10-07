# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.786 |
| node-hours | 2.516 | 2.004 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 235.1 |
| response time (ms), mean | 522.4 | 468.7 |
| response time (ms), 95th percentile | 3162 | 3141 |
| response time (ms), 99th percentile | 4697 | 4707 |
| time over the response line (% of samples) | 15.88 | 15.3 |
| failed requests (%) | 0.01064 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 192 | 192.2 |
| utilisation (used / allocatable) | 0.06239 | 0.07725 |
| CPU used (cores), mean | 1.497 | 1.482 |
| Omni's own CPU (cores), mean | 0 | 0.02 |
| CPU used with Omni's own (cores), mean | 1.497 | 1.502 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.6 | 381.7 |
| HPA replicas, mean | 2.195 | 2.15 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 42.89 | 43.53 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 588.1 | 587.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.042 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.786 | -20.2% | -1.563 to -0.8653 | yes, better |
| node-hours | 2.516 | 2.004 | -20.3% | -0.6531 to -0.3705 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.3 | -0.1% | -1.039 to +0.5178 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 235.1 | -14.0% | -49.08 to -27.74 | yes, better |
| response time (ms), mean | 522.4 | 468.7 | -10.3% | -67.58 to -39.8 | yes, better |
| response time (ms), 95th percentile | 3162 | 3141 | -0.7% | -146.2 to +104.2 | no |
| response time (ms), 99th percentile | 4697 | 4707 | +0.2% | -221 to +242.1 | no |
| time over the response line (% of samples) | 15.88 | 15.3 | -3.6% | -1.144 to -0.01185 | yes, better |
| failed requests (%) | 0.01064 | 0 | -100.0% | -0.0347 to +0.01343 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 192 | 192.2 | +0.1% | -4.514 to +4.867 | no |
| utilisation (used / allocatable) | 0.06239 | 0.07725 | +23.8% | +0.01123 to +0.0185 | yes, more |
| CPU used (cores), mean | 1.497 | 1.482 | -1.0% | -0.04926 to +0.0181 | no |
| Omni's own CPU (cores), mean | 0 | 0.02 | +0.02 (native is 0) | +0.01689 to +0.02311 | yes, more |
| CPU used with Omni's own (cores), mean | 1.497 | 1.502 | +0.3% | -0.03035 to +0.03919 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.6 | 381.7 | -13.4% | -79.47 to -38.43 | yes, less |
| HPA replicas, mean | 2.195 | 2.15 | -2.0% | -0.2844 to +0.1953 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 42.89 | 43.53 | +1.5% | +0.1777 to +1.116 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 588.1 | 587.4 | -0.1% | -3.935 to +2.535 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.042 | -32.6% | -2.392 to -1.524 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*