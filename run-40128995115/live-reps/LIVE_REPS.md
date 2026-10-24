# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.1 | 170.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.1 | 170.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 415.3 | 358.5 |
| response time (ms), 95th percentile | 1622 | 1527 |
| response time (ms), 99th percentile | 4435 | 4269 |
| time over the response line (% of samples) | 18.37 | 16.95 |
| failed requests (%) | 2.658 | 2.34 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8517 | 1.065 |
| utilisation (used / allocatable) | 0.08722 | 0.08674 |
| CPU used (cores), mean | 2.093 | 2.082 |
| Omni's own CPU (cores), mean | 0 | 0.0111 |
| CPU used with Omni's own (cores), mean | 2.093 | 2.093 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 340.6 | 342.4 |
| HPA replicas, mean | 14.6 | 15.02 |
| pods started | 5.9 | 5.9 |
| pod start wait, total (s) | 9.6 | 11.6 |
| pod start wait, mean (s) | 1.647 | 1.959 |
| host CPU busy, the real machine under kind (%) | 60.54 | 61.03 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 329.2 | 355.6 |
| second app: response time (ms), 99th percentile | 1184 | 1107 |
| second app: time over the response line (% of samples) | 11.81 | 12.26 |
| second app: failed requests (%) | 9.667 | 9.76 |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.516 | +0.2% | +0.0002 to +0.0048 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 170.1 | 170.3 | +0.1% | −0.3904 to +0.7243 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.1 | 170.3 | +0.1% | −0.3904 to +0.7243 | no |
| response time (ms), mean | 415.3 | 358.5 | −13.7% | −109.8480 to −3.5923 | yes: GAIN |
| response time (ms), 95th percentile | 1622 | 1527 | −5.8% | −422.0253 to +232.7553 | no |
| response time (ms), 99th percentile | 4435 | 4269 | −3.8% | −679.0838 to +346.3582 | no |
| time over the response line (% of samples) | 18.37 | 16.95 | −7.7% | −3.2347 to +0.3905 | no |
| failed requests (%) | 2.658 | 2.34 | −12.0% | −1.1967 to +0.5605 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.7 | 6.3 | −6.0% | −0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 44.2 | +44.200 (native is 0) | +36.1580 to +52.2420 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8517 | 1.065 | +25.0% | −0.6594 to +1.0861 | no |
| utilisation (used / allocatable) | 0.08722 | 0.08674 | −0.6% | −0.0023 to +0.0014 | no |
| CPU used (cores), mean | 2.093 | 2.082 | −0.6% | −0.0558 to +0.0324 | no |
| Omni's own CPU (cores), mean | 0 | 0.0111 | +0.011 (native is 0) | +0.0098 to +0.0124 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.093 | 2.093 | −0.0% | −0.0446 to +0.0435 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 340.6 | 342.4 | +0.5% | −8.3644 to +11.8583 | no |
| HPA replicas, mean | 14.6 | 15.02 | +2.9% | +0.0014 to +0.8322 | yes: power given |
| pods started | 5.9 | 5.9 | ±0.0% | −0.7540 to +0.7540 | no |
| pod start wait, total (s) | 9.6 | 11.6 | +20.8% | −0.4779 to +4.4779 | no |
| pod start wait, mean (s) | 1.647 | 1.959 | +19.0% | −0.1123 to +0.7366 | no |
| host CPU busy, the real machine under kind (%) | 60.54 | 61.03 | +0.8% | −0.0001 to +0.9654 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 329.2 | 355.6 | +8.0% | −20.9923 to +73.8653 | no |
| second app: response time (ms), 99th percentile | 1184 | 1107 | −6.6% | −734.9335 to +579.6361 | no |
| second app: time over the response line (% of samples) | 11.81 | 12.26 | +3.8% | −0.1230 to +1.0284 | no |
| second app: failed requests (%) | 9.667 | 9.76 | +1.0% | −0.4884 to +0.6751 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*