# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.917 |
| node-hours | 1.493 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 164.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 163 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 198.3 | 110.2 |
| response time (ms), 95th percentile | 376.2 | 174.4 |
| response time (ms), 99th percentile | 1377 | 471.5 |
| time over the response line (% of samples) | 7.283 | 5.218 |
| failed requests (%) | 4.551 | 3.968 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.655 |
| utilisation (used / allocatable) | 0.06735 | 0.06677 |
| CPU used (cores), mean | 1.593 | 1.58 |
| Omni's own CPU (cores), mean | 0 | 0.00961 |
| CPU used with Omni's own (cores), mean | 1.593 | 1.59 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.2 | 423.9 |
| HPA replicas, mean | 8.461 | 10.01 |
| pods started | 5.5 | 6.6 |
| pod start wait, total (s) | 9.3 | 12.1 |
| pod start wait, mean (s) | 1.704 | 1.866 |
| host CPU busy, the real machine under kind (%) | 45.88 | 45.52 |
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
| worker nodes in service, mean | 5.914 | 5.917 | +0.1% | -0.001837 to +0.008281 | no |
| node-hours | 1.493 | 1.491 | -0.1% | -0.01024 to +0.005958 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 164.6 | -0.3% | -1.336 to +0.4758 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 163 | -0.2% | -1.309 to +0.5782 | no |
| response time (ms), mean | 198.3 | 110.2 | -44.4% | -131.9 to -44.37 | yes: GAIN |
| response time (ms), 95th percentile | 376.2 | 174.4 | -53.6% | -265.7 to -137.9 | yes: GAIN |
| response time (ms), 99th percentile | 1377 | 471.5 | -65.8% | -1690 to -120.7 | yes: GAIN |
| time over the response line (% of samples) | 7.283 | 5.218 | -28.3% | -3.099 to -1.03 | yes: GAIN |
| failed requests (%) | 4.551 | 3.968 | -12.8% | -1.015 to -0.1505 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.3 | -19.7% | -2.129 to -0.4706 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 | +28.8 (native is 0) | +22.25 to +35.35 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1083 | 0.655 | +504.6% | +0.1719 to +0.9215 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06735 | 0.06677 | -0.9% | -0.001869 to +0.000702 | no |
| CPU used (cores), mean | 1.593 | 1.58 | -0.8% | -0.04377 to +0.0178 | no |
| Omni's own CPU (cores), mean | 0 | 0.00961 | +0.00961 (native is 0) | +0.007938 to +0.01128 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.593 | 1.59 | -0.2% | -0.03311 to +0.02635 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.2 | 423.9 | +0.6% | -3.814 to +9.253 | no |
| HPA replicas, mean | 8.461 | 10.01 | +18.3% | +0.4235 to +2.674 | yes: power given |
| pods started | 5.5 | 6.6 | +20.0% | -0.7299 to +2.93 | no |
| pod start wait, total (s) | 9.3 | 12.1 | +30.1% | -0.2868 to +5.887 | no |
| pod start wait, mean (s) | 1.704 | 1.866 | +9.5% | -0.09917 to +0.4245 | no |
| host CPU busy, the real machine under kind (%) | 45.88 | 45.52 | -0.8% | -1.007 to +0.2808 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 63 | 13.9 |  |
| machine down | omni | 44 | 9.4 | -19 s (-30%) |
| spike | native | 244 | 56.0 |  |
| spike | omni | 239 | 45.4 | -6 s (-2%) |
| runaway pod started | native | 96 | 9.7 |  |
| runaway pod started | omni | 72 | 5.7 | -24 s (-25%) |
| probe blind | native | 72 | 0.7 |  |
| probe blind | omni | 54 | 0.0 | -18 s (-25%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*