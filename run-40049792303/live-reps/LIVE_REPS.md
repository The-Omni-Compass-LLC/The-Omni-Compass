# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.206 |
| node-hours | 2.512 | 2.179 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 246.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 309.9 | 274.7 |
| response time (ms), 95th percentile | 982.9 | 1015 |
| response time (ms), 99th percentile | 1434 | 1463 |
| time over the response line (% of samples) | 18.41 | 18.24 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.16 | 9.36 |
| utilisation (used / allocatable) | 0.05931 | 0.06837 |
| CPU used (cores), mean | 1.424 | 1.405 |
| Omni's own CPU (cores), mean | 0 | 0.01574 |
| CPU used with Omni's own (cores), mean | 1.424 | 1.421 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 420.2 |
| HPA replicas, mean | 2.022 | 2.503 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 0.1 | 0.9 |
| pod start wait, mean (s) | 0.1 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.32 | 41.12 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 759.7 | 763.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.658 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.05833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 68.65 | 70.34 |
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
| worker nodes in service, mean | 6 | 5.206 | -13.2% | -1.592 to +0.003616 | no |
| node-hours | 2.512 | 2.179 | -13.2% | -0.6673 to +0.00167 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 | -0.1% | -1.116 to +0.7285 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 246.7 | -9.2% | -50.61 to +0.3259 | no |
| response time (ms), mean | 309.9 | 274.7 | -11.4% | -47.55 to -22.8 | yes: GAIN |
| response time (ms), 95th percentile | 982.9 | 1015 | +3.2% | -21.7 to +84.96 | no |
| response time (ms), 99th percentile | 1434 | 1463 | +2.0% | -83.73 to +142 | no |
| time over the response line (% of samples) | 18.41 | 18.24 | -0.9% | -0.803 to +0.4613 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.5 | -1.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 | +32.2 (native is 0) | +20.5 to +43.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.16 | 9.36 | -7.8% | -1.793 to +0.1998 | no |
| utilisation (used / allocatable) | 0.05931 | 0.06837 | +15.3% | +0.0004302 to +0.01768 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.424 | 1.405 | -1.3% | -0.06238 to +0.02562 | no |
| Omni's own CPU (cores), mean | 0 | 0.01574 | +0.0157 (native is 0) | +0.01438 to +0.0171 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.424 | 1.421 | -0.2% | -0.04713 to +0.04185 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 420.2 | -9.3% | -84.34 to -1.793 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.022 | 2.503 | +23.8% | +0.2466 to +0.7166 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.1 | 0.9 | +800.0% | -0.2556 to +1.856 | no |
| pod start wait, mean (s) | 0.1 | 0.9 | +800.0% | -0.2556 to +1.856 | no |
| host CPU busy, the real machine under kind (%) | 40.32 | 41.12 | +2.0% | +0.4246 to +1.179 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.7 | 763.3 | +0.5% | -1.001 to +8.201 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.658 | -22.4% | -2.634 to -0.0508 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.05833 | -17.6% | -0.04706 to +0.02206 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.4 | -42.9% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 68.65 | 70.34 | +2.5% | -3.146 to +6.521 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*