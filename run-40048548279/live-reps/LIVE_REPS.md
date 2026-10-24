# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.569 |
| node-hours | 2.515 | 2.33 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 257 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 286.7 | 262.2 |
| response time (ms), 95th percentile | 1055 | 1161 |
| response time (ms), 99th percentile | 1691 | 1796 |
| time over the response line (% of samples) | 9.507 | 9.298 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.03 | 15.2 |
| utilisation (used / allocatable) | 0.05577 | 0.06019 |
| CPU used (cores), mean | 1.339 | 1.336 |
| Omni's own CPU (cores), mean | 0 | 0.01836 |
| CPU used with Omni's own (cores), mean | 1.339 | 1.354 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.9 | 465.9 |
| HPA replicas, mean | 1.992 | 2.469 |
| pods started | 0.2 | 0.8 |
| pod start wait, total (s) | 0.4 | 1.3 |
| pod start wait, mean (s) | 0.4 | 1.3 |
| host CPU busy, the real machine under kind (%) | 40.11 | 41.18 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 768.9 | 774 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.306 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.8167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 77.71 | 81.62 |
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
| worker nodes in service, mean | 6 | 5.569 | -7.2% | -1 to +0.139 | no |
| node-hours | 2.515 | 2.33 | -7.3% | -0.4214 to +0.05328 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.5 | -0.2% | -1.264 to +0.3546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 257 | -5.2% | -31.67 to +3.626 | no |
| response time (ms), mean | 286.7 | 262.2 | -8.5% | -44.58 to -4.402 | yes: GAIN |
| response time (ms), 95th percentile | 1055 | 1161 | +10.0% | -49.58 to +261 | no |
| response time (ms), 99th percentile | 1691 | 1796 | +6.2% | -125.8 to +335.1 | no |
| time over the response line (% of samples) | 9.507 | 9.298 | -2.2% | -0.9208 to +0.503 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 6.5 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 55.4 | +55.4 (native is 0) | +41.48 to +69.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.03 | 15.2 | +1.1% | -1.402 to +1.725 | no |
| utilisation (used / allocatable) | 0.05577 | 0.06019 | +7.9% | -0.001706 to +0.01055 | no |
| CPU used (cores), mean | 1.339 | 1.336 | -0.2% | -0.02667 to +0.0219 | no |
| Omni's own CPU (cores), mean | 0 | 0.01836 | +0.0184 (native is 0) | +0.01627 to +0.02045 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.339 | 1.354 | +1.2% | -0.007992 to +0.03995 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 494.9 | 465.9 | -5.9% | -73.92 to +16.01 | no |
| HPA replicas, mean | 1.992 | 2.469 | +23.9% | +0.2871 to +0.6666 | yes: power given |
| pods started | 0.2 | 0.8 | +300.0% | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0.4 | 1.3 | +225.0% | -0.02037 to +1.82 | no |
| pod start wait, mean (s) | 0.4 | 1.3 | +225.0% | -0.02037 to +1.82 | no |
| host CPU busy, the real machine under kind (%) | 40.11 | 41.18 | +2.7% | +0.7876 to +1.346 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 768.9 | 774 | +0.7% | -0.2257 to +10.43 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.306 | -11.6% | -1.618 to +0.2301 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.725 | 0.8167 | +12.6% | +0.03239 to +0.1509 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 | +7.1% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 77.71 | 81.62 | +5.0% | -0.4185 to +8.252 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*