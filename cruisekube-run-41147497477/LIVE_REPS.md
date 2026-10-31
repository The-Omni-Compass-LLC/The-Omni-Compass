# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.996 | 5.634 |
| node-hours | 1.513 | 1.421 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.6 | 155.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 154.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 81.77 | 82.56 |
| response time (ms), 95th percentile | 126 | 126.2 |
| response time (ms), 99th percentile | 143 | 143 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.3333 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08889 | 0.02963 |
| utilisation (used / allocatable) | 0.04856 | 0.05451 |
| CPU used (cores), mean | 1.164 | 1.155 |
| Omni's own CPU (cores), mean | 0 | 0.01094 |
| CPU used with Omni's own (cores), mean | 1.164 | 1.166 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 555.7 | 537.6 |
| HPA replicas, mean | 2.717 | 2.765 |
| pods started | 1.111 | 1.333 |
| pod start wait, total (s) | 1.333 | 2.111 |
| pod start wait, mean (s) | 0.963 | 1.5 |
| host CPU busy, the real machine under kind (%) | 36.68 | 36.99 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

Omni-Compass stayed native in 8 of 9 repetitions (repetitions 1, 2, 3, 4, 5, 6, 7, 8): its governor decided at every step, each decision in the audit with its reasons, and made no write; those repetitions count as they ran.

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.996 | 5.634 | −6.0% | −1.2088 to +0.4837 | no |
| node-hours | 1.513 | 1.421 | −6.1% | −0.3040 to +0.1189 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.6 | 155.1 | −4.0% | −20.4965 to +7.6474 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 154.5 | −4.3% | −22.5160 to +8.5559 | no |
| response time (ms), mean | 81.77 | 82.56 | +1.0% | −1.4260 to +3.0003 | no |
| response time (ms), 95th percentile | 126 | 126.2 | +0.2% | −4.5035 to +4.9680 | no |
| response time (ms), 99th percentile | 143 | 143 | −0.0% | −9.2936 to +9.2825 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0.3333 | +0.333 (native is 0) | −0.4353 to +1.1020 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08889 | 0.02963 | −66.7% | −0.1959 to +0.0774 | no |
| utilisation (used / allocatable) | 0.04856 | 0.05451 | +12.3% | −0.0080 to +0.0200 | no |
| CPU used (cores), mean | 1.164 | 1.155 | −0.8% | −0.0365 to +0.0183 | no |
| Omni's own CPU (cores), mean | 0 | 0.01094 | +0.011 (native is 0) | +0.0081 to +0.0138 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.164 | 1.166 | +0.2% | −0.0247 to +0.0283 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 555.7 | 537.6 | −3.3% | −67.1828 to +30.9649 | no |
| HPA replicas, mean | 2.717 | 2.765 | +1.7% | −0.1809 to +0.2759 | no |
| pods started | 1.111 | 1.333 | +20.0% | −0.4183 to +0.8628 | no |
| pod start wait, total (s) | 1.333 | 2.111 | +58.3% | −0.8427 to +2.3983 | no |
| pod start wait, mean (s) | 0.963 | 1.5 | +55.8% | −0.2752 to +1.3492 | no |
| host CPU busy, the real machine under kind (%) | 36.68 | 36.99 | +0.8% | −0.3137 to +0.9280 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*