# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.915 | 5.915 |
| node-hours | 1.492 | 1.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 164.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.3 | 162.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 217.3 | 140.9 |
| response time (ms), 95th percentile | 434.3 | 194.4 |
| response time (ms), 99th percentile | 2139 | 1126 |
| time over the response line (% of samples) | 7.889 | 5.224 |
| failed requests (%) | 4.571 | 3.584 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7633 | 0.65 |
| utilisation (used / allocatable) | 0.06785 | 0.06556 |
| CPU used (cores), mean | 1.605 | 1.551 |
| Omni's own CPU (cores), mean | 0 | 0.00977 |
| CPU used with Omni's own (cores), mean | 1.605 | 1.561 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420 | 430.3 |
| HPA replicas, mean | 8.424 | 9.886 |
| pods started | 5.6 | 7.3 |
| pod start wait, total (s) | 17.8 | 14.5 |
| pod start wait, mean (s) | 2.868 | 1.95 |
| host CPU busy, the real machine under kind (%) | 46.29 | 45.23 |
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
| worker nodes in service, mean | 5.915 | 5.915 | +0.0% | -0.005601 to +0.005669 | no |
| node-hours | 1.492 | 1.489 | -0.2% | -0.01103 to +0.004139 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.9 | 164.1 | -0.5% | -1.81 to +0.1045 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.3 | 162.5 | -0.5% | -1.816 to +0.1183 | no |
| response time (ms), mean | 217.3 | 140.9 | -35.1% | -138.7 to -13.98 | yes: GAIN |
| response time (ms), 95th percentile | 434.3 | 194.4 | -55.2% | -322.8 to -157 | yes: GAIN |
| response time (ms), 99th percentile | 2139 | 1126 | -47.3% | -2445 to +420.9 | no |
| time over the response line (% of samples) | 7.889 | 5.224 | -33.8% | -3.848 to -1.482 | yes: GAIN |
| failed requests (%) | 4.571 | 3.584 | -21.6% | -1.703 to -0.2709 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.1 | -22.7% | -2.408 to -0.5921 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.4 | +29.4 (native is 0) | +24.24 to +34.56 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7633 | 0.65 | -14.8% | -0.8509 to +0.6243 | no |
| utilisation (used / allocatable) | 0.06785 | 0.06556 | -3.4% | -0.00436 to -0.0002234 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.605 | 1.551 | -3.4% | -0.1028 to -0.00537 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00977 | +0.00977 (native is 0) | +0.00852 to +0.01102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 1.561 | -2.8% | -0.09235 to +0.003735 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420 | 430.3 | +2.5% | +1.268 to +19.37 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.424 | 9.886 | +17.3% | +0.4487 to +2.474 | yes: power given |
| pods started | 5.6 | 7.3 | +30.4% | +0.1529 to +3.247 | yes: power given |
| pod start wait, total (s) | 17.8 | 14.5 | -18.5% | -23.78 to +17.18 | no |
| pod start wait, mean (s) | 2.868 | 1.95 | -32.0% | -3.832 to +1.995 | no |
| host CPU busy, the real machine under kind (%) | 46.29 | 45.23 | -2.3% | -2.307 to +0.1934 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 67 | 15.5 |  |
| machine down | omni | 42 | 9.9 | -26 s (-38%) |
| spike | native | 242 | 53.4 |  |
| spike | omni | 238 | 43.6 | -3 s (-1%) |
| runaway pod started | native | 93 | 11.2 |  |
| runaway pod started | omni | 65 | 5.1 | -28 s (-31%) |
| probe blind | native | 68 | 0.6 |  |
| probe blind | omni | 60 | 0.1 | -8 s (-12%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*