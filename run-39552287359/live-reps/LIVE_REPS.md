# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.331 | 4.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 483.8 | 482.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.8 | 482.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 294.4 | 147.6 |
| response time (ms), 95th percentile | 758.3 | 317.3 |
| response time (ms), 99th percentile | 1406 | 799.4 |
| time over the response line (% of samples) | 15.05 | 3.677 |
| failed requests (%) | 1.532 | 1.26 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.6 | 9.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6133 | 0.9 |
| utilisation (used / allocatable) | 0.0829 | 0.08038 |
| CPU used (cores), mean | 1.99 | 1.929 |
| Omni's own CPU (cores), mean | 0 | 0.01081 |
| CPU used with Omni's own (cores), mean | 1.99 | 1.94 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 363.1 | 371.6 |
| HPA replicas, mean | 9.774 | 11.44 |
| pods started | 5.9 | 17 |
| pod start wait, total (s) | 8.4 | 29.4 |
| pod start wait, mean (s) | 1.46 | 1.679 |
| host CPU busy, the real machine under kind (%) | 57.7 | 56.5 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | no |
| node-hours | 4.331 | 4.334 | +0.1% | -0.003722 to +0.009389 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 483.8 | 482.6 | -0.3% | -1.986 to -0.5192 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 483.8 | 482.6 | -0.3% | -1.986 to -0.5192 | yes: GAIN |
| response time (ms), mean | 294.4 | 147.6 | -49.8% | -190.4 to -103.2 | yes: GAIN |
| response time (ms), 95th percentile | 758.3 | 317.3 | -58.2% | -559.4 to -322.5 | yes: GAIN |
| response time (ms), 99th percentile | 1406 | 799.4 | -43.2% | -827.3 to -386.3 | yes: GAIN |
| time over the response line (% of samples) | 15.05 | 3.677 | -75.6% | -16.13 to -6.616 | yes: GAIN |
| failed requests (%) | 1.532 | 1.26 | -17.8% | -0.4225 to -0.1222 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.6 | 9.6 | -62.5% | -22.56 to -9.435 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.9 | +67.9 (native is 0) | +48.48 to +87.32 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6133 | 0.9 | +46.7% | -0.1102 to +0.6835 | no |
| utilisation (used / allocatable) | 0.0829 | 0.08038 | -3.0% | -0.003555 to -0.00148 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.99 | 1.929 | -3.0% | -0.08531 to -0.03551 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01081 | +0.0108 (native is 0) | +0.008843 to +0.01278 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.99 | 1.94 | -2.5% | -0.07315 to -0.02606 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 363.1 | 371.6 | +2.3% | +3.637 to +13.19 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.774 | 11.44 | +17.0% | +0.3487 to +2.98 | yes: power given |
| pods started | 5.9 | 17 | +188.1% | +6.763 to +15.44 | yes: power given |
| pod start wait, total (s) | 8.4 | 29.4 | +250.0% | +11.64 to +30.36 | yes: LOSS |
| pod start wait, mean (s) | 1.46 | 1.679 | +15.0% | -0.08964 to +0.5275 | no |
| host CPU busy, the real machine under kind (%) | 57.7 | 56.5 | -2.1% | -1.946 to -0.4567 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*