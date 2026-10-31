# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.4 | 173.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.4 | 173.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 538.7 | 509.2 |
| response time (ms), 95th percentile | 2117 | 2386 |
| response time (ms), 99th percentile | 5188 | 5660 |
| time over the response line (% of samples) | 26.75 | 25.26 |
| failed requests (%) | 3.673 | 2.684 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.556 | 9.111 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.44 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.372 | 1.339 |
| utilisation (used / allocatable) | 0.1015 | 0.1013 |
| CPU used (cores), mean | 2.436 | 2.432 |
| Omni's own CPU (cores), mean | 0 | 0.01409 |
| CPU used with Omni's own (cores), mean | 2.436 | 2.446 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 284.6 | 284.2 |
| HPA replicas, mean | 15.09 | 15.59 |
| pods started | 5.111 | 4.222 |
| pod start wait, total (s) | 9 | 6.889 |
| pod start wait, mean (s) | 1.769 | 1.519 |
| host CPU busy, the real machine under kind (%) | 70.18 | 70.2 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 235.1 | 240.2 |
| second app: response time (ms), 99th percentile | 2411 | 1671 |
| second app: time over the response line (% of samples) | 15.46 | 15.3 |
| second app: failed requests (%) | 13.75 | 14 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.517 | +0.2% | +0.0003 to +0.0057 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 173.4 | 173.7 | +0.2% | −0.3559 to +0.9279 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.4 | 173.7 | +0.2% | −0.3559 to +0.9279 | no |
| response time (ms), mean | 538.7 | 509.2 | −5.5% | −80.8389 to +21.8754 | no |
| response time (ms), 95th percentile | 2117 | 2386 | +12.7% | −95.1526 to +632.2548 | no |
| response time (ms), 99th percentile | 5188 | 5660 | +9.1% | −556.4113 to +1500.3101 | no |
| time over the response line (% of samples) | 26.75 | 25.26 | −5.6% | −2.8546 to −0.1163 | yes: GAIN |
| failed requests (%) | 3.673 | 2.684 | −26.9% | −2.3477 to +0.3691 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.556 | 9.111 | −4.7% | −0.8496 to −0.0393 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.44 | +47.444 (native is 0) | +35.0315 to +59.8573 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.372 | 1.339 | −2.4% | −0.3500 to +0.2833 | no |
| utilisation (used / allocatable) | 0.1015 | 0.1013 | −0.1% | −0.0020 to +0.0017 | no |
| CPU used (cores), mean | 2.436 | 2.432 | −0.1% | −0.0479 to +0.0407 | no |
| Omni's own CPU (cores), mean | 0 | 0.01409 | +0.014 (native is 0) | +0.0137 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.436 | 2.446 | +0.4% | −0.0338 to +0.0549 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 284.6 | 284.2 | −0.1% | −6.0358 to +5.2683 | no |
| HPA replicas, mean | 15.09 | 15.59 | +3.3% | +0.0120 to +0.9762 | yes: power given |
| pods started | 5.111 | 4.222 | −17.4% | −2.3496 to +0.5718 | no |
| pod start wait, total (s) | 9 | 6.889 | −23.5% | −5.0743 to +0.8521 | no |
| pod start wait, mean (s) | 1.769 | 1.519 | −14.1% | −0.5951 to +0.0951 | no |
| host CPU busy, the real machine under kind (%) | 70.18 | 70.2 | +0.0% | −0.4201 to +0.4682 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 235.1 | 240.2 | +2.2% | −34.5607 to +44.6863 | no |
| second app: response time (ms), 99th percentile | 2411 | 1671 | −30.7% | −1704.3901 to +225.1995 | no |
| second app: time over the response line (% of samples) | 15.46 | 15.3 | −1.0% | −0.8186 to +0.4939 | no |
| second app: failed requests (%) | 13.75 | 14 | +1.8% | −0.4266 to +0.9115 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*