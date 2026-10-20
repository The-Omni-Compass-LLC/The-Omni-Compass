# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.352 |
| node-hours | 2.517 | 1.825 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 219.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 151.5 | 108.1 |
| response time (ms), 95th percentile | 326.4 | 320.4 |
| response time (ms), 99th percentile | 415.6 | 425.7 |
| time over the response line (% of samples) | 0.5461 | 0.6976 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 1.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.297 | 6.615 |
| utilisation (used / allocatable) | 0.05575 | 0.07857 |
| CPU used (cores), mean | 1.338 | 1.35 |
| Omni's own CPU (cores), mean | 0 | 0.0183 |
| CPU used with Omni's own (cores), mean | 1.338 | 1.368 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.2 | 388.3 |
| HPA replicas, mean | 2.191 | 2.271 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 0.2 | 1 |
| pod start wait, mean (s) | 0.2 | 0.75 |
| host CPU busy, the real machine under kind (%) | 38.57 | 39.39 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 720.3 | 720.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.116 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.03333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 26.39 | 26.66 |
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
| worker nodes in service, mean | 6 | 4.352 | -27.5% | -2.256 to -1.04 | yes: GAIN |
| node-hours | 2.517 | 1.825 | -27.5% | -0.9485 to -0.4342 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.6 | +0.1% | -0.2434 to +0.9754 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 219.8 | -19.0% | -70.62 to -32.32 | yes: GAIN |
| response time (ms), mean | 151.5 | 108.1 | -28.6% | -50.29 to -36.47 | yes: GAIN |
| response time (ms), 95th percentile | 326.4 | 320.4 | -1.8% | -40.06 to +28.12 | no |
| response time (ms), 99th percentile | 415.6 | 425.7 | +2.4% | -14.14 to +34.38 | no |
| time over the response line (% of samples) | 0.5461 | 0.6976 | +27.7% | -0.3433 to +0.6463 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.9 | 1.3 | +44.4% | -1.116 to +1.916 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.7 | +39.7 (native is 0) | +30.4 to +49 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.297 | 6.615 | -9.3% | -3.339 to +1.976 | no |
| utilisation (used / allocatable) | 0.05575 | 0.07857 | +40.9% | +0.0135 to +0.03214 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.338 | 1.35 | +0.9% | -0.01806 to +0.04162 | no |
| Omni's own CPU (cores), mean | 0 | 0.0183 | +0.0183 (native is 0) | +0.01685 to +0.01975 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.338 | 1.368 | +2.2% | +0.0008225 to +0.05934 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.2 | 388.3 | -20.8% | -145.1 to -58.69 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.191 | 2.271 | +3.6% | -0.1373 to +0.2959 | no |
| pods started | 0.2 | 0.4 | +100.0% | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 1 | +400.0% | -0.3583 to +1.958 | no |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | -0.3171 to +1.417 | no |
| host CPU busy, the real machine under kind (%) | 38.57 | 39.39 | +2.1% | +0.6909 to +0.936 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 720.3 | 720.5 | +0.0% | -0.2524 to +0.6524 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.116 | -48.1% | -3.849 to -1.919 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.03333 | +14.3% | -0.01782 to +0.02616 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 26.39 | 26.66 | +1.0% | +0.1044 to +0.4372 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*