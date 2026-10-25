# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.516 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.6 | 510.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.6 | 510.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 253.2 | 150.9 |
| response time (ms), 95th percentile | 700.2 | 287.3 |
| response time (ms), 99th percentile | 1873 | 1657 |
| time over the response line (% of samples) | 16.38 | 9.761 |
| failed requests (%) | 8.904 | 7.668 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 17.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.4883 |
| utilisation (used / allocatable) | 0.09504 | 0.09246 |
| CPU used (cores), mean | 2.281 | 2.219 |
| Omni's own CPU (cores), mean | 0 | 0.00868 |
| CPU used with Omni's own (cores), mean | 2.281 | 2.228 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 327 | 338.4 |
| HPA replicas, mean | 9.512 | 9.651 |
| pods started | 5.5 | 6.3 |
| pod start wait, total (s) | 8.5 | 10.5 |
| pod start wait, mean (s) | 1.533 | 1.526 |
| host CPU busy, the real machine under kind (%) | 64.52 | 63.27 |
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
| node-hours | 4.516 | 4.512 | −0.1% | −0.0138 to +0.0058 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.6 | 510.4 | −0.4% | −3.2764 to −1.0692 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.6 | 510.4 | −0.4% | −3.2764 to −1.0692 | yes: GAIN |
| response time (ms), mean | 253.2 | 150.9 | −40.4% | −135.2189 to −69.3750 | yes: GAIN |
| response time (ms), 95th percentile | 700.2 | 287.3 | −59.0% | −540.7423 to −285.1337 | yes: GAIN |
| response time (ms), 99th percentile | 1873 | 1657 | −11.5% | −1071.9380 to +641.4424 | no |
| time over the response line (% of samples) | 16.38 | 9.761 | −40.4% | −9.3895 to −3.8476 | yes: GAIN |
| failed requests (%) | 8.904 | 7.668 | −13.9% | −2.1546 to −0.3171 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.8 | 17.6 | −29.0% | −8.9128 to −5.4872 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.1 | +38.100 (native is 0) | +29.4277 to +46.7723 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.4883 | +85.4% | −0.0428 to +0.4928 | no |
| utilisation (used / allocatable) | 0.09504 | 0.09246 | −2.7% | −0.0032 to −0.0020 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.281 | 2.219 | −2.7% | −0.0769 to −0.0469 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00868 | +0.009 (native is 0) | +0.0074 to +0.0099 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.281 | 2.228 | −2.3% | −0.0689 to −0.0375 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 327 | 338.4 | +3.5% | +3.7759 to +19.1949 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.512 | 9.651 | +1.5% | −0.8819 to +1.1585 | no |
| pods started | 5.5 | 6.3 | +14.5% | −1.3539 to +2.9539 | no |
| pod start wait, total (s) | 8.5 | 10.5 | +23.5% | −3.0804 to +7.0804 | no |
| pod start wait, mean (s) | 1.533 | 1.526 | −0.5% | −0.3449 to +0.3303 | no |
| host CPU busy, the real machine under kind (%) | 64.52 | 63.27 | −1.9% | −1.7403 to −0.7564 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*