# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.915 |
| node-hours | 2.516 | 2.482 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 269.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 141.5 | 105.6 |
| response time (ms), 95th percentile | 239.4 | 226.5 |
| response time (ms), 99th percentile | 338.6 | 334.3 |
| time over the response line (% of samples) | 0.1702 | 0.1933 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1104 | 1121 |
| utilisation (used / allocatable) | 0.05787 | 0.05895 |
| CPU used (cores), mean | 1.389 | 1.397 |
| Omni's own CPU (cores), mean | 0 | 0.01203 |
| CPU used with Omni's own (cores), mean | 1.389 | 1.409 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.4 | 461.4 |
| HPA replicas, mean | 1.964 | 1.991 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.2 |
| host CPU busy, the real machine under kind (%) | 43.41 | 44.36 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1422 | 1422 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.879 |
| queue: job wait, submitted to its first pod running, mean (s) | 166.4 | 157.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 654.5 | 596.8 |
| queue: job turnaround, submitted to done, mean (s) | 816.9 | 814 |
| queue: jobs unfinished at the window's end | 11.2 | 10 |

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
| worker nodes in service, mean | 6 | 5.915 | -1.4% | -0.2697 to +0.09952 | no |
| node-hours | 2.516 | 2.482 | -1.3% | -0.1101 to +0.04286 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.9 | +0.2% | -0.3686 to +1.195 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 269.2 | -0.8% | -8.021 to +3.502 | no |
| response time (ms), mean | 141.5 | 105.6 | -25.4% | -42.57 to -29.24 | yes: GAIN |
| response time (ms), 95th percentile | 239.4 | 226.5 | -5.4% | -26.98 to +1.267 | no |
| response time (ms), 99th percentile | 338.6 | 334.3 | -1.2% | -25.29 to +16.86 | no |
| time over the response line (% of samples) | 0.1702 | 0.1933 | +13.5% | -0.09302 to +0.1391 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.6 | +12.6 (native is 0) | +10.07 to +15.13 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1104 | 1121 | +1.5% | -45.25 to +79.3 | no |
| utilisation (used / allocatable) | 0.05787 | 0.05895 | +1.9% | -0.0004917 to +0.002657 | no |
| CPU used (cores), mean | 1.389 | 1.397 | +0.6% | -0.01421 to +0.03124 | no |
| Omni's own CPU (cores), mean | 0 | 0.01203 | +0.012 (native is 0) | +0.01079 to +0.01327 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.389 | 1.409 | +1.5% | -0.002212 to +0.0433 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.4 | 461.4 | -1.7% | -19.71 to +3.799 | no |
| HPA replicas, mean | 1.964 | 1.991 | +1.4% | -0.04371 to +0.09809 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 43.41 | 44.36 | +2.2% | +0.01985 to +1.866 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1422 | 1422 | +0.1% | -4.169 to +6.169 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.879 | -18.7% | -12.98 to +10.74 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 166.4 | 157.2 | -5.5% | -68.23 to +49.88 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 654.5 | 596.8 | -8.8% | -283.6 to +168.2 | no |
| queue: job turnaround, submitted to done, mean (s) | 816.9 | 814 | -0.3% | -44.23 to +38.58 | no |
| queue: jobs unfinished at the window's end | 11.2 | 10 | -10.7% | -2.946 to +0.5456 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*