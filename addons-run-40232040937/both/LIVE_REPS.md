# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.519 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.6 | 85.25 |
| response time (ms), 95th percentile | 278.3 | 133.2 |
| response time (ms), 99th percentile | 410.7 | 170.9 |
| time over the response line (% of samples) | 0.4621 | 0.0122 |
| failed requests (%) | 0.01299 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2217 |
| utilisation (used / allocatable) | 0.0364 | 0.04817 |
| CPU used (cores), mean | 0.8735 | 1.156 |
| Omni's own CPU (cores), mean | 0 | 0.01609 |
| CPU used with Omni's own (cores), mean | 0.8735 | 1.172 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720 | 558 |
| HPA replicas, mean | 8.865 | 10.28 |
| pods started | 4.9 | 7.3 |
| pod start wait, total (s) | 6.3 | 11.6 |
| pod start wait, mean (s) | 1.298 | 1.575 |
| host CPU busy, the real machine under kind (%) | 27.1 | 35.68 |
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
| node-hours | 1.519 | 1.517 | −0.1% | −0.0084 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 161.6 | +1.6% | +1.8335 to +3.3249 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 161.6 | +1.6% | +1.8335 to +3.3249 | yes: power given |
| response time (ms), mean | 137.6 | 85.25 | −38.1% | −61.9433 to −42.7912 | yes: GAIN |
| response time (ms), 95th percentile | 278.3 | 133.2 | −52.1% | −161.9198 to −128.2042 | yes: GAIN |
| response time (ms), 99th percentile | 410.7 | 170.9 | −58.4% | −269.3822 to −210.1286 | yes: GAIN |
| time over the response line (% of samples) | 0.4621 | 0.0122 | −97.4% | −0.7489 to −0.1509 | yes: GAIN |
| failed requests (%) | 0.01299 | 0 | −100.0% | −0.0424 to +0.0164 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.6 | +30.600 (native is 0) | +21.3335 to +39.8665 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.2217 | +38.5% | −0.3160 to +0.4393 | no |
| utilisation (used / allocatable) | 0.0364 | 0.04817 | +32.3% | +0.0092 to +0.0143 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8735 | 1.156 | +32.3% | +0.2210 to +0.3439 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01609 | +0.016 (native is 0) | +0.0131 to +0.0191 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8735 | 1.172 | +34.2% | +0.2354 to +0.3617 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720 | 558 | −22.5% | −190.4126 to −133.6807 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.865 | 10.28 | +15.9% | +0.7567 to +2.0669 | yes: power given |
| pods started | 4.9 | 7.3 | +49.0% | +1.2715 to +3.5285 | yes: power given |
| pod start wait, total (s) | 6.3 | 11.6 | +84.1% | +2.5595 to +8.0405 | yes: LOSS |
| pod start wait, mean (s) | 1.298 | 1.575 | +21.3% | −0.0239 to +0.5771 | no |
| host CPU busy, the real machine under kind (%) | 27.1 | 35.68 | +31.7% | +6.7532 to +10.4072 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*