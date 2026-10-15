# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 198.5 | 81.9 |
| response time (ms), 95th percentile | 474.8 | 128.8 |
| response time (ms), 99th percentile | 640.7 | 190.9 |
| time over the response line (% of samples) | 4.676 | 0.1215 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.3533 |
| utilisation (used / allocatable) | 0.03128 | 0.04734 |
| CPU used (cores), mean | 0.7508 | 1.136 |
| Omni's own CPU (cores), mean | 0 | 0.00945 |
| CPU used with Omni's own (cores), mean | 0.7508 | 1.146 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 835.2 | 571.7 |
| HPA replicas, mean | 2.925 | 2.411 |
| pods started | 2.9 | 2.3 |
| pod start wait, total (s) | 23.8 | 21.2 |
| pod start wait, mean (s) | 8.167 | 9.15 |
| host CPU busy, the real machine under kind (%) | 23.76 | 34.94 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.833e-16 to +1.116e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.511 | -0.6% | -0.01332 to -0.004676 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.3 | 161 | +1.7% | +1.624 to +3.856 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.3 | 161 | +1.7% | +1.624 to +3.856 | yes: power given |
| response time (ms), mean | 198.5 | 81.9 | -58.7% | -141 to -92.21 | yes: GAIN |
| response time (ms), 95th percentile | 474.8 | 128.8 | -72.9% | -405 to -287 | yes: GAIN |
| response time (ms), 99th percentile | 640.7 | 190.9 | -70.2% | -525.1 to -374.4 | yes: GAIN |
| time over the response line (% of samples) | 4.676 | 0.1215 | -97.4% | -6.735 to -2.374 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 0.1 | -98.0% | -7.456 to -2.344 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 | +4.3 (native is 0) | +3.954 to +4.646 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.3533 | +11.6% | -0.2094 to +0.2827 | no |
| utilisation (used / allocatable) | 0.03128 | 0.04734 | +51.3% | +0.01306 to +0.01906 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7508 | 1.136 | +51.3% | +0.3134 to +0.4575 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00945 | +0.00945 (native is 0) | +0.008233 to +0.01067 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7508 | 1.146 | +52.6% | +0.3217 to +0.4681 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 835.2 | 571.7 | -31.6% | -282.7 to -244.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.925 | 2.411 | -17.6% | -0.687 to -0.34 | yes: GAIN |
| pods started | 2.9 | 2.3 | -20.7% | -0.9694 to -0.2306 | yes: GAIN |
| pod start wait, total (s) | 23.8 | 21.2 | -10.9% | -7.869 to +2.669 | no |
| pod start wait, mean (s) | 8.167 | 9.15 | +12.0% | -0.4177 to +2.384 | no |
| host CPU busy, the real machine under kind (%) | 23.76 | 34.94 | +47.1% | +9.082 to +13.29 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*