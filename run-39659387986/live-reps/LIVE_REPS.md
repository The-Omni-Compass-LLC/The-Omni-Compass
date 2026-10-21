# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.98 |
| node-hours | 2.514 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 134.8 | 100.7 |
| response time (ms), 95th percentile | 226.7 | 219 |
| response time (ms), 99th percentile | 326.1 | 319.3 |
| time over the response line (% of samples) | 0.1384 | 0.1797 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1039 | 1069 |
| utilisation (used / allocatable) | 0.05955 | 0.05939 |
| CPU used (cores), mean | 1.429 | 1.421 |
| Omni's own CPU (cores), mean | 0 | 0.01165 |
| CPU used with Omni's own (cores), mean | 1.429 | 1.433 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.9 | 456 |
| HPA replicas, mean | 1.972 | 2.028 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.65 | 45.01 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1468 | 1467 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.609 |
| queue: job wait, submitted to its first pod running, mean (s) | 140.8 | 145.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 656.2 | 691.3 |
| queue: job turnaround, submitted to done, mean (s) | 782.1 | 803 |
| queue: jobs unfinished at the window's end | 7.7 | 7.9 |

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
| worker nodes in service, mean | 6 | 5.98 | -0.3% | -0.06364 to +0.02462 | no |
| node-hours | 2.514 | 2.508 | -0.2% | -0.02271 to +0.01032 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272 | +0.0% | -0.8401 to +0.9731 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 271.4 | -0.2% | -1.796 to +0.6999 | no |
| response time (ms), mean | 134.8 | 100.7 | -25.2% | -39.84 to -28.18 | yes: GAIN |
| response time (ms), 95th percentile | 226.7 | 219 | -3.4% | -18.75 to +3.264 | no |
| response time (ms), 99th percentile | 326.1 | 319.3 | -2.1% | -29 to +15.35 | no |
| time over the response line (% of samples) | 0.1384 | 0.1797 | +29.8% | -0.05773 to +0.1403 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 | +11.4 (native is 0) | +9.609 to +13.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1039 | 1069 | +2.8% | -40.12 to +99.3 | no |
| utilisation (used / allocatable) | 0.05955 | 0.05939 | -0.3% | -0.001486 to +0.001176 | no |
| CPU used (cores), mean | 1.429 | 1.421 | -0.6% | -0.03838 to +0.02257 | no |
| Omni's own CPU (cores), mean | 0 | 0.01165 | +0.0117 (native is 0) | +0.01087 to +0.01243 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.433 | +0.3% | -0.02689 to +0.03437 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.9 | 456 | +0.2% | -7.83 to +10.03 | no |
| HPA replicas, mean | 1.972 | 2.028 | +2.8% | -0.1302 to +0.2414 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.2 (native is 0) | -0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.65 | 45.01 | +0.8% | -0.6801 to +1.397 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1468 | 1467 | -0.0% | -8.321 to +8.121 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.217 | -13.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 140.8 | 145.9 | +3.6% | -28.69 to +38.7 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 656.2 | 691.3 | +5.3% | -80.46 to +150.7 | no |
| queue: job turnaround, submitted to done, mean (s) | 782.1 | 803 | +2.7% | -46.72 to +88.47 | no |
| queue: jobs unfinished at the window's end | 7.7 | 7.9 | +2.6% | -2.131 to +2.531 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*