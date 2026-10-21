# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.083 |
| node-hours | 2.515 | 2.131 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 242.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 271.9 | 258.1 |
| response time (ms), 95th percentile | 856.6 | 991.2 |
| response time (ms), 99th percentile | 1299 | 1441 |
| time over the response line (% of samples) | 12.98 | 13.77 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.21 | 11.36 |
| utilisation (used / allocatable) | 0.05796 | 0.0681 |
| CPU used (cores), mean | 1.391 | 1.369 |
| Omni's own CPU (cores), mean | 0 | 0.01687 |
| CPU used with Omni's own (cores), mean | 1.391 | 1.385 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.6 | 426.1 |
| HPA replicas, mean | 1.963 | 2.217 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 1.1 |
| pod start wait, mean (s) | 0 | 1.1 |
| host CPU busy, the real machine under kind (%) | 39.49 | 40.61 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 760.2 | 764.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.391 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.08333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 67.41 | 72.24 |
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
| worker nodes in service, mean | 6 | 5.083 | -15.3% | -1.668 to -0.1661 | yes: GAIN |
| node-hours | 2.515 | 2.131 | -15.3% | -0.6995 to -0.06879 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.6 | -0.1% | -1.05 to +0.726 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 242.7 | -10.7% | -53.03 to -5.046 | yes: GAIN |
| response time (ms), mean | 271.9 | 258.1 | -5.1% | -21.76 to -5.831 | yes: GAIN |
| response time (ms), 95th percentile | 856.6 | 991.2 | +15.7% | +57.39 to +211.9 | yes: LOSS |
| response time (ms), 99th percentile | 1299 | 1441 | +11.0% | +49.83 to +235.3 | yes: LOSS |
| time over the response line (% of samples) | 12.98 | 13.77 | +6.1% | -0.2767 to +1.854 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8 | +2.6% | -0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.6 | +47.6 (native is 0) | +26.08 to +69.12 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.21 | 11.36 | +23.3% | +1.091 to +3.205 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05796 | 0.0681 | +17.5% | +0.001671 to +0.0186 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.391 | 1.369 | -1.6% | -0.05399 to +0.009108 | no |
| Omni's own CPU (cores), mean | 0 | 0.01687 | +0.0169 (native is 0) | +0.01546 to +0.01828 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.391 | 1.385 | -0.4% | -0.03721 to +0.02606 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 475.6 | 426.1 | -10.4% | -90.27 to -8.804 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 2.217 | +12.9% | +0.03408 to +0.4731 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.1 (native is 0) | -0.1367 to +2.337 | no |
| pod start wait, mean (s) | 0 | 1.1 | +1.1 (native is 0) | -0.1367 to +2.337 | no |
| host CPU busy, the real machine under kind (%) | 39.49 | 40.61 | +2.8% | +0.8837 to +1.361 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 760.2 | 764.8 | +0.6% | +1.174 to +8.026 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.391 | -26.8% | -2.852 to -0.3653 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.08333 | +11.1% | -0.06964 to +0.08631 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | +0.0% | -0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 67.41 | 72.24 | +7.2% | +1.117 to +8.541 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*