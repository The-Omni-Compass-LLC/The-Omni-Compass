# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.971 | 5.968 |
| node-hours | 4.156 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 446.3 | 446.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.7 | 444.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 171.9 | 93.25 |
| response time (ms), 95th percentile | 340.5 | 123.6 |
| response time (ms), 99th percentile | 579.9 | 248.5 |
| time over the response line (% of samples) | 3.421 | 2.065 |
| failed requests (%) | 1.799 | 1.681 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3133 | 0.4117 |
| utilisation (used / allocatable) | 0.05116 | 0.051 |
| CPU used (cores), mean | 1.222 | 1.217 |
| Omni's own CPU (cores), mean | 0 | 0.02442 |
| CPU used with Omni's own (cores), mean | 1.222 | 1.242 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 547.1 | 541 |
| HPA replicas, mean | 8.69 | 9.248 |
| pods started | 8 | 10.6 |
| pod start wait, total (s) | 11.4 | 17.2 |
| pod start wait, mean (s) | 1.423 | 1.641 |
| host CPU busy, the real machine under kind (%) | 36.69 | 37.29 |
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
| worker nodes in service, mean | 5.971 | 5.968 | -0.0% | -0.006809 to +0.001934 | no |
| node-hours | 4.156 | 4.159 | +0.1% | -0.0006435 to +0.006866 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 446.3 | 446.3 | +0.0% | -1.478 to +1.549 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.7 | 444.7 | -0.0% | -1.631 to +1.444 | no |
| response time (ms), mean | 171.9 | 93.25 | -45.8% | -98.57 to -58.81 | yes: GAIN |
| response time (ms), 95th percentile | 340.5 | 123.6 | -63.7% | -252.9 to -180.9 | yes: GAIN |
| response time (ms), 99th percentile | 579.9 | 248.5 | -57.2% | -438.3 to -224.6 | yes: GAIN |
| time over the response line (% of samples) | 3.421 | 2.065 | -39.6% | -1.987 to -0.7249 | yes: GAIN |
| failed requests (%) | 1.799 | 1.681 | -6.6% | -0.2101 to -0.02594 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 7.4 | -22.1% | -3.137 to -1.063 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 62.1 | +62.1 (native is 0) | +53.31 to +70.89 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3133 | 0.4117 | +31.4% | -0.3249 to +0.5216 | no |
| utilisation (used / allocatable) | 0.05116 | 0.051 | -0.3% | -0.001262 to +0.0009395 | no |
| CPU used (cores), mean | 1.222 | 1.217 | -0.4% | -0.03052 to +0.02167 | no |
| Omni's own CPU (cores), mean | 0 | 0.02442 | +0.0244 (native is 0) | +0.02104 to +0.0278 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.222 | 1.242 | +1.6% | -0.003985 to +0.04397 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 547.1 | 541 | -1.1% | -30.38 to +18.33 | no |
| HPA replicas, mean | 8.69 | 9.248 | +6.4% | -0.2711 to +1.386 | no |
| pods started | 8 | 10.6 | +32.5% | +0.7469 to +4.453 | yes: power given |
| pod start wait, total (s) | 11.4 | 17.2 | +50.9% | +2.365 to +9.235 | yes: LOSS |
| pod start wait, mean (s) | 1.423 | 1.641 | +15.3% | +0.002066 to +0.4334 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.69 | 37.29 | +1.6% | +0.07626 to +1.128 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 84 | 4.4 |  |
| machine down | omni | 40 | 1.1 | -44 s (-52%) |
| spike | native | 275 | 75.6 |  |
| spike | omni | 273 | 70.0 | -2 s (-1%) |
| runaway pod started | native | 4 | 0.4 |  |
| runaway pod started | omni | 3 | 0.1 | -1 s (-18%) |
| probe blind | native | 78 | 1.3 |  |
| probe blind | omni | 61 | 0.1 | -17 s (-22%) |
| api frozen | native | 8 | 0.2 |  |
| api frozen | omni | 3 | 0.0 | -5 s (-67%) |
| metrics down | native | 3 | 0.0 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-52%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*