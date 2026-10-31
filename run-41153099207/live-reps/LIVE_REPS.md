# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 145.7 | 75.14 |
| response time (ms), 95th percentile | 330 | 112.1 |
| response time (ms), 99th percentile | 517.3 | 149.7 |
| time over the response line (% of samples) | 2.068 | 0.01212 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3783 | 0.1617 |
| utilisation (used / allocatable) | 0.03745 | 0.03517 |
| CPU used (cores), mean | 0.8989 | 0.844 |
| Omni's own CPU (cores), mean | 0 | 0.00877 |
| CPU used with Omni's own (cores), mean | 0.8989 | 0.8528 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.5 | 790.4 |
| HPA replicas, mean | 8.302 | 7.847 |
| pods started | 5.5 | 3 |
| pod start wait, total (s) | 8.7 | 4.7 |
| pod start wait, mean (s) | 1.62 | 1.712 |
| host CPU busy, the real machine under kind (%) | 27.36 | 26.62 |
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
| node-hours | 1.511 | 1.512 | +0.0% | −0.0012 to +0.0022 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.1 | −0.3% | −0.8465 to −0.0780 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.1 | −0.3% | −0.8465 to −0.0780 | yes: GAIN |
| response time (ms), mean | 145.7 | 75.14 | −48.4% | −97.8995 to −43.2821 | yes: GAIN |
| response time (ms), 95th percentile | 330 | 112.1 | −66.0% | −296.0118 to −139.8342 | yes: GAIN |
| response time (ms), 99th percentile | 517.3 | 149.7 | −71.1% | −500.6005 to −234.4793 | yes: GAIN |
| time over the response line (% of samples) | 2.068 | 0.01212 | −99.4% | −3.5312 to −0.5801 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 0 | −100.0% | −3.4306 to −0.5694 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 | +15.900 (native is 0) | +13.2140 to +18.5860 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3783 | 0.1617 | −57.3% | −0.5107 to +0.0774 | no |
| utilisation (used / allocatable) | 0.03745 | 0.03517 | −6.1% | −0.0036 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8989 | 0.844 | −6.1% | −0.0865 to −0.0233 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00877 | +0.009 (native is 0) | +0.0074 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8989 | 0.8528 | −5.1% | −0.0766 to −0.0156 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.5 | 790.4 | +4.6% | +14.6059 to +55.2184 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.302 | 7.847 | −5.5% | −1.3469 to +0.4381 | no |
| pods started | 5.5 | 3 | −45.5% | −3.1952 to −1.8048 | yes: GAIN |
| pod start wait, total (s) | 8.7 | 4.7 | −46.0% | −5.4306 to −2.5694 | yes: GAIN |
| pod start wait, mean (s) | 1.62 | 1.712 | +5.7% | −0.1411 to +0.3244 | no |
| host CPU busy, the real machine under kind (%) | 27.36 | 26.62 | −2.7% | −1.4769 to −0.0063 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*