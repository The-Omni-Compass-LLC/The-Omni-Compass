# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.527 |
| node-hours | 2.518 | 2.317 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 260.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 562.7 | 517.1 |
| response time (ms), 95th percentile | 2194 | 2193 |
| response time (ms), 99th percentile | 2964 | 3008 |
| time over the response line (% of samples) | 25.46 | 24.31 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 12.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.8 | 18.87 |
| utilisation (used / allocatable) | 0.06754 | 0.07301 |
| CPU used (cores), mean | 1.621 | 1.619 |
| Omni's own CPU (cores), mean | 0 | 0.01797 |
| CPU used with Omni's own (cores), mean | 1.621 | 1.637 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.4 | 388.3 |
| HPA replicas, mean | 2.015 | 2.201 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.2 | 1.4 |
| pod start wait, mean (s) | 0.2 | 1.15 |
| host CPU busy, the real machine under kind (%) | 47.22 | 48.13 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 860.2 | 866.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.134 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.417 | 2.392 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8.8 | 14.1 |
| queue: job turnaround, submitted to done, mean (s) | 164.1 | 170.5 |
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
| worker nodes in service, mean | 6 | 5.527 | -7.9% | -1.062 to +0.1151 | no |
| node-hours | 2.518 | 2.317 | -8.0% | -0.4486 to +0.04698 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.3 | -0.1% | -1.344 to +0.9392 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 260.4 | -5.5% | -33.89 to +3.769 | no |
| response time (ms), mean | 562.7 | 517.1 | -8.1% | -76.04 to -15.17 | yes: GAIN |
| response time (ms), 95th percentile | 2194 | 2193 | -0.0% | -160.2 to +159.8 | no |
| response time (ms), 99th percentile | 2964 | 3008 | +1.5% | -137.9 to +226.6 | no |
| time over the response line (% of samples) | 25.46 | 24.31 | -4.5% | -2.595 to +0.2876 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.8 | 12.6 | -1.6% | -1.012 to +0.6121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 | +46.9 (native is 0) | +34.1 to +59.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.8 | 18.87 | +12.3% | -0.6926 to +4.823 | no |
| utilisation (used / allocatable) | 0.06754 | 0.07301 | +8.1% | -0.0008383 to +0.01176 | no |
| CPU used (cores), mean | 1.621 | 1.619 | -0.1% | -0.02608 to +0.02211 | no |
| Omni's own CPU (cores), mean | 0 | 0.01797 | +0.018 (native is 0) | +0.01694 to +0.019 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.621 | 1.637 | +1.0% | -0.008411 to +0.04038 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.4 | 388.3 | -6.5% | -59.25 to +5.04 | no |
| HPA replicas, mean | 2.015 | 2.201 | +9.2% | -0.06328 to +0.4338 | no |
| pods started | 0.1 | 0.6 | +500.0% | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0.2 | 1.4 | +600.0% | +0.04168 to +2.358 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.15 | +475.0% | +0.1876 to +1.712 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.22 | 48.13 | +1.9% | +0.3246 to +1.507 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 860.2 | 866.7 | +0.8% | -3.413 to +16.41 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.134 | -14.4% | -1.903 to +0.171 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.417 | 2.392 | +68.8% | -0.3721 to +2.322 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 8.8 | 14.1 | +60.2% | -3.184 to +13.78 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.1 | 170.5 | +3.9% | -2.089 to +15.03 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*