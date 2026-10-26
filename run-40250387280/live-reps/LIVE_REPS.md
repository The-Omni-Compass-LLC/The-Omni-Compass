# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.1 | 171.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.1 | 171.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 496.1 | 413 |
| response time (ms), 95th percentile | 2099 | 1855 |
| response time (ms), 99th percentile | 5436 | 5270 |
| time over the response line (% of samples) | 22.19 | 19.7 |
| failed requests (%) | 2.688 | 2.946 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.052 | 1.197 |
| utilisation (used / allocatable) | 0.09465 | 0.0938 |
| CPU used (cores), mean | 2.272 | 2.251 |
| Omni's own CPU (cores), mean | 0 | 0.01209 |
| CPU used with Omni's own (cores), mean | 2.272 | 2.263 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 308 | 309.7 |
| HPA replicas, mean | 14.96 | 14.98 |
| pods started | 5.7 | 5.2 |
| pod start wait, total (s) | 9.2 | 9.5 |
| pod start wait, mean (s) | 1.606 | 1.769 |
| host CPU busy, the real machine under kind (%) | 65.3 | 64.96 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 280.3 | 285 |
| second app: response time (ms), 99th percentile | 2075 | 2021 |
| second app: time over the response line (% of samples) | 14.03 | 13.9 |
| second app: failed requests (%) | 11.61 | 11.73 |

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
| node-hours | 1.516 | 1.516 | −0.0% | −0.0068 to +0.0061 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.1 | 171.8 | −0.1% | −0.8990 to +0.4128 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.1 | 171.8 | −0.1% | −0.8990 to +0.4128 | no |
| response time (ms), mean | 496.1 | 413 | −16.7% | −130.0628 to −36.0599 | yes: GAIN |
| response time (ms), 95th percentile | 2099 | 1855 | −11.6% | −414.0525 to −73.9785 | yes: GAIN |
| response time (ms), 99th percentile | 5436 | 5270 | −3.0% | −915.9162 to +585.6516 | no |
| time over the response line (% of samples) | 22.19 | 19.7 | −11.2% | −3.7993 to −1.1749 | yes: GAIN |
| failed requests (%) | 2.688 | 2.946 | +9.6% | −0.4670 to +0.9834 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.9 | −1.2% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.2 | +52.200 (native is 0) | +41.0990 to +63.3010 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.052 | 1.197 | +13.8% | −0.7519 to +1.0419 | no |
| utilisation (used / allocatable) | 0.09465 | 0.0938 | −0.9% | −0.0024 to +0.0007 | no |
| CPU used (cores), mean | 2.272 | 2.251 | −0.9% | −0.0571 to +0.0166 | no |
| Omni's own CPU (cores), mean | 0 | 0.01209 | +0.012 (native is 0) | +0.0111 to +0.0131 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.272 | 2.263 | −0.4% | −0.0448 to +0.0285 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 308 | 309.7 | +0.5% | −3.2584 to +6.6009 | no |
| HPA replicas, mean | 14.96 | 14.98 | +0.1% | −0.1548 to +0.1884 | no |
| pods started | 5.7 | 5.2 | −8.8% | −1.2726 to +0.2726 | no |
| pod start wait, total (s) | 9.2 | 9.5 | +3.3% | −2.7169 to +3.3169 | no |
| pod start wait, mean (s) | 1.606 | 1.769 | +10.1% | −0.2312 to +0.5569 | no |
| host CPU busy, the real machine under kind (%) | 65.3 | 64.96 | −0.5% | −1.0081 to +0.3317 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 280.3 | 285 | +1.7% | −24.6524 to +34.0574 | no |
| second app: response time (ms), 99th percentile | 2075 | 2021 | −2.6% | −1089.1115 to +981.1941 | no |
| second app: time over the response line (% of samples) | 14.03 | 13.9 | −0.9% | −0.6506 to +0.4021 | no |
| second app: failed requests (%) | 11.61 | 11.73 | +1.1% | −0.4010 to +0.6527 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*