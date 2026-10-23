# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.339 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 484.2 | 482.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 484.2 | 482.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 292.1 | 149.9 |
| response time (ms), 95th percentile | 750.4 | 319.7 |
| response time (ms), 99th percentile | 1469 | 746.7 |
| time over the response line (% of samples) | 14.9 | 3.888 |
| failed requests (%) | 1.617 | 1.415 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.5 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.395 | 0.6433 |
| utilisation (used / allocatable) | 0.08222 | 0.07983 |
| CPU used (cores), mean | 1.973 | 1.916 |
| Omni's own CPU (cores), mean | 0 | 0.01029 |
| CPU used with Omni's own (cores), mean | 1.973 | 1.926 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 376.1 | 381.8 |
| HPA replicas, mean | 9.703 | 11.83 |
| pods started | 6.4 | 16.7 |
| pod start wait, total (s) | 10.2 | 30.1 |
| pod start wait, mean (s) | 1.618 | 1.79 |
| host CPU busy, the real machine under kind (%) | 56.72 | 55.57 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.534e-15 to +6.461e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.339 | 4.338 | -0.0% | -0.007802 to +0.006469 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 484.2 | 482.6 | -0.3% | -3.114 to -0.1807 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 484.2 | 482.6 | -0.3% | -3.114 to -0.1807 | yes: GAIN |
| response time (ms), mean | 292.1 | 149.9 | -48.7% | -186.8 to -97.6 | yes: GAIN |
| response time (ms), 95th percentile | 750.4 | 319.7 | -57.4% | -551 to -310.3 | yes: GAIN |
| response time (ms), 99th percentile | 1469 | 746.7 | -49.2% | -961.6 to -482.2 | yes: GAIN |
| time over the response line (% of samples) | 14.9 | 3.888 | -73.9% | -15.44 to -6.577 | yes: GAIN |
| failed requests (%) | 1.617 | 1.415 | -12.5% | -0.3217 to -0.08176 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.5 | 10.5 | -60.4% | -22.26 to -9.737 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.1 | +68.1 (native is 0) | +52.65 to +83.55 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.395 | 0.6433 | +62.9% | -0.1038 to +0.6004 | no |
| utilisation (used / allocatable) | 0.08222 | 0.07983 | -2.9% | -0.0037 to -0.001079 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.973 | 1.916 | -2.9% | -0.08881 to -0.02588 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01029 | +0.0103 (native is 0) | +0.008431 to +0.01215 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.973 | 1.926 | -2.4% | -0.07696 to -0.01715 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 376.1 | 381.8 | +1.5% | -1.198 to +12.61 | no |
| HPA replicas, mean | 9.703 | 11.83 | +21.9% | +0.8198 to +3.432 | yes: power given |
| pods started | 6.4 | 16.7 | +160.9% | +6.088 to +14.51 | yes: power given |
| pod start wait, total (s) | 10.2 | 30.1 | +195.1% | +11.77 to +28.03 | yes: LOSS |
| pod start wait, mean (s) | 1.618 | 1.79 | +10.6% | -0.09687 to +0.4412 | no |
| host CPU busy, the real machine under kind (%) | 56.72 | 55.57 | -2.0% | -1.82 to -0.4922 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*