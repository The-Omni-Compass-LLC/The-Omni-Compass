# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.729 |
| node-hours | 2.513 | 2.401 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 266.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 515 | 488.1 |
| response time (ms), 95th percentile | 1915 | 2023 |
| response time (ms), 99th percentile | 2729 | 2900 |
| time over the response line (% of samples) | 27.86 | 27.78 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 13.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.52 | 16.3 |
| utilisation (used / allocatable) | 0.06794 | 0.07121 |
| CPU used (cores), mean | 1.631 | 1.632 |
| Omni's own CPU (cores), mean | 0 | 0.01613 |
| CPU used with Omni's own (cores), mean | 1.631 | 1.648 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.3 | 392.6 |
| HPA replicas, mean | 1.933 | 2.343 |
| pods started | 0.2 | 0.5 |
| pod start wait, total (s) | 0.4 | 0.9 |
| pod start wait, mean (s) | 0.4 | 0.9 |
| host CPU busy, the real machine under kind (%) | 46.38 | 47.28 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 836.6 | 843.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.515 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.1875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 142.3 | 150.1 |
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
| worker nodes in service, mean | 6 | 5.729 | -4.5% | -0.6929 to +0.1517 | no |
| node-hours | 2.513 | 2.401 | -4.4% | -0.2903 to +0.06734 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.4 | +0.1% | -0.7765 to +1.305 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 266.9 | -3.0% | -21.96 to +5.44 | no |
| response time (ms), mean | 515 | 488.1 | -5.2% | -51.68 to -2.222 | yes: GAIN |
| response time (ms), 95th percentile | 1915 | 2023 | +5.6% | +3.853 to +212.1 | yes: LOSS |
| response time (ms), 99th percentile | 2729 | 2900 | +6.2% | -3.681 to +344.4 | no |
| time over the response line (% of samples) | 27.86 | 27.78 | -0.3% | -0.8272 to +0.6615 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 13.3 | +3.1% | +0.03062 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25 | +25 (native is 0) | +9.909 to +40.09 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.52 | 16.3 | -1.3% | -3.521 to +3.098 | no |
| utilisation (used / allocatable) | 0.06794 | 0.07121 | +4.8% | -0.00101 to +0.007558 | no |
| CPU used (cores), mean | 1.631 | 1.632 | +0.1% | -0.02105 to +0.02458 | no |
| Omni's own CPU (cores), mean | 0 | 0.01613 | +0.0161 (native is 0) | +0.01476 to +0.0175 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.631 | 1.648 | +1.1% | -0.004035 to +0.03983 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.3 | 392.6 | -3.6% | -34.9 to +5.583 | no |
| HPA replicas, mean | 1.933 | 2.343 | +21.2% | +0.3092 to +0.51 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | -0.6802 to +1.68 | no |
| pod start wait, mean (s) | 0.4 | 0.9 | +125.0% | -0.6802 to +1.68 | no |
| host CPU busy, the real machine under kind (%) | 46.38 | 47.28 | +1.9% | +0.7018 to +1.091 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 836.6 | 843.4 | +0.8% | +0.342 to +13.26 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.515 | -8.1% | -1.189 to +0.2188 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.1875 | +2.3% | -0.1331 to +0.1414 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.9 | -40.0% | -1.505 to +0.3048 | no |
| queue: job turnaround, submitted to done, mean (s) | 142.3 | 150.1 | +5.5% | -0.4592 to +16.05 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*