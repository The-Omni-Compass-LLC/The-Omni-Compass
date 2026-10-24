# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.918 | 5.915 |
| node-hours | 1.496 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 164.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 162.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 198.8 | 113.2 |
| response time (ms), 95th percentile | 405.3 | 223.7 |
| response time (ms), 99th percentile | 1145 | 557.9 |
| time over the response line (% of samples) | 7.215 | 5.073 |
| failed requests (%) | 4.071 | 3.633 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 5.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.49 |
| utilisation (used / allocatable) | 0.06611 | 0.06542 |
| CPU used (cores), mean | 1.565 | 1.548 |
| Omni's own CPU (cores), mean | 0 | 0.00918 |
| CPU used with Omni's own (cores), mean | 1.565 | 1.557 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.2 | 432.9 |
| HPA replicas, mean | 8.475 | 9.725 |
| pods started | 5.3 | 5.7 |
| pod start wait, total (s) | 16.7 | 9.8 |
| pod start wait, mean (s) | 2.803 | 1.695 |
| host CPU busy, the real machine under kind (%) | 45.27 | 44.95 |
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
| worker nodes in service, mean | 5.918 | 5.915 | −0.0% | −0.0094 to +0.0050 | no |
| node-hours | 1.496 | 1.489 | −0.5% | −0.0166 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165 | 164.1 | −0.5% | −1.9271 to +0.1422 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.4 | 162.5 | −0.6% | −1.9618 to +0.1061 | no |
| response time (ms), mean | 198.8 | 113.2 | −43.1% | −135.6933 to −35.5206 | yes: GAIN |
| response time (ms), 95th percentile | 405.3 | 223.7 | −44.8% | −251.5596 to −111.6474 | yes: GAIN |
| response time (ms), 99th percentile | 1145 | 557.9 | −51.3% | −930.7112 to −244.3676 | yes: GAIN |
| time over the response line (% of samples) | 7.215 | 5.073 | −29.7% | −3.4643 to −0.8205 | yes: GAIN |
| failed requests (%) | 4.071 | 3.633 | −10.8% | −0.9933 to +0.1169 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 5.2 | −16.1% | −2.0663 to +0.0663 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.3 | +24.300 (native is 0) | +21.0299 to +27.5701 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.49 | +2.1% | −0.5507 to +0.5707 | no |
| utilisation (used / allocatable) | 0.06611 | 0.06542 | −1.0% | −0.0022 to +0.0008 | no |
| CPU used (cores), mean | 1.565 | 1.548 | −1.1% | −0.0519 to +0.0176 | no |
| Omni's own CPU (cores), mean | 0 | 0.00918 | +0.009 (native is 0) | +0.0078 to +0.0105 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.565 | 1.557 | −0.5% | −0.0418 to +0.0258 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.2 | 432.9 | +0.2% | −7.9539 to +9.4270 | no |
| HPA replicas, mean | 8.475 | 9.725 | +14.8% | +0.4450 to +2.0560 | yes: power given |
| pods started | 5.3 | 5.7 | +7.5% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 16.7 | 9.8 | −41.3% | −26.4269 to +12.6269 | no |
| pod start wait, mean (s) | 2.803 | 1.695 | −39.5% | −3.8068 to +1.5897 | no |
| host CPU busy, the real machine under kind (%) | 45.27 | 44.95 | −0.7% | −1.2932 to +0.6634 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 78 | 13.0 |  |
| machine down | omni | 36 | 9.6 | -42 s (-54%) |
| spike | native | 238 | 54.6 |  |
| spike | omni | 235 | 46.6 | -3 s (-1%) |
| runaway pod started | native | 95 | 9.8 |  |
| runaway pod started | omni | 68 | 5.6 | -27 s (-28%) |
| probe blind | native | 67 | 0.5 |  |
| probe blind | omni | 60 | 0.1 | -7 s (-11%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*