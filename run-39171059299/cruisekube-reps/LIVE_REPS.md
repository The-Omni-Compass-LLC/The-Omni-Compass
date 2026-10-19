# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 64.75 | 71.36 |
| response time (ms), 95th percentile | 96.11 | 107.6 |
| response time (ms), 99th percentile | 110.6 | 120.3 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.06667 | 0.02667 |
| utilisation (used / allocatable) | 0.04348 | 0.04548 |
| CPU used (cores), mean | 1.044 | 1.091 |
| Omni's own CPU (cores), mean | 0 | 0.00806 |
| CPU used with Omni's own (cores), mean | 1.044 | 1.1 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 619.7 | 593.3 |
| HPA replicas, mean | 2.738 | 2.756 |
| pods started | 1.25 | 1.2 |
| pod start wait, total (s) | 1.625 | 1.8 |
| pod start wait, mean (s) | 1.25 | 1.35 |
| host CPU busy, the real machine under kind (%) | 32.38 | 34.19 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 8 paired repetitions

Omni-Compass stayed native in 8 of 8 repetitions (repetitions 1, 2, 3, 4, 6, 7, 8, 9): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.195e-16 to +8.856e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.513 | -0.1% | -0.01481 to +0.01106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.4 | 160.3 | -0.1% | -1.472 to +1.292 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.4 | 160.3 | -0.1% | -1.472 to +1.292 | no |
| response time (ms), mean | 64.75 | 64.81 | +0.1% | -1.33 to +1.467 | no |
| response time (ms), 95th percentile | 96.11 | 95.19 | -1.0% | -3.613 to +1.771 | no |
| response time (ms), 99th percentile | 110.6 | 106 | -4.1% | -13.19 to +4.09 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.06667 | 0.03333 | -50.0% | -0.1762 to +0.1096 | no |
| utilisation (used / allocatable) | 0.04348 | 0.04378 | +0.7% | -0.0006211 to +0.001225 | no |
| CPU used (cores), mean | 1.044 | 1.051 | +0.7% | -0.01491 to +0.02939 | no |
| Omni's own CPU (cores), mean | 0 | 0.007575 | +0.00758 (native is 0) | +0.006376 to +0.008774 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.044 | 1.058 | +1.4% | -0.006513 to +0.03614 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 619.7 | 613.4 | -1.0% | -19.29 to +6.725 | no |
| HPA replicas, mean | 2.738 | 2.728 | -0.4% | -0.1712 to +0.1518 | no |
| pods started | 1.25 | 1.25 | +0.0% | -0.4469 to +0.4469 | no |
| pod start wait, total (s) | 1.625 | 1.875 | +15.4% | -0.9942 to +1.494 | no |
| pod start wait, mean (s) | 1.25 | 1.312 | +5.0% | -0.8435 to +0.9685 | no |
| host CPU busy, the real machine under kind (%) | 32.38 | 32.98 | +1.9% | +0.306 to +0.9086 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*