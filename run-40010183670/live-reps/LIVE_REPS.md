# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.307 |
| node-hours | 2.512 | 2.222 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 249.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 294.4 | 259.7 |
| response time (ms), 95th percentile | 924.1 | 966.7 |
| response time (ms), 99th percentile | 1338 | 1444 |
| time over the response line (% of samples) | 14.81 | 15.42 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.942 | 9.892 |
| utilisation (used / allocatable) | 0.05772 | 0.0653 |
| CPU used (cores), mean | 1.385 | 1.376 |
| Omni's own CPU (cores), mean | 0 | 0.01744 |
| CPU used with Omni's own (cores), mean | 1.385 | 1.393 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.5 | 434.7 |
| HPA replicas, mean | 1.994 | 2.309 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 40.28 | 40.99 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 759.4 | 760.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.772 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.1875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 65.99 | 67.69 |
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
| worker nodes in service, mean | 6 | 5.307 | -11.6% | -1.322 to -0.06534 | yes: GAIN |
| node-hours | 2.512 | 2.222 | -11.5% | -0.553 to -0.0263 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.3 | +0.0% | -0.6744 to +0.809 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 249.5 | -8.0% | -41.56 to -1.827 | yes: GAIN |
| response time (ms), mean | 294.4 | 259.7 | -11.8% | -46.46 to -22.96 | yes: GAIN |
| response time (ms), 95th percentile | 924.1 | 966.7 | +4.6% | -11.98 to +97.22 | no |
| response time (ms), 99th percentile | 1338 | 1444 | +8.0% | +7.349 to +205.8 | yes: LOSS |
| time over the response line (% of samples) | 14.81 | 15.42 | +4.1% | -0.5698 to +1.79 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 9.5 | +8.0% | -0.05776 to +1.458 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.7 | +52.7 (native is 0) | +27.49 to +77.91 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.942 | 9.892 | +10.6% | -0.7562 to +2.656 | no |
| utilisation (used / allocatable) | 0.05772 | 0.0653 | +13.1% | +0.0004519 to +0.0147 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.385 | 1.376 | -0.7% | -0.02504 to +0.006542 | no |
| Omni's own CPU (cores), mean | 0 | 0.01744 | +0.0174 (native is 0) | +0.01555 to +0.01933 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.385 | 1.393 | +0.6% | -0.008043 to +0.02443 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.5 | 434.7 | -8.4% | -76.83 to -2.844 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.994 | 2.309 | +15.8% | +0.07051 to +0.5587 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.005799 to +1.006 | no |
| host CPU busy, the real machine under kind (%) | 40.28 | 40.99 | +1.8% | +0.3644 to +1.062 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 759.4 | 760.7 | +0.2% | -1.44 to +4.04 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.772 | -20.5% | -2.269 to -0.1874 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.1875 | +2.3% | -0.06944 to +0.07778 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.9 | +0.0% | +0 to +0 | no |
| queue: job turnaround, submitted to done, mean (s) | 65.99 | 67.69 | +2.6% | +0.004386 to +3.404 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*