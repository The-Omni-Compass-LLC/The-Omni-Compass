# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.981 |
| node-hours | 2.514 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 130.5 | 96.66 |
| response time (ms), 95th percentile | 227.7 | 210.3 |
| response time (ms), 99th percentile | 332 | 320.6 |
| time over the response line (% of samples) | 0.1928 | 0.2231 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1032 | 1081 |
| utilisation (used / allocatable) | 0.0585 | 0.05906 |
| CPU used (cores), mean | 1.404 | 1.413 |
| Omni's own CPU (cores), mean | 0 | 0.01193 |
| CPU used with Omni's own (cores), mean | 1.404 | 1.425 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 458.2 |
| HPA replicas, mean | 1.972 | 2.015 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 43.4 | 43.69 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1406 | 1417 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.746 |
| queue: job wait, submitted to its first pod running, mean (s) | 133.6 | 131.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 628 | 636.4 |
| queue: job turnaround, submitted to done, mean (s) | 780.1 | 816.6 |
| queue: jobs unfinished at the window's end | 8.9 | 10 |

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
| worker nodes in service, mean | 6 | 5.981 | -0.3% | -0.04636 to +0.007897 | no |
| node-hours | 2.514 | 2.508 | -0.2% | -0.02196 to +0.01018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.9 | +0.2% | -0.5591 to +1.45 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.3 | -0.1% | -1.544 to +1.226 | no |
| response time (ms), mean | 130.5 | 96.66 | -25.9% | -41.36 to -26.36 | yes: GAIN |
| response time (ms), 95th percentile | 227.7 | 210.3 | -7.6% | -26.05 to -8.699 | yes: GAIN |
| response time (ms), 99th percentile | 332 | 320.6 | -3.4% | -27.78 to +5.042 | no |
| time over the response line (% of samples) | 0.1928 | 0.2231 | +15.7% | -0.05736 to +0.118 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.2 | +13.2 (native is 0) | +11.21 to +15.19 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1032 | 1081 | +4.8% | -24.99 to +123.8 | no |
| utilisation (used / allocatable) | 0.0585 | 0.05906 | +1.0% | -0.0009275 to +0.002045 | no |
| CPU used (cores), mean | 1.404 | 1.413 | +0.6% | -0.02245 to +0.0403 | no |
| Omni's own CPU (cores), mean | 0 | 0.01193 | +0.0119 (native is 0) | +0.01102 to +0.01284 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.404 | 1.425 | +1.5% | -0.01032 to +0.05203 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462 | 458.2 | -0.8% | -14.54 to +7.037 | no |
| HPA replicas, mean | 1.972 | 2.015 | +2.2% | -0.0807 to +0.1675 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 43.4 | 43.69 | +0.7% | -0.7297 to +1.307 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1406 | 1417 | +0.8% | -12.58 to +35.38 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.746 | -4.2% | -0.6133 to +0.1053 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 133.6 | 131.9 | -1.3% | -33.08 to +29.68 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 628 | 636.4 | +1.3% | -232.3 to +249.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 780.1 | 816.6 | +4.7% | -17.82 to +90.92 | no |
| queue: jobs unfinished at the window's end | 8.9 | 10 | +12.4% | -0.791 to +2.991 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*