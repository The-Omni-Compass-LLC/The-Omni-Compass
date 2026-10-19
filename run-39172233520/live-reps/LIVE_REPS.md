# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.8 | 173.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.8 | 173.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 590.7 | 510.9 |
| response time (ms), 95th percentile | 2528 | 2466 |
| response time (ms), 99th percentile | 6470 | 5747 |
| time over the response line (% of samples) | 27.09 | 24.58 |
| failed requests (%) | 4.489 | 3.804 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.675 | 0.89 |
| utilisation (used / allocatable) | 0.1024 | 0.1016 |
| CPU used (cores), mean | 2.458 | 2.438 |
| Omni's own CPU (cores), mean | 0 | 0.01166 |
| CPU used with Omni's own (cores), mean | 2.458 | 2.449 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 282.5 | 284 |
| HPA replicas, mean | 15.22 | 15.47 |
| pods started | 5.1 | 4.2 |
| pod start wait, total (s) | 8.1 | 7.2 |
| pod start wait, mean (s) | 1.613 | 1.665 |
| host CPU busy, the real machine under kind (%) | 71.66 | 71.31 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 251.2 | 241 |
| second app: response time (ms), 99th percentile | 1555 | 1741 |
| second app: time over the response line (% of samples) | 16.12 | 15.91 |
| second app: failed requests (%) | 15.01 | 14.52 |

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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.147e-15 to +8.087e-17 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.517 | +0.1% | -0.005285 to +0.008618 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.8 | 173.7 | -0.0% | -0.8772 to +0.7246 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.8 | 173.7 | -0.0% | -0.8772 to +0.7246 | no |
| response time (ms), mean | 590.7 | 510.9 | -13.5% | -149.9 to -9.504 | yes: GAIN |
| response time (ms), 95th percentile | 2528 | 2466 | -2.5% | -616.3 to +491.4 | no |
| response time (ms), 99th percentile | 6470 | 5747 | -11.2% | -1672 to +225.7 | no |
| time over the response line (% of samples) | 27.09 | 24.58 | -9.3% | -4.151 to -0.8815 | yes: GAIN |
| failed requests (%) | 4.489 | 3.804 | -15.3% | -1.587 to +0.2158 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.2 | -4.2% | -0.7694 to -0.03062 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.1 | +34.1 (native is 0) | +30.93 to +37.27 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.675 | 0.89 | +31.9% | -0.8721 to +1.302 | no |
| utilisation (used / allocatable) | 0.1024 | 0.1016 | -0.8% | -0.001654 to +4.094e-06 | no |
| CPU used (cores), mean | 2.458 | 2.438 | -0.8% | -0.03971 to +9.825e-05 | no |
| Omni's own CPU (cores), mean | 0 | 0.01166 | +0.0117 (native is 0) | +0.01082 to +0.0125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.449 | -0.3% | -0.02826 to +0.01197 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 282.5 | 284 | +0.5% | -1.15 to +4.217 | no |
| HPA replicas, mean | 15.22 | 15.47 | +1.6% | -0.0135 to +0.509 | no |
| pods started | 5.1 | 4.2 | -17.6% | -2.268 to +0.4676 | no |
| pod start wait, total (s) | 8.1 | 7.2 | -11.1% | -3.999 to +2.199 | no |
| pod start wait, mean (s) | 1.613 | 1.665 | +3.2% | -0.384 to +0.4873 | no |
| host CPU busy, the real machine under kind (%) | 71.66 | 71.31 | -0.5% | -0.8496 to +0.145 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 251.2 | 241 | -4.1% | -67.8 to +47.31 | no |
| second app: response time (ms), 99th percentile | 1555 | 1741 | +12.0% | -1362 to +1734 | no |
| second app: time over the response line (% of samples) | 16.12 | 15.91 | -1.3% | -0.6103 to +0.1913 | no |
| second app: failed requests (%) | 15.01 | 14.52 | -3.3% | -1.184 to +0.2 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*