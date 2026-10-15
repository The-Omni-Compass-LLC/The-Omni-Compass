# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 138.7 | 76.47 |
| response time (ms), 95th percentile | 294.9 | 118.6 |
| response time (ms), 99th percentile | 437.8 | 135.3 |
| time over the response line (% of samples) | 0.8175 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 |
| utilisation (used / allocatable) | 0.03329 | 0.04681 |
| CPU used (cores), mean | 0.799 | 1.123 |
| Omni's own CPU (cores), mean | 0 | 0.00792 |
| CPU used with Omni's own (cores), mean | 0.799 | 1.131 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.3 | 576 |
| HPA replicas, mean | 9.77 | 9.799 |
| pods started | 1.9 | 1.1 |
| pod start wait, total (s) | 2.9 | 1.7 |
| pod start wait, mean (s) | 1.392 | 0.7333 |
| host CPU busy, the real machine under kind (%) | 24.22 | 33.24 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.514 | -0.2% | -0.01132 to +0.005989 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161 | +1.8% | +1.882 to +3.798 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161 | +1.8% | +1.882 to +3.798 | yes: power given |
| response time (ms), mean | 138.7 | 76.47 | -44.9% | -79.96 to -44.52 | yes: GAIN |
| response time (ms), 95th percentile | 294.9 | 118.6 | -59.8% | -211.2 to -141.5 | yes: GAIN |
| response time (ms), 99th percentile | 437.8 | 135.3 | -69.1% | -355.4 to -249.6 | yes: GAIN |
| time over the response line (% of samples) | 0.8175 | 0 | -100.0% | -1.391 to -0.2437 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | -100.0% | -2.012 to +0.0116 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.4 | +16.4 (native is 0) | +13.44 to +19.36 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | +33.3% | -0.03365 to +0.08699 | no |
| utilisation (used / allocatable) | 0.03329 | 0.04681 | +40.6% | +0.01057 to +0.01646 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.799 | 1.123 | +40.6% | +0.2536 to +0.395 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00792 | +0.00792 (native is 0) | +0.00717 to +0.00867 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.799 | 1.131 | +41.6% | +0.2609 to +0.4036 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.3 | 576 | -26.7% | -235.3 to -183.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.77 | 9.799 | +0.3% | -0.2021 to +0.2588 | no |
| pods started | 1.9 | 1.1 | -42.1% | -2.053 to +0.4526 | no |
| pod start wait, total (s) | 2.9 | 1.7 | -41.4% | -3.3 to +0.9004 | no |
| pod start wait, mean (s) | 1.392 | 0.7333 | -47.3% | -1.496 to +0.1792 | no |
| host CPU busy, the real machine under kind (%) | 24.22 | 33.24 | +37.3% | +7.187 to +10.86 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*