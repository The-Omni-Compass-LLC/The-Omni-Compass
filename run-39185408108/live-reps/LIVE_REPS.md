# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.972 | 5.97 |
| node-hours | 4.159 | 4.156 |
| energy, parked workers still on at idle power (Wh, declared model) | 445.6 | 444.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.1 | 443.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 165.9 | 95.12 |
| response time (ms), 95th percentile | 327 | 118.9 |
| response time (ms), 99th percentile | 694.1 | 315 |
| time over the response line (% of samples) | 3.446 | 1.97 |
| failed requests (%) | 1.663 | 1.44 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.5367 |
| utilisation (used / allocatable) | 0.04988 | 0.04876 |
| CPU used (cores), mean | 1.192 | 1.164 |
| Omni's own CPU (cores), mean | 0 | 0.0076 |
| CPU used with Omni's own (cores), mean | 1.192 | 1.172 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 568.6 | 573.6 |
| HPA replicas, mean | 8.545 | 8.465 |
| pods started | 8.4 | 9.1 |
| pod start wait, total (s) | 12.8 | 16.4 |
| pod start wait, mean (s) | 1.568 | 1.767 |
| host CPU busy, the real machine under kind (%) | 35.81 | 35.26 |
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
| worker nodes in service, mean | 5.972 | 5.97 | -0.0% | -0.004911 to -0.0001303 | yes: GAIN |
| node-hours | 4.159 | 4.156 | -0.1% | -0.006761 to +0.001594 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 445.6 | 444.9 | -0.2% | -1.589 to +0.2171 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 444.1 | 443.3 | -0.2% | -1.786 to +0.1516 | no |
| response time (ms), mean | 165.9 | 95.12 | -42.7% | -98.44 to -43.2 | yes: GAIN |
| response time (ms), 95th percentile | 327 | 118.9 | -63.6% | -253.6 to -162.6 | yes: GAIN |
| response time (ms), 99th percentile | 694.1 | 315 | -54.6% | -478.4 to -279.8 | yes: GAIN |
| time over the response line (% of samples) | 3.446 | 1.97 | -42.8% | -2.11 to -0.8427 | yes: GAIN |
| failed requests (%) | 1.663 | 1.44 | -13.4% | -0.3074 to -0.139 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 7 | -27.8% | -4.092 to -1.308 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 | +43.6 (native is 0) | +36.38 to +50.82 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.21 | 0.5367 | +155.6% | -0.1468 to +0.8001 | no |
| utilisation (used / allocatable) | 0.04988 | 0.04876 | -2.2% | -0.002111 to -0.000129 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.192 | 1.164 | -2.3% | -0.05131 to -0.003336 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0076 | +0.0076 (native is 0) | +0.006504 to +0.008696 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.192 | 1.172 | -1.7% | -0.04286 to +0.003412 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 568.6 | 573.6 | +0.9% | -11.76 to +21.64 | no |
| HPA replicas, mean | 8.545 | 8.465 | -0.9% | -0.8324 to +0.6728 | no |
| pods started | 8.4 | 9.1 | +8.3% | -1.487 to +2.887 | no |
| pod start wait, total (s) | 12.8 | 16.4 | +28.1% | -1.063 to +8.263 | no |
| pod start wait, mean (s) | 1.568 | 1.767 | +12.7% | -0.1186 to +0.5173 | no |
| host CPU busy, the real machine under kind (%) | 35.81 | 35.26 | -1.5% | -1.018 to -0.08546 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 69 | 4.0 |  |
| machine down | omni | 33 | 1.0 | -36 s (-52%) |
| spike | native | 264 | 72.0 |  |
| spike | omni | 263 | 68.9 | -1 s (-0%) |
| runaway pod started | native | 7 | 0.5 |  |
| runaway pod started | omni | 3 | 0.0 | -4 s (-61%) |
| probe blind | native | 65 | 1.2 |  |
| probe blind | omni | 60 | 0.0 | -5 s (-7%) |
| api frozen | native | 12 | 0.4 |  |
| api frozen | omni | 2 | 0.0 | -10 s (-80%) |
| metrics down | native | 5 | 0.2 |  |
| metrics down | omni | 3 | 0.0 | -2 s (-43%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*