# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.967 |
| node-hours | 4.156 | 4.153 |
| energy, parked workers still on at idle power (Wh, declared model) | 441.6 | 440.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 440 | 439.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 141.4 | 81.61 |
| response time (ms), 95th percentile | 277.5 | 102.3 |
| response time (ms), 99th percentile | 577.3 | 262.8 |
| time over the response line (% of samples) | 2.441 | 1.499 |
| failed requests (%) | 1.063 | 1.002 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.7133 |
| utilisation (used / allocatable) | 0.04342 | 0.04239 |
| CPU used (cores), mean | 1.037 | 1.012 |
| Omni's own CPU (cores), mean | 0 | 0.00696 |
| CPU used with Omni's own (cores), mean | 1.037 | 1.019 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 646.8 | 658.3 |
| HPA replicas, mean | 7.989 | 7.522 |
| pods started | 8.5 | 9.2 |
| pod start wait, total (s) | 13.2 | 16.4 |
| pod start wait, mean (s) | 1.575 | 1.751 |
| host CPU busy, the real machine under kind (%) | 31.42 | 31.03 |
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
| worker nodes in service, mean | 5.969 | 5.967 | −0.0% | −0.0041 to +0.0004 | no |
| node-hours | 4.156 | 4.153 | −0.1% | −0.0096 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 441.6 | 440.9 | −0.2% | −1.3584 to −0.1418 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 440 | 439.2 | −0.2% | −1.4566 to −0.2352 | yes: GAIN |
| response time (ms), mean | 141.4 | 81.61 | −42.3% | −82.1854 to −37.4185 | yes: GAIN |
| response time (ms), 95th percentile | 277.5 | 102.3 | −63.1% | −219.2740 to −131.0330 | yes: GAIN |
| response time (ms), 99th percentile | 577.3 | 262.8 | −54.5% | −372.0084 to −256.9360 | yes: GAIN |
| time over the response line (% of samples) | 2.441 | 1.499 | −38.6% | −1.4932 to −0.3908 | yes: GAIN |
| failed requests (%) | 1.063 | 1.002 | −5.7% | −0.2031 to +0.0813 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 5.3 | −22.1% | −2.6802 to −0.3198 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.4 | +41.400 (native is 0) | +35.0003 to +47.7997 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.7133 | +122.9% | −0.0757 to +0.8623 | no |
| utilisation (used / allocatable) | 0.04342 | 0.04239 | −2.4% | −0.0016 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.037 | 1.012 | −2.4% | −0.0398 to −0.0104 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00696 | +0.007 (native is 0) | +0.0059 to +0.0080 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.037 | 1.019 | −1.8% | −0.0322 to −0.0041 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 646.8 | 658.3 | +1.8% | +4.6207 to +18.3176 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.989 | 7.522 | −5.8% | −1.0799 to +0.1470 | no |
| pods started | 8.5 | 9.2 | +8.2% | −1.0210 to +2.4210 | no |
| pod start wait, total (s) | 13.2 | 16.4 | +24.2% | −1.5663 to +7.9663 | no |
| pod start wait, mean (s) | 1.575 | 1.751 | +11.2% | −0.1638 to +0.5158 | no |
| host CPU busy, the real machine under kind (%) | 31.42 | 31.03 | −1.3% | −0.8644 to +0.0765 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 50 | 2.7 |  |
| machine down | omni | 28 | 1.1 | -22 s (-44%) |
| spike | native | 230 | 44.2 |  |
| spike | omni | 221 | 37.8 | -10 s (-4%) |
| runaway pod started | native | 2 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | +0 s (+8%) |
| probe blind | native | 55 | 0.8 |  |
| probe blind | omni | 60 | 0.0 | +5 s (+10%) |
| api frozen | native | 12 | 0.3 |  |
| api frozen | omni | 2 | 0.0 | -9 s (-80%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | -0 s (-17%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*