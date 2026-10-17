# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 207.3 | 86.91 |
| response time (ms), 95th percentile | 480.7 | 131.3 |
| response time (ms), 99th percentile | 642.8 | 305.8 |
| time over the response line (% of samples) | 4.942 | 0.2189 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.405 |
| utilisation (used / allocatable) | 0.0311 | 0.04795 |
| CPU used (cores), mean | 0.7463 | 1.151 |
| Omni's own CPU (cores), mean | 0 | 0.00939 |
| CPU used with Omni's own (cores), mean | 0.7463 | 1.16 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 839.8 | 561 |
| HPA replicas, mean | 2.827 | 2.528 |
| pods started | 2.7 | 2.6 |
| pod start wait, total (s) | 22.6 | 24.4 |
| pod start wait, mean (s) | 8.417 | 9.325 |
| host CPU busy, the real machine under kind (%) | 23.53 | 35.05 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.588e-16 to +1.014e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.512 | -0.2% | -0.01008 to +0.004409 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.3 | +2.3% | +2.495 to +4.608 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.3 | +2.3% | +2.495 to +4.608 | yes: power given |
| response time (ms), mean | 207.3 | 86.91 | -58.1% | -142.4 to -98.44 | yes: GAIN |
| response time (ms), 95th percentile | 480.7 | 131.3 | -72.7% | -402.3 to -296.7 | yes: GAIN |
| response time (ms), 99th percentile | 642.8 | 305.8 | -52.4% | -401.8 to -272.2 | yes: GAIN |
| time over the response line (% of samples) | 4.942 | 0.2189 | -95.6% | -6.939 to -2.507 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0.1 | -98.0% | -6.671 to -2.929 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.6 | +4.6 (native is 0) | +3.997 to +5.203 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.405 | +18.5% | -0.169 to +0.2957 | no |
| utilisation (used / allocatable) | 0.0311 | 0.04795 | +54.2% | +0.01462 to +0.01909 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7463 | 1.151 | +54.2% | +0.351 to +0.4582 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00939 | +0.00939 (native is 0) | +0.00825 to +0.01053 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7463 | 1.16 | +55.5% | +0.3595 to +0.4685 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 839.8 | 561 | -33.2% | -298.9 to -258.6 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.827 | 2.528 | -10.6% | -0.5249 to -0.07314 | yes: GAIN |
| pods started | 2.7 | 2.6 | -3.7% | -0.7263 to +0.5263 | no |
| pod start wait, total (s) | 22.6 | 24.4 | +8.0% | -3.98 to +7.58 | no |
| pod start wait, mean (s) | 8.417 | 9.325 | +10.8% | -0.01873 to +1.835 | no |
| host CPU busy, the real machine under kind (%) | 23.53 | 35.05 | +49.0% | +10 to +13.06 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*