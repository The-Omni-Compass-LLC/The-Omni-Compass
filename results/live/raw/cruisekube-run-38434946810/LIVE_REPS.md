# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.993 |
| node-hours | 1.488 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 162.5 | 162.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.9 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 82.7 | 82.84 |
| response time (ms), 95th percentile | 127.6 | 128.3 |
| response time (ms), 99th percentile | 147.2 | 147.1 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.08333 |
| utilisation (used / allocatable) | 0.04788 | 0.04786 |
| CPU used (cores), mean | 1.132 | 1.147 |
| Omni's own CPU (cores), mean | 0 | 0.00899 |
| CPU used with Omni's own (cores), mean | 1.132 | 1.156 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 575.1 | 567.6 |
| HPA replicas, mean | 2.659 | 2.708 |
| pods started | 1.4 | 1.6 |
| pod start wait, total (s) | 2 | 4.1 |
| pod start wait, mean (s) | 1.25 | 2.35 |
| host CPU busy, the real machine under kind (%) | 35.78 | 36.11 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.916 | 5.993 | +1.3% | -0.09708 to +0.2509 | no |
| node-hours | 1.488 | 1.519 | +2.1% | -0.0135 to +0.07461 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 162.5 | 162.2 | -0.2% | -3.575 to +2.968 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.9 | 162 | +0.7% | +0.8767 to +1.424 | yes, higher |
| response time (ms), mean | 82.7 | 82.84 | +0.2% | -2.088 to +2.361 | no |
| response time (ms), 95th percentile | 127.6 | 128.3 | +0.5% | -0.9344 to +2.253 | no |
| response time (ms), 99th percentile | 147.2 | 147.1 | -0.1% | -7.604 to +7.332 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.08333 | -21.9% | -0.1937 to +0.1471 | no |
| utilisation (used / allocatable) | 0.04788 | 0.04786 | -0.0% | -0.00107 to +0.001041 | no |
| CPU used (cores), mean | 1.132 | 1.147 | +1.3% | -0.03631 to +0.0668 | no |
| Omni's own CPU (cores), mean | 0 | 0.00899 | +0.00899 (native is 0) | +0.00786 to +0.01012 | yes, higher |
| CPU used with Omni's own (cores), mean | 1.132 | 1.156 | +2.1% | -0.02757 to +0.07603 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 575.1 | 567.6 | -1.3% | -31.94 to +17 | no |
| HPA replicas, mean | 2.659 | 2.708 | +1.8% | -0.09943 to +0.1964 | no |
| pods started | 1.4 | 1.6 | +14.3% | -0.3642 to +0.7642 | no |
| pod start wait, total (s) | 2 | 4.1 | +105.0% | -1.053 to +5.253 | no |
| pod start wait, mean (s) | 1.25 | 2.35 | +88.0% | -0.2676 to +2.468 | no |
| host CPU busy, the real machine under kind (%) | 35.78 | 36.11 | +0.9% | -0.1793 to +0.8313 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*