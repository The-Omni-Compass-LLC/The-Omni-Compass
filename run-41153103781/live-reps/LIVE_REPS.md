# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.51 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 171.9 | 86.98 |
| response time (ms), 95th percentile | 384 | 135.2 |
| response time (ms), 99th percentile | 613.4 | 195.4 |
| time over the response line (% of samples) | 2.802 | 0.01212 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.375 | 0.2167 |
| utilisation (used / allocatable) | 0.04231 | 0.04022 |
| CPU used (cores), mean | 1.015 | 0.9653 |
| Omni's own CPU (cores), mean | 0 | 0.00995 |
| CPU used with Omni's own (cores), mean | 1.015 | 0.9752 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 662.3 | 689.5 |
| HPA replicas, mean | 8.645 | 8.437 |
| pods started | 5 | 3.2 |
| pod start wait, total (s) | 7.8 | 4.9 |
| pod start wait, mean (s) | 1.56 | 1.427 |
| host CPU busy, the real machine under kind (%) | 30.63 | 29.94 |
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
| node-hours | 1.51 | 1.51 | +0.0% | −0.0017 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.5 | 159 | −0.3% | −0.8663 to −0.0765 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.5 | 159 | −0.3% | −0.8663 to −0.0765 | yes: GAIN |
| response time (ms), mean | 171.9 | 86.98 | −49.4% | −106.3872 to −63.4405 | yes: GAIN |
| response time (ms), 95th percentile | 384 | 135.2 | −64.8% | −309.9800 to −187.7520 | yes: GAIN |
| response time (ms), 99th percentile | 613.4 | 195.4 | −68.1% | −514.7757 to −321.2003 | yes: GAIN |
| time over the response line (% of samples) | 2.802 | 0.01212 | −99.6% | −3.8822 to −1.6969 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.4972 to −1.9028 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.3 | +18.300 (native is 0) | +14.6208 to +21.9792 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.375 | 0.2167 | −42.2% | −0.4817 to +0.1650 | no |
| utilisation (used / allocatable) | 0.04231 | 0.04022 | −4.9% | −0.0036 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.015 | 0.9653 | −4.9% | −0.0865 to −0.0138 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00995 | +0.010 (native is 0) | +0.0087 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.015 | 0.9752 | −4.0% | −0.0759 to −0.0045 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 662.3 | 689.5 | +4.1% | +9.3149 to +45.0919 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.645 | 8.437 | −2.4% | −0.8780 to +0.4630 | no |
| pods started | 5 | 3.2 | −36.0% | −2.6121 to −0.9879 | yes: GAIN |
| pod start wait, total (s) | 7.8 | 4.9 | −37.2% | −4.9358 to −0.8642 | yes: GAIN |
| pod start wait, mean (s) | 1.56 | 1.427 | −8.5% | −0.4970 to +0.2304 | no |
| host CPU busy, the real machine under kind (%) | 30.63 | 29.94 | −2.3% | −1.5780 to +0.1964 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*