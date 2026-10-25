# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.171 |
| node-hours | 2.515 | 2.167 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 245 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 314.9 | 285.7 |
| response time (ms), 95th percentile | 1257 | 1300 |
| response time (ms), 99th percentile | 2018 | 2022 |
| time over the response line (% of samples) | 11.81 | 11.47 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.39 | 15.41 |
| utilisation (used / allocatable) | 0.05611 | 0.06584 |
| CPU used (cores), mean | 1.347 | 1.336 |
| Omni's own CPU (cores), mean | 0 | 0.01784 |
| CPU used with Omni's own (cores), mean | 1.347 | 1.354 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491.9 | 441.3 |
| HPA replicas, mean | 1.994 | 2.254 |
| pods started | 0 | 0.7 |
| pod start wait, total (s) | 0 | 1.1 |
| pod start wait, mean (s) | 0 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.39 | 41.48 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 778.1 | 784 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.637 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.8042 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 86.24 | 93.27 |
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
| worker nodes in service, mean | 6 | 5.171 | −13.8% | −1.6273 to −0.0297 | yes: GAIN |
| node-hours | 2.515 | 2.167 | −13.8% | −0.6798 to −0.0154 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271 | −0.1% | −1.1097 to +0.7338 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 245 | −9.7% | −51.1774 to −1.1611 | yes: GAIN |
| response time (ms), mean | 314.9 | 285.7 | −9.3% | −62.9514 to +4.4414 | no |
| response time (ms), 95th percentile | 1257 | 1300 | +3.5% | −114.9412 to +201.8302 | no |
| response time (ms), 99th percentile | 2018 | 2022 | +0.2% | −279.6443 to +286.7669 | no |
| time over the response line (% of samples) | 11.81 | 11.47 | −2.9% | −1.1755 to +0.4963 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.7 | ±0.0% | −0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.1 | +46.100 (native is 0) | +32.3555 to +59.8445 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.39 | 15.41 | +0.1% | −1.5513 to +1.5846 | no |
| utilisation (used / allocatable) | 0.05611 | 0.06584 | +17.3% | +0.0002 to +0.0193 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.347 | 1.336 | −0.8% | −0.0428 to +0.0222 | no |
| Omni's own CPU (cores), mean | 0 | 0.01784 | +0.018 (native is 0) | +0.0149 to +0.0208 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.347 | 1.354 | +0.6% | −0.0261 to +0.0412 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 491.9 | 441.3 | −10.3% | −102.7836 to +1.7354 | no |
| HPA replicas, mean | 1.994 | 2.254 | +13.0% | +0.0688 to +0.4502 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.2172 to +1.1828 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | +0.1198 to +2.0802 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.1887 to +1.6113 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.39 | 41.48 | +2.7% | +0.5037 to +1.6642 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 778.1 | 784 | +0.8% | −2.4857 to +14.2857 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.637 | −22.7% | −2.6526 to −0.0726 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7958 | 0.8042 | +1.0% | −0.1107 to +0.1274 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1.4 | +16.7% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 86.24 | 93.27 | +8.2% | −1.1063 to +15.1646 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*