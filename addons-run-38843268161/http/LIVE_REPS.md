# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 206.7 | 88.16 |
| response time (ms), 95th percentile | 470.9 | 135.7 |
| response time (ms), 99th percentile | 659.8 | 285.1 |
| time over the response line (% of samples) | 4.698 | 0.2432 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4517 | 0.3283 |
| utilisation (used / allocatable) | 0.03143 | 0.04805 |
| CPU used (cores), mean | 0.7544 | 1.153 |
| Omni's own CPU (cores), mean | 0 | 0.00962 |
| CPU used with Omni's own (cores), mean | 0.7544 | 1.163 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 831.4 | 560.6 |
| HPA replicas, mean | 2.994 | 2.439 |
| pods started | 3 | 2.4 |
| pod start wait, total (s) | 28.2 | 23.5 |
| pod start wait, mean (s) | 9.4 | 9.717 |
| host CPU busy, the real machine under kind (%) | 23.81 | 35.52 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.733e-16 to +1.062e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.515 | -0.2% | -0.009899 to +0.004232 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.6 | +2.2% | +2.59 to +4.445 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.6 | +2.2% | +2.59 to +4.445 | yes: power given |
| response time (ms), mean | 206.7 | 88.16 | -57.3% | -136.6 to -100.4 | yes: GAIN |
| response time (ms), 95th percentile | 470.9 | 135.7 | -71.2% | -376.2 to -294.3 | yes: GAIN |
| response time (ms), 99th percentile | 659.8 | 285.1 | -56.8% | -434.5 to -314.9 | yes: GAIN |
| time over the response line (% of samples) | 4.698 | 0.2432 | -94.8% | -6.187 to -2.722 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 0.3 | -94.0% | -6.639 to -2.761 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.4 | +4.4 (native is 0) | +4.031 to +4.769 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4517 | 0.3283 | -27.3% | -0.3562 to +0.1095 | no |
| utilisation (used / allocatable) | 0.03143 | 0.04805 | +52.8% | +0.01446 to +0.01876 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7544 | 1.153 | +52.8% | +0.347 to +0.4503 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00962 | +0.00962 (native is 0) | +0.008465 to +0.01078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7544 | 1.163 | +54.1% | +0.3556 to +0.4609 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 831.4 | 560.6 | -32.6% | -279.9 to -261.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.994 | 2.439 | -18.6% | -0.7278 to -0.3832 | yes: GAIN |
| pods started | 3 | 2.4 | -20.0% | -0.9694 to -0.2306 | yes: GAIN |
| pod start wait, total (s) | 28.2 | 23.5 | -16.7% | -12.09 to +2.688 | no |
| pod start wait, mean (s) | 9.4 | 9.717 | +3.4% | -2.336 to +2.97 | no |
| host CPU busy, the real machine under kind (%) | 23.81 | 35.52 | +49.2% | +10.19 to +13.24 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*