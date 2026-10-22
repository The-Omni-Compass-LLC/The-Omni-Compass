# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.916 |
| node-hours | 1.497 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.1 | 163.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.5 | 162.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 215 | 149.4 |
| response time (ms), 95th percentile | 393.6 | 273.1 |
| response time (ms), 99th percentile | 1994 | 1600 |
| time over the response line (% of samples) | 6.873 | 5.35 |
| failed requests (%) | 3.492 | 2.787 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.525 | 0.9917 |
| utilisation (used / allocatable) | 0.06197 | 0.06247 |
| CPU used (cores), mean | 1.466 | 1.478 |
| Omni's own CPU (cores), mean | 0 | 0.02677 |
| CPU used with Omni's own (cores), mean | 1.466 | 1.505 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.8 | 453.2 |
| HPA replicas, mean | 8.137 | 10.19 |
| pods started | 6.1 | 11 |
| pod start wait, total (s) | 26.6 | 45.2 |
| pod start wait, mean (s) | 3.993 | 4.056 |
| host CPU busy, the real machine under kind (%) | 42.33 | 43.35 |
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
| worker nodes in service, mean | 5.914 | 5.916 | +0.0% | -0.005235 to +0.008506 | no |
| node-hours | 1.497 | 1.493 | -0.2% | -0.01183 to +0.004442 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.1 | 163.9 | -0.2% | -1.179 to +0.6688 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.5 | 162.3 | -0.1% | -1.166 to +0.7263 | no |
| response time (ms), mean | 215 | 149.4 | -30.5% | -142.4 to +11.24 | no |
| response time (ms), 95th percentile | 393.6 | 273.1 | -30.6% | -194.4 to -46.66 | yes: GAIN |
| response time (ms), 99th percentile | 1994 | 1600 | -19.8% | -963.4 to +174.4 | no |
| time over the response line (% of samples) | 6.873 | 5.35 | -22.2% | -2.577 to -0.4702 | yes: GAIN |
| failed requests (%) | 3.492 | 2.787 | -20.2% | -1.266 to -0.1435 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.6 | 4.7 | -16.1% | -1.756 to -0.04362 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44 | +44 (native is 0) | +39.6 to +48.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.525 | 0.9917 | +88.9% | -0.0277 to +0.961 | no |
| utilisation (used / allocatable) | 0.06197 | 0.06247 | +0.8% | -0.0008866 to +0.001867 | no |
| CPU used (cores), mean | 1.466 | 1.478 | +0.8% | -0.02051 to +0.04463 | no |
| Omni's own CPU (cores), mean | 0 | 0.02677 | +0.0268 (native is 0) | +0.02254 to +0.031 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.466 | 1.505 | +2.6% | +0.008084 to +0.06957 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.8 | 453.2 | -1.4% | -17.79 to +4.468 | no |
| HPA replicas, mean | 8.137 | 10.19 | +25.2% | +1.253 to +2.855 | yes: power given |
| pods started | 6.1 | 11 | +80.3% | +3.863 to +5.937 | yes: power given |
| pod start wait, total (s) | 26.6 | 45.2 | +69.9% | +0.3781 to +36.82 | yes: LOSS |
| pod start wait, mean (s) | 3.993 | 4.056 | +1.6% | -2.475 to +2.601 | no |
| host CPU busy, the real machine under kind (%) | 42.33 | 43.35 | +2.4% | +0.2295 to +1.817 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 47 | 14.3 |  |
| machine down | omni | 31 | 10.7 | -16 s (-34%) |
| spike | native | 218 | 46.3 |  |
| spike | omni | 218 | 41.3 | -1 s (-0%) |
| runaway pod started | native | 85 | 7.2 |  |
| runaway pod started | omni | 59 | 5.1 | -26 s (-31%) |
| probe blind | native | 64 | 0.3 |  |
| probe blind | omni | 60 | 0.1 | -4 s (-6%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*