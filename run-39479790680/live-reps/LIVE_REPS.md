# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 12 | 12 |
| node-hours | 5.023 | 5.047 |
| energy, parked workers still on at idle power (Wh, declared model) | 531.2 | 526.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 531.2 | 526.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 1440 | 1812 |
| response time (ms), 95th percentile | 4821 | 5983 |
| response time (ms), 99th percentile | 7423 | 7537 |
| time over the response line (% of samples) | 49.35 | 66.45 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20 | 23 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 40.55 | 256.4 |
| utilisation (used / allocatable) | 0.04311 | 0.03193 |
| CPU used (cores), mean | 2.069 | 1.532 |
| Omni's own CPU (cores), mean | 0 | 0.0128 |
| CPU used with Omni's own (cores), mean | 2.069 | 1.545 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 613.2 | 816.5 |
| HPA replicas, mean | 3.92 | 4.054 |
| pods started | 0 | 2 |
| pod start wait, total (s) | 0 | 2 |
| pod start wait, mean (s) | 0 | 1 |
| host CPU busy, the real machine under kind (%) | 68.7 | 76.78 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1191 | 1361 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 |
| queue: job wait, submitted to its first pod running, mean (s) | 56.71 | 13.79 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 317 | 106 |
| queue: job turnaround, submitted to done, mean (s) | 418.8 | 667.2 |
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
| worker nodes in service, mean | 12 | 12 | +0.0% | +nan to +nan | no |
| node-hours | 5.023 | 5.047 | +0.5% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 531.2 | 526.3 | -0.9% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 531.2 | 526.3 | -0.9% | +nan to +nan | no |
| response time (ms), mean | 1440 | 1812 | +25.8% | +nan to +nan | no |
| response time (ms), 95th percentile | 4821 | 5983 | +24.1% | +nan to +nan | no |
| response time (ms), 99th percentile | 7423 | 7537 | +1.5% | +nan to +nan | no |
| time over the response line (% of samples) | 49.35 | 66.45 | +34.6% | +nan to +nan | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20 | 23 | +15.0% | +nan to +nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29 | +29 (native is 0) | +nan to +nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +nan to +nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 40.55 | 256.4 | +532.3% | +nan to +nan | no |
| utilisation (used / allocatable) | 0.04311 | 0.03193 | -25.9% | +nan to +nan | no |
| CPU used (cores), mean | 2.069 | 1.532 | -25.9% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0128 | +0.0128 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 2.069 | 1.545 | -25.3% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 613.2 | 816.5 | +33.2% | +nan to +nan | no |
| HPA replicas, mean | 3.92 | 4.054 | +3.4% | +nan to +nan | no |
| pods started | 0 | 2 | +2 (native is 0) | +nan to +nan | no |
| pod start wait, total (s) | 0 | 2 | +2 (native is 0) | +nan to +nan | no |
| pod start wait, mean (s) | 0 | 1 | +1 (native is 0) | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 68.7 | 76.78 | +11.8% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |
| batch: queue finished (s) | 1191 | 1361 | +14.3% | +nan to +nan | no |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | +0.0% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 56.71 | 13.79 | -75.7% | +nan to +nan | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 317 | 106 | -66.6% | +nan to +nan | no |
| queue: job turnaround, submitted to done, mean (s) | 418.8 | 667.2 | +59.3% | +nan to +nan | no |
| queue: jobs unfinished at the window's end | 0 | 0 | +0 (native is 0) | +nan to +nan | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*