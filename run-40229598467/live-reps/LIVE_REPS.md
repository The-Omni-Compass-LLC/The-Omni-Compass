# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.912 |
| node-hours | 1.498 | 1.486 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.5 | 163.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 162.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 214.4 | 110.5 |
| response time (ms), 95th percentile | 422 | 206.9 |
| response time (ms), 99th percentile | 1616 | 653.7 |
| time over the response line (% of samples) | 8.134 | 5.398 |
| failed requests (%) | 4.665 | 3.819 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 5.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 1.035 |
| utilisation (used / allocatable) | 0.06739 | 0.06589 |
| CPU used (cores), mean | 1.595 | 1.558 |
| Omni's own CPU (cores), mean | 0 | 0.00989 |
| CPU used with Omni's own (cores), mean | 1.595 | 1.568 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.6 | 430.6 |
| HPA replicas, mean | 8.376 | 10.08 |
| pods started | 5.5 | 6.7 |
| pod start wait, total (s) | 16 | 19.6 |
| pod start wait, mean (s) | 3.01 | 2.848 |
| host CPU busy, the real machine under kind (%) | 45.62 | 45.2 |
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
| worker nodes in service, mean | 5.917 | 5.912 | −0.1% | −0.0115 to +0.0006 | no |
| node-hours | 1.498 | 1.486 | −0.8% | −0.0212 to −0.0042 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 165.5 | 163.9 | −1.0% | −2.6826 to −0.4985 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 162.3 | −1.0% | −2.7899 to −0.5745 | yes: GAIN |
| response time (ms), mean | 214.4 | 110.5 | −48.5% | −138.0399 to −69.7803 | yes: GAIN |
| response time (ms), 95th percentile | 422 | 206.9 | −51.0% | −264.3534 to −165.8906 | yes: GAIN |
| response time (ms), 99th percentile | 1616 | 653.7 | −59.5% | −1747.9168 to −176.5820 | yes: GAIN |
| time over the response line (% of samples) | 8.134 | 5.398 | −33.6% | −3.5674 to −1.9041 | yes: GAIN |
| failed requests (%) | 4.665 | 3.819 | −18.2% | −1.2687 to −0.4249 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 5.2 | −22.4% | −2.2726 to −0.7274 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.9 | +29.900 (native is 0) | +25.2957 to +34.5043 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.33 | 1.035 | +213.6% | +0.1847 to +1.2253 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06739 | 0.06589 | −2.2% | −0.0039 to +0.0009 | no |
| CPU used (cores), mean | 1.595 | 1.558 | −2.3% | −0.0937 to +0.0201 | no |
| Omni's own CPU (cores), mean | 0 | 0.00989 | +0.010 (native is 0) | +0.0081 to +0.0117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.595 | 1.568 | −1.7% | −0.0825 to +0.0287 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.6 | 430.6 | +0.7% | −12.0374 to +18.1798 | no |
| HPA replicas, mean | 8.376 | 10.08 | +20.3% | +0.5595 to +2.8448 | yes: power given |
| pods started | 5.5 | 6.7 | +21.8% | −0.2621 to +2.6621 | no |
| pod start wait, total (s) | 16 | 19.6 | +22.5% | −23.0498 to +30.2498 | no |
| pod start wait, mean (s) | 3.01 | 2.848 | −5.4% | −4.6650 to +4.3428 | no |
| host CPU busy, the real machine under kind (%) | 45.62 | 45.2 | −0.9% | −1.5053 to +0.6673 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 64 | 16.1 |  |
| machine down | omni | 37 | 9.6 | -27 s (-42%) |
| spike | native | 247 | 60.5 |  |
| spike | omni | 244 | 54.1 | -3 s (-1%) |
| runaway pod started | native | 111 | 10.1 |  |
| runaway pod started | omni | 75 | 6.1 | -37 s (-33%) |
| probe blind | native | 61 | 0.2 |  |
| probe blind | omni | 60 | 0.0 | -1 s (-2%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*