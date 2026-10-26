# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.1 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.1 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 78.24 | 78.08 |
| response time (ms), 95th percentile | 120.7 | 119.8 |
| response time (ms), 99th percentile | 135.1 | 137 |
| time over the response line (% of samples) | 0 | 0.01235 |
| failed requests (%) | 0 | 0.01235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0 |
| utilisation (used / allocatable) | 0.0469 | 0.047 |
| CPU used (cores), mean | 1.126 | 1.128 |
| Omni's own CPU (cores), mean | 0 | 0.00916 |
| CPU used with Omni's own (cores), mean | 1.126 | 1.137 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 577.9 | 579.2 |
| HPA replicas, mean | 2.713 | 2.738 |
| pods started | 1.5 | 1.5 |
| pod start wait, total (s) | 1.8 | 2.5 |
| pod start wait, mean (s) | 1.25 | 1.733 |
| host CPU busy, the real machine under kind (%) | 35.19 | 35.57 |
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
| worker nodes in service, mean | 6 | 6 | =0.0% | −0.0000 to +0.0000 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0095 to +0.0065 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.1 | 161 | −0.1% | −0.8952 to +0.7327 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.1 | 161 | −0.1% | −0.8952 to +0.7327 | no |
| response time (ms), mean | 78.24 | 78.08 | −0.2% | −1.0454 to +0.7403 | no |
| response time (ms), 95th percentile | 120.7 | 119.8 | −0.7% | −2.0566 to +0.3866 | no |
| response time (ms), 99th percentile | 135.1 | 137 | +1.5% | −4.6691 to +8.6093 | no |
| time over the response line (% of samples) | 0 | 0.01235 | +0.012 (native is 0) | −0.0156 to +0.0403 | no |
| failed requests (%) | 0 | 0.01235 | +0.012 (native is 0) | −0.0156 to +0.0403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.02667 | 0 | −100.0% | −0.0870 to +0.0337 | no |
| utilisation (used / allocatable) | 0.0469 | 0.047 | +0.2% | −0.0006 to +0.0008 | no |
| CPU used (cores), mean | 1.126 | 1.128 | +0.2% | −0.0144 to +0.0192 | no |
| Omni's own CPU (cores), mean | 0 | 0.00916 | +0.009 (native is 0) | +0.0078 to +0.0105 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.126 | 1.137 | +1.0% | −0.0062 to +0.0293 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 577.9 | 579.2 | +0.2% | −8.5352 to +11.0167 | no |
| HPA replicas, mean | 2.713 | 2.738 | +0.9% | −0.1256 to +0.1767 | no |
| pods started | 1.5 | 1.5 | ±0.0% | −0.4769 to +0.4769 | no |
| pod start wait, total (s) | 1.8 | 2.5 | +38.9% | −0.1953 to +1.5953 | no |
| pod start wait, mean (s) | 1.25 | 1.733 | +38.7% | −0.2263 to +1.1930 | no |
| host CPU busy, the real machine under kind (%) | 35.19 | 35.57 | +1.1% | −0.1336 to +0.8859 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*