# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.97 |
| node-hours | 4.156 | 4.161 |
| energy, parked workers still on at idle power (Wh, declared model) | 444.2 | 444.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.6 | 443.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 160.2 | 92.22 |
| response time (ms), 95th percentile | 312.3 | 115.4 |
| response time (ms), 99th percentile | 602.8 | 252.3 |
| time over the response line (% of samples) | 3.131 | 1.88 |
| failed requests (%) | 1.58 | 1.46 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 6.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4033 | 0.2717 |
| utilisation (used / allocatable) | 0.0484 | 0.04755 |
| CPU used (cores), mean | 1.156 | 1.135 |
| Omni's own CPU (cores), mean | 0 | 0.00762 |
| CPU used with Omni's own (cores), mean | 1.156 | 1.143 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 584.8 | 590.2 |
| HPA replicas, mean | 8.392 | 7.99 |
| pods started | 8.7 | 8.3 |
| pod start wait, total (s) | 14 | 14.9 |
| pod start wait, mean (s) | 1.592 | 1.767 |
| host CPU busy, the real machine under kind (%) | 34.73 | 34.29 |
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
| worker nodes in service, mean | 5.969 | 5.97 | +0.0% | −0.0026 to +0.0040 | no |
| node-hours | 4.156 | 4.161 | +0.1% | −0.0004 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 444.2 | 444.7 | +0.1% | −0.2948 to +1.3949 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.6 | 443.2 | +0.1% | −0.3404 to +1.5113 | no |
| response time (ms), mean | 160.2 | 92.22 | −42.4% | −86.6401 to −49.3288 | yes: GAIN |
| response time (ms), 95th percentile | 312.3 | 115.4 | −63.0% | −234.9052 to −158.8948 | yes: GAIN |
| response time (ms), 99th percentile | 602.8 | 252.3 | −58.1% | −414.7670 to −286.0598 | yes: GAIN |
| time over the response line (% of samples) | 3.131 | 1.88 | −39.9% | −1.6068 to −0.8952 | yes: GAIN |
| failed requests (%) | 1.58 | 1.46 | −7.6% | −0.1788 to −0.0617 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 6.7 | −24.7% | −3.1417 to −1.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.8 | +40.800 (native is 0) | +32.2243 to +49.3757 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4033 | 0.2717 | −32.6% | −0.5488 to +0.2854 | no |
| utilisation (used / allocatable) | 0.0484 | 0.04755 | −1.8% | −0.0016 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.156 | 1.135 | −1.8% | −0.0374 to −0.0032 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00762 | +0.008 (native is 0) | +0.0065 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.156 | 1.143 | −1.1% | −0.0289 to +0.0035 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 584.8 | 590.2 | +0.9% | −3.8293 to +14.5984 | no |
| HPA replicas, mean | 8.392 | 7.99 | −4.8% | −0.9580 to +0.1538 | no |
| pods started | 8.7 | 8.3 | −4.6% | −1.8775 to +1.0775 | no |
| pod start wait, total (s) | 14 | 14.9 | +6.4% | −2.9807 to +4.7807 | no |
| pod start wait, mean (s) | 1.592 | 1.767 | +11.0% | −0.2107 to +0.5609 | no |
| host CPU busy, the real machine under kind (%) | 34.73 | 34.29 | −1.3% | −0.8124 to −0.0703 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 65 | 3.3 |  |
| machine down | omni | 33 | 1.2 | -32 s (-49%) |
| spike | native | 257 | 67.7 |  |
| spike | omni | 241 | 63.3 | -17 s (-6%) |
| runaway pod started | native | 2 | 0.3 |  |
| runaway pod started | omni | 3 | 0.0 | +1 s (+53%) |
| probe blind | native | 56 | 1.0 |  |
| probe blind | omni | 54 | 0.1 | -2 s (-3%) |
| api frozen | native | 7 | 0.4 |  |
| api frozen | omni | 4 | 0.0 | -3 s (-42%) |
| metrics down | native | 2 | 0.2 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-25%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*