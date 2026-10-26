# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 154.1 | 78.98 |
| response time (ms), 95th percentile | 339.8 | 114.5 |
| response time (ms), 99th percentile | 579.8 | 153.4 |
| time over the response line (% of samples) | 2.07 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.05333 |
| utilisation (used / allocatable) | 0.03851 | 0.03692 |
| CPU used (cores), mean | 0.9242 | 0.886 |
| Omni's own CPU (cores), mean | 0 | 0.0081 |
| CPU used with Omni's own (cores), mean | 0.9242 | 0.8941 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.6 | 748.9 |
| HPA replicas, mean | 8.34 | 8 |
| pods started | 5.4 | 4.3 |
| pod start wait, total (s) | 8.2 | 6.6 |
| pod start wait, mean (s) | 1.54 | 1.507 |
| host CPU busy, the real machine under kind (%) | 27.78 | 26.98 |
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
| node-hours | 1.513 | 1.516 | +0.2% | −0.0075 to +0.0131 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.9 | −0.0% | −1.1549 to +1.0490 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.9 | −0.0% | −1.1549 to +1.0490 | no |
| response time (ms), mean | 154.1 | 78.98 | −48.7% | −100.9861 to −49.2538 | yes: GAIN |
| response time (ms), 95th percentile | 339.8 | 114.5 | −66.3% | −293.4525 to −157.2945 | yes: GAIN |
| response time (ms), 99th percentile | 579.8 | 153.4 | −73.5% | −577.9872 to −274.8942 | yes: GAIN |
| time over the response line (% of samples) | 2.07 | 0 | −100.0% | −3.4858 to −0.6550 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 0 | −100.0% | −3.6249 to −0.5751 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 | +17.200 (native is 0) | +14.5707 to +19.8293 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.05333 | ±0.0% | −0.1557 to +0.1557 | no |
| utilisation (used / allocatable) | 0.03851 | 0.03692 | −4.1% | −0.0028 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9242 | 0.886 | −4.1% | −0.0665 to −0.0100 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0081 | +0.008 (native is 0) | +0.0069 to +0.0093 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9242 | 0.8941 | −3.3% | −0.0574 to −0.0028 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.6 | 748.9 | +2.4% | −5.8370 to +40.5206 | no |
| HPA replicas, mean | 8.34 | 8 | −4.1% | −0.8850 to +0.2042 | no |
| pods started | 5.4 | 4.3 | −20.4% | −2.0204 to −0.1796 | yes: GAIN |
| pod start wait, total (s) | 8.2 | 6.6 | −19.5% | −3.4221 to +0.2221 | no |
| pod start wait, mean (s) | 1.54 | 1.507 | −2.2% | −0.3132 to +0.2465 | no |
| host CPU busy, the real machine under kind (%) | 27.78 | 26.98 | −2.9% | −1.6419 to +0.0454 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*