# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.5 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 161.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 80.05 | 78.74 |
| response time (ms), 95th percentile | 120.7 | 118.4 |
| response time (ms), 99th percentile | 138.5 | 133.2 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1367 |
| utilisation (used / allocatable) | 0.04837 | 0.04818 |
| CPU used (cores), mean | 1.161 | 1.156 |
| Omni's own CPU (cores), mean | 0 | 0.00848 |
| CPU used with Omni's own (cores), mean | 1.161 | 1.165 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.1 | 559.7 |
| HPA replicas, mean | 2.701 | 2.624 |
| pods started | 1.3 | 1.2 |
| pod start wait, total (s) | 3.3 | 3.8 |
| pod start wait, mean (s) | 1.967 | 2.283 |
| host CPU busy, the real machine under kind (%) | 35.78 | 35.97 |
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

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.805e-16 to +8.91e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.512 | -0.1% | -0.01145 to +0.00712 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.5 | 161.2 | -0.2% | -1.157 to +0.6366 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 161.2 | -0.2% | -1.157 to +0.6366 | no |
| response time (ms), mean | 80.05 | 78.74 | -1.6% | -2.885 to +0.2549 | no |
| response time (ms), 95th percentile | 120.7 | 118.4 | -1.9% | -4.753 to +0.2101 | no |
| response time (ms), 99th percentile | 138.5 | 133.2 | -3.8% | -13.66 to +3.095 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1367 | +70.8% | -0.121 to +0.2343 | no |
| utilisation (used / allocatable) | 0.04837 | 0.04818 | -0.4% | -0.001184 to +0.000802 | no |
| CPU used (cores), mean | 1.161 | 1.156 | -0.4% | -0.02842 to +0.01925 | no |
| Omni's own CPU (cores), mean | 0 | 0.00848 | +0.00848 (native is 0) | +0.007386 to +0.009574 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.161 | 1.165 | +0.3% | -0.02001 to +0.0278 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 556.1 | 559.7 | +0.6% | -9.607 to +16.75 | no |
| HPA replicas, mean | 2.701 | 2.624 | -2.8% | -0.2658 to +0.1119 | no |
| pods started | 1.3 | 1.2 | -7.7% | -1.02 to +0.8204 | no |
| pod start wait, total (s) | 3.3 | 3.8 | +15.2% | -5.002 to +6.002 | no |
| pod start wait, mean (s) | 1.967 | 2.283 | +16.1% | -1.866 to +2.499 | no |
| host CPU busy, the real machine under kind (%) | 35.78 | 35.97 | +0.5% | -0.4814 to +0.8659 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*