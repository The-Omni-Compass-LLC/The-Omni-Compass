# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.757 |
| node-hours | 2.513 | 1.988 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.2 | 269.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.2 | 230.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 229.7 | 198.1 |
| response time (ms), 95th percentile | 814.3 | 835 |
| response time (ms), 99th percentile | 1333 | 1309 |
| time over the response line (% of samples) | 7.463 | 7.197 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.35 | 12.93 |
| utilisation (used / allocatable) | 0.05138 | 0.06689 |
| CPU used (cores), mean | 1.233 | 1.244 |
| Omni's own CPU (cores), mean | 0 | 0.0152 |
| CPU used with Omni's own (cores), mean | 1.233 | 1.259 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 537.1 | 445.7 |
| HPA replicas, mean | 1.964 | 2.006 |
| pods started | 0.1 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.5 |
| pod start wait, mean (s) | 0.4 | 0.3 |
| host CPU busy, the real machine under kind (%) | 37.74 | 38.61 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 753.8 | 755.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.009 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6583 | 0.7583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 62.07 | 63.91 |
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
| worker nodes in service, mean | 6 | 4.757 | −20.7% | −2.1385 to −0.3465 | yes: GAIN |
| node-hours | 2.513 | 1.988 | −20.9% | −0.8994 to −0.1501 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.2 | 269.1 | −0.0% | −0.7822 to +0.5374 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.2 | 230.1 | −14.5% | −67.3147 to −10.9675 | yes: GAIN |
| response time (ms), mean | 229.7 | 198.1 | −13.8% | −45.1569 to −18.1315 | yes: GAIN |
| response time (ms), 95th percentile | 814.3 | 835 | +2.5% | −17.3221 to +58.6191 | no |
| response time (ms), 99th percentile | 1333 | 1309 | −1.8% | −192.7535 to +145.2255 | no |
| time over the response line (% of samples) | 7.463 | 7.197 | −3.6% | −1.0191 to +0.4883 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.8 | 5.6 | +16.7% | −0.8101 to +2.4101 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.6 | +35.600 (native is 0) | +25.8433 to +45.3567 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.35 | 12.93 | +4.7% | −1.9777 to +3.1477 | no |
| utilisation (used / allocatable) | 0.05138 | 0.06689 | +30.2% | +0.0046 to +0.0264 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.233 | 1.244 | +0.9% | −0.0239 to +0.0460 | no |
| Omni's own CPU (cores), mean | 0 | 0.0152 | +0.015 (native is 0) | +0.0132 to +0.0172 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.233 | 1.259 | +2.1% | −0.0089 to +0.0615 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 537.1 | 445.7 | −17.0% | −155.1589 to −27.6461 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.006 | +2.1% | −0.1373 to +0.2211 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | −25.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 37.74 | 38.61 | +2.3% | +0.3145 to +1.4291 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 753.8 | 755.3 | +0.2% | −1.3262 to +4.3262 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.009 | −33.2% | −3.3657 to −0.6159 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6583 | 0.7583 | +15.2% | +0.0055 to +0.1945 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.4 | +27.3% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.07 | 63.91 | +3.0% | −0.7899 to +4.4732 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*