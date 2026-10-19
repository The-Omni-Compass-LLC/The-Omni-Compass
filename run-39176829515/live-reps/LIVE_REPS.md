# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.919 | 5.916 |
| node-hours | 1.494 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 163.1 | 162.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.6 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 175.7 | 109.8 |
| response time (ms), 95th percentile | 457.8 | 223.7 |
| response time (ms), 99th percentile | 1239 | 946.8 |
| time over the response line (% of samples) | 7.035 | 4.467 |
| failed requests (%) | 2.907 | 2.441 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.5 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.65 | 0.5883 |
| utilisation (used / allocatable) | 0.05907 | 0.05825 |
| CPU used (cores), mean | 1.398 | 1.379 |
| Omni's own CPU (cores), mean | 0 | 0.00852 |
| CPU used with Omni's own (cores), mean | 1.398 | 1.387 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.2 | 482.9 |
| HPA replicas, mean | 8.031 | 9.019 |
| pods started | 6 | 7.3 |
| pod start wait, total (s) | 33.8 | 12.6 |
| pod start wait, mean (s) | 6.389 | 1.693 |
| host CPU busy, the real machine under kind (%) | 40.73 | 40.37 |
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
| worker nodes in service, mean | 5.919 | 5.916 | -0.0% | -0.008132 to +0.002463 | no |
| node-hours | 1.494 | 1.49 | -0.3% | -0.01221 to +0.004212 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 163.1 | 162.6 | -0.3% | -1.343 to +0.3249 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.6 | 161 | -0.3% | -1.383 to +0.2653 | no |
| response time (ms), mean | 175.7 | 109.8 | -37.5% | -95.66 to -36.26 | yes: GAIN |
| response time (ms), 95th percentile | 457.8 | 223.7 | -51.1% | -284.4 to -183.7 | yes: GAIN |
| response time (ms), 99th percentile | 1239 | 946.8 | -23.6% | -989.8 to +405.2 | no |
| time over the response line (% of samples) | 7.035 | 4.467 | -36.5% | -3.544 to -1.593 | yes: GAIN |
| failed requests (%) | 2.907 | 2.441 | -16.0% | -0.9497 to +0.01718 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.5 | 4.7 | -14.5% | -1.742 to +0.1417 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.9 | +28.9 (native is 0) | +24.59 to +33.21 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.65 | 0.5883 | -9.5% | -0.5526 to +0.4292 | no |
| utilisation (used / allocatable) | 0.05907 | 0.05825 | -1.4% | -0.001938 to +0.0002962 | no |
| CPU used (cores), mean | 1.398 | 1.379 | -1.4% | -0.04585 to +0.005956 | no |
| Omni's own CPU (cores), mean | 0 | 0.00852 | +0.00852 (native is 0) | +0.00694 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.398 | 1.387 | -0.8% | -0.03623 to +0.01337 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.2 | 482.9 | +0.6% | -3.729 to +9.038 | no |
| HPA replicas, mean | 8.031 | 9.019 | +12.3% | +0.1326 to +1.842 | yes: power given |
| pods started | 6 | 7.3 | +21.7% | -0.579 to +3.179 | no |
| pod start wait, total (s) | 33.8 | 12.6 | -62.7% | -49.38 to +6.983 | no |
| pod start wait, mean (s) | 6.389 | 1.693 | -73.5% | -10.16 to +0.7716 | no |
| host CPU busy, the real machine under kind (%) | 40.73 | 40.37 | -0.9% | -1.362 to +0.6485 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 61 | 16.0 |  |
| machine down | omni | 35 | 9.2 | -26 s (-43%) |
| spike | native | 205 | 40.9 |  |
| spike | omni | 198 | 34.6 | -7 s (-3%) |
| runaway pod started | native | 53 | 5.2 |  |
| runaway pod started | omni | 43 | 3.6 | -11 s (-20%) |
| probe blind | native | 59 | 0.2 |  |
| probe blind | omni | 60 | 0.0 | +1 s (+1%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*