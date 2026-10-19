# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.5 | 171 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.5 | 171 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 429.4 | 350.7 |
| response time (ms), 95th percentile | 1793 | 1565 |
| response time (ms), 99th percentile | 4272 | 4021 |
| time over the response line (% of samples) | 20 | 17.42 |
| failed requests (%) | 2.277 | 2.594 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7717 | 1.192 |
| utilisation (used / allocatable) | 0.08898 | 0.0888 |
| CPU used (cores), mean | 2.135 | 2.131 |
| Omni's own CPU (cores), mean | 0 | 0.01011 |
| CPU used with Omni's own (cores), mean | 2.135 | 2.141 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 330.6 | 330.4 |
| HPA replicas, mean | 14.72 | 15.08 |
| pods started | 5.6 | 4.3 |
| pod start wait, total (s) | 9.2 | 7.2 |
| pod start wait, mean (s) | 1.648 | 1.787 |
| host CPU busy, the real machine under kind (%) | 61.9 | 62.05 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 288.2 | 282 |
| second app: response time (ms), 99th percentile | 2475 | 2148 |
| second app: time over the response line (% of samples) | 12.51 | 12.29 |
| second app: failed requests (%) | 10.12 | 9.982 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.842e-18 to +1.069e-15 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.518 | +0.3% | +0.003008 to +0.005992 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 170.5 | 171 | +0.3% | +0.1808 to +0.7946 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.5 | 171 | +0.3% | +0.1808 to +0.7946 | yes: power given |
| response time (ms), mean | 429.4 | 350.7 | -18.3% | -131.1 to -26.33 | yes: GAIN |
| response time (ms), 95th percentile | 1793 | 1565 | -12.7% | -594.9 to +138.7 | no |
| response time (ms), 99th percentile | 4272 | 4021 | -5.9% | -847.5 to +345.1 | no |
| time over the response line (% of samples) | 20 | 17.42 | -12.9% | -4.573 to -0.5716 | yes: GAIN |
| failed requests (%) | 2.277 | 2.594 | +13.9% | -0.2218 to +0.8553 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 7.1 | -7.8% | -1.369 to +0.1689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.4 | +33.4 (native is 0) | +30.96 to +35.84 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7717 | 1.192 | +54.4% | -0.3925 to +1.232 | no |
| utilisation (used / allocatable) | 0.08898 | 0.0888 | -0.2% | -0.001256 to +0.0009042 | no |
| CPU used (cores), mean | 2.135 | 2.131 | -0.2% | -0.03015 to +0.0217 | no |
| Omni's own CPU (cores), mean | 0 | 0.01011 | +0.0101 (native is 0) | +0.008521 to +0.0117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.135 | 2.141 | +0.3% | -0.01925 to +0.03102 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 330.6 | 330.4 | -0.1% | -4.845 to +4.416 | no |
| HPA replicas, mean | 14.72 | 15.08 | +2.4% | +0.1039 to +0.6069 | yes: power given |
| pods started | 5.6 | 4.3 | -23.2% | -2.651 to +0.0509 | no |
| pod start wait, total (s) | 9.2 | 7.2 | -21.7% | -5.053 to +1.053 | no |
| pod start wait, mean (s) | 1.648 | 1.787 | +8.5% | -0.4415 to +0.72 | no |
| host CPU busy, the real machine under kind (%) | 61.9 | 62.05 | +0.2% | -0.3933 to +0.7027 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 288.2 | 282 | -2.2% | -58.45 to +45.97 | no |
| second app: response time (ms), 99th percentile | 2475 | 2148 | -13.2% | -1671 to +1016 | no |
| second app: time over the response line (% of samples) | 12.51 | 12.29 | -1.7% | -0.7628 to +0.325 | no |
| second app: failed requests (%) | 10.12 | 9.982 | -1.4% | -0.5576 to +0.2817 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*