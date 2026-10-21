# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.97 |
| node-hours | 4.155 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 444.4 | 444 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.8 | 442.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 164 | 93.58 |
| response time (ms), 95th percentile | 310.1 | 116.8 |
| response time (ms), 99th percentile | 595.3 | 266.7 |
| time over the response line (% of samples) | 3.003 | 1.913 |
| failed requests (%) | 1.529 | 1.425 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.4833 |
| utilisation (used / allocatable) | 0.04802 | 0.04692 |
| CPU used (cores), mean | 1.147 | 1.12 |
| Omni's own CPU (cores), mean | 0 | 0.00815 |
| CPU used with Omni's own (cores), mean | 1.147 | 1.129 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 588.8 | 600.7 |
| HPA replicas, mean | 8.345 | 8.248 |
| pods started | 8.4 | 9.5 |
| pod start wait, total (s) | 13 | 17.3 |
| pod start wait, mean (s) | 1.548 | 1.802 |
| host CPU busy, the real machine under kind (%) | 34.77 | 34.34 |
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
| worker nodes in service, mean | 5.97 | 5.97 | -0.0% | -0.003049 to +0.002864 | no |
| node-hours | 4.155 | 4.159 | +0.1% | -0.002006 to +0.008839 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 444.4 | 444 | -0.1% | -1.004 to +0.3781 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 442.8 | 442.5 | -0.1% | -1.069 to +0.4309 | no |
| response time (ms), mean | 164 | 93.58 | -43.0% | -101.7 to -39.23 | yes: GAIN |
| response time (ms), 95th percentile | 310.1 | 116.8 | -62.3% | -232.7 to -154 | yes: GAIN |
| response time (ms), 99th percentile | 595.3 | 266.7 | -55.2% | -379.3 to -277.8 | yes: GAIN |
| time over the response line (% of samples) | 3.003 | 1.913 | -36.3% | -1.571 to -0.6085 | yes: GAIN |
| failed requests (%) | 1.529 | 1.425 | -6.8% | -0.2137 to +0.005808 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 7 | -17.6% | -2.631 to -0.369 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.9 | +45.9 (native is 0) | +36.08 to +55.72 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.4833 | +82.4% | -0.3715 to +0.8082 | no |
| utilisation (used / allocatable) | 0.04802 | 0.04692 | -2.3% | -0.001654 to -0.0005443 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.147 | 1.12 | -2.3% | -0.0398 to -0.01266 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00815 | +0.00815 (native is 0) | +0.007029 to +0.009271 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.147 | 1.129 | -1.6% | -0.0312 to -0.004954 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 588.8 | 600.7 | +2.0% | +4.606 to +19.09 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.345 | 8.248 | -1.2% | -0.5461 to +0.3534 | no |
| pods started | 8.4 | 9.5 | +13.1% | -0.9909 to +3.191 | no |
| pod start wait, total (s) | 13 | 17.3 | +33.1% | -0.4454 to +9.045 | no |
| pod start wait, mean (s) | 1.548 | 1.802 | +16.4% | +0.06587 to +0.4409 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 34.77 | 34.34 | -1.2% | -0.8368 to -0.01139 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 56 | 3.1 |  |
| machine down | omni | 46 | 1.4 | -10 s (-18%) |
| spike | native | 253 | 64.1 |  |
| spike | omni | 239 | 61.7 | -14 s (-5%) |
| runaway pod started | native | 2 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | +1 s (+39%) |
| probe blind | native | 75 | 1.1 |  |
| probe blind | omni | 60 | 0.1 | -15 s (-19%) |
| api frozen | native | 2 | 0.3 |  |
| api frozen | omni | 2 | 0.0 | -1 s (-22%) |
| metrics down | native | 2 | 0.1 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-34%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*