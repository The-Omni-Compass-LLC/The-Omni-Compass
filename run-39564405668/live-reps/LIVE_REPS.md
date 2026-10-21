# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.381 |
| node-hours | 2.516 | 2.255 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 254.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 406.9 | 365 |
| response time (ms), 95th percentile | 1555 | 1540 |
| response time (ms), 99th percentile | 2516 | 2439 |
| time over the response line (% of samples) | 16.54 | 15.11 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.38 | 23 |
| utilisation (used / allocatable) | 0.06542 | 0.07205 |
| CPU used (cores), mean | 1.57 | 1.555 |
| Omni's own CPU (cores), mean | 0 | 0.01757 |
| CPU used with Omni's own (cores), mean | 1.57 | 1.573 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.8 | 397.2 |
| HPA replicas, mean | 2 | 2.179 |
| pods started | 0.2 | 0.5 |
| pod start wait, total (s) | 0.4 | 1.1 |
| pod start wait, mean (s) | 0.4 | 0.85 |
| host CPU busy, the real machine under kind (%) | 45.5 | 46.43 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 845 | 847.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.934 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.012 | 0.9333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 2.9 |
| queue: job turnaround, submitted to done, mean (s) | 159.2 | 161.1 |
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
| worker nodes in service, mean | 6 | 5.381 | -10.3% | -1.292 to +0.05377 | no |
| node-hours | 2.516 | 2.255 | -10.4% | -0.5406 to +0.01863 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.2 | -0.1% | -1.005 to +0.3194 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 254.8 | -7.2% | -41.16 to +1.627 | no |
| response time (ms), mean | 406.9 | 365 | -10.3% | -63.14 to -20.6 | yes: GAIN |
| response time (ms), 95th percentile | 1555 | 1540 | -0.9% | -174.3 to +145.2 | no |
| response time (ms), 99th percentile | 2516 | 2439 | -3.1% | -230.6 to +75.83 | no |
| time over the response line (% of samples) | 16.54 | 15.11 | -8.6% | -3.064 to +0.204 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.2 | -1.0% | -0.7263 to +0.5263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.4 | +41.4 (native is 0) | +14.21 to +68.59 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.38 | 23 | -1.6% | -2.709 to +1.956 | no |
| utilisation (used / allocatable) | 0.06542 | 0.07205 | +10.1% | +0.0001363 to +0.01311 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.57 | 1.555 | -1.0% | -0.05765 to +0.02746 | no |
| Omni's own CPU (cores), mean | 0 | 0.01757 | +0.0176 (native is 0) | +0.01562 to +0.01952 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.57 | 1.573 | +0.2% | -0.0398 to +0.04475 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.8 | 397.2 | -7.4% | -62.39 to -0.9751 | yes, down (shown, not judged) |
| HPA replicas, mean | 2 | 2.179 | +9.0% | -0.03611 to +0.3944 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.4 | 1.1 | +175.0% | -0.6081 to +2.008 | no |
| pod start wait, mean (s) | 0.4 | 0.85 | +112.5% | -0.4493 to +1.349 | no |
| host CPU busy, the real machine under kind (%) | 45.5 | 46.43 | +2.0% | +0.6038 to +1.248 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 845 | 847.9 | +0.3% | -1.753 to +7.553 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.934 | -17.8% | -2.123 to -0.00961 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.012 | 0.9333 | -7.8% | -0.2863 to +0.128 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 2.9 | +20.8% | -2.366 to +3.366 | no |
| queue: job turnaround, submitted to done, mean (s) | 159.2 | 161.1 | +1.2% | -3.061 to +6.953 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*