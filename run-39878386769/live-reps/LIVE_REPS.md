# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.264 |
| node-hours | 2.517 | 2.206 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 249.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 357.6 | 326.2 |
| response time (ms), 95th percentile | 1443 | 1491 |
| response time (ms), 99th percentile | 2364 | 2416 |
| time over the response line (% of samples) | 14.84 | 14.17 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.41 | 15.87 |
| utilisation (used / allocatable) | 0.05912 | 0.06985 |
| CPU used (cores), mean | 1.419 | 1.44 |
| Omni's own CPU (cores), mean | 0 | 0.05456 |
| CPU used with Omni's own (cores), mean | 1.419 | 1.494 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.7 | 412.6 |
| HPA replicas, mean | 2.004 | 2.752 |
| pods started | 0.1 | 2.1 |
| pod start wait, total (s) | 0.2 | 4 |
| pod start wait, mean (s) | 0.2 | 1.298 |
| host CPU busy, the real machine under kind (%) | 42.86 | 45.14 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 793.4 | 798.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.761 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8125 | 0.7458 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 102.1 | 108.7 |
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
| worker nodes in service, mean | 6 | 5.264 | -12.3% | -1.472 to -0.0001398 | yes: GAIN |
| node-hours | 2.517 | 2.206 | -12.3% | -0.6172 to -0.004082 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 | +0.0% | -1.056 to +1.162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 249.3 | -8.5% | -45.84 to -0.3447 | yes: GAIN |
| response time (ms), mean | 357.6 | 326.2 | -8.8% | -63.51 to +0.6932 | no |
| response time (ms), 95th percentile | 1443 | 1491 | +3.3% | -158.6 to +253.3 | no |
| response time (ms), 99th percentile | 2364 | 2416 | +2.2% | -203.3 to +306.8 | no |
| time over the response line (% of samples) | 14.84 | 14.17 | -4.6% | -2.713 to +1.359 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 9.7 | -1.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.3 | +103 (native is 0) | +88.03 to +118.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.41 | 15.87 | -3.3% | -2.622 to +1.532 | no |
| utilisation (used / allocatable) | 0.05912 | 0.06985 | +18.1% | -0.0006323 to +0.02209 | no |
| CPU used (cores), mean | 1.419 | 1.44 | +1.5% | -0.009832 to +0.05199 | no |
| Omni's own CPU (cores), mean | 0 | 0.05456 | +0.0546 (native is 0) | +0.04844 to +0.06068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.419 | 1.494 | +5.3% | +0.04883 to +0.1025 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.7 | 412.6 | -11.6% | -109.5 to +1.392 | no |
| HPA replicas, mean | 2.004 | 2.752 | +37.4% | +0.4023 to +1.095 | yes: power given |
| pods started | 0.1 | 2.1 | +2000.0% | +0.6097 to +3.39 | yes: power given |
| pod start wait, total (s) | 0.2 | 4 | +1900.0% | +0.8642 to +6.736 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.298 | +549.2% | +0.1279 to +2.069 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.86 | 45.14 | +5.3% | +1.834 to +2.739 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 793.4 | 798.9 | +0.7% | -0.9001 to +11.9 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.761 | -20.6% | -2.401 to -0.07621 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8125 | 0.7458 | -8.2% | -0.1652 to +0.03188 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.3 | -18.8% | -0.6455 to +0.04553 | no |
| queue: job turnaround, submitted to done, mean (s) | 102.1 | 108.7 | +6.5% | +0.7302 to +12.47 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*