# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.737 |
| node-hours | 2.511 | 1.987 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 231.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 298.8 | 268.2 |
| response time (ms), 95th percentile | 1235 | 1251 |
| response time (ms), 99th percentile | 1844 | 1867 |
| time over the response line (% of samples) | 9.991 | 9.9 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.668 | 9.973 |
| utilisation (used / allocatable) | 0.0564 | 0.07021 |
| CPU used (cores), mean | 1.354 | 1.33 |
| Omni's own CPU (cores), mean | 0 | 0.01703 |
| CPU used with Omni's own (cores), mean | 1.354 | 1.347 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.7 | 424.3 |
| HPA replicas, mean | 1.998 | 2.112 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.6 |
| pod start wait, mean (s) | 0 | 0.6 |
| host CPU busy, the real machine under kind (%) | 38.36 | 39.29 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 785 | 788.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.916 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 91.8 | 95.28 |
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
| worker nodes in service, mean | 6 | 4.737 | -21.1% | -2.086 to -0.4409 | yes: GAIN |
| node-hours | 2.511 | 1.987 | -20.9% | -0.8692 to -0.178 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.1 | +0.1% | -0.3565 to +0.8733 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 231.4 | -14.5% | -65.54 to -13.26 | yes: GAIN |
| response time (ms), mean | 298.8 | 268.2 | -10.2% | -57.7 to -3.476 | yes: GAIN |
| response time (ms), 95th percentile | 1235 | 1251 | +1.3% | -115.7 to +149 | no |
| response time (ms), 99th percentile | 1844 | 1867 | +1.2% | -66.25 to +112.1 | no |
| time over the response line (% of samples) | 9.991 | 9.9 | -0.9% | -1.501 to +1.319 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6.1 | +1.7% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.9 | +42.9 (native is 0) | +26.95 to +58.85 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.668 | 9.973 | +3.2% | -2.196 to +2.806 | no |
| utilisation (used / allocatable) | 0.0564 | 0.07021 | +24.5% | +0.004238 to +0.02339 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.354 | 1.33 | -1.7% | -0.03798 to -0.008471 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01703 | +0.017 (native is 0) | +0.01524 to +0.01882 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.354 | 1.347 | -0.5% | -0.02112 to +0.008726 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.7 | 424.3 | -15.8% | -135.9 to -22.95 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.112 | +5.7% | -0.1743 to +0.4034 | no |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.6 (native is 0) | -0.0032 to +1.203 | no |
| host CPU busy, the real machine under kind (%) | 38.36 | 39.29 | +2.4% | +0.6423 to +1.216 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 785 | 788.7 | +0.5% | -1.313 to +8.713 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.916 | -34.7% | -3.369 to -0.7994 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05417 | +8.3% | -0.02547 to +0.03381 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | -0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.8 | 95.28 | +3.8% | -0.374 to +7.341 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*