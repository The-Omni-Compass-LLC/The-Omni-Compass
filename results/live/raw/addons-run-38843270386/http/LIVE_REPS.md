# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 212.3 | 90.27 |
| response time (ms), 95th percentile | 491.7 | 134.7 |
| response time (ms), 99th percentile | 667.4 | 295.8 |
| time over the response line (% of samples) | 5.477 | 0.2556 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.2983 |
| utilisation (used / allocatable) | 0.03167 | 0.04933 |
| CPU used (cores), mean | 0.76 | 1.184 |
| Omni's own CPU (cores), mean | 0 | 0.00969 |
| CPU used with Omni's own (cores), mean | 0.76 | 1.194 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.1 | 547 |
| HPA replicas, mean | 2.975 | 2.517 |
| pods started | 3 | 2.3 |
| pod start wait, total (s) | 27.8 | 22.3 |
| pod start wait, mean (s) | 9.267 | 9.783 |
| host CPU busy, the real machine under kind (%) | 24.14 | 36.05 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.605e-16 to +1.926e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.512 | -0.3% | -0.01061 to +0.001606 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 161.5 | +2.3% | +2.623 to +4.536 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 161.5 | +2.3% | +2.623 to +4.536 | yes: power given |
| response time (ms), mean | 212.3 | 90.27 | -57.5% | -141.6 to -102.5 | yes: GAIN |
| response time (ms), 95th percentile | 491.7 | 134.7 | -72.6% | -409.7 to -304.2 | yes: GAIN |
| response time (ms), 99th percentile | 667.4 | 295.8 | -55.7% | -417.7 to -325.4 | yes: GAIN |
| time over the response line (% of samples) | 5.477 | 0.2556 | -95.3% | -7.384 to -3.058 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.4 | 0.2 | -96.3% | -7.406 to -2.994 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 | +4.3 (native is 0) | +3.954 to +4.646 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.2983 | -37.8% | -0.3643 to +0.001 | no |
| utilisation (used / allocatable) | 0.03167 | 0.04933 | +55.8% | +0.01495 to +0.02037 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.76 | 1.184 | +55.8% | +0.3589 to +0.4888 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00969 | +0.00969 (native is 0) | +0.008708 to +0.01067 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.76 | 1.194 | +57.0% | +0.3678 to +0.4993 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 824.1 | 547 | -33.6% | -296.8 to -257.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.975 | 2.517 | -15.4% | -0.5723 to -0.3437 | yes: GAIN |
| pods started | 3 | 2.3 | -23.3% | -1.046 to -0.3545 | yes: GAIN |
| pod start wait, total (s) | 27.8 | 22.3 | -19.8% | -8.791 to -2.209 | yes: GAIN |
| pod start wait, mean (s) | 9.267 | 9.783 | +5.6% | -0.04939 to +1.083 | no |
| host CPU busy, the real machine under kind (%) | 24.14 | 36.05 | +49.4% | +10.25 to +13.58 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*