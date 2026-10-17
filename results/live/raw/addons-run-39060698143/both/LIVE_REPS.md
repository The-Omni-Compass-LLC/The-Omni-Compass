# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 130.8 | 81.72 |
| response time (ms), 95th percentile | 275.5 | 125.3 |
| response time (ms), 99th percentile | 403.7 | 157.5 |
| time over the response line (% of samples) | 0.5424 | 0.01227 |
| failed requests (%) | 0 | 0.01227 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.1583 |
| utilisation (used / allocatable) | 0.03656 | 0.04744 |
| CPU used (cores), mean | 0.8774 | 1.138 |
| Omni's own CPU (cores), mean | 0 | 0.01183 |
| CPU used with Omni's own (cores), mean | 0.8774 | 1.15 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 718.2 | 569.8 |
| HPA replicas, mean | 8.835 | 9.129 |
| pods started | 5.1 | 4.5 |
| pod start wait, total (s) | 14.8 | 13 |
| pod start wait, mean (s) | 2.847 | 2.662 |
| host CPU busy, the real machine under kind (%) | 27.25 | 35.04 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.733e-16 to +1.062e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.513 | -0.5% | -0.01309 to -0.001244 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 161 | +1.1% | +0.7343 to +2.737 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 161 | +1.1% | +0.7343 to +2.737 | yes: power given |
| response time (ms), mean | 130.8 | 81.72 | -37.5% | -66.06 to -32.12 | yes: GAIN |
| response time (ms), 95th percentile | 275.5 | 125.3 | -54.5% | -179.8 to -120.5 | yes: GAIN |
| response time (ms), 99th percentile | 403.7 | 157.5 | -61.0% | -302.1 to -190.4 | yes: GAIN |
| time over the response line (% of samples) | 0.5424 | 0.01227 | -97.7% | -0.9294 to -0.1308 | yes: GAIN |
| failed requests (%) | 0 | 0.01227 | +0.0123 (native is 0) | -0.01548 to +0.04002 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0 | -100.0% | -1.108 to +0.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.2 | +17.2 (native is 0) | +15.99 to +18.41 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.1583 | -39.9% | -0.3094 to +0.09942 | no |
| utilisation (used / allocatable) | 0.03656 | 0.04744 | +29.8% | +0.007749 to +0.01401 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8774 | 1.138 | +29.8% | +0.186 to +0.3361 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01183 | +0.0118 (native is 0) | +0.01009 to +0.01357 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8774 | 1.15 | +31.1% | +0.1963 to +0.3495 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 718.2 | 569.8 | -20.7% | -179 to -117.9 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.835 | 9.129 | +3.3% | +0.119 to +0.4703 | yes: power given |
| pods started | 5.1 | 4.5 | -11.8% | -1.203 to +0.0032 | no |
| pod start wait, total (s) | 14.8 | 13 | -12.2% | -7.84 to +4.24 | no |
| pod start wait, mean (s) | 2.847 | 2.662 | -6.5% | -1.368 to +0.9977 | no |
| host CPU busy, the real machine under kind (%) | 27.25 | 35.04 | +28.6% | +5.597 to +9.995 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*