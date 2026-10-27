# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.243 |
| node-hours | 2.515 | 2.199 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 248.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 360.3 | 328.1 |
| response time (ms), 95th percentile | 1507 | 1528 |
| response time (ms), 99th percentile | 2379 | 2362 |
| time over the response line (% of samples) | 13.65 | 13.77 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.23 | 16.34 |
| utilisation (used / allocatable) | 0.05945 | 0.06802 |
| CPU used (cores), mean | 1.427 | 1.406 |
| Omni's own CPU (cores), mean | 0 | 0.01807 |
| CPU used with Omni's own (cores), mean | 1.427 | 1.424 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.3 | 422.2 |
| HPA replicas, mean | 2.081 | 2.123 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.3 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 42.95 | 43.71 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 794.1 | 796.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.732 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8417 | 0.8792 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 103.5 | 106.2 |
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
| worker nodes in service, mean | 6 | 5.243 | −12.6% | −1.4776 to −0.0369 | yes: GAIN |
| node-hours | 2.515 | 2.199 | −12.6% | −0.6181 to −0.0142 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.4 | −0.0% | −0.5389 to +0.5277 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 248.6 | −8.7% | −46.3891 to −1.2179 | yes: GAIN |
| response time (ms), mean | 360.3 | 328.1 | −8.9% | −54.5191 to −9.7608 | yes: GAIN |
| response time (ms), 95th percentile | 1507 | 1528 | +1.4% | −189.7231 to +231.4321 | no |
| response time (ms), 99th percentile | 2379 | 2362 | −0.7% | −218.1191 to +182.6653 | no |
| time over the response line (% of samples) | 13.65 | 13.77 | +0.9% | −0.6085 to +0.8434 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.6 | −1.1% | −0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.2 | +39.200 (native is 0) | +23.3631 to +55.0369 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.23 | 16.34 | +0.6% | −1.0942 to +1.2975 | no |
| utilisation (used / allocatable) | 0.05945 | 0.06802 | +14.4% | −0.0002 to +0.0174 | no |
| CPU used (cores), mean | 1.427 | 1.406 | −1.5% | −0.0419 to +0.0002 | no |
| Omni's own CPU (cores), mean | 0 | 0.01807 | +0.018 (native is 0) | +0.0166 to +0.0195 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.427 | 1.424 | −0.2% | −0.0231 to +0.0175 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.3 | 422.2 | −8.7% | −81.9214 to +1.6381 | no |
| HPA replicas, mean | 2.081 | 2.123 | +2.0% | −0.1308 to +0.2149 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 42.95 | 43.71 | +1.8% | +0.4678 to +1.0465 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.1 | 796.4 | +0.3% | −1.0728 to +5.6728 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.732 | −21.1% | −2.3968 to −0.1386 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8417 | 0.8792 | +4.5% | −0.0413 to +0.1163 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.7 | +21.4% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 103.5 | 106.2 | +2.6% | −0.9101 to +6.3018 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*