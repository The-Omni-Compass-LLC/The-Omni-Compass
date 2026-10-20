# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 515 | 513.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515 | 513.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 283.6 | 164.5 |
| response time (ms), 95th percentile | 778 | 316.5 |
| response time (ms), 99th percentile | 2162 | 1810 |
| time over the response line (% of samples) | 17.09 | 9.407 |
| failed requests (%) | 7.766 | 6.743 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 18.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.355 | 0.8233 |
| utilisation (used / allocatable) | 0.09912 | 0.0973 |
| CPU used (cores), mean | 2.379 | 2.335 |
| Omni's own CPU (cores), mean | 0 | 0.00966 |
| CPU used with Omni's own (cores), mean | 2.379 | 2.345 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.1 | 307.4 |
| HPA replicas, mean | 9.611 | 10.43 |
| pods started | 5.6 | 7.9 |
| pod start wait, total (s) | 8.9 | 14.5 |
| pod start wait, mean (s) | 1.63 | 1.802 |
| host CPU busy, the real machine under kind (%) | 67.21 | 66.35 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.417e-15 to +1.735e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.513 | -0.0% | -0.007338 to +0.006338 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515 | 513.8 | -0.2% | -2.187 to -0.2118 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515 | 513.8 | -0.2% | -2.187 to -0.2118 | yes: GAIN |
| response time (ms), mean | 283.6 | 164.5 | -42.0% | -144.3 to -93.91 | yes: GAIN |
| response time (ms), 95th percentile | 778 | 316.5 | -59.3% | -550.5 to -372.5 | yes: GAIN |
| response time (ms), 99th percentile | 2162 | 1810 | -16.3% | -888.7 to +184.2 | no |
| time over the response line (% of samples) | 17.09 | 9.407 | -45.0% | -9.7 to -5.671 | yes: GAIN |
| failed requests (%) | 7.766 | 6.743 | -13.2% | -1.592 to -0.4543 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.1 | 18.8 | -33.1% | -12.24 to -6.359 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 51.8 | +51.8 (native is 0) | +42.1 to +61.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.355 | 0.8233 | +131.9% | +0.01466 to +0.922 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09912 | 0.0973 | -1.8% | -0.002322 to -0.001331 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.379 | 2.335 | -1.8% | -0.05574 to -0.03193 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00966 | +0.00966 (native is 0) | +0.008271 to +0.01105 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.379 | 2.345 | -1.4% | -0.04711 to -0.02124 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.1 | 307.4 | +2.1% | +2.398 to +10.17 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.611 | 10.43 | +8.5% | +0.1522 to +1.48 | yes: power given |
| pods started | 5.6 | 7.9 | +41.1% | -0.502 to +5.102 | no |
| pod start wait, total (s) | 8.9 | 14.5 | +62.9% | -1.163 to +12.36 | no |
| pod start wait, mean (s) | 1.63 | 1.802 | +10.5% | -0.1646 to +0.5081 | no |
| host CPU busy, the real machine under kind (%) | 67.21 | 66.35 | -1.3% | -1.08 to -0.6414 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*