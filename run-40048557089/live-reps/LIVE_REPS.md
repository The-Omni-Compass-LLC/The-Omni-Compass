# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.164 |
| node-hours | 2.514 | 2.164 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 244.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 306.4 | 280.3 |
| response time (ms), 95th percentile | 1196 | 1262 |
| response time (ms), 99th percentile | 1947 | 1915 |
| time over the response line (% of samples) | 11.38 | 12.03 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.7 | 15.81 |
| utilisation (used / allocatable) | 0.05539 | 0.06515 |
| CPU used (cores), mean | 1.329 | 1.328 |
| Omni's own CPU (cores), mean | 0 | 0.01617 |
| CPU used with Omni's own (cores), mean | 1.329 | 1.344 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 506.3 | 445.5 |
| HPA replicas, mean | 1.975 | 2.233 |
| pods started | 0 | 0.8 |
| pod start wait, total (s) | 0 | 1.6 |
| pod start wait, mean (s) | 0 | 1.2 |
| host CPU busy, the real machine under kind (%) | 40.22 | 41.17 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 781.4 | 782.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.657 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7875 | 0.8167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 90.39 | 93 |
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
| worker nodes in service, mean | 6 | 5.164 | -13.9% | -1.691 to +0.01854 | no |
| node-hours | 2.514 | 2.164 | -13.9% | -0.7138 to +0.01294 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.9 | +0.1% | -0.536 to +0.8994 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 244.7 | -9.6% | -53.4 to +1.251 | no |
| response time (ms), mean | 306.4 | 280.3 | -8.5% | -55.03 to +2.665 | no |
| response time (ms), 95th percentile | 1196 | 1262 | +5.5% | -107.4 to +239.7 | no |
| response time (ms), 99th percentile | 1947 | 1915 | -1.6% | -277.3 to +214.7 | no |
| time over the response line (% of samples) | 11.38 | 12.03 | +5.8% | -0.3228 to +1.636 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.2 | 7.8 | +8.3% | -0.5285 to +1.728 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 | +40.7 (native is 0) | +28.29 to +53.11 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.7 | 15.8 | +7.5% | -0.5248 to +2.735 | no |
| utilisation (used / allocatable) | 0.05539 | 0.06515 | +17.6% | -0.0005559 to +0.02007 | no |
| CPU used (cores), mean | 1.329 | 1.328 | -0.1% | -0.01208 to +0.008816 | no |
| Omni's own CPU (cores), mean | 0 | 0.01617 | +0.0162 (native is 0) | +0.01442 to +0.01792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.329 | 1.344 | +1.1% | +0.003418 to +0.02566 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 506.3 | 445.5 | -12.0% | -123.8 to +2.318 | no |
| HPA replicas, mean | 1.975 | 2.233 | +13.1% | +0.04963 to +0.4659 | yes: power given |
| pods started | 0 | 0.8 | +0.8 (native is 0) | +0.2358 to +1.364 | yes: power given |
| pod start wait, total (s) | 0 | 1.6 | +1.6 (native is 0) | +0.3749 to +2.825 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.2 (native is 0) | +0.3207 to +2.079 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.22 | 41.17 | +2.4% | +0.4802 to +1.426 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 781.4 | 782.4 | +0.1% | -3.956 to +5.956 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.657 | -22.4% | -2.665 to -0.02087 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7875 | 0.8167 | +3.7% | -0.05519 to +0.1135 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.4 | -6.7% | -0.506 to +0.306 | no |
| queue: job turnaround, submitted to done, mean (s) | 90.39 | 93 | +2.9% | -3.507 to +8.732 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*