# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 199.1 | 82.63 |
| response time (ms), 95th percentile | 469.5 | 126.7 |
| response time (ms), 99th percentile | 630.1 | 225.2 |
| time over the response line (% of samples) | 4.406 | 0.09599 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5833 | 0.3883 |
| utilisation (used / allocatable) | 0.03127 | 0.04806 |
| CPU used (cores), mean | 0.7505 | 1.153 |
| Omni's own CPU (cores), mean | 0 | 0.00959 |
| CPU used with Omni's own (cores), mean | 0.7505 | 1.163 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 836.8 | 563.9 |
| HPA replicas, mean | 2.905 | 2.552 |
| pods started | 3 | 2.6 |
| pod start wait, total (s) | 26.3 | 25.8 |
| pod start wait, mean (s) | 8.767 | 9.983 |
| host CPU busy, the real machine under kind (%) | 23.65 | 35.14 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.516 | -0.2% | -0.009132 to +0.004132 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.7 | +2.3% | +2.547 to +4.664 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.7 | +2.3% | +2.547 to +4.664 | yes: power given |
| response time (ms), mean | 199.1 | 82.63 | -58.5% | -140 to -92.89 | yes: GAIN |
| response time (ms), 95th percentile | 469.5 | 126.7 | -73.0% | -398.9 to -286.6 | yes: GAIN |
| response time (ms), 99th percentile | 630.1 | 225.2 | -64.3% | -481.5 to -328.4 | yes: GAIN |
| time over the response line (% of samples) | 4.406 | 0.09599 | -97.8% | -6.555 to -2.064 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5833 | 0.3883 | -33.4% | -0.3791 to -0.0109 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03127 | 0.04806 | +53.7% | +0.01397 to +0.0196 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7505 | 1.153 | +53.7% | +0.3354 to +0.4704 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00959 | +0.00959 (native is 0) | +0.008311 to +0.01087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7505 | 1.163 | +55.0% | +0.3438 to +0.4811 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 836.8 | 563.9 | -32.6% | -285.2 to -260.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.905 | 2.552 | -12.1% | -0.5063 to -0.1982 | yes: GAIN |
| pods started | 3 | 2.6 | -13.3% | -0.9001 to +0.1001 | no |
| pod start wait, total (s) | 26.3 | 25.8 | -1.9% | -6.054 to +5.054 | no |
| pod start wait, mean (s) | 8.767 | 9.983 | +13.9% | +0.1697 to +2.264 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.65 | 35.14 | +48.6% | +9.49 to +13.5 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*