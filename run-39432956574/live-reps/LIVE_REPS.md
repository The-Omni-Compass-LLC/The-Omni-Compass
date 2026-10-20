# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.913 |
| node-hours | 1.493 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 163.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 238.6 | 134 |
| response time (ms), 95th percentile | 394.5 | 152.3 |
| response time (ms), 99th percentile | 1425 | 685.5 |
| time over the response line (% of samples) | 8.199 | 5.495 |
| failed requests (%) | 5.408 | 4.524 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.875 | 0.6383 |
| utilisation (used / allocatable) | 0.07306 | 0.07045 |
| CPU used (cores), mean | 1.729 | 1.666 |
| Omni's own CPU (cores), mean | 0 | 0.01067 |
| CPU used with Omni's own (cores), mean | 1.729 | 1.677 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 381.2 | 393.3 |
| HPA replicas, mean | 8.84 | 10.78 |
| pods started | 5 | 5.5 |
| pod start wait, total (s) | 8 | 11 |
| pod start wait, mean (s) | 1.587 | 1.917 |
| host CPU busy, the real machine under kind (%) | 49.7 | 48.89 |
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
| worker nodes in service, mean | 5.915 | 5.913 | -0.0% | -0.005875 to +0.002318 | no |
| node-hours | 1.493 | 1.489 | -0.3% | -0.01506 to +0.005616 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.3 | -0.6% | -2.143 to +0.1129 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 163.6 | -0.6% | -2.214 to +0.1256 | no |
| response time (ms), mean | 238.6 | 134 | -43.9% | -163.2 to -46.12 | yes: GAIN |
| response time (ms), 95th percentile | 394.5 | 152.3 | -61.4% | -308.8 to -175.6 | yes: GAIN |
| response time (ms), 99th percentile | 1425 | 685.5 | -51.9% | -1441 to -36.88 | yes: GAIN |
| time over the response line (% of samples) | 8.199 | 5.495 | -33.0% | -4.138 to -1.27 | yes: GAIN |
| failed requests (%) | 5.408 | 4.524 | -16.3% | -1.288 to -0.4799 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.5 | -22.5% | -2.505 to -0.6952 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28 | +28 (native is 0) | +23.94 to +32.06 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.875 | 0.6383 | -27.0% | -0.9137 to +0.4403 | no |
| utilisation (used / allocatable) | 0.07306 | 0.07045 | -3.6% | -0.004008 to -0.001223 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.729 | 1.666 | -3.6% | -0.0957 to -0.02912 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01067 | +0.0107 (native is 0) | +0.009646 to +0.01169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.729 | 1.677 | -3.0% | -0.08493 to -0.01856 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 381.2 | 393.3 | +3.2% | +5.968 to +18.34 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.84 | 10.78 | +22.0% | +0.6896 to +3.192 | yes: power given |
| pods started | 5 | 5.5 | +10.0% | -0.9795 to +1.979 | no |
| pod start wait, total (s) | 8 | 11 | +37.5% | -0.2866 to +6.287 | no |
| pod start wait, mean (s) | 1.587 | 1.917 | +20.8% | +0.0313 to +0.6297 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.7 | 48.89 | -1.6% | -1.656 to +0.02321 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 62 | 15.1 |  |
| machine down | omni | 51 | 10.3 | -11 s (-18%) |
| spike | native | 271 | 63.7 |  |
| spike | omni | 269 | 46.9 | -2 s (-1%) |
| runaway pod started | native | 109 | 11.0 |  |
| runaway pod started | omni | 79 | 6.0 | -30 s (-28%) |
| probe blind | native | 73 | 1.0 |  |
| probe blind | omni | 60 | 0.1 | -13 s (-18%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*