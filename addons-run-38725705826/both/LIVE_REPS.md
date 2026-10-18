# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 114.3 | 72.41 |
| response time (ms), 95th percentile | 247.1 | 111.8 |
| response time (ms), 99th percentile | 359 | 137.2 |
| time over the response line (% of samples) | 0.3988 | 0 |
| failed requests (%) | 0.01266 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.32 |
| utilisation (used / allocatable) | 0.03581 | 0.04561 |
| CPU used (cores), mean | 0.8594 | 1.095 |
| Omni's own CPU (cores), mean | 0 | 0.01119 |
| CPU used with Omni's own (cores), mean | 0.8594 | 1.106 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733 | 592.3 |
| HPA replicas, mean | 8.762 | 8.904 |
| pods started | 4.8 | 5 |
| pod start wait, total (s) | 11.6 | 15.5 |
| pod start wait, mean (s) | 2.353 | 2.997 |
| host CPU busy, the real machine under kind (%) | 26.74 | 33.68 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.206e-16 to +5.43e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.515 | -0.2% | -0.0131 to +0.006767 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 160.7 | +1.2% | +0.2004 to +3.57 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 160.7 | +1.2% | +0.2004 to +3.57 | yes: power given |
| response time (ms), mean | 114.3 | 72.41 | -36.7% | -57.91 to -25.88 | yes: GAIN |
| response time (ms), 95th percentile | 247.1 | 111.8 | -54.8% | -168.3 to -102.4 | yes: GAIN |
| response time (ms), 99th percentile | 359 | 137.2 | -61.8% | -272.1 to -171.4 | yes: GAIN |
| time over the response line (% of samples) | 0.3988 | 0 | -100.0% | -0.8094 to +0.01185 | no |
| failed requests (%) | 0.01266 | 0 | -100.0% | -0.04129 to +0.01597 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 | -100.0% | -1.369 to +0.1689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | +17.7 (native is 0) | +16.63 to +18.77 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.32 | +140.0% | -0.09839 to +0.4717 | no |
| utilisation (used / allocatable) | 0.03581 | 0.04561 | +27.4% | +0.00658 to +0.01302 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8594 | 1.095 | +27.4% | +0.1579 to +0.3125 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01119 | +0.0112 (native is 0) | +0.009678 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8594 | 1.106 | +28.7% | +0.1678 to +0.325 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 733 | 592.3 | -19.2% | -169.2 to -112.2 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.762 | 8.904 | +1.6% | -0.16 to +0.4445 | no |
| pods started | 4.8 | 5 | +4.2% | -0.5388 to +0.9388 | no |
| pod start wait, total (s) | 11.6 | 15.5 | +33.6% | -1.468 to +9.268 | no |
| pod start wait, mean (s) | 2.353 | 2.997 | +27.3% | -0.1324 to +1.419 | no |
| host CPU busy, the real machine under kind (%) | 26.74 | 33.68 | +26.0% | +4.964 to +8.915 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*