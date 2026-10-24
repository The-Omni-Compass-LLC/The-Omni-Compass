# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.968 | 5.968 |
| node-hours | 4.157 | 4.158 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.2 | 443 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.5 | 441.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 153 | 84.45 |
| response time (ms), 95th percentile | 293.1 | 103.1 |
| response time (ms), 99th percentile | 639.1 | 286.1 |
| time over the response line (% of samples) | 2.796 | 1.743 |
| failed requests (%) | 1.379 | 1.219 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.3533 |
| utilisation (used / allocatable) | 0.04551 | 0.04479 |
| CPU used (cores), mean | 1.086 | 1.069 |
| Omni's own CPU (cores), mean | 0 | 0.00758 |
| CPU used with Omni's own (cores), mean | 1.086 | 1.077 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 615.9 | 618.6 |
| HPA replicas, mean | 8.16 | 7.789 |
| pods started | 8.3 | 10.5 |
| pod start wait, total (s) | 11.8 | 18.3 |
| pod start wait, mean (s) | 1.429 | 1.751 |
| host CPU busy, the real machine under kind (%) | 32.77 | 32.6 |
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
| worker nodes in service, mean | 5.968 | 5.968 | +0.0% | -0.003632 to +0.003641 | EVEN, the same (under one part in a million) |
| node-hours | 4.157 | 4.158 | +0.0% | -0.005815 to +0.007149 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.2 | 443 | -0.0% | -0.8823 to +0.444 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.5 | 441.3 | -0.0% | -0.9079 to +0.4696 | no |
| response time (ms), mean | 153 | 84.45 | -44.8% | -91.85 to -45.2 | yes: GAIN |
| response time (ms), 95th percentile | 293.1 | 103.1 | -64.8% | -232.8 to -147.2 | yes: GAIN |
| response time (ms), 99th percentile | 639.1 | 286.1 | -55.2% | -566.6 to -139.4 | yes: GAIN |
| time over the response line (% of samples) | 2.796 | 1.743 | -37.7% | -1.671 to -0.4367 | yes: GAIN |
| failed requests (%) | 1.379 | 1.219 | -11.6% | -0.2937 to -0.02663 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6.2 | -27.9% | -3.798 to -1.002 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.2 | +44.2 (native is 0) | +38.65 to +49.75 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.3533 | +3.4% | -0.2519 to +0.2753 | no |
| utilisation (used / allocatable) | 0.04551 | 0.04479 | -1.6% | -0.001781 to +0.0003579 | no |
| CPU used (cores), mean | 1.086 | 1.069 | -1.6% | -0.04281 to +0.008757 | no |
| Omni's own CPU (cores), mean | 0 | 0.00758 | +0.00758 (native is 0) | +0.006562 to +0.008598 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.086 | 1.077 | -0.9% | -0.03455 to +0.01565 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 615.9 | 618.6 | +0.4% | -12.47 to +17.8 | no |
| HPA replicas, mean | 8.16 | 7.789 | -4.5% | -0.9662 to +0.2252 | no |
| pods started | 8.3 | 10.5 | +26.5% | +1.042 to +3.358 | yes: power given |
| pod start wait, total (s) | 11.8 | 18.3 | +55.1% | +3.84 to +9.16 | yes: LOSS |
| pod start wait, mean (s) | 1.429 | 1.751 | +22.6% | +0.04825 to +0.5968 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 32.77 | 32.6 | -0.5% | -0.8022 to +0.4473 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 75 | 4.0 |  |
| machine down | omni | 28 | 0.9 | -47 s (-62%) |
| spike | native | 234 | 50.3 |  |
| spike | omni | 233 | 49.7 | -1 s (-0%) |
| runaway pod started | native | 3 | 0.3 |  |
| runaway pod started | omni | 2 | 0.0 | -1 s (-26%) |
| probe blind | native | 72 | 1.2 |  |
| probe blind | omni | 54 | 0.0 | -18 s (-25%) |
| api frozen | native | 13 | 0.3 |  |
| api frozen | omni | 3 | 0.0 | -10 s (-78%) |
| metrics down | native | 3 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | -0 s (-16%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*