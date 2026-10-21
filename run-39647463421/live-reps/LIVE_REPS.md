# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.309 |
| node-hours | 2.517 | 2.224 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 251.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 445.2 | 424.7 |
| response time (ms), 95th percentile | 1936 | 2001 |
| response time (ms), 99th percentile | 2762 | 2778 |
| time over the response line (% of samples) | 15.86 | 16.07 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 28.96 | 31.62 |
| utilisation (used / allocatable) | 0.06123 | 0.0695 |
| CPU used (cores), mean | 1.469 | 1.47 |
| Omni's own CPU (cores), mean | 0 | 0.01704 |
| CPU used with Omni's own (cores), mean | 1.469 | 1.487 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.2 | 415 |
| HPA replicas, mean | 1.985 | 2.16 |
| pods started | 0.2 | 0.9 |
| pod start wait, total (s) | 0.3 | 1.4 |
| pod start wait, mean (s) | 0.3 | 0.7833 |
| host CPU busy, the real machine under kind (%) | 44.76 | 45.81 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 842.5 | 846.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.811 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.279 | 1.092 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4 | 2.9 |
| queue: job turnaround, submitted to done, mean (s) | 141.2 | 147.4 |
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
| worker nodes in service, mean | 6 | 5.309 | -11.5% | -1.453 to +0.07157 | no |
| node-hours | 2.517 | 2.224 | -11.6% | -0.6144 to +0.02953 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.9 | -0.1% | -1.306 to +0.89 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 251.2 | -8.0% | -46.21 to +2.38 | no |
| response time (ms), mean | 445.2 | 424.7 | -4.6% | -39.58 to -1.341 | yes: GAIN |
| response time (ms), 95th percentile | 1936 | 2001 | +3.4% | -77.39 to +208.4 | no |
| response time (ms), 99th percentile | 2762 | 2778 | +0.6% | -275.8 to +306.7 | no |
| time over the response line (% of samples) | 15.86 | 16.07 | +1.3% | -0.2527 to +0.672 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.5 | +1.9% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.8 | +23.8 (native is 0) | +16.44 to +31.16 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 28.96 | 31.62 | +9.2% | -3.825 to +9.139 | no |
| utilisation (used / allocatable) | 0.06123 | 0.0695 | +13.5% | -0.0004409 to +0.01698 | no |
| CPU used (cores), mean | 1.469 | 1.47 | +0.0% | -0.04602 to +0.04748 | no |
| Omni's own CPU (cores), mean | 0 | 0.01704 | +0.017 (native is 0) | +0.01429 to +0.01979 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.469 | 1.487 | +1.2% | -0.02832 to +0.06386 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.2 | 415 | -9.8% | -96.27 to +5.839 | no |
| HPA replicas, mean | 1.985 | 2.16 | +8.8% | -0.01182 to +0.3626 | no |
| pods started | 0.2 | 0.9 | +350.0% | -0.05776 to +1.458 | no |
| pod start wait, total (s) | 0.3 | 1.4 | +366.7% | -0.04101 to +2.241 | no |
| pod start wait, mean (s) | 0.3 | 0.7833 | +161.1% | -0.2841 to +1.251 | no |
| host CPU busy, the real machine under kind (%) | 44.76 | 45.81 | +2.4% | +0.3464 to +1.761 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 842.5 | 846.8 | +0.5% | -5.467 to +14.07 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.811 | -19.8% | -2.484 to +0.1053 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.279 | 1.092 | -14.7% | -0.4111 to +0.03609 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4 | 2.9 | -27.5% | -2.867 to +0.6667 | no |
| queue: job turnaround, submitted to done, mean (s) | 141.2 | 147.4 | +4.3% | -2.737 to +15.01 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*