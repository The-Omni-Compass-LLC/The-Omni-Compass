# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 154.1 | 151.7 |
| response time (ms), 95th percentile | 325.7 | 306 |
| response time (ms), 99th percentile | 471.9 | 451.5 |
| time over the response line (% of samples) | 1.153 | 0.754 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1583 |
| utilisation (used / allocatable) | 0.03398 | 0.03476 |
| CPU used (cores), mean | 0.8156 | 0.8342 |
| Omni's own CPU (cores), mean | 0 | 0.00753 |
| CPU used with Omni's own (cores), mean | 0.8156 | 0.8417 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.2 | 757.2 |
| HPA replicas, mean | 9.733 | 11.7 |
| pods started | 2.4 | 7.2 |
| pod start wait, total (s) | 4.3 | 11.7 |
| pod start wait, mean (s) | 1.558 | 1.623 |
| host CPU busy, the real machine under kind (%) | 24.73 | 25.73 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.52 | +0.2% | +0.0004756 to +0.004858 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.9 | +0.3% | +0.1607 to +0.8128 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.9 | +0.3% | +0.1607 to +0.8128 | yes: power given |
| response time (ms), mean | 154.1 | 151.7 | -1.6% | -7.3 to +2.448 | no |
| response time (ms), 95th percentile | 325.7 | 306 | -6.0% | -42.17 to +2.802 | no |
| response time (ms), 99th percentile | 471.9 | 451.5 | -4.3% | -54.96 to +14.2 | no |
| time over the response line (% of samples) | 1.153 | 0.754 | -34.6% | -0.8143 to +0.01568 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0.4 | -69.2% | -1.687 to -0.1128 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.1 | +5.1 (native is 0) | +2.729 to +7.471 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1583 | +0.158 (native is 0) | -0.07939 to +0.3961 | no |
| utilisation (used / allocatable) | 0.03398 | 0.03476 | +2.3% | +0.0001241 to +0.001424 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8156 | 0.8342 | +2.3% | +0.002978 to +0.03417 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00753 | +0.00753 (native is 0) | +0.006465 to +0.008595 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8156 | 0.8417 | +3.2% | +0.00965 to +0.04255 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.2 | 757.2 | -1.8% | -26.64 to -1.29 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.733 | 11.7 | +20.2% | +0.8797 to +3.047 | yes: power given |
| pods started | 2.4 | 7.2 | +200.0% | +1.963 to +7.637 | yes: power given |
| pod start wait, total (s) | 4.3 | 11.7 | +172.1% | +2.163 to +12.64 | yes: LOSS |
| pod start wait, mean (s) | 1.558 | 1.623 | +4.2% | -0.3676 to +0.4978 | no |
| host CPU busy, the real machine under kind (%) | 24.73 | 25.73 | +4.0% | +0.472 to +1.522 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*