# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.989 |
| node-hours | 1.507 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.5 | 161.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.5 | 161.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 76.11 | 76.35 |
| response time (ms), 95th percentile | 112.8 | 113.6 |
| response time (ms), 99th percentile | 135.2 | 127.6 |
| time over the response line (% of samples) | 0.01227 | 0 |
| failed requests (%) | 0.01227 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.08333 |
| utilisation (used / allocatable) | 0.0475 | 0.04673 |
| CPU used (cores), mean | 1.14 | 1.119 |
| Omni's own CPU (cores), mean | 0 | 0.00834 |
| CPU used with Omni's own (cores), mean | 1.14 | 1.127 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 571 | 581.1 |
| HPA replicas, mean | 2.803 | 2.671 |
| pods started | 1.6 | 1.2 |
| pod start wait, total (s) | 6.3 | 2.6 |
| pod start wait, mean (s) | 3.4 | 1.75 |
| host CPU busy, the real machine under kind (%) | 34.91 | 35.37 |
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

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.989 | -0.2% | -0.03426 to +0.01326 | no |
| node-hours | 1.507 | 1.515 | +0.5% | +0.00259 to +0.01308 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 160.5 | 161.7 | +0.7% | +0.4611 to +1.834 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.5 | 161.5 | +0.6% | +0.5866 to +1.308 | yes: power given |
| response time (ms), mean | 76.11 | 76.35 | +0.3% | -0.7313 to +1.214 | no |
| response time (ms), 95th percentile | 112.8 | 113.6 | +0.7% | -1.144 to +2.691 | no |
| response time (ms), 99th percentile | 135.2 | 127.6 | -5.6% | -21.5 to +6.315 | no |
| time over the response line (% of samples) | 0.01227 | 0 | -100.0% | -0.04002 to +0.01548 | no |
| failed requests (%) | 0.01227 | 0 | -100.0% | -0.04002 to +0.01548 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.08333 | -69.7% | -0.4011 to +0.01781 | no |
| utilisation (used / allocatable) | 0.0475 | 0.04673 | -1.6% | -0.001643 to +8.599e-05 | no |
| CPU used (cores), mean | 1.14 | 1.119 | -1.8% | -0.04122 to -0.0007356 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00834 | +0.00834 (native is 0) | +0.007285 to +0.009395 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.14 | 1.127 | -1.1% | -0.03261 to +0.007342 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 571 | 581.1 | +1.8% | -1.692 to +21.95 | no |
| HPA replicas, mean | 2.803 | 2.671 | -4.7% | -0.3574 to +0.09249 | no |
| pods started | 1.6 | 1.2 | -25.0% | -1.003 to +0.2032 | no |
| pod start wait, total (s) | 6.3 | 2.6 | -58.7% | -9.075 to +1.675 | no |
| pod start wait, mean (s) | 3.4 | 1.75 | -48.5% | -4.052 to +0.7525 | no |
| host CPU busy, the real machine under kind (%) | 34.91 | 35.37 | +1.3% | -0.04314 to +0.9701 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*