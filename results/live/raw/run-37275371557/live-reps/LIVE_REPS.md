# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.986 |
| node-hours | 2.514 | 2.088 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 241.5 |
| response time (ms), mean | 509.9 | 455.6 |
| response time (ms), 95th percentile | 3017 | 3014 |
| response time (ms), 99th percentile | 4700 | 4702 |
| time over the response line (% of samples) | 15.64 | 15.25 |
| failed requests (%) | 0.281 | 0.2408 |
| pending pods, pod-minutes | 188.4 | 194.2 |
| utilisation (used / allocatable) | 0.06272 | 0.07452 |
| CPU used (cores), mean | 1.505 | 1.486 |
| Omni's own CPU (cores), mean | 0 | 0.02208 |
| CPU used with Omni's own (cores), mean | 1.505 | 1.508 |
| energy per core-hour (Wh, the 25 W standby model) | 440.4 | 391.6 |
| HPA replicas, mean | 2.331 | 2.587 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 42.9 | 43.98 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 584 | 594.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.366 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.986 | -16.9% | -1.447 to -0.5806 | yes, better |
| node-hours | 2.514 | 2.088 | -16.9% | -0.6024 to -0.2491 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.3 | +0.0% | -0.6275 to +0.7862 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 241.5 | -11.6% | -45.03 to -18.55 | yes, better |
| response time (ms), mean | 509.9 | 455.6 | -10.6% | -75.04 to -33.54 | yes, better |
| response time (ms), 95th percentile | 3017 | 3014 | -0.1% | -140.3 to +135.2 | no |
| response time (ms), 99th percentile | 4700 | 4702 | +0.0% | -310.2 to +313.2 | no |
| time over the response line (% of samples) | 15.64 | 15.25 | -2.5% | -0.8613 to +0.07957 | no |
| failed requests (%) | 0.281 | 0.2408 | -14.3% | -0.1318 to +0.05144 | no |
| pending pods, pod-minutes | 188.4 | 194.2 | +3.0% | +0.603 to +10.87 | yes, worse |
| utilisation (used / allocatable) | 0.06272 | 0.07452 | +18.8% | +0.00687 to +0.01674 | yes, more |
| CPU used (cores), mean | 1.505 | 1.486 | -1.3% | -0.04933 to +0.01044 | no |
| Omni's own CPU (cores), mean | 0 | 0.02208 | +0.0221 (native is 0) | +0.0182 to +0.02596 | yes, more |
| CPU used with Omni's own (cores), mean | 1.505 | 1.508 | +0.2% | -0.02861 to +0.03388 | no |
| energy per core-hour (Wh, the 25 W standby model) | 440.4 | 391.6 | -11.1% | -75.03 to -22.65 | yes, better |
| HPA replicas, mean | 2.331 | 2.587 | +11.0% | -0.1902 to +0.7013 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 42.9 | 43.98 | +2.5% | +0.8443 to +1.316 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 584 | 594.3 | +1.8% | +7.379 to +13.22 | yes, worse |
| batch: worker machines in service after the queue finished, mean | 6 | 4.366 | -27.2% | -2.232 to -1.036 | yes, better |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*