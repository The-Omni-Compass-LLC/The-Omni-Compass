# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 12 | 6.816 |
| node-hours | 5.01 | 2.853 |
| energy, parked workers still on at idle power (Wh, declared model) | 503.2 | 504.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.2 | 342 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 145 | 80.61 |
| response time (ms), 95th percentile | 196.9 | 104.3 |
| response time (ms), 99th percentile | 232 | 151.1 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0 |
| utilisation (used / allocatable) | 0.006565 | 0.009613 |
| CPU used (cores), mean | 0.3151 | 0.2621 |
| Omni's own CPU (cores), mean | 0 | 0.01 |
| CPU used with Omni's own (cores), mean | 0.3151 | 0.2721 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3824 | 3117 |
| HPA replicas, mean | 4.392 | 3.975 |
| pods started | 1 | 0 |
| pod start wait, total (s) | 1 | 0 |
| pod start wait, mean (s) | 1 | 0 |
| host CPU busy, the real machine under kind (%) | 15.29 | 16.08 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1502 | 1501 |
| batch: worker machines in service after the queue finished, mean | nan | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 1154 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 1471 |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 1154 |
| queue: jobs unfinished at the window's end | 24 | 24 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.816 | -43.2% | +nan to +nan | no |
| node-hours | 5.01 | 2.853 | -43.0% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 503.2 | 504.8 | +0.3% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 503.2 | 342 | -32.0% | +nan to +nan | no |
| response time (ms), mean | 145 | 80.61 | -44.4% | +nan to +nan | no |
| response time (ms), 95th percentile | 196.9 | 104.3 | -47.0% | +nan to +nan | no |
| response time (ms), 99th percentile | 232 | 151.1 | -34.9% | +nan to +nan | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23 | +23 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| utilisation (used / allocatable) | 0.006565 | 0.009613 | +46.4% | +nan to +nan | no |
| CPU used (cores), mean | 0.3151 | 0.2621 | -16.8% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.01 | +0.01 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 0.3151 | 0.2721 | -13.7% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 3824 | 3117 | -18.5% | +nan to +nan | no |
| HPA replicas, mean | 4.392 | 3.975 | -9.5% | +nan to +nan | no |
| pods started | 1 | 0 | -100.0% | +nan to +nan | no |
| pod start wait, total (s) | 1 | 0 | -100.0% | +nan to +nan | no |
| pod start wait, mean (s) | 1 | 0 | -100.0% | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 15.29 | 16.08 | +5.2% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |
| batch: queue finished (s) | 1502 | 1501 | -0.1% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1156 | 1154 | -0.1% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1472 | 1471 | -0.1% | +nan to +nan | no |
| queue: job turnaround, submitted to done, mean (s) | 1156 | 1154 | -0.1% | +nan to +nan | no |
| queue: jobs unfinished at the window's end | 24 | 24 | +0.0% | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*