# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.971 | 5.969 |
| node-hours | 4.157 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 442.9 | 443 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.4 | 441.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 147.5 | 85.46 |
| response time (ms), 95th percentile | 288.4 | 107.7 |
| response time (ms), 99th percentile | 715.2 | 279.6 |
| time over the response line (% of samples) | 2.958 | 1.886 |
| failed requests (%) | 1.405 | 1.31 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3983 | 0.4167 |
| utilisation (used / allocatable) | 0.04549 | 0.04503 |
| CPU used (cores), mean | 1.086 | 1.075 |
| Omni's own CPU (cores), mean | 0 | 0.00746 |
| CPU used with Omni's own (cores), mean | 1.086 | 1.083 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 626.9 | 626 |
| HPA replicas, mean | 8.117 | 8.068 |
| pods started | 9 | 9.1 |
| pod start wait, total (s) | 13.3 | 16.3 |
| pod start wait, mean (s) | 1.473 | 1.771 |
| host CPU busy, the real machine under kind (%) | 32.68 | 32.51 |
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
| worker nodes in service, mean | 5.971 | 5.969 | −0.0% | −0.0048 to +0.0013 | no |
| node-hours | 4.157 | 4.159 | +0.1% | −0.0003 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 442.9 | 443 | +0.0% | −0.4834 to +0.7058 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.4 | 441.4 | +0.0% | −0.5734 to +0.6083 | no |
| response time (ms), mean | 147.5 | 85.46 | −42.1% | −82.6382 to −41.4394 | yes: GAIN |
| response time (ms), 95th percentile | 288.4 | 107.7 | −62.7% | −224.9320 to −136.5470 | yes: GAIN |
| response time (ms), 99th percentile | 715.2 | 279.6 | −60.9% | −726.0356 to −145.2044 | yes: GAIN |
| time over the response line (% of samples) | 2.958 | 1.886 | −36.2% | −1.6018 to −0.5416 | yes: GAIN |
| failed requests (%) | 1.405 | 1.31 | −6.8% | −0.1709 to −0.0198 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 6.5 | −24.4% | −2.8113 to −1.3887 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.8 | +40.800 (native is 0) | +33.0093 to +48.5907 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3983 | 0.4167 | +4.6% | −0.3342 to +0.3709 | no |
| utilisation (used / allocatable) | 0.04549 | 0.04503 | −1.0% | −0.0014 to +0.0005 | no |
| CPU used (cores), mean | 1.086 | 1.075 | −1.0% | −0.0333 to +0.0105 | no |
| Omni's own CPU (cores), mean | 0 | 0.00746 | +0.007 (native is 0) | +0.0062 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.086 | 1.083 | −0.4% | −0.0248 to +0.0170 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 626.9 | 626 | −0.2% | −13.8442 to +11.8821 | no |
| HPA replicas, mean | 8.117 | 8.068 | −0.6% | −0.6204 to +0.5211 | no |
| pods started | 9 | 9.1 | +1.1% | −1.1818 to +1.3818 | no |
| pod start wait, total (s) | 13.3 | 16.3 | +22.6% | −1.9787 to +7.9787 | no |
| pod start wait, mean (s) | 1.473 | 1.771 | +20.2% | −0.1087 to +0.7042 | no |
| host CPU busy, the real machine under kind (%) | 32.68 | 32.51 | −0.5% | −0.7191 to +0.3659 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 83 | 4.0 |  |
| machine down | omni | 41 | 1.3 | -42 s (-51%) |
| spike | native | 248 | 58.3 |  |
| spike | omni | 239 | 56.0 | -9 s (-3%) |
| runaway pod started | native | 7 | 0.3 |  |
| runaway pod started | omni | 2 | 0.0 | -5 s (-72%) |
| probe blind | native | 57 | 0.8 |  |
| probe blind | omni | 60 | 0.0 | +3 s (+6%) |
| api frozen | native | 2 | 0.2 |  |
| api frozen | omni | 3 | 0.0 | +1 s (+43%) |
| metrics down | native | 3 | 0.1 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-49%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*