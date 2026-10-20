# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.919 | 5.912 |
| node-hours | 1.496 | 1.487 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.7 | 165.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.1 | 163.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 228.9 | 122.6 |
| response time (ms), 95th percentile | 432.5 | 183.2 |
| response time (ms), 99th percentile | 1029 | 630.3 |
| time over the response line (% of samples) | 9.216 | 5.662 |
| failed requests (%) | 5.816 | 4.596 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7633 | 0.8833 |
| utilisation (used / allocatable) | 0.07418 | 0.07075 |
| CPU used (cores), mean | 1.756 | 1.673 |
| Omni's own CPU (cores), mean | 0 | 0.01018 |
| CPU used with Omni's own (cores), mean | 1.756 | 1.683 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 384.6 | 397.9 |
| HPA replicas, mean | 8.785 | 10.63 |
| pods started | 4.7 | 6.8 |
| pod start wait, total (s) | 23 | 12.3 |
| pod start wait, mean (s) | 5.627 | 1.788 |
| host CPU busy, the real machine under kind (%) | 50.47 | 48.57 |
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
| worker nodes in service, mean | 5.919 | 5.912 | -0.1% | -0.01529 to +0.001326 | no |
| node-hours | 1.496 | 1.487 | -0.6% | -0.01725 to -0.0007482 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 166.7 | 165.1 | -0.9% | -2.558 to -0.544 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.1 | 163.5 | -1.0% | -2.62 to -0.732 | yes: GAIN |
| response time (ms), mean | 228.9 | 122.6 | -46.4% | -158.3 to -54.35 | yes: GAIN |
| response time (ms), 95th percentile | 432.5 | 183.2 | -57.7% | -318.2 to -180.5 | yes: GAIN |
| response time (ms), 99th percentile | 1029 | 630.3 | -38.8% | -780.1 to -17.48 | yes: GAIN |
| time over the response line (% of samples) | 9.216 | 5.662 | -38.6% | -4.759 to -2.348 | yes: GAIN |
| failed requests (%) | 5.816 | 4.596 | -21.0% | -1.897 to -0.5427 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 5.9 | -26.2% | -3.19 to -1.01 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.8 | +29.8 (native is 0) | +26.96 to +32.64 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7633 | 0.8833 | +15.7% | -0.8888 to +1.129 | no |
| utilisation (used / allocatable) | 0.07418 | 0.07075 | -4.6% | -0.005386 to -0.001489 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.756 | 1.673 | -4.7% | -0.1278 to -0.0381 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01018 | +0.0102 (native is 0) | +0.008992 to +0.01137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.756 | 1.683 | -4.1% | -0.1168 to -0.02874 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 384.6 | 397.9 | +3.5% | +3.22 to +23.54 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.785 | 10.63 | +21.0% | +1.189 to +2.497 | yes: power given |
| pods started | 4.7 | 6.8 | +44.7% | +0.5751 to +3.625 | yes: power given |
| pod start wait, total (s) | 23 | 12.3 | -46.5% | -36.05 to +14.65 | no |
| pod start wait, mean (s) | 5.627 | 1.788 | -68.2% | -10.07 to +2.393 | no |
| host CPU busy, the real machine under kind (%) | 50.47 | 48.57 | -3.7% | -2.99 to -0.7928 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 57 | 14.5 |  |
| machine down | omni | 42 | 8.9 | -16 s (-27%) |
| spike | native | 276 | 79.1 |  |
| spike | omni | 270 | 57.3 | -6 s (-2%) |
| runaway pod started | native | 155 | 16.7 |  |
| runaway pod started | omni | 98 | 8.1 | -57 s (-37%) |
| probe blind | native | 73 | 1.1 |  |
| probe blind | omni | 60 | 0.0 | -13 s (-18%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*