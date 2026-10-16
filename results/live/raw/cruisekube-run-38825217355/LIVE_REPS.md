# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.979 | 5.979 |
| node-hours | 1.504 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 162.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 65.91 | 88.3 |
| response time (ms), 95th percentile | 94.69 | 127.9 |
| response time (ms), 99th percentile | 108.1 | 151.9 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0.2 | 0 |
| time pods had no machine to take them, pod-minutes | 0.01667 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1567 | 0.1133 |
| utilisation (used / allocatable) | 0.04415 | 0.05044 |
| CPU used (cores), mean | 1.055 | 1.206 |
| Omni's own CPU (cores), mean | 0 | 0.00944 |
| CPU used with Omni's own (cores), mean | 1.055 | 1.215 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 614 | 534.1 |
| HPA replicas, mean | 2.697 | 2.771 |
| pods started | 2 | 1.4 |
| pod start wait, total (s) | 3.8 | 6.2 |
| pod start wait, mean (s) | 1.6 | 3.7 |
| host CPU busy, the real machine under kind (%) | 33.09 | 38.2 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

Omni-Compass stayed native in 1 of 1 repetitions (repetition 1): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.894 | 6 | +1.8% | +nan to +nan | no |
| node-hours | 1.48 | 1.525 | +3.0% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 163.8 | -0.1% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162 | 163.8 | +1.1% | +nan to +nan | no |
| response time (ms), mean | 101.9 | 100.9 | -1.0% | +nan to +nan | no |
| response time (ms), 95th percentile | 141.3 | 141.8 | +0.4% | +nan to +nan | no |
| response time (ms), 99th percentile | 159.5 | 170.1 | +6.6% | +nan to +nan | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 1 | 0 | -100.0% | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0.08333 | 0 | -100.0% | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0 | -100.0% | +nan to +nan | no |
| utilisation (used / allocatable) | 0.05485 | 0.05396 | -1.6% | +nan to +nan | no |
| CPU used (cores), mean | 1.293 | 1.295 | +0.2% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0098 | +0.0098 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 1.293 | 1.305 | +0.9% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.8 | 497.6 | -0.3% | +nan to +nan | no |
| HPA replicas, mean | 2.913 | 2.543 | -12.7% | +nan to +nan | no |
| pods started | 1 | 1 | +0.0% | +nan to +nan | no |
| pod start wait, total (s) | 1 | 2 | +100.0% | +nan to +nan | no |
| pod start wait, mean (s) | 1 | 2 | +100.0% | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 40.97 | 40.79 | -0.4% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*