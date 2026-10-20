# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.099 |
| node-hours | 2.516 | 2.135 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 243.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 191.3 | 151.5 |
| response time (ms), 95th percentile | 469.7 | 494.8 |
| response time (ms), 99th percentile | 621.8 | 650.1 |
| time over the response line (% of samples) | 5.064 | 5.459 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.885 | 7.367 |
| utilisation (used / allocatable) | 0.06149 | 0.071 |
| CPU used (cores), mean | 1.476 | 1.439 |
| Omni's own CPU (cores), mean | 0 | 0.01963 |
| CPU used with Omni's own (cores), mean | 1.476 | 1.459 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.1 | 407 |
| HPA replicas, mean | 2.159 | 2.343 |
| pods started | 0.2 | 0.5 |
| pod start wait, total (s) | 0.5 | 1 |
| pod start wait, mean (s) | 0.5 | 0.75 |
| host CPU busy, the real machine under kind (%) | 41.42 | 42.54 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 721.9 | 722.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.415 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.03333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 |
| queue: job turnaround, submitted to done, mean (s) | 27.32 | 27.65 |
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
| worker nodes in service, mean | 6 | 5.099 | -15.0% | -1.536 to -0.2664 | yes: GAIN |
| node-hours | 2.516 | 2.135 | -15.2% | -0.6464 to -0.1167 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.1 | -0.4% | -2.49 to +0.4534 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 243.8 | -10.7% | -50.04 to -8.503 | yes: GAIN |
| response time (ms), mean | 191.3 | 151.5 | -20.8% | -46.27 to -33.44 | yes: GAIN |
| response time (ms), 95th percentile | 469.7 | 494.8 | +5.3% | -5.805 to +55.92 | no |
| response time (ms), 99th percentile | 621.8 | 650.1 | +4.5% | +6.713 to +49.82 | yes: LOSS |
| time over the response line (% of samples) | 5.064 | 5.459 | +7.8% | -0.8274 to +1.617 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 8.3 | +22.1% | -0.385 to +3.385 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 | +41.2 (native is 0) | +24.73 to +57.67 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.885 | 7.367 | -6.6% | -2.444 to +1.407 | no |
| utilisation (used / allocatable) | 0.06149 | 0.071 | +15.5% | +0.003067 to +0.01596 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.476 | 1.439 | -2.5% | -0.1408 to +0.06815 | no |
| Omni's own CPU (cores), mean | 0 | 0.01963 | +0.0196 (native is 0) | +0.01703 to +0.02223 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.476 | 1.459 | -1.1% | -0.1216 to +0.08815 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.1 | 407 | -8.6% | -70.04 to -6.166 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.159 | 2.343 | +8.6% | -0.04241 to +0.4123 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.5 | 1 | +100.0% | -0.8593 to +1.859 | no |
| pod start wait, mean (s) | 0.5 | 0.75 | +50.0% | -0.6925 to +1.192 | no |
| host CPU busy, the real machine under kind (%) | 41.42 | 42.54 | +2.7% | +0.9013 to +1.325 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 721.9 | 722.9 | +0.1% | -0.7521 to +2.752 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.415 | -26.4% | -2.607 to -0.5631 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.025 | 0.03333 | +33.3% | -0.0255 to +0.04217 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 27.32 | 27.65 | +1.2% | +0.1689 to +0.4978 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*