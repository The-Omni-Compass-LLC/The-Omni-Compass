# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.023 |
| node-hours | 2.517 | 1.685 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.4 | 268.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.4 | 206.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 152.4 | 116.2 |
| response time (ms), 95th percentile | 320.5 | 309.9 |
| response time (ms), 99th percentile | 503.8 | 512.7 |
| time over the response line (% of samples) | 2.792 | 2.408 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 3.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 10.96 |
| utilisation (used / allocatable) | 0.05135 | 0.07391 |
| CPU used (cores), mean | 1.232 | 1.176 |
| Omni's own CPU (cores), mean | 0 | 0.01704 |
| CPU used with Omni's own (cores), mean | 1.232 | 1.193 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 534.6 | 426.3 |
| HPA replicas, mean | 1.975 | 2.162 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 0.2 | 0.4 |
| pod start wait, mean (s) | 0.2 | 0.4 |
| host CPU busy, the real machine under kind (%) | 36.19 | 37.03 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 740.2 | 741.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 2.794 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5542 | 0.6042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 48.5 | 47.32 |
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
| worker nodes in service, mean | 6 | 4.023 | −33.0% | −2.6692 to −1.2857 | yes: GAIN |
| node-hours | 2.517 | 1.685 | −33.0% | −1.1214 to −0.5419 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.4 | 268.6 | −0.3% | −1.6700 to +0.0023 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.4 | 206.4 | −23.4% | −84.8275 to −41.1653 | yes: GAIN |
| response time (ms), mean | 152.4 | 116.2 | −23.7% | −47.8532 to −24.3769 | yes: GAIN |
| response time (ms), 95th percentile | 320.5 | 309.9 | −3.3% | −52.4868 to +31.3798 | no |
| response time (ms), 99th percentile | 503.8 | 512.7 | +1.8% | −75.5106 to +93.2484 | no |
| time over the response line (% of samples) | 2.792 | 2.408 | −13.8% | −1.5048 to +0.7369 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.6 | 3.2 | +23.1% | −0.5285 to +1.7285 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 53.3 | +53.300 (native is 0) | +23.5212 to +83.0788 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.89 | 10.96 | +0.6% | −1.8294 to +1.9594 | no |
| utilisation (used / allocatable) | 0.05135 | 0.07391 | +43.9% | +0.0137 to +0.0314 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.232 | 1.176 | −4.6% | −0.0864 to −0.0269 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01704 | +0.017 (native is 0) | +0.0137 to +0.0204 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.232 | 1.193 | −3.2% | −0.0713 to −0.0079 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 534.6 | 426.3 | −20.3% | −149.3499 to −67.3058 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.975 | 2.162 | +9.5% | +0.0179 to +0.3560 | yes: power given |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.6793 to +1.0793 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.6793 to +1.0793 | no |
| host CPU busy, the real machine under kind (%) | 36.19 | 37.03 | +2.3% | +0.5914 to +1.0828 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 740.2 | 741.4 | +0.2% | −0.5128 to +2.9128 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.794 | −53.4% | −4.2373 to −2.1756 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5542 | 0.6042 | +9.0% | −0.0292 to +0.1292 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1 | −9.1% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 48.5 | 47.32 | −2.4% | −3.8315 to +1.4648 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*