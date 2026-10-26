# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.92 | 5.919 |
| node-hours | 1.495 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 163.9 | 163.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.3 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 207.4 | 107 |
| response time (ms), 95th percentile | 477.9 | 217.7 |
| response time (ms), 99th percentile | 1640 | 655.5 |
| time over the response line (% of samples) | 7.071 | 4.646 |
| failed requests (%) | 3.381 | 3.018 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 4.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3633 | 0.6383 |
| utilisation (used / allocatable) | 0.0618 | 0.06113 |
| CPU used (cores), mean | 1.463 | 1.447 |
| Omni's own CPU (cores), mean | 0 | 0.00856 |
| CPU used with Omni's own (cores), mean | 1.463 | 1.456 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.5 | 463.1 |
| HPA replicas, mean | 8.257 | 9.292 |
| pods started | 5.7 | 6.7 |
| pod start wait, total (s) | 25.8 | 13.2 |
| pod start wait, mean (s) | 3.968 | 1.974 |
| host CPU busy, the real machine under kind (%) | 42.26 | 42.07 |
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
| worker nodes in service, mean | 5.92 | 5.919 | −0.0% | −0.0085 to +0.0082 | no |
| node-hours | 1.495 | 1.491 | −0.2% | −0.0106 to +0.0043 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 163.9 | 163.4 | −0.3% | −1.2618 to +0.2683 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.3 | 161.8 | −0.3% | −1.2490 to +0.2555 | no |
| response time (ms), mean | 207.4 | 107 | −48.4% | −152.3890 to −48.4315 | yes: GAIN |
| response time (ms), 95th percentile | 477.9 | 217.7 | −54.5% | −348.8797 to −171.5593 | yes: GAIN |
| response time (ms), 99th percentile | 1640 | 655.5 | −60.0% | −1689.9699 to −278.1173 | yes: GAIN |
| time over the response line (% of samples) | 7.071 | 4.646 | −34.3% | −3.5573 to −1.2944 | yes: GAIN |
| failed requests (%) | 3.381 | 3.018 | −10.7% | −0.6939 to −0.0313 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 4.8 | −14.3% | −1.5388 to −0.0612 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.9 | +25.900 (native is 0) | +20.2631 to +31.5369 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3633 | 0.6383 | +75.7% | −0.3226 to +0.8726 | no |
| utilisation (used / allocatable) | 0.0618 | 0.06113 | −1.1% | −0.0017 to +0.0004 | no |
| CPU used (cores), mean | 1.463 | 1.447 | −1.1% | −0.0406 to +0.0079 | no |
| Omni's own CPU (cores), mean | 0 | 0.00856 | +0.009 (native is 0) | +0.0067 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.463 | 1.456 | −0.5% | −0.0323 to +0.0167 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.5 | 463.1 | +1.2% | −0.6330 to +11.8541 | no |
| HPA replicas, mean | 8.257 | 9.292 | +12.5% | −0.3944 to +2.4630 | no |
| pods started | 5.7 | 6.7 | +17.5% | +0.0463 to +1.9537 | yes: power given |
| pod start wait, total (s) | 25.8 | 13.2 | −48.8% | −39.0893 to +13.8893 | no |
| pod start wait, mean (s) | 3.968 | 1.974 | −50.2% | −5.7057 to +1.7184 | no |
| host CPU busy, the real machine under kind (%) | 42.26 | 42.07 | −0.4% | −0.8215 to +0.4454 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 47 | 15.3 |  |
| machine down | omni | 39 | 9.0 | -8 s (-18%) |
| spike | native | 216 | 41.9 |  |
| spike | omni | 207 | 34.5 | -9 s (-4%) |
| runaway pod started | native | 67 | 6.7 |  |
| runaway pod started | omni | 54 | 4.8 | -14 s (-20%) |
| probe blind | native | 61 | 0.3 |  |
| probe blind | omni | 60 | 0.0 | -0 s (-1%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*