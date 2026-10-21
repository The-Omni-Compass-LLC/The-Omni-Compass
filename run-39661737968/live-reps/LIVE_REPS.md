# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.916 |
| node-hours | 2.513 | 2.477 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 268.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 138.3 | 104.9 |
| response time (ms), 95th percentile | 232.3 | 229.8 |
| response time (ms), 99th percentile | 341.2 | 346.2 |
| time over the response line (% of samples) | 0.2163 | 0.2464 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1125 | 1179 |
| utilisation (used / allocatable) | 0.05875 | 0.05855 |
| CPU used (cores), mean | 1.41 | 1.389 |
| Omni's own CPU (cores), mean | 0 | 0.01236 |
| CPU used with Omni's own (cores), mean | 1.41 | 1.401 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.9 | 465.1 |
| HPA replicas, mean | 2.029 | 2.029 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.18 | 44.35 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1423 | 1423 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.902 |
| queue: job wait, submitted to its first pod running, mean (s) | 141.5 | 157.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 728.1 | 745 |
| queue: job turnaround, submitted to done, mean (s) | 839.1 | 860.8 |
| queue: jobs unfinished at the window's end | 12.2 | 12.4 |

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
| worker nodes in service, mean | 6 | 5.916 | -1.4% | -0.2693 to +0.1008 | no |
| node-hours | 2.513 | 2.477 | -1.4% | -0.1194 to +0.0474 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.1 | -0.1% | -1.691 to +0.994 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 268.5 | -1.1% | -9.342 to +3.37 | no |
| response time (ms), mean | 138.3 | 104.9 | -24.2% | -39.54 to -27.27 | yes: GAIN |
| response time (ms), 95th percentile | 232.3 | 229.8 | -1.1% | -18.09 to +13.06 | no |
| response time (ms), 99th percentile | 341.2 | 346.2 | +1.5% | -25.56 to +35.59 | no |
| time over the response line (% of samples) | 0.2163 | 0.2464 | +13.9% | -0.102 to +0.1622 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.4 | +12.4 (native is 0) | +9.615 to +15.18 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1125 | 1179 | +4.8% | -17.64 to +124.6 | no |
| utilisation (used / allocatable) | 0.05875 | 0.05855 | -0.3% | -0.002289 to +0.001886 | no |
| CPU used (cores), mean | 1.41 | 1.389 | -1.5% | -0.05205 to +0.009467 | no |
| Omni's own CPU (cores), mean | 0 | 0.01236 | +0.0124 (native is 0) | +0.01152 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.401 | -0.6% | -0.03965 to +0.02178 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.9 | 465.1 | +0.0% | -16.48 to +16.82 | no |
| HPA replicas, mean | 2.029 | 2.029 | -0.0% | -0.1508 to +0.1507 | no |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.5048 to +1.305 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.18 | 44.35 | +0.4% | -0.8024 to +1.129 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1423 | 1423 | +0.0% | -8.572 to +8.972 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.902 | -18.3% | -13.24 to +11.04 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 141.5 | 157.8 | +11.6% | -18.15 to +50.9 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 728.1 | 745 | +2.3% | -171.3 to +205.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 839.1 | 860.8 | +2.6% | -10.43 to +53.79 | no |
| queue: jobs unfinished at the window's end | 12.2 | 12.4 | +1.6% | -2.408 to +2.808 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*