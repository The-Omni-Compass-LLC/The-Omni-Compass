# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.915 |
| node-hours | 1.494 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.4 | 165.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 164 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 220.2 | 137.2 |
| response time (ms), 95th percentile | 401.3 | 169.5 |
| response time (ms), 99th percentile | 1313 | 1044 |
| time over the response line (% of samples) | 8.454 | 6.062 |
| failed requests (%) | 5.475 | 4.69 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.8367 |
| utilisation (used / allocatable) | 0.07297 | 0.07191 |
| CPU used (cores), mean | 1.727 | 1.701 |
| Omni's own CPU (cores), mean | 0 | 0.01035 |
| CPU used with Omni's own (cores), mean | 1.727 | 1.712 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 390.9 | 393.4 |
| HPA replicas, mean | 8.628 | 9.47 |
| pods started | 5.1 | 5.7 |
| pod start wait, total (s) | 24.3 | 30.1 |
| pod start wait, mean (s) | 4.957 | 5.408 |
| host CPU busy, the real machine under kind (%) | 49.66 | 49.16 |
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
| worker nodes in service, mean | 5.915 | 5.915 | −0.0% | −0.0064 to +0.0057 | no |
| node-hours | 1.494 | 1.49 | −0.3% | −0.0124 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.4 | 165.6 | −0.4% | −1.5434 to +0.0942 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 164 | −0.4% | −1.5435 to +0.0901 | no |
| response time (ms), mean | 220.2 | 137.2 | −37.7% | −134.4674 to −31.5764 | yes: GAIN |
| response time (ms), 95th percentile | 401.3 | 169.5 | −57.8% | −271.3293 to −192.3447 | yes: GAIN |
| response time (ms), 99th percentile | 1313 | 1044 | −20.5% | −1042.0433 to +503.0891 | no |
| time over the response line (% of samples) | 8.454 | 6.062 | −28.3% | −3.6317 to −1.1521 | yes: GAIN |
| failed requests (%) | 5.475 | 4.69 | −14.3% | −1.6164 to +0.0459 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 6 | −22.1% | −2.9639 to −0.4361 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.9 | +27.900 (native is 0) | +25.1513 to +30.6487 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.8367 | +83.9% | −0.4575 to +1.2208 | no |
| utilisation (used / allocatable) | 0.07297 | 0.07191 | −1.4% | −0.0038 to +0.0017 | no |
| CPU used (cores), mean | 1.727 | 1.701 | −1.5% | −0.0913 to +0.0410 | no |
| Omni's own CPU (cores), mean | 0 | 0.01035 | +0.010 (native is 0) | +0.0089 to +0.0118 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.727 | 1.712 | −0.9% | −0.0804 to +0.0507 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 390.9 | 393.4 | +0.6% | −10.0793 to +14.9477 | no |
| HPA replicas, mean | 8.628 | 9.47 | +9.8% | −0.1441 to +1.8288 | no |
| pods started | 5.1 | 5.7 | +11.8% | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 24.3 | 30.1 | +23.9% | −38.4101 to +50.0101 | no |
| pod start wait, mean (s) | 4.957 | 5.408 | +9.1% | −8.0622 to +8.9658 | no |
| host CPU busy, the real machine under kind (%) | 49.66 | 49.16 | −1.0% | −1.9586 to +0.9572 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 57 | 13.9 |  |
| machine down | omni | 32 | 8.9 | -25 s (-44%) |
| spike | native | 265 | 70.7 |  |
| spike | omni | 265 | 68.4 | -0 s (-0%) |
| runaway pod started | native | 140 | 16.0 |  |
| runaway pod started | omni | 107 | 10.5 | -33 s (-24%) |
| probe blind | native | 79 | 1.5 |  |
| probe blind | omni | 60 | 0.1 | -19 s (-24%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*