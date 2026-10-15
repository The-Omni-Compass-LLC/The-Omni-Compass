# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.872 |
| node-hours | 1.513 | 1.479 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.7 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 159.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 68.11 | 68.87 |
| response time (ms), 95th percentile | 100.9 | 102.6 |
| response time (ms), 99th percentile | 112.6 | 119.4 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02833 | 0.215 |
| utilisation (used / allocatable) | 0.04511 | 0.0455 |
| CPU used (cores), mean | 1.083 | 1.061 |
| Omni's own CPU (cores), mean | 0 | 0.00828 |
| CPU used with Omni's own (cores), mean | 1.083 | 1.069 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 597.3 | 603.6 |
| HPA replicas, mean | 2.705 | 2.756 |
| pods started | 1.4 | 1.6 |
| pod start wait, total (s) | 3.6 | 5.2 |
| pod start wait, mean (s) | 2.05 | 2.617 |
| host CPU busy, the real machine under kind (%) | 33.36 | 33.73 |
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

Omni-Compass stayed native in 9 of 10 repetitions (repetitions 1, 2, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.872 | -2.1% | -0.4168 to +0.1613 | no |
| node-hours | 1.513 | 1.479 | -2.3% | -0.1104 to +0.04155 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.7 | 161.5 | +0.5% | -1.822 to +3.406 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 159.1 | -1.0% | -4.794 to +1.586 | no |
| response time (ms), mean | 68.11 | 68.87 | +1.1% | -0.3294 to +1.851 | no |
| response time (ms), 95th percentile | 100.9 | 102.6 | +1.7% | -0.321 to +3.762 | no |
| response time (ms), 99th percentile | 112.6 | 119.4 | +6.0% | -4.547 to +18.13 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02833 | 0.215 | +658.8% | -0.01297 to +0.3863 | no |
| utilisation (used / allocatable) | 0.04511 | 0.0455 | +0.9% | -0.001604 to +0.002387 | no |
| CPU used (cores), mean | 1.083 | 1.061 | -2.0% | -0.0525 to +0.009363 | no |
| Omni's own CPU (cores), mean | 0 | 0.00828 | +0.00828 (native is 0) | +0.006583 to +0.009977 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.083 | 1.069 | -1.2% | -0.04328 to +0.01671 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 597.3 | 603.6 | +1.1% | -5.993 to +18.71 | no |
| HPA replicas, mean | 2.705 | 2.756 | +1.9% | -0.1427 to +0.2438 | no |
| pods started | 1.4 | 1.6 | +14.3% | -0.6121 to +1.012 | no |
| pod start wait, total (s) | 3.6 | 5.2 | +44.4% | -3.207 to +6.407 | no |
| pod start wait, mean (s) | 2.05 | 2.617 | +27.6% | -1.412 to +2.546 | no |
| host CPU busy, the real machine under kind (%) | 33.36 | 33.73 | +1.1% | -0.5478 to +1.279 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*