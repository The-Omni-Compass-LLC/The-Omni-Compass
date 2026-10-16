# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.959 |
| node-hours | 1.512 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.4 | 163.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.4 | 162.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 87.3 | 87.96 |
| response time (ms), 95th percentile | 139.1 | 138.9 |
| response time (ms), 99th percentile | 159.3 | 159.1 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.135 | 0.02667 |
| utilisation (used / allocatable) | 0.04977 | 0.05032 |
| CPU used (cores), mean | 1.195 | 1.199 |
| Omni's own CPU (cores), mean | 0 | 0.00964 |
| CPU used with Omni's own (cores), mean | 1.195 | 1.209 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.8 | 539.6 |
| HPA replicas, mean | 2.768 | 2.82 |
| pods started | 1.3 | 1.2 |
| pod start wait, total (s) | 4.4 | 3.7 |
| pod start wait, mean (s) | 2.85 | 2.45 |
| host CPU busy, the real machine under kind (%) | 37.07 | 37.64 |
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
| worker nodes in service, mean | 6 | 5.959 | -0.7% | -0.1349 to +0.05219 | no |
| node-hours | 1.512 | 1.51 | -0.1% | -0.02452 to +0.02186 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.4 | 163.3 | +1.2% | -0.1897 to +3.912 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.4 | 162.5 | +0.7% | +0.3256 to +1.822 | yes: power given |
| response time (ms), mean | 87.3 | 87.96 | +0.8% | -0.8384 to +2.164 | no |
| response time (ms), 95th percentile | 139.1 | 138.9 | -0.1% | -2.422 to +2.056 | no |
| response time (ms), 99th percentile | 159.3 | 159.1 | -0.1% | -7.445 to +7.161 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.135 | 0.02667 | -80.2% | -0.2059 to -0.01079 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04977 | 0.05032 | +1.1% | -0.0002307 to +0.001318 | no |
| CPU used (cores), mean | 1.195 | 1.199 | +0.4% | -0.01337 to +0.02192 | no |
| Omni's own CPU (cores), mean | 0 | 0.00964 | +0.00964 (native is 0) | +0.008849 to +0.01043 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.195 | 1.209 | +1.2% | -0.003985 to +0.03181 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.8 | 539.6 | -0.2% | -8.329 to +5.988 | no |
| HPA replicas, mean | 2.768 | 2.82 | +1.9% | -0.1847 to +0.2891 | no |
| pods started | 1.3 | 1.2 | -7.7% | -0.506 to +0.306 | no |
| pod start wait, total (s) | 4.4 | 3.7 | -15.9% | -4.775 to +3.375 | no |
| pod start wait, mean (s) | 2.85 | 2.45 | -14.0% | -2.343 to +1.543 | no |
| host CPU busy, the real machine under kind (%) | 37.07 | 37.64 | +1.6% | +0.1795 to +0.9705 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*