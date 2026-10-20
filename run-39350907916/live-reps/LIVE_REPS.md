# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.121 |
| node-hours | 2.513 | 2.15 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 244.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 173.8 | 138 |
| response time (ms), 95th percentile | 369.2 | 405.6 |
| response time (ms), 99th percentile | 519.6 | 569.8 |
| time over the response line (% of samples) | 1.527 | 2.172 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 2.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.03 | 10.24 |
| utilisation (used / allocatable) | 0.05992 | 0.06717 |
| CPU used (cores), mean | 1.438 | 1.378 |
| Omni's own CPU (cores), mean | 0 | 0.02089 |
| CPU used with Omni's own (cores), mean | 1.438 | 1.399 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.4 | 427.5 |
| HPA replicas, mean | 2.212 | 2.468 |
| pods started | 0.3 | 0 |
| pod start wait, total (s) | 0.6 | 0 |
| pod start wait, mean (s) | 0.4 | 0 |
| host CPU busy, the real machine under kind (%) | 42.99 | 43.67 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 724.3 | 727.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.34 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.625 | 0.6208 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 30.8 | 32.45 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.121 | -14.7% | -1.453 to -0.3061 | yes: GAIN |
| node-hours | 2.513 | 2.15 | -14.4% | -0.6018 to -0.1242 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.2 | +0.0% | -1.097 to +1.302 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 244.5 | -10.1% | -45.89 to -9.28 | yes: GAIN |
| response time (ms), mean | 173.8 | 138 | -20.6% | -43.77 to -27.96 | yes: GAIN |
| response time (ms), 95th percentile | 369.2 | 405.6 | +9.9% | -20.95 to +93.83 | no |
| response time (ms), 99th percentile | 519.6 | 569.8 | +9.7% | -12.33 to +112.7 | no |
| time over the response line (% of samples) | 1.527 | 2.172 | +42.3% | -0.1406 to +1.432 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.8 | 2.9 | +61.1% | -0.3871 to +2.587 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.2 | +26.2 (native is 0) | +17.28 to +35.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.03 | 10.24 | -7.2% | -2.908 to +1.325 | no |
| utilisation (used / allocatable) | 0.05992 | 0.06717 | +12.1% | +0.001717 to +0.0128 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.438 | 1.378 | -4.1% | -0.1193 to +0.0002978 | no |
| Omni's own CPU (cores), mean | 0 | 0.02089 | +0.0209 (native is 0) | +0.01478 to +0.027 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.438 | 1.399 | -2.7% | -0.09426 to +0.017 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.4 | 427.5 | -7.1% | -63.75 to -2.003 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.212 | 2.468 | +11.5% | -0.002157 to +0.513 | no |
| pods started | 0.3 | 0 | -100.0% | -0.7828 to +0.1828 | no |
| pod start wait, total (s) | 0.6 | 0 | -100.0% | -1.566 to +0.3656 | no |
| pod start wait, mean (s) | 0.4 | 0 | -100.0% | -1.003 to +0.2032 | no |
| host CPU busy, the real machine under kind (%) | 42.99 | 43.67 | +1.6% | -0.06499 to +1.414 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 724.3 | 727.5 | +0.4% | +0.5492 to +5.851 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.34 | -27.7% | -2.733 to -0.587 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.625 | 0.6208 | -0.7% | -0.05374 to +0.04541 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 30.8 | 32.45 | +5.3% | -0.7363 to +4.028 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*