# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.917 |
| node-hours | 1.495 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.1 | 164.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.5 | 162.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 198.1 | 133.2 |
| response time (ms), 95th percentile | 406 | 242.3 |
| response time (ms), 99th percentile | 1193 | 999.4 |
| time over the response line (% of samples) | 7.559 | 6.026 |
| failed requests (%) | 4.329 | 4.028 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 5.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.103 | 1.123 |
| utilisation (used / allocatable) | 0.06674 | 0.06599 |
| CPU used (cores), mean | 1.579 | 1.562 |
| Omni's own CPU (cores), mean | 0 | 0.01003 |
| CPU used with Omni's own (cores), mean | 1.579 | 1.572 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.3 | 430.3 |
| HPA replicas, mean | 8.426 | 10.36 |
| pods started | 5.7 | 8.8 |
| pod start wait, total (s) | 32.7 | 25.6 |
| pod start wait, mean (s) | 6.041 | 2.932 |
| host CPU busy, the real machine under kind (%) | 45.51 | 45.49 |
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
| worker nodes in service, mean | 5.915 | 5.917 | +0.0% | -0.005287 to +0.008892 | no |
| node-hours | 1.495 | 1.491 | -0.3% | -0.01223 to +0.002614 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.1 | 164.3 | -0.5% | -1.844 to +0.303 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.5 | 162.7 | -0.4% | -1.784 to +0.3229 | no |
| response time (ms), mean | 198.1 | 133.2 | -32.8% | -115.6 to -14.26 | yes: GAIN |
| response time (ms), 95th percentile | 406 | 242.3 | -40.3% | -284.3 to -43.01 | yes: GAIN |
| response time (ms), 99th percentile | 1193 | 999.4 | -16.2% | -596.9 to +209.5 | no |
| time over the response line (% of samples) | 7.559 | 6.026 | -20.3% | -3.115 to +0.04948 | no |
| failed requests (%) | 4.329 | 4.028 | -7.0% | -0.9247 to +0.3224 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 5.4 | -21.7% | -2.727 to -0.2726 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33 | +33 (native is 0) | +30.62 to +35.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.103 | 1.123 | +1.8% | -0.6113 to +0.6513 | no |
| utilisation (used / allocatable) | 0.06674 | 0.06599 | -1.1% | -0.002877 to +0.001378 | no |
| CPU used (cores), mean | 1.579 | 1.562 | -1.1% | -0.06694 to +0.03233 | no |
| Omni's own CPU (cores), mean | 0 | 0.01003 | +0.01 (native is 0) | +0.008724 to +0.01134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.579 | 1.572 | -0.5% | -0.05654 to +0.04199 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.3 | 430.3 | +0.2% | -11.88 to +13.92 | no |
| HPA replicas, mean | 8.426 | 10.36 | +23.0% | +1.024 to +2.852 | yes: power given |
| pods started | 5.7 | 8.8 | +54.4% | +1.775 to +4.425 | yes: power given |
| pod start wait, total (s) | 32.7 | 25.6 | -21.7% | -41.96 to +27.76 | no |
| pod start wait, mean (s) | 6.041 | 2.932 | -51.5% | -9.037 to +2.818 | no |
| host CPU busy, the real machine under kind (%) | 45.51 | 45.49 | -0.0% | -1.321 to +1.283 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 82 | 13.9 |  |
| machine down | omni | 45 | 11.6 | -37 s (-45%) |
| spike | native | 234 | 59.3 |  |
| spike | omni | 246 | 54.0 | +11 s (+5%) |
| runaway pod started | native | 116 | 10.0 |  |
| runaway pod started | omni | 78 | 6.6 | -38 s (-33%) |
| probe blind | native | 65 | 0.6 |  |
| probe blind | omni | 60 | 0.1 | -5 s (-8%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*