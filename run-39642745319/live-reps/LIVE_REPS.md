# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.711 |
| node-hours | 2.518 | 2.396 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 265.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 499.6 | 458 |
| response time (ms), 95th percentile | 2182 | 2181 |
| response time (ms), 99th percentile | 3185 | 3275 |
| time over the response line (% of samples) | 20.8 | 20.27 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 13 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.54 | 22.43 |
| utilisation (used / allocatable) | 0.06503 | 0.06877 |
| CPU used (cores), mean | 1.561 | 1.57 |
| Omni's own CPU (cores), mean | 0 | 0.0171 |
| CPU used with Omni's own (cores), mean | 1.561 | 1.587 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.1 | 405.2 |
| HPA replicas, mean | 1.998 | 2.326 |
| pods started | 0 | 0.9 |
| pod start wait, total (s) | 0 | 1.1 |
| pod start wait, mean (s) | 0 | 0.8333 |
| host CPU busy, the real machine under kind (%) | 46.9 | 47.86 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 850.5 | 852.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.46 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.008 | 1.004 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.7 |
| queue: job turnaround, submitted to done, mean (s) | 158 | 159.4 |
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
| worker nodes in service, mean | 6 | 5.711 | -4.8% | -0.7197 to +0.1424 | no |
| node-hours | 2.518 | 2.396 | -4.8% | -0.3028 to +0.05882 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.9 | +0.1% | -0.382 to +0.8049 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 265.8 | -3.2% | -22.41 to +4.659 | no |
| response time (ms), mean | 499.6 | 458 | -8.3% | -65.98 to -17.24 | yes: GAIN |
| response time (ms), 95th percentile | 2182 | 2181 | -0.1% | -177.1 to +174.7 | no |
| response time (ms), 99th percentile | 3185 | 3275 | +2.8% | -94.4 to +274.6 | no |
| time over the response line (% of samples) | 20.8 | 20.27 | -2.6% | -1.777 to +0.7053 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 13 | +1.6% | -0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.9 | +26.9 (native is 0) | +19.69 to +34.11 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.54 | 22.43 | +4.1% | -2.033 to +3.81 | no |
| utilisation (used / allocatable) | 0.06503 | 0.06877 | +5.8% | -0.001482 to +0.008962 | no |
| CPU used (cores), mean | 1.561 | 1.57 | +0.6% | -0.01158 to +0.03006 | no |
| Omni's own CPU (cores), mean | 0 | 0.0171 | +0.0171 (native is 0) | +0.01536 to +0.01884 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.561 | 1.587 | +1.7% | +0.005254 to +0.04743 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.1 | 405.2 | -4.7% | -47.11 to +7.419 | no |
| HPA replicas, mean | 1.998 | 2.326 | +16.4% | +0.2221 to +0.4343 | yes: power given |
| pods started | 0 | 0.9 | +0.9 (native is 0) | +0.2737 to +1.526 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | +0.2436 to +1.956 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8333 | +0.833 (native is 0) | +0.3665 to +1.3 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.9 | 47.86 | +2.0% | +0.5476 to +1.374 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 850.5 | 852.3 | +0.2% | -2.215 to +5.815 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.46 | -9.0% | -1.334 to +0.2534 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.008 | 1.004 | -0.4% | -0.1378 to +0.1295 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.7 | +42.1% | -0.07931 to +1.679 | no |
| queue: job turnaround, submitted to done, mean (s) | 158 | 159.4 | +0.9% | -1.906 to +4.765 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*