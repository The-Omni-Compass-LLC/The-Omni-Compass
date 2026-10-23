# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.7 | 160.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 160.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 74.59 | 75.32 |
| response time (ms), 95th percentile | 116.3 | 116.5 |
| response time (ms), 99th percentile | 136 | 135.2 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02667 |
| utilisation (used / allocatable) | 0.04629 | 0.04647 |
| CPU used (cores), mean | 1.111 | 1.115 |
| Omni's own CPU (cores), mean | 0 | 0.03082 |
| CPU used with Omni's own (cores), mean | 1.111 | 1.146 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 587.4 | 584.8 |
| HPA replicas, mean | 2.659 | 2.781 |
| pods started | 1 | 1.5 |
| pod start wait, total (s) | 1.4 | 2 |
| pod start wait, mean (s) | 0.95 | 1.4 |
| host CPU busy, the real machine under kind (%) | 34.11 | 35.3 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.599e-16 to +1.115e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.513 | +0.1% | -0.009072 to +0.01107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.7 | 160.9 | +0.1% | -0.9433 to +1.231 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.7 | 160.9 | +0.1% | -0.9433 to +1.231 | no |
| response time (ms), mean | 74.59 | 75.32 | +1.0% | -1.338 to +2.792 | no |
| response time (ms), 95th percentile | 116.3 | 116.5 | +0.2% | -4.424 to +4.792 | no |
| response time (ms), 99th percentile | 136 | 135.2 | -0.6% | -9.009 to +7.28 | no |
| time over the response line (% of samples) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4 (native is 0) | +4 to +4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.02667 | -50.0% | -0.1349 to +0.08161 | no |
| utilisation (used / allocatable) | 0.04629 | 0.04647 | +0.4% | -0.0003232 to +0.0006746 | no |
| CPU used (cores), mean | 1.111 | 1.115 | +0.4% | -0.007756 to +0.01619 | no |
| Omni's own CPU (cores), mean | 0 | 0.03082 | +0.0308 (native is 0) | +0.02563 to +0.03601 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.111 | 1.146 | +3.2% | +0.02263 to +0.04745 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 587.4 | 584.8 | -0.5% | -8.656 to +3.369 | no |
| HPA replicas, mean | 2.659 | 2.781 | +4.6% | -0.02577 to +0.2691 | no |
| pods started | 1 | 1.5 | +50.0% | -0.1079 to +1.108 | no |
| pod start wait, total (s) | 1.4 | 2 | +42.9% | -0.3048 to +1.505 | no |
| pod start wait, mean (s) | 0.95 | 1.4 | +47.4% | -0.2543 to +1.154 | no |
| host CPU busy, the real machine under kind (%) | 34.11 | 35.3 | +3.5% | +0.6478 to +1.726 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*