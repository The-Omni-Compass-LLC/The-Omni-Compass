# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.287 |
| node-hours | 2.516 | 2.215 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 250.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 258.4 | 238.8 |
| response time (ms), 95th percentile | 741.8 | 809.9 |
| response time (ms), 99th percentile | 1274 | 1521 |
| time over the response line (% of samples) | 10.16 | 11.34 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.97 | 15.7 |
| utilisation (used / allocatable) | 0.06079 | 0.06967 |
| CPU used (cores), mean | 1.459 | 1.47 |
| Omni's own CPU (cores), mean | 0 | 0.01802 |
| CPU used with Omni's own (cores), mean | 1.459 | 1.488 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457 | 411.4 |
| HPA replicas, mean | 1.987 | 2.312 |
| pods started | 0.1 | 0.7 |
| pod start wait, total (s) | 0.2 | 2.3 |
| pod start wait, mean (s) | 0.2 | 1.55 |
| host CPU busy, the real machine under kind (%) | 42.56 | 43.62 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 791.8 | 797.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.673 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7042 | 0.7417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 105.5 | 110.4 |
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
| worker nodes in service, mean | 6 | 5.287 | -11.9% | -1.227 to -0.1989 | yes: GAIN |
| node-hours | 2.516 | 2.215 | -12.0% | -0.5189 to -0.08335 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.9 | +0.0% | -0.8831 to +0.9264 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 250.4 | -8.2% | -38.58 to -6.196 | yes: GAIN |
| response time (ms), mean | 258.4 | 238.8 | -7.6% | -41.35 to +1.983 | no |
| response time (ms), 95th percentile | 741.8 | 809.9 | +9.2% | -103 to +239.2 | no |
| response time (ms), 99th percentile | 1274 | 1521 | +19.4% | -66.43 to +559.9 | no |
| time over the response line (% of samples) | 10.16 | 11.34 | +11.7% | +0.006474 to +2.361 | yes: LOSS |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.3 | +3.3% | -0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 | +32.2 (native is 0) | +25.1 to +39.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.97 | 15.71 | +4.9% | -1.367 to +2.834 | no |
| utilisation (used / allocatable) | 0.06079 | 0.06967 | +14.6% | +0.002609 to +0.01515 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.459 | 1.47 | +0.7% | -0.01011 to +0.03182 | no |
| Omni's own CPU (cores), mean | 0 | 0.01802 | +0.018 (native is 0) | +0.01691 to +0.01913 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.459 | 1.488 | +2.0% | +0.008306 to +0.04944 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457 | 411.4 | -10.0% | -83.44 to -7.772 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.987 | 2.312 | +16.4% | +0.124 to +0.5265 | yes: power given |
| pods started | 0.1 | 0.7 | +600.0% | +0.09985 to +1.1 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.3 | +1050.0% | +0.1498 to +4.05 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.55 | +675.0% | +0.231 to +2.469 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.56 | 43.62 | +2.5% | +0.5902 to +1.543 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 791.8 | 797.8 | +0.8% | +1.021 to +10.98 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.673 | -22.1% | -2.246 to -0.4078 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7042 | 0.7417 | +5.3% | -0.05296 to +0.128 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.2 | -7.7% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.5 | 110.4 | +4.6% | -1.005 to +10.65 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*