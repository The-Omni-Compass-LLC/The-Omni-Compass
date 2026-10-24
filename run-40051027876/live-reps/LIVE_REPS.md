# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.884 |
| node-hours | 2.513 | 2.046 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 236 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 259.1 | 224.2 |
| response time (ms), 95th percentile | 906.2 | 912.8 |
| response time (ms), 99th percentile | 1414 | 1453 |
| time over the response line (% of samples) | 11.61 | 11.07 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.1 | 9.988 |
| utilisation (used / allocatable) | 0.05639 | 0.06967 |
| CPU used (cores), mean | 1.353 | 1.339 |
| Omni's own CPU (cores), mean | 0 | 0.016 |
| CPU used with Omni's own (cores), mean | 1.353 | 1.355 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489 | 420.9 |
| HPA replicas, mean | 1.969 | 2.308 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 38.64 | 39.59 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 749.2 | 753.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.111 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 61.78 | 63.5 |
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
| worker nodes in service, mean | 6 | 4.884 | -18.6% | -1.926 to -0.3063 | yes: GAIN |
| node-hours | 2.513 | 2.046 | -18.6% | -0.8085 to -0.1255 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 | +0.0% | -0.5616 to +0.7035 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 236 | -12.9% | -60.74 to -9.34 | yes: GAIN |
| response time (ms), mean | 259.1 | 224.2 | -13.5% | -51.09 to -18.64 | yes: GAIN |
| response time (ms), 95th percentile | 906.2 | 912.8 | +0.7% | -82.5 to +95.59 | no |
| response time (ms), 99th percentile | 1414 | 1453 | +2.7% | -121.8 to +199.2 | no |
| time over the response line (% of samples) | 11.61 | 11.07 | -4.6% | -1.804 to +0.7266 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 7.8 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.7 | +34.7 (native is 0) | +26.95 to +42.45 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.1 | 9.988 | -1.1% | -2.271 to +2.048 | no |
| utilisation (used / allocatable) | 0.05639 | 0.06967 | +23.5% | +0.003135 to +0.02341 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.353 | 1.339 | -1.1% | -0.04176 to +0.01296 | no |
| Omni's own CPU (cores), mean | 0 | 0.016 | +0.016 (native is 0) | +0.01384 to +0.01816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.353 | 1.355 | +0.1% | -0.02663 to +0.02983 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489 | 420.9 | -13.9% | -122.2 to -14 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.308 | +17.2% | +0.1622 to +0.5159 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.4 (native is 0) | -0.2032 to +1.003 | no |
| host CPU busy, the real machine under kind (%) | 38.64 | 39.59 | +2.4% | +0.6818 to +1.202 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 749.2 | 753.5 | +0.6% | +0.59 to +8.01 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.111 | -31.5% | -3.157 to -0.6206 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.05833 | +27.3% | -0.02206 to +0.04706 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | -0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 61.78 | 63.5 | +2.8% | -1.759 to +5.201 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*