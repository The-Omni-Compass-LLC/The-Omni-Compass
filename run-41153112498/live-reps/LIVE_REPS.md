# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 518 | 516.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518 | 516.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 304.5 | 165.8 |
| response time (ms), 95th percentile | 757.7 | 276.8 |
| response time (ms), 99th percentile | 3567 | 2324 |
| time over the response line (% of samples) | 18.69 | 11.48 |
| failed requests (%) | 10.03 | 8.925 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.6 | 21.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3867 | 0.2467 |
| utilisation (used / allocatable) | 0.1034 | 0.101 |
| CPU used (cores), mean | 2.482 | 2.425 |
| Omni's own CPU (cores), mean | 0 | 0.0103 |
| CPU used with Omni's own (cores), mean | 2.482 | 2.435 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 289.2 | 296.7 |
| HPA replicas, mean | 9.643 | 9.978 |
| pods started | 5.2 | 7.2 |
| pod start wait, total (s) | 8.2 | 11 |
| pod start wait, mean (s) | 1.623 | 1.497 |
| host CPU busy, the real machine under kind (%) | 69.81 | 68.65 |
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
| node-hours | 4.513 | 4.514 | +0.0% | −0.0070 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 518 | 516.6 | −0.3% | −2.4760 to −0.3934 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518 | 516.6 | −0.3% | −2.4760 to −0.3934 | yes: GAIN |
| response time (ms), mean | 304.5 | 165.8 | −45.5% | −164.6565 to −112.7055 | yes: GAIN |
| response time (ms), 95th percentile | 757.7 | 276.8 | −63.5% | −525.8737 to −435.9123 | yes: GAIN |
| response time (ms), 99th percentile | 3567 | 2324 | −34.9% | −2052.5952 to −434.2010 | yes: GAIN |
| time over the response line (% of samples) | 18.69 | 11.48 | −38.6% | −8.7745 to −5.6406 | yes: GAIN |
| failed requests (%) | 10.03 | 8.925 | −11.0% | −1.7545 to −0.4468 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 28.6 | 21.5 | −24.8% | −8.9607 to −5.2393 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.7 | +44.700 (native is 0) | +36.6916 to +52.7084 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3867 | 0.2467 | −36.2% | −0.5084 to +0.2284 | no |
| utilisation (used / allocatable) | 0.1034 | 0.101 | −2.3% | −0.0030 to −0.0018 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.482 | 2.425 | −2.3% | −0.0715 to −0.0434 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0103 | +0.010 (native is 0) | +0.0097 to +0.0109 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.482 | 2.435 | −1.9% | −0.0617 to −0.0326 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 289.2 | 296.7 | +2.6% | +3.1548 to +11.8039 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.643 | 9.978 | +3.5% | +0.1363 to +0.5335 | yes: power given |
| pods started | 5.2 | 7.2 | +38.5% | +0.1841 to +3.8159 | yes: power given |
| pod start wait, total (s) | 8.2 | 11 | +34.1% | −0.1551 to +5.7551 | no |
| pod start wait, mean (s) | 1.623 | 1.497 | −7.8% | −0.5675 to +0.3142 | no |
| host CPU busy, the real machine under kind (%) | 69.81 | 68.65 | −1.7% | −1.4808 to −0.8385 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*