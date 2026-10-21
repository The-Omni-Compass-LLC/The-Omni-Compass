# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.968 | 5.969 |
| node-hours | 4.158 | 4.16 |
| energy, parked workers still on at idle power (Wh, declared model) | 443.1 | 442.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.4 | 440.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 160.3 | 88.06 |
| response time (ms), 95th percentile | 300.9 | 106.9 |
| response time (ms), 99th percentile | 574.6 | 280.7 |
| time over the response line (% of samples) | 2.832 | 1.554 |
| failed requests (%) | 1.208 | 1.007 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 5.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.46 | 0.3217 |
| utilisation (used / allocatable) | 0.04527 | 0.04435 |
| CPU used (cores), mean | 1.081 | 1.059 |
| Omni's own CPU (cores), mean | 0 | 0.00791 |
| CPU used with Omni's own (cores), mean | 1.081 | 1.067 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 622.6 | 626.8 |
| HPA replicas, mean | 8.149 | 7.964 |
| pods started | 7.2 | 10.7 |
| pod start wait, total (s) | 11.7 | 19.4 |
| pod start wait, mean (s) | 1.623 | 1.798 |
| host CPU busy, the real machine under kind (%) | 33.18 | 32.79 |
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
| worker nodes in service, mean | 5.968 | 5.969 | +0.0% | -0.002289 to +0.004693 | no |
| node-hours | 4.158 | 4.16 | +0.0% | -0.003087 to +0.006421 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 443.1 | 442.1 | -0.2% | -2.575 to +0.7511 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 441.4 | 440.5 | -0.2% | -2.559 to +0.8596 | no |
| response time (ms), mean | 160.3 | 88.06 | -45.1% | -96.31 to -48.16 | yes: GAIN |
| response time (ms), 95th percentile | 300.9 | 106.9 | -64.5% | -242 to -146 | yes: GAIN |
| response time (ms), 99th percentile | 574.6 | 280.7 | -51.2% | -421.8 to -166.1 | yes: GAIN |
| time over the response line (% of samples) | 2.832 | 1.554 | -45.1% | -2.26 to -0.2951 | yes: GAIN |
| failed requests (%) | 1.208 | 1.007 | -16.6% | -0.4337 to +0.03229 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 5.5 | -26.7% | -4.546 to +0.5458 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.9 | +49.9 (native is 0) | +41.47 to +58.33 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.46 | 0.3217 | -30.1% | -0.5118 to +0.2351 | no |
| utilisation (used / allocatable) | 0.04527 | 0.04435 | -2.0% | -0.002283 to +0.0004358 | no |
| CPU used (cores), mean | 1.081 | 1.059 | -2.0% | -0.05465 to +0.01078 | no |
| Omni's own CPU (cores), mean | 0 | 0.00791 | +0.00791 (native is 0) | +0.006664 to +0.009156 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.081 | 1.067 | -1.3% | -0.04603 to +0.01799 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 622.6 | 626.8 | +0.7% | -11.5 to +19.81 | no |
| HPA replicas, mean | 8.149 | 7.964 | -2.3% | -0.6165 to +0.2464 | no |
| pods started | 7.2 | 10.7 | +48.6% | +1.415 to +5.585 | yes: power given |
| pod start wait, total (s) | 11.7 | 19.4 | +65.8% | +2.744 to +12.66 | yes: LOSS |
| pod start wait, mean (s) | 1.623 | 1.798 | +10.7% | -0.09687 to +0.4458 | no |
| host CPU busy, the real machine under kind (%) | 33.18 | 32.79 | -1.2% | -1.266 to +0.4863 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 66 | 3.2 |  |
| machine down | omni | 31 | 1.0 | -35 s (-53%) |
| spike | native | 234 | 48.1 |  |
| spike | omni | 232 | 44.7 | -2 s (-1%) |
| runaway pod started | native | 5 | 0.2 |  |
| runaway pod started | omni | 2 | 0.0 | -3 s (-57%) |
| probe blind | native | 65 | 1.0 |  |
| probe blind | omni | 60 | 0.0 | -5 s (-7%) |
| api frozen | native | 4 | 0.3 |  |
| api frozen | omni | 3 | 0.0 | -1 s (-28%) |
| metrics down | native | 2 | 0.0 |  |
| metrics down | omni | 2 | 0.0 | +0 s (+8%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*