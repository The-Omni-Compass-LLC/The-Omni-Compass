# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.918 |
| node-hours | 1.49 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 165.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 163.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 215.5 | 145 |
| response time (ms), 95th percentile | 380.6 | 140 |
| response time (ms), 99th percentile | 1391 | 792.6 |
| time over the response line (% of samples) | 8.146 | 5.582 |
| failed requests (%) | 5.349 | 4.572 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.94 | 0.5183 |
| utilisation (used / allocatable) | 0.0733 | 0.07057 |
| CPU used (cores), mean | 1.734 | 1.671 |
| Omni's own CPU (cores), mean | 0 | 0.01012 |
| CPU used with Omni's own (cores), mean | 1.734 | 1.681 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 381.9 | 393.3 |
| HPA replicas, mean | 8.741 | 10.06 |
| pods started | 5 | 4.4 |
| pod start wait, total (s) | 39.7 | 19.7 |
| pod start wait, mean (s) | 7.243 | 3.583 |
| host CPU busy, the real machine under kind (%) | 49.69 | 48.28 |
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
| worker nodes in service, mean | 5.914 | 5.918 | +0.1% | -0.001286 to +0.009293 | no |
| node-hours | 1.49 | 1.491 | +0.1% | -0.006488 to +0.009154 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.8 | 165.3 | -0.3% | -1.417 to +0.312 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.2 | 163.7 | -0.3% | -1.351 to +0.3964 | no |
| response time (ms), mean | 215.5 | 145 | -32.7% | -123.9 to -17.09 | yes: GAIN |
| response time (ms), 95th percentile | 380.6 | 140 | -63.2% | -295.1 to -186.1 | yes: GAIN |
| response time (ms), 99th percentile | 1391 | 792.6 | -43.0% | -1103 to -94.61 | yes: GAIN |
| time over the response line (% of samples) | 8.146 | 5.582 | -31.5% | -3.929 to -1.199 | yes: GAIN |
| failed requests (%) | 5.349 | 4.572 | -14.5% | -1.247 to -0.3072 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 5.7 | -19.7% | -2.423 to -0.3772 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.7 | +27.7 (native is 0) | +24.36 to +31.04 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.94 | 0.5183 | -44.9% | -0.8913 to +0.04793 | no |
| utilisation (used / allocatable) | 0.0733 | 0.07057 | -3.7% | -0.005207 to -0.0002436 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.734 | 1.671 | -3.6% | -0.1218 to -0.004694 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01012 | +0.0101 (native is 0) | +0.009436 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.734 | 1.681 | -3.1% | -0.1114 to +0.005158 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 381.9 | 393.3 | +3.0% | +0.7071 to +22.22 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.741 | 10.06 | +15.1% | +0.619 to +2.012 | yes: power given |
| pods started | 5 | 4.4 | -12.0% | -2.039 to +0.8385 | no |
| pod start wait, total (s) | 39.7 | 19.7 | -50.4% | -43.58 to +3.585 | no |
| pod start wait, mean (s) | 7.243 | 3.583 | -50.5% | -7.844 to +0.5233 | no |
| host CPU busy, the real machine under kind (%) | 49.69 | 48.28 | -2.8% | -2.689 to -0.1224 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 75 | 14.6 |  |
| machine down | omni | 39 | 9.6 | -36 s (-48%) |
| spike | native | 267 | 70.4 |  |
| spike | omni | 265 | 56.1 | -1 s (-1%) |
| runaway pod started | native | 105 | 12.0 |  |
| runaway pod started | omni | 83 | 6.7 | -22 s (-21%) |
| probe blind | native | 67 | 0.8 |  |
| probe blind | omni | 60 | 0.1 | -7 s (-10%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*