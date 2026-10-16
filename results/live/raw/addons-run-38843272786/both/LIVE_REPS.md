# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 161.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 138.9 | 86.55 |
| response time (ms), 95th percentile | 287.7 | 133.8 |
| response time (ms), 99th percentile | 410.3 | 173.6 |
| time over the response line (% of samples) | 0.5918 | 0.01235 |
| failed requests (%) | 0.01282 | 0.01235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.27 |
| utilisation (used / allocatable) | 0.03675 | 0.04847 |
| CPU used (cores), mean | 0.8819 | 1.163 |
| Omni's own CPU (cores), mean | 0 | 0.01287 |
| CPU used with Omni's own (cores), mean | 0.8819 | 1.176 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 715.3 | 557.9 |
| HPA replicas, mean | 8.93 | 9.429 |
| pods started | 4.7 | 5.5 |
| pod start wait, total (s) | 10.8 | 14.6 |
| pod start wait, mean (s) | 2.225 | 2.61 |
| host CPU busy, the real machine under kind (%) | 27.51 | 35.96 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +9.868e-17 to +1.145e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.518 | -0.1% | -0.009691 to +0.007357 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 161.7 | +1.6% | +1.172 to +3.93 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 161.7 | +1.6% | +1.172 to +3.93 | yes: power given |
| response time (ms), mean | 138.9 | 86.55 | -37.7% | -67.3 to -37.44 | yes: GAIN |
| response time (ms), 95th percentile | 287.7 | 133.8 | -53.5% | -186.5 to -121.3 | yes: GAIN |
| response time (ms), 99th percentile | 410.3 | 173.6 | -57.7% | -286.8 to -186.5 | yes: GAIN |
| time over the response line (% of samples) | 0.5918 | 0.01235 | -97.9% | -0.8936 to -0.2654 | yes: GAIN |
| failed requests (%) | 0.01282 | 0.01235 | -3.7% | -0.04291 to +0.04196 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | -100.0% | -0.6455 to +0.04553 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.7 | +19.7 (native is 0) | +14.03 to +25.37 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.27 | +70.5% | -0.2279 to +0.4512 | no |
| utilisation (used / allocatable) | 0.03675 | 0.04847 | +31.9% | +0.008782 to +0.01467 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8819 | 1.163 | +31.9% | +0.2108 to +0.352 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01287 | +0.0129 (native is 0) | +0.01058 to +0.01516 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8819 | 1.176 | +33.4% | +0.2217 to +0.3668 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 715.3 | 557.9 | -22.0% | -186.5 to -128.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.93 | 9.429 | +5.6% | -0.3179 to +1.317 | no |
| pods started | 4.7 | 5.5 | +17.0% | -0.6226 to +2.223 | no |
| pod start wait, total (s) | 10.8 | 14.6 | +35.2% | -1.687 to +9.287 | no |
| pod start wait, mean (s) | 2.225 | 2.61 | +17.3% | -0.4696 to +1.239 | no |
| host CPU busy, the real machine under kind (%) | 27.51 | 35.96 | +30.7% | +6.417 to +10.49 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*