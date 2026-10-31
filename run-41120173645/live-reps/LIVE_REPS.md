# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.1 | 172.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.1 | 172.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 511.8 | 495.6 |
| response time (ms), 95th percentile | 2107 | 2245 |
| response time (ms), 99th percentile | 5241 | 5378 |
| time over the response line (% of samples) | 24.2 | 22.79 |
| failed requests (%) | 3.382 | 2.387 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.562 | 1.973 |
| utilisation (used / allocatable) | 0.0967 | 0.09604 |
| CPU used (cores), mean | 2.321 | 2.305 |
| Omni's own CPU (cores), mean | 0 | 0.01325 |
| CPU used with Omni's own (cores), mean | 2.321 | 2.318 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305 | 306.3 |
| HPA replicas, mean | 14.95 | 15.56 |
| pods started | 5.4 | 4.2 |
| pod start wait, total (s) | 8.7 | 6.9 |
| pod start wait, mean (s) | 1.621 | 1.572 |
| host CPU busy, the real machine under kind (%) | 67.38 | 67.33 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 276.3 | 276.1 |
| second app: response time (ms), 99th percentile | 2217 | 1908 |
| second app: time over the response line (% of samples) | 14.44 | 14.27 |
| second app: failed requests (%) | 12.4 | 12.53 |

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
| node-hours | 1.512 | 1.516 | +0.2% | −0.0011 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.1 | 172.3 | +0.1% | −0.5475 to +0.8711 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.1 | 172.3 | +0.1% | −0.5475 to +0.8711 | no |
| response time (ms), mean | 511.8 | 495.6 | −3.2% | −29.9248 to −2.4855 | yes: GAIN |
| response time (ms), 95th percentile | 2107 | 2245 | +6.6% | −50.1453 to +326.8403 | no |
| response time (ms), 99th percentile | 5241 | 5378 | +2.6% | −748.1713 to +1023.0941 | no |
| time over the response line (% of samples) | 24.2 | 22.79 | −5.8% | −3.2420 to +0.4165 | no |
| failed requests (%) | 3.382 | 2.387 | −29.4% | −1.7175 to −0.2740 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 8.1 | −10.0% | −1.4278 to −0.3722 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.9 | +43.900 (native is 0) | +33.1442 to +54.6558 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.562 | 1.973 | +26.4% | −0.4185 to +1.2418 | no |
| utilisation (used / allocatable) | 0.0967 | 0.09604 | −0.7% | −0.0025 to +0.0011 | no |
| CPU used (cores), mean | 2.321 | 2.305 | −0.7% | −0.0589 to +0.0272 | no |
| Omni's own CPU (cores), mean | 0 | 0.01325 | +0.013 (native is 0) | +0.0120 to +0.0145 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.321 | 2.318 | −0.1% | −0.0451 to +0.0399 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305 | 306.3 | +0.4% | −5.4042 to +7.8536 | no |
| HPA replicas, mean | 14.95 | 15.56 | +4.1% | +0.0549 to +1.1645 | yes: power given |
| pods started | 5.4 | 4.2 | −22.2% | −2.0121 to −0.3879 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 6.9 | −20.7% | −3.8176 to +0.2176 | no |
| pod start wait, mean (s) | 1.621 | 1.572 | −3.0% | −0.3827 to +0.2846 | no |
| host CPU busy, the real machine under kind (%) | 67.38 | 67.33 | −0.1% | −0.7198 to +0.6084 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 276.3 | 276.1 | −0.1% | −55.5060 to +55.1350 | no |
| second app: response time (ms), 99th percentile | 2217 | 1908 | −13.9% | −1186.2483 to +568.5283 | no |
| second app: time over the response line (% of samples) | 14.44 | 14.27 | −1.2% | −0.8455 to +0.5002 | no |
| second app: failed requests (%) | 12.4 | 12.53 | +1.1% | −0.3712 to +0.6400 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*