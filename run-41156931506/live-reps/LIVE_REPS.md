# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 169.7 | 169.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.7 | 169.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 394 | 328.2 |
| response time (ms), 95th percentile | 1674 | 1408 |
| response time (ms), 99th percentile | 3764 | 3885 |
| time over the response line (% of samples) | 17.26 | 15.76 |
| failed requests (%) | 2.036 | 2.275 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.42 | 1.093 |
| utilisation (used / allocatable) | 0.08581 | 0.08505 |
| CPU used (cores), mean | 2.06 | 2.041 |
| Omni's own CPU (cores), mean | 0 | 0.01212 |
| CPU used with Omni's own (cores), mean | 2.06 | 2.053 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 345.3 | 347.6 |
| HPA replicas, mean | 14.52 | 14.64 |
| pods started | 6.2 | 5.2 |
| pod start wait, total (s) | 10.2 | 10.8 |
| pod start wait, mean (s) | 1.606 | 1.913 |
| host CPU busy, the real machine under kind (%) | 59.27 | 59.44 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 290.1 | 325.7 |
| second app: response time (ms), 99th percentile | 1854 | 2124 |
| second app: time over the response line (% of samples) | 10.79 | 10.98 |
| second app: failed requests (%) | 8.812 | 8.613 |

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
| node-hours | 1.512 | 1.514 | +0.1% | −0.0030 to +0.0060 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 169.7 | 169.6 | −0.0% | −0.7648 to +0.6354 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.7 | 169.6 | −0.0% | −0.7648 to +0.6354 | no |
| response time (ms), mean | 394 | 328.2 | −16.7% | −137.1309 to +5.6145 | no |
| response time (ms), 95th percentile | 1674 | 1408 | −15.9% | −719.9372 to +186.4562 | no |
| response time (ms), 99th percentile | 3764 | 3885 | +3.2% | −588.3732 to +829.8038 | no |
| time over the response line (% of samples) | 17.26 | 15.76 | −8.7% | −3.5619 to +0.5603 | no |
| failed requests (%) | 2.036 | 2.275 | +11.7% | −0.6281 to +1.1055 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.4 | 6.1 | −4.7% | −0.8889 to +0.2889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 | +47.300 (native is 0) | +38.0774 to +56.5226 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.42 | 1.093 | −23.0% | −0.9151 to +0.2617 | no |
| utilisation (used / allocatable) | 0.08581 | 0.08505 | −0.9% | −0.0021 to +0.0006 | no |
| CPU used (cores), mean | 2.06 | 2.041 | −0.9% | −0.0504 to +0.0136 | no |
| Omni's own CPU (cores), mean | 0 | 0.01212 | +0.012 (native is 0) | +0.0108 to +0.0135 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.06 | 2.053 | −0.3% | −0.0380 to +0.0255 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 345.3 | 347.6 | +0.7% | −4.7419 to +9.2374 | no |
| HPA replicas, mean | 14.52 | 14.64 | +0.9% | −0.1244 to +0.3749 | no |
| pods started | 6.2 | 5.2 | −16.1% | −1.9537 to −0.0463 | yes: GAIN |
| pod start wait, total (s) | 10.2 | 10.8 | +5.9% | −1.8362 to +3.0362 | no |
| pod start wait, mean (s) | 1.606 | 1.913 | +19.1% | +0.1050 to +0.5088 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.27 | 59.44 | +0.3% | −0.4350 to +0.7731 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 290.1 | 325.7 | +12.3% | −36.5281 to +107.6671 | no |
| second app: response time (ms), 99th percentile | 1854 | 2124 | +14.6% | −636.0543 to +1176.2923 | no |
| second app: time over the response line (% of samples) | 10.79 | 10.98 | +1.8% | −0.5474 to +0.9348 | no |
| second app: failed requests (%) | 8.812 | 8.613 | −2.3% | −0.4779 to +0.0790 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*