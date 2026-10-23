# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.336 | 4.33 |
| energy, parked workers still on at idle power (Wh, declared model) | 487.2 | 484.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 487.2 | 484.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 321.1 | 165.7 |
| response time (ms), 95th percentile | 818.3 | 369.9 |
| response time (ms), 99th percentile | 1611 | 928.9 |
| time over the response line (% of samples) | 16.43 | 4.613 |
| failed requests (%) | 1.638 | 1.37 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29 | 11.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5017 | 0.715 |
| utilisation (used / allocatable) | 0.08733 | 0.08468 |
| CPU used (cores), mean | 2.096 | 2.032 |
| Omni's own CPU (cores), mean | 0 | 0.01069 |
| CPU used with Omni's own (cores), mean | 2.096 | 2.043 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 341.2 | 349.9 |
| HPA replicas, mean | 9.787 | 12.03 |
| pods started | 5.5 | 16.4 |
| pod start wait, total (s) | 9.1 | 30.2 |
| pod start wait, mean (s) | 1.722 | 1.828 |
| host CPU busy, the real machine under kind (%) | 60.23 | 59.18 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.063e-16 to +7.286e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.336 | 4.33 | -0.1% | -0.01603 to +0.00503 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 487.2 | 484.9 | -0.5% | -3.901 to -0.7569 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 487.2 | 484.9 | -0.5% | -3.901 to -0.7569 | yes: GAIN |
| response time (ms), mean | 321.1 | 165.7 | -48.4% | -188.8 to -122 | yes: GAIN |
| response time (ms), 95th percentile | 818.3 | 369.9 | -54.8% | -533.5 to -363.4 | yes: GAIN |
| response time (ms), 99th percentile | 1611 | 928.9 | -42.3% | -869.2 to -494.5 | yes: GAIN |
| time over the response line (% of samples) | 16.43 | 4.613 | -71.9% | -15.26 to -8.379 | yes: GAIN |
| failed requests (%) | 1.638 | 1.37 | -16.4% | -0.4526 to -0.08333 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 29 | 11.9 | -59.0% | -21.74 to -12.46 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 66.6 | +66.6 (native is 0) | +52.63 to +80.57 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5017 | 0.715 | +42.5% | -0.191 to +0.6177 | no |
| utilisation (used / allocatable) | 0.08733 | 0.08468 | -3.0% | -0.003532 to -0.001752 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.096 | 2.032 | -3.0% | -0.08477 to -0.04205 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01069 | +0.0107 (native is 0) | +0.009089 to +0.01229 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.096 | 2.043 | -2.5% | -0.07376 to -0.03167 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 341.2 | 349.9 | +2.6% | +5.094 to +12.39 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.787 | 12.03 | +22.9% | +1.006 to +3.48 | yes: power given |
| pods started | 5.5 | 16.4 | +198.2% | +7.913 to +13.89 | yes: power given |
| pod start wait, total (s) | 9.1 | 30.2 | +231.9% | +15.19 to +27.01 | yes: LOSS |
| pod start wait, mean (s) | 1.722 | 1.828 | +6.2% | -0.2169 to +0.4305 | no |
| host CPU busy, the real machine under kind (%) | 60.23 | 59.18 | -1.7% | -1.643 to -0.4449 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*