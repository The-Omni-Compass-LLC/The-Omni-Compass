# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.9 | 162.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.9 | 162.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 86.67 | 87.96 |
| response time (ms), 95th percentile | 136.3 | 136.7 |
| response time (ms), 99th percentile | 152 | 156.8 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.08167 |
| utilisation (used / allocatable) | 0.05006 | 0.05049 |
| CPU used (cores), mean | 1.201 | 1.212 |
| Omni's own CPU (cores), mean | 0 | 0.00953 |
| CPU used with Omni's own (cores), mean | 1.201 | 1.221 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 535.8 | 531.9 |
| HPA replicas, mean | 2.756 | 2.844 |
| pods started | 1.1 | 1.6 |
| pod start wait, total (s) | 3.4 | 7.4 |
| pod start wait, mean (s) | 1.917 | 4.233 |
| host CPU busy, the real machine under kind (%) | 36.92 | 37.67 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.104e-16 to +7.88e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.518 | +0.2% | -0.007046 to +0.01271 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.9 | 162.3 | +0.2% | -0.7261 to +1.466 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.9 | 162.3 | +0.2% | -0.7261 to +1.466 | no |
| response time (ms), mean | 86.67 | 87.96 | +1.5% | -0.1334 to +2.699 | no |
| response time (ms), 95th percentile | 136.3 | 136.7 | +0.3% | -1.553 to +2.392 | no |
| response time (ms), 99th percentile | 152 | 156.8 | +3.1% | +0.8937 to +8.652 | yes: LOSS |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.08167 | +2.1% | -0.1256 to +0.1289 | no |
| utilisation (used / allocatable) | 0.05006 | 0.05049 | +0.9% | -0.0002787 to +0.001134 | no |
| CPU used (cores), mean | 1.201 | 1.212 | +0.9% | -0.006688 to +0.02722 | no |
| Omni's own CPU (cores), mean | 0 | 0.00953 | +0.00953 (native is 0) | +0.008894 to +0.01017 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.201 | 1.221 | +1.6% | +0.002641 to +0.03695 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 535.8 | 531.9 | -0.7% | -10.7 to +2.95 | no |
| HPA replicas, mean | 2.756 | 2.844 | +3.2% | -0.2505 to +0.4275 | no |
| pods started | 1.1 | 1.6 | +45.5% | -0.4079 to +1.408 | no |
| pod start wait, total (s) | 3.4 | 7.4 | +117.6% | -2.853 to +10.85 | no |
| pod start wait, mean (s) | 1.917 | 4.233 | +120.9% | -0.7178 to +5.351 | no |
| host CPU busy, the real machine under kind (%) | 36.92 | 37.67 | +2.0% | +0.2931 to +1.212 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*