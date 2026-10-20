# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.282 |
| node-hours | 2.514 | 2.214 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 250.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 210.5 | 159 |
| response time (ms), 95th percentile | 523.3 | 522.3 |
| response time (ms), 99th percentile | 672.1 | 678.9 |
| time over the response line (% of samples) | 6.971 | 6.514 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 25 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.693 | 7.125 |
| utilisation (used / allocatable) | 0.06247 | 0.06953 |
| CPU used (cores), mean | 1.499 | 1.473 |
| Omni's own CPU (cores), mean | 0 | 0.02202 |
| CPU used with Omni's own (cores), mean | 1.499 | 1.495 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.1 | 411.4 |
| HPA replicas, mean | 2.39 | 2.449 |
| pods started | 0.6 | 0 |
| pod start wait, total (s) | 1.3 | 0 |
| pod start wait, mean (s) | 0.65 | 0 |
| host CPU busy, the real machine under kind (%) | 43 | 43.99 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 722.8 | 724.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.677 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.01667 | 0.0125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0 |
| queue: job turnaround, submitted to done, mean (s) | 28.22 | 28.48 |
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
| worker nodes in service, mean | 6 | 5.282 | -12.0% | -1.163 to -0.2736 | yes: GAIN |
| node-hours | 2.514 | 2.214 | -12.0% | -0.4888 to -0.1129 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273 | -0.1% | -1.985 to +1.223 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 250.4 | -8.4% | -37.98 to -8.003 | yes: GAIN |
| response time (ms), mean | 210.5 | 159 | -24.5% | -60.56 to -42.38 | yes: GAIN |
| response time (ms), 95th percentile | 523.3 | 522.3 | -0.2% | -27.67 to +25.64 | no |
| response time (ms), 99th percentile | 672.1 | 678.9 | +1.0% | -17.31 to +30.96 | no |
| time over the response line (% of samples) | 6.971 | 6.514 | -6.6% | -1.369 to +0.4557 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.7 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.3 | +38.3 (native is 0) | +23.57 to +53.03 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.693 | 7.125 | +6.4% | -1.248 to +2.112 | no |
| utilisation (used / allocatable) | 0.06247 | 0.06953 | +11.3% | +0.002981 to +0.01114 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.499 | 1.473 | -1.8% | -0.1051 to +0.05191 | no |
| Omni's own CPU (cores), mean | 0 | 0.02202 | +0.022 (native is 0) | +0.01899 to +0.02505 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.499 | 1.495 | -0.3% | -0.0836 to +0.07446 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.1 | 411.4 | -6.5% | -51.86 to -5.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.39 | 2.449 | +2.5% | -0.05982 to +0.1782 | no |
| pods started | 0.6 | 0 | -100.0% | -1.291 to +0.09105 | no |
| pod start wait, total (s) | 1.3 | 0 | -100.0% | -2.81 to +0.2099 | no |
| pod start wait, mean (s) | 0.65 | 0 | -100.0% | -1.405 to +0.1049 | no |
| host CPU busy, the real machine under kind (%) | 43 | 43.99 | +2.3% | +0.8235 to +1.159 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 722.8 | 724.4 | +0.2% | +0.04742 to +3.153 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.677 | -22.0% | -2.093 to -0.5524 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.01667 | 0.0125 | -25.0% | -0.02616 to +0.01782 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 28.22 | 28.48 | +0.9% | +0.04666 to +0.4867 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*