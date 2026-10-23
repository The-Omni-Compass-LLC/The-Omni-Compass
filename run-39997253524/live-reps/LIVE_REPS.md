# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.666 |
| node-hours | 2.516 | 2.372 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 262.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 513.9 | 460.9 |
| response time (ms), 95th percentile | 3087 | 3080 |
| response time (ms), 99th percentile | 4563 | 4570 |
| time over the response line (% of samples) | 15.65 | 15.5 |
| failed requests (%) | 0.0107 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.5 | 187.9 |
| utilisation (used / allocatable) | 0.06135 | 0.06553 |
| CPU used (cores), mean | 1.472 | 1.485 |
| Omni's own CPU (cores), mean | 0 | 0.01675 |
| CPU used with Omni's own (cores), mean | 1.472 | 1.502 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 431.5 |
| HPA replicas, mean | 2.162 | 2.314 |
| pods started | 0 | 0.8 |
| pod start wait, total (s) | 0 | 2.1 |
| pod start wait, mean (s) | 0 | 1.45 |
| host CPU busy, the real machine under kind (%) | 42.42 | 43.21 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 577.2 | 581.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.475 |

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
| worker nodes in service, mean | 6 | 5.666 | -5.6% | -0.6692 to +0.001462 | no |
| node-hours | 2.516 | 2.372 | -5.7% | -0.2871 to -0.00218 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 272.9 | -0.1% | -1.564 to +0.7811 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 262.4 | -4.0% | -21.87 to +0.1203 | no |
| response time (ms), mean | 513.9 | 460.9 | -10.3% | -68.76 to -37.17 | yes: GAIN |
| response time (ms), 95th percentile | 3087 | 3080 | -0.2% | -139.6 to +126.4 | no |
| response time (ms), 99th percentile | 4563 | 4570 | +0.2% | -136.6 to +150.7 | no |
| time over the response line (% of samples) | 15.65 | 15.5 | -1.0% | -0.7068 to +0.3969 | no |
| failed requests (%) | 0.0107 | 0 | -100.0% | -0.03489 to +0.0135 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.1 | +2.0% | -0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 | +12.3 (native is 0) | +11.54 to +13.06 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.5 | 187.9 | -0.9% | -5.931 to +2.607 | no |
| utilisation (used / allocatable) | 0.06135 | 0.06553 | +6.8% | +0.001237 to +0.007122 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.472 | 1.485 | +0.9% | -0.02637 to +0.05216 | no |
| Omni's own CPU (cores), mean | 0 | 0.01675 | +0.0168 (native is 0) | +0.01497 to +0.01853 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.472 | 1.502 | +2.0% | -0.009332 to +0.06862 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.2 | 431.5 | -4.8% | -36.68 to -6.668 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.162 | 2.314 | +7.0% | -0.08733 to +0.3913 | no |
| pods started | 0 | 0.8 | +0.8 (native is 0) | +0.3476 to +1.252 | yes: power given |
| pod start wait, total (s) | 0 | 2.1 | +2.1 (native is 0) | -0.7101 to +4.91 | no |
| pod start wait, mean (s) | 0 | 1.45 | +1.45 (native is 0) | +0.03487 to +2.865 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.42 | 43.21 | +1.9% | +0.4151 to +1.16 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 577.2 | 581.8 | +0.8% | -1.481 to +10.68 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.475 | -8.7% | -1.044 to -0.005886 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*