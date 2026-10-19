# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.916 |
| node-hours | 1.494 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.6 | 164.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163 | 162.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 188.4 | 132.7 |
| response time (ms), 95th percentile | 374.8 | 180.2 |
| response time (ms), 99th percentile | 1248 | 721.4 |
| time over the response line (% of samples) | 6.655 | 4.982 |
| failed requests (%) | 3.898 | 3.45 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4733 | 0.835 |
| utilisation (used / allocatable) | 0.06544 | 0.06464 |
| CPU used (cores), mean | 1.548 | 1.529 |
| Omni's own CPU (cores), mean | 0 | 0.00925 |
| CPU used with Omni's own (cores), mean | 1.548 | 1.539 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 431.8 | 433.4 |
| HPA replicas, mean | 8.493 | 10.03 |
| pods started | 5.2 | 6.8 |
| pod start wait, total (s) | 25.6 | 28.9 |
| pod start wait, mean (s) | 4.479 | 3.724 |
| host CPU busy, the real machine under kind (%) | 44.73 | 44.26 |
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
| worker nodes in service, mean | 5.916 | 5.916 | -0.0% | -0.0007746 to +0.0007169 | no |
| node-hours | 1.494 | 1.492 | -0.2% | -0.01018 to +0.005572 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.6 | 164.1 | -0.3% | -1.377 to +0.4481 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163 | 162.5 | -0.3% | -1.375 to +0.4509 | no |
| response time (ms), mean | 188.4 | 132.7 | -29.6% | -97.62 to -13.8 | yes: GAIN |
| response time (ms), 95th percentile | 374.8 | 180.2 | -51.9% | -263.6 to -125.7 | yes: GAIN |
| response time (ms), 99th percentile | 1248 | 721.4 | -42.2% | -1010 to -43.77 | yes: GAIN |
| time over the response line (% of samples) | 6.655 | 4.982 | -25.1% | -2.703 to -0.6421 | yes: GAIN |
| failed requests (%) | 3.898 | 3.45 | -11.5% | -0.8554 to -0.04107 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.9 | 5 | -15.3% | -1.687 to -0.1128 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.6 | +32.6 (native is 0) | +27.84 to +37.36 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4733 | 0.835 | +76.4% | -0.1781 to +0.9014 | no |
| utilisation (used / allocatable) | 0.06544 | 0.06464 | -1.2% | -0.002288 to +0.0006897 | no |
| CPU used (cores), mean | 1.548 | 1.529 | -1.2% | -0.05416 to +0.01636 | no |
| Omni's own CPU (cores), mean | 0 | 0.00925 | +0.00925 (native is 0) | +0.008094 to +0.01041 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.548 | 1.539 | -0.6% | -0.0442 to +0.0249 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 431.8 | 433.4 | +0.4% | -8.44 to +11.73 | no |
| HPA replicas, mean | 8.493 | 10.03 | +18.1% | +0.4777 to +2.589 | yes: power given |
| pods started | 5.2 | 6.8 | +30.8% | -0.2835 to +3.483 | no |
| pod start wait, total (s) | 25.6 | 28.9 | +12.9% | -8.115 to +14.72 | no |
| pod start wait, mean (s) | 4.479 | 3.724 | -16.9% | -2.368 to +0.8563 | no |
| host CPU busy, the real machine under kind (%) | 44.73 | 44.26 | -1.1% | -1.267 to +0.32 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 50 | 13.6 |  |
| machine down | omni | 41 | 9.3 | -9 s (-17%) |
| spike | native | 233 | 48.6 |  |
| spike | omni | 230 | 42.3 | -3 s (-1%) |
| runaway pod started | native | 73 | 6.9 |  |
| runaway pod started | omni | 59 | 5.0 | -14 s (-20%) |
| probe blind | native | 64 | 0.2 |  |
| probe blind | omni | 54 | 0.1 | -9 s (-15%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*