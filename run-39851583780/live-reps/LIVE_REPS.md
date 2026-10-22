# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.354 |
| node-hours | 2.515 | 2.242 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 251.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 225 | 214.2 |
| response time (ms), 95th percentile | 574.2 | 735.4 |
| response time (ms), 99th percentile | 984.2 | 1354 |
| time over the response line (% of samples) | 9.177 | 9.753 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.37 | 13.93 |
| utilisation (used / allocatable) | 0.05871 | 0.06589 |
| CPU used (cores), mean | 1.409 | 1.408 |
| Omni's own CPU (cores), mean | 0 | 0.052 |
| CPU used with Omni's own (cores), mean | 1.409 | 1.46 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.1 | 431 |
| HPA replicas, mean | 2.061 | 2.611 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.3 | 1.1 |
| pod start wait, mean (s) | 0.3 | 0.5333 |
| host CPU busy, the real machine under kind (%) | 40.7 | 43.34 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 773.7 | 783 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.743 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7042 | 0.7292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 88.03 | 94.62 |
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
| worker nodes in service, mean | 6 | 5.354 | -10.8% | -1.264 to -0.02851 | yes: GAIN |
| node-hours | 2.515 | 2.242 | -10.8% | -0.5311 to -0.01392 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.8 | -0.0% | -0.9708 to +0.8216 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 251.5 | -7.5% | -39.99 to -0.7608 | yes: GAIN |
| response time (ms), mean | 225 | 214.2 | -4.8% | -30.93 to +9.41 | no |
| response time (ms), 95th percentile | 574.2 | 735.4 | +28.1% | -8.364 to +330.9 | no |
| response time (ms), 99th percentile | 984.2 | 1354 | +37.6% | +34.1 to +705.1 | yes: LOSS |
| time over the response line (% of samples) | 9.177 | 9.753 | +6.3% | -0.9471 to +2.1 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.2 | +3.8% | -0.2889 to +0.8889 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.6 | +116 (native is 0) | +72.95 to +158.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.37 | 13.93 | -3.1% | -2.779 to +1.889 | no |
| utilisation (used / allocatable) | 0.05871 | 0.06589 | +12.2% | +0.0008202 to +0.01355 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.409 | 1.408 | -0.0% | -0.03481 to +0.03352 | no |
| Omni's own CPU (cores), mean | 0 | 0.052 | +0.052 (native is 0) | +0.04488 to +0.05912 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.409 | 1.46 | +3.6% | +0.01145 to +0.09125 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469.1 | 431 | -8.1% | -70.99 to -5.313 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.061 | 2.611 | +26.7% | +0.2247 to +0.8753 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | -0.1952 to +1.195 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | -0.845 to +2.445 | no |
| pod start wait, mean (s) | 0.3 | 0.5333 | +77.8% | -0.623 to +1.09 | no |
| host CPU busy, the real machine under kind (%) | 40.7 | 43.34 | +6.5% | +2.098 to +3.188 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 773.7 | 783 | +1.2% | +3.064 to +15.54 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.743 | -20.9% | -2.439 to -0.07529 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7042 | 0.7292 | +3.6% | -0.03155 to +0.08155 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 1.5 | -6.3% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 88.03 | 94.62 | +7.5% | +2.561 to +10.62 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*