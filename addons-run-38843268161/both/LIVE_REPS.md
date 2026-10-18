# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 145.7 | 89.97 |
| response time (ms), 95th percentile | 295.5 | 141.1 |
| response time (ms), 99th percentile | 436.9 | 181.5 |
| time over the response line (% of samples) | 0.6027 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.245 |
| utilisation (used / allocatable) | 0.03727 | 0.04956 |
| CPU used (cores), mean | 0.8944 | 1.189 |
| Omni's own CPU (cores), mean | 0 | 0.01253 |
| CPU used with Omni's own (cores), mean | 0.8944 | 1.202 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705 | 542.3 |
| HPA replicas, mean | 8.934 | 9.169 |
| pods started | 4.8 | 4.8 |
| pod start wait, total (s) | 13.1 | 15.9 |
| pod start wait, mean (s) | 2.555 | 3.123 |
| host CPU busy, the real machine under kind (%) | 27.69 | 36.72 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.688e-16 to +1.768e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.516 | -0.1% | -0.01019 to +0.008187 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.7 | +1.7% | +1.411 to +3.916 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.7 | +1.7% | +1.411 to +3.916 | yes: power given |
| response time (ms), mean | 145.7 | 89.97 | -38.2% | -66.58 to -44.86 | yes: GAIN |
| response time (ms), 95th percentile | 295.5 | 141.1 | -52.3% | -177.3 to -131.6 | yes: GAIN |
| response time (ms), 99th percentile | 436.9 | 181.5 | -58.5% | -301.9 to -208.9 | yes: GAIN |
| time over the response line (% of samples) | 0.6027 | 0 | -100.0% | -0.9473 to -0.258 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | -100.0% | -0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.7 | +16.7 (native is 0) | +15.69 to +17.71 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.245 | -29.3% | -0.3443 to +0.141 | no |
| utilisation (used / allocatable) | 0.03727 | 0.04956 | +33.0% | +0.01031 to +0.01427 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8944 | 1.189 | +33.0% | +0.2474 to +0.3425 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01253 | +0.0125 (native is 0) | +0.01131 to +0.01375 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8944 | 1.202 | +34.4% | +0.2588 to +0.3561 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 705 | 542.3 | -23.1% | -181.2 to -144.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.934 | 9.169 | +2.6% | -0.02062 to +0.4909 | no |
| pods started | 4.8 | 4.8 | +0.0% | -1.118 to +1.118 | no |
| pod start wait, total (s) | 13.1 | 15.9 | +21.4% | -6.913 to +12.51 | no |
| pod start wait, mean (s) | 2.555 | 3.123 | +22.2% | -0.7819 to +1.919 | no |
| host CPU busy, the real machine under kind (%) | 27.69 | 36.72 | +32.6% | +7.724 to +10.34 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*