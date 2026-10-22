# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.286 |
| node-hours | 2.513 | 2.212 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 249 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 312.8 | 297.9 |
| response time (ms), 95th percentile | 1041 | 1184 |
| response time (ms), 99th percentile | 1491 | 1730 |
| time over the response line (% of samples) | 15.15 | 15.55 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 157.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.935 | 9.785 |
| utilisation (used / allocatable) | 0.05778 | 0.06628 |
| CPU used (cores), mean | 1.387 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0.05024 |
| CPU used with Omni's own (cores), mean | 1.387 | 1.448 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.7 | 431.6 |
| HPA replicas, mean | 2.015 | 2.52 |
| pods started | 0 | 1.3 |
| pod start wait, total (s) | 0 | 2.8 |
| pod start wait, mean (s) | 0 | 1.4 |
| host CPU busy, the real machine under kind (%) | 40.21 | 42.85 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 772 | 780.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.561 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.2208 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 79.28 | 86.62 |
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
| worker nodes in service, mean | 6 | 5.286 | -11.9% | -1.266 to -0.1614 | yes: GAIN |
| node-hours | 2.513 | 2.212 | -12.0% | -0.5359 to -0.06548 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 | -0.0% | -0.9414 to +0.7929 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 249 | -8.3% | -40.16 to -4.72 | yes: GAIN |
| response time (ms), mean | 312.8 | 297.9 | -4.8% | -28.18 to -1.628 | yes: GAIN |
| response time (ms), 95th percentile | 1041 | 1184 | +13.7% | +45.27 to +239.6 | yes: LOSS |
| response time (ms), 99th percentile | 1491 | 1730 | +16.0% | +25.11 to +452.2 | yes: LOSS |
| time over the response line (% of samples) | 15.15 | 15.55 | +2.7% | -0.4948 to +1.299 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.2 | +6.5% | -0.5796 to +1.58 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 157.7 | +158 (native is 0) | +75.97 to +239.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.935 | 9.785 | +9.5% | -1.014 to +2.714 | no |
| utilisation (used / allocatable) | 0.05778 | 0.06628 | +14.7% | +0.002124 to +0.01487 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.387 | 1.398 | +0.8% | -0.03167 to +0.0547 | no |
| Omni's own CPU (cores), mean | 0 | 0.05024 | +0.0502 (native is 0) | +0.04447 to +0.05601 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.387 | 1.448 | +4.5% | +0.01942 to +0.1041 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.7 | 431.6 | -10.2% | -91.81 to -6.454 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.015 | 2.52 | +25.0% | +0.1577 to +0.8508 | yes: power given |
| pods started | 0 | 1.3 | +1.3 (native is 0) | +0.3433 to +2.257 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.8 (native is 0) | +0.4444 to +5.156 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.4 | +1.4 (native is 0) | +0.5775 to +2.223 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.21 | 42.85 | +6.6% | +2.304 to +2.981 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772 | 780.6 | +1.1% | +1.721 to +15.48 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.561 | -24.0% | -2.518 to -0.3601 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.2208 | +39.5% | +0.01136 to +0.1136 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1 | +25.0% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.28 | 86.62 | +9.3% | +0.962 to +13.73 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*