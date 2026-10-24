# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.7 | 520.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.7 | 520.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 300.6 | 172.9 |
| response time (ms), 95th percentile | 795.8 | 373.4 |
| response time (ms), 99th percentile | 2866 | 1990 |
| time over the response line (% of samples) | 21.52 | 13.59 |
| failed requests (%) | 12.16 | 10.71 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.7 | 24.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.4317 |
| utilisation (used / allocatable) | 0.1087 | 0.1071 |
| CPU used (cores), mean | 2.61 | 2.571 |
| Omni's own CPU (cores), mean | 0 | 0.0093 |
| CPU used with Omni's own (cores), mean | 2.61 | 2.581 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 276.8 | 280.2 |
| HPA replicas, mean | 9.646 | 10.37 |
| pods started | 5.3 | 6.8 |
| pod start wait, total (s) | 7.2 | 10.6 |
| pod start wait, mean (s) | 1.379 | 1.525 |
| host CPU busy, the real machine under kind (%) | 73.07 | 72.31 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.512 | -0.0% | -0.009964 to +0.006631 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.7 | 520.5 | -0.2% | -2.279 to -0.05415 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.7 | 520.5 | -0.2% | -2.279 to -0.05415 | yes: GAIN |
| response time (ms), mean | 300.6 | 172.9 | -42.5% | -161.4 to -94.02 | yes: GAIN |
| response time (ms), 95th percentile | 795.8 | 373.4 | -53.1% | -544.6 to -300.2 | yes: GAIN |
| response time (ms), 99th percentile | 2866 | 1990 | -30.6% | -1617 to -134.3 | yes: GAIN |
| time over the response line (% of samples) | 21.52 | 13.59 | -36.8% | -9.837 to -6.012 | yes: GAIN |
| failed requests (%) | 12.16 | 10.71 | -11.9% | -2.042 to -0.8479 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.7 | 24.7 | -22.1% | -9.106 to -4.894 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.2 | +41.2 (native is 0) | +32.18 to +50.22 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3767 | 0.4317 | +14.6% | -0.1261 to +0.2361 | no |
| utilisation (used / allocatable) | 0.1087 | 0.1071 | -1.5% | -0.002396 to -0.0008207 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.61 | 2.571 | -1.5% | -0.05752 to -0.0197 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0093 | +0.0093 (native is 0) | +0.008443 to +0.01016 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.61 | 2.581 | -1.1% | -0.04777 to -0.01084 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 276.8 | 280.2 | +1.2% | +1.938 to +4.762 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.646 | 10.37 | +7.5% | -0.009554 to +1.458 | no |
| pods started | 5.3 | 6.8 | +28.3% | -0.7683 to +3.768 | no |
| pod start wait, total (s) | 7.2 | 10.6 | +47.2% | -0.8812 to +7.681 | no |
| pod start wait, mean (s) | 1.379 | 1.525 | +10.6% | -0.06506 to +0.3565 | no |
| host CPU busy, the real machine under kind (%) | 73.07 | 72.31 | -1.0% | -1.159 to -0.3596 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*