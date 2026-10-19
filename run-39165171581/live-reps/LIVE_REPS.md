# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.916 |
| node-hours | 1.498 | 1.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 163 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 204.5 | 129.3 |
| response time (ms), 95th percentile | 359.4 | 177.2 |
| response time (ms), 99th percentile | 1619 | 972.2 |
| time over the response line (% of samples) | 6.845 | 5.471 |
| failed requests (%) | 4.137 | 3.906 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.7417 |
| utilisation (used / allocatable) | 0.06571 | 0.06573 |
| CPU used (cores), mean | 1.555 | 1.555 |
| Omni's own CPU (cores), mean | 0 | 0.00941 |
| CPU used with Omni's own (cores), mean | 1.555 | 1.565 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.7 | 433.1 |
| HPA replicas, mean | 8.47 | 10.06 |
| pods started | 5.3 | 7.7 |
| pod start wait, total (s) | 19.6 | 20.1 |
| pod start wait, mean (s) | 3.36 | 2.575 |
| host CPU busy, the real machine under kind (%) | 44.59 | 44.74 |
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
| worker nodes in service, mean | 5.916 | 5.916 | -0.0% | -0.006053 to +0.005686 | no |
| node-hours | 1.498 | 1.493 | -0.3% | -0.01253 to +0.002253 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.6 | -0.3% | -1.453 to +0.4116 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 163 | -0.3% | -1.442 to +0.404 | no |
| response time (ms), mean | 204.5 | 129.3 | -36.8% | -134.1 to -16.38 | yes: GAIN |
| response time (ms), 95th percentile | 359.4 | 177.2 | -50.7% | -234.6 to -129.8 | yes: GAIN |
| response time (ms), 99th percentile | 1619 | 972.2 | -39.9% | -1244 to -48.88 | yes: GAIN |
| time over the response line (% of samples) | 6.845 | 5.471 | -20.1% | -2.09 to -0.6589 | yes: GAIN |
| failed requests (%) | 4.137 | 3.906 | -5.6% | -0.6782 to +0.2175 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 5.3 | -13.1% | -1.679 to +0.07931 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.7 | +33.7 (native is 0) | +27.99 to +39.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4467 | 0.7417 | +66.0% | -0.1578 to +0.7478 | no |
| utilisation (used / allocatable) | 0.06571 | 0.06573 | +0.0% | -0.001318 to +0.001349 | no |
| CPU used (cores), mean | 1.555 | 1.555 | +0.0% | -0.03133 to +0.03195 | no |
| Omni's own CPU (cores), mean | 0 | 0.00941 | +0.00941 (native is 0) | +0.00782 to +0.011 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.555 | 1.565 | +0.6% | -0.02143 to +0.04087 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.7 | 433.1 | -0.6% | -12.47 to +7.369 | no |
| HPA replicas, mean | 8.47 | 10.06 | +18.8% | +0.7076 to +2.47 | yes: power given |
| pods started | 5.3 | 7.7 | +45.3% | +0.7758 to +4.024 | yes: power given |
| pod start wait, total (s) | 19.6 | 20.1 | +2.6% | -7.228 to +8.228 | no |
| pod start wait, mean (s) | 3.36 | 2.575 | -23.4% | -1.782 to +0.2122 | no |
| host CPU busy, the real machine under kind (%) | 44.59 | 44.74 | +0.3% | -0.6156 to +0.912 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 55 | 13.8 |  |
| machine down | omni | 39 | 9.9 | -17 s (-30%) |
| spike | native | 239 | 53.6 |  |
| spike | omni | 231 | 52.1 | -8 s (-3%) |
| runaway pod started | native | 87 | 7.5 |  |
| runaway pod started | omni | 74 | 6.7 | -14 s (-16%) |
| probe blind | native | 65 | 0.3 |  |
| probe blind | omni | 60 | 0.1 | -5 s (-8%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*