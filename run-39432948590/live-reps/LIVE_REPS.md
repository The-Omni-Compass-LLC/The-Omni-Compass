# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 169.9 | 170.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.9 | 170.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 409 | 359.7 |
| response time (ms), 95th percentile | 1640 | 1583 |
| response time (ms), 99th percentile | 4179 | 4306 |
| time over the response line (% of samples) | 17.67 | 16.24 |
| failed requests (%) | 1.202 | 1.392 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.213 | 1.188 |
| utilisation (used / allocatable) | 0.08751 | 0.08815 |
| CPU used (cores), mean | 2.1 | 2.116 |
| Omni's own CPU (cores), mean | 0 | 0.01058 |
| CPU used with Omni's own (cores), mean | 2.1 | 2.126 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 333.2 | 328.9 |
| HPA replicas, mean | 14.77 | 14.77 |
| pods started | 5.7 | 5.3 |
| pod start wait, total (s) | 9.1 | 8.7 |
| pod start wait, mean (s) | 1.58 | 1.707 |
| host CPU busy, the real machine under kind (%) | 60.75 | 60.92 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 335.4 | 368.9 |
| second app: response time (ms), 99th percentile | 2298 | 2334 |
| second app: time over the response line (% of samples) | 11.96 | 12.41 |
| second app: failed requests (%) | 8.97 | 9.032 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.115e-15 to +7.599e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.511 | 1.512 | +0.1% | -0.006749 to +0.009415 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 169.9 | 170.1 | +0.2% | -0.7696 to +1.288 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.9 | 170.1 | +0.2% | -0.7696 to +1.288 | no |
| response time (ms), mean | 409 | 359.7 | -12.1% | -92.47 to -6.149 | yes: GAIN |
| response time (ms), 95th percentile | 1640 | 1583 | -3.4% | -286.3 to +173.2 | no |
| response time (ms), 99th percentile | 4179 | 4306 | +3.0% | -480.3 to +735.1 | no |
| time over the response line (% of samples) | 17.67 | 16.24 | -8.1% | -2.88 to +0.006416 | no |
| failed requests (%) | 1.202 | 1.392 | +15.9% | -0.1991 to +0.5801 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.9 | +0.0% | -0.4769 to +0.4769 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33 | +33 (native is 0) | +30.66 to +35.34 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.213 | 1.188 | -2.1% | -0.7593 to +0.7093 | no |
| utilisation (used / allocatable) | 0.08751 | 0.08815 | +0.7% | -0.0009981 to +0.002276 | no |
| CPU used (cores), mean | 2.1 | 2.116 | +0.7% | -0.02395 to +0.05462 | no |
| Omni's own CPU (cores), mean | 0 | 0.01058 | +0.0106 (native is 0) | +0.009205 to +0.01196 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.1 | 2.126 | +1.2% | -0.01248 to +0.0643 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 333.2 | 328.9 | -1.3% | -10.61 to +1.93 | no |
| HPA replicas, mean | 14.77 | 14.77 | +0.0% | -0.3064 to +0.3098 | no |
| pods started | 5.7 | 5.3 | -7.0% | -1.366 to +0.5656 | no |
| pod start wait, total (s) | 9.1 | 8.7 | -4.4% | -2.429 to +1.629 | no |
| pod start wait, mean (s) | 1.58 | 1.707 | +8.1% | -0.2029 to +0.4582 | no |
| host CPU busy, the real machine under kind (%) | 60.75 | 60.92 | +0.3% | -0.4936 to +0.8261 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 335.4 | 368.9 | +10.0% | -17.37 to +84.37 | no |
| second app: response time (ms), 99th percentile | 2298 | 2334 | +1.6% | -948.9 to +1022 | no |
| second app: time over the response line (% of samples) | 11.96 | 12.41 | +3.7% | -0.5586 to +1.443 | no |
| second app: failed requests (%) | 8.97 | 9.032 | +0.7% | -0.571 to +0.6955 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*