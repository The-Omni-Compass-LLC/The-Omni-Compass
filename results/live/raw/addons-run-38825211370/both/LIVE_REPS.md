# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 142.6 | 140.5 |
| response time (ms), 95th percentile | 292.9 | 285 |
| response time (ms), 99th percentile | 415.2 | 414.6 |
| time over the response line (% of samples) | 0.4621 | 0.4348 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 3.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.5767 |
| utilisation (used / allocatable) | 0.03732 | 0.03809 |
| CPU used (cores), mean | 0.8956 | 0.9141 |
| Omni's own CPU (cores), mean | 0 | 0.01061 |
| CPU used with Omni's own (cores), mean | 0.8956 | 0.9247 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.1 | 690.3 |
| HPA replicas, mean | 8.895 | 10.44 |
| pods started | 4.9 | 8.3 |
| pod start wait, total (s) | 13.5 | 19.2 |
| pod start wait, mean (s) | 2.643 | 2.307 |
| host CPU busy, the real machine under kind (%) | 27.59 | 28.67 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.066e-16 to +9.395e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.514 | -0.2% | -0.01161 to +0.005272 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159 | -0.1% | -0.9545 to +0.6333 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159 | -0.1% | -0.9545 to +0.6333 | no |
| response time (ms), mean | 142.6 | 140.5 | -1.5% | -5.177 to +0.873 | no |
| response time (ms), 95th percentile | 292.9 | 285 | -2.7% | -17.58 to +1.731 | no |
| response time (ms), 99th percentile | 415.2 | 414.6 | -0.1% | -25.71 to +24.55 | no |
| time over the response line (% of samples) | 0.4621 | 0.4348 | -5.9% | -0.2938 to +0.2391 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 3.2 | +3.2 (native is 0) | +1.818 to +4.582 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2367 | 0.5767 | +143.7% | -0.07429 to +0.7543 | no |
| utilisation (used / allocatable) | 0.03732 | 0.03809 | +2.1% | +0.0001633 to +0.001379 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8956 | 0.9141 | +2.1% | +0.003919 to +0.03309 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01061 | +0.0106 (native is 0) | +0.009683 to +0.01154 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8956 | 0.9247 | +3.3% | +0.0139 to +0.04433 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 703.1 | 690.3 | -1.8% | -23.38 to -2.167 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.895 | 10.44 | +17.3% | +0.929 to +2.157 | yes: power given |
| pods started | 4.9 | 8.3 | +69.4% | +1.641 to +5.159 | yes: power given |
| pod start wait, total (s) | 13.5 | 19.2 | +42.2% | -2.266 to +13.67 | no |
| pod start wait, mean (s) | 2.643 | 2.307 | -12.7% | -1.254 to +0.5819 | no |
| host CPU busy, the real machine under kind (%) | 27.59 | 28.67 | +3.9% | +0.598 to +1.572 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*