# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 162.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 162.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 228.6 | 99.17 |
| response time (ms), 95th percentile | 532.4 | 151.3 |
| response time (ms), 99th percentile | 735.2 | 305 |
| time over the response line (% of samples) | 6.086 | 0.2078 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 60 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.02667 |
| utilisation (used / allocatable) | 0.03158 | 0.05043 |
| CPU used (cores), mean | 0.758 | 1.21 |
| Omni's own CPU (cores), mean | 0 | 0.03773 |
| CPU used with Omni's own (cores), mean | 0.758 | 1.248 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825 | 530.8 |
| HPA replicas, mean | 3.018 | 2.518 |
| pods started | 2.8 | 2.5 |
| pod start wait, total (s) | 4.2 | 4 |
| pod start wait, mean (s) | 1.533 | 1.617 |
| host CPU busy, the real machine under kind (%) | 24.23 | 38.38 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.519 | +0.1% | -0.008274 to +0.01127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158 | 162.5 | +2.8% | +3.533 to +5.448 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158 | 162.5 | +2.8% | +3.533 to +5.448 | yes: power given |
| response time (ms), mean | 228.6 | 99.17 | -56.6% | -137.1 to -121.7 | yes: GAIN |
| response time (ms), 95th percentile | 532.4 | 151.3 | -71.6% | -410.8 to -351.6 | yes: GAIN |
| response time (ms), 99th percentile | 735.2 | 305 | -58.5% | -485.2 to -375.3 | yes: GAIN |
| time over the response line (% of samples) | 6.086 | 0.2078 | -96.6% | -6.961 to -4.796 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.5 | 0 | -100.0% | -7.979 to -5.021 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.9 | +13.9 (native is 0) | +9.642 to +18.16 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.02667 | -80.0% | -0.24 to +0.02671 | no |
| utilisation (used / allocatable) | 0.03158 | 0.05043 | +59.7% | +0.01754 to +0.02015 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.758 | 1.21 | +59.7% | +0.421 to +0.4837 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03773 | +0.0377 (native is 0) | +0.03458 to +0.04088 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.758 | 1.248 | +64.6% | +0.4591 to +0.521 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 825 | 530.8 | -35.7% | -314.8 to -273.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.018 | 2.518 | -16.6% | -0.7374 to -0.2645 | yes: GAIN |
| pods started | 2.8 | 2.5 | -10.7% | -0.8889 to +0.2889 | no |
| pod start wait, total (s) | 4.2 | 4 | -4.8% | -0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 1.533 | 1.617 | +5.4% | -0.2989 to +0.4655 | no |
| host CPU busy, the real machine under kind (%) | 24.23 | 38.38 | +58.4% | +13.41 to +14.89 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*