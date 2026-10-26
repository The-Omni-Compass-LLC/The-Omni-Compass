# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.981 |
| node-hours | 2.513 | 2.506 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 270.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 126.7 | 95.1 |
| response time (ms), 95th percentile | 214.8 | 206.5 |
| response time (ms), 99th percentile | 311.2 | 311.9 |
| time over the response line (% of samples) | 0.1766 | 0.1335 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 986.5 | 1000 |
| utilisation (used / allocatable) | 0.05828 | 0.05795 |
| CPU used (cores), mean | 1.399 | 1.386 |
| Omni's own CPU (cores), mean | 0 | 0.01175 |
| CPU used with Omni's own (cores), mean | 1.399 | 1.398 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.4 | 466.5 |
| HPA replicas, mean | 1.986 | 2.046 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 43.15 | 43.61 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1381 | 1418 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.678 |
| queue: job wait, submitted to its first pod running, mean (s) | 138.7 | 165.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 686.1 | 743 |
| queue: job turnaround, submitted to done, mean (s) | 740.8 | 766.1 |
| queue: jobs unfinished at the window's end | 8.9 | 7.8 |

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
| worker nodes in service, mean | 6 | 5.981 | −0.3% | −0.0470 to +0.0082 | no |
| node-hours | 2.513 | 2.506 | −0.3% | −0.0209 to +0.0066 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.3 | −0.0% | −1.1645 to +0.9201 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 270.7 | −0.3% | −2.0506 to +0.5853 | no |
| response time (ms), mean | 126.7 | 95.1 | −24.9% | −39.6146 to −23.5637 | yes: GAIN |
| response time (ms), 95th percentile | 214.8 | 206.5 | −3.9% | −17.1813 to +0.5633 | no |
| response time (ms), 99th percentile | 311.2 | 311.9 | +0.2% | −17.9145 to +19.1365 | no |
| time over the response line (% of samples) | 0.1766 | 0.1335 | −24.4% | −0.1609 to +0.0747 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.700 (native is 0) | +10.4361 to +12.9639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 986.5 | 1000 | +1.4% | −62.4485 to +90.5085 | no |
| utilisation (used / allocatable) | 0.05828 | 0.05795 | −0.6% | −0.0019 to +0.0012 | no |
| CPU used (cores), mean | 1.399 | 1.386 | −0.9% | −0.0489 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0.01175 | +0.012 (native is 0) | +0.0108 to +0.0127 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.398 | −0.0% | −0.0370 to +0.0361 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.4 | 466.5 | +0.5% | −8.5062 to +12.8597 | no |
| HPA replicas, mean | 1.986 | 2.046 | +3.0% | −0.0884 to +0.2080 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.15 | 43.61 | +1.1% | −0.5582 to +1.4782 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1381 | 1418 | +2.7% | −21.9761 to +96.3761 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.678 | −5.4% | −0.8765 to +0.2325 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 138.7 | 165.7 | +19.5% | −4.7923 to +58.8090 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 686.1 | 743 | +8.3% | −106.1170 to +219.9170 | no |
| queue: job turnaround, submitted to done, mean (s) | 740.8 | 766.1 | +3.4% | −32.5299 to +83.2799 | no |
| queue: jobs unfinished at the window's end | 8.9 | 7.8 | −12.4% | −3.4471 to +1.2471 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*