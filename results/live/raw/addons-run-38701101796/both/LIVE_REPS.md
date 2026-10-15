# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 161.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 161.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 144.6 | 85.54 |
| response time (ms), 95th percentile | 300.9 | 128.6 |
| response time (ms), 99th percentile | 437 | 161.1 |
| time over the response line (% of samples) | 0.793 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.3567 |
| utilisation (used / allocatable) | 0.03756 | 0.04894 |
| CPU used (cores), mean | 0.9015 | 1.175 |
| Omni's own CPU (cores), mean | 0 | 0.01199 |
| CPU used with Omni's own (cores), mean | 0.9015 | 1.187 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 700.2 | 551.2 |
| HPA replicas, mean | 8.835 | 9.1 |
| pods started | 5 | 5 |
| pod start wait, total (s) | 16 | 16.8 |
| pod start wait, mean (s) | 3.053 | 3.185 |
| host CPU busy, the real machine under kind (%) | 28.02 | 36.16 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.247e-16 to +1.391e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.516 | -0.1% | -0.00964 to +0.00564 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 161.6 | +1.5% | +1.168 to +3.46 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 161.6 | +1.5% | +1.168 to +3.46 | yes: power given |
| response time (ms), mean | 144.6 | 85.54 | -40.8% | -74.12 to -43.91 | yes: GAIN |
| response time (ms), 95th percentile | 300.9 | 128.6 | -57.3% | -205.6 to -139.1 | yes: GAIN |
| response time (ms), 99th percentile | 437 | 161.1 | -63.1% | -328.2 to -223.6 | yes: GAIN |
| time over the response line (% of samples) | 0.793 | 0 | -100.0% | -1.333 to -0.2531 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 | -100.0% | -1.203 to +0.0032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.4 (native is 0) | +16.9 to +17.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3167 | 0.3567 | +12.6% | -0.1745 to +0.2545 | no |
| utilisation (used / allocatable) | 0.03756 | 0.04894 | +30.3% | +0.008459 to +0.0143 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9015 | 1.175 | +30.3% | +0.203 to +0.3431 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01199 | +0.012 (native is 0) | +0.01053 to +0.01345 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9015 | 1.187 | +31.6% | +0.2138 to +0.3564 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 700.2 | 551.2 | -21.3% | -178.9 to -119.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.835 | 9.1 | +3.0% | +0.105 to +0.4248 | yes: power given |
| pods started | 5 | 5 | +0.0% | -0.754 to +0.754 | no |
| pod start wait, total (s) | 16 | 16.8 | +5.0% | -7.527 to +9.127 | no |
| pod start wait, mean (s) | 3.053 | 3.185 | +4.3% | -1.131 to +1.394 | no |
| host CPU busy, the real machine under kind (%) | 28.02 | 36.16 | +29.1% | +6.107 to +10.18 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*