# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.251 |
| node-hours | 2.512 | 2.198 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 247.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 447.4 | 401.5 |
| response time (ms), 95th percentile | 2716 | 2683 |
| response time (ms), 99th percentile | 3990 | 4244 |
| time over the response line (% of samples) | 14.85 | 14.54 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 172.6 | 177.9 |
| utilisation (used / allocatable) | 0.05816 | 0.06543 |
| CPU used (cores), mean | 1.396 | 1.365 |
| Omni's own CPU (cores), mean | 0 | 0.01521 |
| CPU used with Omni's own (cores), mean | 1.396 | 1.38 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.4 | 437.2 |
| HPA replicas, mean | 2.05 | 2.46 |
| pods started | 0 | 0.6 |
| pod start wait, total (s) | 0 | 0.8 |
| pod start wait, mean (s) | 0 | 0.8 |
| host CPU busy, the real machine under kind (%) | 39.74 | 40.44 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 538 | 544.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.895 |

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
| worker nodes in service, mean | 6 | 5.251 | −12.5% | −1.3972 to −0.1008 | yes: GAIN |
| node-hours | 2.512 | 2.198 | −12.5% | −0.5823 to −0.0458 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.2 | −0.1% | −1.2522 to +0.5963 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 247.7 | −8.8% | −44.0257 to −3.7136 | yes: GAIN |
| response time (ms), mean | 447.4 | 401.5 | −10.3% | −63.6096 to −28.1841 | yes: GAIN |
| response time (ms), 95th percentile | 2716 | 2683 | −1.2% | −121.3347 to +54.2117 | no |
| response time (ms), 99th percentile | 3990 | 4244 | +6.4% | −2.3379 to +511.6607 | no |
| time over the response line (% of samples) | 14.85 | 14.54 | −2.1% | −0.9280 to +0.3140 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.4 | +1.1% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.9 | +11.900 (native is 0) | +10.1658 to +13.6342 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 172.6 | 177.9 | +3.0% | +0.3671 to +10.1563 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05816 | 0.06543 | +12.5% | +0.0002 to +0.0143 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.396 | 1.365 | −2.2% | −0.0581 to −0.0030 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01521 | +0.015 (native is 0) | +0.0140 to +0.0164 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.396 | 1.38 | −1.1% | −0.0434 to +0.0127 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.4 | 437.2 | −7.6% | −70.6181 to −1.7013 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.05 | 2.46 | +20.0% | +0.1550 to +0.6652 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | +0.2358 to +1.3642 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.2358 to +1.3642 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.74 | 40.44 | +1.8% | +0.4514 to +0.9440 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 538 | 544.2 | +1.2% | +2.9692 to +9.4308 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.895 | −18.4% | −2.0549 to −0.1547 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*