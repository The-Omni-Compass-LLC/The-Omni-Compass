# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.1 | 161.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.1 | 161.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 77.74 | 77.63 |
| response time (ms), 95th percentile | 121.2 | 120.1 |
| response time (ms), 99th percentile | 142 | 138.6 |
| time over the response line (% of samples) | 0 | 0.01235 |
| failed requests (%) | 0 | 0.01235 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.055 |
| utilisation (used / allocatable) | 0.04708 | 0.04694 |
| CPU used (cores), mean | 1.13 | 1.126 |
| Omni's own CPU (cores), mean | 0 | 0.00917 |
| CPU used with Omni's own (cores), mean | 1.13 | 1.136 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 575.4 | 578.3 |
| HPA replicas, mean | 2.833 | 2.622 |
| pods started | 1.3 | 1.2 |
| pod start wait, total (s) | 1.9 | 1.9 |
| pod start wait, mean (s) | 1.25 | 1.5 |
| host CPU busy, the real machine under kind (%) | 34.88 | 35.32 |
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
| node-hours | 1.513 | 1.514 | +0.1% | −0.0095 to +0.0122 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.1 | 161.1 | +0.0% | −1.0660 to +1.2214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.1 | 161.1 | +0.0% | −1.0660 to +1.2214 | no |
| response time (ms), mean | 77.74 | 77.63 | −0.1% | −1.1714 to +0.9514 | no |
| response time (ms), 95th percentile | 121.2 | 120.1 | −0.9% | −5.9376 to +3.6886 | no |
| response time (ms), 99th percentile | 142 | 138.6 | −2.4% | −18.0011 to +11.2271 | no |
| time over the response line (% of samples) | 0 | 0.01235 | +0.012 (native is 0) | −0.0156 to +0.0403 | no |
| failed requests (%) | 0 | 0.01235 | +0.012 (native is 0) | −0.0156 to +0.0403 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1067 | 0.055 | −48.4% | −0.1707 to +0.0673 | no |
| utilisation (used / allocatable) | 0.04708 | 0.04694 | −0.3% | −0.0006 to +0.0003 | no |
| CPU used (cores), mean | 1.13 | 1.126 | −0.3% | −0.0138 to +0.0069 | no |
| Omni's own CPU (cores), mean | 0 | 0.00917 | +0.009 (native is 0) | +0.0077 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.13 | 1.136 | +0.5% | −0.0056 to +0.0170 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 575.4 | 578.3 | +0.5% | −2.8801 to +8.6320 | no |
| HPA replicas, mean | 2.833 | 2.622 | −7.4% | −0.4179 to −0.0028 | yes: GAIN |
| pods started | 1.3 | 1.2 | −7.7% | −0.7263 to +0.5263 | no |
| pod start wait, total (s) | 1.9 | 1.9 | ±0.0% | −1.3060 to +1.3060 | no |
| pod start wait, mean (s) | 1.25 | 1.5 | +20.0% | −0.4084 to +0.9084 | no |
| host CPU busy, the real machine under kind (%) | 34.88 | 35.32 | +1.3% | −0.0143 to +0.8870 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*