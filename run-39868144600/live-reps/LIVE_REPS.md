# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.957 |
| node-hours | 2.511 | 2.076 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 238.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 215.5 | 203.5 |
| response time (ms), 95th percentile | 561.9 | 696.2 |
| response time (ms), 99th percentile | 953.6 | 1236 |
| time over the response line (% of samples) | 8.382 | 8.495 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.29 | 15.11 |
| utilisation (used / allocatable) | 0.05762 | 0.06929 |
| CPU used (cores), mean | 1.383 | 1.361 |
| Omni's own CPU (cores), mean | 0 | 0.04633 |
| CPU used with Omni's own (cores), mean | 1.383 | 1.407 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483 | 422.4 |
| HPA replicas, mean | 2.007 | 2.478 |
| pods started | 0 | 0.5 |
| pod start wait, total (s) | 0 | 1.1 |
| pod start wait, mean (s) | 0 | 0.65 |
| host CPU busy, the real machine under kind (%) | 39.88 | 41.98 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 772 | 777.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.133 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7083 | 0.6583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 84.85 | 88.12 |
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
| worker nodes in service, mean | 6 | 4.957 | -17.4% | -1.792 to -0.2935 | yes: GAIN |
| node-hours | 2.511 | 2.076 | -17.3% | -0.7499 to -0.1201 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.1 | +0.0% | -0.9259 to +0.9688 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 238.3 | -12.1% | -56.52 to -9.014 | yes: GAIN |
| response time (ms), mean | 215.5 | 203.5 | -5.6% | -28.6 to +4.513 | no |
| response time (ms), 95th percentile | 561.9 | 696.2 | +23.9% | -14.87 to +283.6 | no |
| response time (ms), 99th percentile | 953.6 | 1236 | +29.6% | -5.661 to +570.5 | no |
| time over the response line (% of samples) | 8.382 | 8.495 | +1.3% | -0.6652 to +0.8914 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.9 | +3.0% | -0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.5 | +106 (native is 0) | +54.05 to +159 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.29 | 15.11 | +13.7% | -0.1326 to +3.763 | no |
| utilisation (used / allocatable) | 0.05762 | 0.06929 | +20.3% | +0.002248 to +0.02109 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.383 | 1.361 | -1.6% | -0.06547 to +0.0214 | no |
| Omni's own CPU (cores), mean | 0 | 0.04633 | +0.0463 (native is 0) | +0.03902 to +0.05364 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.383 | 1.407 | +1.8% | -0.01955 to +0.06814 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483 | 422.4 | -12.5% | -109.2 to -11.87 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.007 | 2.478 | +23.5% | +0.137 to +0.8051 | yes: power given |
| pods started | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | -0.2676 to +2.468 | no |
| pod start wait, mean (s) | 0 | 0.65 | +0.65 (native is 0) | -0.1049 to +1.405 | no |
| host CPU busy, the real machine under kind (%) | 39.88 | 41.98 | +5.3% | +1.567 to +2.635 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 772 | 777.2 | +0.7% | -1.107 to +11.51 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.133 | -31.1% | -3.156 to -0.5783 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7083 | 0.6583 | -7.1% | -0.1568 to +0.05682 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.4 | +16.7% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.85 | 88.12 | +3.9% | -2.661 to +9.219 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*