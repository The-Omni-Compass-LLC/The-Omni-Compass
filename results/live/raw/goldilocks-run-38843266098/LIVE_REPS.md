# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 161.3 | 86.35 |
| response time (ms), 95th percentile | 339.5 | 129.4 |
| response time (ms), 99th percentile | 516.7 | 160.9 |
| time over the response line (% of samples) | 1.488 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.1067 |
| utilisation (used / allocatable) | 0.03382 | 0.04949 |
| CPU used (cores), mean | 0.8118 | 1.188 |
| Omni's own CPU (cores), mean | 0 | 0.00839 |
| CPU used with Omni's own (cores), mean | 0.8118 | 1.196 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.7 | 546.2 |
| HPA replicas, mean | 9.611 | 9.939 |
| pods started | 3.5 | 0.4 |
| pod start wait, total (s) | 5 | 0.6 |
| pod start wait, mean (s) | 1.417 | 0.5 |
| host CPU busy, the real machine under kind (%) | 24.96 | 35.11 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.087e-17 to +1.147e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.516 | +0.0% | -0.008205 to +0.008871 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.7 | +2.3% | +2.806 to +4.316 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.7 | +2.3% | +2.806 to +4.316 | yes: power given |
| response time (ms), mean | 161.3 | 86.35 | -46.5% | -92.7 to -57.25 | yes: GAIN |
| response time (ms), 95th percentile | 339.5 | 129.4 | -61.9% | -253.1 to -167.1 | yes: GAIN |
| response time (ms), 99th percentile | 516.7 | 160.9 | -68.9% | -422.3 to -289.4 | yes: GAIN |
| time over the response line (% of samples) | 1.488 | 0 | -100.0% | -2.429 to -0.5466 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.7 | 0 | -100.0% | -2.821 to -0.5791 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 | +14.1 (native is 0) | +12.77 to +15.43 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.1067 | +106.5% | -0.06528 to +0.1753 | no |
| utilisation (used / allocatable) | 0.03382 | 0.04949 | +46.3% | +0.01238 to +0.01895 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8118 | 1.188 | +46.3% | +0.2971 to +0.4548 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00839 | +0.00839 (native is 0) | +0.007719 to +0.009061 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8118 | 1.196 | +47.3% | +0.305 to +0.4637 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.7 | 546.2 | -29.4% | -259.9 to -194.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.611 | 9.939 | +3.4% | +0.2161 to +0.4391 | yes: power given |
| pods started | 3.5 | 0.4 | -88.6% | -3.726 to -2.474 | yes: GAIN |
| pod start wait, total (s) | 5 | 0.6 | -88.0% | -5.839 to -2.961 | yes: GAIN |
| pod start wait, mean (s) | 1.417 | 0.5 | -64.7% | -1.65 to -0.1828 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 24.96 | 35.11 | +40.6% | +8.187 to +12.11 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*