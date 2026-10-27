# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.993 | 5.983 |
| node-hours | 1.51 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.2 | 161.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.1 | 161.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 79.32 | 79.42 |
| response time (ms), 95th percentile | 116.6 | 115.4 |
| response time (ms), 99th percentile | 133 | 130.7 |
| time over the response line (% of samples) | 0 | 0.01227 |
| failed requests (%) | 0 | 0.01227 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.05333 |
| utilisation (used / allocatable) | 0.04746 | 0.04824 |
| CPU used (cores), mean | 1.138 | 1.154 |
| Omni's own CPU (cores), mean | 0 | 0.00855 |
| CPU used with Omni's own (cores), mean | 1.138 | 1.163 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 569.1 | 561.7 |
| HPA replicas, mean | 2.657 | 2.784 |
| pods started | 1.3 | 1.6 |
| pod start wait, total (s) | 1.6 | 2.5 |
| pod start wait, mean (s) | 0.9333 | 1.5 |
| host CPU busy, the real machine under kind (%) | 35.2 | 35.82 |
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

Omni-Compass stayed native in 10 of 10 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.993 | 5.983 | −0.2% | −0.0301 to +0.0093 | no |
| node-hours | 1.51 | 1.509 | −0.1% | −0.0080 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.2 | 161.6 | +0.3% | −0.4931 to +1.4131 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.1 | 161.3 | +0.2% | −0.4901 to +1.0143 | no |
| response time (ms), mean | 79.32 | 79.42 | +0.1% | −0.7084 to +0.9045 | no |
| response time (ms), 95th percentile | 116.6 | 115.4 | −1.0% | −3.5871 to +1.2121 | no |
| response time (ms), 99th percentile | 133 | 130.7 | −1.7% | −8.1428 to +3.6082 | no |
| time over the response line (% of samples) | 0 | 0.01227 | +0.012 (native is 0) | −0.0155 to +0.0400 | no |
| failed requests (%) | 0 | 0.01227 | +0.012 (native is 0) | −0.0155 to +0.0400 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05167 | 0.05333 | +3.2% | −0.1236 to +0.1269 | no |
| utilisation (used / allocatable) | 0.04746 | 0.04824 | +1.6% | +0.0002 to +0.0014 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.138 | 1.154 | +1.5% | +0.0038 to +0.0299 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00855 | +0.009 (native is 0) | +0.0073 to +0.0098 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.138 | 1.163 | +2.2% | +0.0119 to +0.0390 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 569.1 | 561.7 | −1.3% | −12.3090 to −2.4209 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.657 | 2.784 | +4.8% | −0.0463 to +0.3005 | no |
| pods started | 1.3 | 1.6 | +23.1% | −0.2889 to +0.8889 | no |
| pod start wait, total (s) | 1.6 | 2.5 | +56.2% | −0.3818 to +2.1818 | no |
| pod start wait, mean (s) | 0.9333 | 1.5 | +60.7% | +0.1606 to +0.9727 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 35.2 | 35.82 | +1.8% | +0.1671 to +1.0691 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*