# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.522 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 162.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 162.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 154.6 | 92.72 |
| response time (ms), 95th percentile | 316.6 | 138.7 |
| response time (ms), 99th percentile | 441.8 | 183 |
| time over the response line (% of samples) | 0.6059 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.43 |
| utilisation (used / allocatable) | 0.03785 | 0.0512 |
| CPU used (cores), mean | 0.9084 | 1.229 |
| Omni's own CPU (cores), mean | 0 | 0.0126 |
| CPU used with Omni's own (cores), mean | 0.9084 | 1.241 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.8 | 523.7 |
| HPA replicas, mean | 8.907 | 9.223 |
| pods started | 4.6 | 5 |
| pod start wait, total (s) | 12.6 | 14.8 |
| pod start wait, mean (s) | 2.592 | 2.842 |
| host CPU busy, the real machine under kind (%) | 28.18 | 37.95 |
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
| node-hours | 1.522 | 1.517 | -0.3% | -0.01071 to +0.0003812 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 162.3 | +1.6% | +1.829 to +3.229 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 162.3 | +1.6% | +1.829 to +3.229 | yes: power given |
| response time (ms), mean | 154.6 | 92.72 | -40.0% | -67.36 to -56.48 | yes: GAIN |
| response time (ms), 95th percentile | 316.6 | 138.7 | -56.2% | -193 to -162.7 | yes: GAIN |
| response time (ms), 99th percentile | 441.8 | 183 | -58.6% | -283.4 to -234.3 | yes: GAIN |
| time over the response line (% of samples) | 0.6059 | 0 | -100.0% | -0.9031 to -0.3086 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | -100.0% | -0.7694 to -0.03062 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17 | +17 (native is 0) | +16.42 to +17.58 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4283 | 0.43 | +0.4% | -0.2342 to +0.2375 | no |
| utilisation (used / allocatable) | 0.03785 | 0.0512 | +35.3% | +0.01177 to +0.01492 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9084 | 1.229 | +35.3% | +0.2825 to +0.3581 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0126 | +0.0126 (native is 0) | +0.01154 to +0.01366 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9084 | 1.241 | +36.6% | +0.2946 to +0.3712 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 693.8 | 523.7 | -24.5% | -183.7 to -156.4 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.907 | 9.223 | +3.5% | +0.1676 to +0.4643 | yes: power given |
| pods started | 4.6 | 5 | +8.7% | -0.5656 to +1.366 | no |
| pod start wait, total (s) | 12.6 | 14.8 | +17.5% | -6.429 to +10.83 | no |
| pod start wait, mean (s) | 2.592 | 2.842 | +9.6% | -1.037 to +1.537 | no |
| host CPU busy, the real machine under kind (%) | 28.18 | 37.95 | +34.7% | +8.744 to +10.8 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*