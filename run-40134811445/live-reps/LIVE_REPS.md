# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.767 |
| node-hours | 2.51 | 2.417 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 266.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 382.5 | 338 |
| response time (ms), 95th percentile | 1333 | 1272 |
| response time (ms), 99th percentile | 1878 | 1970 |
| time over the response line (% of samples) | 23.13 | 22.37 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 12.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.52 | 10.33 |
| utilisation (used / allocatable) | 0.0628 | 0.06545 |
| CPU used (cores), mean | 1.507 | 1.507 |
| Omni's own CPU (cores), mean | 0 | 0.01729 |
| CPU used with Omni's own (cores), mean | 1.507 | 1.524 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.7 | 421.5 |
| HPA replicas, mean | 1.998 | 2.582 |
| pods started | 0 | 0.5 |
| pod start wait, total (s) | 0 | 0.9 |
| pod start wait, mean (s) | 0 | 0.9 |
| host CPU busy, the real machine under kind (%) | 43.49 | 44.14 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 781.1 | 780.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.543 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2333 | 0.2083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 88.74 | 87.77 |
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
| worker nodes in service, mean | 6 | 5.767 | −3.9% | −0.5743 to +0.1090 | no |
| node-hours | 2.51 | 2.417 | −3.7% | −0.2357 to +0.0498 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.4 | +0.2% | −0.3003 to +1.3435 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 266.1 | −2.5% | −17.4858 to +3.9166 | no |
| response time (ms), mean | 382.5 | 338 | −11.6% | −70.7808 to −18.1416 | yes: GAIN |
| response time (ms), 95th percentile | 1333 | 1272 | −4.5% | −251.7319 to +130.7699 | no |
| response time (ms), 99th percentile | 1878 | 1970 | +4.9% | −183.3191 to +366.7665 | no |
| time over the response line (% of samples) | 23.13 | 22.37 | −3.3% | −1.5841 to +0.0635 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 12.2 | −3.9% | −1.9405 to +0.9405 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 | +28.800 (native is 0) | +19.7847 to +37.8153 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.52 | 10.33 | −10.3% | −3.3244 to +0.9577 | no |
| utilisation (used / allocatable) | 0.0628 | 0.06545 | +4.2% | −0.0014 to +0.0067 | no |
| CPU used (cores), mean | 1.507 | 1.507 | −0.0% | −0.0206 to +0.0202 | no |
| Omni's own CPU (cores), mean | 0 | 0.01729 | +0.017 (native is 0) | +0.0164 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.507 | 1.524 | +1.1% | −0.0036 to +0.0378 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.7 | 421.5 | −3.0% | −32.9959 to +6.7339 | no |
| HPA replicas, mean | 1.998 | 2.582 | +29.2% | +0.3493 to +0.8194 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | +0.1230 to +0.8770 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1128 to +1.6872 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1128 to +1.6872 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.49 | 44.14 | +1.5% | +0.0686 to +1.2203 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.1 | 780.7 | −0.1% | −10.7888 to +9.9888 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.543 | −7.6% | −1.1199 to +0.2050 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2333 | 0.2083 | −10.7% | −0.0849 to +0.0349 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.9 | −10.0% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.74 | 87.77 | −1.1% | −10.8005 to +8.8588 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*