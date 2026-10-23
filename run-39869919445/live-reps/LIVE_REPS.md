# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.968 | 5.971 |
| node-hours | 4.158 | 4.159 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.6 | 443.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.9 | 442.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 157.8 | 87.14 |
| response time (ms), 95th percentile | 297 | 112.6 |
| response time (ms), 99th percentile | 903 | 344.1 |
| time over the response line (% of samples) | 3.325 | 1.905 |
| failed requests (%) | 1.386 | 1.373 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 6.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.8117 |
| utilisation (used / allocatable) | 0.04703 | 0.0463 |
| CPU used (cores), mean | 1.123 | 1.106 |
| Omni's own CPU (cores), mean | 0 | 0.02325 |
| CPU used with Omni's own (cores), mean | 1.123 | 1.129 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 608.5 | 617.3 |
| HPA replicas, mean | 8.165 | 8.536 |
| pods started | 8.7 | 11.5 |
| pod start wait, total (s) | 13.4 | 19.4 |
| pod start wait, mean (s) | 1.541 | 1.711 |
| host CPU busy, the real machine under kind (%) | 33.78 | 34.12 |
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
| worker nodes in service, mean | 5.968 | 5.971 | +0.0% | +0.0002674 to +0.005068 | yes: power given |
| node-hours | 4.158 | 4.159 | +0.0% | -0.01046 to +0.01252 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.6 | 443.6 | +0.0% | -1.546 to +1.589 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.9 | 442.1 | +0.0% | -1.433 to +1.755 | no |
| response time (ms), mean | 157.8 | 87.14 | -44.8% | -91.61 to -49.65 | yes: GAIN |
| response time (ms), 95th percentile | 297 | 112.6 | -62.1% | -230.9 to -137.9 | yes: GAIN |
| response time (ms), 99th percentile | 903 | 344.1 | -61.9% | -793.7 to -324.2 | yes: GAIN |
| time over the response line (% of samples) | 3.325 | 1.905 | -42.7% | -1.783 to -1.057 | yes: GAIN |
| failed requests (%) | 1.386 | 1.373 | -0.9% | -0.2044 to +0.1788 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 6.8 | -13.9% | -2.137 to -0.06342 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.2 | +59.2 (native is 0) | +53.35 to +65.05 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.8117 | +70.3% | -0.1764 to +0.8464 | no |
| utilisation (used / allocatable) | 0.04703 | 0.0463 | -1.6% | -0.001128 to -0.0003378 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.123 | 1.106 | -1.5% | -0.02608 to -0.007726 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02325 | +0.0232 (native is 0) | +0.01988 to +0.02662 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.123 | 1.129 | +0.6% | -0.00178 to +0.01448 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 608.5 | 617.3 | +1.5% | +3.822 to +13.93 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.165 | 8.536 | +4.5% | -0.2342 to +0.977 | no |
| pods started | 8.7 | 11.5 | +32.2% | +1.3 to +4.3 | yes: power given |
| pod start wait, total (s) | 13.4 | 19.4 | +44.8% | +2.801 to +9.199 | yes: LOSS |
| pod start wait, mean (s) | 1.541 | 1.711 | +11.0% | -0.1268 to +0.4669 | no |
| host CPU busy, the real machine under kind (%) | 33.78 | 34.12 | +1.0% | -0.0759 to +0.7507 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 48 | 3.2 |  |
| machine down | omni | 41 | 1.4 | -7 s (-15%) |
| spike | native | 242 | 66.3 |  |
| spike | omni | 238 | 61.0 | -4 s (-2%) |
| runaway pod started | native | 5 | 0.3 |  |
| runaway pod started | omni | 2 | 0.0 | -3 s (-63%) |
| probe blind | native | 63 | 1.0 |  |
| probe blind | omni | 60 | 0.0 | -3 s (-5%) |
| api frozen | native | 4 | 0.2 |  |
| api frozen | omni | 2 | 0.0 | -2 s (-49%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | -1 s (-30%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*