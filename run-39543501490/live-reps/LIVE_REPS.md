# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.927 |
| node-hours | 2.516 | 2.068 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 238.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 248.6 | 227.9 |
| response time (ms), 95th percentile | 890 | 944 |
| response time (ms), 99th percentile | 1422 | 1531 |
| time over the response line (% of samples) | 9.057 | 9.211 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.78 | 13.91 |
| utilisation (used / allocatable) | 0.05776 | 0.07036 |
| CPU used (cores), mean | 1.386 | 1.381 |
| Omni's own CPU (cores), mean | 0 | 0.01851 |
| CPU used with Omni's own (cores), mean | 1.386 | 1.399 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.6 | 423.5 |
| HPA replicas, mean | 2.025 | 2.284 |
| pods started | 0.4 | 0.5 |
| pod start wait, total (s) | 1.1 | 1.3 |
| pod start wait, mean (s) | 1 | 1.3 |
| host CPU busy, the real machine under kind (%) | 40.53 | 41.6 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 783.8 | 787.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.134 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7417 | 0.6708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 93.77 | 97.65 |
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
| worker nodes in service, mean | 6 | 4.927 | -17.9% | -1.826 to -0.3205 | yes: GAIN |
| node-hours | 2.516 | 2.068 | -17.8% | -0.7637 to -0.1328 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.9 | +0.1% | -0.8948 to +1.308 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 238.2 | -12.3% | -57.46 to -9.648 | yes: GAIN |
| response time (ms), mean | 248.6 | 227.9 | -8.3% | -38.59 to -2.895 | yes: GAIN |
| response time (ms), 95th percentile | 890 | 944 | +6.1% | -90.52 to +198.5 | no |
| response time (ms), 99th percentile | 1422 | 1531 | +7.7% | -37.19 to +256.5 | no |
| time over the response line (% of samples) | 9.057 | 9.211 | +1.7% | -1.621 to +1.931 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.7 | +0.0% | -0.584 to +0.584 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.4 | +52.4 (native is 0) | +28.01 to +76.79 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.78 | 13.91 | +1.0% | -1.443 to +1.713 | no |
| utilisation (used / allocatable) | 0.05776 | 0.07036 | +21.8% | +0.003397 to +0.02179 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.386 | 1.381 | -0.4% | -0.06044 to +0.04904 | no |
| Omni's own CPU (cores), mean | 0 | 0.01851 | +0.0185 (native is 0) | +0.01672 to +0.0203 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.386 | 1.399 | +0.9% | -0.04198 to +0.0676 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 484.6 | 423.5 | -12.6% | -107.1 to -15.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.284 | +12.8% | +0.04539 to +0.4714 | yes: power given |
| pods started | 0.4 | 0.5 | +25.0% | -0.6113 to +0.8113 | no |
| pod start wait, total (s) | 1.1 | 1.3 | +18.2% | -1.546 to +1.946 | no |
| pod start wait, mean (s) | 1 | 1.3 | +30.0% | -1.388 to +1.988 | no |
| host CPU busy, the real machine under kind (%) | 40.53 | 41.6 | +2.6% | +0.6052 to +1.525 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 783.8 | 787.4 | +0.5% | -1.171 to +8.371 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.134 | -31.1% | -3.093 to -0.6385 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7417 | 0.6708 | -9.6% | -0.195 to +0.05329 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.3 | +8.3% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.77 | 97.65 | +4.1% | +0.5255 to +7.233 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*