# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 162.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 162.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 151.6 | 89.77 |
| response time (ms), 95th percentile | 300 | 133.1 |
| response time (ms), 99th percentile | 433.8 | 161.5 |
| time over the response line (% of samples) | 0.5279 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.3467 |
| utilisation (used / allocatable) | 0.03754 | 0.05071 |
| CPU used (cores), mean | 0.9009 | 1.217 |
| Omni's own CPU (cores), mean | 0 | 0.01206 |
| CPU used with Omni's own (cores), mean | 0.9009 | 1.229 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 699.1 | 528.3 |
| HPA replicas, mean | 8.904 | 9.223 |
| pods started | 4.8 | 5 |
| pod start wait, total (s) | 11.9 | 15.3 |
| pod start wait, mean (s) | 2.37 | 2.9 |
| host CPU busy, the real machine under kind (%) | 27.65 | 37.08 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.733e-16 to +1.062e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.519 | +0.0% | -0.008006 to +0.009006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 162.4 | +1.9% | +2.343 to +3.809 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 162.4 | +1.9% | +2.343 to +3.809 | yes: power given |
| response time (ms), mean | 151.6 | 89.77 | -40.8% | -69.18 to -54.5 | yes: GAIN |
| response time (ms), 95th percentile | 300 | 133.1 | -55.6% | -183.9 to -149.9 | yes: GAIN |
| response time (ms), 99th percentile | 433.8 | 161.5 | -62.8% | -296.2 to -248.2 | yes: GAIN |
| time over the response line (% of samples) | 0.5279 | 0 | -100.0% | -0.793 to -0.2628 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.3467 | +118.9% | -0.1067 to +0.4833 | no |
| utilisation (used / allocatable) | 0.03754 | 0.05071 | +35.1% | +0.01159 to +0.01475 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9009 | 1.217 | +35.1% | +0.2782 to +0.3539 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01206 | +0.0121 (native is 0) | +0.01093 to +0.01319 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9009 | 1.229 | +36.4% | +0.2894 to +0.3668 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 699.1 | 528.3 | -24.4% | -185.8 to -155.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.904 | 9.223 | +3.6% | +0.2109 to +0.4263 | yes: power given |
| pods started | 4.8 | 5 | +4.2% | -0.4573 to +0.8573 | no |
| pod start wait, total (s) | 11.9 | 15.3 | +28.6% | -2.901 to +9.701 | no |
| pod start wait, mean (s) | 2.37 | 2.9 | +22.4% | -0.4812 to +1.541 | no |
| host CPU busy, the real machine under kind (%) | 27.65 | 37.08 | +34.1% | +8.525 to +10.33 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*