# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.917 |
| node-hours | 1.492 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 163.7 | 163.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.2 | 162.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 183.4 | 149.4 |
| response time (ms), 95th percentile | 393.2 | 238.5 |
| response time (ms), 99th percentile | 1156 | 1383 |
| time over the response line (% of samples) | 6.369 | 5.227 |
| failed requests (%) | 3.289 | 3.223 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.5 | 5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.06 | 0.3417 |
| utilisation (used / allocatable) | 0.06325 | 0.06211 |
| CPU used (cores), mean | 1.497 | 1.47 |
| Omni's own CPU (cores), mean | 0 | 0.00905 |
| CPU used with Omni's own (cores), mean | 1.497 | 1.479 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.1 | 453.3 |
| HPA replicas, mean | 8.29 | 9.473 |
| pods started | 5.8 | 6.6 |
| pod start wait, total (s) | 35.5 | 11 |
| pod start wait, mean (s) | 6.538 | 1.697 |
| host CPU busy, the real machine under kind (%) | 43.17 | 42.78 |
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
| worker nodes in service, mean | 5.917 | 5.917 | -0.0% | -0.008461 to +0.008337 | no |
| node-hours | 1.492 | 1.492 | +0.0% | -0.001829 to +0.002106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 163.7 | 163.6 | -0.0% | -0.3767 to +0.2217 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.2 | 162.1 | -0.0% | -0.3639 to +0.2046 | no |
| response time (ms), mean | 183.4 | 149.4 | -18.6% | -72.6 to +4.457 | no |
| response time (ms), 95th percentile | 393.2 | 238.5 | -39.3% | -252 to -57.36 | yes: GAIN |
| response time (ms), 99th percentile | 1156 | 1383 | +19.6% | -600.6 to +1054 | no |
| time over the response line (% of samples) | 6.369 | 5.227 | -17.9% | -2.451 to +0.1676 | no |
| failed requests (%) | 3.289 | 3.223 | -2.0% | -0.3001 to +0.1685 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.5 | 5 | -9.1% | -1.273 to +0.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.9 | +26.9 (native is 0) | +22.66 to +31.14 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.06 | 0.3417 | -67.8% | -1.249 to -0.1877 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06325 | 0.06211 | -1.8% | -0.002476 to +0.0001944 | no |
| CPU used (cores), mean | 1.497 | 1.47 | -1.8% | -0.05847 to +0.004036 | no |
| Omni's own CPU (cores), mean | 0 | 0.00905 | +0.00905 (native is 0) | +0.007613 to +0.01049 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.497 | 1.479 | -1.2% | -0.04877 to +0.01243 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.1 | 453.3 | +1.2% | -3.094 to +13.47 | no |
| HPA replicas, mean | 8.29 | 9.473 | +14.3% | +0.245 to +2.121 | yes: power given |
| pods started | 5.8 | 6.6 | +13.8% | -0.6226 to +2.223 | no |
| pod start wait, total (s) | 35.5 | 11 | -69.0% | -55.74 to +6.742 | no |
| pod start wait, mean (s) | 6.538 | 1.697 | -74.0% | -10.46 to +0.7797 | no |
| host CPU busy, the real machine under kind (%) | 43.17 | 42.78 | -0.9% | -1.011 to +0.2257 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 48 | 12.4 |  |
| machine down | omni | 40 | 10.8 | -9 s (-18%) |
| spike | native | 225 | 44.7 |  |
| spike | omni | 220 | 38.7 | -6 s (-2%) |
| runaway pod started | native | 62 | 6.2 |  |
| runaway pod started | omni | 52 | 4.0 | -10 s (-16%) |
| probe blind | native | 64 | 0.3 |  |
| probe blind | omni | 55 | 0.2 | -10 s (-15%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*