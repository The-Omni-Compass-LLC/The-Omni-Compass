# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.52 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 192.8 | 80.89 |
| response time (ms), 95th percentile | 451 | 120.9 |
| response time (ms), 99th percentile | 603.7 | 243.8 |
| time over the response line (% of samples) | 4.27 | 0.08537 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05333 |
| utilisation (used / allocatable) | 0.02975 | 0.0458 |
| CPU used (cores), mean | 0.7139 | 1.099 |
| Omni's own CPU (cores), mean | 0 | 0.00899 |
| CPU used with Omni's own (cores), mean | 0.7139 | 1.108 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 876.6 | 590.1 |
| HPA replicas, mean | 2.885 | 2.348 |
| pods started | 3 | 2.2 |
| pod start wait, total (s) | 4.4 | 3.4 |
| pod start wait, mean (s) | 1.467 | 1.533 |
| host CPU busy, the real machine under kind (%) | 22.73 | 33.92 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.073e-17 to +1.432e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.52 | 1.515 | -0.3% | -0.01223 to +0.003559 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.9 | 161.1 | +2.1% | +2.033 to +4.491 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.9 | 161.1 | +2.1% | +2.033 to +4.491 | yes: power given |
| response time (ms), mean | 192.8 | 80.89 | -58.1% | -138.3 to -85.6 | yes: GAIN |
| response time (ms), 95th percentile | 451 | 120.9 | -73.2% | -400.2 to -260 | yes: GAIN |
| response time (ms), 99th percentile | 603.7 | 243.8 | -59.6% | -441.5 to -278.1 | yes: GAIN |
| time over the response line (% of samples) | 4.27 | 0.08537 | -98.0% | -6.824 to -1.547 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 0 | -100.0% | -6.891 to -1.709 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.2 | +4.2 (native is 0) | +3.748 to +4.652 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0.05333 | +100.0% | -0.08161 to +0.1349 | no |
| utilisation (used / allocatable) | 0.02975 | 0.0458 | +54.0% | +0.01308 to +0.01903 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7139 | 1.099 | +54.0% | +0.3138 to +0.4566 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00899 | +0.00899 (native is 0) | +0.007722 to +0.01026 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7139 | 1.108 | +55.2% | +0.3217 to +0.4668 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 876.6 | 590.1 | -32.7% | -305.1 to -268.1 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.885 | 2.348 | -18.6% | -0.7058 to -0.3683 | yes: GAIN |
| pods started | 3 | 2.2 | -26.7% | -1.364 to -0.2358 | yes: GAIN |
| pod start wait, total (s) | 4.4 | 3.4 | -22.7% | -2.066 to +0.06632 | no |
| pod start wait, mean (s) | 1.467 | 1.533 | +4.5% | -0.2264 to +0.3598 | no |
| host CPU busy, the real machine under kind (%) | 22.73 | 33.92 | +49.3% | +9.094 to +13.3 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*