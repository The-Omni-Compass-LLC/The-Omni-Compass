# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.798 |
| node-hours | 2.516 | 2.426 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 270.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 652.3 | 588.6 |
| response time (ms), 95th percentile | 3544 | 3548 |
| response time (ms), 99th percentile | 4564 | 4643 |
| time over the response line (% of samples) | 19.66 | 18.4 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 215.9 | 216.3 |
| utilisation (used / allocatable) | 0.07118 | 0.07389 |
| CPU used (cores), mean | 1.708 | 1.711 |
| Omni's own CPU (cores), mean | 0 | 0.0181 |
| CPU used with Omni's own (cores), mean | 1.708 | 1.729 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 388.7 | 379.4 |
| HPA replicas, mean | 2.433 | 2.49 |
| pods started | 0 | 0.7 |
| pod start wait, total (s) | 0 | 0.8 |
| pod start wait, mean (s) | 0 | 0.8 |
| host CPU busy, the real machine under kind (%) | 49.52 | 50.21 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 682.9 | 685.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.647 |

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
| worker nodes in service, mean | 6 | 5.798 | −3.4% | −0.4705 to +0.0667 | no |
| node-hours | 2.516 | 2.426 | −3.6% | −0.2054 to +0.0263 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.5 | −0.1% | −1.3601 to +0.9233 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 270.2 | −2.4% | −15.2943 to +2.2242 | no |
| response time (ms), mean | 652.3 | 588.6 | −9.8% | −71.8610 to −55.7003 | yes: GAIN |
| response time (ms), 95th percentile | 3544 | 3548 | +0.1% | −67.1363 to +74.3703 | no |
| response time (ms), 99th percentile | 4564 | 4643 | +1.7% | −99.2584 to +257.4784 | no |
| time over the response line (% of samples) | 19.66 | 18.4 | −6.4% | −1.6354 to −0.8878 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.6 | 11.5 | −0.9% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.5 | +11.500 (native is 0) | +10.5921 to +12.4079 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 215.9 | 216.3 | +0.2% | −4.6645 to +5.4378 | no |
| utilisation (used / allocatable) | 0.07118 | 0.07389 | +3.8% | −0.0014 to +0.0068 | no |
| CPU used (cores), mean | 1.708 | 1.711 | +0.2% | −0.0430 to +0.0483 | no |
| Omni's own CPU (cores), mean | 0 | 0.0181 | +0.018 (native is 0) | +0.0166 to +0.0196 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.708 | 1.729 | +1.2% | −0.0256 to +0.0670 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 388.7 | 379.4 | −2.4% | −26.9994 to +8.3705 | no |
| HPA replicas, mean | 2.433 | 2.49 | +2.4% | −0.3120 to +0.4267 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.3545 to +1.0455 | yes: power given |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | +0.2358 to +1.3642 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.2358 to +1.3642 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.52 | 50.21 | +1.4% | +0.4033 to +0.9693 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 682.9 | 685.9 | +0.4% | −0.9898 to +6.9898 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.647 | −5.9% | −0.7937 to +0.0881 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*