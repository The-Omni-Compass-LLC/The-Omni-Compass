# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native |
|---|---:|
| worker nodes in service, mean | 6 |
| node-hours | 0.615 |
| energy, parked workers still on at idle power (Wh, declared model) | 66.38 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 66.38 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan |
| response time (ms), mean | 100 |
| response time (ms), 95th percentile | 154.7 |
| response time (ms), 99th percentile | 205.4 |
| time over the response line (% of samples) | 0 |
| failed requests (%) | 0 |
| pods with no machine to take them (unschedulable) | 0 |
| time pods had no machine to take them, pod-minutes | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 |
| utilisation (used / allocatable) | 0.05718 |
| CPU used (cores), mean | 1.372 |
| Omni's own CPU (cores), mean | 0 |
| CPU used with Omni's own (cores), mean | 1.372 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.9 |
| HPA replicas, mean | 2.957 |
| pods started | 2 |
| pod start wait, total (s) | 11 |
| pod start wait, mean (s) | 5.5 |
| host CPU busy, the real machine under kind (%) | 42.96 |
| host cores (the real machine under kind) | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*