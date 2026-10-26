# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.358 |
| node-hours | 2.515 | 2.246 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 252.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 343.5 | 298.4 |
| response time (ms), 95th percentile | 1331 | 1368 |
| response time (ms), 99th percentile | 2075 | 2177 |
| time over the response line (% of samples) | 16.42 | 15.14 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.04 | 12.26 |
| utilisation (used / allocatable) | 0.06006 | 0.06764 |
| CPU used (cores), mean | 1.441 | 1.434 |
| Omni's own CPU (cores), mean | 0 | 0.01515 |
| CPU used with Omni's own (cores), mean | 1.441 | 1.45 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 421.1 |
| HPA replicas, mean | 2.035 | 2.158 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.8 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 41.3 | 42.06 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 773.5 | 777.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.953 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.08333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 85.46 | 89.45 |
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
| worker nodes in service, mean | 6 | 5.358 | −10.7% | −1.3988 to +0.1140 | no |
| node-hours | 2.515 | 2.246 | −10.7% | −0.5868 to +0.0481 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.6 | +0.0% | −0.6275 to +0.8038 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 252.4 | −7.4% | −43.7971 to +3.5693 | no |
| response time (ms), mean | 343.5 | 298.4 | −13.1% | −77.7444 to −12.5097 | yes: GAIN |
| response time (ms), 95th percentile | 1331 | 1368 | +2.8% | −224.2331 to +297.6041 | no |
| response time (ms), 99th percentile | 2075 | 2177 | +4.9% | −307.6610 to +510.1936 | no |
| time over the response line (% of samples) | 16.42 | 15.14 | −7.8% | −2.8812 to +0.3242 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 10.6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 | +23.000 (native is 0) | +15.9510 to +30.0490 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.04 | 12.26 | +1.9% | −1.5060 to +1.9560 | no |
| utilisation (used / allocatable) | 0.06006 | 0.06764 | +12.6% | −0.0017 to +0.0169 | no |
| CPU used (cores), mean | 1.441 | 1.434 | −0.5% | −0.0266 to +0.0128 | no |
| Omni's own CPU (cores), mean | 0 | 0.01515 | +0.015 (native is 0) | +0.0136 to +0.0167 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.441 | 1.45 | +0.6% | −0.0117 to +0.0282 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 421.1 | −9.1% | −97.3836 to +13.2565 | no |
| HPA replicas, mean | 2.035 | 2.158 | +6.0% | +0.0165 to +0.2277 | yes: power given |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.2003 to +1.8003 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| host CPU busy, the real machine under kind (%) | 41.3 | 42.06 | +1.8% | +0.2217 to +1.2921 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.5 | 777.7 | +0.5% | −4.5138 to +12.9138 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.953 | −17.5% | −2.1911 to +0.0970 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.08333 | +5.3% | −0.0315 to +0.0398 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.46 | 89.45 | +4.7% | −3.9335 to +11.9252 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*