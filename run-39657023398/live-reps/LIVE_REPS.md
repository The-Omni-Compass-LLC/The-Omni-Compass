# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.387 |
| node-hours | 2.513 | 2.26 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 254.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 392.6 | 359.6 |
| response time (ms), 95th percentile | 1643 | 1725 |
| response time (ms), 99th percentile | 2469 | 2601 |
| time over the response line (% of samples) | 15.94 | 15.51 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.35 | 13.12 |
| utilisation (used / allocatable) | 0.063 | 0.07068 |
| CPU used (cores), mean | 1.512 | 1.51 |
| Omni's own CPU (cores), mean | 0 | 0.017 |
| CPU used with Omni's own (cores), mean | 1.512 | 1.527 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.8 | 403.8 |
| HPA replicas, mean | 1.991 | 2.348 |
| pods started | 0 | 0.7 |
| pod start wait, total (s) | 0 | 1.1 |
| pod start wait, mean (s) | 0 | 0.95 |
| host CPU busy, the real machine under kind (%) | 43.33 | 44.03 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 806.6 | 808.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.982 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.08333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 115.7 | 116.3 |
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
| worker nodes in service, mean | 6 | 5.387 | -10.2% | -1.323 to +0.09796 | no |
| node-hours | 2.513 | 2.26 | -10.1% | -0.5538 to +0.04807 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 | +0.1% | -0.6623 to +1.148 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 254.6 | -6.9% | -41.66 to +3.664 | no |
| response time (ms), mean | 392.6 | 359.6 | -8.4% | -61.06 to -4.832 | yes: GAIN |
| response time (ms), 95th percentile | 1643 | 1725 | +5.0% | -49.2 to +213.7 | no |
| response time (ms), 99th percentile | 2469 | 2601 | +5.3% | -74.75 to +338.4 | no |
| time over the response line (% of samples) | 15.94 | 15.51 | -2.7% | -1.538 to +0.6705 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.9 | -1.0% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37 | +37 (native is 0) | +26.76 to +47.24 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.35 | 13.12 | -1.7% | -3.766 to +3.313 | no |
| utilisation (used / allocatable) | 0.063 | 0.07068 | +12.2% | -0.001446 to +0.01682 | no |
| CPU used (cores), mean | 1.512 | 1.51 | -0.1% | -0.01889 to +0.01474 | no |
| Omni's own CPU (cores), mean | 0 | 0.017 | +0.017 (native is 0) | +0.01564 to +0.01836 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.512 | 1.527 | +1.0% | -0.001319 to +0.03117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.8 | 403.8 | -8.8% | -84.91 to +6.775 | no |
| HPA replicas, mean | 1.991 | 2.348 | +17.9% | +0.1637 to +0.5501 | yes: power given |
| pods started | 0 | 0.7 | +0.7 (native is 0) | +0.2172 to +1.183 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | +0.3128 to +1.887 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.95 | +0.95 (native is 0) | +0.3091 to +1.591 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.33 | 44.03 | +1.6% | +0.2438 to +1.173 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 806.6 | 808.1 | +0.2% | -6.481 to +9.481 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.982 | -17.0% | -2.2 to +0.1638 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.08333 | -48.7% | -0.1971 to +0.03876 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.6 | -33.3% | -1.314 to +0.7144 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.7 | 116.3 | +0.5% | -5.856 to +7.081 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*