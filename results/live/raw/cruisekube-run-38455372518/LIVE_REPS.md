# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.951 | 6 |
| node-hours | 1.503 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 162.2 | 161.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.3 | 161.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 75.77 | 75.93 |
| response time (ms), 95th percentile | 112.5 | 115 |
| response time (ms), 99th percentile | 129 | 137 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2433 | 0.16 |
| utilisation (used / allocatable) | 0.04689 | 0.04652 |
| CPU used (cores), mean | 1.115 | 1.116 |
| Omni's own CPU (cores), mean | 0 | 0.00811 |
| CPU used with Omni's own (cores), mean | 1.115 | 1.125 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 583 | 582 |
| HPA replicas, mean | 2.733 | 2.799 |
| pods started | 1.6 | 1.6 |
| pod start wait, total (s) | 6.1 | 6.2 |
| pod start wait, mean (s) | 3.117 | 3.75 |
| host CPU busy, the real machine under kind (%) | 34.64 | 34.92 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.951 | 6 | +0.8% | -0.0615 to +0.159 | no |
| node-hours | 1.503 | 1.515 | +0.8% | -0.02006 to +0.044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 162.2 | 161.2 | -0.6% | -3.206 to +1.183 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.3 | 161.2 | -0.1% | -1.226 to +1.049 | no |
| response time (ms), mean | 75.77 | 75.93 | +0.2% | -1.916 to +2.237 | no |
| response time (ms), 95th percentile | 112.5 | 115 | +2.2% | -1.918 to +6.899 | no |
| response time (ms), 99th percentile | 129 | 137 | +6.2% | -4.554 to +20.56 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2433 | 0.16 | -34.2% | -0.2897 to +0.123 | no |
| utilisation (used / allocatable) | 0.04689 | 0.04652 | -0.8% | -0.001489 to +0.0007515 | no |
| CPU used (cores), mean | 1.115 | 1.116 | +0.2% | -0.02743 to +0.03103 | no |
| Omni's own CPU (cores), mean | 0 | 0.00811 | +0.00811 (native is 0) | +0.006992 to +0.009228 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.115 | 1.125 | +0.9% | -0.01948 to +0.0393 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 583 | 582 | -0.2% | -16.01 to +14.12 | no |
| HPA replicas, mean | 2.733 | 2.799 | +2.4% | -0.1923 to +0.3249 | no |
| pods started | 1.6 | 1.6 | +0.0% | -0.826 to +0.826 | no |
| pod start wait, total (s) | 6.1 | 6.2 | +1.6% | -5.676 to +5.876 | no |
| pod start wait, mean (s) | 3.117 | 3.75 | +20.3% | -1.782 to +3.048 | no |
| host CPU busy, the real machine under kind (%) | 34.64 | 34.92 | +0.8% | -0.3821 to +0.9421 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*