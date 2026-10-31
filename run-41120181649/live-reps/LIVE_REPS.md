# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.913 |
| node-hours | 1.493 | 1.495 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.6 | 166 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.9 | 164.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 260.2 | 120 |
| response time (ms), 95th percentile | 414.3 | 159.2 |
| response time (ms), 99th percentile | 1430 | 435.1 |
| time over the response line (% of samples) | 9.232 | 5.526 |
| failed requests (%) | 5.894 | 4.696 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9383 | 0.4883 |
| utilisation (used / allocatable) | 0.07456 | 0.07087 |
| CPU used (cores), mean | 1.763 | 1.676 |
| Omni's own CPU (cores), mean | 0 | 0.01137 |
| CPU used with Omni's own (cores), mean | 1.763 | 1.688 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 379.2 | 396.5 |
| HPA replicas, mean | 8.745 | 10.61 |
| pods started | 5 | 5.9 |
| pod start wait, total (s) | 7.2 | 20 |
| pod start wait, mean (s) | 1.426 | 3.258 |
| host CPU busy, the real machine under kind (%) | 50.51 | 48.81 |
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
| worker nodes in service, mean | 5.913 | 5.913 | +0.0% | −0.0000 to +0.0007 | no |
| node-hours | 1.493 | 1.495 | +0.1% | +0.0005 to +0.0039 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 166.6 | 166 | −0.3% | −0.9337 to −0.1452 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.9 | 164.4 | −0.3% | −0.9317 to −0.1388 | yes: GAIN |
| response time (ms), mean | 260.2 | 120 | −53.9% | −188.2041 to −92.1570 | yes: GAIN |
| response time (ms), 95th percentile | 414.3 | 159.2 | −61.6% | −300.4836 to −209.6384 | yes: GAIN |
| response time (ms), 99th percentile | 1430 | 435.1 | −69.6% | −1610.1633 to −378.7779 | yes: GAIN |
| time over the response line (% of samples) | 9.232 | 5.526 | −40.2% | −4.6269 to −2.7870 | yes: GAIN |
| failed requests (%) | 5.894 | 4.696 | −20.3% | −1.9448 to −0.4510 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 5.6 | −28.2% | −3.1417 to −1.2583 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.5 | +27.500 (native is 0) | +22.7283 to +32.2717 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9383 | 0.4883 | −48.0% | −1.0023 to +0.1023 | no |
| utilisation (used / allocatable) | 0.07456 | 0.07087 | −4.9% | −0.0054 to −0.0020 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.763 | 1.676 | −4.9% | −0.1275 to −0.0468 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01137 | +0.011 (native is 0) | +0.0097 to +0.0130 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.763 | 1.688 | −4.3% | −0.1150 to −0.0365 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 379.2 | 396.5 | +4.6% | +9.5716 to +24.9435 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.745 | 10.61 | +21.3% | +0.6671 to +3.0587 | yes: power given |
| pods started | 5 | 5.9 | +18.0% | −0.8342 to +2.6342 | no |
| pod start wait, total (s) | 7.2 | 20 | +177.8% | −6.8208 to +32.4208 | no |
| pod start wait, mean (s) | 1.426 | 3.258 | +128.4% | −1.2684 to +4.9312 | no |
| host CPU busy, the real machine under kind (%) | 50.51 | 48.81 | −3.4% | −2.7378 to −0.6688 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 95 | 16.4 |  |
| machine down | omni | 45 | 8.8 | -50 s (-53%) |
| spike | native | 277 | 74.7 |  |
| spike | omni | 267 | 57.6 | -10 s (-4%) |
| runaway pod started | native | 150 | 14.8 |  |
| runaway pod started | omni | 94 | 7.2 | -56 s (-38%) |
| probe blind | native | 72 | 0.8 |  |
| probe blind | omni | 60 | 0.1 | -12 s (-17%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*