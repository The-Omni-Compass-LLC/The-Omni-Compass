# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.462 |
| node-hours | 2.516 | 2.289 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 255.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 338.5 | 300.3 |
| response time (ms), 95th percentile | 1110 | 1120 |
| response time (ms), 99th percentile | 1566 | 1676 |
| time over the response line (% of samples) | 19.62 | 19.53 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 11.1 |
| utilisation (used / allocatable) | 0.06106 | 0.06748 |
| CPU used (cores), mean | 1.465 | 1.462 |
| Omni's own CPU (cores), mean | 0 | 0.0166 |
| CPU used with Omni's own (cores), mean | 1.465 | 1.479 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 418.3 |
| HPA replicas, mean | 1.987 | 2.087 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.3 | 0.1 |
| pod start wait, mean (s) | 0.3 | 0.1 |
| host CPU busy, the real machine under kind (%) | 41.79 | 42.7 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 765.7 | 768.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.973 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.06667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 73.65 | 77.37 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.462 | −9.0% | −1.0286 to −0.0471 | yes: GAIN |
| node-hours | 2.516 | 2.289 | −9.0% | −0.4344 to −0.0200 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.7 | −0.0% | −1.0840 to +0.8555 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 255.9 | −6.2% | −32.5244 to −1.4041 | yes: GAIN |
| response time (ms), mean | 338.5 | 300.3 | −11.3% | −56.2856 to −20.0892 | yes: GAIN |
| response time (ms), 95th percentile | 1110 | 1120 | +0.9% | −79.2866 to +99.5736 | no |
| response time (ms), 99th percentile | 1566 | 1676 | +7.0% | −17.7488 to +237.5848 | no |
| time over the response line (% of samples) | 19.62 | 19.53 | −0.5% | −1.1736 to +0.9934 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11.1 | +2.8% | −0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.800 (native is 0) | +17.5964 to +42.0036 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.59 | 11.1 | +4.9% | −1.5658 to +2.5991 | no |
| utilisation (used / allocatable) | 0.06106 | 0.06748 | +10.5% | −0.0004 to +0.0132 | no |
| CPU used (cores), mean | 1.465 | 1.462 | −0.2% | −0.0212 to +0.0144 | no |
| Omni's own CPU (cores), mean | 0 | 0.0166 | +0.017 (native is 0) | +0.0157 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.479 | +0.9% | −0.0043 to +0.0307 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.8 | 418.3 | −6.6% | −60.3304 to +1.4228 | no |
| HPA replicas, mean | 1.987 | 2.087 | +5.0% | −0.0569 to +0.2554 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 41.79 | 42.7 | +2.2% | +0.5157 to +1.3033 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 765.7 | 768.6 | +0.4% | −2.7871 to +8.5871 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.973 | −17.1% | −1.8986 to −0.1550 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.06667 | +33.3% | −0.0399 to +0.0732 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.5840 to +0.5840 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.65 | 77.37 | +5.0% | −1.7053 to +9.1303 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*