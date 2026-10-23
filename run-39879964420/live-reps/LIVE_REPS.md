# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.962 |
| node-hours | 2.512 | 2.08 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 238.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 310.3 | 285.4 |
| response time (ms), 95th percentile | 1284 | 1349 |
| response time (ms), 99th percentile | 1932 | 2257 |
| time over the response line (% of samples) | 11.6 | 11.06 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 83.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.97 | 16.08 |
| utilisation (used / allocatable) | 0.05567 | 0.06832 |
| CPU used (cores), mean | 1.336 | 1.337 |
| Omni's own CPU (cores), mean | 0 | 0.05094 |
| CPU used with Omni's own (cores), mean | 1.336 | 1.388 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.6 | 429.1 |
| HPA replicas, mean | 1.988 | 2.493 |
| pods started | 0 | 1.7 |
| pod start wait, total (s) | 0 | 2.9 |
| pod start wait, mean (s) | 0 | 0.8667 |
| host CPU busy, the real machine under kind (%) | 40.16 | 42.69 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 777.6 | 787.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.16 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.825 | 0.8125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 87.05 | 96.69 |
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
| worker nodes in service, mean | 6 | 4.962 | -17.3% | -1.836 to -0.2403 | yes: GAIN |
| node-hours | 2.512 | 2.08 | -17.2% | -0.7703 to -0.09323 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 271.1 | +0.2% | -0.09274 to +1.312 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 238.5 | -11.8% | -57.54 to -6.477 | yes: GAIN |
| response time (ms), mean | 310.3 | 285.4 | -8.0% | -42.53 to -7.176 | yes: GAIN |
| response time (ms), 95th percentile | 1284 | 1349 | +5.1% | -75.19 to +205.3 | no |
| response time (ms), 99th percentile | 1932 | 2257 | +16.8% | +15.37 to +633 | yes: LOSS |
| time over the response line (% of samples) | 11.6 | 11.06 | -4.7% | -1.019 to -0.06934 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 7.1 | +2.9% | -0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.7 | +103 (native is 0) | +87.36 to +118 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.97 | 16.08 | +7.4% | -0.259 to +2.476 | no |
| utilisation (used / allocatable) | 0.05567 | 0.06832 | +22.7% | +0.002754 to +0.02255 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.336 | 1.337 | +0.0% | -0.04155 to +0.04277 | no |
| Omni's own CPU (cores), mean | 0 | 0.05094 | +0.0509 (native is 0) | +0.0422 to +0.05968 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.336 | 1.388 | +3.9% | +0.009455 to +0.09365 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.6 | 429.1 | -13.9% | -122.1 to -16.96 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.988 | 2.493 | +25.4% | +0.1282 to +0.8812 | yes: power given |
| pods started | 0 | 1.7 | +1.7 (native is 0) | +0.2283 to +3.172 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.9 (native is 0) | +0.3001 to +5.5 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8667 | +0.867 (native is 0) | +0.1969 to +1.536 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.16 | 42.69 | +6.3% | +1.986 to +3.075 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 777.6 | 787.1 | +1.2% | +0.6859 to +18.31 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.16 | -30.7% | -3.22 to -0.4602 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.825 | 0.8125 | -1.5% | -0.1309 to +0.1059 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.4 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 87.05 | 96.69 | +11.1% | +0.1734 to +19.09 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*