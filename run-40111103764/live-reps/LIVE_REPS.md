# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.97 | 5.969 |
| node-hours | 4.157 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 442 | 441.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 440.4 | 440.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 139.1 | 93.88 |
| response time (ms), 95th percentile | 267.2 | 100.3 |
| response time (ms), 99th percentile | 649.4 | 322.5 |
| time over the response line (% of samples) | 2.589 | 1.717 |
| failed requests (%) | 1.267 | 1.081 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.4617 |
| utilisation (used / allocatable) | 0.04378 | 0.04292 |
| CPU used (cores), mean | 1.045 | 1.025 |
| Omni's own CPU (cores), mean | 0 | 0.00788 |
| CPU used with Omni's own (cores), mean | 1.045 | 1.033 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 638.8 | 648.8 |
| HPA replicas, mean | 7.878 | 7.738 |
| pods started | 8.8 | 10.5 |
| pod start wait, total (s) | 12.8 | 19.4 |
| pod start wait, mean (s) | 1.452 | 1.804 |
| host CPU busy, the real machine under kind (%) | 31.94 | 31.54 |
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
| worker nodes in service, mean | 5.97 | 5.969 | −0.0% | −0.0050 to +0.0038 | no |
| node-hours | 4.157 | 4.16 | +0.1% | −0.0019 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 442 | 441.8 | −0.0% | −0.4811 to +0.1046 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 440.4 | 440.2 | −0.0% | −0.6073 to +0.1684 | no |
| response time (ms), mean | 139.1 | 93.88 | −32.5% | −65.1664 to −25.1962 | yes: GAIN |
| response time (ms), 95th percentile | 267.2 | 100.3 | −62.5% | −206.3239 to −127.6271 | yes: GAIN |
| response time (ms), 99th percentile | 649.4 | 322.5 | −50.3% | −414.1628 to −239.7526 | yes: GAIN |
| time over the response line (% of samples) | 2.589 | 1.717 | −33.7% | −1.3776 to −0.3657 | yes: GAIN |
| failed requests (%) | 1.267 | 1.081 | −14.7% | −0.3540 to −0.0182 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 5.7 | −18.6% | −2.6081 to +0.0081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.7 | +46.700 (native is 0) | +38.3035 to +55.0965 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2667 | 0.4617 | +73.1% | −0.1779 to +0.5679 | no |
| utilisation (used / allocatable) | 0.04378 | 0.04292 | −2.0% | −0.0014 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.045 | 1.025 | −2.0% | −0.0328 to −0.0085 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00788 | +0.008 (native is 0) | +0.0068 to +0.0089 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.045 | 1.033 | −1.2% | −0.0241 to −0.0014 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 638.8 | 648.8 | +1.6% | +4.9143 to +15.0459 | yes, up (shown, not judged) |
| HPA replicas, mean | 7.878 | 7.738 | −1.8% | −0.7748 to +0.4944 | no |
| pods started | 8.8 | 10.5 | +19.3% | −0.3800 to +3.7800 | no |
| pod start wait, total (s) | 12.8 | 19.4 | +51.6% | +0.3532 to +12.8468 | yes: LOSS |
| pod start wait, mean (s) | 1.452 | 1.804 | +24.2% | +0.0563 to +0.6475 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 31.94 | 31.54 | −1.2% | −0.7369 to −0.0520 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 64 | 3.0 |  |
| machine down | omni | 37 | 0.9 | -28 s (-43%) |
| spike | native | 228 | 49.9 |  |
| spike | omni | 222 | 46.6 | -7 s (-3%) |
| runaway pod started | native | 2 | 0.2 |  |
| runaway pod started | omni | 3 | 0.0 | +1 s (+23%) |
| probe blind | native | 63 | 0.7 |  |
| probe blind | omni | 60 | 0.2 | -2 s (-4%) |
| api frozen | native | 15 | 0.3 |  |
| api frozen | omni | 1 | 0.0 | -14 s (-92%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 1 | 0.0 | -1 s (-30%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*