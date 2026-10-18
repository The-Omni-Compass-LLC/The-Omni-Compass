# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 162.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 162.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 166.9 | 90.21 |
| response time (ms), 95th percentile | 340.7 | 143.3 |
| response time (ms), 99th percentile | 483.1 | 167.9 |
| time over the response line (% of samples) | 0.9107 | 0.01212 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 |
| utilisation (used / allocatable) | 0.03425 | 0.05064 |
| CPU used (cores), mean | 0.822 | 1.215 |
| Omni's own CPU (cores), mean | 0 | 0.00854 |
| CPU used with Omni's own (cores), mean | 0.822 | 1.224 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 763.5 | 528.4 |
| HPA replicas, mean | 9.826 | 9.938 |
| pods started | 2.1 | 0.7 |
| pod start wait, total (s) | 2.8 | 1.2 |
| pod start wait, mean (s) | 1.083 | 0.85 |
| host CPU busy, the real machine under kind (%) | 24.8 | 35.76 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.213e-15 to +5.023e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.519 | +0.3% | -0.0004777 to +0.01048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 162.4 | +2.7% | +3.55 to +5.003 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 162.4 | +2.7% | +3.55 to +5.003 | yes: power given |
| response time (ms), mean | 166.9 | 90.21 | -46.0% | -86.88 to -66.51 | yes: GAIN |
| response time (ms), 95th percentile | 340.7 | 143.3 | -57.9% | -221.3 to -173.4 | yes: GAIN |
| response time (ms), 99th percentile | 483.1 | 167.9 | -65.2% | -351.1 to -279.3 | yes: GAIN |
| time over the response line (% of samples) | 0.9107 | 0.01212 | -98.7% | -1.261 to -0.5358 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.6 | 0 | -100.0% | -1.203 to +0.0032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.1 | +15.1 (native is 0) | +13.33 to +16.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 | +0.08 (native is 0) | -0.01214 to +0.1721 | no |
| utilisation (used / allocatable) | 0.03425 | 0.05064 | +47.9% | +0.01489 to +0.01789 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.822 | 1.215 | +47.9% | +0.3575 to +0.4293 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00854 | +0.00854 (native is 0) | +0.007949 to +0.009131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.822 | 1.224 | +48.9% | +0.3656 to +0.4382 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 763.5 | 528.4 | -30.8% | -258 to -212.2 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.826 | 9.938 | +1.1% | -0.02495 to +0.2482 | no |
| pods started | 2.1 | 0.7 | -66.7% | -2.528 to -0.2715 | yes: GAIN |
| pod start wait, total (s) | 2.8 | 1.2 | -57.1% | -3.189 to -0.01122 | yes: GAIN |
| pod start wait, mean (s) | 1.083 | 0.85 | -21.5% | -0.9814 to +0.5148 | no |
| host CPU busy, the real machine under kind (%) | 24.8 | 35.76 | +44.2% | +10.11 to +11.82 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*