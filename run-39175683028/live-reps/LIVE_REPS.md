# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 154 | 78.47 |
| response time (ms), 95th percentile | 347.1 | 118.7 |
| response time (ms), 99th percentile | 558.5 | 162.2 |
| time over the response line (% of samples) | 2.18 | 0.01212 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.265 |
| utilisation (used / allocatable) | 0.03817 | 0.0362 |
| CPU used (cores), mean | 0.9162 | 0.8688 |
| Omni's own CPU (cores), mean | 0 | 0.0078 |
| CPU used with Omni's own (cores), mean | 0.9162 | 0.8766 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 738.9 | 763.1 |
| HPA replicas, mean | 8.526 | 8.326 |
| pods started | 4.8 | 3.7 |
| pod start wait, total (s) | 6.9 | 4.5 |
| pod start wait, mean (s) | 1.51 | 1.25 |
| host CPU busy, the real machine under kind (%) | 27.58 | 26.49 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.707e-16 to +1.337e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.515 | 1.519 | +0.2% | -0.001683 to +0.008016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159 | -0.1% | -0.7158 to +0.4659 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159 | -0.1% | -0.7158 to +0.4659 | no |
| response time (ms), mean | 154 | 78.47 | -49.0% | -101.6 to -49.39 | yes: GAIN |
| response time (ms), 95th percentile | 347.1 | 118.7 | -65.8% | -302.7 to -154 | yes: GAIN |
| response time (ms), 99th percentile | 558.5 | 162.2 | -71.0% | -525 to -267.7 | yes: GAIN |
| time over the response line (% of samples) | 2.18 | 0.01212 | -99.4% | -3.534 to -0.802 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.2 | 0 | -100.0% | -3.662 to -0.7379 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.3 | +17.3 (native is 0) | +15.36 to +19.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.265 | +893.8% | +0.04874 to +0.4279 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03817 | 0.0362 | -5.2% | -0.003277 to -0.0006731 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9162 | 0.8688 | -5.2% | -0.07866 to -0.01615 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0078 | +0.0078 (native is 0) | +0.006743 to +0.008857 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9162 | 0.8766 | -4.3% | -0.07 to -0.00921 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 738.9 | 763.1 | +3.3% | -2.377 to +50.69 | no |
| HPA replicas, mean | 8.526 | 8.326 | -2.4% | -0.5255 to +0.1245 | no |
| pods started | 4.8 | 3.7 | -22.9% | -2.137 to -0.06342 | yes: GAIN |
| pod start wait, total (s) | 6.9 | 4.5 | -34.8% | -4.882 to +0.08248 | no |
| pod start wait, mean (s) | 1.51 | 1.25 | -17.2% | -0.6136 to +0.09362 | no |
| host CPU busy, the real machine under kind (%) | 27.58 | 26.49 | -4.0% | -1.925 to -0.2641 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*