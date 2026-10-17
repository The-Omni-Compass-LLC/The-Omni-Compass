# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.913 |
| node-hours | 1.49 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.8 | 166.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.2 | 164.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 248.1 | 122.5 |
| response time (ms), 95th percentile | 425.5 | 156.9 |
| response time (ms), 99th percentile | 1251 | 534.3 |
| time over the response line (% of samples) | 9.001 | 6.035 |
| failed requests (%) | 5.718 | 5.119 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6567 | 0.4717 |
| utilisation (used / allocatable) | 0.07718 | 0.07544 |
| CPU used (cores), mean | 1.826 | 1.784 |
| Omni's own CPU (cores), mean | 0 | 0.01065 |
| CPU used with Omni's own (cores), mean | 1.826 | 1.795 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 360.1 | 367.4 |
| HPA replicas, mean | 9.107 | 11.01 |
| pods started | 3.9 | 5.5 |
| pod start wait, total (s) | 17.5 | 13.1 |
| pod start wait, mean (s) | 3.573 | 2.217 |
| host CPU busy, the real machine under kind (%) | 52.38 | 51.56 |
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
| worker nodes in service, mean | 5.915 | 5.913 | -0.0% | -0.005731 to +0.002093 | no |
| node-hours | 1.49 | 1.49 | +0.0% | -0.008543 to +0.009265 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.8 | 166.5 | -0.2% | -1.239 to +0.6445 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.2 | 164.8 | -0.2% | -1.26 to +0.5941 | no |
| response time (ms), mean | 248.1 | 122.5 | -50.6% | -165.2 to -85.88 | yes: GAIN |
| response time (ms), 95th percentile | 425.5 | 156.9 | -63.1% | -308.2 to -229 | yes: GAIN |
| response time (ms), 99th percentile | 1251 | 534.3 | -57.3% | -1202 to -232 | yes: GAIN |
| time over the response line (% of samples) | 9.001 | 6.035 | -33.0% | -3.928 to -2.006 | yes: GAIN |
| failed requests (%) | 5.718 | 5.119 | -10.5% | -1.132 to -0.06643 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 6.2 | -18.4% | -2.366 to -0.4344 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30 | +30 (native is 0) | +25.36 to +34.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6567 | 0.4717 | -28.2% | -0.9037 to +0.5337 | no |
| utilisation (used / allocatable) | 0.07718 | 0.07544 | -2.3% | -0.002903 to -0.0005817 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.826 | 1.784 | -2.3% | -0.06873 to -0.01464 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01065 | +0.0106 (native is 0) | +0.009825 to +0.01148 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.826 | 1.795 | -1.7% | -0.05808 to -0.00399 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 360.1 | 367.4 | +2.0% | +2.54 to +11.99 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.107 | 11.01 | +20.9% | +1.171 to +2.632 | yes: power given |
| pods started | 3.9 | 5.5 | +41.0% | +0.2428 to +2.957 | yes: power given |
| pod start wait, total (s) | 17.5 | 13.1 | -25.1% | -22.03 to +13.23 | no |
| pod start wait, mean (s) | 3.573 | 2.217 | -38.0% | -4.073 to +1.36 | no |
| host CPU busy, the real machine under kind (%) | 52.38 | 51.56 | -1.6% | -1.467 to -0.1647 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 69 | 14.0 |  |
| machine down | omni | 41 | 8.9 | -28 s (-41%) |
| spike | native | 292 | 80.7 |  |
| spike | omni | 292 | 67.9 | -0 s (-0%) |
| runaway pod started | native | 136 | 15.0 |  |
| runaway pod started | omni | 113 | 9.1 | -23 s (-17%) |
| probe blind | native | 79 | 0.9 |  |
| probe blind | omni | 60 | 0.0 | -19 s (-24%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*