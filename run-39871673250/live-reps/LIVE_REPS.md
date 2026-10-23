# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.971 | 5.967 |
| node-hours | 4.155 | 4.156 |
| energy, parked workers still on at idle power (Wh, declared model) | 444.1 | 444 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.7 | 442.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 152.3 | 85.67 |
| response time (ms), 95th percentile | 306.9 | 113.3 |
| response time (ms), 99th percentile | 692.2 | 351.3 |
| time over the response line (% of samples) | 3.272 | 2.083 |
| failed requests (%) | 1.526 | 1.38 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3717 | 0.765 |
| utilisation (used / allocatable) | 0.04791 | 0.04668 |
| CPU used (cores), mean | 1.144 | 1.114 |
| Omni's own CPU (cores), mean | 0 | 0.02329 |
| CPU used with Omni's own (cores), mean | 1.144 | 1.137 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 596.8 | 607.9 |
| HPA replicas, mean | 8.2 | 8.247 |
| pods started | 8.4 | 10.9 |
| pod start wait, total (s) | 13.6 | 19.2 |
| pod start wait, mean (s) | 1.625 | 1.755 |
| host CPU busy, the real machine under kind (%) | 34.38 | 34.44 |
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
| worker nodes in service, mean | 5.971 | 5.967 | -0.1% | -0.009069 to +0.0004356 | no |
| node-hours | 4.155 | 4.156 | +0.0% | -0.001591 to +0.003869 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 444.1 | 444 | -0.0% | -0.8729 to +0.5243 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.7 | 442.3 | -0.1% | -1.058 to +0.2553 | no |
| response time (ms), mean | 152.3 | 85.67 | -43.7% | -88.1 to -45.14 | yes: GAIN |
| response time (ms), 95th percentile | 306.9 | 113.3 | -63.1% | -229.1 to -158 | yes: GAIN |
| response time (ms), 99th percentile | 692.2 | 351.3 | -49.2% | -446.2 to -235.6 | yes: GAIN |
| time over the response line (% of samples) | 3.272 | 2.083 | -36.3% | -1.699 to -0.6792 | yes: GAIN |
| failed requests (%) | 1.526 | 1.38 | -9.6% | -0.3182 to +0.02652 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 6.9 | -22.5% | -3.582 to -0.4184 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.7 | +61.7 (native is 0) | +52.74 to +70.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3717 | 0.765 | +105.8% | -0.02742 to +0.8141 | no |
| utilisation (used / allocatable) | 0.04791 | 0.04668 | -2.6% | -0.002091 to -0.0003701 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.144 | 1.114 | -2.6% | -0.05108 to -0.009517 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02329 | +0.0233 (native is 0) | +0.0194 to +0.02718 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.144 | 1.137 | -0.6% | -0.02487 to +0.01086 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 596.8 | 607.9 | +1.9% | +3.778 to +18.35 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.2 | 8.247 | +0.6% | -0.6645 to +0.7581 | no |
| pods started | 8.4 | 10.9 | +29.8% | +1.531 to +3.469 | yes: power given |
| pod start wait, total (s) | 13.6 | 19.2 | +41.2% | +1.903 to +9.297 | yes: LOSS |
| pod start wait, mean (s) | 1.625 | 1.755 | +8.0% | -0.1495 to +0.4093 | no |
| host CPU busy, the real machine under kind (%) | 34.38 | 34.44 | +0.2% | -0.3425 to +0.4574 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 57 | 3.2 |  |
| machine down | omni | 29 | 1.0 | -29 s (-50%) |
| spike | native | 252 | 65.8 |  |
| spike | omni | 249 | 64.3 | -3 s (-1%) |
| runaway pod started | native | 5 | 0.2 |  |
| runaway pod started | omni | 3 | 0.0 | -3 s (-51%) |
| probe blind | native | 69 | 1.0 |  |
| probe blind | omni | 60 | 0.0 | -8 s (-12%) |
| api frozen | native | 19 | 0.5 |  |
| api frozen | omni | 1 | 0.0 | -18 s (-93%) |
| metrics down | native | 3 | 0.1 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-38%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*