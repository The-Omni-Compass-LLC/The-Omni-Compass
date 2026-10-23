# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.338 |
| node-hours | 2.516 | 2.235 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 250.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 274.6 | 264.4 |
| response time (ms), 95th percentile | 874.7 | 1009 |
| response time (ms), 99th percentile | 1256 | 1465 |
| time over the response line (% of samples) | 14.91 | 16.02 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.877 | 10.81 |
| utilisation (used / allocatable) | 0.05702 | 0.06479 |
| CPU used (cores), mean | 1.368 | 1.382 |
| Omni's own CPU (cores), mean | 0 | 0.04716 |
| CPU used with Omni's own (cores), mean | 1.368 | 1.429 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 435.8 |
| HPA replicas, mean | 1.97 | 2.706 |
| pods started | 0.1 | 1.8 |
| pod start wait, total (s) | 0.2 | 4.8 |
| pod start wait, mean (s) | 0.2 | 1.307 |
| host CPU busy, the real machine under kind (%) | 38.92 | 41.36 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 753.6 | 762.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.724 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.06667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 60.51 | 70.09 |
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
| worker nodes in service, mean | 6 | 5.338 | -11.0% | -1.268 to -0.05576 | yes: GAIN |
| node-hours | 2.516 | 2.235 | -11.2% | -0.5313 to -0.03079 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.4 | -0.0% | -0.7095 to +0.7006 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 250.6 | -7.7% | -39.59 to -2.074 | yes: GAIN |
| response time (ms), mean | 274.6 | 264.4 | -3.7% | -27.74 to +7.356 | no |
| response time (ms), 95th percentile | 874.7 | 1009 | +15.3% | +9.354 to +258.3 | yes: LOSS |
| response time (ms), 99th percentile | 1256 | 1465 | +16.7% | +64.56 to +354.4 | yes: LOSS |
| time over the response line (% of samples) | 14.91 | 16.02 | +7.5% | -0.1184 to +2.345 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.2 | 8.6 | +4.9% | -0.5048 to +1.305 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 128.5 | +128 (native is 0) | +74.28 to +182.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.877 | 10.81 | +9.5% | -1.311 to +3.185 | no |
| utilisation (used / allocatable) | 0.05702 | 0.06479 | +13.6% | +0.001679 to +0.01387 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.368 | 1.382 | +1.0% | -0.01576 to +0.0429 | no |
| Omni's own CPU (cores), mean | 0 | 0.04716 | +0.0472 (native is 0) | +0.04165 to +0.05267 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.368 | 1.429 | +4.4% | +0.02891 to +0.09254 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 435.8 | -9.7% | -84.37 to -8.853 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.97 | 2.706 | +37.3% | +0.2873 to +1.183 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +0.2283 to +3.172 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.8 | +2300.0% | +0.5649 to +8.635 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.307 | +553.3% | +0.223 to +1.99 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.92 | 41.36 | +6.3% | +2.006 to +2.867 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 753.6 | 762.3 | +1.2% | +0.4676 to +16.93 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.724 | -21.3% | -2.445 to -0.1078 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.06667 | +77.8% | -0.002407 to +0.06074 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 60.51 | 70.09 | +15.8% | +1.385 to +17.78 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*