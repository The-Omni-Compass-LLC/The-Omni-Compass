# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.105 |
| node-hours | 2.51 | 2.141 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 243.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 457.5 | 396.5 |
| response time (ms), 95th percentile | 2798 | 2640 |
| response time (ms), 99th percentile | 4288 | 4268 |
| time over the response line (% of samples) | 14.52 | 14.5 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 176.4 | 176.6 |
| utilisation (used / allocatable) | 0.05831 | 0.06657 |
| CPU used (cores), mean | 1.399 | 1.359 |
| Omni's own CPU (cores), mean | 0 | 0.01651 |
| CPU used with Omni's own (cores), mean | 1.399 | 1.375 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.2 | 430.5 |
| HPA replicas, mean | 2.033 | 2.354 |
| pods started | 0 | 0.6 |
| pod start wait, total (s) | 0 | 1.5 |
| pod start wait, mean (s) | 0 | 0.8333 |
| host CPU busy, the real machine under kind (%) | 40.12 | 40.41 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 540.9 | 540.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.67 |

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
| worker nodes in service, mean | 6 | 5.105 | −14.9% | −1.4230 to −0.3662 | yes: GAIN |
| node-hours | 2.51 | 2.141 | −14.7% | −0.5927 to −0.1463 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.6 | 271.3 | −0.1% | −0.9239 to +0.4283 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.6 | 243.2 | −10.4% | −45.0320 to −11.7094 | yes: GAIN |
| response time (ms), mean | 457.5 | 396.5 | −13.3% | −81.6328 to −40.2425 | yes: GAIN |
| response time (ms), 95th percentile | 2798 | 2640 | −5.7% | −298.7782 to −17.7258 | yes: GAIN |
| response time (ms), 99th percentile | 4288 | 4268 | −0.5% | −236.0100 to +196.8272 | no |
| time over the response line (% of samples) | 14.52 | 14.5 | −0.2% | −0.4759 to +0.4292 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.3 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.9 | +12.900 (native is 0) | +11.6633 to +14.1367 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 176.4 | 176.6 | +0.1% | −6.1348 to +6.4448 | no |
| utilisation (used / allocatable) | 0.05831 | 0.06657 | +14.2% | +0.0015 to +0.0150 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.399 | 1.359 | −2.9% | −0.0798 to −0.0019 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01651 | +0.017 (native is 0) | +0.0150 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.375 | −1.7% | −0.0634 to +0.0147 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.2 | 430.5 | −9.4% | −85.7444 to −3.5191 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.033 | 2.354 | +15.8% | +0.0503 to +0.5920 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| pod start wait, total (s) | 0 | 1.5 | +1.500 (native is 0) | −0.7176 to +3.7176 | no |
| pod start wait, mean (s) | 0 | 0.8333 | +0.833 (native is 0) | −0.0319 to +1.6985 | no |
| host CPU busy, the real machine under kind (%) | 40.12 | 40.41 | +0.7% | −0.3334 to +0.9163 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 540.9 | 540.6 | −0.1% | −8.5048 to +7.9048 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.67 | −22.2% | −2.0642 to −0.5962 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*