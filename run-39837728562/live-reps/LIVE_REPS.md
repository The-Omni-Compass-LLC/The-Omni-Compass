# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.833 |
| node-hours | 2.514 | 2.025 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 237.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 533 | 482 |
| response time (ms), 95th percentile | 3058 | 3023 |
| response time (ms), 99th percentile | 4425 | 4400 |
| time over the response line (% of samples) | 17.21 | 16.81 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 195.3 | 198.2 |
| utilisation (used / allocatable) | 0.0636 | 0.07917 |
| CPU used (cores), mean | 1.526 | 1.524 |
| Omni's own CPU (cores), mean | 0 | 0.05438 |
| CPU used with Omni's own (cores), mean | 1.526 | 1.578 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.6 | 374.8 |
| HPA replicas, mean | 2.241 | 2.241 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 44.17 | 45.8 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 604.2 | 612.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.074 |

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
| worker nodes in service, mean | 6 | 4.833 | -19.5% | -1.679 to -0.6554 | yes: GAIN |
| node-hours | 2.514 | 2.025 | -19.4% | -0.7027 to -0.2742 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 273.8 | +0.1% | -1.001 to +1.454 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 237.2 | -13.3% | -52.73 to -20.21 | yes: GAIN |
| response time (ms), mean | 533 | 482 | -9.6% | -61.67 to -40.22 | yes: GAIN |
| response time (ms), 95th percentile | 3058 | 3023 | -1.1% | -152.7 to +83.46 | no |
| response time (ms), 99th percentile | 4425 | 4400 | -0.6% | -278.4 to +229.1 | no |
| time over the response line (% of samples) | 17.21 | 16.81 | -2.3% | -0.9604 to +0.1533 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.5 | +2.9% | -0.04553 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.6 | +10.6 (native is 0) | +8.657 to +12.54 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 195.3 | 198.2 | +1.5% | -2.12 to +7.953 | no |
| utilisation (used / allocatable) | 0.0636 | 0.07917 | +24.5% | +0.008756 to +0.02238 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.526 | 1.524 | -0.2% | -0.04724 to +0.04261 | no |
| Omni's own CPU (cores), mean | 0 | 0.05438 | +0.0544 (native is 0) | +0.04662 to +0.06214 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.526 | 1.578 | +3.4% | +0.005031 to +0.0991 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 435.6 | 374.8 | -14.0% | -92.54 to -29.13 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.241 | 2.241 | +0.0% | -0.4213 to +0.4213 | no |
| pods started | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, total (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pod start wait, mean (s) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| host CPU busy, the real machine under kind (%) | 44.17 | 45.8 | +3.7% | +1.036 to +2.226 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 604.2 | 612.8 | +1.4% | +1.566 to +15.63 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.074 | -32.1% | -2.681 to -1.171 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*