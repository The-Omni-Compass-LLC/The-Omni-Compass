# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.337 | 4.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.2 | 478 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.2 | 478 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 255.8 | 128.4 |
| response time (ms), 95th percentile | 667.6 | 254.3 |
| response time (ms), 99th percentile | 1265 | 624.7 |
| time over the response line (% of samples) | 10.98 | 2.551 |
| failed requests (%) | 1 | 0.8541 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.1 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8167 | 0.93 |
| utilisation (used / allocatable) | 0.0764 | 0.07348 |
| CPU used (cores), mean | 1.834 | 1.763 |
| Omni's own CPU (cores), mean | 0 | 0.00919 |
| CPU used with Omni's own (cores), mean | 1.834 | 1.773 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387 | 399.5 |
| HPA replicas, mean | 9.722 | 10.49 |
| pods started | 6 | 13.2 |
| pod start wait, total (s) | 22.4 | 32.5 |
| pod start wait, mean (s) | 3.517 | 2.472 |
| host CPU busy, the real machine under kind (%) | 52.9 | 51.56 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.599e-15 to +1.779e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.337 | 4.334 | -0.1% | -0.01135 to +0.006355 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480.2 | 478 | -0.4% | -2.994 to -1.288 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.2 | 478 | -0.4% | -2.994 to -1.288 | yes: GAIN |
| response time (ms), mean | 255.8 | 128.4 | -49.8% | -165.5 to -89.16 | yes: GAIN |
| response time (ms), 95th percentile | 667.6 | 254.3 | -61.9% | -526.4 to -300.3 | yes: GAIN |
| response time (ms), 99th percentile | 1265 | 624.7 | -50.6% | -806 to -475.6 | yes: GAIN |
| time over the response line (% of samples) | 10.98 | 2.551 | -76.8% | -12.58 to -4.281 | yes: GAIN |
| failed requests (%) | 1 | 0.8541 | -14.6% | -0.2766 to -0.01601 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.1 | 6.9 | -65.7% | -18.3 to -8.099 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.2 | +55.2 (native is 0) | +34.34 to +76.06 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8167 | 0.93 | +13.9% | -0.589 to +0.8157 | no |
| utilisation (used / allocatable) | 0.0764 | 0.07348 | -3.8% | -0.003875 to -0.001974 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.834 | 1.763 | -3.8% | -0.093 to -0.04738 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00919 | +0.00919 (native is 0) | +0.007481 to +0.0109 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.834 | 1.773 | -3.3% | -0.08228 to -0.03972 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387 | 399.5 | +3.2% | +11.15 to +13.83 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.722 | 10.49 | +7.9% | -0.4466 to +1.984 | no |
| pods started | 6 | 13.2 | +120.0% | +2.122 to +12.28 | yes: power given |
| pod start wait, total (s) | 22.4 | 32.5 | +45.1% | -5.559 to +25.76 | no |
| pod start wait, mean (s) | 3.517 | 2.472 | -29.7% | -2.066 to -0.02548 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 52.9 | 51.56 | -2.5% | -1.878 to -0.7856 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*