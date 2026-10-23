# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.967 |
| node-hours | 2.518 | 2.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 270.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 119 | 91.68 |
| response time (ms), 95th percentile | 205.3 | 200.7 |
| response time (ms), 99th percentile | 296.4 | 308.8 |
| time over the response line (% of samples) | 0.1929 | 0.171 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 960.3 | 1014 |
| utilisation (used / allocatable) | 0.05863 | 0.05821 |
| CPU used (cores), mean | 1.407 | 1.389 |
| Omni's own CPU (cores), mean | 0 | 0.04285 |
| CPU used with Omni's own (cores), mean | 1.407 | 1.432 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 464.9 |
| HPA replicas, mean | 2.002 | 2.052 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.1 | 0.6 |
| pod start wait, mean (s) | 0.1 | 0.2667 |
| host CPU busy, the real machine under kind (%) | 43.46 | 44.28 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1378 | 1381 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.611 |
| queue: job wait, submitted to its first pod running, mean (s) | 112 | 128.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 529.5 | 610.9 |
| queue: job turnaround, submitted to done, mean (s) | 743.2 | 766.7 |
| queue: jobs unfinished at the window's end | 7.4 | 8.4 |

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
| worker nodes in service, mean | 6 | 5.967 | -0.6% | -0.06744 to +0.0009095 | no |
| node-hours | 2.518 | 2.503 | -0.6% | -0.03044 to +0.001165 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.7 | -0.1% | -1.149 to +0.6519 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 270.6 | -0.5% | -2.453 to -0.1399 | yes: GAIN |
| response time (ms), mean | 119 | 91.68 | -22.9% | -38.71 to -15.89 | yes: GAIN |
| response time (ms), 95th percentile | 205.3 | 200.7 | -2.2% | -20.28 to +11.06 | no |
| response time (ms), 99th percentile | 296.4 | 308.8 | +4.2% | -10.17 to +35.05 | no |
| time over the response line (% of samples) | 0.1929 | 0.171 | -11.4% | -0.1268 to +0.083 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29 | +29 (native is 0) | +17.81 to +40.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 960.3 | 1014 | +5.5% | -42.55 to +149 | no |
| utilisation (used / allocatable) | 0.05863 | 0.05821 | -0.7% | -0.00229 to +0.001459 | no |
| CPU used (cores), mean | 1.407 | 1.389 | -1.2% | -0.06 to +0.02494 | no |
| Omni's own CPU (cores), mean | 0 | 0.04285 | +0.0429 (native is 0) | +0.03762 to +0.04808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.432 | +1.8% | -0.01619 to +0.06683 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 464.9 | +0.6% | -9.519 to +15.31 | no |
| HPA replicas, mean | 2.002 | 2.052 | +2.5% | -0.1897 to +0.2885 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.4578 to +1.058 | no |
| pod start wait, total (s) | 0.1 | 0.6 | +500.0% | -0.6802 to +1.68 | no |
| pod start wait, mean (s) | 0.1 | 0.2667 | +166.7% | -0.3391 to +0.6725 | no |
| host CPU busy, the real machine under kind (%) | 43.46 | 44.28 | +1.9% | -0.7321 to +2.379 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1378 | 1381 | +0.2% | -16.78 to +21.18 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.611 | -6.5% | -0.7047 to -0.07372 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 112 | 128.6 | +14.7% | -9.429 to +42.48 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 529.5 | 610.9 | +15.4% | -70.15 to +233 | no |
| queue: job turnaround, submitted to done, mean (s) | 743.2 | 766.7 | +3.2% | -23.15 to +70.11 | no |
| queue: jobs unfinished at the window's end | 7.4 | 8.4 | +13.5% | -0.2617 to +2.262 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*