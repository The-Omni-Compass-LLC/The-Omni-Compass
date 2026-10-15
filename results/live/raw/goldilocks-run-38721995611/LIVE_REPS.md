# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 157.5 | 84.08 |
| response time (ms), 95th percentile | 331 | 128.2 |
| response time (ms), 99th percentile | 474.3 | 154.5 |
| time over the response line (% of samples) | 1.041 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.08 |
| utilisation (used / allocatable) | 0.03414 | 0.04937 |
| CPU used (cores), mean | 0.8193 | 1.185 |
| Omni's own CPU (cores), mean | 0 | 0.00816 |
| CPU used with Omni's own (cores), mean | 0.8193 | 1.193 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.7 | 546 |
| HPA replicas, mean | 9.8 | 9.86 |
| pods started | 2 | 1.1 |
| pod start wait, total (s) | 3.1 | 1.8 |
| pod start wait, mean (s) | 1.35 | 0.8 |
| host CPU busy, the real machine under kind (%) | 24.73 | 34.9 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | no |
| node-hours | 1.515 | 1.517 | +0.2% | -0.00394 to +0.009273 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.1 | 161.9 | +2.4% | +2.719 to +4.822 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.1 | 161.9 | +2.4% | +2.719 to +4.822 | yes: power given |
| response time (ms), mean | 157.5 | 84.08 | -46.6% | -87.57 to -59.28 | yes: GAIN |
| response time (ms), 95th percentile | 331 | 128.2 | -61.3% | -233.8 to -171.8 | yes: GAIN |
| response time (ms), 99th percentile | 474.3 | 154.5 | -67.4% | -363 to -276.7 | yes: GAIN |
| time over the response line (% of samples) | 1.041 | 0 | -100.0% | -1.574 to -0.5075 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.7 | 0 | -100.0% | -1.379 to -0.0214 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16 | +16 (native is 0) | +13.64 to +18.36 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.08 | +200.0% | -0.02709 to +0.1338 | no |
| utilisation (used / allocatable) | 0.03414 | 0.04937 | +44.6% | +0.01261 to +0.01785 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8193 | 1.185 | +44.6% | +0.3028 to +0.4285 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00816 | +0.00816 (native is 0) | +0.007314 to +0.009006 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8193 | 1.193 | +45.6% | +0.3103 to +0.4372 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 766.7 | 546 | -28.8% | -247.1 to -194.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.8 | 9.86 | +0.6% | -0.1327 to +0.2525 | no |
| pods started | 2 | 1.1 | -45.0% | -2.387 to +0.5871 | no |
| pod start wait, total (s) | 3.1 | 1.8 | -41.9% | -4.142 to +1.542 | no |
| pod start wait, mean (s) | 1.35 | 0.8 | -40.7% | -1.521 to +0.4206 | no |
| host CPU busy, the real machine under kind (%) | 24.73 | 34.9 | +41.1% | +8.408 to +11.93 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*