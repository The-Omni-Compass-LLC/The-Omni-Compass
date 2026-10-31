# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 204.6 | 86.16 |
| response time (ms), 95th percentile | 483.8 | 129.5 |
| response time (ms), 99th percentile | 656 | 282.7 |
| time over the response line (% of samples) | 5.009 | 0.3411 |
| failed requests (%) | 0.01408 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1333 |
| utilisation (used / allocatable) | 0.03021 | 0.04703 |
| CPU used (cores), mean | 0.7251 | 1.129 |
| Omni's own CPU (cores), mean | 0 | 0.01036 |
| CPU used with Omni's own (cores), mean | 0.7251 | 1.139 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 864.9 | 574.6 |
| HPA replicas, mean | 2.864 | 2.436 |
| pods started | 2.7 | 2.3 |
| pod start wait, total (s) | 3.7 | 3 |
| pod start wait, mean (s) | 1.383 | 1.283 |
| host CPU busy, the real machine under kind (%) | 23.34 | 34.84 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.517 | 1.52 | +0.2% | −0.0069 to +0.0126 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161.8 | +2.6% | +2.7026 to +5.6082 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161.8 | +2.6% | +2.7026 to +5.6082 | yes: power given |
| response time (ms), mean | 204.6 | 86.16 | −57.9% | −139.1587 to −97.7265 | yes: GAIN |
| response time (ms), 95th percentile | 483.8 | 129.5 | −73.2% | −408.1104 to −300.3956 | yes: GAIN |
| response time (ms), 99th percentile | 656 | 282.7 | −56.9% | −466.4179 to −280.1765 | yes: GAIN |
| time over the response line (% of samples) | 5.009 | 0.3411 | −93.2% | −6.9778 to −2.3576 | yes: GAIN |
| failed requests (%) | 0.01408 | 0 | −100.0% | −0.0459 to +0.0178 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 0.3 | −93.9% | −6.7380 to −2.4620 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 | +5.500 (native is 0) | +3.7724 to +7.2276 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.1333 | −28.6% | −0.3045 to +0.1978 | no |
| utilisation (used / allocatable) | 0.03021 | 0.04703 | +55.7% | +0.0141 to +0.0195 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7251 | 1.129 | +55.7% | +0.3390 to +0.4683 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01036 | +0.010 (native is 0) | +0.0087 to +0.0120 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7251 | 1.139 | +57.1% | +0.3479 to +0.4801 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 864.9 | 574.6 | −33.6% | −306.9650 to −273.6882 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.864 | 2.436 | −14.9% | −0.6151 to −0.2402 | yes: GAIN |
| pods started | 2.7 | 2.3 | −14.8% | −0.7694 to −0.0306 | yes: GAIN |
| pod start wait, total (s) | 3.7 | 3 | −18.9% | −1.1828 to −0.2172 | yes: GAIN |
| pod start wait, mean (s) | 1.383 | 1.283 | −7.2% | −0.2508 to +0.0508 | no |
| host CPU busy, the real machine under kind (%) | 23.34 | 34.84 | +49.3% | +9.5131 to +13.4858 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*