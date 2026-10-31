# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.335 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 482.4 | 480.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.4 | 480.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 276.4 | 133.7 |
| response time (ms), 95th percentile | 738.4 | 273.9 |
| response time (ms), 99th percentile | 1371 | 618.2 |
| time over the response line (% of samples) | 13.08 | 2.836 |
| failed requests (%) | 1.095 | 0.9029 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.685 |
| utilisation (used / allocatable) | 0.08018 | 0.07705 |
| CPU used (cores), mean | 1.924 | 1.849 |
| Omni's own CPU (cores), mean | 0 | 0.00985 |
| CPU used with Omni's own (cores), mean | 1.924 | 1.859 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 366.6 | 380.5 |
| HPA replicas, mean | 9.784 | 11.32 |
| pods started | 6 | 13.9 |
| pod start wait, total (s) | 8 | 24.9 |
| pod start wait, mean (s) | 1.352 | 1.778 |
| host CPU busy, the real machine under kind (%) | 55.48 | 53.85 |
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
| node-hours | 4.335 | 4.337 | +0.1% | −0.0072 to +0.0125 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 482.4 | 480.7 | −0.4% | −2.7586 to −0.6371 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.4 | 480.7 | −0.4% | −2.7586 to −0.6371 | yes: GAIN |
| response time (ms), mean | 276.4 | 133.7 | −51.6% | −180.0230 to −105.3829 | yes: GAIN |
| response time (ms), 95th percentile | 738.4 | 273.9 | −62.9% | −577.5775 to −351.3485 | yes: GAIN |
| response time (ms), 99th percentile | 1371 | 618.2 | −54.9% | −944.7040 to −560.1526 | yes: GAIN |
| time over the response line (% of samples) | 13.08 | 2.836 | −78.3% | −14.6258 to −5.8649 | yes: GAIN |
| failed requests (%) | 1.095 | 0.9029 | −17.5% | −0.3444 to −0.0389 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.3 | 8.1 | −65.2% | −19.6326 to −10.7674 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.2 | +53.200 (native is 0) | +37.1244 to +69.2756 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3683 | 0.685 | +86.0% | −0.0073 to +0.6406 | no |
| utilisation (used / allocatable) | 0.08018 | 0.07705 | −3.9% | −0.0038 to −0.0025 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.924 | 1.849 | −3.9% | −0.0913 to −0.0588 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00985 | +0.010 (native is 0) | +0.0080 to +0.0117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.924 | 1.859 | −3.4% | −0.0809 to −0.0495 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 366.6 | 380.5 | +3.8% | +9.6568 to +18.0162 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.784 | 11.32 | +15.7% | −0.1415 to +3.2189 | no |
| pods started | 6 | 13.9 | +131.7% | +4.9325 to +10.8675 | yes: power given |
| pod start wait, total (s) | 8 | 24.9 | +211.2% | +11.2129 to +22.5871 | yes: LOSS |
| pod start wait, mean (s) | 1.352 | 1.778 | +31.5% | +0.2394 to +0.6124 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 55.48 | 53.85 | −2.9% | −2.0079 to −1.2468 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*