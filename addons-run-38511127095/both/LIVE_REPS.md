# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 134.4 | 82.64 |
| response time (ms), 95th percentile | 281.8 | 124.2 |
| response time (ms), 99th percentile | 404.8 | 154.5 |
| time over the response line (% of samples) | 0.4868 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.24 |
| utilisation (used / allocatable) | 0.03695 | 0.04855 |
| CPU used (cores), mean | 0.8867 | 1.165 |
| Omni's own CPU (cores), mean | 0 | 0.01205 |
| CPU used with Omni's own (cores), mean | 0.8867 | 1.177 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711 | 555.3 |
| HPA replicas, mean | 8.852 | 9.072 |
| pods started | 5.1 | 4.7 |
| pod start wait, total (s) | 15 | 12.3 |
| pod start wait, mean (s) | 2.88 | 2.535 |
| host CPU busy, the real machine under kind (%) | 27.42 | 35.81 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.033e-16 to +9.586e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.513 | -0.3% | -0.01177 to +0.003105 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.3 | +1.4% | +1.193 to +3.12 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.3 | +1.4% | +1.193 to +3.12 | yes: power given |
| response time (ms), mean | 134.4 | 82.64 | -38.5% | -65.25 to -38.33 | yes: GAIN |
| response time (ms), 95th percentile | 281.8 | 124.2 | -55.9% | -184.2 to -131.1 | yes: GAIN |
| response time (ms), 99th percentile | 404.8 | 154.5 | -61.8% | -296.4 to -204.2 | yes: GAIN |
| time over the response line (% of samples) | 0.4868 | 0 | -100.0% | -0.8158 to -0.1579 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | -100.0% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.7 | +17.7 (native is 0) | +16.8 to +18.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2933 | 0.24 | -18.2% | -0.4307 to +0.3241 | no |
| utilisation (used / allocatable) | 0.03695 | 0.04855 | +31.4% | +0.008874 to +0.01433 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8867 | 1.165 | +31.4% | +0.213 to +0.344 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01205 | +0.0121 (native is 0) | +0.01073 to +0.01337 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8867 | 1.177 | +32.8% | +0.2241 to +0.3569 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 711 | 555.3 | -21.9% | -180.7 to -130.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.852 | 9.072 | +2.5% | +0.06336 to +0.3763 | yes: power given |
| pods started | 5.1 | 4.7 | -7.8% | -1.169 to +0.3689 | no |
| pod start wait, total (s) | 15 | 12.3 | -18.0% | -7.826 to +2.426 | no |
| pod start wait, mean (s) | 2.88 | 2.535 | -12.0% | -1.091 to +0.4015 | no |
| host CPU busy, the real machine under kind (%) | 27.42 | 35.81 | +30.6% | +6.653 to +10.13 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*