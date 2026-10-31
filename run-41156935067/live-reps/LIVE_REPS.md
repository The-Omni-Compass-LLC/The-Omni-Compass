# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.913 |
| node-hours | 1.494 | 1.495 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.6 | 164 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 212.6 | 106 |
| response time (ms), 95th percentile | 379.7 | 161.8 |
| response time (ms), 99th percentile | 1500 | 550 |
| time over the response line (% of samples) | 8.199 | 5.551 |
| failed requests (%) | 5.344 | 4.498 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8533 | 0.5467 |
| utilisation (used / allocatable) | 0.07265 | 0.06937 |
| CPU used (cores), mean | 1.718 | 1.641 |
| Omni's own CPU (cores), mean | 0 | 0.01126 |
| CPU used with Omni's own (cores), mean | 1.718 | 1.652 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 391.6 | 404.7 |
| HPA replicas, mean | 8.652 | 10.79 |
| pods started | 5.1 | 6.8 |
| pod start wait, total (s) | 9.2 | 12 |
| pod start wait, mean (s) | 1.787 | 1.712 |
| host CPU busy, the real machine under kind (%) | 49.22 | 47.74 |
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
| worker nodes in service, mean | 5.913 | 5.913 | +0.0% | −0.0005 to +0.0009 | no |
| node-hours | 1.494 | 1.495 | +0.1% | −0.0037 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.6 | −0.4% | −1.0514 to −0.1677 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.6 | 164 | −0.4% | −1.0513 to −0.1637 | yes: GAIN |
| response time (ms), mean | 212.6 | 106 | −50.1% | −147.1765 to −65.9823 | yes: GAIN |
| response time (ms), 95th percentile | 379.7 | 161.8 | −57.4% | −260.3385 to −175.3885 | yes: GAIN |
| response time (ms), 99th percentile | 1500 | 550 | −63.3% | −1853.0014 to −46.0976 | yes: GAIN |
| time over the response line (% of samples) | 8.199 | 5.551 | −32.3% | −3.6186 to −1.6784 | yes: GAIN |
| failed requests (%) | 5.344 | 4.498 | −15.8% | −1.3581 to −0.3322 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.6 | −20.0% | −2.4769 to −0.3231 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 | +27.500 (native is 0) | +22.7045 to +32.2955 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8533 | 0.5467 | −35.9% | −0.8381 to +0.2248 | no |
| utilisation (used / allocatable) | 0.07265 | 0.06937 | −4.5% | −0.0055 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.718 | 1.641 | −4.5% | −0.1293 to −0.0254 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01126 | +0.011 (native is 0) | +0.0099 to +0.0126 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.718 | 1.652 | −3.8% | −0.1170 to −0.0152 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 391.6 | 404.7 | +3.4% | +3.6876 to +22.6114 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.652 | 10.79 | +24.7% | +0.9922 to +3.2829 | yes: power given |
| pods started | 5.1 | 6.8 | +33.3% | +0.3491 to +3.0509 | yes: power given |
| pod start wait, total (s) | 9.2 | 12 | +30.4% | −2.7999 to +8.3999 | no |
| pod start wait, mean (s) | 1.787 | 1.712 | −4.2% | −0.6819 to +0.5329 | no |
| host CPU busy, the real machine under kind (%) | 49.22 | 47.74 | −3.0% | −2.8115 to −0.1473 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 69 | 14.3 |  |
| machine down | omni | 47 | 10.1 | -22 s (-32%) |
| spike | native | 264 | 70.1 |  |
| spike | omni | 263 | 50.5 | -1 s (-0%) |
| runaway pod started | native | 131 | 12.5 |  |
| runaway pod started | omni | 78 | 6.0 | -53 s (-40%) |
| probe blind | native | 68 | 0.6 |  |
| probe blind | omni | 60 | 0.0 | -8 s (-12%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*