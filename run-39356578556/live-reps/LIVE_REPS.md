# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.545 |
| node-hours | 2.518 | 1.906 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 225.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 151.3 | 114.2 |
| response time (ms), 95th percentile | 334.1 | 331.6 |
| response time (ms), 99th percentile | 427.2 | 439.5 |
| time over the response line (% of samples) | 0.7443 | 1.042 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 2.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 71.43 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.637 | 6.633 |
| utilisation (used / allocatable) | 0.05771 | 0.07455 |
| CPU used (cores), mean | 1.385 | 1.346 |
| Omni's own CPU (cores), mean | 0 | 0.01894 |
| CPU used with Omni's own (cores), mean | 1.385 | 1.365 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.2 | 403.3 |
| HPA replicas, mean | 2.19 | 2.214 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.1 | 0.6 |
| pod start wait, mean (s) | 0.1 | 0.5 |
| host CPU busy, the real machine under kind (%) | 38.85 | 39.91 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 721.2 | 721.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.51 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.02083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 |
| queue: job turnaround, submitted to done, mean (s) | 26.6 | 26.97 |
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
| worker nodes in service, mean | 6 | 4.545 | -24.2% | -2.192 to -0.7173 | yes: GAIN |
| node-hours | 2.518 | 1.906 | -24.3% | -0.9203 to -0.3035 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.5 | -0.2% | -1.771 to +0.4604 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 225.8 | -17.0% | -69.93 to -22.81 | yes: GAIN |
| response time (ms), mean | 151.3 | 114.2 | -24.6% | -48.27 to -26.04 | yes: GAIN |
| response time (ms), 95th percentile | 334.1 | 331.6 | -0.7% | -29.97 to +25.03 | no |
| response time (ms), 99th percentile | 427.2 | 439.5 | +2.9% | -5.236 to +29.78 | no |
| time over the response line (% of samples) | 0.7443 | 1.042 | +40.0% | -0.0697 to +0.6649 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.2 | 2.1 | +75.0% | -0.1366 to +1.937 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.5 | +40.5 (native is 0) | +26.94 to +54.06 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.637 | 6.633 | -13.1% | -3.761 to +1.755 | no |
| utilisation (used / allocatable) | 0.05771 | 0.07455 | +29.2% | +0.007823 to +0.02587 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.385 | 1.346 | -2.8% | -0.09165 to +0.01318 | no |
| Omni's own CPU (cores), mean | 0 | 0.01894 | +0.0189 (native is 0) | +0.01587 to +0.02201 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.385 | 1.365 | -1.5% | -0.07324 to +0.03264 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479.2 | 403.3 | -15.8% | -120 to -31.82 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.19 | 2.214 | +1.1% | -0.1917 to +0.2388 | no |
| pods started | 0.1 | 0.4 | +300.0% | -0.2889 to +0.8889 | no |
| pod start wait, total (s) | 0.1 | 0.6 | +500.0% | -0.2726 to +1.273 | no |
| pod start wait, mean (s) | 0.1 | 0.5 | +400.0% | -0.2911 to +1.091 | no |
| host CPU busy, the real machine under kind (%) | 38.85 | 39.91 | +2.7% | +0.8605 to +1.274 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 721.2 | 721.7 | +0.1% | +0.123 to +0.877 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.51 | -41.5% | -3.699 to -1.282 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.02083 | -28.6% | -0.03912 to +0.02245 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 26.6 | 26.97 | +1.4% | +0.2174 to +0.5159 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*