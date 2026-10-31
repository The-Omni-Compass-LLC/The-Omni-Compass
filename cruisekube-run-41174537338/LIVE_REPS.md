# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.972 | 6 |
| node-hours | 1.509 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 162.8 | 161.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.3 | 161.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 91.41 | 92.21 |
| response time (ms), 95th percentile | 143.5 | 144.5 |
| response time (ms), 99th percentile | 164.2 | 169.1 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.1083 |
| utilisation (used / allocatable) | 0.05148 | 0.05138 |
| CPU used (cores), mean | 1.229 | 1.233 |
| Omni's own CPU (cores), mean | 0 | 0.01104 |
| CPU used with Omni's own (cores), mean | 1.229 | 1.244 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 527.8 | 526 |
| HPA replicas, mean | 2.894 | 2.893 |
| pods started | 1.6 | 1.4 |
| pod start wait, total (s) | 2.1 | 2 |
| pod start wait, mean (s) | 1.283 | 1.25 |
| host CPU busy, the real machine under kind (%) | 38.62 | 39.45 |
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
| worker nodes in service, mean | 5.972 | 6 | +0.5% | −0.0349 to +0.0901 | no |
| node-hours | 1.509 | 1.512 | +0.1% | −0.0146 to +0.0189 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 162.8 | 161.8 | −0.6% | −2.8604 to +0.7569 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.3 | 161.8 | −0.3% | −1.6684 to +0.6150 | no |
| response time (ms), mean | 91.41 | 92.21 | +0.9% | −1.3129 to +2.9158 | no |
| response time (ms), 95th percentile | 143.5 | 144.5 | +0.7% | −1.5318 to +3.4498 | no |
| response time (ms), 99th percentile | 164.2 | 169.1 | +2.9% | −2.7146 to +12.4006 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08167 | 0.1083 | +32.7% | −0.1420 to +0.1954 | no |
| utilisation (used / allocatable) | 0.05148 | 0.05138 | −0.2% | −0.0010 to +0.0008 | no |
| CPU used (cores), mean | 1.229 | 1.233 | +0.3% | −0.0119 to +0.0197 | no |
| Omni's own CPU (cores), mean | 0 | 0.01104 | +0.011 (native is 0) | +0.0100 to +0.0121 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.229 | 1.244 | +1.2% | −0.0009 to +0.0308 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 527.8 | 526 | −0.4% | −7.8130 to +4.0601 | no |
| HPA replicas, mean | 2.894 | 2.893 | −0.0% | −0.1812 to +0.1791 | no |
| pods started | 1.6 | 1.4 | −12.5% | −1.0793 to +0.6793 | no |
| pod start wait, total (s) | 2.1 | 2 | −4.8% | −1.5086 to +1.3086 | no |
| pod start wait, mean (s) | 1.283 | 1.25 | −2.6% | −0.5805 to +0.5139 | no |
| host CPU busy, the real machine under kind (%) | 38.62 | 39.45 | +2.1% | +0.3135 to +1.3370 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*