# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 143.4 | 76.5 |
| response time (ms), 95th percentile | 307.3 | 118.4 |
| response time (ms), 99th percentile | 449.6 | 148.5 |
| time over the response line (% of samples) | 1.046 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05333 |
| utilisation (used / allocatable) | 0.03256 | 0.04665 |
| CPU used (cores), mean | 0.7814 | 1.12 |
| Omni's own CPU (cores), mean | 0 | 0.00774 |
| CPU used with Omni's own (cores), mean | 0.7814 | 1.127 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.2 | 579.7 |
| HPA replicas, mean | 9.78 | 9.828 |
| pods started | 2.1 | 1.3 |
| pod start wait, total (s) | 2.6 | 1.7 |
| pod start wait, mean (s) | 0.7417 | 0.65 |
| host CPU busy, the real machine under kind (%) | 23.64 | 32.94 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.8e-16 to +5.576e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.514 | -0.1% | -0.007912 to +0.005578 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.8 | +1.9% | +2.166 to +3.951 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160.8 | +1.9% | +2.166 to +3.951 | yes: power given |
| response time (ms), mean | 143.4 | 76.5 | -46.6% | -86.31 to -47.4 | yes: GAIN |
| response time (ms), 95th percentile | 307.3 | 118.4 | -61.5% | -226.8 to -151.1 | yes: GAIN |
| response time (ms), 99th percentile | 449.6 | 148.5 | -67.0% | -362.3 to -239.9 | yes: GAIN |
| time over the response line (% of samples) | 1.046 | 0 | -100.0% | -1.825 to -0.2676 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | -100.0% | -2.168 to +0.1681 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 | +16.6 (native is 0) | +13.7 to +19.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05333 | +0.0533 (native is 0) | -0.02709 to +0.1338 | no |
| utilisation (used / allocatable) | 0.03256 | 0.04665 | +43.3% | +0.01039 to +0.0178 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7814 | 1.12 | +43.3% | +0.2494 to +0.4273 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00774 | +0.00774 (native is 0) | +0.006612 to +0.008868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7814 | 1.127 | +44.3% | +0.2562 to +0.436 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 801.2 | 579.7 | -27.7% | -258.6 to -184.5 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.78 | 9.828 | +0.5% | -0.1473 to +0.2449 | no |
| pods started | 2.1 | 1.3 | -38.1% | -2.053 to +0.4526 | no |
| pod start wait, total (s) | 2.6 | 1.7 | -34.6% | -2.85 to +1.05 | no |
| pod start wait, mean (s) | 0.7417 | 0.65 | -12.4% | -0.7089 to +0.5255 | no |
| host CPU busy, the real machine under kind (%) | 23.64 | 32.94 | +39.3% | +6.75 to +11.83 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*