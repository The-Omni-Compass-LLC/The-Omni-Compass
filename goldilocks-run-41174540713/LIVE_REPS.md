# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 174.5 | 93.95 |
| response time (ms), 95th percentile | 360.7 | 148.1 |
| response time (ms), 99th percentile | 523.1 | 198.9 |
| time over the response line (% of samples) | 1.412 | 0.0122 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.08 |
| utilisation (used / allocatable) | 0.03466 | 0.0511 |
| CPU used (cores), mean | 0.8319 | 1.226 |
| Omni's own CPU (cores), mean | 0 | 0.01299 |
| CPU used with Omni's own (cores), mean | 0.8319 | 1.239 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.9 | 523.7 |
| HPA replicas, mean | 9.654 | 12.46 |
| pods started | 3.3 | 6.2 |
| pod start wait, total (s) | 5.7 | 11.6 |
| pod start wait, mean (s) | 1.825 | 1.603 |
| host CPU busy, the real machine under kind (%) | 25.69 | 37.41 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.513 | −0.2% | −0.0119 to +0.0052 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 161.8 | +2.1% | +2.6126 to +4.1781 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 161.8 | +2.1% | +2.6126 to +4.1781 | yes: power given |
| response time (ms), mean | 174.5 | 93.95 | −46.2% | −90.3118 to −70.8847 | yes: GAIN |
| response time (ms), 95th percentile | 360.7 | 148.1 | −58.9% | −236.5456 to −188.7084 | yes: GAIN |
| response time (ms), 99th percentile | 523.1 | 198.9 | −62.0% | −362.7356 to −285.5878 | yes: GAIN |
| time over the response line (% of samples) | 1.412 | 0.0122 | −99.1% | −1.8834 to −0.9165 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 0 | −100.0% | −2.2003 to −0.1997 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.9 | +41.900 (native is 0) | +30.0238 to +53.7762 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.08 | −25.0% | −0.1674 to +0.1141 | no |
| utilisation (used / allocatable) | 0.03466 | 0.0511 | +47.4% | +0.0155 to +0.0174 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8319 | 1.226 | +47.4% | +0.3711 to +0.4181 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01299 | +0.013 (native is 0) | +0.0111 to +0.0149 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8319 | 1.239 | +49.0% | +0.3840 to +0.4311 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.9 | 523.7 | −30.7% | −254.5707 to −209.8291 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.654 | 12.46 | +29.1% | +1.9767 to +3.6429 | yes: power given |
| pods started | 3.3 | 6.2 | +87.9% | +0.9208 to +4.8792 | yes: power given |
| pod start wait, total (s) | 5.7 | 11.6 | +103.5% | +0.6064 to +11.1936 | yes: LOSS |
| pod start wait, mean (s) | 1.825 | 1.603 | −12.2% | −0.9955 to +0.5508 | no |
| host CPU busy, the real machine under kind (%) | 25.69 | 37.41 | +45.6% | +10.9713 to +12.4703 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*