# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 220.6 | 92.56 |
| response time (ms), 95th percentile | 551.5 | 135.9 |
| response time (ms), 99th percentile | 738.9 | 332.3 |
| time over the response line (% of samples) | 6.197 | 0.3542 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.4633 |
| utilisation (used / allocatable) | 0.03195 | 0.04915 |
| CPU used (cores), mean | 0.7668 | 1.18 |
| Omni's own CPU (cores), mean | 0 | 0.0097 |
| CPU used with Omni's own (cores), mean | 0.7668 | 1.189 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 817.3 | 548.4 |
| HPA replicas, mean | 3.037 | 2.523 |
| pods started | 3 | 2.5 |
| pod start wait, total (s) | 27.4 | 25.3 |
| pod start wait, mean (s) | 9.133 | 9.917 |
| host CPU busy, the real machine under kind (%) | 24.15 | 36.22 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.092e-16 to +7.789e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.515 | -0.2% | -0.00978 to +0.004447 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.8 | +2.3% | +2.775 to +4.609 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.8 | +2.3% | +2.775 to +4.609 | yes: power given |
| response time (ms), mean | 220.6 | 92.56 | -58.0% | -156.9 to -99.14 | yes: GAIN |
| response time (ms), 95th percentile | 551.5 | 135.9 | -75.4% | -546.2 to -285 | yes: GAIN |
| response time (ms), 99th percentile | 738.9 | 332.3 | -55.0% | -573.7 to -239.5 | yes: GAIN |
| time over the response line (% of samples) | 6.197 | 0.3542 | -94.3% | -9.096 to -2.589 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 0.4 | -93.2% | -7.818 to -3.182 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.9 | +4.9 (native is 0) | +3.81 to +5.99 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.4633 | +3.7% | -0.2775 to +0.3108 | no |
| utilisation (used / allocatable) | 0.03195 | 0.04915 | +53.8% | +0.01475 to +0.01965 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7668 | 1.18 | +53.8% | +0.3539 to +0.4717 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0097 | +0.0097 (native is 0) | +0.008557 to +0.01084 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7668 | 1.189 | +55.1% | +0.3627 to +0.4823 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 817.3 | 548.4 | -32.9% | -285.2 to -252.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.037 | 2.523 | -16.9% | -0.6519 to -0.376 | yes: GAIN |
| pods started | 3 | 2.5 | -16.7% | -0.877 to -0.123 | yes: GAIN |
| pod start wait, total (s) | 27.4 | 25.3 | -7.7% | -7.049 to +2.849 | no |
| pod start wait, mean (s) | 9.133 | 9.917 | +8.6% | -0.0874 to +1.654 | no |
| host CPU busy, the real machine under kind (%) | 24.15 | 36.22 | +50.0% | +10.28 to +13.86 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*