# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.609 |
| node-hours | 2.511 | 2.352 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 276.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 263.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 615.9 | 556.5 |
| response time (ms), 95th percentile | 3397 | 3372 |
| response time (ms), 99th percentile | 4523 | 4488 |
| time over the response line (% of samples) | 18.38 | 18.24 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 208.7 | 210 |
| utilisation (used / allocatable) | 0.06986 | 0.07397 |
| CPU used (cores), mean | 1.677 | 1.66 |
| Omni's own CPU (cores), mean | 0 | 0.01882 |
| CPU used with Omni's own (cores), mean | 1.677 | 1.679 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 397.9 | 382.4 |
| HPA replicas, mean | 2.242 | 2.393 |
| pods started | 0.1 | 0.5 |
| pod start wait, total (s) | 0.2 | 1.3 |
| pod start wait, mean (s) | 0.2 | 0.85 |
| host CPU busy, the real machine under kind (%) | 48.02 | 48.74 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 658.9 | 663.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.354 |

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
| worker nodes in service, mean | 6 | 5.609 | −6.5% | −0.7730 to −0.0096 | yes: GAIN |
| node-hours | 2.511 | 2.352 | −6.3% | −0.3235 to +0.0049 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 276.2 | +0.1% | −0.9260 to +1.6411 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 263.9 | −4.3% | −24.6480 to +0.7964 | no |
| response time (ms), mean | 615.9 | 556.5 | −9.6% | −70.3685 to −48.3292 | yes: GAIN |
| response time (ms), 95th percentile | 3397 | 3372 | −0.7% | −126.3878 to +77.3328 | no |
| response time (ms), 99th percentile | 4523 | 4488 | −0.8% | −163.4763 to +93.6361 | no |
| time over the response line (% of samples) | 18.38 | 18.24 | −0.8% | −0.5618 to +0.2760 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.2 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.6 | +11.600 (native is 0) | +10.1225 to +13.0775 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 208.7 | 210 | +0.6% | −4.6265 to +7.2232 | no |
| utilisation (used / allocatable) | 0.06986 | 0.07397 | +5.9% | −0.0004 to +0.0086 | no |
| CPU used (cores), mean | 1.677 | 1.66 | −1.0% | −0.0508 to +0.0177 | no |
| Omni's own CPU (cores), mean | 0 | 0.01882 | +0.019 (native is 0) | +0.0168 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.677 | 1.679 | +0.1% | −0.0322 to +0.0368 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 397.9 | 382.4 | −3.9% | −33.7675 to +2.8112 | no |
| HPA replicas, mean | 2.242 | 2.393 | +6.7% | −0.3587 to +0.6605 | no |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.2 | 1.3 | +550.0% | −1.0179 to +3.2179 | no |
| pod start wait, mean (s) | 0.2 | 0.85 | +325.0% | −0.5664 to +1.8664 | no |
| host CPU busy, the real machine under kind (%) | 48.02 | 48.74 | +1.5% | +0.2357 to +1.2020 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 658.9 | 663.5 | +0.7% | −1.4433 to +10.6433 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.354 | −10.8% | −1.2363 to −0.0553 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*