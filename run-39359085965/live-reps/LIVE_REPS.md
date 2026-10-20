# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.946 |
| node-hours | 2.514 | 2.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 270.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.8 | 86.64 |
| response time (ms), 95th percentile | 212.3 | 162 |
| response time (ms), 99th percentile | 274.5 | 251.8 |
| time over the response line (% of samples) | 0.04596 | 0.02947 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1091 | 1088 |
| utilisation (used / allocatable) | 0.05964 | 0.06035 |
| CPU used (cores), mean | 1.431 | 1.437 |
| Omni's own CPU (cores), mean | 0 | 0.01274 |
| CPU used with Omni's own (cores), mean | 1.431 | 1.449 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 450.8 |
| HPA replicas, mean | 2.036 | 2.118 |
| pods started | 0.1 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.8 |
| pod start wait, mean (s) | 0.2 | 0.6 |
| host CPU busy, the real machine under kind (%) | 44.99 | 45.32 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1440 | 1420 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.312 |
| queue: job wait, submitted to its first pod running, mean (s) | 147.3 | 140.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 654.8 | 679 |
| queue: job turnaround, submitted to done, mean (s) | 809 | 783.7 |
| queue: jobs unfinished at the window's end | 10.5 | 10.3 |

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
| worker nodes in service, mean | 6 | 5.946 | -0.9% | -0.1383 to +0.03115 | no |
| node-hours | 2.514 | 2.493 | -0.8% | -0.06131 to +0.01859 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.2 | +0.1% | -0.7093 to +1.092 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 270.6 | -0.5% | -4.546 to +1.575 | no |
| response time (ms), mean | 137.8 | 86.64 | -37.1% | -63.17 to -39.18 | yes: GAIN |
| response time (ms), 95th percentile | 212.3 | 162 | -23.7% | -62.08 to -38.59 | yes: GAIN |
| response time (ms), 99th percentile | 274.5 | 251.8 | -8.3% | -37.64 to -7.733 | yes: GAIN |
| time over the response line (% of samples) | 0.04596 | 0.02947 | -35.9% | -0.06641 to +0.03342 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 | +13.2 (native is 0) | +11.59 to +14.81 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1091 | 1088 | -0.2% | -57.3 to +52.47 | no |
| utilisation (used / allocatable) | 0.05964 | 0.06035 | +1.2% | -0.0006448 to +0.002055 | no |
| CPU used (cores), mean | 1.431 | 1.437 | +0.4% | -0.02142 to +0.03165 | no |
| Omni's own CPU (cores), mean | 0 | 0.01274 | +0.0127 (native is 0) | +0.01182 to +0.01366 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.449 | +1.2% | -0.008827 to +0.04453 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 450.8 | -1.0% | -13.26 to +4.365 | no |
| HPA replicas, mean | 2.036 | 2.118 | +4.0% | -0.118 to +0.282 | no |
| pods started | 0.1 | 0.5 | +400.0% | -0.2032 to +1.003 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | -0.5285 to +1.728 | no |
| pod start wait, mean (s) | 0.2 | 0.6 | +200.0% | -0.4396 to +1.24 | no |
| host CPU busy, the real machine under kind (%) | 44.99 | 45.32 | +0.7% | -0.6275 to +1.295 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1440 | 1420 | -1.3% | -48.4 to +9.799 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.969 | -17.2% | -4.191 to +2.129 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 147.3 | 140.4 | -4.7% | -36.81 to +22.94 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 654.8 | 679 | +3.7% | -173.7 to +222.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 809 | 783.7 | -3.1% | -70.33 to +19.74 | no |
| queue: jobs unfinished at the window's end | 10.5 | 10.3 | -1.9% | -1.406 to +1.006 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*