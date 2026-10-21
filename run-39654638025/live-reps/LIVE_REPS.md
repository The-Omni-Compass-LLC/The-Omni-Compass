# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.813 |
| node-hours | 2.515 | 2.018 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 270.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 233.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 217.4 | 182.6 |
| response time (ms), 95th percentile | 721.8 | 699.4 |
| response time (ms), 99th percentile | 1039 | 1018 |
| time over the response line (% of samples) | 5.745 | 5.633 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 5.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 57.14 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.533 | 8.332 |
| utilisation (used / allocatable) | 0.05444 | 0.06897 |
| CPU used (cores), mean | 1.307 | 1.303 |
| Omni's own CPU (cores), mean | 0 | 0.01659 |
| CPU used with Omni's own (cores), mean | 1.307 | 1.32 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.9 | 428.7 |
| HPA replicas, mean | 2.046 | 2.214 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.1 | 0.8 |
| pod start wait, mean (s) | 0.1 | 0.8 |
| host CPU busy, the real machine under kind (%) | 37.76 | 38.56 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 746 | 745.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.979 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.04167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 |
| queue: job turnaround, submitted to done, mean (s) | 52.93 | 53.53 |
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
| worker nodes in service, mean | 6 | 4.813 | -19.8% | -1.913 to -0.4603 | yes: GAIN |
| node-hours | 2.515 | 2.018 | -19.8% | -0.8004 to -0.1941 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 270.6 | -0.0% | -0.7442 to +0.6793 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 233.3 | -13.8% | -60.18 to -14.52 | yes: GAIN |
| response time (ms), mean | 217.4 | 182.6 | -16.0% | -43.45 to -26.16 | yes: GAIN |
| response time (ms), 95th percentile | 721.8 | 699.4 | -3.1% | -52.85 to +8.041 | no |
| response time (ms), 99th percentile | 1039 | 1018 | -2.0% | -77.23 to +36.47 | no |
| time over the response line (% of samples) | 5.745 | 5.633 | -1.9% | -0.4213 to +0.1979 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 5.1 | +4.1% | -1.006 to +1.406 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 49.5 | +49.5 (native is 0) | +36.72 to +62.28 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.533 | 8.332 | -2.4% | -1.837 to +1.433 | no |
| utilisation (used / allocatable) | 0.05444 | 0.06897 | +26.7% | +0.005817 to +0.02324 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.307 | 1.303 | -0.3% | -0.03121 to +0.02454 | no |
| Omni's own CPU (cores), mean | 0 | 0.01659 | +0.0166 (native is 0) | +0.01525 to +0.01793 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.307 | 1.32 | +1.0% | -0.01384 to +0.04036 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 500.9 | 428.7 | -14.4% | -113.3 to -31.14 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.046 | 2.214 | +8.2% | -0.01712 to +0.3517 | no |
| pods started | 0.1 | 0.6 | +500.0% | -0.005799 to +1.006 | no |
| pod start wait, total (s) | 0.1 | 0.8 | +700.0% | +0.0214 to +1.379 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 0.8 | +700.0% | +0.0214 to +1.379 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.76 | 38.56 | +2.1% | +0.5829 to +1.001 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 746 | 745.2 | -0.1% | -4.013 to +2.413 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.979 | -33.7% | -3.246 to -0.7962 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.04167 | +0.0% | -0.03442 to +0.03442 | EVEN, the same (under one part in a million) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 52.93 | 53.53 | +1.1% | -2.073 to +3.282 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*