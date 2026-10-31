# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 160.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 160.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 121.5 | 77.09 |
| response time (ms), 95th percentile | 250.9 | 117.9 |
| response time (ms), 99th percentile | 367.3 | 153.2 |
| time over the response line (% of samples) | 0.4098 | 0.02439 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.2733 |
| utilisation (used / allocatable) | 0.03597 | 0.04632 |
| CPU used (cores), mean | 0.8633 | 1.112 |
| Omni's own CPU (cores), mean | 0 | 0.01633 |
| CPU used with Omni's own (cores), mean | 0.8633 | 1.128 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.1 | 583.6 |
| HPA replicas, mean | 8.787 | 9.955 |
| pods started | 5 | 6.9 |
| pod start wait, total (s) | 6.3 | 10.1 |
| pod start wait, mean (s) | 1.27 | 1.445 |
| host CPU busy, the real machine under kind (%) | 27.48 | 35.19 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.514 | +0.2% | −0.0052 to +0.0115 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.2 | 160.8 | +1.7% | +1.6002 to +3.7707 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.2 | 160.8 | +1.7% | +1.6002 to +3.7707 | yes: power given |
| response time (ms), mean | 121.5 | 77.09 | −36.6% | −58.7105 to −30.1059 | yes: GAIN |
| response time (ms), 95th percentile | 250.9 | 117.9 | −53.0% | −163.6611 to −102.4349 | yes: GAIN |
| response time (ms), 99th percentile | 367.3 | 153.2 | −58.3% | −249.0411 to −179.1169 | yes: GAIN |
| time over the response line (% of samples) | 0.4098 | 0.02439 | −94.0% | −0.7119 to −0.0590 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.3 | +31.300 (native is 0) | +21.3939 to +41.2061 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.265 | 0.2733 | +3.1% | −0.3124 to +0.3290 | no |
| utilisation (used / allocatable) | 0.03597 | 0.04632 | +28.8% | +0.0069 to +0.0138 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8633 | 1.112 | +28.8% | +0.1661 to +0.3305 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01633 | +0.016 (native is 0) | +0.0123 to +0.0203 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8633 | 1.128 | +30.7% | +0.1789 to +0.3504 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 729.1 | 583.6 | −20.0% | −182.2065 to −108.7171 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.787 | 9.955 | +13.3% | +0.4782 to +1.8585 | yes: power given |
| pods started | 5 | 6.9 | +38.0% | +0.4129 to +3.3871 | yes: power given |
| pod start wait, total (s) | 6.3 | 10.1 | +60.3% | +1.0856 to +6.5144 | yes: LOSS |
| pod start wait, mean (s) | 1.27 | 1.445 | +13.8% | −0.1158 to +0.4663 | no |
| host CPU busy, the real machine under kind (%) | 27.48 | 35.19 | +28.0% | +5.2624 to +10.1482 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*