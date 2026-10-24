# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.968 |
| node-hours | 4.156 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 444.7 | 444.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.1 | 442.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 157.4 | 86.57 |
| response time (ms), 95th percentile | 317.8 | 114.5 |
| response time (ms), 99th percentile | 639.6 | 346.9 |
| time over the response line (% of samples) | 3.514 | 2.07 |
| failed requests (%) | 1.722 | 1.43 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3867 | 0.575 |
| utilisation (used / allocatable) | 0.04845 | 0.04741 |
| CPU used (cores), mean | 1.157 | 1.132 |
| Omni's own CPU (cores), mean | 0 | 0.00786 |
| CPU used with Omni's own (cores), mean | 1.157 | 1.14 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 595.8 | 604.5 |
| HPA replicas, mean | 8.163 | 7.939 |
| pods started | 8.4 | 9.3 |
| pod start wait, total (s) | 13.2 | 16.3 |
| pod start wait, mean (s) | 1.573 | 1.736 |
| host CPU busy, the real machine under kind (%) | 34.56 | 34.13 |
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
| worker nodes in service, mean | 5.97 | 5.968 | −0.0% | −0.0048 to +0.0011 | no |
| node-hours | 4.156 | 4.16 | +0.1% | +0.0001 to +0.0079 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 444.7 | 444.6 | −0.0% | −0.7441 to +0.6168 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 443.1 | 442.9 | −0.0% | −0.8585 to +0.5353 | no |
| response time (ms), mean | 157.4 | 86.57 | −45.0% | −95.6026 to −46.0983 | yes: GAIN |
| response time (ms), 95th percentile | 317.8 | 114.5 | −64.0% | −241.8624 to −164.6176 | yes: GAIN |
| response time (ms), 99th percentile | 639.6 | 346.9 | −45.8% | −421.9372 to −163.6040 | yes: GAIN |
| time over the response line (% of samples) | 3.514 | 2.07 | −41.1% | −2.0040 to −0.8837 | yes: GAIN |
| failed requests (%) | 1.722 | 1.43 | −16.9% | −0.4153 to −0.1681 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 7 | −22.2% | −3.0663 to −0.9337 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.4 | +44.400 (native is 0) | +32.9989 to +55.8011 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3867 | 0.575 | +48.7% | −0.2307 to +0.6074 | no |
| utilisation (used / allocatable) | 0.04845 | 0.04741 | −2.1% | −0.0017 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.157 | 1.132 | −2.2% | −0.0415 to −0.0090 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00786 | +0.008 (native is 0) | +0.0065 to +0.0092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.157 | 1.14 | −1.5% | −0.0328 to −0.0020 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 595.8 | 604.5 | +1.5% | −0.7395 to +18.1601 | no |
| HPA replicas, mean | 8.163 | 7.939 | −2.8% | −0.9156 to +0.4658 | no |
| pods started | 8.4 | 9.3 | +10.7% | −1.1077 to +2.9077 | no |
| pod start wait, total (s) | 13.2 | 16.3 | +23.5% | −1.5167 to +7.7167 | no |
| pod start wait, mean (s) | 1.573 | 1.736 | +10.3% | −0.1413 to +0.4665 | no |
| host CPU busy, the real machine under kind (%) | 34.56 | 34.13 | −1.2% | −0.9873 to +0.1297 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 77 | 4.9 |  |
| machine down | omni | 25 | 0.8 | -52 s (-67%) |
| spike | native | 254 | 69.3 |  |
| spike | omni | 254 | 68.8 | -0 s (-0%) |
| runaway pod started | native | 5 | 0.5 |  |
| runaway pod started | omni | 3 | 0.0 | -2 s (-45%) |
| probe blind | native | 59 | 1.5 |  |
| probe blind | omni | 60 | 0.0 | +1 s (+3%) |
| api frozen | native | 12 | 0.5 |  |
| api frozen | omni | 4 | 0.0 | -9 s (-71%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | -0 s (-18%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*