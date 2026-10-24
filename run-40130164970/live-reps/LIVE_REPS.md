# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.332 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 480 | 479.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480 | 479.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 254.4 | 131.3 |
| response time (ms), 95th percentile | 650.8 | 270.2 |
| response time (ms), 99th percentile | 1196 | 619.6 |
| time over the response line (% of samples) | 11.35 | 2.723 |
| failed requests (%) | 1.045 | 0.911 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.8 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.5367 |
| utilisation (used / allocatable) | 0.07679 | 0.07487 |
| CPU used (cores), mean | 1.843 | 1.797 |
| Omni's own CPU (cores), mean | 0 | 0.00931 |
| CPU used with Omni's own (cores), mean | 1.843 | 1.806 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.5 | 394.8 |
| HPA replicas, mean | 9.742 | 11.27 |
| pods started | 6.1 | 14.2 |
| pod start wait, total (s) | 9.8 | 24.8 |
| pod start wait, mean (s) | 1.593 | 1.705 |
| host CPU busy, the real machine under kind (%) | 53.04 | 52.17 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 4.332 | 4.338 | +0.1% | −0.0019 to +0.0132 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480 | 479.4 | −0.1% | −1.7127 to +0.4725 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480 | 479.4 | −0.1% | −1.7127 to +0.4725 | no |
| response time (ms), mean | 254.4 | 131.3 | −48.4% | −161.0000 to −85.1724 | yes: GAIN |
| response time (ms), 95th percentile | 650.8 | 270.2 | −58.5% | −481.3571 to −279.9289 | yes: GAIN |
| response time (ms), 99th percentile | 1196 | 619.6 | −48.2% | −772.1612 to −381.2626 | yes: GAIN |
| time over the response line (% of samples) | 11.35 | 2.723 | −76.0% | −13.0509 to −4.1938 | yes: GAIN |
| failed requests (%) | 1.045 | 0.911 | −12.8% | −0.2594 to −0.0090 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 19.8 | 7.8 | −60.6% | −16.4480 to −7.5520 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.1 | +54.100 (native is 0) | +36.5480 to +71.6520 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4017 | 0.5367 | +33.6% | +0.0005 to +0.2695 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07679 | 0.07487 | −2.5% | −0.0030 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.843 | 1.797 | −2.5% | −0.0708 to −0.0216 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00931 | +0.009 (native is 0) | +0.0076 to +0.0110 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.843 | 1.806 | −2.0% | −0.0612 to −0.0126 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 387.5 | 394.8 | +1.9% | −1.4942 to +16.0108 | no |
| HPA replicas, mean | 9.742 | 11.27 | +15.7% | −0.1468 to +3.2097 | no |
| pods started | 6.1 | 14.2 | +132.8% | +4.1181 to +12.0819 | yes: power given |
| pod start wait, total (s) | 9.8 | 24.8 | +153.1% | +6.0024 to +23.9976 | yes: LOSS |
| pod start wait, mean (s) | 1.593 | 1.705 | +7.1% | −0.1827 to +0.4079 | no |
| host CPU busy, the real machine under kind (%) | 53.04 | 52.17 | −1.6% | −1.5311 to −0.2192 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*