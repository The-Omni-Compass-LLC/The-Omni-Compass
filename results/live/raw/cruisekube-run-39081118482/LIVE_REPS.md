# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.7 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 86.23 | 87.21 |
| response time (ms), 95th percentile | 134.7 | 136.3 |
| response time (ms), 99th percentile | 151.1 | 155.1 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.08 |
| utilisation (used / allocatable) | 0.04967 | 0.05013 |
| CPU used (cores), mean | 1.192 | 1.203 |
| Omni's own CPU (cores), mean | 0 | 0.00961 |
| CPU used with Omni's own (cores), mean | 1.192 | 1.213 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 542 | 536.2 |
| HPA replicas, mean | 2.773 | 2.809 |
| pods started | 1.2 | 1.3 |
| pod start wait, total (s) | 2.3 | 3.9 |
| pod start wait, mean (s) | 1.55 | 2.6 |
| host CPU busy, the real machine under kind (%) | 36.73 | 37.66 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.566e-16 to +7.895e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.514 | -0.0% | -0.008044 to +0.00771 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.8 | +0.1% | -0.7259 to +0.9053 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.7 | 161.8 | +0.1% | -0.7259 to +0.9053 | no |
| response time (ms), mean | 86.23 | 87.21 | +1.1% | -0.6011 to +2.562 | no |
| response time (ms), 95th percentile | 134.7 | 136.3 | +1.2% | -1.026 to +4.213 | no |
| response time (ms), 99th percentile | 151.1 | 155.1 | +2.7% | -2.402 to +10.5 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.19 | 0.08 | -57.9% | -0.2975 to +0.07751 | no |
| utilisation (used / allocatable) | 0.04967 | 0.05013 | +0.9% | -0.0004306 to +0.001347 | no |
| CPU used (cores), mean | 1.192 | 1.203 | +0.9% | -0.01033 to +0.03234 | no |
| Omni's own CPU (cores), mean | 0 | 0.00961 | +0.00961 (native is 0) | +0.008921 to +0.0103 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.192 | 1.213 | +1.7% | -0.0004662 to +0.04169 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 542 | 536.2 | -1.1% | -15.39 to +3.725 | no |
| HPA replicas, mean | 2.773 | 2.809 | +1.3% | -0.1621 to +0.2338 | no |
| pods started | 1.2 | 1.3 | +8.3% | -0.6113 to +0.8113 | no |
| pod start wait, total (s) | 2.3 | 3.9 | +69.6% | -2.505 to +5.705 | no |
| pod start wait, mean (s) | 1.55 | 2.6 | +67.7% | -0.8157 to +2.916 | no |
| host CPU busy, the real machine under kind (%) | 36.73 | 37.66 | +2.5% | +0.2017 to +1.667 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*