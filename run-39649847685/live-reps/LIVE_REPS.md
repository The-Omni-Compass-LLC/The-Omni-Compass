# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.953 |
| node-hours | 2.516 | 2.5 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 270.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 139.1 | 104.3 |
| response time (ms), 95th percentile | 245.4 | 232.7 |
| response time (ms), 99th percentile | 350.4 | 345.6 |
| time over the response line (% of samples) | 0.1697 | 0.2381 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1160 | 1186 |
| utilisation (used / allocatable) | 0.05887 | 0.05878 |
| CPU used (cores), mean | 1.413 | 1.4 |
| Omni's own CPU (cores), mean | 0 | 0.01228 |
| CPU used with Omni's own (cores), mean | 1.413 | 1.413 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.1 | 460.8 |
| HPA replicas, mean | 1.96 | 1.936 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.13 | 44.51 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1457 | 1440 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.052 |
| queue: job wait, submitted to its first pod running, mean (s) | 185.2 | 168.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 902.9 | 711.1 |
| queue: job turnaround, submitted to done, mean (s) | 836.9 | 871.7 |
| queue: jobs unfinished at the window's end | 12.3 | 13 |

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
| worker nodes in service, mean | 6 | 5.953 | -0.8% | -0.1296 to +0.03578 | no |
| node-hours | 2.516 | 2.5 | -0.6% | -0.04961 to +0.01749 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.1 | +0.1% | -0.6304 to +1.114 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 270.6 | -0.5% | -4.073 to +1.598 | no |
| response time (ms), mean | 139.1 | 104.3 | -25.0% | -40.16 to -29.43 | yes: GAIN |
| response time (ms), 95th percentile | 245.4 | 232.7 | -5.2% | -24.73 to -0.5583 | yes: GAIN |
| response time (ms), 99th percentile | 350.4 | 345.6 | -1.4% | -32.04 to +22.49 | no |
| time over the response line (% of samples) | 0.1697 | 0.2381 | +40.3% | -0.05035 to +0.1872 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.5 (native is 0) | +10.53 to +14.47 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1160 | 1186 | +2.3% | -60.01 to +113.1 | no |
| utilisation (used / allocatable) | 0.05887 | 0.05878 | -0.1% | -0.001123 to +0.0009562 | no |
| CPU used (cores), mean | 1.413 | 1.4 | -0.9% | -0.04465 to +0.01983 | no |
| Omni's own CPU (cores), mean | 0 | 0.01228 | +0.0123 (native is 0) | +0.01133 to +0.01323 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.413 | 1.413 | -0.0% | -0.03283 to +0.03257 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.1 | 460.8 | +0.4% | -5.908 to +9.211 | no |
| HPA replicas, mean | 1.96 | 1.936 | -1.2% | -0.1654 to +0.1176 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.13 | 44.51 | +0.9% | -0.5485 to +1.317 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1457 | 1440 | -1.2% | -47.41 to +13.01 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.052 | -15.8% | -5.519 to +3.623 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 185.2 | 168.8 | -8.9% | -57.26 to +24.42 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 902.9 | 711.1 | -21.2% | -330.3 to -53.31 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 836.9 | 871.7 | +4.2% | -31.71 to +101.4 | no |
| queue: jobs unfinished at the window's end | 12.3 | 13 | +5.7% | -1.117 to +2.517 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*