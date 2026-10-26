# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.019 |
| node-hours | 2.512 | 2.105 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 240.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 291.6 | 265 |
| response time (ms), 95th percentile | 947.9 | 1009 |
| response time (ms), 99th percentile | 1402 | 1459 |
| time over the response line (% of samples) | 14.66 | 14.55 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 9.64 |
| utilisation (used / allocatable) | 0.05678 | 0.06711 |
| CPU used (cores), mean | 1.363 | 1.331 |
| Omni's own CPU (cores), mean | 0 | 0.01678 |
| CPU used with Omni's own (cores), mean | 1.363 | 1.348 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.2 | 433 |
| HPA replicas, mean | 2.09 | 2.078 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 0.2 | 0.6 |
| pod start wait, mean (s) | 0.2 | 0.6 |
| host CPU busy, the real machine under kind (%) | 39.52 | 40.42 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 763.2 | 766.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.339 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.1625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 70.6 | 74.01 |
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
| worker nodes in service, mean | 6 | 5.019 | −16.4% | −1.7676 to −0.1950 | yes: GAIN |
| node-hours | 2.512 | 2.105 | −16.2% | −0.7381 to −0.0760 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.9 | 271.1 | +0.1% | −0.6064 to +1.0882 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.9 | 240.2 | −11.3% | −55.5148 to −5.8075 | yes: GAIN |
| response time (ms), mean | 291.6 | 265 | −9.1% | −36.3383 to −16.9218 | yes: GAIN |
| response time (ms), 95th percentile | 947.9 | 1009 | +6.4% | +22.2462 to +99.3508 | yes: LOSS |
| response time (ms), 99th percentile | 1402 | 1459 | +4.1% | −22.2227 to +137.1699 | no |
| time over the response line (% of samples) | 14.66 | 14.55 | −0.8% | −0.6994 to +0.4720 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 8.2 | +12.3% | −0.5871 to +2.3871 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.1 | +49.100 (native is 0) | +23.8315 to +74.3685 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.07 | 9.64 | −4.2% | −2.1468 to +1.2968 | no |
| utilisation (used / allocatable) | 0.05678 | 0.06711 | +18.2% | +0.0009 to +0.0198 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.363 | 1.331 | −2.3% | −0.0695 to +0.0065 | no |
| Omni's own CPU (cores), mean | 0 | 0.01678 | +0.017 (native is 0) | +0.0152 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.348 | −1.1% | −0.0524 to +0.0229 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.2 | 433 | −11.3% | −109.0668 to −1.2747 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.09 | 2.078 | −0.6% | −0.2750 to +0.2499 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.4396 to +1.2396 | no |
| pod start wait, mean (s) | 0.2 | 0.6 | +200.0% | −0.4396 to +1.2396 | no |
| host CPU busy, the real machine under kind (%) | 39.52 | 40.42 | +2.3% | +0.7153 to +1.0867 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.2 | 766.6 | +0.4% | +0.0078 to +6.7922 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.339 | −27.7% | −2.8852 to −0.4365 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.175 | 0.1625 | −7.1% | −0.0670 to +0.0420 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 70.6 | 74.01 | +4.8% | +0.7949 to +6.0134 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*