# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.697 |
| node-hours | 2.516 | 1.969 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.3 | 269.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.3 | 228.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 171 | 152.8 |
| response time (ms), 95th percentile | 536.8 | 618.4 |
| response time (ms), 99th percentile | 807.8 | 909 |
| time over the response line (% of samples) | 5.134 | 5.002 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.7 | 3.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 119.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.445 | 8.51 |
| utilisation (used / allocatable) | 0.05076 | 0.06459 |
| CPU used (cores), mean | 1.218 | 1.204 |
| Omni's own CPU (cores), mean | 0 | 0.04023 |
| CPU used with Omni's own (cores), mean | 1.218 | 1.244 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 536.1 | 456.8 |
| HPA replicas, mean | 2.003 | 2.295 |
| pods started | 0 | 1 |
| pod start wait, total (s) | 0 | 1.8 |
| pod start wait, mean (s) | 0 | 0.85 |
| host CPU busy, the real machine under kind (%) | 34.58 | 36.41 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 734.3 | 738.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.602 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.04583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 42.19 | 46.5 |
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
| worker nodes in service, mean | 6 | 4.697 | -21.7% | -1.931 to -0.6743 | yes: GAIN |
| node-hours | 2.516 | 1.969 | -21.7% | -0.809 to -0.2851 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.3 | 269.2 | -0.1% | -1.025 to +0.7549 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.3 | 228.2 | -15.3% | -60.98 to -21.25 | yes: GAIN |
| response time (ms), mean | 171 | 152.8 | -10.7% | -25.85 to -10.58 | yes: GAIN |
| response time (ms), 95th percentile | 536.8 | 618.4 | +15.2% | -54.22 to +217.3 | no |
| response time (ms), 99th percentile | 807.8 | 909 | +12.5% | -62.01 to +264.4 | no |
| time over the response line (% of samples) | 5.134 | 5.002 | -2.6% | -0.4598 to +0.1968 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.7 | 3.7 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 119.3 | +119 (native is 0) | +96.08 to +142.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.445 | 8.51 | +0.8% | -2.154 to +2.284 | no |
| utilisation (used / allocatable) | 0.05076 | 0.06459 | +27.2% | +0.006232 to +0.02142 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.218 | 1.204 | -1.2% | -0.04876 to +0.01986 | no |
| Omni's own CPU (cores), mean | 0 | 0.04023 | +0.0402 (native is 0) | +0.03261 to +0.04785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.218 | 1.244 | +2.1% | -0.01523 to +0.06679 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 536.1 | 456.8 | -14.8% | -115.2 to -43.36 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.295 | +14.6% | -0.1917 to +0.777 | no |
| pods started | 0 | 1 | +1 (native is 0) | +0.04626 to +1.954 | yes: power given |
| pod start wait, total (s) | 0 | 1.8 | +1.8 (native is 0) | -0.07138 to +3.671 | no |
| pod start wait, mean (s) | 0 | 0.85 | +0.85 (native is 0) | +0.1745 to +1.525 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 34.58 | 36.41 | +5.3% | +1.183 to +2.459 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 734.3 | 738.7 | +0.6% | -1.364 to +10.16 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.602 | -40.0% | -3.49 to -1.305 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.04583 | +22.2% | -0.02245 to +0.03912 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 42.19 | 46.5 | +10.2% | -1.472 to +10.09 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*