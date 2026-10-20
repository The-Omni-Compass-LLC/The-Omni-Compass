# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.395 |
| node-hours | 2.512 | 2.263 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 273.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 254.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 292.4 | 263 |
| response time (ms), 95th percentile | 927.8 | 1052 |
| response time (ms), 99th percentile | 1606 | 1751 |
| time over the response line (% of samples) | 12.3 | 12.13 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.19 | 17.75 |
| utilisation (used / allocatable) | 0.06075 | 0.0678 |
| CPU used (cores), mean | 1.458 | 1.471 |
| Omni's own CPU (cores), mean | 0 | 0.01712 |
| CPU used with Omni's own (cores), mean | 1.458 | 1.488 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.2 | 419.3 |
| HPA replicas, mean | 1.996 | 2.1 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.5 |
| host CPU busy, the real machine under kind (%) | 42.61 | 43.62 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 804.4 | 809.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.882 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7333 | 0.825 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 119 | 124.1 |
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
| worker nodes in service, mean | 6 | 5.395 | -10.1% | -1.252 to +0.04134 | no |
| node-hours | 2.512 | 2.263 | -9.9% | -0.5242 to +0.02689 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 273.1 | +0.3% | -0.1276 to +1.849 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 254.1 | -6.7% | -39.02 to +2.771 | no |
| response time (ms), mean | 292.4 | 263 | -10.1% | -45.89 to -12.93 | yes: GAIN |
| response time (ms), 95th percentile | 927.8 | 1052 | +13.4% | -2.229 to +250.9 | no |
| response time (ms), 99th percentile | 1606 | 1751 | +9.0% | -51.76 to +342.2 | no |
| time over the response line (% of samples) | 12.3 | 12.13 | -1.4% | -1.855 to +1.508 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 9.8 | +4.3% | -0.2911 to +1.091 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.9 | +33.9 (native is 0) | +21.07 to +46.73 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.19 | 17.75 | +3.2% | -2.425 to +3.535 | no |
| utilisation (used / allocatable) | 0.06075 | 0.0678 | +11.6% | +0.0006416 to +0.01346 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.458 | 1.471 | +0.9% | -0.009723 to +0.0362 | no |
| Omni's own CPU (cores), mean | 0 | 0.01712 | +0.0171 (native is 0) | +0.01598 to +0.01826 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.458 | 1.488 | +2.1% | +0.007778 to +0.05294 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.2 | 419.3 | -9.7% | -90.38 to +0.5427 | no |
| HPA replicas, mean | 1.996 | 2.1 | +5.2% | +0.03489 to +0.1732 | yes: power given |
| pods started | 0 | 0.3 | +0.3 (native is 0) | -0.04553 to +0.6455 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.5 (native is 0) | -0.1079 to +1.108 | no |
| host CPU busy, the real machine under kind (%) | 42.61 | 43.62 | +2.4% | +0.7802 to +1.229 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 804.4 | 809.9 | +0.7% | +1.726 to +9.274 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.882 | -18.6% | -2.284 to +0.04676 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7333 | 0.825 | +12.5% | -0.04799 to +0.2313 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.7 | +21.4% | -0.04553 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 119 | 124.1 | +4.3% | +1.195 to +8.947 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*