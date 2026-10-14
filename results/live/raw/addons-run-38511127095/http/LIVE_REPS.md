# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 212.5 | 87.21 |
| response time (ms), 95th percentile | 518.5 | 138.5 |
| response time (ms), 99th percentile | 702.8 | 203.5 |
| time over the response line (% of samples) | 6.065 | 0.1573 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3133 | 0.2733 |
| utilisation (used / allocatable) | 0.03174 | 0.04931 |
| CPU used (cores), mean | 0.7619 | 1.183 |
| Omni's own CPU (cores), mean | 0 | 0.01007 |
| CPU used with Omni's own (cores), mean | 0.7619 | 1.193 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 822.7 | 545.8 |
| HPA replicas, mean | 2.929 | 2.567 |
| pods started | 3 | 2.4 |
| pod start wait, total (s) | 23.3 | 23.4 |
| pod start wait, mean (s) | 7.767 | 9.683 |
| host CPU busy, the real machine under kind (%) | 24.09 | 36.35 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.452e-16 to +1.609e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.519 | 1.512 | -0.4% | -0.009477 to -0.003857 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.5 | +2.1% | +2.519 to +4.073 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.5 | +2.1% | +2.519 to +4.073 | yes: power given |
| response time (ms), mean | 212.5 | 87.21 | -59.0% | -146.6 to -103.9 | yes: GAIN |
| response time (ms), 95th percentile | 518.5 | 138.5 | -73.3% | -435.5 to -324.6 | yes: GAIN |
| response time (ms), 99th percentile | 702.8 | 203.5 | -71.0% | -563.6 to -435 | yes: GAIN |
| time over the response line (% of samples) | 6.065 | 0.1573 | -97.4% | -8.164 to -3.652 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 0.1 | -98.4% | -8.159 to -3.841 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.4 | +4.4 (native is 0) | +4.031 to +4.769 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3133 | 0.2733 | -12.8% | -0.1899 to +0.1099 | no |
| utilisation (used / allocatable) | 0.03174 | 0.04931 | +55.3% | +0.01514 to +0.01999 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7619 | 1.183 | +55.3% | +0.3633 to +0.4797 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01007 | +0.0101 (native is 0) | +0.009363 to +0.01078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7619 | 1.193 | +56.6% | +0.3728 to +0.4903 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 822.7 | 545.8 | -33.7% | -302 to -251.8 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.929 | 2.567 | -12.4% | -0.5056 to -0.2181 | yes: GAIN |
| pods started | 3 | 2.4 | -20.0% | -0.9694 to -0.2306 | yes: GAIN |
| pod start wait, total (s) | 23.3 | 23.4 | +0.4% | -4.578 to +4.778 | no |
| pod start wait, mean (s) | 7.767 | 9.683 | +24.7% | +0.9396 to +2.894 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 24.09 | 36.35 | +50.9% | +10.71 to +13.8 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*