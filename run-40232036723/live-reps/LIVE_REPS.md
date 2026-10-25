# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.336 | 4.339 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.6 | 478.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.6 | 478.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 262 | 130.3 |
| response time (ms), 95th percentile | 693.8 | 265.6 |
| response time (ms), 99th percentile | 1301 | 616 |
| time over the response line (% of samples) | 12.09 | 2.726 |
| failed requests (%) | 1.046 | 0.8548 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.9 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.81 |
| utilisation (used / allocatable) | 0.07708 | 0.07403 |
| CPU used (cores), mean | 1.85 | 1.777 |
| Omni's own CPU (cores), mean | 0 | 0.00896 |
| CPU used with Omni's own (cores), mean | 1.85 | 1.786 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 393 | 406.5 |
| HPA replicas, mean | 9.699 | 11.2 |
| pods started | 6.1 | 12.7 |
| pod start wait, total (s) | 10 | 20.9 |
| pod start wait, mean (s) | 1.639 | 1.622 |
| host CPU busy, the real machine under kind (%) | 53.18 | 51.62 |
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
| node-hours | 4.336 | 4.339 | +0.1% | −0.0053 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480.6 | 478.9 | −0.3% | −2.7436 to −0.5338 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.6 | 478.9 | −0.3% | −2.7436 to −0.5338 | yes: GAIN |
| response time (ms), mean | 262 | 130.3 | −50.3% | −176.5717 to −86.8229 | yes: GAIN |
| response time (ms), 95th percentile | 693.8 | 265.6 | −61.7% | −556.4237 to −299.9773 | yes: GAIN |
| response time (ms), 99th percentile | 1301 | 616 | −52.7% | −894.2228 to −476.3004 | yes: GAIN |
| time over the response line (% of samples) | 12.09 | 2.726 | −77.4% | −14.0654 to −4.6562 | yes: GAIN |
| failed requests (%) | 1.046 | 0.8548 | −18.3% | −0.3448 to −0.0370 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.9 | 8.1 | −61.2% | −18.1081 to −7.4919 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50 | +50.000 (native is 0) | +35.6780 to +64.3220 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4767 | 0.81 | +69.9% | −0.1602 to +0.8268 | no |
| utilisation (used / allocatable) | 0.07708 | 0.07403 | −4.0% | −0.0039 to −0.0022 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.85 | 1.777 | −4.0% | −0.0935 to −0.0528 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00896 | +0.009 (native is 0) | +0.0072 to +0.0108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.85 | 1.786 | −3.5% | −0.0832 to −0.0452 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 393 | 406.5 | +3.4% | +9.3356 to +17.7702 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.699 | 11.2 | +15.5% | −0.2691 to +3.2751 | no |
| pods started | 6.1 | 12.7 | +108.2% | +3.3273 to +9.8727 | yes: power given |
| pod start wait, total (s) | 10 | 20.9 | +109.0% | +3.1192 to +18.6808 | yes: LOSS |
| pod start wait, mean (s) | 1.639 | 1.622 | −1.1% | −0.3464 to +0.3119 | no |
| host CPU busy, the real machine under kind (%) | 53.18 | 51.62 | −2.9% | −2.0390 to −1.0705 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*