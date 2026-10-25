# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.152 |
| node-hours | 2.513 | 2.162 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 245.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 449.6 | 395.1 |
| response time (ms), 95th percentile | 2720 | 2656 |
| response time (ms), 99th percentile | 4087 | 4113 |
| time over the response line (% of samples) | 15.11 | 14.41 |
| failed requests (%) | 0 | 0.01036 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174 | 176.5 |
| utilisation (used / allocatable) | 0.05798 | 0.06738 |
| CPU used (cores), mean | 1.392 | 1.378 |
| Omni's own CPU (cores), mean | 0 | 0.01577 |
| CPU used with Omni's own (cores), mean | 1.392 | 1.393 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.9 | 426.4 |
| HPA replicas, mean | 2.11 | 2.201 |
| pods started | 0 | 0.6 |
| pod start wait, total (s) | 0 | 0.9 |
| pod start wait, mean (s) | 0 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.16 | 40.52 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 545.2 | 544.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.744 |

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
| worker nodes in service, mean | 6 | 5.152 | −14.1% | −1.5014 to −0.1949 | yes: GAIN |
| node-hours | 2.513 | 2.162 | −14.0% | −0.6295 to −0.0738 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.2 | +0.2% | −0.4419 to +1.3250 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 245.5 | −9.6% | −47.0100 to −5.4027 | yes: GAIN |
| response time (ms), mean | 449.6 | 395.1 | −12.1% | −71.3871 to −37.4877 | yes: GAIN |
| response time (ms), 95th percentile | 2720 | 2656 | −2.4% | −156.1446 to +28.2466 | no |
| response time (ms), 99th percentile | 4087 | 4113 | +0.6% | −253.3913 to +305.3195 | no |
| time over the response line (% of samples) | 15.11 | 14.41 | −4.7% | −1.2810 to −0.1254 | yes: GAIN |
| failed requests (%) | 0 | 0.01036 | +0.010 (native is 0) | −0.0131 to +0.0338 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.3 | −1.1% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.500 (native is 0) | +11.0595 to +13.9405 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174 | 176.5 | +1.5% | −1.9808 to +7.0608 | no |
| utilisation (used / allocatable) | 0.05798 | 0.06738 | +16.2% | +0.0013 to +0.0175 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.392 | 1.378 | −1.0% | −0.0474 to +0.0195 | no |
| Omni's own CPU (cores), mean | 0 | 0.01577 | +0.016 (native is 0) | +0.0142 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.393 | +0.1% | −0.0312 to +0.0348 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.9 | 426.4 | −10.4% | −94.7142 to −4.3051 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.11 | 2.201 | +4.3% | −0.1477 to +0.3305 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1887 to +1.6113 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1887 to +1.6113 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.16 | 40.52 | +0.9% | −0.2383 to +0.9678 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 545.2 | 544.4 | −0.1% | −6.8301 to +5.2301 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.744 | −20.9% | −2.2042 to −0.3072 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*