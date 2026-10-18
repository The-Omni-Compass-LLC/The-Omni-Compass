# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 156.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 156.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 184.1 | 185.9 |
| response time (ms), 95th percentile | 438.9 | 452.7 |
| response time (ms), 99th percentile | 610.9 | 609.7 |
| time over the response line (% of samples) | 4.003 | 4.254 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 4.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.3733 |
| utilisation (used / allocatable) | 0.03026 | 0.03066 |
| CPU used (cores), mean | 0.7264 | 0.7359 |
| Omni's own CPU (cores), mean | 0 | 0.00828 |
| CPU used with Omni's own (cores), mean | 0.7264 | 0.7441 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.3 | 851.9 |
| HPA replicas, mean | 2.836 | 2.878 |
| pods started | 2.8 | 3 |
| pod start wait, total (s) | 23.3 | 24.6 |
| pod start wait, mean (s) | 8.3 | 8.2 |
| host CPU busy, the real machine under kind (%) | 23.04 | 23.74 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.518 | 1.507 | -0.7% | -0.01732 to -0.004012 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 156.8 | -0.7% | -1.772 to -0.321 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 156.8 | -0.7% | -1.772 to -0.321 | yes: GAIN |
| response time (ms), mean | 184.1 | 185.9 | +1.0% | -6.514 to +10.24 | no |
| response time (ms), 95th percentile | 438.9 | 452.7 | +3.1% | -7.036 to +34.67 | no |
| response time (ms), 99th percentile | 610.9 | 609.7 | -0.2% | -29.39 to +27.02 | no |
| time over the response line (% of samples) | 4.003 | 4.254 | +6.3% | -0.3313 to +0.8329 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 4.2 | +5.0% | -0.6121 to +1.012 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 1 | +1 (native is 0) | +1 to +1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.345 | 0.3733 | +8.2% | -0.2482 to +0.3049 | no |
| utilisation (used / allocatable) | 0.03026 | 0.03066 | +1.3% | -0.0003315 to +0.001124 | no |
| CPU used (cores), mean | 0.7264 | 0.7359 | +1.3% | -0.007956 to +0.02697 | no |
| Omni's own CPU (cores), mean | 0 | 0.00828 | +0.00828 (native is 0) | +0.007153 to +0.009407 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7264 | 0.7441 | +2.4% | +0.0003829 to +0.03519 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.3 | 851.9 | -1.3% | -30.77 to +7.915 | no |
| HPA replicas, mean | 2.836 | 2.878 | +1.4% | -0.1377 to +0.2199 | no |
| pods started | 2.8 | 3 | +7.1% | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 23.3 | 24.6 | +5.6% | -4.231 to +6.831 | no |
| pod start wait, mean (s) | 8.3 | 8.2 | -1.2% | -1.507 to +1.307 | no |
| host CPU busy, the real machine under kind (%) | 23.04 | 23.74 | +3.0% | +0.2782 to +1.115 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*