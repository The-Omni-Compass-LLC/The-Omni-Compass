# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.993 | 6 |
| node-hours | 1.512 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 161.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 84.26 | 85.57 |
| response time (ms), 95th percentile | 131.7 | 132.8 |
| response time (ms), 99th percentile | 152.8 | 158.6 |
| time over the response line (% of samples) | 0 | 0.01227 |
| failed requests (%) | 0 | 0.01227 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.05333 |
| utilisation (used / allocatable) | 0.04913 | 0.04928 |
| CPU used (cores), mean | 1.178 | 1.183 |
| Omni's own CPU (cores), mean | 0 | 0.03421 |
| CPU used with Omni's own (cores), mean | 1.178 | 1.217 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 551.1 | 549.4 |
| HPA replicas, mean | 2.829 | 2.754 |
| pods started | 1.7 | 1.6 |
| pod start wait, total (s) | 2.6 | 2.2 |
| pod start wait, mean (s) | 1.6 | 1.333 |
| host CPU busy, the real machine under kind (%) | 36.49 | 37.78 |
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
| worker nodes in service, mean | 5.993 | 6 | +0.1% | -0.008876 to +0.02294 | no |
| node-hours | 1.512 | 1.512 | +0.0% | -0.007509 to +0.007732 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.7 | 161.4 | -0.2% | -1.272 to +0.757 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 161.4 | -0.1% | -0.9499 to +0.7019 | no |
| response time (ms), mean | 84.26 | 85.57 | +1.5% | +0.02609 to +2.576 | yes: LOSS |
| response time (ms), 95th percentile | 131.7 | 132.8 | +0.9% | -0.6998 to +2.96 | no |
| response time (ms), 99th percentile | 152.8 | 158.6 | +3.8% | -6.589 to +18.1 | no |
| time over the response line (% of samples) | 0 | 0.01227 | +0.0123 (native is 0) | -0.01548 to +0.04002 | no |
| failed requests (%) | 0 | 0.01227 | +0.0123 (native is 0) | -0.01548 to +0.04002 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4 (native is 0) | +4 to +4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.05333 | +0.0% | -0.1272 to +0.1272 | no |
| utilisation (used / allocatable) | 0.04913 | 0.04928 | +0.3% | -0.0008838 to +0.001196 | no |
| CPU used (cores), mean | 1.178 | 1.183 | +0.4% | -0.01812 to +0.02865 | no |
| Omni's own CPU (cores), mean | 0 | 0.03421 | +0.0342 (native is 0) | +0.02988 to +0.03854 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.178 | 1.217 | +3.4% | +0.01465 to +0.06429 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 551.1 | 549.4 | -0.3% | -10.76 to +7.431 | no |
| HPA replicas, mean | 2.829 | 2.754 | -2.6% | -0.368 to +0.218 | no |
| pods started | 1.7 | 1.6 | -5.9% | -1.02 to +0.8204 | no |
| pod start wait, total (s) | 2.6 | 2.2 | -15.4% | -1.715 to +0.9146 | no |
| pod start wait, mean (s) | 1.6 | 1.333 | -16.7% | -0.7308 to +0.1975 | no |
| host CPU busy, the real machine under kind (%) | 36.49 | 37.78 | +3.5% | +0.5579 to +2.019 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*