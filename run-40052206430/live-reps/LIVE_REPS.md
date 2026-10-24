# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.975 |
| node-hours | 2.517 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 127.8 | 94.01 |
| response time (ms), 95th percentile | 212.5 | 201.4 |
| response time (ms), 99th percentile | 300.6 | 291.6 |
| time over the response line (% of samples) | 0.1529 | 0.09584 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 931.6 | 911.3 |
| utilisation (used / allocatable) | 0.05848 | 0.05851 |
| CPU used (cores), mean | 1.404 | 1.399 |
| Omni's own CPU (cores), mean | 0 | 0.0115 |
| CPU used with Omni's own (cores), mean | 1.404 | 1.41 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 462.5 |
| HPA replicas, mean | 2.008 | 1.901 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 43.07 | 43.43 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1385 | 1396 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.754 |
| queue: job wait, submitted to its first pod running, mean (s) | 133.6 | 138 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 636.4 | 622.1 |
| queue: job turnaround, submitted to done, mean (s) | 728 | 703.7 |
| queue: jobs unfinished at the window's end | 6.3 | 5.3 |

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
| worker nodes in service, mean | 6 | 5.975 | -0.4% | -0.05677 to +0.007115 | no |
| node-hours | 2.517 | 2.508 | -0.4% | -0.02345 to +0.00489 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.8 | +0.0% | -0.9059 to +1.052 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271 | -0.3% | -2.037 to +0.6163 | no |
| response time (ms), mean | 127.8 | 94.01 | -26.5% | -40.81 to -26.81 | yes: GAIN |
| response time (ms), 95th percentile | 212.5 | 201.4 | -5.2% | -21.56 to -0.7284 | yes: GAIN |
| response time (ms), 99th percentile | 300.6 | 291.6 | -3.0% | -24.86 to +6.934 | no |
| time over the response line (% of samples) | 0.1529 | 0.09584 | -37.3% | -0.1927 to +0.07851 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.5 (native is 0) | +11.1 to +13.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 931.6 | 911.3 | -2.2% | -77.47 to +36.92 | no |
| utilisation (used / allocatable) | 0.05848 | 0.05851 | +0.1% | -0.001249 to +0.001312 | no |
| CPU used (cores), mean | 1.404 | 1.399 | -0.3% | -0.03383 to +0.02424 | no |
| Omni's own CPU (cores), mean | 0 | 0.0115 | +0.0115 (native is 0) | +0.0106 to +0.0124 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.404 | 1.41 | +0.5% | -0.02182 to +0.03523 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 462.5 | +0.1% | -9.39 to +10.04 | no |
| HPA replicas, mean | 2.008 | 1.901 | -5.3% | -0.2217 to +0.00704 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 43.07 | 43.43 | +0.8% | -0.3302 to +1.058 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1385 | 1396 | +0.8% | -58.8 to +81.8 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.754 | -4.1% | -0.5735 to +0.08083 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 133.6 | 138 | +3.3% | -23.82 to +32.75 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 636.4 | 622.1 | -2.2% | -208.1 to +179.5 | no |
| queue: job turnaround, submitted to done, mean (s) | 728 | 703.7 | -3.3% | -83.21 to +34.66 | no |
| queue: jobs unfinished at the window's end | 6.3 | 5.3 | -15.9% | -2.066 to +0.06632 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*