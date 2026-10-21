# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.547 |
| node-hours | 2.512 | 2.327 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 261.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 386.2 | 369.3 |
| response time (ms), 95th percentile | 1429 | 1637 |
| response time (ms), 99th percentile | 2418 | 2574 |
| time over the response line (% of samples) | 16.46 | 16.8 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 12.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.83 | 19.42 |
| utilisation (used / allocatable) | 0.0676 | 0.0728 |
| CPU used (cores), mean | 1.622 | 1.603 |
| Omni's own CPU (cores), mean | 0 | 0.01823 |
| CPU used with Omni's own (cores), mean | 1.622 | 1.621 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 408.5 | 390.1 |
| HPA replicas, mean | 2.046 | 2.416 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.3 | 1.9 |
| pod start wait, mean (s) | 0.3 | 1.7 |
| host CPU busy, the real machine under kind (%) | 47.1 | 47.64 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 844.2 | 841.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.07 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.875 | 0.8292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 159.2 | 158 |
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
| worker nodes in service, mean | 6 | 5.547 | -7.5% | -0.9258 to +0.02005 | no |
| node-hours | 2.512 | 2.328 | -7.3% | -0.3844 to +0.01611 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275.3 | +0.1% | -0.1858 to +1 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 261.1 | -5.0% | -28.75 to +1.114 | no |
| response time (ms), mean | 386.2 | 369.3 | -4.4% | -48.29 to +14.64 | no |
| response time (ms), 95th percentile | 1429 | 1637 | +14.5% | -51.83 to +466.2 | no |
| response time (ms), 99th percentile | 2418 | 2574 | +6.5% | -31.11 to +344 | no |
| time over the response line (% of samples) | 16.46 | 16.8 | +2.0% | -1.513 to +2.182 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.1 | 12.6 | +4.1% | -0.4685 to +1.469 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.7 | +32.7 (native is 0) | +20.7 to +44.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.83 | 19.42 | -2.1% | -2.88 to +2.063 | no |
| utilisation (used / allocatable) | 0.0676 | 0.0728 | +7.7% | -0.001515 to +0.01191 | no |
| CPU used (cores), mean | 1.622 | 1.603 | -1.2% | -0.03506 to -0.004386 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01823 | +0.0182 (native is 0) | +0.01685 to +0.01961 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.622 | 1.621 | -0.1% | -0.01638 to +0.0134 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 408.5 | 390.1 | -4.5% | -45.4 to +8.502 | no |
| HPA replicas, mean | 2.046 | 2.416 | +18.1% | +0.2069 to +0.534 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | -0.1079 to +1.108 | no |
| pod start wait, total (s) | 0.3 | 1.9 | +533.3% | -0.3134 to +3.513 | no |
| pod start wait, mean (s) | 0.3 | 1.7 | +466.7% | -0.4221 to +3.222 | no |
| host CPU busy, the real machine under kind (%) | 47.1 | 47.64 | +1.1% | +0.1519 to +0.9187 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 844.2 | 841.2 | -0.4% | -7.672 to +1.672 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.07 | -15.5% | -1.819 to -0.04037 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.875 | 0.8292 | -5.2% | -0.1662 to +0.07458 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 1.5 | -21.1% | -1.169 to +0.3689 | no |
| queue: job turnaround, submitted to done, mean (s) | 159.2 | 158 | -0.7% | -6.87 to +4.62 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*