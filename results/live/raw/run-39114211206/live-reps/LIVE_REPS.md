# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.519 | 4.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 524.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 524.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 343.4 | 187.1 |
| response time (ms), 95th percentile | 884.3 | 362.6 |
| response time (ms), 99th percentile | 3496 | 2293 |
| time over the response line (% of samples) | 23.98 | 14.83 |
| failed requests (%) | 13.55 | 11.9 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 34.8 | 27.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.3 |
| utilisation (used / allocatable) | 0.1149 | 0.1127 |
| CPU used (cores), mean | 2.758 | 2.705 |
| Omni's own CPU (cores), mean | 0 | 0.00971 |
| CPU used with Omni's own (cores), mean | 2.758 | 2.715 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 256.1 | 260.2 |
| HPA replicas, mean | 9.77 | 10.57 |
| pods started | 4 | 4.9 |
| pod start wait, total (s) | 11.1 | 11.6 |
| pod start wait, mean (s) | 2.477 | 1.683 |
| host CPU busy, the real machine under kind (%) | 77.15 | 76.08 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.246e-16 to +1.102e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.519 | 4.517 | -0.0% | -0.01175 to +0.008085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 524.8 | -0.3% | -2.52 to -0.7261 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 524.8 | -0.3% | -2.52 to -0.7261 | yes: GAIN |
| response time (ms), mean | 343.4 | 187.1 | -45.5% | -180.9 to -131.7 | yes: GAIN |
| response time (ms), 95th percentile | 884.3 | 362.6 | -59.0% | -567.3 to -476 | yes: GAIN |
| response time (ms), 99th percentile | 3496 | 2293 | -34.4% | -2027 to -378.8 | yes: GAIN |
| time over the response line (% of samples) | 23.98 | 14.83 | -38.2% | -10.14 to -8.167 | yes: GAIN |
| failed requests (%) | 13.55 | 11.9 | -12.2% | -2.265 to -1.043 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 34.8 | 27.6 | -20.7% | -9.01 to -5.39 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.6 | +47.6 (native is 0) | +39.44 to +55.76 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.3 | -34.1% | -0.4527 to +0.1427 | no |
| utilisation (used / allocatable) | 0.1149 | 0.1127 | -1.9% | -0.00282 to -0.00157 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.758 | 2.705 | -1.9% | -0.06767 to -0.03768 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00971 | +0.00971 (native is 0) | +0.009031 to +0.01039 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.758 | 2.715 | -1.6% | -0.05759 to -0.02834 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 256.1 | 260.2 | +1.6% | +3.061 to +5.263 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.77 | 10.57 | +8.2% | +0.02729 to +1.573 | yes: power given |
| pods started | 4 | 4.9 | +22.5% | -1.95 to +3.75 | no |
| pod start wait, total (s) | 11.1 | 11.6 | +4.5% | -9.116 to +10.12 | no |
| pod start wait, mean (s) | 2.477 | 1.683 | -32.0% | -1.761 to +0.1735 | no |
| host CPU busy, the real machine under kind (%) | 77.15 | 76.08 | -1.4% | -1.441 to -0.6917 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*