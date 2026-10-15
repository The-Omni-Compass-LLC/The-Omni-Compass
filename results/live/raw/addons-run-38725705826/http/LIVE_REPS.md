# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 160.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 160.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 181.9 | 73.63 |
| response time (ms), 95th percentile | 455.4 | 114.6 |
| response time (ms), 99th percentile | 608.7 | 158.2 |
| time over the response line (% of samples) | 4.071 | 0.03615 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.4117 |
| utilisation (used / allocatable) | 0.02982 | 0.04545 |
| CPU used (cores), mean | 0.7156 | 1.091 |
| Omni's own CPU (cores), mean | 0 | 0.00886 |
| CPU used with Omni's own (cores), mean | 0.7156 | 1.1 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 877.5 | 595.7 |
| HPA replicas, mean | 2.722 | 2.419 |
| pods started | 2.6 | 2.3 |
| pod start wait, total (s) | 20.9 | 22.8 |
| pod start wait, mean (s) | 7.867 | 9.65 |
| host CPU busy, the real machine under kind (%) | 22.82 | 33.68 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | no |
| node-hours | 1.52 | 1.511 | -0.6% | -0.01271 to -0.005952 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 160.5 | +1.6% | +1.543 to +3.635 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 160.5 | +1.6% | +1.543 to +3.635 | yes: power given |
| response time (ms), mean | 181.9 | 73.63 | -59.5% | -135.1 to -81.49 | yes: GAIN |
| response time (ms), 95th percentile | 455.4 | 114.6 | -74.8% | -419.8 to -261.8 | yes: GAIN |
| response time (ms), 99th percentile | 608.7 | 158.2 | -74.0% | -553.3 to -347.7 | yes: GAIN |
| time over the response line (% of samples) | 4.071 | 0.03615 | -99.1% | -6.981 to -1.088 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.5 | 0 | -100.0% | -5.89 to -1.11 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.7 | +4.7 (native is 0) | +3.579 to +5.821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.4117 | +11.8% | -0.1225 to +0.2092 | no |
| utilisation (used / allocatable) | 0.02982 | 0.04545 | +52.5% | +0.01239 to +0.01888 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7156 | 1.091 | +52.5% | +0.2974 to +0.4532 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00886 | +0.00886 (native is 0) | +0.007459 to +0.01026 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7156 | 1.1 | +53.7% | +0.305 to +0.4634 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 877.5 | 595.7 | -32.1% | -308.6 to -255.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.722 | 2.419 | -11.1% | -0.4729 to -0.1318 | yes: GAIN |
| pods started | 2.6 | 2.3 | -11.5% | -0.6455 to +0.04553 | no |
| pod start wait, total (s) | 20.9 | 22.8 | +9.1% | -2.957 to +6.757 | no |
| pod start wait, mean (s) | 7.867 | 9.65 | +22.7% | +0.622 to +2.945 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 22.82 | 33.68 | +47.6% | +8.755 to +12.97 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*