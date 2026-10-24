# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.969 | 5.97 |
| node-hours | 4.156 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.6 | 443.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442 | 441.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 145.9 | 82.85 |
| response time (ms), 95th percentile | 301 | 111.1 |
| response time (ms), 99th percentile | 589.4 | 242.5 |
| time over the response line (% of samples) | 3.076 | 1.805 |
| failed requests (%) | 1.497 | 1.421 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 6.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.425 | 0.4367 |
| utilisation (used / allocatable) | 0.04649 | 0.0451 |
| CPU used (cores), mean | 1.11 | 1.077 |
| Omni's own CPU (cores), mean | 0 | 0.00738 |
| CPU used with Omni's own (cores), mean | 1.11 | 1.084 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 619.9 | 639.2 |
| HPA replicas, mean | 8.051 | 7.921 |
| pods started | 8.7 | 9.4 |
| pod start wait, total (s) | 12.3 | 17 |
| pod start wait, mean (s) | 1.418 | 1.761 |
| host CPU busy, the real machine under kind (%) | 33.23 | 32.65 |
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
| worker nodes in service, mean | 5.969 | 5.97 | +0.0% | -0.0004813 to +0.003316 | no |
| node-hours | 4.156 | 4.16 | +0.1% | -0.004125 to +0.01174 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.6 | 443.1 | -0.1% | -1.154 to +0.1882 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442 | 441.5 | -0.1% | -1.094 to +0.2741 | no |
| response time (ms), mean | 145.9 | 82.85 | -43.2% | -83.85 to -42.16 | yes: GAIN |
| response time (ms), 95th percentile | 301 | 111.1 | -63.1% | -234.2 to -145.5 | yes: GAIN |
| response time (ms), 99th percentile | 589.4 | 242.5 | -58.9% | -441.2 to -252.7 | yes: GAIN |
| time over the response line (% of samples) | 3.076 | 1.805 | -41.3% | -1.733 to -0.8093 | yes: GAIN |
| failed requests (%) | 1.497 | 1.421 | -5.1% | -0.2186 to +0.06546 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 6.2 | -30.3% | -4.008 to -1.392 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.5 | +42.5 (native is 0) | +32.34 to +52.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.425 | 0.4367 | +2.7% | -0.61 to +0.6333 | no |
| utilisation (used / allocatable) | 0.04649 | 0.0451 | -3.0% | -0.00204 to -0.0007453 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.11 | 1.077 | -3.0% | -0.04848 to -0.01741 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00738 | +0.00738 (native is 0) | +0.005941 to +0.008819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.11 | 1.084 | -2.3% | -0.04094 to -0.01019 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 619.9 | 639.2 | +3.1% | +6.201 to +32.5 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.051 | 7.921 | -1.6% | -0.8427 to +0.5821 | no |
| pods started | 8.7 | 9.4 | +8.0% | -1.179 to +2.579 | no |
| pod start wait, total (s) | 12.3 | 17 | +38.2% | -0.2103 to +9.61 | no |
| pod start wait, mean (s) | 1.418 | 1.761 | +24.2% | +0.06272 to +0.6226 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 33.23 | 32.65 | -1.7% | -0.9474 to -0.2148 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 65 | 3.6 |  |
| machine down | omni | 44 | 1.5 | -22 s (-33%) |
| spike | native | 248 | 64.1 |  |
| spike | omni | 236 | 60.2 | -12 s (-5%) |
| runaway pod started | native | 2 | 0.1 |  |
| runaway pod started | omni | 2 | 0.0 | -0 s (-11%) |
| probe blind | native | 71 | 1.2 |  |
| probe blind | omni | 60 | 0.0 | -11 s (-15%) |
| api frozen | native | 11 | 0.3 |  |
| api frozen | omni | 4 | 0.0 | -7 s (-62%) |
| metrics down | native | 3 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-37%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*