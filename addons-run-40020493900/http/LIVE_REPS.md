# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 192.1 | 79.85 |
| response time (ms), 95th percentile | 452.3 | 121.9 |
| response time (ms), 99th percentile | 614.8 | 218.6 |
| time over the response line (% of samples) | 3.949 | 0.08507 |
| failed requests (%) | 0 | 0.01205 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.1067 |
| utilisation (used / allocatable) | 0.0299 | 0.04556 |
| CPU used (cores), mean | 0.7176 | 1.094 |
| Omni's own CPU (cores), mean | 0 | 0.0094 |
| CPU used with Omni's own (cores), mean | 0.7176 | 1.103 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 873.6 | 593.3 |
| HPA replicas, mean | 2.884 | 2.361 |
| pods started | 2.7 | 2.1 |
| pod start wait, total (s) | 3.2 | 2.9 |
| pod start wait, mean (s) | 1.167 | 1.383 |
| host CPU busy, the real machine under kind (%) | 22.68 | 33.76 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.13e-17 to +1.295e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.517 | 1.515 | -0.1% | -0.009051 to +0.004718 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 161 | +2.1% | +2.608 to +4.158 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 161 | +2.1% | +2.608 to +4.158 | yes: power given |
| response time (ms), mean | 192.1 | 79.85 | -58.4% | -130.7 to -93.86 | yes: GAIN |
| response time (ms), 95th percentile | 452.3 | 121.9 | -73.0% | -385.6 to -275.1 | yes: GAIN |
| response time (ms), 99th percentile | 614.8 | 218.6 | -64.4% | -459.2 to -333.1 | yes: GAIN |
| time over the response line (% of samples) | 3.949 | 0.08507 | -97.8% | -5.937 to -1.791 | yes: GAIN |
| failed requests (%) | 0 | 0.01205 | +0.012 (native is 0) | -0.0152 to +0.0393 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 0 | -100.0% | -6.487 to -2.113 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.7 | +4.7 (native is 0) | +3.349 to +6.051 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.1067 | +100.0% | -0.02709 to +0.1338 | no |
| utilisation (used / allocatable) | 0.0299 | 0.04556 | +52.4% | +0.01292 to +0.01841 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7176 | 1.094 | +52.4% | +0.31 to +0.4419 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0094 | +0.0094 (native is 0) | +0.007883 to +0.01092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7176 | 1.103 | +53.7% | +0.3181 to +0.4526 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 873.6 | 593.3 | -32.1% | -295.3 to -265.3 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.884 | 2.361 | -18.2% | -0.7206 to -0.3264 | yes: GAIN |
| pods started | 2.7 | 2.1 | -22.2% | -0.9694 to -0.2306 | yes: GAIN |
| pod start wait, total (s) | 3.2 | 2.9 | -9.4% | -1.314 to +0.7144 | no |
| pod start wait, mean (s) | 1.167 | 1.383 | +18.6% | -0.1345 to +0.5679 | no |
| host CPU busy, the real machine under kind (%) | 22.68 | 33.76 | +48.8% | +8.919 to +13.24 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*