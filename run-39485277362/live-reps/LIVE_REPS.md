# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 3.753 |
| node-hours | 2.512 | 1.57 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 267.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 197.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 113.9 | 108.8 |
| response time (ms), 95th percentile | 281.8 | 284.8 |
| response time (ms), 99th percentile | 516.7 | 484.8 |
| time over the response line (% of samples) | 1.185 | 0.738 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.717 | 8.3 |
| utilisation (used / allocatable) | 0.05395 | 0.07733 |
| CPU used (cores), mean | 1.295 | 1.161 |
| Omni's own CPU (cores), mean | 0 | 0.0115 |
| CPU used with Omni's own (cores), mean | 1.295 | 1.172 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.2 | 406.4 |
| HPA replicas, mean | 1.927 | 2.135 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 37.21 | 37.11 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 729 | 729 |
| batch: worker machines in service after the queue finished, mean | 6 | 2 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.04167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0 |
| queue: job turnaround, submitted to done, mean (s) | 32.17 | 31.21 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 3.753 | -37.5% | +nan to +nan | no |
| node-hours | 2.512 | 1.57 | -37.5% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.5 | 267.9 | -0.6% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.5 | 197.4 | -26.8% | +nan to +nan | no |
| response time (ms), mean | 113.9 | 108.8 | -4.5% | +nan to +nan | no |
| response time (ms), 95th percentile | 281.8 | 284.8 | +1.1% | +nan to +nan | no |
| response time (ms), 99th percentile | 516.7 | 484.8 | -6.2% | +nan to +nan | no |
| time over the response line (% of samples) | 1.185 | 0.738 | -37.7% | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 1 | -50.0% | +nan to +nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8 | +8 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.717 | 8.3 | +205.5% | +nan to +nan | no |
| utilisation (used / allocatable) | 0.05395 | 0.07733 | +43.3% | +nan to +nan | no |
| CPU used (cores), mean | 1.295 | 1.161 | -10.3% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0115 | +0.0115 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 1.295 | 1.172 | -9.5% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.2 | 406.4 | -18.3% | +nan to +nan | no |
| HPA replicas, mean | 1.927 | 2.135 | +10.8% | +nan to +nan | no |
| pods started | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 37.21 | 37.11 | -0.3% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |
| batch: queue finished (s) | 729 | 729 | +0.0% | +nan to +nan | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | -66.7% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.04167 | -50.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0 | -100.0% | +nan to +nan | no |
| queue: job turnaround, submitted to done, mean (s) | 32.17 | 31.21 | -3.0% | +nan to +nan | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*