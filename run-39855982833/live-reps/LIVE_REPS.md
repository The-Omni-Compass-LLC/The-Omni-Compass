# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.2 | 516.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.2 | 516.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 284.4 | 167.4 |
| response time (ms), 95th percentile | 745.9 | 376.1 |
| response time (ms), 99th percentile | 2523 | 1723 |
| time over the response line (% of samples) | 18.09 | 12.16 |
| failed requests (%) | 9.329 | 9.177 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.8 | 21.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.6267 |
| utilisation (used / allocatable) | 0.1018 | 0.102 |
| CPU used (cores), mean | 2.444 | 2.447 |
| Omni's own CPU (cores), mean | 0 | 0.02859 |
| CPU used with Omni's own (cores), mean | 2.444 | 2.476 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296 | 293.5 |
| HPA replicas, mean | 9.657 | 11.55 |
| pods started | 4.9 | 10.3 |
| pod start wait, total (s) | 6.6 | 16.7 |
| pod start wait, mean (s) | 1.331 | 1.619 |
| host CPU busy, the real machine under kind (%) | 68.54 | 69.66 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.65e-15 to -4.82e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.515 | 4.511 | -0.1% | -0.01194 to +0.003273 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.2 | 516.8 | -0.1% | -1.907 to +1.187 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.2 | 516.8 | -0.1% | -1.907 to +1.187 | no |
| response time (ms), mean | 284.4 | 167.4 | -41.1% | -143.3 to -90.7 | yes: GAIN |
| response time (ms), 95th percentile | 745.9 | 376.1 | -49.6% | -434.6 to -305.1 | yes: GAIN |
| response time (ms), 99th percentile | 2523 | 1723 | -31.7% | -1242 to -357.4 | yes: GAIN |
| time over the response line (% of samples) | 18.09 | 12.16 | -32.7% | -7.587 to -4.26 | yes: GAIN |
| failed requests (%) | 9.329 | 9.177 | -1.6% | -1.042 to +0.7366 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.8 | 21.4 | -25.7% | -9.538 to -5.262 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.7 | +56.7 (native is 0) | +48.14 to +65.26 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3233 | 0.6267 | +93.8% | -0.04911 to +0.6558 | no |
| utilisation (used / allocatable) | 0.1018 | 0.102 | +0.1% | -0.001703 to +0.002003 | no |
| CPU used (cores), mean | 2.444 | 2.447 | +0.1% | -0.04086 to +0.04807 | no |
| Omni's own CPU (cores), mean | 0 | 0.02859 | +0.0286 (native is 0) | +0.02499 to +0.03219 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.444 | 2.476 | +1.3% | -0.01142 to +0.07581 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296 | 293.5 | -0.8% | -12.13 to +7.116 | no |
| HPA replicas, mean | 9.657 | 11.55 | +19.6% | +0.5558 to +3.221 | yes: power given |
| pods started | 4.9 | 10.3 | +110.2% | +2.806 to +7.994 | yes: power given |
| pod start wait, total (s) | 6.6 | 16.7 | +153.0% | +4.871 to +15.33 | yes: LOSS |
| pod start wait, mean (s) | 1.331 | 1.619 | +21.7% | -0.07578 to +0.6525 | no |
| host CPU busy, the real machine under kind (%) | 68.54 | 69.66 | +1.6% | -0.08988 to +2.327 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*