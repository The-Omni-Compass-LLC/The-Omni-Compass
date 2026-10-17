# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.913 |
| node-hours | 1.493 | 1.487 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.8 | 164 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.2 | 162.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 194.1 | 124.3 |
| response time (ms), 95th percentile | 387.1 | 190.7 |
| response time (ms), 99th percentile | 1224 | 1103 |
| time over the response line (% of samples) | 7.31 | 5.072 |
| failed requests (%) | 4.221 | 3.503 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 5.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.435 | 0.7117 |
| utilisation (used / allocatable) | 0.06697 | 0.06585 |
| CPU used (cores), mean | 1.585 | 1.558 |
| Omni's own CPU (cores), mean | 0 | 0.00949 |
| CPU used with Omni's own (cores), mean | 1.585 | 1.567 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 424.5 | 427.9 |
| HPA replicas, mean | 8.58 | 10.16 |
| pods started | 5 | 6.7 |
| pod start wait, total (s) | 17 | 21.2 |
| pod start wait, mean (s) | 3.142 | 2.931 |
| host CPU busy, the real machine under kind (%) | 45.49 | 45.07 |
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
| worker nodes in service, mean | 5.917 | 5.913 | -0.1% | -0.008478 to +0.001276 | no |
| node-hours | 1.493 | 1.487 | -0.4% | -0.01398 to +0.002311 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.8 | 164 | -0.5% | -1.84 to +0.1673 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.2 | 162.3 | -0.6% | -1.87 to +0.0722 | no |
| response time (ms), mean | 194.1 | 124.3 | -36.0% | -96.31 to -43.26 | yes: GAIN |
| response time (ms), 95th percentile | 387.1 | 190.7 | -50.7% | -257.2 to -135.4 | yes: GAIN |
| response time (ms), 99th percentile | 1224 | 1103 | -9.9% | -1036 to +794.2 | no |
| time over the response line (% of samples) | 7.31 | 5.072 | -30.6% | -3.067 to -1.409 | yes: GAIN |
| failed requests (%) | 4.221 | 3.503 | -17.0% | -1.079 to -0.3571 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 5.2 | -16.1% | -1.826 to -0.174 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.3 | +32.3 (native is 0) | +27.53 to +37.07 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.435 | 0.7117 | +63.6% | -0.06292 to +0.6163 | no |
| utilisation (used / allocatable) | 0.06697 | 0.06585 | -1.7% | -0.002473 to +0.0002461 | no |
| CPU used (cores), mean | 1.585 | 1.558 | -1.7% | -0.05911 to +0.004803 | no |
| Omni's own CPU (cores), mean | 0 | 0.00949 | +0.00949 (native is 0) | +0.008052 to +0.01093 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.585 | 1.567 | -1.1% | -0.04861 to +0.01329 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 424.5 | 427.9 | +0.8% | -4.605 to +11.3 | no |
| HPA replicas, mean | 8.58 | 10.16 | +18.4% | +0.5948 to +2.565 | yes: power given |
| pods started | 5 | 6.7 | +34.0% | +0.4819 to +2.918 | yes: power given |
| pod start wait, total (s) | 17 | 21.2 | +24.7% | -0.9449 to +9.345 | no |
| pod start wait, mean (s) | 3.142 | 2.931 | -6.7% | -0.7803 to +0.3571 | no |
| host CPU busy, the real machine under kind (%) | 45.49 | 45.07 | -0.9% | -1.162 to +0.3157 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 56 | 13.7 |  |
| machine down | omni | 37 | 9.1 | -19 s (-34%) |
| spike | native | 242 | 54.2 |  |
| spike | omni | 237 | 45.5 | -5 s (-2%) |
| runaway pod started | native | 85 | 9.3 |  |
| runaway pod started | omni | 67 | 5.3 | -18 s (-21%) |
| probe blind | native | 67 | 1.0 |  |
| probe blind | omni | 60 | 0.0 | -7 s (-11%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*