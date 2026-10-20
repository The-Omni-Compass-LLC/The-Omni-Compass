# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.996 |
| node-hours | 2.516 | 2.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 121.3 | 76.33 |
| response time (ms), 95th percentile | 189.9 | 142.6 |
| response time (ms), 99th percentile | 246.6 | 209.6 |
| time over the response line (% of samples) | 0.02305 | 0.02925 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 918.8 | 965.3 |
| utilisation (used / allocatable) | 0.05916 | 0.05888 |
| CPU used (cores), mean | 1.42 | 1.412 |
| Omni's own CPU (cores), mean | 0 | 0.01189 |
| CPU used with Omni's own (cores), mean | 1.42 | 1.424 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.9 | 459.6 |
| HPA replicas, mean | 2.01 | 2.014 |
| pods started | 0.1 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.65 |
| host CPU busy, the real machine under kind (%) | 44.26 | 44.31 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1436 | 1418 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.95 |
| queue: job wait, submitted to its first pod running, mean (s) | 141 | 123.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 677.9 | 574.5 |
| queue: job turnaround, submitted to done, mean (s) | 702.9 | 741.8 |
| queue: jobs unfinished at the window's end | 5 | 6.8 |

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
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01101 to +0.002233 | no |
| node-hours | 2.516 | 2.509 | -0.3% | -0.01789 to +0.00322 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.2 | -0.3% | -1.957 to +0.3483 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.1 | -0.3% | -2.162 to +0.2785 | no |
| response time (ms), mean | 121.3 | 76.33 | -37.1% | -54.43 to -35.49 | yes: GAIN |
| response time (ms), 95th percentile | 189.9 | 142.6 | -24.9% | -55.35 to -39.21 | yes: GAIN |
| response time (ms), 99th percentile | 246.6 | 209.6 | -15.0% | -57.13 to -16.96 | yes: GAIN |
| time over the response line (% of samples) | 0.02305 | 0.02925 | +26.9% | -0.03976 to +0.05216 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 | +13.2 (native is 0) | +11.36 to +15.04 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 918.8 | 965.3 | +5.1% | -49.22 to +142.1 | no |
| utilisation (used / allocatable) | 0.05916 | 0.05888 | -0.5% | -0.00174 to +0.001174 | no |
| CPU used (cores), mean | 1.42 | 1.412 | -0.5% | -0.04242 to +0.02691 | no |
| Omni's own CPU (cores), mean | 0 | 0.01189 | +0.0119 (native is 0) | +0.0108 to +0.01298 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.42 | 1.424 | +0.3% | -0.03016 to +0.03842 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.9 | 459.6 | +0.4% | -8.09 to +11.47 | no |
| HPA replicas, mean | 2.01 | 2.014 | +0.2% | -0.1122 to +0.1216 | no |
| pods started | 0.1 | 0.5 | +400.0% | -0.2032 to +1.003 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | -0.6081 to +2.008 | no |
| pod start wait, mean (s) | 0.2 | 0.65 | +225.0% | -0.4493 to +1.349 | no |
| host CPU busy, the real machine under kind (%) | 44.26 | 44.31 | +0.1% | -0.7673 to +0.8655 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1436 | 1418 | -1.2% | -80.03 to +45.43 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.917 | -1.4% | -0.2626 to +0.09596 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 141 | 123.3 | -12.6% | -42 to +6.495 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 677.9 | 574.5 | -15.3% | -293.9 to +87.06 | no |
| queue: job turnaround, submitted to done, mean (s) | 702.9 | 741.8 | +5.5% | -20.27 to +98.17 | no |
| queue: jobs unfinished at the window's end | 5 | 6.8 | +36.0% | -0.3273 to +3.927 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*