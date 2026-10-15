# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 204.3 | 83.71 |
| response time (ms), 95th percentile | 493.4 | 125.4 |
| response time (ms), 99th percentile | 653.3 | 207 |
| time over the response line (% of samples) | 5.151 | 0.158 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3717 | 0.325 |
| utilisation (used / allocatable) | 0.03105 | 0.04827 |
| CPU used (cores), mean | 0.7452 | 1.158 |
| Omni's own CPU (cores), mean | 0 | 0.00915 |
| CPU used with Omni's own (cores), mean | 0.7452 | 1.168 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 841.2 | 558.1 |
| HPA replicas, mean | 2.886 | 2.439 |
| pods started | 2.7 | 2.3 |
| pod start wait, total (s) | 24.1 | 23.2 |
| pod start wait, mean (s) | 8.783 | 9.883 |
| host CPU busy, the real machine under kind (%) | 23.59 | 35.18 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.512 | -0.4% | -0.01261 to +0.001947 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.3 | +2.1% | +2.413 to +4.338 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.3 | +2.1% | +2.413 to +4.338 | yes: power given |
| response time (ms), mean | 204.3 | 83.71 | -59.0% | -140.5 to -100.7 | yes: GAIN |
| response time (ms), 95th percentile | 493.4 | 125.4 | -74.6% | -421.8 to -314.2 | yes: GAIN |
| response time (ms), 99th percentile | 653.3 | 207 | -68.3% | -511.3 to -381.3 | yes: GAIN |
| time over the response line (% of samples) | 5.151 | 0.158 | -96.9% | -7.275 to -2.71 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 0.1 | -98.1% | -7.423 to -2.777 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.3 | +4.3 (native is 0) | +3.954 to +4.646 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3717 | 0.325 | -12.6% | -0.3746 to +0.2813 | no |
| utilisation (used / allocatable) | 0.03105 | 0.04827 | +55.4% | +0.01478 to +0.01965 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7452 | 1.158 | +55.4% | +0.3548 to +0.4717 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00915 | +0.00915 (native is 0) | +0.008066 to +0.01023 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7452 | 1.168 | +56.7% | +0.3631 to +0.4817 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 841.2 | 558.1 | -33.6% | -306.7 to -259.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.886 | 2.439 | -15.5% | -0.654 to -0.2395 | yes: GAIN |
| pods started | 2.7 | 2.3 | -14.8% | -0.9001 to +0.1001 | no |
| pod start wait, total (s) | 24.1 | 23.2 | -3.7% | -7.425 to +5.625 | no |
| pod start wait, mean (s) | 8.783 | 9.883 | +12.5% | +0.2057 to +1.994 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.59 | 35.18 | +49.1% | +9.764 to +13.41 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*