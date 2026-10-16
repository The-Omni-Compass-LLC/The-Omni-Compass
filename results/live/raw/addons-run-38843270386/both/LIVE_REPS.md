# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 125.3 | 80.23 |
| response time (ms), 95th percentile | 259 | 121.1 |
| response time (ms), 99th percentile | 371.5 | 158.3 |
| time over the response line (% of samples) | 0.4117 | 0 |
| failed requests (%) | 0.0129 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3217 | 0.2717 |
| utilisation (used / allocatable) | 0.0368 | 0.04684 |
| CPU used (cores), mean | 0.8833 | 1.124 |
| Omni's own CPU (cores), mean | 0 | 0.01192 |
| CPU used with Omni's own (cores), mean | 0.8833 | 1.136 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 577.1 |
| HPA replicas, mean | 8.813 | 9.04 |
| pods started | 5.2 | 5 |
| pod start wait, total (s) | 15.7 | 14.7 |
| pod start wait, mean (s) | 2.937 | 2.818 |
| host CPU busy, the real machine under kind (%) | 27.58 | 35.01 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.13e-17 to +1.295e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.515 | -0.3% | -0.01218 to +0.003846 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 161 | +1.1% | +0.5545 to +2.987 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 161 | +1.1% | +0.5545 to +2.987 | yes: power given |
| response time (ms), mean | 125.3 | 80.23 | -36.0% | -58.37 to -31.73 | yes: GAIN |
| response time (ms), 95th percentile | 259 | 121.1 | -53.2% | -169.7 to -106 | yes: GAIN |
| response time (ms), 99th percentile | 371.5 | 158.3 | -57.4% | -258.4 to -168 | yes: GAIN |
| time over the response line (% of samples) | 0.4117 | 0 | -100.0% | -0.7133 to -0.11 | yes: GAIN |
| failed requests (%) | 0.0129 | 0 | -100.0% | -0.04209 to +0.01628 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | -100.0% | -0.7694 to -0.03062 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.4 (native is 0) | +16.38 to +18.42 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3217 | 0.2717 | -15.5% | -0.1981 to +0.09805 | no |
| utilisation (used / allocatable) | 0.0368 | 0.04684 | +27.3% | +0.006691 to +0.01337 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8833 | 1.124 | +27.3% | +0.1606 to +0.3209 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01192 | +0.0119 (native is 0) | +0.01044 to +0.0134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8833 | 1.136 | +28.6% | +0.1712 to +0.3342 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 577.1 | -19.1% | -170.7 to -102.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.813 | 9.04 | +2.6% | +0.0071 to +0.4464 | yes: power given |
| pods started | 5.2 | 5 | -3.8% | -0.8573 to +0.4573 | no |
| pod start wait, total (s) | 15.7 | 14.7 | -6.4% | -7.786 to +5.786 | no |
| pod start wait, mean (s) | 2.937 | 2.818 | -4.0% | -1.14 to +0.9027 | no |
| host CPU busy, the real machine under kind (%) | 27.58 | 35.01 | +26.9% | +5.124 to +9.726 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*