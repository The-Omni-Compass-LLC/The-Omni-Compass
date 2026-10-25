# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.932 |
| node-hours | 2.517 | 2.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 269.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 120.3 | 91.19 |
| response time (ms), 95th percentile | 205 | 200.9 |
| response time (ms), 99th percentile | 298.5 | 307.6 |
| time over the response line (% of samples) | 0.1693 | 0.2019 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 899.3 | 970.9 |
| utilisation (used / allocatable) | 0.058 | 0.05864 |
| CPU used (cores), mean | 1.392 | 1.392 |
| Omni's own CPU (cores), mean | 0 | 0.01159 |
| CPU used with Omni's own (cores), mean | 1.392 | 1.404 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.9 | 462.9 |
| HPA replicas, mean | 1.949 | 1.963 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 42.17 | 42.95 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1361 | 1371 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.518 |
| queue: job wait, submitted to its first pod running, mean (s) | 121.4 | 115.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 544.1 | 598.3 |
| queue: job turnaround, submitted to done, mean (s) | 706.1 | 736.5 |
| queue: jobs unfinished at the window's end | 6.9 | 6.7 |

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
| worker nodes in service, mean | 6 | 5.932 | −1.1% | −0.1588 to +0.0228 | no |
| node-hours | 2.517 | 2.488 | −1.1% | −0.0667 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271.7 | +0.0% | −0.5756 to +0.8441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 269.5 | −0.7% | −5.0378 to +1.0271 | no |
| response time (ms), mean | 120.3 | 91.19 | −24.2% | −35.7850 to −22.4672 | yes: GAIN |
| response time (ms), 95th percentile | 205 | 200.9 | −2.0% | −13.3862 to +5.3262 | no |
| response time (ms), 99th percentile | 298.5 | 307.6 | +3.1% | −7.0478 to +25.3072 | no |
| time over the response line (% of samples) | 0.1693 | 0.2019 | +19.3% | −0.0548 to +0.1200 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.500 (native is 0) | +10.2317 to +14.7683 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 899.3 | 970.9 | +8.0% | −15.7501 to +159.0501 | no |
| utilisation (used / allocatable) | 0.058 | 0.05864 | +1.1% | −0.0008 to +0.0021 | no |
| CPU used (cores), mean | 1.392 | 1.392 | +0.0% | −0.0368 to +0.0372 | no |
| Omni's own CPU (cores), mean | 0 | 0.01159 | +0.012 (native is 0) | +0.0106 to +0.0126 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.392 | 1.404 | +0.8% | −0.0254 to +0.0490 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.9 | 462.9 | −0.7% | −13.0934 to +6.9755 | no |
| HPA replicas, mean | 1.949 | 1.963 | +0.7% | −0.1264 to +0.1535 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 42.17 | 42.95 | +1.9% | −0.3299 to +1.9001 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1361 | 1371 | +0.8% | −28.2960 to +49.0960 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.518 | −8.0% | −1.0549 to +0.0918 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 121.4 | 115.4 | −5.0% | −31.1404 to +19.0821 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 544.1 | 598.3 | +10.0% | −112.1966 to +220.5966 | no |
| queue: job turnaround, submitted to done, mean (s) | 706.1 | 736.5 | +4.3% | −33.5241 to +94.2991 | no |
| queue: jobs unfinished at the window's end | 6.9 | 6.7 | −2.9% | −2.1892 to +1.7892 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*