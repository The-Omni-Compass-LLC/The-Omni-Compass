# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 136.2 | 74.88 |
| response time (ms), 95th percentile | 291.9 | 116.4 |
| response time (ms), 99th percentile | 427.2 | 140.9 |
| time over the response line (% of samples) | 0.7163 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.135 |
| utilisation (used / allocatable) | 0.03282 | 0.04629 |
| CPU used (cores), mean | 0.7878 | 1.111 |
| Omni's own CPU (cores), mean | 0 | 0.00796 |
| CPU used with Omni's own (cores), mean | 0.7878 | 1.119 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 797.5 | 584.1 |
| HPA replicas, mean | 9.737 | 9.797 |
| pods started | 2.2 | 1.6 |
| pod start wait, total (s) | 2.9 | 2.6 |
| pod start wait, mean (s) | 0.9083 | 1.3 |
| host CPU busy, the real machine under kind (%) | 23.73 | 32.76 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.513 | -0.3% | -0.01303 to +0.004359 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 160.7 | +1.6% | +1.793 to +3.396 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 160.7 | +1.6% | +1.793 to +3.396 | yes: power given |
| response time (ms), mean | 136.2 | 74.88 | -45.0% | -79.46 to -43.27 | yes: GAIN |
| response time (ms), 95th percentile | 291.9 | 116.4 | -60.1% | -212.8 to -138.1 | yes: GAIN |
| response time (ms), 99th percentile | 427.2 | 140.9 | -67.0% | -335.2 to -237.3 | yes: GAIN |
| time over the response line (% of samples) | 0.7163 | 0 | -100.0% | -1.255 to -0.1775 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | -100.0% | -2.066 to +0.06632 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.8 | +17.8 (native is 0) | +15.4 to +20.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.135 | +0.135 (native is 0) | -0.0008654 to +0.2709 | no |
| utilisation (used / allocatable) | 0.03282 | 0.04629 | +41.0% | +0.01016 to +0.01676 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7878 | 1.111 | +41.0% | +0.2439 to +0.4022 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00796 | +0.00796 (native is 0) | +0.006945 to +0.008975 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7878 | 1.119 | +42.0% | +0.2509 to +0.4111 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 797.5 | 584.1 | -26.8% | -245.5 to -181.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.737 | 9.797 | +0.6% | -0.1743 to +0.2947 | no |
| pods started | 2.2 | 1.6 | -27.3% | -1.825 to +0.6251 | no |
| pod start wait, total (s) | 2.9 | 2.6 | -10.3% | -2.054 to +1.454 | no |
| pod start wait, mean (s) | 0.9083 | 1.3 | +43.1% | -0.3047 to +1.088 | no |
| host CPU busy, the real machine under kind (%) | 23.73 | 32.76 | +38.1% | +6.83 to +11.23 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*