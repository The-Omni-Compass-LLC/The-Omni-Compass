# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 151.7 | 79.56 |
| response time (ms), 95th percentile | 321.3 | 126.2 |
| response time (ms), 99th percentile | 465.4 | 182.8 |
| time over the response line (% of samples) | 1.149 | 0.06098 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.02833 |
| utilisation (used / allocatable) | 0.03255 | 0.04704 |
| CPU used (cores), mean | 0.7812 | 1.129 |
| Omni's own CPU (cores), mean | 0 | 0.02995 |
| CPU used with Omni's own (cores), mean | 0.7812 | 1.159 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 800.8 | 572.2 |
| HPA replicas, mean | 9.709 | 13.2 |
| pods started | 2.9 | 6.4 |
| pod start wait, total (s) | 4.3 | 11.9 |
| pod start wait, mean (s) | 1.317 | 1.759 |
| host CPU busy, the real machine under kind (%) | 23.93 | 34.69 |
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
| node-hours | 1.516 | 1.511 | -0.3% | -0.01179 to +0.003127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160.7 | +1.8% | +2.359 to +3.367 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160.7 | +1.8% | +2.359 to +3.367 | yes: power given |
| response time (ms), mean | 151.7 | 79.56 | -47.6% | -91.44 to -52.84 | yes: GAIN |
| response time (ms), 95th percentile | 321.3 | 126.2 | -60.7% | -231.6 to -158.6 | yes: GAIN |
| response time (ms), 99th percentile | 465.4 | 182.8 | -60.7% | -332.6 to -232.6 | yes: GAIN |
| time over the response line (% of samples) | 1.149 | 0.06098 | -94.7% | -1.846 to -0.3305 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.1 | 0.1 | -90.9% | -2.066 to +0.06632 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.1 | +59.1 (native is 0) | +28.19 to +90.01 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.02833 | -45.2% | -0.1322 to +0.08553 | no |
| utilisation (used / allocatable) | 0.03255 | 0.04704 | +44.5% | +0.01129 to +0.0177 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7812 | 1.129 | +44.5% | +0.2709 to +0.4247 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02995 | +0.0299 (native is 0) | +0.02422 to +0.03568 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7812 | 1.159 | +48.4% | +0.2957 to +0.4598 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 800.8 | 572.2 | -28.5% | -259.4 to -197.7 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.709 | 13.2 | +35.9% | +2.454 to +4.521 | yes: power given |
| pods started | 2.9 | 6.4 | +120.7% | +1.645 to +5.355 | yes: power given |
| pod start wait, total (s) | 4.3 | 11.9 | +176.7% | +3.386 to +11.81 | yes: LOSS |
| pod start wait, mean (s) | 1.317 | 1.759 | +33.6% | +0.00217 to +0.8819 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 23.93 | 34.69 | +44.9% | +8.275 to +13.24 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*