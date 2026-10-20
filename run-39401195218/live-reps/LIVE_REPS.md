# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.92 | 5.906 |
| node-hours | 1.492 | 1.484 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.3 | 164 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.8 | 162.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 217.2 | 119 |
| response time (ms), 95th percentile | 451.8 | 253.1 |
| response time (ms), 99th percentile | 1296 | 751.6 |
| time over the response line (% of samples) | 8.164 | 5.69 |
| failed requests (%) | 4.604 | 3.787 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.078 | 0.865 |
| utilisation (used / allocatable) | 0.06955 | 0.06663 |
| CPU used (cores), mean | 1.647 | 1.573 |
| Omni's own CPU (cores), mean | 0 | 0.01046 |
| CPU used with Omni's own (cores), mean | 1.647 | 1.584 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.8 | 426.5 |
| HPA replicas, mean | 8.425 | 10.35 |
| pods started | 5.5 | 7.3 |
| pod start wait, total (s) | 31.5 | 20.5 |
| pod start wait, mean (s) | 5.709 | 2.459 |
| host CPU busy, the real machine under kind (%) | 47.03 | 45.91 |
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
| worker nodes in service, mean | 5.92 | 5.906 | -0.2% | -0.04106 to +0.01327 | no |
| node-hours | 1.492 | 1.484 | -0.6% | -0.01802 to +0.00119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.3 | 164 | -0.8% | -2.203 to -0.3406 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.8 | 162.2 | -0.9% | -2.751 to -0.3057 | yes: GAIN |
| response time (ms), mean | 217.2 | 119 | -45.2% | -140.8 to -55.61 | yes: GAIN |
| response time (ms), 95th percentile | 451.8 | 253.1 | -44.0% | -268.9 to -128.5 | yes: GAIN |
| response time (ms), 99th percentile | 1296 | 751.6 | -42.0% | -875.7 to -213.6 | yes: GAIN |
| time over the response line (% of samples) | 8.164 | 5.69 | -30.3% | -3.858 to -1.089 | yes: GAIN |
| failed requests (%) | 4.604 | 3.787 | -17.7% | -1.638 to +0.005127 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.8 | -12.1% | -1.856 to +0.2556 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 | +31.3 (native is 0) | +27.79 to +34.81 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.078 | 0.865 | -19.8% | -1.006 to +0.5797 | no |
| utilisation (used / allocatable) | 0.06955 | 0.06663 | -4.2% | -0.004743 to -0.001102 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.647 | 1.573 | -4.5% | -0.1212 to -0.02564 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01046 | +0.0105 (native is 0) | +0.008567 to +0.01235 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.647 | 1.584 | -3.8% | -0.1096 to -0.01635 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.8 | 426.5 | +3.6% | +6.825 to +22.52 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.425 | 10.35 | +22.8% | +1.385 to +2.465 | yes: power given |
| pods started | 5.5 | 7.3 | +32.7% | -0.2176 to +3.818 | no |
| pod start wait, total (s) | 31.5 | 20.5 | -34.9% | -47.74 to +25.74 | no |
| pod start wait, mean (s) | 5.709 | 2.459 | -56.9% | -9.044 to +2.545 | no |
| host CPU busy, the real machine under kind (%) | 47.03 | 45.91 | -2.4% | -2.731 to +0.4864 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 80 | 15.0 |  |
| machine down | omni | 44 | 10.4 | -36 s (-45%) |
| spike | native | 254 | 65.1 |  |
| spike | omni | 249 | 44.7 | -6 s (-2%) |
| runaway pod started | native | 109 | 10.6 |  |
| runaway pod started | omni | 79 | 5.8 | -30 s (-27%) |
| probe blind | native | 62 | 0.2 |  |
| probe blind | omni | 60 | 0.0 | -3 s (-4%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*