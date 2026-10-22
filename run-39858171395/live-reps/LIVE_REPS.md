# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.331 |
| energy, parked workers still on at idle power (Wh, declared model) | 484.2 | 483.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 484.2 | 483.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 297.8 | 162.6 |
| response time (ms), 95th percentile | 761.1 | 363.5 |
| response time (ms), 99th percentile | 1432 | 1014 |
| time over the response line (% of samples) | 14.92 | 4.576 |
| failed requests (%) | 1.413 | 1.286 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.5 | 11.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 83.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5017 | 0.6 |
| utilisation (used / allocatable) | 0.08302 | 0.08201 |
| CPU used (cores), mean | 1.993 | 1.968 |
| Omni's own CPU (cores), mean | 0 | 0.03058 |
| CPU used with Omni's own (cores), mean | 1.993 | 1.999 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 363.1 | 365.2 |
| HPA replicas, mean | 9.745 | 12.05 |
| pods started | 5.8 | 18.1 |
| pod start wait, total (s) | 8.9 | 31.5 |
| pod start wait, mean (s) | 1.576 | 1.741 |
| host CPU busy, the real machine under kind (%) | 57.2 | 57.73 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.33 | -0.1% | -0.01293 to +0.007592 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 484.2 | 483.2 | -0.2% | -2.837 to +0.8445 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 484.2 | 483.2 | -0.2% | -2.837 to +0.8445 | no |
| response time (ms), mean | 297.8 | 162.6 | -45.4% | -173.8 to -96.48 | yes: GAIN |
| response time (ms), 95th percentile | 761.1 | 363.5 | -52.2% | -489.8 to -305.4 | yes: GAIN |
| response time (ms), 99th percentile | 1432 | 1014 | -29.2% | -651.2 to -184.7 | yes: GAIN |
| time over the response line (% of samples) | 14.92 | 4.576 | -69.3% | -14.58 to -6.108 | yes: GAIN |
| failed requests (%) | 1.413 | 1.286 | -9.0% | -0.2605 to +0.006941 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.5 | 11.6 | -54.5% | -18.63 to -9.174 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 83.9 | +83.9 (native is 0) | +66.92 to +100.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5017 | 0.6 | +19.6% | -0.192 to +0.3887 | no |
| utilisation (used / allocatable) | 0.08302 | 0.08201 | -1.2% | -0.002376 to +0.0003561 | no |
| CPU used (cores), mean | 1.993 | 1.968 | -1.2% | -0.05701 to +0.008547 | no |
| Omni's own CPU (cores), mean | 0 | 0.03058 | +0.0306 (native is 0) | +0.02661 to +0.03455 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.993 | 1.999 | +0.3% | -0.02465 to +0.03735 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 363.1 | 365.2 | +0.6% | -2.425 to +6.587 | no |
| HPA replicas, mean | 9.745 | 12.05 | +23.6% | +1.08 to +3.521 | yes: power given |
| pods started | 5.8 | 18.1 | +212.1% | +8.41 to +16.19 | yes: power given |
| pod start wait, total (s) | 8.9 | 31.5 | +253.9% | +15.62 to +29.58 | yes: LOSS |
| pod start wait, mean (s) | 1.576 | 1.741 | +10.5% | -0.08186 to +0.4124 | no |
| host CPU busy, the real machine under kind (%) | 57.2 | 57.73 | +0.9% | -0.175 to +1.222 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*