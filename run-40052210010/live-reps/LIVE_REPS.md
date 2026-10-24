# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.951 |
| node-hours | 2.516 | 2.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 269.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 126.5 | 94.87 |
| response time (ms), 95th percentile | 214.6 | 202.6 |
| response time (ms), 99th percentile | 301.8 | 312.3 |
| time over the response line (% of samples) | 0.1383 | 0.2175 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 989.8 | 1000 |
| utilisation (used / allocatable) | 0.05821 | 0.05882 |
| CPU used (cores), mean | 1.397 | 1.401 |
| Omni's own CPU (cores), mean | 0 | 0.01169 |
| CPU used with Omni's own (cores), mean | 1.397 | 1.412 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 460.9 |
| HPA replicas, mean | 2.004 | 2.053 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.2 |
| host CPU busy, the real machine under kind (%) | 43 | 43.53 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1378 | 1389 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.584 |
| queue: job wait, submitted to its first pod running, mean (s) | 125.3 | 125.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 629.4 | 642.6 |
| queue: job turnaround, submitted to done, mean (s) | 742.9 | 745.1 |
| queue: jobs unfinished at the window's end | 8 | 8.6 |

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
| worker nodes in service, mean | 6 | 5.951 | -0.8% | -0.112 to +0.01366 | no |
| node-hours | 2.516 | 2.493 | -0.9% | -0.04831 to +0.00198 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.4 | -0.1% | -1.235 to +0.6637 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 269.9 | -0.7% | -3.514 to -0.158 | yes: GAIN |
| response time (ms), mean | 126.5 | 94.87 | -25.0% | -40.35 to -22.95 | yes: GAIN |
| response time (ms), 95th percentile | 214.6 | 202.6 | -5.6% | -17.65 to -6.329 | yes: GAIN |
| response time (ms), 99th percentile | 301.8 | 312.3 | +3.5% | -9.163 to +30.2 | no |
| time over the response line (% of samples) | 0.1383 | 0.2175 | +57.2% | -0.06766 to +0.226 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.4 | +12.4 (native is 0) | +10.49 to +14.31 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 989.8 | 1000 | +1.1% | -74.45 to +95.28 | no |
| utilisation (used / allocatable) | 0.05821 | 0.05882 | +1.0% | -0.001164 to +0.00238 | no |
| CPU used (cores), mean | 1.397 | 1.401 | +0.3% | -0.03247 to +0.03971 | no |
| Omni's own CPU (cores), mean | 0 | 0.01169 | +0.0117 (native is 0) | +0.01064 to +0.01274 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.397 | 1.412 | +1.1% | -0.02077 to +0.05139 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465.3 | 460.9 | -1.0% | -16.74 to +7.826 | no |
| HPA replicas, mean | 2.004 | 2.053 | +2.4% | -0.0942 to +0.1922 | no |
| pods started | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | +0.0% | -0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 43 | 43.53 | +1.2% | -0.2027 to +1.266 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 1378 | 1389 | +0.8% | -25.85 to +48.25 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.584 | -6.9% | -0.9191 to +0.08669 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 125.3 | 125.2 | -0.1% | -30.25 to +30.12 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 629.4 | 642.6 | +2.1% | -158.7 to +185.1 | no |
| queue: job turnaround, submitted to done, mean (s) | 742.9 | 745.1 | +0.3% | -56.21 to +60.58 | no |
| queue: jobs unfinished at the window's end | 8 | 8.6 | +7.5% | -0.9888 to +2.189 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*