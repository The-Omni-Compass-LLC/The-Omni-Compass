# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.189 |
| node-hours | 2.511 | 2.17 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.1 | 269.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.1 | 244 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 259.2 | 219.6 |
| response time (ms), 95th percentile | 794.1 | 795.5 |
| response time (ms), 99th percentile | 1183 | 1220 |
| time over the response line (% of samples) | 12.26 | 11.57 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.157 | 8.042 |
| utilisation (used / allocatable) | 0.05498 | 0.06167 |
| CPU used (cores), mean | 1.32 | 1.273 |
| Omni's own CPU (cores), mean | 0 | 0.01589 |
| CPU used with Omni's own (cores), mean | 1.32 | 1.289 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.3 | 465.5 |
| HPA replicas, mean | 2.009 | 2.362 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 1 |
| pod start wait, mean (s) | 0 | 1 |
| host CPU busy, the real machine under kind (%) | 40.2 | 40.07 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 751.4 | 751.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.679 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.1125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 58.44 | 58 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.189 | −13.5% | −1.5948 to −0.0279 | yes: GAIN |
| node-hours | 2.511 | 2.17 | −13.6% | −0.6681 to −0.0127 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.1 | 269.5 | −0.2% | −1.5011 to +0.2487 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.1 | 244 | −9.7% | −51.0869 to −1.0488 | yes: GAIN |
| response time (ms), mean | 259.2 | 219.6 | −15.3% | −51.8516 to −27.3668 | yes: GAIN |
| response time (ms), 95th percentile | 794.1 | 795.5 | +0.2% | −30.7620 to +33.4810 | no |
| response time (ms), 99th percentile | 1183 | 1220 | +3.1% | −10.1830 to +82.8482 | no |
| time over the response line (% of samples) | 12.26 | 11.57 | −5.7% | −1.9310 to +0.5334 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.8 | +11.4% | +0.1427 to +1.4573 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.7 | +60.700 (native is 0) | +39.2804 to +82.1196 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.157 | 8.042 | −12.2% | −2.5522 to +0.3222 | no |
| utilisation (used / allocatable) | 0.05498 | 0.06167 | +12.2% | −0.0003 to +0.0137 | no |
| CPU used (cores), mean | 1.32 | 1.273 | −3.6% | −0.0908 to −0.0032 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01589 | +0.016 (native is 0) | +0.0144 to +0.0174 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.32 | 1.289 | −2.4% | −0.0757 to +0.0136 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 504.3 | 465.5 | −7.7% | −84.7397 to +7.0253 | no |
| HPA replicas, mean | 2.009 | 2.362 | +17.5% | +0.0480 to +0.6566 | yes: power given |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −0.3903 to +2.3903 | no |
| pod start wait, mean (s) | 0 | 1 | +1.000 (native is 0) | −0.3903 to +2.3903 | no |
| host CPU busy, the real machine under kind (%) | 40.2 | 40.07 | −0.3% | −2.2082 to +1.9421 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 751.4 | 751.1 | −0.0% | −2.8469 to +2.2469 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.679 | −22.0% | −2.5160 to −0.1261 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.1125 | −15.6% | −0.0739 to +0.0322 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 58.44 | 58 | −0.8% | −2.2622 to +1.3789 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*