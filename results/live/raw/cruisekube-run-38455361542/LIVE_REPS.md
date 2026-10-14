# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.958 | 6 |
| node-hours | 1.499 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.8 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 82.97 | 83.11 |
| response time (ms), 95th percentile | 127.7 | 126.5 |
| response time (ms), 99th percentile | 146.3 | 143.4 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.055 |
| utilisation (used / allocatable) | 0.04879 | 0.04862 |
| CPU used (cores), mean | 1.163 | 1.167 |
| Omni's own CPU (cores), mean | 0 | 0.00884 |
| CPU used with Omni's own (cores), mean | 1.163 | 1.176 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 558.1 | 556.2 |
| HPA replicas, mean | 2.711 | 2.697 |
| pods started | 1.5 | 1 |
| pod start wait, total (s) | 3.9 | 3.3 |
| pod start wait, mean (s) | 2.083 | 2 |
| host CPU busy, the real machine under kind (%) | 36.1 | 36.55 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.958 | 6 | +0.7% | -0.05295 to +0.1369 | no |
| node-hours | 1.499 | 1.517 | +1.2% | -0.008235 to +0.04357 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.8 | 161.8 | -0.0% | -1.833 to +1.759 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161 | 161.8 | +0.5% | +0.02502 to +1.475 | yes: power given |
| response time (ms), mean | 82.97 | 83.11 | +0.2% | -0.971 to +1.243 | no |
| response time (ms), 95th percentile | 127.7 | 126.5 | -1.0% | -4.076 to +1.617 | no |
| response time (ms), 99th percentile | 146.3 | 143.4 | -2.0% | -12.74 to +6.88 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.055 | -65.6% | -0.3118 to +0.1018 | no |
| utilisation (used / allocatable) | 0.04879 | 0.04862 | -0.4% | -0.0007369 to +0.0003925 | no |
| CPU used (cores), mean | 1.163 | 1.167 | +0.3% | -0.02012 to +0.02796 | no |
| Omni's own CPU (cores), mean | 0 | 0.00884 | +0.00884 (native is 0) | +0.007724 to +0.009956 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.163 | 1.176 | +1.1% | -0.01111 to +0.03662 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 558.1 | 556.2 | -0.3% | -13.77 to +10.11 | no |
| HPA replicas, mean | 2.711 | 2.697 | -0.5% | -0.2055 to +0.178 | no |
| pods started | 1.5 | 1 | -33.3% | -1.108 to +0.1079 | no |
| pod start wait, total (s) | 3.9 | 3.3 | -15.4% | -4.691 to +3.491 | no |
| pod start wait, mean (s) | 2.083 | 2 | -4.0% | -2.051 to +1.885 | no |
| host CPU busy, the real machine under kind (%) | 36.1 | 36.55 | +1.2% | +0.08145 to +0.8159 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*