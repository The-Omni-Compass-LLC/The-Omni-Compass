# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.155 |
| node-hours | 2.51 | 2.161 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 245.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 250.3 | 236.8 |
| response time (ms), 95th percentile | 671.7 | 851.6 |
| response time (ms), 99th percentile | 1092 | 1388 |
| time over the response line (% of samples) | 10.56 | 11.36 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.99 | 14.98 |
| utilisation (used / allocatable) | 0.06041 | 0.06894 |
| CPU used (cores), mean | 1.45 | 1.416 |
| Omni's own CPU (cores), mean | 0 | 0.01666 |
| CPU used with Omni's own (cores), mean | 1.45 | 1.432 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458 | 418 |
| HPA replicas, mean | 1.983 | 2.356 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.9 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 41.78 | 42.83 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 786.4 | 794.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.503 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6542 | 0.7625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 102.6 | 109.8 |
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
| worker nodes in service, mean | 6 | 5.155 | -14.1% | -1.589 to -0.101 | yes: GAIN |
| node-hours | 2.51 | 2.161 | -13.9% | -0.667 to -0.03016 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.2 | +0.1% | -1.104 to +1.538 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 245.7 | -9.7% | -50.83 to -1.741 | yes: GAIN |
| response time (ms), mean | 250.3 | 236.8 | -5.4% | -26.27 to -0.7795 | yes: GAIN |
| response time (ms), 95th percentile | 671.7 | 851.6 | +26.8% | +17.93 to +341.8 | yes: LOSS |
| response time (ms), 99th percentile | 1092 | 1388 | +27.2% | +2.921 to +590.1 | yes: LOSS |
| time over the response line (% of samples) | 10.56 | 11.36 | +7.6% | -1.03 to +2.628 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.3 | +1.1% | -0.306 to +0.506 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.1 | +33.1 (native is 0) | +23.86 to +42.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.99 | 14.98 | -0.1% | -2.499 to +2.482 | no |
| utilisation (used / allocatable) | 0.06041 | 0.06894 | +14.1% | +0.001317 to +0.01574 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.45 | 1.416 | -2.3% | -0.08004 to +0.01196 | no |
| Omni's own CPU (cores), mean | 0 | 0.01666 | +0.0167 (native is 0) | +0.0144 to +0.01892 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.432 | -1.2% | -0.06501 to +0.03025 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458 | 418 | -8.7% | -75.46 to -4.553 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.356 | +18.8% | +0.2102 to +0.5357 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | -0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.9 (native is 0) | -0.4676 to +2.268 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.1689 to +1.369 | no |
| host CPU busy, the real machine under kind (%) | 41.78 | 42.83 | +2.5% | +0.5673 to +1.536 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 786.4 | 794.2 | +1.0% | +2.492 to +13.11 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.503 | -25.0% | -2.721 to -0.2731 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6542 | 0.7625 | +16.6% | +0.01387 to +0.2028 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.4 | +16.7% | -0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 102.6 | 109.8 | +7.1% | +0.3848 to +14.1 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*