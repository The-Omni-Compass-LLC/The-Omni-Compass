# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.681 |
| node-hours | 2.516 | 1.965 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 270.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 228.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 208.4 | 174 |
| response time (ms), 95th percentile | 575.4 | 595.2 |
| response time (ms), 99th percentile | 858.6 | 841.6 |
| time over the response line (% of samples) | 7.354 | 7.38 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 5.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.957 | 7.878 |
| utilisation (used / allocatable) | 0.053 | 0.06749 |
| CPU used (cores), mean | 1.272 | 1.255 |
| Omni's own CPU (cores), mean | 0 | 0.01582 |
| CPU used with Omni's own (cores), mean | 1.272 | 1.271 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516.9 | 435.6 |
| HPA replicas, mean | 1.939 | 2.142 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.1 |
| pod start wait, mean (s) | 0 | 0.1 |
| host CPU busy, the real machine under kind (%) | 36.34 | 37.08 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 735.9 | 736.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.634 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.03333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 |
| queue: job turnaround, submitted to done, mean (s) | 43.25 | 43.18 |
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
| worker nodes in service, mean | 6 | 4.681 | −22.0% | −1.9302 to −0.7087 | yes: GAIN |
| node-hours | 2.516 | 1.965 | −21.9% | −0.8060 to −0.2950 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.9 | 270.3 | +0.1% | −0.2263 to +0.9538 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.9 | 228.8 | −15.2% | −60.0579 to −22.2355 | yes: GAIN |
| response time (ms), mean | 208.4 | 174 | −16.5% | −48.4096 to −20.3178 | yes: GAIN |
| response time (ms), 95th percentile | 575.4 | 595.2 | +3.5% | −35.7511 to +75.4681 | no |
| response time (ms), 99th percentile | 858.6 | 841.6 | −2.0% | −89.2298 to +55.3654 | no |
| time over the response line (% of samples) | 7.354 | 7.38 | +0.4% | −0.7325 to +0.7850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 5.9 | +3.5% | −1.3744 to +1.7744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.5 | +50.500 (native is 0) | +36.1294 to +64.8706 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.957 | 7.878 | −12.0% | −2.0446 to −0.1121 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.053 | 0.06749 | +27.3% | +0.0069 to +0.0221 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.272 | 1.255 | −1.3% | −0.0352 to +0.0011 | no |
| Omni's own CPU (cores), mean | 0 | 0.01582 | +0.016 (native is 0) | +0.0143 to +0.0173 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.272 | 1.271 | −0.1% | −0.0186 to +0.0162 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 516.9 | 435.6 | −15.7% | −130.6353 to −32.0045 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.939 | 2.142 | +10.4% | −0.0370 to +0.4422 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 36.34 | 37.08 | +2.0% | +0.5323 to +0.9466 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 735.9 | 736.1 | +0.0% | −1.3744 to +1.7744 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.634 | −39.4% | −3.3890 to −1.3439 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.03333 | +14.3% | −0.0286 to +0.0370 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 43.25 | 43.18 | −0.1% | −2.0545 to +1.9295 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*