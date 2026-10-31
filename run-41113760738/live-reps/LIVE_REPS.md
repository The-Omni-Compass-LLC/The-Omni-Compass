# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 156.8 | 79.53 |
| response time (ms), 95th percentile | 362.3 | 121.9 |
| response time (ms), 99th percentile | 593.8 | 171.9 |
| time over the response line (% of samples) | 2.529 | 0.0241 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.2433 |
| utilisation (used / allocatable) | 0.03858 | 0.03693 |
| CPU used (cores), mean | 0.9259 | 0.8862 |
| Omni's own CPU (cores), mean | 0 | 0.00919 |
| CPU used with Omni's own (cores), mean | 0.9259 | 0.8954 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 753 |
| HPA replicas, mean | 8.416 | 7.883 |
| pods started | 5.3 | 2.8 |
| pod start wait, total (s) | 8.5 | 4.1 |
| pod start wait, mean (s) | 1.617 | 1.27 |
| host CPU busy, the real machine under kind (%) | 28.51 | 27.57 |
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
| node-hours | 1.515 | 1.512 | −0.2% | −0.0080 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.5 | −0.4% | −1.2394 to −0.0323 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.5 | −0.4% | −1.2394 to −0.0323 | yes: GAIN |
| response time (ms), mean | 156.8 | 79.53 | −49.3% | −101.1572 to −53.4333 | yes: GAIN |
| response time (ms), 95th percentile | 362.3 | 121.9 | −66.3% | −308.4984 to −172.2996 | yes: GAIN |
| response time (ms), 99th percentile | 593.8 | 171.9 | −71.1% | −531.8573 to −311.9525 | yes: GAIN |
| time over the response line (% of samples) | 2.529 | 0.0241 | −99.0% | −3.8136 to −1.1962 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.7 | 0 | −100.0% | −4.0924 to −1.3076 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 | +16.300 (native is 0) | +12.5292 to +20.0708 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.27 | 0.2433 | −9.9% | −0.3852 to +0.3319 | no |
| utilisation (used / allocatable) | 0.03858 | 0.03693 | −4.3% | −0.0026 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9259 | 0.8862 | −4.3% | −0.0612 to −0.0182 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00919 | +0.009 (native is 0) | +0.0078 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9259 | 0.8954 | −3.3% | −0.0509 to −0.0100 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 730.6 | 753 | +3.1% | +4.8836 to +39.8006 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.416 | 7.883 | −6.3% | −1.5957 to +0.5302 | no |
| pods started | 5.3 | 2.8 | −47.2% | −4.0544 to −0.9456 | yes: GAIN |
| pod start wait, total (s) | 8.5 | 4.1 | −51.8% | −6.9503 to −1.8497 | yes: GAIN |
| pod start wait, mean (s) | 1.617 | 1.27 | −21.4% | −0.8402 to +0.1469 | no |
| host CPU busy, the real machine under kind (%) | 28.51 | 27.57 | −3.3% | −1.6682 to −0.2055 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*