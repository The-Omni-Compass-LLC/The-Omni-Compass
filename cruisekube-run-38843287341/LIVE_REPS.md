# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 6 |
| node-hours | 1.502 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.3 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 161.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 76.54 | 76.59 |
| response time (ms), 95th percentile | 120.7 | 120.6 |
| response time (ms), 99th percentile | 139.2 | 139.3 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1933 | 0.08167 |
| utilisation (used / allocatable) | 0.04681 | 0.04647 |
| CPU used (cores), mean | 1.117 | 1.115 |
| Omni's own CPU (cores), mean | 0 | 0.00853 |
| CPU used with Omni's own (cores), mean | 1.117 | 1.124 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 582.8 | 584.2 |
| HPA replicas, mean | 2.796 | 2.817 |
| pods started | 1.6 | 1.3 |
| pod start wait, total (s) | 6 | 5.5 |
| pod start wait, mean (s) | 2.967 | 3.7 |
| host CPU busy, the real machine under kind (%) | 34.92 | 35 |
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
| worker nodes in service, mean | 5.969 | 6 | +0.5% | -0.03907 to +0.101 | no |
| node-hours | 1.502 | 1.518 | +1.0% | +0.002946 to +0.02705 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 161.3 | 161.4 | +0.1% | -1.948 to +2.147 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 161.4 | +0.4% | -0.08574 to +1.459 | no |
| response time (ms), mean | 76.54 | 76.59 | +0.1% | -1.204 to +1.293 | no |
| response time (ms), 95th percentile | 120.7 | 120.6 | -0.1% | -2.814 to +2.663 | no |
| response time (ms), 99th percentile | 139.2 | 139.3 | +0.0% | -5.762 to +5.821 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1933 | 0.08167 | -57.8% | -0.3444 to +0.1211 | no |
| utilisation (used / allocatable) | 0.04681 | 0.04647 | -0.7% | -0.001076 to +0.0003862 | no |
| CPU used (cores), mean | 1.117 | 1.115 | -0.1% | -0.01965 to +0.01635 | no |
| Omni's own CPU (cores), mean | 0 | 0.00853 | +0.00853 (native is 0) | +0.007232 to +0.009828 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.117 | 1.124 | +0.6% | -0.01156 to +0.02532 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 582.8 | 584.2 | +0.3% | -6.065 to +8.983 | no |
| HPA replicas, mean | 2.796 | 2.817 | +0.7% | -0.1811 to +0.2222 | no |
| pods started | 1.6 | 1.3 | -18.8% | -1.058 to +0.4578 | no |
| pod start wait, total (s) | 6 | 5.5 | -8.3% | -5.295 to +4.295 | no |
| pod start wait, mean (s) | 2.967 | 3.7 | +24.7% | -2.035 to +3.502 | no |
| host CPU busy, the real machine under kind (%) | 34.92 | 35 | +0.2% | -0.474 to +0.6247 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*