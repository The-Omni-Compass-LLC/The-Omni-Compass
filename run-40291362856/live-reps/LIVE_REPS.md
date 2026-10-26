# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.971 |
| node-hours | 4.158 | 4.158 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.7 | 443.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 152.3 | 89.7 |
| response time (ms), 95th percentile | 317.4 | 119 |
| response time (ms), 99th percentile | 590.7 | 275.7 |
| time over the response line (% of samples) | 3.338 | 2.106 |
| failed requests (%) | 1.715 | 1.598 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 7.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.2133 |
| utilisation (used / allocatable) | 0.04909 | 0.04836 |
| CPU used (cores), mean | 1.172 | 1.155 |
| Omni's own CPU (cores), mean | 0 | 0.00794 |
| CPU used with Omni's own (cores), mean | 1.172 | 1.163 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 581.5 | 584.7 |
| HPA replicas, mean | 8.314 | 8.58 |
| pods started | 8.5 | 9.2 |
| pod start wait, total (s) | 12.4 | 15.7 |
| pod start wait, mean (s) | 1.459 | 1.697 |
| host CPU busy, the real machine under kind (%) | 35.32 | 34.93 |
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
| worker nodes in service, mean | 5.97 | 5.971 | +0.0% | −0.0039 to +0.0051 | no |
| node-hours | 4.158 | 4.158 | +0.0% | −0.0040 to +0.0044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.2 | 444.9 | −0.1% | −1.1001 to +0.3229 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.7 | 443.3 | −0.1% | −0.9955 to +0.2766 | no |
| response time (ms), mean | 152.3 | 89.7 | −41.1% | −81.1997 to −43.9052 | yes: GAIN |
| response time (ms), 95th percentile | 317.4 | 119 | −62.5% | −241.8364 to −155.0546 | yes: GAIN |
| response time (ms), 99th percentile | 590.7 | 275.7 | −53.3% | −399.8366 to −230.1994 | yes: GAIN |
| time over the response line (% of samples) | 3.338 | 2.106 | −36.9% | −1.6556 to −0.8084 | yes: GAIN |
| failed requests (%) | 1.715 | 1.598 | −6.8% | −0.2246 to −0.0099 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 7.6 | −19.1% | −2.8003 to −0.7997 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 39.8 | +39.800 (native is 0) | +33.7793 to +45.8207 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3183 | 0.2133 | −33.0% | −0.3426 to +0.1326 | no |
| utilisation (used / allocatable) | 0.04909 | 0.04836 | −1.5% | −0.0014 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.172 | 1.155 | −1.5% | −0.0338 to −0.0008 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00794 | +0.008 (native is 0) | +0.0068 to +0.0091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.172 | 1.163 | −0.8% | −0.0251 to +0.0063 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 581.5 | 584.7 | +0.6% | −5.7038 to +12.1352 | no |
| HPA replicas, mean | 8.314 | 8.58 | +3.2% | −0.0362 to +0.5665 | no |
| pods started | 8.5 | 9.2 | +8.2% | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 12.4 | 15.7 | +26.6% | −0.3325 to +6.9325 | no |
| pod start wait, mean (s) | 1.459 | 1.697 | +16.3% | −0.1168 to +0.5936 | no |
| host CPU busy, the real machine under kind (%) | 35.32 | 34.93 | −1.1% | −0.8354 to +0.0612 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 77 | 3.6 |  |
| machine down | omni | 49 | 1.7 | -28 s (-36%) |
| spike | native | 259 | 71.4 |  |
| spike | omni | 260 | 68.3 | +0 s (+0%) |
| runaway pod started | native | 7 | 0.7 |  |
| runaway pod started | omni | 2 | 0.0 | -5 s (-68%) |
| probe blind | native | 82 | 1.3 |  |
| probe blind | omni | 60 | 0.0 | -22 s (-26%) |
| api frozen | native | 7 | 0.2 |  |
| api frozen | omni | 3 | 0.0 | -4 s (-54%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-46%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*