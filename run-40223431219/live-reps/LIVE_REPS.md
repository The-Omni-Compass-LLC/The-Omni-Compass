# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 147.5 | 75.95 |
| response time (ms), 95th percentile | 327.2 | 111.9 |
| response time (ms), 99th percentile | 524.8 | 148.7 |
| time over the response line (% of samples) | 1.852 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1567 | 0.1333 |
| utilisation (used / allocatable) | 0.03707 | 0.03551 |
| CPU used (cores), mean | 0.8898 | 0.8523 |
| Omni's own CPU (cores), mean | 0 | 0.00791 |
| CPU used with Omni's own (cores), mean | 0.8898 | 0.8602 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 762.4 | 782.6 |
| HPA replicas, mean | 8.349 | 7.917 |
| pods started | 5.2 | 3 |
| pod start wait, total (s) | 8.4 | 3.9 |
| pod start wait, mean (s) | 1.624 | 1.28 |
| host CPU busy, the real machine under kind (%) | 26.78 | 25.87 |
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
| node-hours | 1.517 | 1.515 | −0.1% | −0.0081 to +0.0037 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.5 | −0.4% | −1.2736 to +0.1291 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.5 | −0.4% | −1.2736 to +0.1291 | no |
| response time (ms), mean | 147.5 | 75.95 | −48.5% | −97.5149 to −45.5781 | yes: GAIN |
| response time (ms), 95th percentile | 327.2 | 111.9 | −65.8% | −288.9316 to −141.6784 | yes: GAIN |
| response time (ms), 99th percentile | 524.8 | 148.7 | −71.7% | −494.5048 to −257.7320 | yes: GAIN |
| time over the response line (% of samples) | 1.852 | 0 | −100.0% | −3.2028 to −0.5022 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.5452 to −0.4548 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.5 | +15.500 (native is 0) | +12.8395 to +18.1605 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1567 | 0.1333 | −14.9% | −0.2134 to +0.1667 | no |
| utilisation (used / allocatable) | 0.03707 | 0.03551 | −4.2% | −0.0027 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8898 | 0.8523 | −4.2% | −0.0639 to −0.0110 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00791 | +0.008 (native is 0) | +0.0066 to +0.0092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8898 | 0.8602 | −3.3% | −0.0549 to −0.0042 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 762.4 | 782.6 | +2.7% | −3.7756 to +44.1946 | no |
| HPA replicas, mean | 8.349 | 7.917 | −5.2% | −1.1599 to +0.2972 | no |
| pods started | 5.2 | 3 | −42.3% | −3.2003 to −1.1997 | yes: GAIN |
| pod start wait, total (s) | 8.4 | 3.9 | −53.6% | −6.5855 to −2.4145 | yes: GAIN |
| pod start wait, mean (s) | 1.624 | 1.28 | −21.2% | −0.6103 to −0.0773 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 26.78 | 25.87 | −3.4% | −1.6661 to −0.1447 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*