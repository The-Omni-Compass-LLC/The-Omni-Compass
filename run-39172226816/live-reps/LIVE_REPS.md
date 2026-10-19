# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.516 | 4.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 515 | 513.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515 | 513.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 271.9 | 148.2 |
| response time (ms), 95th percentile | 733.9 | 266.6 |
| response time (ms), 99th percentile | 2121 | 1308 |
| time over the response line (% of samples) | 16.75 | 8.904 |
| failed requests (%) | 7.922 | 6.998 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.1 | 18.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.7367 |
| utilisation (used / allocatable) | 0.09843 | 0.09647 |
| CPU used (cores), mean | 2.362 | 2.315 |
| Omni's own CPU (cores), mean | 0 | 0.0088 |
| CPU used with Omni's own (cores), mean | 2.362 | 2.324 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.7 | 310.7 |
| HPA replicas, mean | 9.611 | 10.37 |
| pods started | 5.2 | 8.7 |
| pod start wait, total (s) | 6.8 | 14.7 |
| pod start wait, mean (s) | 1.29 | 1.647 |
| host CPU busy, the real machine under kind (%) | 66.26 | 65.41 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.566e-16 to +7.895e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.516 | 4.518 | +0.0% | -0.004541 to +0.007874 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515 | 513.9 | -0.2% | -1.995 to -0.2935 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515 | 513.9 | -0.2% | -1.995 to -0.2935 | yes: GAIN |
| response time (ms), mean | 271.9 | 148.2 | -45.5% | -148.9 to -98.5 | yes: GAIN |
| response time (ms), 95th percentile | 733.9 | 266.6 | -63.7% | -560.4 to -374.2 | yes: GAIN |
| response time (ms), 99th percentile | 2121 | 1308 | -38.3% | -1096 to -530.2 | yes: GAIN |
| time over the response line (% of samples) | 16.75 | 8.904 | -46.8% | -9.848 to -5.836 | yes: GAIN |
| failed requests (%) | 7.922 | 6.998 | -11.7% | -1.591 to -0.2578 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.1 | 18.5 | -31.7% | -10.82 to -6.384 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.2 | +54.2 (native is 0) | +44.1 to +64.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.7367 | +112.5% | -0.1782 to +0.9582 | no |
| utilisation (used / allocatable) | 0.09843 | 0.09647 | -2.0% | -0.002649 to -0.001286 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.362 | 2.315 | -2.0% | -0.06357 to -0.03087 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0088 | +0.0088 (native is 0) | +0.00762 to +0.00998 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.362 | 2.324 | -1.6% | -0.05423 to -0.02261 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.7 | 310.7 | +1.6% | +3.162 to +6.715 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.611 | 10.37 | +7.9% | +0.1044 to +1.412 | yes: power given |
| pods started | 5.2 | 8.7 | +67.3% | +1.11 to +5.89 | yes: power given |
| pod start wait, total (s) | 6.8 | 14.7 | +116.2% | +3.043 to +12.76 | yes: LOSS |
| pod start wait, mean (s) | 1.29 | 1.647 | +27.7% | +0.04136 to +0.6729 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 66.26 | 65.41 | -1.3% | -1.343 to -0.3668 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*