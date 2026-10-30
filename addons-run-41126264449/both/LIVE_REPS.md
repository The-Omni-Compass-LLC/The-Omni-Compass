# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.508 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 158.7 | 96.92 |
| response time (ms), 95th percentile | 326.9 | 148 |
| response time (ms), 99th percentile | 471.8 | 196.8 |
| time over the response line (% of samples) | 0.8918 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.25 |
| utilisation (used / allocatable) | 0.03762 | 0.05106 |
| CPU used (cores), mean | 0.9029 | 1.225 |
| Omni's own CPU (cores), mean | 0 | 0.01928 |
| CPU used with Omni's own (cores), mean | 0.9029 | 1.245 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.5 | 524.5 |
| HPA replicas, mean | 8.908 | 10.7 |
| pods started | 4.8 | 7.8 |
| pod start wait, total (s) | 6.3 | 12 |
| pod start wait, mean (s) | 1.315 | 1.529 |
| host CPU busy, the real machine under kind (%) | 28.68 | 38.57 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | +0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.508 | 1.513 | +0.4% | −0.0038 to +0.0151 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 161.8 | +2.3% | +2.4839 to +4.7951 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 161.8 | +2.3% | +2.4839 to +4.7951 | yes: power given |
| response time (ms), mean | 158.7 | 96.92 | −38.9% | −66.2525 to −57.2775 | yes: GAIN |
| response time (ms), 95th percentile | 326.9 | 148 | −54.7% | −197.6233 to −160.1967 | yes: GAIN |
| response time (ms), 99th percentile | 471.8 | 196.8 | −58.3% | −311.5481 to −238.4939 | yes: GAIN |
| time over the response line (% of samples) | 0.8918 | 0 | −100.0% | −1.2915 to −0.4921 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1 | 0 | −100.0% | −1.7540 to −0.2460 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.3 | +34.300 (native is 0) | +25.6303 to +42.9697 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.25 | −15.3% | −0.4224 to +0.3324 | no |
| utilisation (used / allocatable) | 0.03762 | 0.05106 | +35.7% | +0.0123 to +0.0146 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9029 | 1.225 | +35.7% | +0.2953 to +0.3497 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01928 | +0.019 (native is 0) | +0.0167 to +0.0218 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9029 | 1.245 | +37.9% | +0.3127 to +0.3708 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.5 | 524.5 | −24.8% | −181.3925 to −164.6372 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.908 | 10.7 | +20.1% | +1.1458 to +2.4366 | yes: power given |
| pods started | 4.8 | 7.8 | +62.5% | +1.6940 to +4.3060 | yes: power given |
| pod start wait, total (s) | 6.3 | 12 | +90.5% | +2.7983 to +8.6017 | yes: LOSS |
| pod start wait, mean (s) | 1.315 | 1.529 | +16.3% | +0.0443 to +0.3842 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 28.68 | 38.57 | +34.5% | +9.0104 to +10.7564 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*