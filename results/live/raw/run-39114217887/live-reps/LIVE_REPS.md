# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 630.8 | 569.9 |
| response time (ms), 95th percentile | 2617 | 2719 |
| response time (ms), 99th percentile | 6853 | 6573 |
| time over the response line (% of samples) | 29.72 | 26.42 |
| failed requests (%) | 5.179 | 4.576 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8083 | 1.438 |
| utilisation (used / allocatable) | 0.1066 | 0.1061 |
| CPU used (cores), mean | 2.559 | 2.548 |
| Omni's own CPU (cores), mean | 0 | 0.01185 |
| CPU used with Omni's own (cores), mean | 2.559 | 2.559 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 270.8 | 271.8 |
| HPA replicas, mean | 15.52 | 15.95 |
| pods started | 3.7 | 2.9 |
| pod start wait, total (s) | 6.6 | 5.2 |
| pod start wait, mean (s) | 1.737 | 1.808 |
| host CPU busy, the real machine under kind (%) | 74.64 | 74.76 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 242.6 | 240.9 |
| second app: response time (ms), 99th percentile | 1289 | 1273 |
| second app: time over the response line (% of samples) | 17.15 | 17.21 |
| second app: failed requests (%) | 16.13 | 16.44 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.516 | +0.1% | -0.003904 to +0.006904 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.6 | 174.7 | +0.1% | -0.6168 to +0.8098 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.6 | 174.7 | +0.1% | -0.6168 to +0.8098 | no |
| response time (ms), mean | 630.8 | 569.9 | -9.6% | -129.6 to +7.881 | no |
| response time (ms), 95th percentile | 2617 | 2719 | +3.9% | -294.8 to +499.1 | no |
| response time (ms), 99th percentile | 6853 | 6573 | -4.1% | -1431 to +869.9 | no |
| time over the response line (% of samples) | 29.72 | 26.42 | -11.1% | -5.353 to -1.24 | yes: GAIN |
| failed requests (%) | 5.179 | 4.576 | -11.6% | -2.082 to +0.8772 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 9.8 | -4.9% | -1.006 to +0.005799 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.2 | +33.2 (native is 0) | +31.86 to +34.54 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8083 | 1.438 | +77.9% | -0.2862 to +1.546 | no |
| utilisation (used / allocatable) | 0.1066 | 0.1061 | -0.4% | -0.001022 to +0.0001102 | no |
| CPU used (cores), mean | 2.559 | 2.548 | -0.4% | -0.02452 to +0.002645 | no |
| Omni's own CPU (cores), mean | 0 | 0.01185 | +0.0119 (native is 0) | +0.01126 to +0.01244 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.559 | 2.559 | +0.0% | -0.01281 to +0.01463 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 270.8 | 271.8 | +0.4% | -0.1882 to +2.328 | no |
| HPA replicas, mean | 15.52 | 15.95 | +2.7% | -0.002919 to +0.8494 | no |
| pods started | 3.7 | 2.9 | -21.6% | -1.679 to +0.07931 | no |
| pod start wait, total (s) | 6.6 | 5.2 | -21.2% | -4.081 to +1.281 | no |
| pod start wait, mean (s) | 1.737 | 1.808 | +4.1% | -0.4547 to +0.598 | no |
| host CPU busy, the real machine under kind (%) | 74.64 | 74.76 | +0.2% | -0.3828 to +0.6212 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 242.6 | 240.9 | -0.7% | -20.12 to +16.65 | no |
| second app: response time (ms), 99th percentile | 1289 | 1273 | -1.3% | -569.3 to +536.6 | no |
| second app: time over the response line (% of samples) | 17.15 | 17.21 | +0.4% | -0.3576 to +0.4878 | no |
| second app: failed requests (%) | 16.13 | 16.44 | +1.9% | -0.03147 to +0.6416 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*