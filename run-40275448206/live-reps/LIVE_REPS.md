# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.336 |
| energy, parked workers still on at idle power (Wh, declared model) | 486.6 | 485 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 486.6 | 485 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 311.5 | 154.7 |
| response time (ms), 95th percentile | 799.5 | 325.2 |
| response time (ms), 99th percentile | 1651 | 866.1 |
| time over the response line (% of samples) | 14.85 | 3.689 |
| failed requests (%) | 1.358 | 1.182 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.6 | 9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.9333 |
| utilisation (used / allocatable) | 0.08666 | 0.0839 |
| CPU used (cores), mean | 2.08 | 2.014 |
| Omni's own CPU (cores), mean | 0 | 0.01009 |
| CPU used with Omni's own (cores), mean | 2.08 | 2.024 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 329 | 339.3 |
| HPA replicas, mean | 9.887 | 11.76 |
| pods started | 4.6 | 15.4 |
| pod start wait, total (s) | 7.7 | 29.2 |
| pod start wait, mean (s) | 1.7 | 1.891 |
| host CPU busy, the real machine under kind (%) | 59.63 | 58.32 |
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
| node-hours | 4.334 | 4.335 | +0.0% | −0.0056 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 486.6 | 485 | −0.3% | −2.4297 to −0.7227 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 486.6 | 485 | −0.3% | −2.4297 to −0.7227 | yes: GAIN |
| response time (ms), mean | 311.5 | 154.7 | −50.3% | −178.1038 to −135.6004 | yes: GAIN |
| response time (ms), 95th percentile | 799.5 | 325.2 | −59.3% | −526.4678 to −422.1162 | yes: GAIN |
| response time (ms), 99th percentile | 1651 | 866.1 | −47.5% | −949.2623 to −621.0553 | yes: GAIN |
| time over the response line (% of samples) | 14.85 | 3.689 | −75.2% | −13.8843 to −8.4303 | yes: GAIN |
| failed requests (%) | 1.358 | 1.182 | −13.0% | −0.3098 to −0.0425 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 27.6 | 9 | −67.4% | −21.5819 to −15.6181 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.3 | +60.300 (native is 0) | +44.0057 to +76.5943 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.9333 | +169.2% | +0.0390 to +1.1343 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.08666 | 0.0839 | −3.2% | −0.0034 to −0.0022 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.08 | 2.014 | −3.2% | −0.0807 to −0.0518 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01009 | +0.010 (native is 0) | +0.0086 to +0.0115 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.08 | 2.024 | −2.7% | −0.0710 to −0.0413 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 329 | 339.3 | +3.1% | +6.9166 to +13.6080 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.887 | 11.76 | +18.9% | +0.6410 to +3.1049 | yes: power given |
| pods started | 4.6 | 15.4 | +234.8% | +7.4996 to +14.1004 | yes: power given |
| pod start wait, total (s) | 7.7 | 29.2 | +279.2% | +13.9130 to +29.0870 | yes: LOSS |
| pod start wait, mean (s) | 1.7 | 1.891 | +11.2% | −0.1133 to +0.4950 | no |
| host CPU busy, the real machine under kind (%) | 59.63 | 58.32 | −2.2% | −1.6833 to −0.9400 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*