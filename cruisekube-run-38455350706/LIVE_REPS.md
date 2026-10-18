# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.989 | 6 |
| node-hours | 1.513 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 162.1 | 162.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.9 | 162.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 84.57 | 85.2 |
| response time (ms), 95th percentile | 131.1 | 130.4 |
| response time (ms), 99th percentile | 152.1 | 147.1 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.14 |
| utilisation (used / allocatable) | 0.04974 | 0.0496 |
| CPU used (cores), mean | 1.191 | 1.19 |
| Omni's own CPU (cores), mean | 0 | 0.00927 |
| CPU used with Omni's own (cores), mean | 1.191 | 1.2 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.8 | 541.9 |
| HPA replicas, mean | 2.834 | 2.833 |
| pods started | 1.4 | 0.9 |
| pod start wait, total (s) | 5.9 | 3.1 |
| pod start wait, mean (s) | 3.1 | 1.95 |
| host CPU busy, the real machine under kind (%) | 36.64 | 37.21 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.989 | 6 | +0.2% | -0.01336 to +0.03453 | no |
| node-hours | 1.513 | 1.519 | +0.4% | -0.006324 to +0.01766 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 162.1 | 162.2 | +0.1% | -0.8357 to +1.021 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.9 | 162.2 | +0.2% | -0.6876 to +1.273 | no |
| response time (ms), mean | 84.57 | 85.2 | +0.7% | -0.5863 to +1.844 | no |
| response time (ms), 95th percentile | 131.1 | 130.4 | -0.6% | -2.835 to +1.387 | no |
| response time (ms), 99th percentile | 152.1 | 147.1 | -3.3% | -11.8 to +1.799 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.14 | -26.3% | -0.2289 to +0.1289 | no |
| utilisation (used / allocatable) | 0.04974 | 0.0496 | -0.3% | -0.001086 to +0.0008147 | no |
| CPU used (cores), mean | 1.191 | 1.19 | -0.1% | -0.02509 to +0.02303 | no |
| Omni's own CPU (cores), mean | 0 | 0.00927 | +0.00927 (native is 0) | +0.008368 to +0.01017 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.191 | 1.2 | +0.7% | -0.01607 to +0.03255 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 540.8 | 541.9 | +0.2% | -8.875 to +11.11 | no |
| HPA replicas, mean | 2.834 | 2.833 | -0.0% | -0.1683 to +0.1662 | no |
| pods started | 1.4 | 0.9 | -35.7% | -1.108 to +0.1079 | no |
| pod start wait, total (s) | 5.9 | 3.1 | -47.5% | -7.53 to +1.93 | no |
| pod start wait, mean (s) | 3.1 | 1.95 | -37.1% | -3.462 to +1.162 | no |
| host CPU busy, the real machine under kind (%) | 36.64 | 37.21 | +1.6% | +0.05299 to +1.09 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*