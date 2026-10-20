# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.978 |
| node-hours | 2.517 | 2.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 271.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.8 | 88.12 |
| response time (ms), 95th percentile | 216.4 | 168.6 |
| response time (ms), 99th percentile | 284.3 | 257.3 |
| time over the response line (% of samples) | 0.05429 | 0.03682 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1122 | 1137 |
| utilisation (used / allocatable) | 0.06037 | 0.06026 |
| CPU used (cores), mean | 1.449 | 1.441 |
| Omni's own CPU (cores), mean | 0 | 0.0131 |
| CPU used with Omni's own (cores), mean | 1.449 | 1.454 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.8 | 450.2 |
| HPA replicas, mean | 2.126 | 2.206 |
| pods started | 0.2 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.8 |
| pod start wait, mean (s) | 0.2 | 0.8 |
| host CPU busy, the real machine under kind (%) | 45.45 | 45.99 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1443 | 1422 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.697 |
| queue: job wait, submitted to its first pod running, mean (s) | 182.7 | 169 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 805.6 | 775.4 |
| queue: job turnaround, submitted to done, mean (s) | 807.2 | 812.6 |
| queue: jobs unfinished at the window's end | 10 | 10.4 |

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
| worker nodes in service, mean | 6 | 5.978 | -0.4% | -0.06561 to +0.02228 | no |
| node-hours | 2.517 | 2.503 | -0.6% | -0.03883 to +0.01039 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272 | -0.2% | -2.157 to +1.045 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 271.3 | -0.5% | -3.305 to +0.835 | no |
| response time (ms), mean | 137.8 | 88.12 | -36.0% | -60.43 to -38.89 | yes: GAIN |
| response time (ms), 95th percentile | 216.4 | 168.6 | -22.1% | -53.72 to -41.87 | yes: GAIN |
| response time (ms), 99th percentile | 284.3 | 257.3 | -9.5% | -35.57 to -18.46 | yes: GAIN |
| time over the response line (% of samples) | 0.05429 | 0.03682 | -32.2% | -0.06777 to +0.03282 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.9 | +12.9 (native is 0) | +11.86 to +13.94 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1122 | 1137 | +1.4% | -50.69 to +81.15 | no |
| utilisation (used / allocatable) | 0.06037 | 0.06026 | -0.2% | -0.001937 to +0.001718 | no |
| CPU used (cores), mean | 1.449 | 1.441 | -0.5% | -0.0452 to +0.03004 | no |
| Omni's own CPU (cores), mean | 0 | 0.0131 | +0.0131 (native is 0) | +0.01201 to +0.01419 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.449 | 1.454 | +0.4% | -0.03134 to +0.04238 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.8 | 450.2 | +0.1% | -12.21 to +13.09 | no |
| HPA replicas, mean | 2.126 | 2.206 | +3.8% | -0.1635 to +0.3233 | no |
| pods started | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | -0.09105 to +1.291 | no |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | -0.09105 to +1.291 | no |
| host CPU busy, the real machine under kind (%) | 45.45 | 45.99 | +1.2% | -0.02176 to +1.091 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1443 | 1422 | -1.4% | -61.04 to +19.24 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.697 | -5.0% | -1.347 to +0.7419 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 182.7 | 169 | -7.5% | -65.88 to +38.45 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 805.6 | 775.4 | -3.7% | -192.9 to +132.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 807.2 | 812.6 | +0.7% | -45.21 to +56.07 | no |
| queue: jobs unfinished at the window's end | 10 | 10.4 | +4.0% | -3.042 to +3.842 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*