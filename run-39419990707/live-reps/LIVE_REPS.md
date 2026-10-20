# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.055 |
| node-hours | 2.516 | 2.118 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 242.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 315.2 | 283.9 |
| response time (ms), 95th percentile | 1210 | 1277 |
| response time (ms), 99th percentile | 1865 | 1964 |
| time over the response line (% of samples) | 12.56 | 12.28 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.73 | 17.89 |
| utilisation (used / allocatable) | 0.05931 | 0.07021 |
| CPU used (cores), mean | 1.424 | 1.424 |
| Omni's own CPU (cores), mean | 0 | 0.01822 |
| CPU used with Omni's own (cores), mean | 1.424 | 1.442 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484 | 416.1 |
| HPA replicas, mean | 2.026 | 2.117 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.2 | 1.5 |
| pod start wait, mean (s) | 0.2 | 1.5 |
| host CPU busy, the real machine under kind (%) | 42.18 | 42.7 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 811.3 | 811.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.317 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.825 | 0.7875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 123.5 | 122.6 |
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
| worker nodes in service, mean | 6 | 5.055 | -15.8% | -1.698 to -0.1926 | yes: GAIN |
| node-hours | 2.516 | 2.118 | -15.8% | -0.7164 to -0.08018 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.3 | -0.0% | -0.7733 to +0.6881 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 242.6 | -10.9% | -53.42 to -6.177 | yes: GAIN |
| response time (ms), mean | 315.2 | 283.9 | -9.9% | -50.44 to -12.22 | yes: GAIN |
| response time (ms), 95th percentile | 1210 | 1277 | +5.5% | -45.89 to +179.9 | no |
| response time (ms), 99th percentile | 1865 | 1964 | +5.3% | -114.4 to +311.9 | no |
| time over the response line (% of samples) | 12.56 | 12.28 | -2.2% | -0.9212 to +0.3576 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.5 | +2.4% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.9 | +38.9 (native is 0) | +26.36 to +51.44 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.73 | 17.89 | -9.3% | -4.331 to +0.6573 | no |
| utilisation (used / allocatable) | 0.05931 | 0.07021 | +18.4% | +0.001715 to +0.02007 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.424 | 1.424 | +0.0% | -0.02292 to +0.02382 | no |
| Omni's own CPU (cores), mean | 0 | 0.01822 | +0.0182 (native is 0) | +0.01502 to +0.02142 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.424 | 1.442 | +1.3% | -0.004162 to +0.0415 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484 | 416.1 | -14.0% | -128.4 to -7.52 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.117 | +4.5% | -0.05293 to +0.2348 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0.2 | 1.5 | +650.0% | -0.2471 to +2.847 | no |
| pod start wait, mean (s) | 0.2 | 1.5 | +650.0% | -0.2471 to +2.847 | no |
| host CPU busy, the real machine under kind (%) | 42.18 | 42.7 | +1.2% | +0.1984 to +0.8475 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 811.3 | 811.4 | +0.0% | -4.077 to +4.277 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.317 | -28.1% | -2.919 to -0.448 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.825 | 0.7875 | -4.5% | -0.1651 to +0.09008 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 1.6 | -23.8% | -1.68 to +0.6802 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.5 | 122.6 | -0.8% | -4.828 to +2.953 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*