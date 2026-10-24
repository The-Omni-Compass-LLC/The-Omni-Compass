# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.773 |
| node-hours | 2.514 | 2.002 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 232.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 196 | 167.7 |
| response time (ms), 95th percentile | 457.9 | 515.5 |
| response time (ms), 99th percentile | 725.3 | 840.2 |
| time over the response line (% of samples) | 6.068 | 6.391 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.43 | 12.8 |
| utilisation (used / allocatable) | 0.05587 | 0.06999 |
| CPU used (cores), mean | 1.341 | 1.323 |
| Omni's own CPU (cores), mean | 0 | 0.01694 |
| CPU used with Omni's own (cores), mean | 1.341 | 1.34 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 422.3 |
| HPA replicas, mean | 2.024 | 2.263 |
| pods started | 0.2 | 0.2 |
| pod start wait, total (s) | 0.4 | 0.8 |
| pod start wait, mean (s) | 0.4 | 0.8 |
| host CPU busy, the real machine under kind (%) | 39.18 | 40.01 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 759.5 | 766.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.909 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6583 | 0.6583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 72.35 | 77.58 |
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
| worker nodes in service, mean | 6 | 4.773 | -20.4% | -2.027 to -0.4266 | yes: GAIN |
| node-hours | 2.514 | 2.002 | -20.4% | -0.853 to -0.172 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.9 | +0.0% | -1.02 to +1.189 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 232.3 | -14.2% | -64.37 to -12.6 | yes: GAIN |
| response time (ms), mean | 196 | 167.7 | -14.4% | -41.17 to -15.29 | yes: GAIN |
| response time (ms), 95th percentile | 457.9 | 515.5 | +12.6% | -35.82 to +151.1 | no |
| response time (ms), 99th percentile | 725.3 | 840.2 | +15.8% | -70.32 to +300.2 | no |
| time over the response line (% of samples) | 6.068 | 6.391 | +5.3% | -0.8433 to +1.49 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 6.9 | +7.8% | -0.4079 to +1.408 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.1 | +41.1 (native is 0) | +23.33 to +58.87 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.43 | 12.8 | -11.3% | -3.477 to +0.2202 | no |
| utilisation (used / allocatable) | 0.05587 | 0.06999 | +25.3% | +0.005015 to +0.02322 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.341 | 1.323 | -1.3% | -0.06056 to +0.02536 | no |
| Omni's own CPU (cores), mean | 0 | 0.01694 | +0.0169 (native is 0) | +0.01396 to +0.01992 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.341 | 1.34 | -0.0% | -0.04469 to +0.04337 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.9 | 422.3 | -14.8% | -122.4 to -24.71 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.024 | 2.263 | +11.8% | +0.02693 to +0.4527 | yes: power given |
| pods started | 0.2 | 0.2 | +0.0% | -0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.4 | 0.8 | +100.0% | -1.116 to +1.916 | no |
| pod start wait, mean (s) | 0.4 | 0.8 | +100.0% | -1.116 to +1.916 | no |
| host CPU busy, the real machine under kind (%) | 39.18 | 40.01 | +2.1% | +0.1829 to +1.484 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.5 | 766.3 | +0.9% | +1.733 to +11.87 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.909 | -34.9% | -3.345 to -0.8371 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6583 | 0.6583 | +0.0% | -0.04443 to +0.04443 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.1 | +10.0% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.35 | 77.58 | +7.2% | -1.526 to +11.99 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*