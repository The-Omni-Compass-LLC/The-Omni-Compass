# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.219 |
| node-hours | 2.517 | 2.189 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 247.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 303 | 269.7 |
| response time (ms), 95th percentile | 936.6 | 996.9 |
| response time (ms), 99th percentile | 1368 | 1438 |
| time over the response line (% of samples) | 16.64 | 16.77 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.718 | 9.278 |
| utilisation (used / allocatable) | 0.05867 | 0.06849 |
| CPU used (cores), mean | 1.408 | 1.415 |
| Omni's own CPU (cores), mean | 0 | 0.01583 |
| CPU used with Omni's own (cores), mean | 1.408 | 1.431 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468 | 418 |
| HPA replicas, mean | 1.952 | 2.428 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.6 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 40.19 | 41.06 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 760.7 | 762.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.593 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 69.28 | 71.7 |
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
| worker nodes in service, mean | 6 | 5.219 | -13.0% | -1.454 to -0.1085 | yes: GAIN |
| node-hours | 2.517 | 2.189 | -13.0% | -0.6097 to -0.04589 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.3 | +0.1% | -0.4312 to +0.838 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 247.8 | -9.0% | -45.46 to -3.304 | yes: GAIN |
| response time (ms), mean | 303 | 269.7 | -11.0% | -39.96 to -26.58 | yes: GAIN |
| response time (ms), 95th percentile | 936.6 | 996.9 | +6.4% | +30.54 to +90.04 | yes: LOSS |
| response time (ms), 99th percentile | 1368 | 1438 | +5.1% | +11.94 to +128.4 | yes: LOSS |
| time over the response line (% of samples) | 16.64 | 16.77 | +0.8% | -0.2764 to +0.5522 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 9.4 | +4.4% | -0.2911 to +1.091 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.4 | +36.4 (native is 0) | +22.22 to +50.58 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.718 | 9.278 | -4.5% | -1.696 to +0.8156 | no |
| utilisation (used / allocatable) | 0.05867 | 0.06849 | +16.7% | +0.001418 to +0.01822 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.408 | 1.415 | +0.5% | -0.00629 to +0.02037 | no |
| Omni's own CPU (cores), mean | 0 | 0.01583 | +0.0158 (native is 0) | +0.01454 to +0.01712 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.408 | 1.431 | +1.6% | +0.008447 to +0.0373 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 468 | 418 | -10.7% | -91.26 to -8.769 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.428 | +24.4% | +0.1411 to +0.8113 | yes: power given |
| pods started | 0 | 0.2 | +0.2 (native is 0) | -0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.3656 to +1.566 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.3656 to +1.566 | no |
| host CPU busy, the real machine under kind (%) | 40.19 | 41.06 | +2.2% | +0.6391 to +1.099 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 760.7 | 762.8 | +0.3% | -0.4558 to +4.656 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.593 | -23.4% | -2.552 to -0.2622 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05833 | +40.0% | -0.01832 to +0.05165 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 69.28 | 71.7 | +3.5% | +0.4601 to +4.382 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*