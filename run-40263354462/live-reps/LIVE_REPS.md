# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.581 |
| node-hours | 2.518 | 1.915 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 269.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 225.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 193.5 | 156.1 |
| response time (ms), 95th percentile | 463 | 431 |
| response time (ms), 99th percentile | 735.3 | 706.2 |
| time over the response line (% of samples) | 5.542 | 5.332 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 5.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.18 | 13.16 |
| utilisation (used / allocatable) | 0.05571 | 0.07352 |
| CPU used (cores), mean | 1.337 | 1.315 |
| Omni's own CPU (cores), mean | 0 | 0.01601 |
| CPU used with Omni's own (cores), mean | 1.337 | 1.331 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491 | 409.8 |
| HPA replicas, mean | 2.067 | 2.052 |
| pods started | 0.2 | 0.1 |
| pod start wait, total (s) | 0.6 | 0.2 |
| pod start wait, mean (s) | 0.6 | 0.2 |
| host CPU busy, the real machine under kind (%) | 38.73 | 39.71 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 752.2 | 754.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.655 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.6708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 61.77 | 63.04 |
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
| worker nodes in service, mean | 6 | 4.581 | −23.6% | −2.2504 to −0.5874 | yes: GAIN |
| node-hours | 2.518 | 1.915 | −24.0% | −0.9505 to −0.2567 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 269.9 | −0.5% | −2.6036 to −0.0864 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 225.4 | −16.9% | −72.0409 to −19.6617 | yes: GAIN |
| response time (ms), mean | 193.5 | 156.1 | −19.4% | −50.3967 to −24.5574 | yes: GAIN |
| response time (ms), 95th percentile | 463 | 431 | −6.9% | −91.5255 to +27.3535 | no |
| response time (ms), 99th percentile | 735.3 | 706.2 | −4.0% | −127.0554 to +68.9078 | no |
| time over the response line (% of samples) | 5.542 | 5.332 | −3.8% | −1.4271 to +1.0082 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 5.7 | ±0.0% | −0.7540 to +0.7540 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.3 | +47.300 (native is 0) | +24.0845 to +70.5155 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.18 | 13.16 | −0.2% | −1.7131 to +1.6731 | no |
| utilisation (used / allocatable) | 0.05571 | 0.07352 | +32.0% | +0.0073 to +0.0283 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.337 | 1.315 | −1.6% | −0.0600 to +0.0161 | no |
| Omni's own CPU (cores), mean | 0 | 0.01601 | +0.016 (native is 0) | +0.0143 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.337 | 1.331 | −0.4% | −0.0445 to +0.0327 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491 | 409.8 | −16.5% | −128.4944 to −33.7891 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.067 | 2.052 | −0.7% | −0.1635 to +0.1340 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.5060 to +0.3060 | no |
| pod start wait, total (s) | 0.6 | 0.2 | −66.7% | −1.4769 to +0.6769 | no |
| pod start wait, mean (s) | 0.6 | 0.2 | −66.7% | −1.4769 to +0.6769 | no |
| host CPU busy, the real machine under kind (%) | 38.73 | 39.71 | +2.5% | +0.7059 to +1.2453 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 752.2 | 754.2 | +0.3% | −0.2870 to +4.2870 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.655 | −39.1% | −3.6121 to −1.0784 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6958 | 0.6708 | −3.6% | −0.1107 to +0.0607 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.1 | −15.4% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 61.77 | 63.04 | +2.1% | −0.8099 to +3.3515 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*