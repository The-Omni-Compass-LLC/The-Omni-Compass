# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.916 | 5.917 |
| node-hours | 1.496 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 164.4 | 163.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 184 | 125 |
| response time (ms), 95th percentile | 376.9 | 199.5 |
| response time (ms), 99th percentile | 1656 | 917.7 |
| time over the response line (% of samples) | 6.54 | 4.752 |
| failed requests (%) | 3.322 | 3.139 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9883 | 1.115 |
| utilisation (used / allocatable) | 0.06411 | 0.06293 |
| CPU used (cores), mean | 1.517 | 1.489 |
| Omni's own CPU (cores), mean | 0 | 0.00906 |
| CPU used with Omni's own (cores), mean | 1.517 | 1.498 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.8 | 448.1 |
| HPA replicas, mean | 8.456 | 9.654 |
| pods started | 4.8 | 7.6 |
| pod start wait, total (s) | 43.4 | 34 |
| pod start wait, mean (s) | 7.607 | 4.013 |
| host CPU busy, the real machine under kind (%) | 43.31 | 43.09 |
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
| worker nodes in service, mean | 5.916 | 5.917 | +0.0% | -0.002644 to +0.005109 | no |
| node-hours | 1.496 | 1.49 | -0.3% | -0.01147 to +0.001246 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164.4 | 163.6 | -0.5% | -1.627 to -0.05299 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.8 | 162 | -0.5% | -1.621 to -0.0007913 | yes: GAIN |
| response time (ms), mean | 184 | 125 | -32.1% | -85.63 to -32.42 | yes: GAIN |
| response time (ms), 95th percentile | 376.9 | 199.5 | -47.1% | -263.7 to -91.11 | yes: GAIN |
| response time (ms), 99th percentile | 1656 | 917.7 | -44.6% | -1151 to -325.9 | yes: GAIN |
| time over the response line (% of samples) | 6.54 | 4.752 | -27.3% | -2.93 to -0.6457 | yes: GAIN |
| failed requests (%) | 3.322 | 3.139 | -5.5% | -0.6508 to +0.2856 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.3 | 5 | -5.7% | -1.257 to +0.6567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.5 | +30.5 (native is 0) | +25.5 to +35.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9883 | 1.115 | +12.8% | -0.7924 to +1.046 | no |
| utilisation (used / allocatable) | 0.06411 | 0.06293 | -1.8% | -0.002409 to +5.38e-05 | no |
| CPU used (cores), mean | 1.517 | 1.489 | -1.8% | -0.0576 to +0.001635 | no |
| Omni's own CPU (cores), mean | 0 | 0.00906 | +0.00906 (native is 0) | +0.007799 to +0.01032 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 1.498 | -1.2% | -0.048 to +0.01015 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.8 | 448.1 | +1.4% | -3.968 to +16.68 | no |
| HPA replicas, mean | 8.456 | 9.654 | +14.2% | +0.3487 to +2.047 | yes: power given |
| pods started | 4.8 | 7.6 | +58.3% | +1.594 to +4.006 | yes: power given |
| pod start wait, total (s) | 43.4 | 34 | -21.7% | -46.97 to +28.17 | no |
| pod start wait, mean (s) | 7.607 | 4.013 | -47.3% | -9.597 to +2.407 | no |
| host CPU busy, the real machine under kind (%) | 43.31 | 43.09 | -0.5% | -0.9822 to +0.5388 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 38 | 12.0 |  |
| machine down | omni | 38 | 9.2 | +0 s (+1%) |
| spike | native | 226 | 48.6 |  |
| spike | omni | 218 | 40.5 | -7 s (-3%) |
| runaway pod started | native | 74 | 8.0 |  |
| runaway pod started | omni | 55 | 4.8 | -18 s (-25%) |
| probe blind | native | 58 | 0.2 |  |
| probe blind | omni | 60 | 0.1 | +2 s (+4%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*