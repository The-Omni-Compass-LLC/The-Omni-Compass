# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.864 |
| node-hours | 2.518 | 2.043 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 235.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 174.5 | 137.2 |
| response time (ms), 95th percentile | 417.2 | 455 |
| response time (ms), 99th percentile | 553.2 | 584.8 |
| time over the response line (% of samples) | 3.574 | 4.049 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.5 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.752 | 7.298 |
| utilisation (used / allocatable) | 0.05621 | 0.06988 |
| CPU used (cores), mean | 1.349 | 1.331 |
| Omni's own CPU (cores), mean | 0 | 0.01929 |
| CPU used with Omni's own (cores), mean | 1.349 | 1.35 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.7 | 421.6 |
| HPA replicas, mean | 2.119 | 2.236 |
| pods started | 0.2 | 0.2 |
| pod start wait, total (s) | 0.5 | 0.4 |
| pod start wait, mean (s) | 0.5 | 0.4 |
| host CPU busy, the real machine under kind (%) | 38.56 | 39.55 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 720.3 | 720.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.186 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.03333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 |
| queue: job turnaround, submitted to done, mean (s) | 25.72 | 25.95 |
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
| worker nodes in service, mean | 6 | 4.864 | -18.9% | -1.898 to -0.3735 | yes: GAIN |
| node-hours | 2.518 | 2.043 | -18.9% | -0.7972 to -0.1529 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.4 | +0.1% | -1.097 to +1.445 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 235.7 | -13.1% | -60.16 to -10.95 | yes: GAIN |
| response time (ms), mean | 174.5 | 137.2 | -21.4% | -44.85 to -29.82 | yes: GAIN |
| response time (ms), 95th percentile | 417.2 | 455 | +9.1% | +16.46 to +59.24 | yes: LOSS |
| response time (ms), 99th percentile | 553.2 | 584.8 | +5.7% | +5.517 to +57.52 | yes: LOSS |
| time over the response line (% of samples) | 3.574 | 4.049 | +13.3% | -0.05318 to +1.005 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.5 | 5.8 | +28.9% | -0.1717 to +2.772 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 60.2 | +60.2 (native is 0) | +42.77 to +77.63 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.752 | 7.298 | +8.1% | -2.206 to +3.3 | no |
| utilisation (used / allocatable) | 0.05621 | 0.06988 | +24.3% | +0.004777 to +0.02257 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.349 | 1.331 | -1.4% | -0.1063 to +0.06972 | no |
| Omni's own CPU (cores), mean | 0 | 0.01929 | +0.0193 (native is 0) | +0.01724 to +0.02134 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.349 | 1.35 | +0.1% | -0.08713 to +0.08917 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.7 | 421.6 | -13.5% | -111.7 to -20.44 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.119 | 2.236 | +5.5% | -0.06272 to +0.2973 | no |
| pods started | 0.2 | 0.2 | +0.0% | -0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.5 | 0.4 | -20.0% | -1.19 to +0.99 | no |
| pod start wait, mean (s) | 0.5 | 0.4 | -20.0% | -1.19 to +0.99 | no |
| host CPU busy, the real machine under kind (%) | 38.56 | 39.55 | +2.5% | +0.7737 to +1.19 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 720.3 | 720.4 | +0.0% | -0.306 to +0.506 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.186 | -30.2% | -3.036 to -0.5919 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.03333 | +60.0% | -0.01204 to +0.03704 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | +0.0% | -0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 25.72 | 25.95 | +0.9% | +0.03225 to +0.4177 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*