# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.79 |
| node-hours | 2.513 | 2.011 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 233.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 277.2 | 249.9 |
| response time (ms), 95th percentile | 887.4 | 937.7 |
| response time (ms), 99th percentile | 1259 | 1354 |
| time over the response line (% of samples) | 16.38 | 15.62 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.04 | 9.34 |
| utilisation (used / allocatable) | 0.05725 | 0.0717 |
| CPU used (cores), mean | 1.374 | 1.353 |
| Omni's own CPU (cores), mean | 0 | 0.01569 |
| CPU used with Omni's own (cores), mean | 1.374 | 1.369 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.3 | 412.1 |
| HPA replicas, mean | 1.972 | 2.254 |
| pods started | 0.1 | 0.8 |
| pod start wait, total (s) | 0.2 | 1.5 |
| pod start wait, mean (s) | 0.2 | 1.033 |
| host CPU busy, the real machine under kind (%) | 38.68 | 39.44 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 755.2 | 756.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.992 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.05833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 63.77 | 64.4 |
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
| worker nodes in service, mean | 6 | 4.79 | −20.2% | −2.0128 to −0.4064 | yes: GAIN |
| node-hours | 2.513 | 2.011 | −20.0% | −0.8391 to −0.1652 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.6 | +0.1% | −0.2483 to +1.0026 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 233.6 | −13.9% | −63.1083 to −12.1125 | yes: GAIN |
| response time (ms), mean | 277.2 | 249.9 | −9.8% | −46.0318 to −8.5400 | yes: GAIN |
| response time (ms), 95th percentile | 887.4 | 937.7 | +5.7% | −29.8110 to +130.4830 | no |
| response time (ms), 99th percentile | 1259 | 1354 | +7.6% | +7.9165 to +183.2637 | yes: LOSS |
| time over the response line (% of samples) | 16.38 | 15.62 | −4.7% | −1.5991 to +0.0728 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.9 | +1.3% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.1 | +38.100 (native is 0) | +23.7128 to +52.4872 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.04 | 9.34 | +3.3% | −1.8925 to +2.4925 | no |
| utilisation (used / allocatable) | 0.05725 | 0.0717 | +25.2% | +0.0049 to +0.0240 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.374 | 1.353 | −1.5% | −0.0525 to +0.0109 | no |
| Omni's own CPU (cores), mean | 0 | 0.01569 | +0.016 (native is 0) | +0.0138 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.374 | 1.369 | −0.4% | −0.0383 to +0.0281 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.3 | 412.1 | −14.2% | −114.8882 to −21.6848 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.972 | 2.254 | +14.3% | +0.0591 to +0.5064 | yes: power given |
| pods started | 0.1 | 0.8 | +700.0% | −0.0578 to +1.4578 | no |
| pod start wait, total (s) | 0.2 | 1.5 | +650.0% | +0.0361 to +2.5639 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.033 | +416.7% | +0.0131 to +1.6535 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.68 | 39.44 | +2.0% | +0.2506 to +1.2614 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.2 | 756.8 | +0.2% | −1.0379 to +4.2379 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.992 | −33.5% | −3.2090 to −0.8071 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.05833 | +55.6% | −0.0002 to +0.0419 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.77 | 64.4 | +1.0% | −1.7759 to +3.0176 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*