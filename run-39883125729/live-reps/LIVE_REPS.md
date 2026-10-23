# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.468 |
| node-hours | 2.515 | 2.297 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 256 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 306.5 | 288 |
| response time (ms), 95th percentile | 982.8 | 1090 |
| response time (ms), 99th percentile | 1425 | 1639 |
| time over the response line (% of samples) | 17.69 | 17.41 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 120.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 10.82 |
| utilisation (used / allocatable) | 0.0589 | 0.06517 |
| CPU used (cores), mean | 1.414 | 1.422 |
| Omni's own CPU (cores), mean | 0 | 0.04851 |
| CPU used with Omni's own (cores), mean | 1.414 | 1.47 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.4 | 431.1 |
| HPA replicas, mean | 1.969 | 2.77 |
| pods started | 0.1 | 1.8 |
| pod start wait, total (s) | 0.2 | 4.2 |
| pod start wait, mean (s) | 0.2 | 1.692 |
| host CPU busy, the real machine under kind (%) | 40.08 | 42.31 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 758.3 | 767.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.974 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 67.15 | 74.85 |
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
| worker nodes in service, mean | 6 | 5.468 | -8.9% | -1.101 to +0.03794 | no |
| node-hours | 2.515 | 2.297 | -8.7% | -0.4576 to +0.02052 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.8 | +0.2% | -0.2217 to +1.547 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 256 | -5.9% | -33.92 to +1.694 | no |
| response time (ms), mean | 306.5 | 288 | -6.0% | -39.95 to +2.92 | no |
| response time (ms), 95th percentile | 982.8 | 1090 | +10.9% | -12.91 to +227.4 | no |
| response time (ms), 99th percentile | 1425 | 1639 | +15.1% | -37.33 to +466.8 | no |
| time over the response line (% of samples) | 17.69 | 17.41 | -1.6% | -2.207 to +1.63 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10 | +7.5% | -0.1953 to +1.595 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 120.2 | +120 (native is 0) | +70.9 to +169.5 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.752 | 10.82 | +11.0% | -0.8799 to +3.02 | no |
| utilisation (used / allocatable) | 0.0589 | 0.06517 | +10.6% | -0.0002869 to +0.01282 | no |
| CPU used (cores), mean | 1.414 | 1.422 | +0.6% | -0.02834 to +0.04439 | no |
| Omni's own CPU (cores), mean | 0 | 0.04851 | +0.0485 (native is 0) | +0.04236 to +0.05466 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.47 | +4.0% | +0.01798 to +0.0951 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466.4 | 431.1 | -7.6% | -73.83 to +3.16 | no |
| HPA replicas, mean | 1.969 | 2.77 | +40.7% | +0.4719 to +1.132 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +0.3919 to +3.008 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.2 | +2000.0% | +0.2603 to +7.74 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.692 | +745.8% | +0.2914 to +2.692 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.08 | 42.31 | +5.5% | +1.502 to +2.946 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 758.3 | 767.8 | +1.3% | +0.9811 to +18.02 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.974 | -17.1% | -2.118 to +0.06606 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04583 | +0.0% | -0.03442 to +0.03442 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.15 | 74.85 | +11.5% | -1.044 to +16.45 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*