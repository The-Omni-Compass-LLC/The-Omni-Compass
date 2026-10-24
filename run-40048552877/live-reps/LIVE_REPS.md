# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.753 |
| node-hours | 2.517 | 1.993 |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 269.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 230.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 216.4 | 167.1 |
| response time (ms), 95th percentile | 728 | 631.4 |
| response time (ms), 99th percentile | 1095 | 1055 |
| time over the response line (% of samples) | 6.486 | 5.604 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.34 | 12.48 |
| utilisation (used / allocatable) | 0.05235 | 0.0667 |
| CPU used (cores), mean | 1.256 | 1.231 |
| Omni's own CPU (cores), mean | 0 | 0.01657 |
| CPU used with Omni's own (cores), mean | 1.256 | 1.248 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.8 | 446.4 |
| HPA replicas, mean | 1.966 | 2.261 |
| pods started | 0.2 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.9 |
| host CPU busy, the real machine under kind (%) | 37.63 | 38.1 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 747.6 | 747.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.072 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6875 | 0.6792 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.2 |
| queue: job turnaround, submitted to done, mean (s) | 55.89 | 55.65 |
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
| worker nodes in service, mean | 6 | 4.753 | -20.8% | -2.131 to -0.3623 | yes: GAIN |
| node-hours | 2.517 | 1.993 | -20.8% | -0.8942 to -0.1542 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270 | 269.6 | -0.1% | -1.376 to +0.7356 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270 | 230.4 | -14.7% | -67.43 to -11.71 | yes: GAIN |
| response time (ms), mean | 216.4 | 167.1 | -22.8% | -81.95 to -16.65 | yes: GAIN |
| response time (ms), 95th percentile | 728 | 631.4 | -13.3% | -274 to +80.72 | no |
| response time (ms), 99th percentile | 1095 | 1055 | -3.6% | -185.3 to +105.7 | no |
| time over the response line (% of samples) | 6.486 | 5.604 | -13.6% | -2.502 to +0.737 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 4.7 | +2.2% | -0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.8 | +46.8 (native is 0) | +32.03 to +61.57 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.34 | 12.48 | +1.1% | -1.513 to +1.79 | no |
| utilisation (used / allocatable) | 0.05235 | 0.0667 | +27.4% | +0.00336 to +0.02533 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.256 | 1.231 | -2.0% | -0.06806 to +0.01737 | no |
| Omni's own CPU (cores), mean | 0 | 0.01657 | +0.0166 (native is 0) | +0.01427 to +0.01887 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.256 | 1.248 | -0.7% | -0.05191 to +0.03436 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 521.8 | 446.4 | -14.4% | -135.3 to -15.46 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.966 | 2.261 | +15.0% | +0.03525 to +0.5548 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | -0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | -0.1294 to +1.529 | no |
| pod start wait, mean (s) | 0.2 | 0.9 | +350.0% | -0.1294 to +1.529 | no |
| host CPU busy, the real machine under kind (%) | 37.63 | 38.1 | +1.3% | -0.2567 to +1.203 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 747.6 | 747.3 | -0.0% | -4.899 to +4.299 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.072 | -32.1% | -3.256 to -0.6014 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6875 | 0.6792 | -1.2% | -0.1249 to +0.1082 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1.2 | -7.7% | -0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 55.89 | 55.65 | -0.4% | -4.436 to +3.961 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*