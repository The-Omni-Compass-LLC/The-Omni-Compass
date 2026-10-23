# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.29 |
| node-hours | 2.516 | 2.215 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 272.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 250.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 259.2 | 226.5 |
| response time (ms), 95th percentile | 697.2 | 730.3 |
| response time (ms), 99th percentile | 1211 | 1285 |
| time over the response line (% of samples) | 10.96 | 10.66 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.06 | 17.61 |
| utilisation (used / allocatable) | 0.06206 | 0.06977 |
| CPU used (cores), mean | 1.489 | 1.463 |
| Omni's own CPU (cores), mean | 0 | 0.01819 |
| CPU used with Omni's own (cores), mean | 1.489 | 1.481 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.9 | 410.2 |
| HPA replicas, mean | 2.027 | 2.448 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 1.5 |
| pod start wait, mean (s) | 0 | 1.5 |
| host CPU busy, the real machine under kind (%) | 42.73 | 43.59 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 788.6 | 793.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.736 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7125 | 0.7417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 104.7 | 108.3 |
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
| worker nodes in service, mean | 6 | 5.29 | -11.8% | -1.412 to -0.00811 | yes: GAIN |
| node-hours | 2.516 | 2.215 | -12.0% | -0.5915 to -0.01033 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 272.7 | -0.2% | -1.638 to +0.396 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 250.3 | -8.4% | -44.92 to -1.033 | yes: GAIN |
| response time (ms), mean | 259.2 | 226.5 | -12.6% | -52.95 to -12.55 | yes: GAIN |
| response time (ms), 95th percentile | 697.2 | 730.3 | +4.7% | -73.55 to +139.6 | no |
| response time (ms), 99th percentile | 1211 | 1285 | +6.1% | -126.3 to +275 | no |
| time over the response line (% of samples) | 10.96 | 10.66 | -2.7% | -2.632 to +2.04 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.2 | -1.0% | -0.506 to +0.306 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.4 | +40.4 (native is 0) | +32.49 to +48.31 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.06 | 17.61 | +16.9% | +0.1403 to +4.96 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06206 | 0.06977 | +12.4% | -3.35e-05 to +0.01546 | no |
| CPU used (cores), mean | 1.489 | 1.463 | -1.8% | -0.06205 to +0.009639 | no |
| Omni's own CPU (cores), mean | 0 | 0.01819 | +0.0182 (native is 0) | +0.01547 to +0.02091 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.489 | 1.481 | -0.5% | -0.04596 to +0.02994 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443.9 | 410.2 | -7.6% | -69.93 to +2.434 | no |
| HPA replicas, mean | 2.027 | 2.448 | +20.8% | +0.2711 to +0.5716 | yes: power given |
| pods started | 0 | 0.4 | +0.4 (native is 0) | +0.03062 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 1.5 | +1.5 (native is 0) | -0.05441 to +3.054 | no |
| pod start wait, mean (s) | 0 | 1.5 | +1.5 (native is 0) | -0.05441 to +3.054 | no |
| host CPU busy, the real machine under kind (%) | 42.73 | 43.59 | +2.0% | +0.2459 to +1.491 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 788.6 | 793.8 | +0.7% | -1.354 to +11.75 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.736 | -21.1% | -2.388 to -0.1392 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7125 | 0.7417 | +4.1% | -0.05975 to +0.1181 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.5 | +7.1% | -0.5263 to +0.7263 | no |
| queue: job turnaround, submitted to done, mean (s) | 104.7 | 108.3 | +3.4% | -4.661 to +11.84 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*